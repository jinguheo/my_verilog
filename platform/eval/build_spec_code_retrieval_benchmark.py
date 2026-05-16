#!/usr/bin/env python3
"""Build a spec-code retrieval benchmark from Graphify bridge edges.

The benchmark is designed to test whether a retrieval graph benefits from
having spec and code nodes connected.  Each question has both spec-side and
code-side gold evidence.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_GRAPH = ROOT / "dbs" / "graphify-out" / "spec-code-graphify" / "graph.json"
DEFAULT_OUT = ROOT / "out" / "spec_code_retrieval_benchmark" / "questions_all.jsonl"
DEFAULT_PROMPTS = ROOT / "out" / "spec_code_retrieval_benchmark" / "prompts_only.jsonl"
DEFAULT_CATALOG = ROOT / "out" / "spec_code_retrieval_benchmark" / "catalog.md"

BRIDGE_RELATIONS = {"spec_component_matches_code", "spec_path_matches_code_path"}
GENERIC = {
    "component",
    "document",
    "section",
    "topic",
    "source",
    "code",
    "spec",
    "graph",
    "opentitan",
    "lowrisc",
    "software",
    "system",
    "readme",
    "overview",
    "testing",
    "verification",
    "interfaces",
    "registers",
    "security",
    "theory",
    "operation",
    "testplan",
    "autogen",
    "rtl",
    "doc",
    "data",
    "hw",
    "ip",
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def tokens(text: str) -> list[str]:
    out = []
    for token in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", text.lower()):
        if len(token) < 3 or token in GENERIC:
            continue
        out.append(token)
        out.extend(part for part in token.split("_") if len(part) >= 3 and part not in GENERIC)
    return out


def clean_label(label: str) -> str:
    label = label.replace("component:", "").replace("topic:", "")
    return label.strip()


def path_tail(path: str, depth: int = 4) -> str:
    parts = [part for part in re.split(r"[\\/]+", path) if part]
    return "/".join(parts[-depth:]) if parts else path


def ip_hint(path: str, label: str) -> str:
    source = path.replace("\\", "/").lower()
    for marker in ("/hw/ip/", "/ip_autogen/", "/ip_templates/"):
        if marker in source:
            return source.split(marker, 1)[1].split("/", 1)[0]
    label_tokens = tokens(label)
    return label_tokens[0] if label_tokens else "unknown"


def gold_node(node: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": node["id"],
        "label": node.get("label", ""),
        "file_type": node.get("file_type", ""),
        "role": node.get("role", ""),
        "source_file": node.get("source_file", ""),
        "source_location": node.get("source_location", ""),
        "community": node.get("community", ""),
    }


def node_quality(spec: dict[str, Any], code: dict[str, Any]) -> int:
    score = 0
    spec_label = clean_label(str(spec.get("label", "")))
    code_label = str(code.get("label", ""))
    spec_path = str(spec.get("source_file", ""))
    code_path = str(code.get("source_file", ""))
    shared = set(tokens(spec_label + " " + spec_path)).intersection(tokens(code_label + " " + code_path))
    score += 10 * len(shared)
    if code_path.lower().endswith((".sv", ".v", ".svh", ".vh")):
        score += 20
    if str(spec.get("role")) in {"component", "document", "section", "topic"}:
        score += 10
    if "testplan" in spec_path.lower() or "theory_of_operation" in spec_path.lower() or "interfaces" in spec_path.lower():
        score += 12
    if len(clean_label(spec_label)) >= 3 and len(code_label) >= 3:
        score += 5
    return score


def build_candidates(graph: dict[str, Any]) -> list[dict[str, Any]]:
    nodes = {str(node["id"]): node for node in graph.get("nodes", [])}
    component_by_token: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for node in nodes.values():
        if node.get("file_type") == "document" and node.get("role") == "component":
            label = clean_label(str(node.get("label", "")))
            for token in tokens(label):
                component_by_token[token].append(node)
    candidates = []
    seen: set[tuple[str, str, str]] = set()
    for edge in graph.get("links", []):
        rel = str(edge.get("relation") or "")
        if rel not in BRIDGE_RELATIONS:
            continue
        src = str(edge.get("source") or edge.get("_src"))
        tgt = str(edge.get("target") or edge.get("_tgt"))
        spec = nodes.get(src)
        code = nodes.get(tgt)
        if not spec or not code:
            continue
        if spec.get("file_type") != "document":
            spec, code = code, spec
        if spec.get("file_type") != "document" or code.get("file_type") not in {"code", "rationale"}:
            continue
        key = (str(spec["id"]), str(code["id"]), rel)
        if key in seen:
            continue
        seen.add(key)
        hint_tokens = tokens(ip_hint(str(spec.get("source_file", "")) + " " + str(code.get("source_file", "")), str(spec.get("label", ""))))
        alternate_specs = []
        seen_alt = {str(spec["id"])}
        for token in hint_tokens:
            for alt in component_by_token.get(token, [])[:3]:
                if str(alt["id"]) not in seen_alt:
                    alternate_specs.append(alt)
                    seen_alt.add(str(alt["id"]))
        candidates.append(
            {
                "spec": spec,
                "alternate_specs": alternate_specs,
                "code": code,
                "relation": rel,
                "quality": node_quality(spec, code),
            }
        )
    candidates.sort(key=lambda item: item["quality"], reverse=True)
    return candidates


def question_templates(candidate: dict[str, Any], index: int) -> tuple[str, str, list[str]]:
    spec = candidate["spec"]
    code = candidate["code"]
    rel = candidate["relation"]
    spec_label = clean_label(str(spec.get("label", "")))
    code_label = str(code.get("label", ""))
    spec_path = str(spec.get("source_file", ""))
    code_path = str(code.get("source_file", ""))
    component = clean_label(spec_label) or ip_hint(spec_path, code_label)
    ip = ip_hint(spec_path + " " + code_path, component)
    spec_tail = path_tail(spec_path, 5)
    code_tail = path_tail(code_path, 5)

    variants = [
        (
            "spec_to_code_trace",
            (
                f"Find the implementation-side code evidence for the spec concept `{component}`. "
                f"The spec-side clue is `{spec_tail}` and the expected answer should include the connected RTL/code node, not just the document node."
            ),
            [component, spec_tail, "implementation", rel],
        ),
        (
            "code_to_spec_trace",
            (
                f"Find the spec-side evidence that explains the code node `{code_label}` under `{code_tail}`. "
                f"Return the relevant spec/document node as well as the code node so traceability can be checked."
            ),
            [code_label, code_tail, "spec evidence", rel],
        ),
        (
            "requirement_to_rtl",
            (
                f"A reviewer asks where the `{ip}` requirement described around `{component}` is implemented. "
                f"Retrieve both the spec node and the RTL/code node connected by the spec-code graph."
            ),
            [ip, component, "requirement", "RTL"],
        ),
        (
            "bridge_disambiguation",
            (
                f"Use the graph bridge, not only lexical filename matching: connect spec clue `{component}` "
                f"from `{spec_tail}` to the most relevant code artifact in `{code_tail}`."
            ),
            [component, spec_tail, code_tail, "bridge"],
        ),
        (
            "verification_trace",
            (
                f"For verification or review, identify the spec/document anchor and code artifact that should be inspected together "
                f"for `{component}` in the `{ip}` area."
            ),
            [component, ip, "verification", "review"],
        ),
    ]
    return variants[index % len(variants)]


def build_rows(candidates: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    rows = []
    type_counts = Counter()
    used_pairs: set[tuple[str, str]] = set()
    for candidate in candidates:
        spec = candidate["spec"]
        code = candidate["code"]
        pair = (str(spec["id"]), str(code["id"]))
        if pair in used_pairs:
            continue
        qtype, question, evidence = question_templates(candidate, len(rows))
        if type_counts[qtype] >= (limit // 5 + 4):
            continue
        used_pairs.add(pair)
        type_counts[qtype] += 1
        rows.append(
            {
                "task_id": f"speccode_{len(rows) + 1:03d}",
                "level": "L5" if len(rows) % 3 else "L4",
                "type": qtype,
                "question": question,
                "gold_spec_nodes": [gold_node(spec)] + [gold_node(alt) for alt in candidate.get("alternate_specs", [])],
                "gold_code_nodes": [gold_node(code)],
                "gold_bridge_relations": [candidate["relation"]],
                "gold_evidence": evidence,
                "notes": "Spec-code retrieval: answer requires both spec-side and code-side evidence.",
            }
        )
        if len(rows) >= limit:
            break
    return rows


def write_catalog(path: Path, rows: list[dict[str, Any]], graph_path: Path) -> None:
    by_type = Counter(row["type"] for row in rows)
    lines = [
        "# Spec-Code Retrieval Benchmark",
        "",
        f"- Questions: {len(rows)}",
        f"- Source graph: `{graph_path}`",
        "- Goal: compare code-only, spec-only, and spec-code Graphify variants.",
        "",
        "## Distribution",
        "",
        "| Type | Count |",
        "|---|---:|",
    ]
    for qtype, count in sorted(by_type.items()):
        lines.append(f"| {qtype} | {count} |")
    lines += [
        "",
        "## First 10 Questions",
        "",
    ]
    for row in rows[:10]:
        lines += [
            f"### {row['task_id']} - {row['type']}",
            "",
            row["question"],
            "",
            f"- Spec gold: `{row['gold_spec_nodes'][0]['label']}` from `{row['gold_spec_nodes'][0]['source_file']}`",
            f"- Code gold: `{row['gold_code_nodes'][0]['label']}` from `{row['gold_code_nodes'][0]['source_file']}`",
            "",
        ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--prompts", type=Path, default=DEFAULT_PROMPTS)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--limit", type=int, default=150)
    args = parser.parse_args()

    graph = read_json(args.graph)
    rows = build_rows(build_candidates(graph), args.limit)
    if len(rows) < args.limit:
        raise SystemExit(f"only built {len(rows)} rows; need {args.limit}")
    write_jsonl(args.out, rows)
    write_jsonl(args.prompts, [{"task_id": row["task_id"], "question": row["question"]} for row in rows])
    write_catalog(args.catalog, rows, args.graph)
    print(json.dumps({"status": "ok", "questions": len(rows), "out": str(args.out)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
