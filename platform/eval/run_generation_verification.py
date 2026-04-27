#!/usr/bin/env python3
"""Verify generated Verilog with compile/simulation tests.

The script accepts VerilogEval-like JSONL problems plus generated candidates.
It can also run in `--candidate-mode reference` for a smoke check using the
canonical solution as the generated answer.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUT = ROOT / "out" / "generation_eval"
DEFAULT_FIXTURE = ROOT / "platform" / "eval" / "fixtures" / "generation_smoke.jsonl"
PORTABLE_IVERILOG = ROOT / "tools" / "iverilog" / "bin" / "iverilog.exe"
PORTABLE_VVP = ROOT / "tools" / "iverilog" / "bin" / "vvp.exe"


@dataclass
class Problem:
    task_id: str
    prompt: str
    reference: str
    testbench: str
    source: dict[str, Any]


@dataclass
class Candidate:
    task_id: str
    code: str
    source: dict[str, Any]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"{path}:{line_no}: invalid JSONL row: {exc}") from exc
    return rows


def first_present(row: dict[str, Any], keys: tuple[str, ...], default: str = "") -> str:
    for key in keys:
        value = row.get(key)
        if value is not None:
            return str(value)
    return default


def normalize_problem(row: dict[str, Any], index: int) -> Problem:
    task_id = first_present(row, ("task_id", "problem_id", "id", "name"), f"problem_{index:04d}")
    prompt = first_present(row, ("prompt", "ifc", "module_header", "interface"))
    reference = first_present(row, ("canonical_solution", "reference", "ref", "solution", "answer"))
    testbench = first_present(row, ("test", "testbench", "tb", "test_bench"))
    if not prompt and "module" in reference:
        prompt = ""
    missing = [name for name, value in (("reference", reference), ("testbench", testbench)) if not value]
    if missing:
        raise SystemExit(f"{task_id}: missing required field(s): {', '.join(missing)}")
    return Problem(task_id=task_id, prompt=prompt, reference=reference, testbench=testbench, source=row)


def normalize_candidate(row: dict[str, Any], index: int) -> Candidate:
    task_id = first_present(row, ("task_id", "problem_id", "id", "name"), f"problem_{index:04d}")
    code = first_present(row, ("completion", "generated_code", "code", "rtl", "answer", "candidate"))
    if not code:
        raise SystemExit(f"{task_id}: missing candidate code field")
    return Candidate(task_id=task_id, code=code, source=row)


def strip_code_fences(text: str) -> str:
    text = text.strip()
    fence = re.match(r"^```(?:systemverilog|verilog|sv)?\s*(.*?)\s*```$", text, re.DOTALL | re.IGNORECASE)
    return fence.group(1).strip() if fence else text


def compose_design(prompt: str, completion: str) -> str:
    completion = strip_code_fences(completion)
    prompt = strip_code_fences(prompt)
    if re.search(r"\bmodule\s+\w+", completion):
        return completion.rstrip() + "\n"
    if prompt:
        return prompt.rstrip() + "\n" + completion.rstrip() + "\n"
    return completion.rstrip() + "\n"


def tree_sitter_syntax_ok(verilog_text: str) -> tuple[str, str]:
    try:
        import tree_sitter_verilog as tsverilog
        from tree_sitter import Language, Parser
    except Exception as exc:
        return "NOT_RUN", f"tree-sitter-verilog unavailable: {exc}"
    try:
        parser = Parser(Language(tsverilog.language()))
        tree = parser.parse(verilog_text.encode("utf-8", errors="replace"))
    except Exception as exc:
        return "ERROR", str(exc)
    return ("FAIL", "tree-sitter parse has errors") if tree.root_node.has_error else ("PASS", "")


def detect_fail_pattern(stdout: str, stderr: str) -> tuple[bool, str]:
    text = f"{stdout}\n{stderr}"
    mismatch = re.search(r"\bMismatches?\s*:\s*([0-9]+)", text, re.IGNORECASE)
    if mismatch and int(mismatch.group(1)) > 0:
        return True, f"Mismatches={mismatch.group(1)}"
    fail_patterns = [
        r"\bFAIL(?:ED)?\b",
        r"\bINCORRECT\b",
        r"\bERROR\b",
        r"\bWRONG\b",
    ]
    pass_patterns = [
        r"\bPASS(?:ED)?\b",
        r"\bSUCCESS\b",
        r"\bMismatches?\s*:\s*0\b",
    ]
    has_fail = any(re.search(pattern, text, re.IGNORECASE) for pattern in fail_patterns)
    has_pass = any(re.search(pattern, text, re.IGNORECASE) for pattern in pass_patterns)
    if has_fail and not has_pass:
        return True, "failure marker in simulator output"
    return False, ""


def run_command(cmd: list[str], cwd: Path, timeout: int) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=str(cwd),
        timeout=timeout,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        errors="replace",
    )


def verify_one(
    problem: Problem,
    candidate: Candidate,
    out_dir: Path,
    iverilog: str | None,
    vvp: str | None,
    timeout: int,
) -> dict[str, Any]:
    task_dir = out_dir / "work" / safe_name(problem.task_id)
    task_dir.mkdir(parents=True, exist_ok=True)
    design = compose_design(problem.prompt, candidate.code)
    combined = design + "\n" + problem.testbench.rstrip() + "\n"
    combined_path = task_dir / "combined.sv"
    vvp_path = task_dir / "sim.vvp"
    combined_path.write_text(combined, encoding="utf-8")

    syntax_status, syntax_detail = tree_sitter_syntax_ok(combined)
    result: dict[str, Any] = {
        "task_id": problem.task_id,
        "status": "",
        "syntax_status": syntax_status,
        "syntax_detail": syntax_detail,
        "compile_returncode": None,
        "sim_returncode": None,
        "detail": "",
        "combined_path": str(combined_path),
    }

    if not iverilog or not vvp:
        result["status"] = "TOOL_MISSING"
        result["detail"] = "iverilog/vvp not found on PATH; install Icarus Verilog to run functional simulation"
        return result

    compile_cmd = [iverilog, "-g2012", "-Wall", "-o", str(vvp_path), str(combined_path)]
    try:
        compile_proc = run_command(compile_cmd, task_dir, timeout)
    except subprocess.TimeoutExpired:
        result["status"] = "COMPILE_TIMEOUT"
        result["detail"] = f"compile timed out after {timeout}s"
        return result

    result["compile_returncode"] = compile_proc.returncode
    result["compile_stdout"] = compile_proc.stdout[-4000:]
    result["compile_stderr"] = compile_proc.stderr[-4000:]
    if compile_proc.returncode != 0:
        result["status"] = "COMPILE_FAIL"
        result["detail"] = compile_proc.stderr.strip().splitlines()[-1] if compile_proc.stderr.strip() else "iverilog failed"
        return result

    try:
        sim_proc = run_command([vvp, str(vvp_path)], task_dir, timeout)
    except subprocess.TimeoutExpired:
        result["status"] = "SIM_TIMEOUT"
        result["detail"] = f"simulation timed out after {timeout}s"
        return result

    result["sim_returncode"] = sim_proc.returncode
    result["sim_stdout"] = sim_proc.stdout[-4000:]
    result["sim_stderr"] = sim_proc.stderr[-4000:]
    failed, reason = detect_fail_pattern(sim_proc.stdout, sim_proc.stderr)
    if sim_proc.returncode != 0:
        result["status"] = "SIM_FAIL"
        result["detail"] = sim_proc.stderr.strip().splitlines()[-1] if sim_proc.stderr.strip() else "vvp failed"
    elif failed:
        result["status"] = "FUNCTION_FAIL"
        result["detail"] = reason
    else:
        result["status"] = "PASS"
        result["detail"] = "compiled and simulated without failure markers"
    return result


def safe_name(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", text).strip("._") or "task"


def default_tool(name: str, portable_path: Path) -> str | None:
    found = shutil.which(name)
    if found:
        return found
    return str(portable_path) if portable_path.exists() else None


def load_candidates(problems: list[Problem], mode: str, candidates_path: Path | None) -> dict[str, Candidate]:
    if mode == "reference":
        return {
            problem.task_id: Candidate(problem.task_id, problem.reference, {"mode": "reference"})
            for problem in problems
        }
    if mode == "external":
        if not candidates_path:
            raise SystemExit("--candidates is required with --candidate-mode external")
        rows = read_jsonl(candidates_path)
        candidates = [normalize_candidate(row, idx) for idx, row in enumerate(rows, 1)]
        return {candidate.task_id: candidate for candidate in candidates}
    raise SystemExit(f"unsupported candidate mode: {mode}")


def aggregate(results: list[dict[str, Any]]) -> dict[str, Any]:
    counts: dict[str, int] = {}
    for result in results:
        counts[result["status"]] = counts.get(result["status"], 0) + 1
    total = len(results)
    passed = counts.get("PASS", 0)
    attempted = total - counts.get("TOOL_MISSING", 0)
    return {
        "total": total,
        "pass": passed,
        "pass_rate": round(passed / total, 4) if total else 0.0,
        "attempted_with_simulator": attempted,
        "simulated_pass_rate": round(passed / attempted, 4) if attempted else 0.0,
        "status_counts": dict(sorted(counts.items())),
    }


def write_outputs(out_dir: Path, results: list[dict[str, Any]], metadata: dict[str, Any]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    report = {
        "metadata": metadata,
        "summary": aggregate(results),
        "results": results,
    }
    (out_dir / "generation_eval_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    csv_fields = [
        "task_id",
        "status",
        "syntax_status",
        "compile_returncode",
        "sim_returncode",
        "detail",
        "combined_path",
    ]
    with (out_dir / "generation_eval_results.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=csv_fields)
        writer.writeheader()
        for result in results:
            writer.writerow({field: result.get(field, "") for field in csv_fields})

    summary = report["summary"]
    lines = [
        "# Generation Verification Report",
        "",
        f"- Problems: {summary['total']}",
        f"- PASS: {summary['pass']}",
        f"- Pass rate: {summary['pass_rate']}",
        f"- Simulator-attempted pass rate: {summary['simulated_pass_rate']}",
        "",
        "## Status Counts",
        "",
        "| Status | Count |",
        "|---|---:|",
    ]
    for status, count in summary["status_counts"].items():
        lines.append(f"| {status} | {count} |")
    lines += [
        "",
        "## Results",
        "",
        "| Task | Status | Syntax | Detail |",
        "|---|---|---|---|",
    ]
    for result in results:
        lines.append(
            f"| {md_escape(result['task_id'])} | {result['status']} | {result['syntax_status']} | {md_escape(result.get('detail', ''))} |"
        )
    (out_dir / "generation_eval_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def md_escape(value: Any) -> str:
    return str(value).replace("\n", " ").replace("\r", " ").replace("|", "\\|")


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify generated Verilog candidates with VerilogEval-style tests")
    parser.add_argument("--problems", type=Path, default=DEFAULT_FIXTURE, help="JSONL problem file")
    parser.add_argument("--candidates", type=Path, help="JSONL generated candidate file")
    parser.add_argument("--candidate-mode", choices=("external", "reference"), default="external")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--iverilog", default=default_tool("iverilog", PORTABLE_IVERILOG))
    parser.add_argument("--vvp", default=default_tool("vvp", PORTABLE_VVP))
    args = parser.parse_args()

    problem_rows = read_jsonl(args.problems)
    problems = [normalize_problem(row, idx) for idx, row in enumerate(problem_rows, 1)]
    candidates_by_id = load_candidates(problems, args.candidate_mode, args.candidates)

    results: list[dict[str, Any]] = []
    for problem in problems:
        candidate = candidates_by_id.get(problem.task_id)
        if not candidate:
            results.append({
                "task_id": problem.task_id,
                "status": "NO_CANDIDATE",
                "syntax_status": "NOT_RUN",
                "detail": "no candidate found for task_id",
                "combined_path": "",
            })
            continue
        results.append(verify_one(problem, candidate, args.out, args.iverilog, args.vvp, args.timeout))

    metadata = {
        "problems": str(args.problems),
        "candidates": str(args.candidates) if args.candidates else None,
        "candidate_mode": args.candidate_mode,
        "iverilog": args.iverilog,
        "vvp": args.vvp,
        "timeout": args.timeout,
    }
    write_outputs(args.out, results, metadata)
    print(json.dumps({"summary": aggregate(results), "out": str(args.out)}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
