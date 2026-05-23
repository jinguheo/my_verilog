#!/usr/bin/env python3
"""Prepare an OpenKB workspace for Verilog retrieval/generation evaluation.

This script does not call OpenKB's LLM-backed `add` or `query` commands.  It
creates an OpenKB-ready directory with raw Markdown inputs, benchmark questions,
and run instructions so evaluation can start once an LLM API key is available.
"""
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUT = ROOT / "out" / "openkb_eval"


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


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


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def copy_if_exists(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    return True


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(cell).replace("|", "/") for cell in row) + " |")
    return "\n".join(lines)


def build_seed_summary(raw_dir: Path) -> dict[str, Any]:
    kg_summary_path = ROOT / "out" / "kg_full" / "kg_full_summary.json"
    retrieval_report_path = ROOT / "out" / "manticore_analysis" / "manticore_retrieval_report.json"
    frontend_report_path = ROOT / "out" / "frontend_compare" / "regex_vs_tree_sitter_eval.json"

    kg_summary = read_json(kg_summary_path) if kg_summary_path.exists() else {}
    retrieval_report = read_json(retrieval_report_path) if retrieval_report_path.exists() else {}
    frontend_report = read_json(frontend_report_path) if frontend_report_path.exists() else {}

    lines = [
        "# Verilog Knowledge Base Evaluation Snapshot",
        "",
        "This file is prepared as OpenKB raw input. It summarizes the current local RTL knowledge-base benchmark state.",
        "",
        "## KG Snapshot",
        "",
    ]
    if kg_summary:
        lines += [
            markdown_table(
                ["Metric", "Value"],
                [
                    ["modules", kg_summary.get("modules")],
                    ["ports", kg_summary.get("ports")],
                    ["instance_edges", kg_summary.get("instance_edges")],
                    ["total_nodes", kg_summary.get("total_nodes")],
                    ["total_edges", kg_summary.get("total_edges")],
                ],
            ),
            "",
            "## Project Modules",
            "",
            markdown_table(["Project", "Modules"], [[k, v] for k, v in kg_summary.get("projects", {}).items()]),
            "",
        ]
    if retrieval_report:
        rows = []
        for mode, metrics in retrieval_report.get("by_mode", {}).items():
            rows.append([
                mode,
                metrics.get("hit_at_1"),
                metrics.get("hit_at_3"),
                metrics.get("mrr"),
                metrics.get("weighted_hit_at_1"),
            ])
        lines += ["## Current Retrieval Metrics", "", markdown_table(["Mode", "hit@1", "hit@3", "MRR", "weighted hit@1"], rows), ""]
    if frontend_report:
        lines += [
            "## Regex vs Tree-Sitter Frontend",
            "",
            "Tree-sitter is the default frontend for methods 1-3. Regex remains a fallback.",
            "",
        ]
    path = raw_dir / "verilog_kb_eval_snapshot.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {
        "kg_summary": str(kg_summary_path) if kg_summary else None,
        "retrieval_report": str(retrieval_report_path) if retrieval_report else None,
        "frontend_report": str(frontend_report_path) if frontend_report else None,
        "raw_file": str(path),
    }


def build_generation_summary(raw_dir: Path) -> dict[str, Any]:
    summary_path = ROOT / "out" / "reports" / "four_method_generation_eval_full_detail.md"
    ctx_report_path = ROOT / "out" / "generation_context_eval" / "generation_context_eval_report.json"
    dst = raw_dir / "four_method_generation_eval_full_detail.md"
    copied = copy_if_exists(summary_path, dst)
    ctx = read_json(ctx_report_path) if ctx_report_path.exists() else {}
    return {
        "copied": copied,
        "source": str(summary_path) if summary_path.exists() else None,
        "raw_file": str(dst) if copied else None,
        "questions": ctx.get("questions"),
    }


def build_graphify_summary(raw_dir: Path) -> dict[str, Any]:
    src = ROOT / "graphify-out" / "GRAPH_REPORT.md"
    dst = raw_dir / "graphify_graph_report.md"
    copied = copy_if_exists(src, dst)
    return {"copied": copied, "source": str(src) if src.exists() else None, "raw_file": str(dst) if copied else None}


def build_question_set(out_dir: Path, max_questions: int) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []

    hard_gen = ROOT / "out" / "generation_context_eval" / "hard_generation_context_questions.jsonl"
    if hard_gen.exists():
        for row in read_jsonl(hard_gen)[:max_questions]:
            rows.append({
                "task_id": row.get("task_id"),
                "category": "generation_context",
                "question": row.get("question"),
                "gold_modules": row.get("gold_modules", []),
                "gold_paths": row.get("gold_paths", []),
                "scoring": "answer_contains_gold_module_name",
            })

    retrieval = ROOT / "out" / "multiaxis_benchmark" / "questions_all.jsonl"
    if retrieval.exists():
        for row in read_jsonl(retrieval):
            if len(rows) >= max_questions * 2:
                break
            if row.get("level") in {"L4", "L5"}:
                rows.append({
                    "task_id": f"retrieval_{len(rows) + 1:03d}",
                    "category": "rtl_retrieval",
                    "question": row.get("question"),
                    "gold_modules": row.get("gold_modules", []),
                    "gold_paths": row.get("gold_paths", []),
                    "scoring": "answer_contains_gold_module_name",
                })

    jsonl_path = out_dir / "openkb_eval_questions.jsonl"
    write_jsonl(jsonl_path, rows)

    md_lines = [
        "# OpenKB Evaluation Questions",
        "",
        "These questions are prepared for `openkb query`. Score a response as a hit when it names at least one gold module.",
        "",
        markdown_table(
            ["task_id", "category", "gold_modules", "question"],
            [[r["task_id"], r["category"], ", ".join(r["gold_modules"]), r["question"]] for r in rows],
        ),
    ]
    md_path = out_dir / "openkb_eval_questions.md"
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    return {"jsonl": str(jsonl_path), "markdown": str(md_path), "count": len(rows)}


def initialize_openkb_skeleton(kb_dir: Path) -> dict[str, Any]:
    """Create the same directory skeleton as `openkb init` without prompts."""
    openkb_dir = kb_dir / ".openkb"
    wiki_dir = kb_dir / "wiki"
    raw_dir = kb_dir / "raw"

    raw_dir.mkdir(parents=True, exist_ok=True)
    (wiki_dir / "sources" / "images").mkdir(parents=True, exist_ok=True)
    (wiki_dir / "summaries").mkdir(parents=True, exist_ok=True)
    (wiki_dir / "concepts").mkdir(parents=True, exist_ok=True)
    (wiki_dir / "explorations").mkdir(parents=True, exist_ok=True)
    openkb_dir.mkdir(parents=True, exist_ok=True)

    agents_src = ROOT / "tools" / "OpenKB" / "openkb" / "schema.py"
    agents_md = (
        "# OpenKB Wiki Instructions\n\n"
        "Maintain a concise Markdown wiki with sources, summaries, concepts, and explorations.\n"
    )
    if agents_src.exists():
        text = agents_src.read_text(encoding="utf-8", errors="replace")
        marker = 'AGENTS_MD = """'
        start = text.find(marker)
        if start >= 0:
            start += len(marker)
            end = text.find('"""', start)
            if end > start:
                agents_md = text[start:end]

    (wiki_dir / "AGENTS.md").write_text(agents_md, encoding="utf-8")
    (wiki_dir / "index.md").write_text(
        "# Knowledge Base Index\n\n## Documents\n\n## Concepts\n\n## Explorations\n",
        encoding="utf-8",
    )
    (wiki_dir / "log.md").write_text("# Operations Log\n\n", encoding="utf-8")
    (openkb_dir / "config.yaml").write_text(
        "model: gpt-5.4-mini\nlanguage: en\npageindex_threshold: 20\n",
        encoding="utf-8",
    )
    (openkb_dir / "hashes.json").write_text("{}\n", encoding="utf-8")
    (kb_dir / ".env.example").write_text("LLM_API_KEY=<your key>\n", encoding="utf-8")

    return {
        "kb_dir": str(kb_dir),
        "config": str(openkb_dir / "config.yaml"),
        "wiki_index": str(wiki_dir / "index.md"),
        "env_example": str(kb_dir / ".env.example"),
    }


def write_runbook(out_dir: Path, kb_dir: Path, question_info: dict[str, Any]) -> Path:
    runbook = out_dir / "OPENKB_EVAL_RUNBOOK.md"
    runbook.write_text(
        "\n".join([
            "# OpenKB Evaluation Runbook",
            "",
            "## Repository",
            "",
            "- Source: https://github.com/VectifyAI/OpenKB",
            "- Local checkout: `tools/OpenKB`",
            "- Installed into: `.venv-graphify`",
            "",
            "## Environment",
            "",
            "PowerShell:",
            "",
            "```powershell",
            "$env:PYTHONIOENCODING='utf-8'",
            "$env:LITELLM_LOCAL_MODEL_COST_MAP='True'",
            "$env:LLM_API_KEY='<your key>'",
            "```",
            "",
            "## Build OpenKB Wiki",
            "",
            "The KB skeleton is already initialized by `prepare_openkb_eval.py`.",
            "If you want to recreate it interactively, run `openkb init`; otherwise start from `openkb add`.",
            "",
            "```powershell",
            "cd out\\openkb_eval\\kb",
            "..\\..\\..\\.venv-graphify\\Scripts\\openkb.exe add .\\raw",
            "..\\..\\..\\.venv-graphify\\Scripts\\openkb.exe status",
            "```",
            "",
            "The raw files are already staged in:",
            "",
            f"```text\n{kb_dir / 'raw'}\n```",
            "",
            "## Query Evaluation",
            "",
            f"Questions: `{question_info['jsonl']}`",
            "",
            "For each row, run:",
            "",
            "```powershell",
            "..\\..\\..\\.venv-graphify\\Scripts\\openkb.exe query \"<question>\"",
            "```",
            "",
            "Score as hit@1-style success when the answer explicitly names at least one `gold_modules` value.",
            "",
            "## Notes",
            "",
            "- OpenKB is LLM-backed; evaluation cannot be completed offline without `LLM_API_KEY`.",
            "- OpenKB's value here is compiled wiki/context synthesis, not direct Verilog simulation.",
            "- Compare against existing Parser/LSP, Manticore, KG, and Graphify context-readiness reports.",
            "",
        ]),
        encoding="utf-8",
    )
    return runbook


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare OpenKB Verilog evaluation assets")
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--max-generation-questions", type=int, default=40)
    args = parser.parse_args()

    out_dir = args.out_dir.resolve()
    kb_dir = out_dir / "kb"
    raw_dir = kb_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    skeleton_info = initialize_openkb_skeleton(kb_dir)
    seed_info = build_seed_summary(raw_dir)
    generation_info = build_generation_summary(raw_dir)
    graphify_info = build_graphify_summary(raw_dir)
    question_info = build_question_set(out_dir, args.max_generation_questions)
    runbook_path = write_runbook(out_dir, kb_dir, question_info)

    manifest = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "openkb_repo": "https://github.com/VectifyAI/OpenKB",
        "local_checkout": str(ROOT / "tools" / "OpenKB"),
        "kb_dir": str(kb_dir),
        "raw_dir": str(raw_dir),
        "skeleton": skeleton_info,
        "seed_info": seed_info,
        "generation_info": generation_info,
        "graphify_info": graphify_info,
        "questions": question_info,
        "runbook": str(runbook_path),
        "status": "prepared_offline; run openkb add/query after setting LLM_API_KEY",
    }
    write_json(out_dir / "openkb_eval_manifest.json", manifest)
    print(json.dumps({"status": "ok", "out_dir": str(out_dir), "questions": question_info["count"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
