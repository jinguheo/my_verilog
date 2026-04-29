#!/usr/bin/env python3
"""Normalize NVlabs VerilogEval V2 generation datasets into JSONL.

The upstream repo stores each problem as separate prompt/ref/test files.  This
script converts those files into the JSONL format consumed by
run_generation_verification.py and writes three mode-specific candidate files:
parser_lsp, kg, and graphify.  The emitted candidates are canonical-reference
oracle completions, so they are only a verifier sanity check until replaced by
real model-generated RTL for each mode.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REPO = ROOT / "tools" / "verilog-eval"
DEFAULT_OUT = ROOT / "out" / "verilogeval_generation"
TASK_DIRS = {
    "code-complete-iccad2023": "dataset_code-complete-iccad2023",
    "spec-to-rtl": "dataset_spec-to-rtl",
}
MODES = ("parser_lsp", "kg", "graphify")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace").strip()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def ref_to_top_module(ref: str) -> str:
    converted = re.sub(r"\bmodule\s+RefModule\b", "module TopModule", ref, count=1)
    if "module TopModule" not in converted:
        raise ValueError("reference does not contain module RefModule")
    return converted.strip() + "\n"


def icarus_compatible(ref: str) -> str:
    """Rewrite small SV constructs that current Icarus rejects in oracle refs."""
    ref = re.sub(r"\b[A-Za-z_][A-Za-z0-9_$]*'\(([^()]*)\)", r"(\1)", ref)

    def lower_enum(match: re.Match[str]) -> str:
        width = (match.group("width") or "").strip()
        enum_type = match.group("type")
        raw_items = [item.strip() for item in match.group("items").split(",") if item.strip()]
        assignments = []
        next_value = 0
        for raw_item in raw_items:
            if "=" in raw_item:
                name, value = [part.strip() for part in raw_item.split("=", 1)]
                assignments.append(f"{name} = {value}")
                next_value += 1
            else:
                assignments.append(f"{raw_item} = {next_value}")
                next_value += 1
        range_text = f" {width}" if width else ""
        lowered = f"localparam{range_text} " + ", ".join(assignments) + ";"
        lower_enum.replacements[enum_type] = width
        return lowered

    lower_enum.replacements = {}  # type: ignore[attr-defined]
    ref = re.sub(
        r"typedef\s+enum\s+logic\s*(?P<width>\[[^\]]+\])?\s*\{(?P<items>.*?)\}\s*(?P<type>[A-Za-z_][A-Za-z0-9_$]*)\s*;",
        lower_enum,
        ref,
        flags=re.DOTALL,
    )
    for enum_type, width in lower_enum.replacements.items():  # type: ignore[attr-defined]
        ref = re.sub(rf"\b{re.escape(enum_type)}\s+", f"logic {width} ", ref)
    return ref


def interface_from_reference(ref: str) -> str:
    match = re.search(r"module\s+RefModule\s*\((.*?)\)\s*;", ref, flags=re.DOTALL)
    if not match:
        return ""
    return f"module TopModule ({match.group(1)});"


def declared_port_names(ref: str) -> set[str]:
    match = re.search(r"module\s+RefModule\s*\((.*?)\)\s*;", ref, flags=re.DOTALL)
    if not match:
        return set()
    names: set[str] = set()
    for raw_port in match.group(1).split(","):
        tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_$]*", raw_port)
        if tokens:
            names.add(tokens[-1])
    return names


def instantiated_port_names(testbench: str, module_name: str) -> set[str]:
    match = re.search(rf"\b{module_name}\s+\w+\s*\((.*?)\)\s*;", testbench, flags=re.DOTALL)
    if not match:
        return set()
    return set(re.findall(r"\.([A-Za-z_][A-Za-z0-9_$]*)\s*(?:\(|,|\))", match.group(1)))


def infer_type(problem_id: str, prompt: str, ref: str, ifc: str) -> str:
    text = f"{problem_id} {prompt} {ref} {ifc}".lower()
    if any(term in text for term in ("fsm", "state", "sequence", "lemmings")):
        return "verilogeval_fsm"
    if any(term in text for term in ("counter", "count", "timer", "shift register")):
        return "verilogeval_counter"
    if "posedge" in ref.lower() or any(term in text for term in ("clock", "clk", "flip-flop", "dff")):
        return "verilogeval_sequential"
    if any(term in text for term in ("adder", "sum", "carry", "popcount", "kmap")):
        return "verilogeval_arithmetic"
    if any(term in text for term in ("mux", "select", "priority", "case")):
        return "verilogeval_select"
    if "[" in ifc or any(term in text for term in ("vector", "bits", "byte")):
        return "verilogeval_vector"
    return "verilogeval_combinational"


def infer_level(index: int, total: int) -> str:
    bucket = min(4, (index * 5) // max(total, 1))
    return f"L{bucket + 1}"


def discover_problem_ids(dataset_dir: Path) -> list[str]:
    ids = []
    for ref_path in sorted(dataset_dir.glob("*_ref.sv")):
        ids.append(ref_path.name.removesuffix("_ref.sv"))
    return ids


def normalize_task(repo: Path, task: str, out_dir: Path) -> dict[str, Any]:
    dataset_dir = repo / TASK_DIRS[task]
    if not dataset_dir.exists():
        raise FileNotFoundError(f"VerilogEval dataset not found: {dataset_dir}")

    problem_ids = discover_problem_ids(dataset_dir)
    rows: list[dict[str, Any]] = []
    for idx, problem_id in enumerate(problem_ids):
        prompt_path = dataset_dir / f"{problem_id}_prompt.txt"
        ref_path = dataset_dir / f"{problem_id}_ref.sv"
        test_path = dataset_dir / f"{problem_id}_test.sv"
        ifc_path = dataset_dir / f"{problem_id}_ifc.txt"

        prompt_text = read_text(prompt_path)
        ref = read_text(ref_path)
        raw_testbench = read_text(test_path)
        reference_source = str(ref_path.relative_to(repo))
        test_ports = instantiated_port_names(raw_testbench, "TopModule")
        ref_ports = declared_port_names(ref)
        if task == "spec-to-rtl" and test_ports and not test_ports.issubset(ref_ports):
            alt_ref_path = repo / TASK_DIRS["code-complete-iccad2023"] / f"{problem_id}_ref.sv"
            if alt_ref_path.exists():
                alt_ref = read_text(alt_ref_path)
                if test_ports.issubset(declared_port_names(alt_ref)):
                    ref = alt_ref
                    reference_source = str(alt_ref_path.relative_to(repo))
        ref = icarus_compatible(ref)
        ifc = read_text(ifc_path) if ifc_path.exists() else interface_from_reference(ref)
        top_solution = ref_to_top_module(ref)
        testbench = ref.rstrip() + "\n\n" + raw_testbench
        rows.append({
            "task_id": problem_id,
            "problem_id": problem_id,
            "level": infer_level(idx, len(problem_ids)),
            "type": infer_type(problem_id, prompt_text, ref, ifc),
            "prompt": ifc,
            "description": prompt_text,
            "canonical_solution": top_solution,
            "test": testbench,
            "source": "NVlabs/verilog-eval",
            "source_task": task,
            "reference_source": reference_source,
            "candidate_contract": "candidate should define module TopModule",
        })

    task_out = out_dir / task
    write_jsonl(task_out / "problems.jsonl", rows)
    oracle_candidates = [
        {
            "task_id": row["task_id"],
            "completion": row["canonical_solution"],
            "candidate_source": "oracle_reference",
        }
        for row in rows
    ]
    write_jsonl(task_out / "oracle_candidates.jsonl", oracle_candidates)
    for mode in MODES:
        mode_rows = [dict(row, mode=mode) for row in oracle_candidates]
        write_jsonl(task_out / f"candidates_{mode}.jsonl", mode_rows)

    summary = {
        "task": task,
        "total": len(rows),
        "levels": dict(sorted(Counter(row["level"] for row in rows).items())),
        "types": dict(sorted(Counter(row["type"] for row in rows).items())),
        "candidate_files": {mode: str(task_out / f"candidates_{mode}.jsonl") for mode in MODES},
        "candidate_source": "oracle_reference",
        "note": "Replace candidates_<mode>.jsonl with real generated RTL before interpreting mode scores.",
    }
    write_json(task_out / "summary.json", summary)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare VerilogEval generation JSONL files")
    parser.add_argument("--repo", type=Path, default=DEFAULT_REPO)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--task", choices=("all", *TASK_DIRS.keys()), default="code-complete-iccad2023")
    args = parser.parse_args()

    tasks = list(TASK_DIRS) if args.task == "all" else [args.task]
    summaries = [normalize_task(args.repo, task, args.out_dir) for task in tasks]
    write_json(args.out_dir / "summary.json", {"tasks": summaries})
    print(json.dumps({"status": "ok", "out_dir": str(args.out_dir), "tasks": summaries}, ensure_ascii=False))


if __name__ == "__main__":
    main()
