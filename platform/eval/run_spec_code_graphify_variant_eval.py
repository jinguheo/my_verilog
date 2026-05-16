#!/usr/bin/env python3
"""Evaluate spec-only, code-only, and spec-code Graphify variants."""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_QUESTIONS = ROOT / "out" / "spec_code_retrieval_benchmark" / "questions_all.jsonl"
DEFAULT_OUT = ROOT / "out" / "spec_code_graphify_variant_eval"
GRAPH_PATHS = {
    "spec-only": ROOT / "dbs" / "graphify-out" / "spec-only-graphify" / "graph.json",
    "code-only": ROOT / "dbs" / "graphify-out" / "code-only-graphify" / "graph.json",
    "spec-code": ROOT / "dbs" / "graphify-out" / "spec-code-graphify" / "graph.json",
}

BRIDGE_RELATIONS = {"spec_component_matches_code", "spec_path_matches_code_path"}
STOP = {
    "the",
    "and",
    "for",
    "that",
    "with",
    "from",
    "node",
    "nodes",
    "code",
    "spec",
    "side",
    "evidence",
    "relevant",
    "return",
    "retrieve",
    "graph",
    "connected",
    "implementation",
    "document",
    "artifact",
    "where",
    "review",
    "reviewer",
    "traceability",
    "checked",
    "concept",
    "clue",
    "area",
    "only",
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def tokenize(text: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for raw in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", text.lower()):
        parts = [raw] + raw.split("_")
        for token in parts:
            if len(token) < 3 or token in STOP:
                continue
            counts[token] += 1
    return counts


def norm_path(path: str) -> str:
    return path.replace("/", "\\").lower()


def node_text(node: dict[str, Any]) -> str:
    return " ".join(
        str(node.get(key, ""))
        for key in ("label", "file_type", "role", "source_file", "source_location", "community", "graph_variant")
    )


def relation(edge: dict[str, Any]) -> str:
    return str(edge.get("relation") or edge.get("type") or "related")


def source(edge: dict[str, Any]) -> str:
    return str(edge.get("source") or edge.get("_src") or "")


def target(edge: dict[str, Any]) -> str:
    return str(edge.get("target") or edge.get("_tgt") or "")


def load_graph(path: Path) -> dict[str, Any]:
    graph = read_json(path)
    nodes = {str(node["id"]): node for node in graph.get("nodes", [])}
    links = graph.get("links", graph.get("edges", []))
    adjacency: dict[str, list[tuple[str, dict[str, Any]]]] = defaultdict(list)
    for edge in links:
        src, tgt = source(edge), target(edge)
        if src in nodes and tgt in nodes:
            adjacency[src].append((tgt, edge))
            adjacency[tgt].append((src, edge))
    token_index = {node_id: tokenize(node_text(node)) for node_id, node in nodes.items()}
    return {"nodes": nodes, "links": links, "adjacency": adjacency, "token_index": token_index, "path": str(path)}


def overlap_score(query: Counter[str], doc: Counter[str]) -> float:
    score = 0.0
    for token, q_count in query.items():
        if token in doc:
            score += 1.0 + min(q_count, doc[token]) * 0.25
    return score


def retrieve(graph: dict[str, Any], question: str, limit: int = 30) -> list[dict[str, Any]]:
    query = tokenize(question)
    base: dict[str, float] = {}
    for node_id, tok in graph["token_index"].items():
        score = overlap_score(query, tok)
        if score:
            base[node_id] = score

    scores = dict(base)
    for node_id, score in list(base.items()):
        for nbr, edge in graph["adjacency"].get(node_id, []):
            rel = relation(edge)
            if rel in BRIDGE_RELATIONS:
                factor = 0.9
            elif rel in {"documents_component", "references_component", "contains"}:
                factor = 0.35
            elif rel in {"instantiates", "defines", "calls"}:
                factor = 0.25
            else:
                factor = 0.15
            scores[nbr] = scores.get(nbr, 0.0) + score * factor

    ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))[:limit]
    out = []
    for node_id, score in ranked:
        node = graph["nodes"][node_id]
        out.append(
            {
                "id": node_id,
                "label": node.get("label", ""),
                "file_type": node.get("file_type", ""),
                "role": node.get("role", ""),
                "source_file": node.get("source_file", ""),
                "community": node.get("community", ""),
                "score": round(score, 4),
            }
        )
    return out


def gold_match(candidate: dict[str, Any], gold: dict[str, Any]) -> bool:
    cand_path = norm_path(str(candidate.get("source_file", "")))
    gold_path = norm_path(str(gold.get("source_file", "")))
    cand_label = str(candidate.get("label", "")).lower()
    gold_label = str(gold.get("label", "")).lower()
    if gold_path and cand_path == gold_path and cand_label == gold_label:
        return True
    if gold_path and cand_path == gold_path:
        return True
    return bool(gold_label and cand_label == gold_label and candidate.get("file_type") == gold.get("file_type"))


def rank_of(topk: list[dict[str, Any]], golds: list[dict[str, Any]]) -> int | None:
    for idx, candidate in enumerate(topk, 1):
        if any(gold_match(candidate, gold) for gold in golds):
            return idx
    return None


def metrics(runs: list[dict[str, Any]], key: str) -> dict[str, Any]:
    ranks = [run.get(key) for run in runs]
    total = len(ranks)
    return {
        "count": total,
        "hit_at_1": round(sum(1 for rank in ranks if rank == 1) / total, 4) if total else 0,
        "hit_at_3": round(sum(1 for rank in ranks if rank is not None and rank <= 3) / total, 4) if total else 0,
        "hit_at_5": round(sum(1 for rank in ranks if rank is not None and rank <= 5) / total, 4) if total else 0,
        "hit_at_10": round(sum(1 for rank in ranks if rank is not None and rank <= 10) / total, 4) if total else 0,
        "mrr": round(sum((1 / rank) if rank else 0 for rank in ranks) / total, 4) if total else 0,
        "misses_at_10": sum(1 for rank in ranks if rank is None or rank > 10),
    }


def aggregate(questions: list[dict[str, Any]], runs: list[dict[str, Any]]) -> dict[str, Any]:
    out = {
        "spec": metrics(runs, "spec_rank"),
        "code": metrics(runs, "code_rank"),
        "joint": metrics(runs, "joint_rank"),
    }
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for question, run in zip(questions, runs):
        by_type[str(question.get("type", "unknown"))].append(run)
    out["by_type"] = {
        qtype: {
            "spec": metrics(items, "spec_rank"),
            "code": metrics(items, "code_rank"),
            "joint": metrics(items, "joint_rank"),
        }
        for qtype, items in sorted(by_type.items())
    }
    return out


def joint_rank(spec_rank: int | None, code_rank: int | None) -> int | None:
    if spec_rank is None or code_rank is None:
        return None
    return max(spec_rank, code_rank)


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    lines = [
        "# Spec-Code Graphify Variant Evaluation",
        "",
        f"- Questions: {report['questions']}",
        f"- Benchmark: `{report['benchmark']}`",
        "",
        "## Overall",
        "",
        "| Variant | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 | joint MRR |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for variant, perf in report["performance"].items():
        lines.append(
            f"| {variant} | {perf['spec']['hit_at_5']} | {perf['code']['hit_at_5']} | "
            f"{perf['joint']['hit_at_5']} | {perf['joint']['hit_at_10']} | {perf['joint']['mrr']} |"
        )
    lines += ["", "## By Type", ""]
    for variant, perf in report["performance"].items():
        lines += [
            f"### {variant}",
            "",
            "| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |",
            "|---|---:|---:|---:|---:|",
        ]
        for qtype, vals in perf["by_type"].items():
            lines.append(
                f"| {qtype} | {vals['spec']['hit_at_5']} | {vals['code']['hit_at_5']} | "
                f"{vals['joint']['hit_at_5']} | {vals['joint']['hit_at_10']} |"
            )
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--questions", type=Path, default=DEFAULT_QUESTIONS)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--limit", type=int, default=30)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    questions = read_jsonl(args.questions)
    graphs = {name: load_graph(path) for name, path in GRAPH_PATHS.items()}

    detailed: dict[str, list[dict[str, Any]]] = {}
    performance = {}
    for name, graph in graphs.items():
        runs = []
        for row in questions:
            topk = retrieve(graph, row["question"], limit=args.limit)
            spec_rank = rank_of(topk, row.get("gold_spec_nodes", []))
            code_rank = rank_of(topk, row.get("gold_code_nodes", []))
            runs.append(
                {
                    "task_id": row["task_id"],
                    "type": row.get("type"),
                    "spec_rank": spec_rank,
                    "code_rank": code_rank,
                    "joint_rank": joint_rank(spec_rank, code_rank),
                    "topk": topk[:10],
                }
            )
        detailed[name] = runs
        performance[name] = aggregate(questions, runs)

    report = {
        "questions": len(questions),
        "benchmark": str(args.questions),
        "graphs": {name: str(path) for name, path in GRAPH_PATHS.items()},
        "performance": performance,
    }
    (args.out_dir / "spec_code_graphify_variant_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (args.out_dir / "spec_code_graphify_variant_predictions.json").write_text(
        json.dumps(detailed, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_markdown(args.out_dir / "spec_code_graphify_variant_report.md", report)
    print(json.dumps({"status": "ok", "out_dir": str(args.out_dir), "performance": performance}, ensure_ascii=False))


if __name__ == "__main__":
    main()
