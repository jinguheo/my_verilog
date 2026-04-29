#!/usr/bin/env python3
"""Run VerilogEval generation verification for parser_lsp, kg, and graphify modes."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from run_generation_verification import (
    PORTABLE_IVERILOG,
    PORTABLE_VVP,
    aggregate,
    default_tool,
    load_candidates,
    normalize_problem,
    read_jsonl,
    verify_one,
    write_outputs,
)


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BASE = ROOT / "out" / "verilogeval_generation" / "code-complete-iccad2023"
MODES = ("parser_lsp", "kg", "graphify")


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def mode_note(candidate_path: Path) -> str:
    try:
        first = read_jsonl(candidate_path)[0]
    except Exception:
        return "unknown"
    return str(first.get("candidate_source", "external"))


def run_mode(
    mode: str,
    problems_path: Path,
    candidates_path: Path,
    out_dir: Path,
    iverilog: str | None,
    vvp: str | None,
    timeout: int,
) -> dict[str, Any]:
    problem_rows = read_jsonl(problems_path)
    problems = [normalize_problem(row, idx) for idx, row in enumerate(problem_rows, 1)]
    candidates_by_id = load_candidates(problems, "external", candidates_path)

    results = []
    for problem in problems:
        candidate = candidates_by_id.get(problem.task_id)
        if not candidate:
            results.append({
                "task_id": problem.task_id,
                "level": problem.source.get("level", ""),
                "type": problem.source.get("type", problem.source.get("category", "")),
                "status": "NO_CANDIDATE",
                "syntax_status": "NOT_RUN",
                "detail": "no candidate found for task_id",
                "combined_path": "",
            })
            continue
        results.append(verify_one(problem, candidate, out_dir, iverilog, vvp, timeout))

    metadata = {
        "mode": mode,
        "problems": str(problems_path),
        "candidates": str(candidates_path),
        "candidate_source": mode_note(candidates_path),
        "iverilog": iverilog,
        "vvp": vvp,
        "timeout": timeout,
    }
    write_outputs(out_dir, results, metadata)
    summary = aggregate(results)
    summary["candidate_source"] = metadata["candidate_source"]
    return summary


def write_markdown(path: Path, task: str, summaries: dict[str, Any]) -> None:
    lines = [
        "# VerilogEval Generation Modes",
        "",
        f"- Task: {task}",
        "- Modes: parser_lsp, kg, graphify",
        "",
        "| Mode | Candidate source | Problems | PASS | Pass rate | Simulator pass rate |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for mode, summary in summaries.items():
        lines.append(
            f"| {mode} | {summary.get('candidate_source', '')} | {summary['total']} | "
            f"{summary['pass']} | {summary['pass_rate']} | {summary['simulated_pass_rate']} |"
        )
    lines += [
        "",
        "## Interpretation",
        "",
        "When candidate_source is `oracle_reference`, this is a harness sanity check, not a real comparison of generation quality.",
        "Replace each candidates_<mode>.jsonl file with RTL generated under that context strategy to get true mode scores.",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run VerilogEval generation verification by mode")
    parser.add_argument("--base-dir", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--iverilog", default=default_tool("iverilog", PORTABLE_IVERILOG))
    parser.add_argument("--vvp", default=default_tool("vvp", PORTABLE_VVP))
    parser.add_argument("--modes", nargs="+", default=list(MODES))
    args = parser.parse_args()

    problems_path = args.base_dir / "problems.jsonl"
    task = args.base_dir.name
    out_root = args.out_dir or (ROOT / "out" / "verilogeval_generation_eval" / task)
    summaries: dict[str, Any] = {}
    for mode in args.modes:
        candidates_path = args.base_dir / f"candidates_{mode}.jsonl"
        if not candidates_path.exists():
            raise FileNotFoundError(f"candidate file not found for mode {mode}: {candidates_path}")
        summaries[mode] = run_mode(
            mode,
            problems_path,
            candidates_path,
            out_root / mode,
            args.iverilog,
            args.vvp,
            args.timeout,
        )

    report = {
        "task": task,
        "modes": summaries,
        "note": "oracle_reference candidates validate the harness only; replace with generated RTL for real mode scores.",
    }
    write_json(out_root / "mode_summary.json", report)
    write_markdown(out_root / "mode_summary.md", task, summaries)
    print(json.dumps({"status": "ok", "out_dir": str(out_root), "task": task, "modes": summaries}, ensure_ascii=False))


if __name__ == "__main__":
    main()
