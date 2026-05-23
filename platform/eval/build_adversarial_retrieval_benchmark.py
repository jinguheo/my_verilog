#!/usr/bin/env python3
"""Build an adversarial RTL retrieval benchmark.

This benchmark is intentionally harder than name-hidden rewrites.  It selects
modules from ambiguous neighborhoods: many modules sharing a child, common
interfaces, or similar labels.  Questions hide the target name and avoid highly
unique port/filename clues where possible.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SEED = ROOT / "out" / "merged_ontology_seed.jsonl"
DEFAULT_OUT = ROOT / "out" / "adversarial_retrieval_benchmark" / "questions_all.jsonl"
DEFAULT_PROMPTS = ROOT / "out" / "adversarial_retrieval_benchmark" / "prompts_only.jsonl"
DEFAULT_REPORT = ROOT / "out" / "adversarial_retrieval_benchmark" / "catalog.md"

RESERVED = {
    "if", "for", "while", "case", "module", "interface", "end", "begin",
    "generate", "assign", "always", "function", "task", "unique", "auto",
    "is", "tb", "to", "can", "contains", "checks", "values",
}
PATH_EXCLUDES = ["\\dv\\", "\\tb", "\\formal\\", "\\pre_sca\\", "\\lint\\", "\\fpv\\", "\\doc\\"]
GENERIC_LABELS = {"clocked", "resettable", "hierarchical", "opentitan_ip", "ibex_core"}
COMMON_PORTS = {
    "clk_i", "rst_ni", "rst_i", "clock", "reset", "tlul_pkg", "prim_alert_pkg",
    "valid_i", "ready_i", "valid_o", "ready_o",
}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def clean_modules(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for row in rows:
        if row.get("entity_type") != "module":
            continue
        name = row.get("name", "")
        path_lower = row.get("path", "").lower()
        if not name or name.lower() in RESERVED or len(name) < 3:
            continue
        if any(token in path_lower for token in PATH_EXCLUDES):
            continue
        if sum(ch.isalpha() for ch in name) < 3:
            continue
        if re.fullmatch(r"[a-z]+", name.lower()) and name.lower() not in path_lower:
            continue
        mod = dict(row)
        mod["ports"] = [
            p for p in row.get("ports", [])
            if p.get("name") and p["name"].lower() not in RESERVED
        ]
        mod["instances"] = [
            i for i in row.get("instances", [])
            if i.get("type") and i["type"].lower() not in RESERVED
        ]
        mod["labels"] = sorted(set(row.get("labels", [])))
        out.append(mod)
    return out


def module_snapshot(module: dict[str, Any]) -> dict[str, Any]:
    return {
        "name": module["name"],
        "project": module.get("project", ""),
        "path": module.get("path", ""),
        "labels": module.get("labels", []),
        "ports": [p["name"] for p in module.get("ports", [])[:12]],
        "instances": [i["type"] for i in module.get("instances", [])[:12]],
    }


def indexes(modules: list[dict[str, Any]]) -> dict[str, Any]:
    by_child = defaultdict(list)
    by_label = defaultdict(list)
    by_prefix = defaultdict(list)
    for mod in modules:
        for inst in mod.get("instances", []):
            by_child[inst["type"]].append(mod)
        for label in mod.get("labels", []):
            if label not in GENERIC_LABELS:
                by_label[label].append(mod)
        prefix = mod["name"].split("_")[0]
        if len(prefix) > 2:
            by_prefix[prefix].append(mod)
    return {"by_child": by_child, "by_label": by_label, "by_prefix": by_prefix}


def labels(module: dict[str, Any], limit: int = 3) -> list[str]:
    selected = [label for label in module.get("labels", []) if label not in GENERIC_LABELS]
    return selected[:limit] or module.get("labels", [])[:limit]


def commonish_ports(module: dict[str, Any], limit: int = 4) -> list[str]:
    names = [p["name"] for p in module.get("ports", [])]
    common = [name for name in names if name in COMMON_PORTS]
    fallback = [
        name for name in names
        if not any(token in name.lower() for token in module["name"].lower().split("_") if len(token) > 2)
    ]
    selected = common + [name for name in fallback if name not in common]
    return selected[:limit]


def child_names(module: dict[str, Any], limit: int = 4) -> list[str]:
    names = []
    for inst in module.get("instances", []):
        name = inst["type"]
        if name != module["name"] and name not in names:
            names.append(name)
        if len(names) >= limit:
            break
    return names


def path_hint(module: dict[str, Any]) -> str:
    parts = [p for p in module.get("path", "").replace("/", "\\").split("\\") if p]
    name_tokens = [t for t in module["name"].lower().split("_") if len(t) > 2]
    filtered = []
    for part in parts:
        stem = Path(part).stem.lower()
        if stem == module["name"].lower() or any(token in stem for token in name_tokens):
            continue
        if stem in {"d:", "mywork", "verilog", "dbs", "hw", "rtl", "ip", "autogen", "shared"}:
            continue
        filtered.append(part)
    return " / ".join(filtered[-3:]) if filtered else module.get("project", "rtl")


def add_question(rows: list[dict[str, Any]], used: set[tuple[str, str]], qtype: str, module: dict[str, Any], question: str, evidence: list[str]) -> bool:
    key = (qtype, module["name"])
    if key in used:
        return False
    used.add(key)
    rows.append({
        "task_id": f"advret_{len(rows) + 1:03d}",
        "level": "L5" if len(rows) % 2 else "L4",
        "type": qtype,
        "question": question,
        "gold_modules": [module["name"]],
        "gold_projects": [module.get("project", "")],
        "gold_paths": [module.get("path", "")],
        "gold_evidence": evidence + ["adversarial_retrieval", "name_hidden"],
        "notes": "Adversarial blind retrieval: target name hidden and clues chosen from ambiguous neighborhoods.",
        "module_snapshots": [module_snapshot(module)],
    })
    return True


def parent_disambiguation(rows: list[dict[str, Any]], used: set[tuple[str, str]], modules: list[dict[str, Any]], by_child: dict[str, list[dict[str, Any]]]) -> None:
    for child, parents in sorted(by_child.items(), key=lambda item: -len(item[1])):
        unique = {p["name"]: p for p in parents}
        if len(unique) < 3:
            continue
        for parent in list(unique.values())[:4]:
            ports = ", ".join(commonish_ports(parent)) or "common clock/reset interface"
            lbl = ", ".join(labels(parent)) or "generic RTL role"
            question = (
                "Adversarial parent retrieval. A query is centered on a reused child dependency "
                f"`{child}`, but the answer must be the owning parent module. Pick the parent whose "
                f"coarse area is {path_hint(parent)}, whose common interface clues are {ports}, "
                f"and whose semantic role hints are {lbl}. Do not return the child itself or another parent "
                "that only shares the same child."
            )
            add_question(rows, used, "adversarial_parent_from_shared_child", parent, question, [f"shared_child={child}", *commonish_ports(parent), *labels(parent)])
            if len(rows) >= 50:
                return


def sibling_disambiguation(rows: list[dict[str, Any]], used: set[tuple[str, str]], by_prefix: dict[str, list[dict[str, Any]]]) -> None:
    for prefix, group in sorted(by_prefix.items(), key=lambda item: -len(item[1])):
        group = [m for m in group if len(m.get("ports", [])) >= 2]
        if len(group) < 3:
            continue
        for module in group[:4]:
            ports = ", ".join(commonish_ports(module)) or "common interface"
            deps = ", ".join(child_names(module, 3)) or "few explicit child blocks"
            lbl = ", ".join(labels(module)) or "generic RTL role"
            question = (
                "Adversarial sibling retrieval. Several modules in the same naming family are plausible, "
                "and the exact target name is hidden. Select the owner module matching this profile: "
                f"coarse area={path_hint(module)}; common ports={ports}; dependency hints={deps}; "
                f"semantic hints={lbl}. Avoid selecting a package, reg_top, primitive, or sibling that only "
                "matches the prefix."
            )
            add_question(rows, used, "adversarial_sibling_disambiguation", module, question, [*commonish_ports(module), *child_names(module, 3), *labels(module)])
            if len(rows) >= 95:
                return


def label_ambiguity(rows: list[dict[str, Any]], used: set[tuple[str, str]], by_label: dict[str, list[dict[str, Any]]]) -> None:
    for label, group in sorted(by_label.items(), key=lambda item: -len(item[1])):
        if len(group) < 10:
            continue
        candidates = [m for m in group if len(m.get("ports", [])) >= 2]
        for module in candidates[:5]:
            ports = ", ".join(commonish_ports(module)) or "common interface"
            deps = ", ".join(child_names(module, 3)) or "no strong child clue"
            question = (
                "Adversarial semantic retrieval. Many modules share the same broad semantic label, "
                f"`{label}`. Identify the one matching this hidden profile: project={module.get('project', '')}; "
                f"coarse area={path_hint(module)}; common interface={ports}; local dependency hints={deps}. "
                "Do not answer with another module that merely shares the label."
            )
            add_question(rows, used, "adversarial_label_ambiguity", module, question, [f"label={label}", *commonish_ports(module), *child_names(module, 3)])
            if len(rows) >= 140:
                return


def build_rows(modules: list[dict[str, Any]]) -> list[dict[str, Any]]:
    idx = indexes(modules)
    rows: list[dict[str, Any]] = []
    used: set[tuple[str, str]] = set()
    parent_disambiguation(rows, used, modules, idx["by_child"])
    sibling_disambiguation(rows, used, idx["by_prefix"])
    label_ambiguity(rows, used, idx["by_label"])
    return rows[:140]


def prompt_only(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "task_id": row["task_id"],
            "level": row["level"],
            "type": row["type"],
            "question": row["question"],
        }
        for row in rows
    ]


def write_report(path: Path, rows: list[dict[str, Any]]) -> None:
    by_type = Counter(row["type"] for row in rows)
    lines = [
        "# Adversarial Retrieval Benchmark",
        "",
        f"- Total tasks: {len(rows)}",
        "- Target names are hidden.",
        "- Questions are built from ambiguous child, sibling, and label neighborhoods.",
        "",
        "| Type | Count |",
        "|---|---:|",
    ]
    for qtype, count in sorted(by_type.items()):
        lines.append(f"| {qtype} | {count} |")
    lines += ["", "## Samples", ""]
    for row in rows[:12]:
        lines.append(f"- `{row['task_id']}` gold=`{row['gold_modules'][0]}`")
        lines.append(f"  - {row['question']}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build adversarial RTL retrieval benchmark")
    parser.add_argument("--seed", type=Path, default=DEFAULT_SEED)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--prompts-only", type=Path, default=DEFAULT_PROMPTS)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    modules = clean_modules(read_jsonl(args.seed))
    rows = build_rows(modules)
    write_jsonl(args.output, rows)
    write_jsonl(args.prompts_only, prompt_only(rows))
    write_report(args.report, rows)
    print(json.dumps({
        "status": "ok",
        "modules": len(modules),
        "tasks": len(rows),
        "output": str(args.output),
        "prompts_only": str(args.prompts_only),
        "report": str(args.report),
        "types": dict(sorted(Counter(row["type"] for row in rows).items())),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
