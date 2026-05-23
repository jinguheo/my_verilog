#!/usr/bin/env python3
"""Run and score OpenKB answers for prepared Verilog evaluation questions.

This script expects `platform/eval/prepare_openkb_eval.py` to have created
`out/openkb_eval/kb` and `out/openkb_eval/openkb_eval_questions.jsonl`.

It calls the OpenKB CLI for each question and scores a hit when the answer
contains one of the gold module names.  Because OpenKB is LLM-backed, set
`LLM_API_KEY` before running.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUT = ROOT / "out" / "openkb_eval"
DEFAULT_QUESTIONS = DEFAULT_OUT / "openkb_eval_questions.jsonl"
DEFAULT_KB = DEFAULT_OUT / "kb"
DEFAULT_OPENKB = ROOT / ".venv-graphify" / "Scripts" / "openkb.exe"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def score_answer(answer: str, gold_modules: list[str]) -> dict[str, Any]:
    answer_l = answer.lower()
    hits = [module for module in gold_modules if module and module.lower() in answer_l]
    return {
        "hit": bool(hits),
        "matched_modules": hits,
    }


def run_query(openkb: Path, kb_dir: Path, question: str, timeout: int) -> dict[str, Any]:
    env = dict(os.environ)
    env.setdefault("PYTHONIOENCODING", "utf-8")
    env.setdefault("LITELLM_LOCAL_MODEL_COST_MAP", "True")
    proc = subprocess.run(
        [str(openkb), "--kb-dir", str(kb_dir), "query", question],
        cwd=str(ROOT),
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        errors="replace",
        timeout=timeout,
    )
    return {
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(rows)
    hits = sum(1 for row in rows if row.get("hit"))
    by_category: dict[str, dict[str, Any]] = {}
    for category in sorted({row.get("category", "unknown") for row in rows}):
        subset = [row for row in rows if row.get("category", "unknown") == category]
        count = len(subset)
        passed = sum(1 for row in subset if row.get("hit"))
        by_category[category] = {
            "count": count,
            "hits": passed,
            "hit_rate": round(passed / count, 4) if count else 0.0,
        }
    status_counts = Counter(row.get("status", "unknown") for row in rows)
    return {
        "total": total,
        "hits": hits,
        "hit_rate": round(hits / total, 4) if total else 0.0,
        "status_counts": dict(sorted(status_counts.items())),
        "by_category": by_category,
    }


def write_markdown(path: Path, summary: dict[str, Any], rows: list[dict[str, Any]]) -> None:
    lines = [
        "# OpenKB Verilog Evaluation Report",
        "",
        f"- Questions: {summary['total']}",
        f"- Hits: {summary['hits']}",
        f"- Hit rate: {summary['hit_rate']}",
        "",
        "## By Category",
        "",
        "| Category | Count | Hits | Hit rate |",
        "|---|---:|---:|---:|",
    ]
    for category, metrics in summary["by_category"].items():
        lines.append(f"| {category} | {metrics['count']} | {metrics['hits']} | {metrics['hit_rate']} |")
    lines += [
        "",
        "## Details",
        "",
        "| task_id | category | hit | matched_modules | gold_modules |",
        "|---|---|---:|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row.get('task_id')} | {row.get('category')} | {row.get('hit')} | "
            f"{', '.join(row.get('matched_modules', []))} | {', '.join(row.get('gold_modules', []))} |"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run OpenKB query evaluation")
    parser.add_argument("--questions", type=Path, default=DEFAULT_QUESTIONS)
    parser.add_argument("--kb-dir", type=Path, default=DEFAULT_KB)
    parser.add_argument("--openkb", type=Path, default=DEFAULT_OPENKB)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT / "runs")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    questions = read_jsonl(args.questions)
    if args.limit:
        questions = questions[: args.limit]

    if args.dry_run:
        print(json.dumps({
            "status": "dry_run",
            "questions": len(questions),
            "kb_dir": str(args.kb_dir),
            "openkb": str(args.openkb),
            "llm_api_key_present": bool(os.environ.get("LLM_API_KEY")),
        }, ensure_ascii=False))
        return

    rows: list[dict[str, Any]] = []
    for idx, question in enumerate(questions, 1):
        task_id = question.get("task_id", f"q{idx:04d}")
        payload = run_query(args.openkb, args.kb_dir, question["question"], args.timeout)
        status = "ok" if payload["returncode"] == 0 else "cli_error"
        score = score_answer(payload["stdout"], question.get("gold_modules", []))
        rows.append({
            "task_id": task_id,
            "category": question.get("category", ""),
            "question": question.get("question", ""),
            "gold_modules": question.get("gold_modules", []),
            "status": status,
            "hit": score["hit"] if status == "ok" else False,
            "matched_modules": score["matched_modules"] if status == "ok" else [],
            "stdout": payload["stdout"],
            "stderr": payload["stderr"],
            "returncode": payload["returncode"],
        })
        print(json.dumps({"idx": idx, "task_id": task_id, "status": status, "hit": rows[-1]["hit"]}, ensure_ascii=False))

    summary = aggregate(rows)
    write_json(args.out_dir / "openkb_eval_report.json", {"summary": summary, "rows": rows})
    write_markdown(args.out_dir / "openkb_eval_report.md", summary, rows)
    print(json.dumps({"status": "ok", "summary": summary, "out_dir": str(args.out_dir)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
