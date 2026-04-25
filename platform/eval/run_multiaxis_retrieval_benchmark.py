#!/usr/bin/env python3
import argparse
import json
from collections import defaultdict
from pathlib import Path

from retrieval_common import prepare_retrieval, rank_of, read_jsonl, retrieve, write_json


def level_weight(level):
    return {"L1": 1.0, "L2": 1.2, "L3": 1.5, "L4": 1.8, "L5": 2.2}[level]


def aggregate(questions, runs_by_mode):
    report = {"by_mode": {}}
    for mode, runs in runs_by_mode.items():
        total = len(runs)
        hit1 = hit3 = 0
        mrr = 0.0
        weighted_hit = 0.0
        weighted_total = 0.0
        by_level = defaultdict(lambda: {"count": 0, "hit1": 0, "hit3": 0, "mrr": 0.0})
        by_type = defaultdict(lambda: {"count": 0, "hit1": 0, "hit3": 0, "mrr": 0.0})
        for question, run in zip(questions, runs):
            rank = run["gold_rank"]
            level = question["level"]
            qtype = question["type"]
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
            if rank is not None:
                rr = 1.0 / rank
                mrr += rr
                by_level[level]["mrr"] += rr
                by_type[qtype]["mrr"] += rr
        report["by_mode"][mode] = {
            "count": total,
            "hit_at_1": round(hit1 / total, 4),
            "hit_at_3": round(hit3 / total, 4),
            "mrr": round(mrr / total, 4),
            "weighted_hit_at_1": round(weighted_hit / weighted_total, 4),
            "by_level": {
                key: {
                    "count": vals["count"],
                    "hit_at_1": round(vals["hit1"] / vals["count"], 4),
                    "hit_at_3": round(vals["hit3"] / vals["count"], 4),
                    "mrr": round(vals["mrr"] / vals["count"], 4),
                }
                for key, vals in sorted(by_level.items())
            },
            "by_type": {
                key: {
                    "count": vals["count"],
                    "hit_at_1": round(vals["hit1"] / vals["count"], 4),
                    "hit_at_3": round(vals["hit3"] / vals["count"], 4),
                    "mrr": round(vals["mrr"] / vals["count"], 4),
                }
                for key, vals in sorted(by_type.items())
            },
        }
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", required=True)
    ap.add_argument("--questions", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--approved-labels")
    args = ap.parse_args()

    questions = read_jsonl(args.questions)
    modules, idf_by_mode, known_projects, approved_summary = prepare_retrieval(
        args.seed,
        args.approved_labels,
    )
    for question in questions:
        question["_idf"] = idf_by_mode
        question["_known_projects"] = known_projects

    runs_by_mode = {"baseline": [], "kg": []}
    for question in questions:
        for mode in runs_by_mode:
            topk = retrieve(question, modules, mode, 5)
            runs_by_mode[mode].append({
                "level": question["level"],
                "type": question["type"],
                "gold_modules": question["gold_modules"],
                "gold_rank": rank_of(question["gold_modules"], topk),
                "topk": topk,
            })

    report = aggregate(questions, runs_by_mode)
    retrieval_metadata = {
        "modules_indexed": len(modules),
        "approved_labels": approved_summary,
    }
    out_dir = Path(args.out_dir)
    write_json(out_dir / "multiaxis_report.json", report)
    write_json(out_dir / "multiaxis_metadata.json", retrieval_metadata)
    write_json(out_dir / "multiaxis_detailed_runs.json", runs_by_mode)
    print(json.dumps({
        "status": "ok",
        "out_dir": str(out_dir),
        "modules_indexed": len(modules),
        "approved_labels": approved_summary,
        "baseline_hit_at_1": report["by_mode"]["baseline"]["hit_at_1"],
        "kg_hit_at_1": report["by_mode"]["kg"]["hit_at_1"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
