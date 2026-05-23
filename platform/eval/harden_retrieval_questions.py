#!/usr/bin/env python3
"""Create a harder blind retrieval benchmark from the multi-axis question set.

The default multi-axis retrieval set contains many direct name lookups.  This
rewriter hides gold module names and turns each question into a profile-based
retrieval task.  It preserves answer keys for scoring and writes a prompt-only
file that can be handed to a model without leaking gold modules.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_IN = ROOT / "out" / "multiaxis_benchmark" / "questions_all.jsonl"
DEFAULT_OUT = ROOT / "out" / "hard_retrieval_benchmark" / "questions_all.jsonl"
DEFAULT_PROMPTS = ROOT / "out" / "hard_retrieval_benchmark" / "prompts_only.jsonl"
DEFAULT_REPORT = ROOT / "out" / "hard_retrieval_benchmark" / "catalog.md"

GENERIC_LABELS = {"clocked", "resettable", "hierarchical", "opentitan_ip", "ibex_core"}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def snap_name(snap: dict[str, Any]) -> str:
    return str(snap.get("name", "target"))


def clean_list(values: list[Any], limit: int) -> list[str]:
    out: list[str] = []
    for raw in values:
        value = str(raw)
        if value and value not in out:
            out.append(value)
        if len(out) >= limit:
            break
    return out


def useful_labels(labels: list[str], limit: int = 4) -> list[str]:
    selected = [label for label in labels if label and label not in GENERIC_LABELS]
    return clean_list(selected or labels, limit)


def hidden_level(level: str) -> str:
    return {"L1": "L4", "L2": "L4", "L3": "L4", "L4": "L5", "L5": "L5"}.get(level, "L5")


def coarse_path(path: str, gold_names: list[str]) -> str:
    if not path:
        return "unknown RTL area"
    lower_names = {name.lower() for name in gold_names}
    name_tokens = {
        token
        for name in lower_names
        for token in re.split(r"[_\W]+", name)
        if len(token) > 2
    }
    parts = [part for part in path.replace("/", "\\").split("\\") if part]
    filtered: list[str] = []
    for part in parts:
        stem = Path(part).stem.lower()
        if stem in lower_names or any(token in stem for token in name_tokens):
            continue
        if stem in {"d:", "mywork", "verilog", "dbs", "hw", "rtl", "autogen", "ip", "shared"}:
            continue
        filtered.append(part)
    return " / ".join(filtered[-4:]) if filtered else "RTL implementation area"


def leak_free(text: str, gold_names: list[str]) -> str:
    for gold in sorted(gold_names, key=len, reverse=True):
        if gold:
            text = re.sub(re.escape(gold), "[hidden-target]", text, flags=re.IGNORECASE)
    return text


def role_hint(snap: dict[str, Any], original_type: str) -> str:
    name = snap_name(snap).lower()
    path = str(snap.get("path", "")).lower()
    instances = snap.get("instances", [])
    if original_type == "search_navigation":
        return "module navigation target"
    if original_type == "comparison_similarity":
        return "candidate in an architectural comparison"
    if original_type == "function_similarity":
        return "semantic/function analog candidate"
    if "reg_top" in name:
        return "register interface block"
    if name.startswith("top_") or "\\top_" in path:
        return "top-level integration block"
    if len(instances) >= 3:
        return "hierarchical RTL block"
    return "RTL implementation block"


def profile_text(snap: dict[str, Any], gold_names: list[str], original_type: str, idx: int) -> str:
    ports = clean_list(list(snap.get("ports", [])), 6)
    instances = clean_list(list(snap.get("instances", [])), 6)
    labels = useful_labels(list(snap.get("labels", [])), 4)
    path_hint = coarse_path(str(snap.get("path", "")), gold_names)
    text = (
        f"Profile {idx}: role={role_hint(snap, original_type)}; project={snap.get('project', 'unknown')}; "
        f"coarse location={path_hint}; exposed interface clues={', '.join(ports) if ports else 'not enough port data'}; "
        f"child/dependency clues={', '.join(instances) if instances else 'few or no local child instances'}; "
        f"semantic labels={', '.join(labels) if labels else 'none'}."
    )
    return leak_free(text, gold_names)


def hard_question(row: dict[str, Any]) -> str:
    gold_names = [str(name) for name in row.get("gold_modules", [])]
    snapshots = row.get("module_snapshots") or []
    original_type = str(row.get("type", "retrieval"))
    profiles = [
        profile_text(snap, gold_names, original_type, idx)
        for idx, snap in enumerate(snapshots[:3], start=1)
    ]
    if not profiles:
        profiles = ["Profile 1: sparse module profile; use available evidence only."]

    instruction = (
        "Blind RTL retrieval task. The original module names are intentionally hidden. "
        "Identify the best matching RTL module or modules from the knowledge DB using only the profiles below. "
        "Do not answer with primitive cells, packages, testbench files, documentation pages, child-only helpers, "
        "or a neighbor that merely shares a port name. "
    )
    if len(gold_names) > 1:
        instruction += "Multiple profiles may correspond to multiple valid gold modules; return the strongest matching module first. "
    else:
        instruction += "Return the primary owner module, not one of its children. "
    return instruction + " ".join(profiles)


def harden_row(row: dict[str, Any], index: int) -> dict[str, Any]:
    gold_names = [str(name) for name in row.get("gold_modules", [])]
    question = hard_question(row)
    return {
        **row,
        "task_id": f"hardret_{index:03d}",
        "level": hidden_level(str(row.get("level", "L5"))),
        "type": f"hard_retrieval_blind_{row.get('type', 'unknown')}",
        "question": leak_free(question, gold_names),
        "gold_evidence": sorted(set([*row.get("gold_evidence", []), "blind_retrieval", "name_hidden"])),
        "difficulty_notes": [
            "gold module names removed from prompt",
            "all direct lookup questions converted to profile retrieval",
            "requires owner/child/helper/neighbor disambiguation",
        ],
        "source_index": index,
    }


def prompt_only_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "task_id": row["task_id"],
            "level": row["level"],
            "type": row["type"],
            "question": row["question"],
            "difficulty_notes": row["difficulty_notes"],
        }
        for row in rows
    ]


def write_report(path: Path, rows: list[dict[str, Any]]) -> None:
    by_level = Counter(row["level"] for row in rows)
    by_type = Counter(row["type"] for row in rows)
    lines = [
        "# Hard Retrieval Benchmark Catalog",
        "",
        f"- Total tasks: {len(rows)}",
        "- Style: blind RTL retrieval",
        "- Gold module names are removed from prompt text.",
        "- Direct lookup tasks are converted into profile-based retrieval tasks.",
        "",
        "## Level Counts",
        "",
        "| Level | Count |",
        "|---|---:|",
    ]
    for level, count in sorted(by_level.items()):
        lines.append(f"| {level} | {count} |")
    lines += ["", "## Type Counts", "", "| Type | Count |", "|---|---:|"]
    for qtype, count in sorted(by_type.items()):
        lines.append(f"| {qtype} | {count} |")
    lines += ["", "## Samples", ""]
    for row in rows[:12]:
        lines.append(f"- `{row['task_id']}` {row['level']} gold=`{', '.join(row['gold_modules'])}`")
        lines.append(f"  - {row['question']}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a hard blind retrieval benchmark")
    parser.add_argument("--input", type=Path, default=DEFAULT_IN)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--prompts-only", type=Path, default=DEFAULT_PROMPTS)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    source_rows = read_jsonl(args.input)
    rows = [harden_row(row, idx) for idx, row in enumerate(source_rows, 1)]
    write_jsonl(args.output, rows)
    write_jsonl(args.prompts_only, prompt_only_rows(rows))
    write_report(args.report, rows)
    print(json.dumps({
        "status": "ok",
        "input": str(args.input),
        "output": str(args.output),
        "prompts_only": str(args.prompts_only),
        "report": str(args.report),
        "total": len(rows),
        "levels": dict(sorted(Counter(row["level"] for row in rows).items())),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
