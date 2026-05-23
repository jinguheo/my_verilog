#!/usr/bin/env python3
"""Create a harder blind-anchor generation-context benchmark.

The existing hard-generation-context questions are useful, but many include the
gold module name directly in the prompt.  That makes lexical retrieval too easy.
This script rewrites those questions into blind-anchor tasks: the target module
name is hidden, while interface, child-instance, label, and role clues remain.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_IN = ROOT / "out" / "generation_context_eval" / "hard_generation_context_questions.jsonl"
DEFAULT_OUT = ROOT / "out" / "generation_context_eval" / "harder_generation_context_questions.jsonl"
DEFAULT_PROMPTS = ROOT / "out" / "generation_context_eval" / "harder_generation_context_prompts_only.jsonl"
DEFAULT_REPORT = ROOT / "out" / "generation_context_eval" / "harder_generation_context_report.md"

GENERIC_LABELS = {"clocked", "resettable", "hierarchical", "opentitan_ip", "ibex_core"}
HELPER_HINTS = ("reg_top", "_pkg", "prim_", "tlul_", "_core_reg_", "_cfg", "_status")


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


def first_snapshot(row: dict[str, Any]) -> dict[str, Any]:
    if isinstance(row.get("module_snapshot"), dict):
        return row["module_snapshot"]
    snapshots = row.get("module_snapshots")
    if isinstance(snapshots, list) and snapshots:
        return snapshots[0]
    return {}


def names_from_ports(raw_ports: list[Any], limit: int) -> list[str]:
    names = []
    for item in raw_ports:
        name = item.get("name") if isinstance(item, dict) else str(item)
        if name and name not in names:
            names.append(name)
        if len(names) >= limit:
            break
    return names


def names_from_instances(raw_instances: list[Any], limit: int) -> list[str]:
    names = []
    for item in raw_instances:
        name = item.get("type") if isinstance(item, dict) else str(item)
        if name and name not in names:
            names.append(name)
        if len(names) >= limit:
            break
    return names


def non_generic_labels(labels: list[str], limit: int) -> list[str]:
    chosen = [label for label in labels if label and label not in GENERIC_LABELS]
    return chosen[:limit] or labels[:limit]


def module_role(name: str, path: str, instances: list[str]) -> str:
    lower = f"{name} {path}".lower()
    if "chip_" in lower or "\\rtl\\autogen\\chip_" in lower:
        return "board/chip integration wrapper"
    if "\\top_" in lower or name.startswith("top_"):
        return "top-level SoC integration wrapper"
    if name.endswith("_reg_top") or "reg_top" in name:
        return "register interface block"
    if name.endswith("_core") or "_core" in name:
        return "core implementation block"
    if len(instances) >= 3:
        return "hierarchical controller or subsystem wrapper"
    return "primary RTL implementation block"


def visible_path_hint(path: str, gold: str) -> str:
    """Keep coarse path context without leaking the file/module name."""
    if not path:
        return "unknown RTL area"
    normalized = path.replace("/", "\\")
    parts = [part for part in normalized.split("\\") if part]
    filtered: list[str] = []
    gold_tokens = {token for token in re.split(r"[_\W]+", gold.lower()) if len(token) > 2}
    for part in parts:
        stem = Path(part).stem.lower()
        if stem == gold.lower() or gold.lower() in stem:
            continue
        if any(token and token in stem for token in gold_tokens):
            continue
        if part.lower() in {"rtl", "autogen", "ip", "hw", "dbs", "verilog"}:
            continue
        filtered.append(part)
    return " / ".join(filtered[-4:]) if filtered else "RTL implementation area"


def leak_free(text: str, gold_names: list[str]) -> str:
    for gold in sorted(gold_names, key=len, reverse=True):
        if not gold:
            continue
        text = re.sub(re.escape(gold), "[hidden-target]", text, flags=re.IGNORECASE)
    return text


def harder_level(level: str) -> str:
    return {"L1": "L4", "L2": "L4", "L3": "L4", "L4": "L5", "L5": "L5"}.get(level, "L5")


def make_question(row: dict[str, Any]) -> tuple[str, list[str]]:
    gold_names = [str(name) for name in row.get("gold_modules", [])]
    gold = gold_names[0] if gold_names else "target"
    snap = first_snapshot(row)
    ports = names_from_ports(snap.get("ports", []), 5)
    instances = names_from_instances(snap.get("instances", []), 5)
    labels = non_generic_labels(list(snap.get("labels", [])), 4)
    path_hint = visible_path_hint(str(snap.get("path", row.get("gold_paths", [""])[0] if row.get("gold_paths") else "")), gold)
    role = module_role(gold, str(snap.get("path", "")), instances)

    port_text = ", ".join(ports) if ports else "the exposed clock/reset and transaction interface"
    inst_text = ", ".join(instances) if instances else "its local implementation dependencies"
    label_text = ", ".join(labels) if labels else "its inferred subsystem role"

    question = (
        "Blind anchor retrieval task: identify the existing RTL module that should be used as the "
        "primary source for a generation brief. The target module name is intentionally hidden. "
        f"Use the following clues: role={role}; coarse location={path_hint}; key interface signals/types="
        f"{port_text}; local child/dependency clues={inst_text}; semantic labels={label_text}. "
        "Return the primary owner module, not a primitive, package, register helper, child dependency, "
        "or similarly named neighbor."
    )
    return leak_free(question, gold_names), ports + instances + labels


def harden_row(row: dict[str, Any], index: int) -> dict[str, Any]:
    question, evidence = make_question(row)
    gold_modules = [str(name) for name in row.get("gold_modules", [])]
    hardened = {
        **row,
        "task_id": f"hardblind_{index:03d}",
        "level": harder_level(str(row.get("level", "L5"))),
        "type": "hard_generation_context_blind_anchor",
        "question": question,
        "gold_evidence": sorted(set([*row.get("gold_evidence", []), *evidence, "blind_anchor", "name_hidden"])),
        "difficulty_notes": [
            "gold module name removed from prompt",
            "requires owner-vs-child disambiguation",
            "negative constraints penalize primitive/package/helper answers",
        ],
        "source_index": index,
    }
    return hardened


def write_report(path: Path, rows: list[dict[str, Any]]) -> None:
    by_level = Counter(row["level"] for row in rows)
    lines = [
        "# Harder Generation Context Benchmark",
        "",
        f"- Total tasks: {len(rows)}",
        "- Style: blind-anchor retrieval",
        "- Gold module names are removed from question text.",
        "- Questions emphasize interfaces, child dependencies, coarse location, role, and negative constraints.",
        "",
        "## Level Counts",
        "",
        "| Level | Count |",
        "|---|---:|",
    ]
    for level, count in sorted(by_level.items()):
        lines.append(f"| {level} | {count} |")
    lines += [
        "",
        "## Sample Questions",
        "",
    ]
    for row in rows[:10]:
        lines.append(f"- `{row['task_id']}` gold=`{', '.join(row['gold_modules'])}`")
        lines.append(f"  - {row['question']}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


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


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a harder blind-anchor generation-context question set")
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
