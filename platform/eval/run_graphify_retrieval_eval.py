#!/usr/bin/env python3
"""Evaluate Graphify retrieval on an arbitrary RTL question JSONL file."""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT / "platform" / "eval") not in sys.path:
    sys.path.insert(0, str(ROOT / "platform" / "eval"))

from compare_graphify_vs_kg import (  # noqa: E402
    graphify_candidates,
    load_kg,
    load_or_build_graphify,
    norm_path,
    rank_of,
    read_jsonl,
)

PATH_EXCLUDES = ("\\dv\\", "\\tb", "\\formal\\", "\\pre_sca\\", "\\lint\\", "\\fpv\\", "\\doc\\")


def is_rtl_candidate(candidate: dict[str, Any]) -> bool:
    path = str(candidate.get("path", "")).lower().replace("/", "\\")
    return not any(token in path for token in PATH_EXCLUDES)


def question_tokens(text: str) -> set[str]:
    import re

    stop = {
        "the", "and", "that", "with", "from", "module", "modules", "return",
        "answer", "query", "retrieval", "adversarial", "common", "whose",
        "clues", "semantic", "role", "parent", "child", "dependency",
        "hidden", "target", "owner", "only", "same", "shared",
    }
    tokens = set()
    for raw in re.findall(r"[A-Za-z0-9_$]+", text.lower()):
        if len(raw) <= 2 or raw in stop:
            continue
        tokens.add(raw)
        for part in raw.split("_"):
            if len(part) > 2 and part not in stop:
                tokens.add(part)
    return tokens


def record_for_candidate(kg: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any] | None:
    records = kg["by_path"].get(norm_path(candidate.get("path", "")), [])
    if records:
        return records[0]
    records = kg["by_name_project"].get((candidate.get("name", "").lower(), candidate.get("project", "").lower()), [])
    return records[0] if records else None


def card_score(record: dict[str, Any], question: str) -> float:
    tokens = question_tokens(question)
    score = 0.0
    for port in record.get("ports", []):
        parts = question_tokens(port)
        if port.lower() in tokens or parts.intersection(tokens):
            score += 5.0
    for inst in record.get("instances", []):
        parts = question_tokens(inst)
        if inst.lower() in tokens or parts.intersection(tokens):
            score += 7.0
    for label in record.get("labels", []):
        parts = question_tokens(label)
        if label.lower() in tokens or parts.intersection(tokens):
            score += 3.0
    project = str(record.get("project", "")).lower()
    if project and project in tokens:
        score += 2.0
    path_parts = question_tokens(str(record.get("path", "")).replace("\\", " "))
    score += 0.6 * len(path_parts.intersection(tokens))
    return score


def rerank_by_module_card(kg: dict[str, Any], candidates: list[dict[str, Any]], question: str) -> list[dict[str, Any]]:
    scored = []
    for idx, candidate in enumerate(candidates):
        record = record_for_candidate(kg, candidate)
        if not record:
            continue
        score = card_score(record, question)
        adjusted = dict(candidate)
        adjusted["graphify_score"] = candidate.get("score")
        adjusted["score"] = round(score, 3)
        scored.append((score, -idx, adjusted))
    scored.sort(key=lambda item: (-item[0], item[1], item[2].get("name", "")))
    return [item[2] for item in scored]


def aggregate(rows: list[dict[str, Any]], predictions: list[dict[str, Any]]) -> dict[str, Any]:
    ranks = [pred["gold_rank"] for pred in predictions]

    def metrics(indexes: list[int]) -> dict[str, Any]:
        local = [ranks[i] for i in indexes]
        total = len(local)
        return {
            "count": total,
            "hit_at_1": round(sum(1 for rank in local if rank == 1) / total, 4) if total else 0.0,
            "hit_at_3": round(sum(1 for rank in local if rank is not None and rank <= 3) / total, 4) if total else 0.0,
            "hit_at_5": round(sum(1 for rank in local if rank is not None and rank <= 5) / total, 4) if total else 0.0,
            "mrr": round(sum((1 / rank) if rank else 0 for rank in local) / total, 4) if total else 0.0,
            "misses": sum(1 for rank in local if rank is None),
        }

    out = metrics(list(range(len(rows))))
    for key in ("level", "type"):
        grouped: dict[str, list[int]] = defaultdict(list)
        for idx, row in enumerate(rows):
            grouped[str(row.get(key, "unknown"))].append(idx)
        out[f"by_{key}"] = {name: metrics(indexes) for name, indexes in sorted(grouped.items())}
    return out


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    perf = report["performance"]
    lines = [
        "# Graphify Retrieval Evaluation",
        "",
        f"- Questions: {perf['count']}",
        f"- Question file: `{report['questions']}`",
        f"- Graph: `{report['graph']}`",
        "",
        "## Overall",
        "",
        "| Method | hit@1 | hit@3 | hit@5 | MRR | Misses |",
        "|---|---:|---:|---:|---:|---:|",
        f"| Graphify | {perf['hit_at_1']} | {perf['hit_at_3']} | {perf['hit_at_5']} | {perf['mrr']} | {perf['misses']} |",
        "",
        "## By Level",
        "",
        "| Level | Count | hit@1 | hit@3 | hit@5 | MRR |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for level, vals in perf["by_level"].items():
        lines.append(
            f"| {level} | {vals['count']} | {vals['hit_at_1']} | {vals['hit_at_3']} | {vals['hit_at_5']} | {vals['mrr']} |"
        )
    lines += [
        "",
        "## By Type",
        "",
        "| Type | Count | hit@1 | hit@3 | hit@5 | MRR |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for qtype, vals in perf["by_type"].items():
        lines.append(
            f"| {qtype} | {vals['count']} | {vals['hit_at_1']} | {vals['hit_at_3']} | {vals['hit_at_5']} | {vals['mrr']} |"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate Graphify on a question JSONL file")
    parser.add_argument("--questions", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--rebuild", action="store_true")
    parser.add_argument(
        "--rerank",
        choices=("none", "module-card"),
        default="none",
        help="Optional reranker over Graphify candidate pool.",
    )
    parser.add_argument("--candidate-limit", type=int, default=80)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    rows = read_jsonl(args.questions)
    kg = load_kg()
    graph, metadata = load_or_build_graphify(kg, rebuild=args.rebuild)

    predictions = []
    for row in rows:
        raw_candidates, _context = graphify_candidates(graph, kg, row["question"], limit=args.candidate_limit)
        candidates = [candidate for candidate in raw_candidates if is_rtl_candidate(candidate)][:10]
        if args.rerank == "module-card":
            candidate_pool = [candidate for candidate in raw_candidates if is_rtl_candidate(candidate)]
            candidates = rerank_by_module_card(kg, candidate_pool, row["question"])[:10]
        predictions.append({
            "task_id": row.get("task_id"),
            "level": row.get("level"),
            "type": row.get("type"),
            "question": row.get("question"),
            "gold_modules": row.get("gold_modules", []),
            "gold_paths": row.get("gold_paths", []),
            "gold_rank": rank_of(candidates, row),
            "topk": candidates[:5],
        })

    report = {
        "questions": str(args.questions),
        "graph": metadata.get("graph_path"),
        "rerank": args.rerank,
        "graphify_build": metadata,
        "performance": aggregate(rows, predictions),
    }
    (args.out_dir / "graphify_retrieval_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (args.out_dir / "graphify_predictions.json").write_text(
        json.dumps(predictions, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_markdown(args.out_dir / "graphify_retrieval_report.md", report)
    print(json.dumps({
        "status": "ok",
        "out_dir": str(args.out_dir),
        "questions": len(rows),
        "performance": report["performance"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
