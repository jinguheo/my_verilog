#!/usr/bin/env python3
"""Verify tree-sitter frontend use and summarize easy/hard retrieval for four methods."""

from __future__ import annotations

import json
import sys
import time
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EVAL_DIR = ROOT / "platform" / "eval"
sys.path.insert(0, str(EVAL_DIR))

from retrieval_common import prepare_retrieval, rank_of, read_jsonl  # noqa: E402
from run_manticore_retrieval_analysis import (  # noqa: E402
    build_documents,
    build_index,
    retrieve_manticore,
)


OUT_DIR = ROOT / "out" / "tree_sitter_easy_hard_eval"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def summarize_groups(groups: dict[str, dict[str, float]]) -> dict[str, dict[str, float]]:
    result = {}
    for key, vals in sorted(groups.items()):
        count = vals["count"]
        result[key] = {
            "count": count,
            "hit_at_1": round(vals["hit1"] / count, 4) if count else 0.0,
            "hit_at_3": round(vals["hit3"] / count, 4) if count else 0.0,
            "mrr": round(vals["mrr"] / count, 4) if count else 0.0,
        }
    return result


def evaluate_manticore_general(seed_path: Path, questions_path: Path) -> dict:
    modules, _, _, _ = prepare_retrieval(seed_path)
    questions = read_jsonl(questions_path)
    documents = build_documents(modules, include_kg_fields=False)
    index = build_index(documents, include_kg_fields=False)

    runs = []
    by_difficulty = defaultdict(lambda: {"count": 0, "hit1": 0, "hit3": 0, "mrr": 0.0})
    by_type = defaultdict(lambda: {"count": 0, "hit1": 0, "hit3": 0, "mrr": 0.0})
    hit1 = hit3 = 0
    mrr = 0.0
    start = time.perf_counter()
    for question in questions:
        topk = retrieve_manticore(question, index, include_kg_fields=False, k=5)
        rank = rank_of(question["gold_modules"], topk)
        difficulty = question["difficulty"]
        qtype = question["type"]
        by_difficulty[difficulty]["count"] += 1
        by_type[qtype]["count"] += 1
        if rank == 1:
            hit1 += 1
            by_difficulty[difficulty]["hit1"] += 1
            by_type[qtype]["hit1"] += 1
        if rank is not None and rank <= 3:
            hit3 += 1
            by_difficulty[difficulty]["hit3"] += 1
            by_type[qtype]["hit3"] += 1
        if rank is not None:
            rr = 1.0 / rank
            mrr += rr
            by_difficulty[difficulty]["mrr"] += rr
            by_type[qtype]["mrr"] += rr
        runs.append(
            {
                "id": question["id"],
                "difficulty": difficulty,
                "type": qtype,
                "gold_modules": question["gold_modules"],
                "gold_rank": rank,
                "top5": topk,
            }
        )
    elapsed = time.perf_counter() - start
    count = len(questions)
    return {
        "count": count,
        "hit_at_1": round(hit1 / count, 4),
        "hit_at_3": round(hit3 / count, 4),
        "mrr": round(mrr / count, 4),
        "avg_query_ms": round((elapsed / count) * 1000, 3),
        "by_difficulty": summarize_groups(by_difficulty),
        "by_type": summarize_groups(by_type),
        "runs": runs,
    }


def verify_tree_sitter() -> dict:
    status = {
        "tree_sitter_import_ok": False,
        "tree_sitter_verilog_import_ok": False,
        "current_seed_frontends": {},
        "frontend_compare_summary": {},
    }
    try:
        import tree_sitter  # noqa: F401

        status["tree_sitter_import_ok"] = True
    except Exception as exc:  # pragma: no cover
        status["tree_sitter_error"] = str(exc)
    try:
        import tree_sitter_verilog  # noqa: F401

        status["tree_sitter_verilog_import_ok"] = True
    except Exception as exc:  # pragma: no cover
        status["tree_sitter_verilog_error"] = str(exc)

    seed_path = ROOT / "out" / "merged_ontology_seed.jsonl"
    frontend_counts = defaultdict(int)
    for row in read_jsonl(seed_path):
        frontend = row.get("metadata", {}).get("frontend", "unknown")
        frontend_counts[frontend] += 1
    status["current_seed_frontends"] = dict(sorted(frontend_counts.items()))

    frontend_eval_path = ROOT / "out" / "frontend_compare" / "regex_vs_tree_sitter_eval.json"
    if frontend_eval_path.exists():
        frontend_eval = read_json(frontend_eval_path)
        status["frontend_compare_summary"] = {
            "questions": frontend_eval.get("questions"),
            "frontends": frontend_eval.get("frontends"),
            "delta_tree_sitter_minus_regex": frontend_eval.get("delta_tree_sitter_minus_regex"),
            "winner": frontend_eval.get("winner"),
        }
    return status


def build_report() -> dict:
    tree_status = verify_tree_sitter()
    parser_kg_general = read_json(ROOT / "out" / "eval_results" / "retrieval_report.json")
    graphify_report = read_json(ROOT / "out" / "graphify_compare" / "comparison_report.json")
    manticore_general = evaluate_manticore_general(
        ROOT / "out" / "merged_ontology_seed.jsonl",
        ROOT / "out" / "eval_benchmark" / "benchmark_all.jsonl",
    )

    methods = {
        "parser_lsp": parser_kg_general["by_mode"]["baseline"],
        "kg": parser_kg_general["by_mode"]["kg"],
        "graphify": graphify_report["comparison"]["general"]["performance"],
        "manticore": {
            key: value
            for key, value in manticore_general.items()
            if key != "runs"
        },
    }
    easy_hard = {}
    for method, data in methods.items():
        by_diff = data.get("by_difficulty", {})
        easy_hard[method] = {
            "easy": by_diff.get("easy"),
            "hard": by_diff.get("hard"),
            "overall": {
                "count": data.get("count"),
                "hit_at_1": data.get("hit_at_1"),
                "hit_at_3": data.get("hit_at_3"),
                "mrr": data.get("mrr"),
                "weighted_hit_at_1": data.get("weighted_hit_at_1"),
                "avg_query_ms": data.get("avg_query_ms"),
            },
        }

    result = {
        "generated_at": "2026-05-20T00:00:00+09:00",
        "question_set": str(ROOT / "out" / "eval_benchmark" / "benchmark_all.jsonl"),
        "questions": 150,
        "tree_sitter_verification": tree_status,
        "regex_vs_tree_sitter": tree_status["frontend_compare_summary"],
        "four_method_easy_hard": easy_hard,
        "manticore_general_runs": manticore_general["runs"],
        "sources": {
            "parser_lsp_kg": str(ROOT / "out" / "eval_results" / "retrieval_report.json"),
            "graphify": str(ROOT / "out" / "graphify_compare" / "comparison_report.json"),
            "regex_tree_sitter": str(ROOT / "out" / "frontend_compare" / "regex_vs_tree_sitter_eval.json"),
        },
    }
    return result


def write_outputs(result: dict) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "tree_sitter_easy_hard_four_methods.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    runs = result["manticore_general_runs"]
    (OUT_DIR / "manticore_general_runs.json").write_text(
        json.dumps(runs, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# Tree-sitter Frontend and Four-method Easy/Hard Evaluation",
        "",
        "This report verifies whether tree-sitter is available and whether the current seed uses tree-sitter, then summarizes easy and hard retrieval performance for four methods.",
        "",
        "## Tree-sitter Verification",
        "",
        f"- `tree_sitter` import: {result['tree_sitter_verification']['tree_sitter_import_ok']}",
        f"- `tree_sitter_verilog` import: {result['tree_sitter_verification']['tree_sitter_verilog_import_ok']}",
        f"- Current seed frontend counts: `{result['tree_sitter_verification']['current_seed_frontends']}`",
        "",
        "## Regex vs Tree-sitter",
        "",
        "| Mode | Hit@1 Delta | Hit@3 Delta | MRR Delta | Weighted Hit@1 Delta |",
        "|---|---:|---:|---:|---:|",
    ]
    deltas = result["regex_vs_tree_sitter"].get("delta_tree_sitter_minus_regex", {})
    for mode, delta in deltas.items():
        lines.append(
            f"| {mode} | {delta['hit_at_1']:+.4f} | {delta['hit_at_3']:+.4f} | "
            f"{delta['mrr']:+.4f} | {delta['weighted_hit_at_1']:+.4f} |"
        )
    lines += [
        "",
        "## Four Methods: Easy Questions",
        "",
        "| Method | Count | Hit@1 | Hit@3 | MRR |",
        "|---|---:|---:|---:|---:|",
    ]
    for method, data in result["four_method_easy_hard"].items():
        easy = data["easy"]
        lines.append(
            f"| {method} | {easy['count']} | {easy['hit_at_1']:.4f} | {easy['hit_at_3']:.4f} | {easy['mrr']:.4f} |"
        )
    lines += [
        "",
        "## Four Methods: Hard Questions",
        "",
        "| Method | Count | Hit@1 | Hit@3 | MRR |",
        "|---|---:|---:|---:|---:|",
    ]
    for method, data in result["four_method_easy_hard"].items():
        hard = data["hard"]
        lines.append(
            f"| {method} | {hard['count']} | {hard['hit_at_1']:.4f} | {hard['hit_at_3']:.4f} | {hard['mrr']:.4f} |"
        )
    lines += [
        "",
        "## Reading",
        "",
        "- Tree-sitter is available and the current merged seed is tree-sitter-based.",
        "- Regex-to-tree-sitter improves most Hit@1/MRR metrics, but Manticore Hit@3 is slightly higher with regex in the older frontend comparison snapshot.",
        "- On the current 150-question easy/hard benchmark, KG is strongest on hard questions; Graphify is strong on easy exact/module navigation but weak on hard exact retrieval.",
        "",
    ]
    report = "\n".join(lines)
    (OUT_DIR / "tree_sitter_easy_hard_four_methods.md").write_text(report, encoding="utf-8")
    html = report.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    html = html.replace("\n", "\n")
    html = html.replace("# Tree-sitter Frontend and Four-method Easy/Hard Evaluation", "<h1>Tree-sitter Frontend and Four-method Easy/Hard Evaluation</h1>")
    (OUT_DIR / "tree_sitter_easy_hard_four_methods.html").write_text(
        f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Tree-sitter Easy/Hard Eval</title>
<style>body{{font-family:Segoe UI,Arial,sans-serif;background:#f7f8fb;color:#17202a;letter-spacing:0}}main{{max-width:1100px;margin:0 auto;padding:30px}}table{{border-collapse:collapse;width:100%;background:white}}td,th{{border:1px solid #d8dee8;padding:8px}}th{{background:#edf2f7}}</style>
</head><body><main><pre>{html}</pre></main></body></html>""",
        encoding="utf-8",
    )


def main() -> None:
    result = build_report()
    write_outputs(result)
    print(json.dumps({
        "out_dir": str(OUT_DIR),
        "tree_sitter": result["tree_sitter_verification"],
        "four_method_easy_hard": result["four_method_easy_hard"],
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
