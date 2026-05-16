#!/usr/bin/env python3
"""Export question, gold answer, and retrieved answer details for spec-code KG eval."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_QUESTIONS = ROOT / "out" / "spec_code_retrieval_benchmark" / "questions_all.jsonl"
DEFAULT_PREDICTIONS = ROOT / "out" / "spec_code_graphify_variant_eval" / "spec_code_graphify_variant_predictions.json"
DEFAULT_OUT = ROOT / "out" / "spec_code_graphify_variant_eval"
VARIANTS = ("spec-only", "code-only", "spec-code")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def short_node(node: dict[str, Any]) -> str:
    label = str(node.get("label") or node.get("id") or "")
    path = str(node.get("source_file") or "")
    loc = str(node.get("source_location") or "")
    role = str(node.get("role") or node.get("file_type") or "")
    suffix = f":{loc}" if loc and loc != "L1" else ""
    if path:
        return f"{label} [{role}] @ {path}{suffix}"
    return f"{label} [{role}]"


def top_answer(topk: list[dict[str, Any]], limit: int = 5) -> str:
    if not topk:
        return "No retrieved nodes."
    parts = []
    for idx, node in enumerate(topk[:limit], 1):
        score = node.get("score", "")
        score_text = f", score={score}" if score != "" else ""
        parts.append(f"{idx}. {short_node(node)}{score_text}")
    return " | ".join(parts)


def top_labels(topk: list[dict[str, Any]], limit: int = 5) -> str:
    return "; ".join(str(node.get("label") or node.get("id") or "") for node in topk[:limit])


def hit(rank: int | None, k: int) -> str:
    return "Y" if rank is not None and rank <= k else "N"


def rank_text(rank: int | None) -> str:
    return str(rank) if rank is not None else "-"


def compact_gold(nodes: list[dict[str, Any]], limit: int = 4) -> str:
    if not nodes:
        return "-"
    shown = [short_node(node) for node in nodes[:limit]]
    if len(nodes) > limit:
        shown.append(f"... +{len(nodes) - limit} more")
    return " | ".join(shown)


def best_variant(predictions_by_variant: dict[str, dict[str, Any]]) -> str:
    for variant in ("spec-code", "code-only", "spec-only"):
        run = predictions_by_variant.get(variant, {})
        if run.get("joint_rank") is not None and run["joint_rank"] <= 10:
            return variant
    for variant in ("spec-code", "code-only", "spec-only"):
        run = predictions_by_variant.get(variant, {})
        if run.get("code_rank") is not None and run["code_rank"] <= 10:
            return variant
    for variant in ("spec-code", "spec-only", "code-only"):
        run = predictions_by_variant.get(variant, {})
        if run.get("spec_rank") is not None and run["spec_rank"] <= 10:
            return variant
    return "-"


def build_rows(questions: list[dict[str, Any]], predictions: dict[str, list[dict[str, Any]]]) -> list[dict[str, Any]]:
    pred_by_variant: dict[str, dict[str, dict[str, Any]]] = {}
    for variant, rows in predictions.items():
        pred_by_variant[variant] = {str(row["task_id"]): row for row in rows}

    details = []
    for question in questions:
        task_id = str(question["task_id"])
        by_variant = {variant: pred_by_variant.get(variant, {}).get(task_id, {}) for variant in VARIANTS}
        details.append(
            {
                "task_id": task_id,
                "level": question.get("level", ""),
                "type": question.get("type", ""),
                "question": question.get("question", ""),
                "expected_answer": question.get("expected_answer", ""),
                "gold_spec_answer": compact_gold(question.get("gold_spec_nodes", [])),
                "gold_code_answer": compact_gold(question.get("gold_code_nodes", [])),
                "gold_bridge_relations": ", ".join(question.get("gold_bridge_relations", [])),
                "gold_evidence": ", ".join(question.get("gold_evidence", [])),
                "best_variant_at_10": best_variant(by_variant),
                "variants": by_variant,
            }
        )
    return details


def write_jsonl(path: Path, details: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in details:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_csv(path: Path, details: list[dict[str, Any]]) -> None:
    fieldnames = [
        "task_id",
        "level",
        "type",
        "question",
        "expected_answer",
        "gold_spec_answer",
        "gold_code_answer",
        "gold_bridge_relations",
        "best_variant_at_10",
    ]
    for variant in VARIANTS:
        fieldnames.extend(
            [
                f"{variant}_spec_rank",
                f"{variant}_code_rank",
                f"{variant}_joint_rank",
                f"{variant}_hit_at_5",
                f"{variant}_top5_labels",
                f"{variant}_actual_answer_top5",
            ]
        )

    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in details:
            out = {key: row.get(key, "") for key in fieldnames if key in row}
            for variant in VARIANTS:
                run = row["variants"].get(variant, {})
                topk = run.get("topk", [])
                out[f"{variant}_spec_rank"] = rank_text(run.get("spec_rank"))
                out[f"{variant}_code_rank"] = rank_text(run.get("code_rank"))
                out[f"{variant}_joint_rank"] = rank_text(run.get("joint_rank"))
                out[f"{variant}_hit_at_5"] = (
                    f"spec={hit(run.get('spec_rank'), 5)}, code={hit(run.get('code_rank'), 5)}, "
                    f"joint={hit(run.get('joint_rank'), 5)}"
                )
                out[f"{variant}_top5_labels"] = top_labels(topk)
                out[f"{variant}_actual_answer_top5"] = top_answer(topk)
            writer.writerow(out)


def write_markdown(path: Path, details: list[dict[str, Any]]) -> None:
    lines = [
        "# Spec-Code KG Evaluation Details",
        "",
        f"- Questions: {len(details)}",
        "- Variants: spec-only, code-only, spec-code",
        "- Each item includes the benchmark question, gold answers, and the actual top retrieved nodes.",
        "",
        "## Summary Table",
        "",
        "| Task | Type | Best@10 | Gold Bridge |",
        "|---|---|---|---|",
    ]
    for row in details:
        lines.append(
            f"| {row['task_id']} | {row['type']} | {row['best_variant_at_10']} | "
            f"{row['gold_bridge_relations'] or '-'} |"
        )

    lines.extend(["", "## Detailed Questions", ""])
    for row in details:
        lines.extend(
            [
                f"### {row['task_id']} ({row['type']}, {row['level']})",
                "",
                f"**Question**: {row['question']}",
                "",
                f"**Expected answer**: {row['expected_answer'] or '-'}",
                "",
                f"**Gold spec answer**: {row['gold_spec_answer']}",
                "",
                f"**Gold code answer**: {row['gold_code_answer']}",
                "",
                f"**Gold bridge**: {row['gold_bridge_relations'] or '-'}",
                "",
                f"**Gold evidence terms**: {row['gold_evidence'] or '-'}",
                "",
                "| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |",
                "|---|---:|---:|---:|---|---|",
            ]
        )
        for variant in VARIANTS:
            run = row["variants"].get(variant, {})
            topk = top_answer(run.get("topk", []), limit=5).replace("|", "\\|")
            hit5 = (
                f"spec={hit(run.get('spec_rank'), 5)}, "
                f"code={hit(run.get('code_rank'), 5)}, "
                f"joint={hit(run.get('joint_rank'), 5)}"
            )
            lines.append(
                f"| {variant} | {rank_text(run.get('spec_rank'))} | {rank_text(run.get('code_rank'))} | "
                f"{rank_text(run.get('joint_rank'))} | {hit5} | {topk} |"
            )
        lines.append("")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--questions", type=Path, default=DEFAULT_QUESTIONS)
    parser.add_argument("--predictions", type=Path, default=DEFAULT_PREDICTIONS)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    questions = read_jsonl(args.questions)
    predictions = read_json(args.predictions)
    details = build_rows(questions, predictions)

    md_path = args.out_dir / "spec_code_question_answer_details.md"
    jsonl_path = args.out_dir / "spec_code_question_answer_details.jsonl"
    csv_path = args.out_dir / "spec_code_question_answer_details.csv"
    write_markdown(md_path, details)
    write_jsonl(jsonl_path, details)
    write_csv(csv_path, details)

    summary = {
        "status": "ok",
        "questions": len(details),
        "outputs": {
            "markdown": str(md_path),
            "jsonl": str(jsonl_path),
            "csv": str(csv_path),
        },
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
