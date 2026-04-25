#!/usr/bin/env python3
import argparse
import json
from collections import defaultdict
from pathlib import Path

from retrieval_common import prepare_retrieval, rank_of, read_jsonl, retrieve, write_json


def difficulty_weight(difficulty):
    return {"easy": 1.0, "medium": 1.5, "hard": 2.0}[difficulty]


def aggregate(question_rows, runs_by_mode):
    report = {"by_mode": {}, "proxy_verilogeval": {}}
    for mode, runs in runs_by_mode.items():
        hit1 = hit3 = 0
        mrr = 0.0
        weighted = 0.0
        weighted_total = 0.0
        by_diff = defaultdict(lambda: {"count": 0, "hit1": 0, "hit3": 0, "mrr": 0.0})
        for row, run in zip(question_rows, runs):
            rank = run["gold_rank"]
            diff = row["difficulty"]
            weight = difficulty_weight(diff)
            weighted_total += weight
            by_diff[diff]["count"] += 1
            if rank == 1:
                hit1 += 1
                by_diff[diff]["hit1"] += 1
                weighted += weight
            if rank is not None and rank <= 3:
                hit3 += 1
                by_diff[diff]["hit3"] += 1
            if rank is not None:
                rr = 1.0 / rank
                mrr += rr
                by_diff[diff]["mrr"] += rr
        total = len(runs)
        report["by_mode"][mode] = {
            "count": total,
            "hit_at_1": round(hit1 / total, 4),
            "hit_at_3": round(hit3 / total, 4),
            "mrr": round(mrr / total, 4),
            "weighted_hit_at_1": round(weighted / weighted_total, 4) if weighted_total else 0.0,
            "by_difficulty": {
                diff: {
                    "count": vals["count"],
                    "hit_at_1": round(vals["hit1"] / vals["count"], 4),
                    "hit_at_3": round(vals["hit3"] / vals["count"], 4),
                    "mrr": round(vals["mrr"] / vals["count"], 4),
                }
                for diff, vals in sorted(by_diff.items())
            },
        }
        # This is a local proxy, not an official VerilogEval score.
        report["proxy_verilogeval"][mode] = {
            "status": "proxy_only",
            "score_100": round(
                100.0 * (
                    0.45 * report["by_mode"][mode]["weighted_hit_at_1"]
                    + 0.35 * report["by_mode"][mode]["hit_at_3"]
                    + 0.20 * report["by_mode"][mode]["mrr"]
                ),
                2,
            ),
        }
    return report


def build_markdown(report, adapter_status, retrieval_metadata):
    lines = [
        "# Retrieval Benchmark Report",
        "",
        "This report compares two retrieval conditions:",
        "",
        "- `kg`: uses field-aware module facts, labels, summaries, reverse graph hints, query expansion, and approved label context when available.",
        "- `baseline`: uses parser/LSP style file-local clues such as module name, path, ports, and instances.",
        "",
        "## Aggregate",
        "",
    ]
    for mode, metrics in report["by_mode"].items():
        lines.extend([
            f"### {mode}",
            "",
            f"- hit@1: {metrics['hit_at_1']}",
            f"- hit@3: {metrics['hit_at_3']}",
            f"- mrr: {metrics['mrr']}",
            f"- weighted hit@1: {metrics['weighted_hit_at_1']}",
            f"- proxy VerilogEval score (/100): {report['proxy_verilogeval'][mode]['score_100']}",
            "",
        ])
    lines.extend([
        "## Retrieval Inputs",
        "",
        f"- modules indexed: {retrieval_metadata['modules_indexed']}",
        f"- approved labels: {retrieval_metadata['approved_labels']['path'] or 'not found'}",
        f"- module labels added: {retrieval_metadata['approved_labels']['module_labels_added']}",
        f"- IP context labels added: {retrieval_metadata['approved_labels']['ip_context_labels_added']}",
        "",
        "## VerilogEval Adapter",
        "",
        f"- status: {adapter_status['status']}",
        f"- detail: {adapter_status['detail']}",
        "",
        "The proxy score is not an official VerilogEval number. It is a local readiness score derived from weighted retrieval accuracy.",
        "",
    ])
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", required=True)
    ap.add_argument("--benchmark", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--approved-labels")
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    questions = read_jsonl(args.benchmark)
    modules, idf_by_mode, known_projects, approved_summary = prepare_retrieval(
        args.seed,
        args.approved_labels,
    )
    for question in questions:
        question["_idf"] = idf_by_mode
        question["_known_projects"] = known_projects

    runs_by_mode = {"baseline": [], "kg": []}
    for question in questions:
        gold = question["gold_modules"][0]
        for mode in runs_by_mode:
            topk = retrieve(question, modules, mode, k=5)
            runs_by_mode[mode].append({
                "id": question["id"],
                "difficulty": question["difficulty"],
                "gold": gold,
                "gold_rank": rank_of(gold, topk),
                "topk": topk,
            })

    report = aggregate(questions, runs_by_mode)
    retrieval_metadata = {
        "modules_indexed": len(modules),
        "approved_labels": approved_summary,
    }
    adapter_status = {
        "status": "unavailable",
        "detail": "verilogeval package or runner was not available in this workspace; generated proxy-only score and adapter metadata.",
    }
    adapter = {
        "status": adapter_status["status"],
        "detail": adapter_status["detail"],
        "expected_inputs": {
            "questions_jsonl": str(Path(args.benchmark)),
            "predictions_json": str(out_dir / "predictions_for_verilogeval.json"),
        },
        "note": "Map each question to a model answer, then hand it to an external VerilogEval runner when available.",
    }

    predictions = []
    for mode, runs in runs_by_mode.items():
        for run in runs:
            predictions.append({
                "mode": mode,
                "id": run["id"],
                "gold": run["gold"],
                "prediction_top1": run["topk"][0]["name"] if run["topk"] else None,
                "prediction_top5": [row["name"] for row in run["topk"]],
                "gold_rank": run["gold_rank"],
            })

    write_json(out_dir / "retrieval_report.json", report)
    write_json(out_dir / "retrieval_metadata.json", retrieval_metadata)
    write_json(out_dir / "verilogeval_adapter.json", adapter)
    write_json(out_dir / "predictions_for_verilogeval.json", predictions)
    write_json(out_dir / "detailed_runs.json", runs_by_mode)
    with open(out_dir / "retrieval_report.md", "w", encoding="utf-8") as fp:
        fp.write(build_markdown(report, adapter_status, retrieval_metadata))
    print(json.dumps({
        "status": "ok",
        "out_dir": str(out_dir),
        "modules_indexed": len(modules),
        "approved_labels": approved_summary,
        "baseline_hit_at_1": report["by_mode"]["baseline"]["hit_at_1"],
        "kg_hit_at_1": report["by_mode"]["kg"]["hit_at_1"],
        "baseline_proxy_score": report["proxy_verilogeval"]["baseline"]["score_100"],
        "kg_proxy_score": report["proxy_verilogeval"]["kg"]["score_100"],
        "verilogeval_status": adapter_status["status"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
