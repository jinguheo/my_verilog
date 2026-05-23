#!/usr/bin/env python3
"""Build the final four-method retrieval comparison report.

The four methods are:
1. parser_lsp
2. kg
3. graphify
4. manticore

Manticore uses the parser+LSP document fields and a Manticore Search-style
BM25F ranker.  Graphify metrics are loaded from the existing Graphify comparison
artifact.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]


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


def level_weight(level: str) -> float:
    return {"L1": 1.0, "L2": 1.2, "L3": 1.5, "L4": 1.8, "L5": 2.2}[level]


def weighted_hit_at_1(questions: list[dict[str, Any]], predictions: list[dict[str, Any]]) -> float:
    weighted_hit = 0.0
    weighted_total = 0.0
    for question, prediction in zip(questions, predictions):
        weight = level_weight(question["level"])
        weighted_total += weight
        if prediction.get("gold_rank") == 1:
            weighted_hit += weight
    return round(weighted_hit / weighted_total, 4) if weighted_total else 0.0


def mantic_latency(metadata: dict[str, Any]) -> float:
    return metadata.get("latency_ms", {}).get("manticore_parser_lsp", {}).get("avg_query_ms", 0.0)


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    questions = read_jsonl(Path(args.questions))
    multiaxis = read_json(Path(args.multiaxis_report))
    graphify = read_json(Path(args.graphify_report))
    graphify_predictions = read_json(Path(args.graphify_predictions))
    manticore = read_json(Path(args.manticore_report))
    manticore_metadata = read_json(Path(args.manticore_metadata))

    baseline = multiaxis["by_mode"]["baseline"]
    kg = multiaxis["by_mode"]["kg"]
    graphify_perf = graphify["comparison"]["multiaxis"]["performance"]
    manticore_perf = manticore["by_mode"]["manticore_parser_lsp"]

    methods = {
        "parser_lsp": {
            "label": "Parser+LSP",
            "hit_at_1": baseline["hit_at_1"],
            "hit_at_3": baseline["hit_at_3"],
            "mrr": baseline["mrr"],
            "weighted_hit_at_1": baseline["weighted_hit_at_1"],
            "avg_query_ms": None,
            "features": {
                "Input signals": "tree-sitter parser/LSP seed: module name, file path, ports, instances",
                "Ranking": "Parser/LSP-style lexical overlap with exact anchors",
                "Strength": "Fast structural RTL lookup",
                "Tradeoff": "No cross-module graph or full-text ranker",
            },
        },
        "kg": {
            "label": "KG",
            "hit_at_1": kg["hit_at_1"],
            "hit_at_3": kg["hit_at_3"],
            "mrr": kg["mrr"],
            "weighted_hit_at_1": kg["weighted_hit_at_1"],
            "avg_query_ms": None,
            "features": {
                "Input signals": "parser/LSP seed plus labels, summaries, reverse parents",
                "Ranking": "KG-aware scorer with semantic expansion",
                "Strength": "Best weighted structural retrieval in this run",
                "Tradeoff": "Depends on KG label and graph quality",
            },
        },
        "graphify": {
            "label": "Graphify",
            "hit_at_1": graphify_perf["hit_at_1"],
            "hit_at_3": graphify_perf["hit_at_3"],
            "mrr": graphify_perf["mrr"],
            "weighted_hit_at_1": weighted_hit_at_1(questions, graphify_predictions),
            "avg_query_ms": None,
            "features": {
                "Input signals": "Graphify AST graph and BFS query subgraph",
                "Ranking": "Graph node match mapped back to RTL modules",
                "Strength": "General codebase navigation and relationship context",
                "Tradeoff": "Less Verilog-specific than the custom KG",
            },
        },
        "manticore": {
            "label": "Manticore",
            "hit_at_1": manticore_perf["hit_at_1"],
            "hit_at_3": manticore_perf["hit_at_3"],
            "mrr": manticore_perf["mrr"],
            "weighted_hit_at_1": manticore_perf["weighted_hit_at_1"],
            "avg_query_ms": mantic_latency(manticore_metadata),
            "features": {
                "Input signals": "parser/LSP fields indexed as Manticore-style full-text documents",
                "Ranking": "BM25F-style field weighting with exact boosts",
                "Strength": "Best Hit@3/MRR among parser+LSP-only methods",
                "Tradeoff": "Local proxy model; real searchd server not started",
            },
        },
    }

    return {
        "generated_at": args.generated_at,
        "question_set": str(Path(args.questions)),
        "questions": len(questions),
        "method_count": 4,
        "methods": methods,
        "sources": {
            "parser_lsp_and_kg": str(Path(args.multiaxis_report)),
            "graphify": str(Path(args.graphify_report)),
            "manticore": str(Path(args.manticore_report)),
            "manticore_github": "https://github.com/manticoresoftware/manticoresearch",
        },
    }


def write_markdown(report: dict[str, Any], path: Path) -> None:
    lines = [
        "# Retrieval Methods Comparison",
        "",
        f"Total methods: {report['method_count']}",
        f"Questions: {report['questions']}",
        "",
        "## Performance",
        "",
        "| Method | Hit@1 | Hit@3 | MRR | Weighted Hit@1 | Avg query ms |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for method in report["methods"].values():
        avg_query_ms = method["avg_query_ms"]
        avg_text = "n/a" if avg_query_ms is None else f"{avg_query_ms:.3f}"
        lines.append(
            f"| {method['label']} | {method['hit_at_1']:.4f} | {method['hit_at_3']:.4f} | "
            f"{method['mrr']:.4f} | {method['weighted_hit_at_1']:.4f} | {avg_text} |"
        )
    lines += [
        "",
        "## Method Features",
        "",
        "| Method | Input signals | Ranking | Strength | Tradeoff |",
        "|---|---|---|---|---|",
    ]
    for method in report["methods"].values():
        features = method["features"]
        lines.append(
            f"| {method['label']} | {features['Input signals']} | {features['Ranking']} | "
            f"{features['Strength']} | {features['Tradeoff']} |"
        )
    lines += [
        "",
        "## Reading",
        "",
        "- `KG` has the best weighted hit@1 because Verilog-specific labels and reverse graph hints help harder questions.",
        "- `Manticore` improves parser+LSP full-text ranking, especially hit@3 and MRR, without requiring KG fields.",
        "- `Graphify` is useful for broad codebase navigation but is weaker for exact Verilog module retrieval in this benchmark.",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Write four-method retrieval comparison")
    parser.add_argument("--questions", default=str(ROOT / "out" / "multiaxis_benchmark" / "questions_all.jsonl"))
    parser.add_argument("--multiaxis-report", default=str(ROOT / "out" / "multiaxis_eval_results" / "multiaxis_report.json"))
    parser.add_argument("--graphify-report", default=str(ROOT / "out" / "graphify_compare" / "comparison_report.json"))
    parser.add_argument("--graphify-predictions", default=str(ROOT / "out" / "graphify_compare" / "multiaxis_graphify_predictions.json"))
    parser.add_argument("--manticore-report", default=str(ROOT / "out" / "manticore_analysis" / "manticore_retrieval_report.json"))
    parser.add_argument("--manticore-metadata", default=str(ROOT / "out" / "manticore_analysis" / "manticore_retrieval_metadata.json"))
    parser.add_argument("--out-json", default=str(ROOT / "out" / "reports" / "retrieval_methods_comparison.json"))
    parser.add_argument("--out-md", default=str(ROOT / "out" / "reports" / "retrieval_methods_comparison.md"))
    parser.add_argument("--generated-at", default="2026-05-10T00:00:00+09:00")
    args = parser.parse_args()

    report = build_report(args)
    out_json = Path(args.out_json)
    out_md = Path(args.out_md)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_markdown(report, out_md)
    print(json.dumps({
        "status": "ok",
        "methods": list(report["methods"]),
        "out_json": str(out_json),
        "out_md": str(out_md),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
