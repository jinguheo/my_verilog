#!/usr/bin/env python3
"""Evaluate rank-fusion hybrids over existing retrieval runs."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


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
    return {"L1": 1.0, "L2": 1.2, "L3": 1.5, "L4": 1.8, "L5": 2.2}.get(level, 1.0)


def rank_of(gold_modules: list[str], topk: list[dict[str, Any]]) -> int | None:
    gold = {name.lower() for name in gold_modules}
    for idx, item in enumerate(topk, 1):
        if str(item.get("name", "")).lower() in gold:
            return idx
    return None


def score_norm(topk: list[dict[str, Any]], score: float) -> float:
    values = [float(item.get("score", 0.0) or 0.0) for item in topk]
    if not values:
        return 0.0
    lo = min(values)
    hi = max(values)
    if hi <= lo:
        return 0.0
    return (score - lo) / (hi - lo)


def fuse_runs(
    question: dict[str, Any],
    sources: dict[str, list[dict[str, Any]]],
    source_names: list[str],
    weights: dict[str, float],
    index: int,
    rrf_k: int,
    score_alpha: float,
) -> dict[str, Any]:
    by_name: dict[str, dict[str, Any]] = {}
    for source in source_names:
        run = sources[source][index]
        topk = run.get("topk", [])
        for rank, item in enumerate(topk, 1):
            name = str(item.get("name", ""))
            if not name:
                continue
            key = name.lower()
            row = by_name.setdefault(key, {
                "name": name,
                "project": item.get("project"),
                "score": 0.0,
                "sources": [],
                "source_ranks": {},
            })
            weight = weights.get(source, 1.0)
            raw_score = float(item.get("score", 0.0) or 0.0)
            fused = weight / (rrf_k + rank)
            fused += score_alpha * weight * score_norm(topk, raw_score)
            row["score"] += fused
            row["sources"].append(source)
            row["source_ranks"][source] = rank
            if item.get("project") and not row.get("project"):
                row["project"] = item.get("project")

    fused_rows = sorted(
        by_name.values(),
        key=lambda row: (-row["score"], -len(set(row["sources"])), row["name"]),
    )
    topk = [
        {
            "name": row["name"],
            "project": row.get("project"),
            "score": round(row["score"], 6),
            "sources": sorted(set(row["sources"])),
            "source_ranks": row["source_ranks"],
        }
        for row in fused_rows[:5]
    ]
    return {
        "task_id": question.get("task_id"),
        "level": question.get("level"),
        "type": question.get("type"),
        "gold_modules": question.get("gold_modules", []),
        "gold_rank": rank_of(question.get("gold_modules", []), topk),
        "topk": topk,
    }


def aggregate(questions: list[dict[str, Any]], runs_by_mode: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    report = {"by_mode": {}}
    for mode, runs in runs_by_mode.items():
        total = len(runs)
        hit1 = hit3 = hit5 = 0
        mrr = 0.0
        weighted_hit = 0.0
        weighted_total = 0.0
        by_level = defaultdict(lambda: {"count": 0, "hit1": 0, "hit3": 0, "hit5": 0, "mrr": 0.0})
        by_type = defaultdict(lambda: {"count": 0, "hit1": 0, "hit3": 0, "hit5": 0, "mrr": 0.0})
        for question, run in zip(questions, runs):
            rank = run["gold_rank"]
            level = str(question.get("level", "unknown"))
            qtype = str(question.get("type", "unknown"))
            weight = level_weight(level)
            weighted_total += weight
            by_level[level]["count"] += 1
            by_type[qtype]["count"] += 1
            if rank == 1:
                hit1 += 1
                weighted_hit += weight
                by_level[level]["hit1"] += 1
                by_type[qtype]["hit1"] += 1
            if rank is not None and rank <= 3:
                hit3 += 1
                by_level[level]["hit3"] += 1
                by_type[qtype]["hit3"] += 1
            if rank is not None and rank <= 5:
                hit5 += 1
                by_level[level]["hit5"] += 1
                by_type[qtype]["hit5"] += 1
            if rank is not None:
                rr = 1.0 / rank
                mrr += rr
                by_level[level]["mrr"] += rr
                by_type[qtype]["mrr"] += rr
        report["by_mode"][mode] = {
            "count": total,
            "hit_at_1": round(hit1 / total, 4) if total else 0.0,
            "hit_at_3": round(hit3 / total, 4) if total else 0.0,
            "hit_at_5": round(hit5 / total, 4) if total else 0.0,
            "mrr": round(mrr / total, 4) if total else 0.0,
            "weighted_hit_at_1": round(weighted_hit / weighted_total, 4) if weighted_total else 0.0,
            "misses": total - hit5,
            "by_level": {
                key: {
                    "count": vals["count"],
                    "hit_at_1": round(vals["hit1"] / vals["count"], 4),
                    "hit_at_3": round(vals["hit3"] / vals["count"], 4),
                    "hit_at_5": round(vals["hit5"] / vals["count"], 4),
                    "mrr": round(vals["mrr"] / vals["count"], 4),
                }
                for key, vals in sorted(by_level.items())
            },
            "by_type": {
                key: {
                    "count": vals["count"],
                    "hit_at_1": round(vals["hit1"] / vals["count"], 4),
                    "hit_at_3": round(vals["hit3"] / vals["count"], 4),
                    "hit_at_5": round(vals["hit5"] / vals["count"], 4),
                    "mrr": round(vals["mrr"] / vals["count"], 4),
                }
                for key, vals in sorted(by_type.items())
            },
        }
    return report


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    lines = [
        "# Hybrid Retrieval Evaluation",
        "",
        f"- Questions: {report['questions']}",
        f"- Fusion: {report['fusion']}",
        "",
        "## Overall",
        "",
        "| Method | hit@1 | hit@3 | hit@5 | MRR | weighted hit@1 | misses |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for mode, vals in report["performance"]["by_mode"].items():
        lines.append(
            f"| {mode} | {vals['hit_at_1']:.4f} | {vals['hit_at_3']:.4f} | "
            f"{vals['hit_at_5']:.4f} | {vals['mrr']:.4f} | {vals['weighted_hit_at_1']:.4f} | {vals['misses']} |"
        )
    lines += [
        "",
        "## By Type",
        "",
    ]
    for mode, vals in report["performance"]["by_mode"].items():
        lines += [
            f"### {mode}",
            "",
            "| Type | count | hit@1 | hit@3 | hit@5 | MRR |",
            "|---|---:|---:|---:|---:|---:|",
        ]
        for qtype, metric in vals["by_type"].items():
            lines.append(
                f"| {qtype} | {metric['count']} | {metric['hit_at_1']:.4f} | "
                f"{metric['hit_at_3']:.4f} | {metric['hit_at_5']:.4f} | {metric['mrr']:.4f} |"
            )
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run hybrid retrieval rank fusion")
    parser.add_argument("--questions", type=Path, default=Path("out/adversarial_retrieval_benchmark/questions_all.jsonl"))
    parser.add_argument("--manticore-runs", type=Path, default=Path("out/adversarial_manticore_eval/manticore_detailed_runs.json"))
    parser.add_argument("--graphify-runs", type=Path, default=Path("out/adversarial_graphify_module_card_eval/graphify_predictions.json"))
    parser.add_argument("--out-dir", type=Path, default=Path("out/adversarial_hybrid_eval"))
    parser.add_argument("--rrf-k", type=int, default=60)
    parser.add_argument("--score-alpha", type=float, default=0.015)
    args = parser.parse_args()

    questions = read_jsonl(args.questions)
    manticore_runs = read_json(args.manticore_runs)
    graphify_runs = read_json(args.graphify_runs)
    sources = {
        "parser_lsp": manticore_runs["baseline"],
        "kg": manticore_runs["kg"],
        "manticore": manticore_runs["manticore_parser_lsp"],
        "graphify": graphify_runs,
    }
    weights = {
        "parser_lsp": 1.0,
        "kg": 1.25,
        "manticore": 0.45,
        "graphify": 0.35,
    }
    combinations = {
        "hybrid_parser_kg_manticore": ["parser_lsp", "kg", "manticore"],
        "hybrid_parser_kg_graphify": ["parser_lsp", "kg", "graphify"],
        "hybrid_kg_manticore_graphify": ["kg", "manticore", "graphify"],
        "hybrid_all_4": ["parser_lsp", "kg", "manticore", "graphify"],
    }

    runs_by_mode: dict[str, list[dict[str, Any]]] = {}
    for mode, source_names in combinations.items():
        runs_by_mode[mode] = [
            fuse_runs(question, sources, source_names, weights, idx, args.rrf_k, args.score_alpha)
            for idx, question in enumerate(questions)
        ]

    performance = aggregate(questions, runs_by_mode)
    report = {
        "questions": len(questions),
        "question_file": str(args.questions),
        "fusion": {
            "type": "weighted reciprocal rank fusion plus light normalized score",
            "rrf_k": args.rrf_k,
            "score_alpha": args.score_alpha,
            "weights": weights,
            "combinations": combinations,
        },
        "performance": performance,
        "sources": {
            "manticore_runs": str(args.manticore_runs),
            "graphify_runs": str(args.graphify_runs),
        },
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "hybrid_retrieval_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (args.out_dir / "hybrid_detailed_runs.json").write_text(
        json.dumps(runs_by_mode, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_markdown(args.out_dir / "hybrid_retrieval_report.md", report)
    print(json.dumps({
        "status": "ok",
        "out_dir": str(args.out_dir),
        "best_hit_at_1": max(
            (vals["hit_at_1"], mode)
            for mode, vals in performance["by_mode"].items()
        ),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
