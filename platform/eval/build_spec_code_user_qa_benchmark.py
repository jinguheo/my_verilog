#!/usr/bin/env python3
"""Build a user-style QA benchmark from the spec-code traceability benchmark."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCE = ROOT / "out" / "spec_code_retrieval_benchmark" / "questions_all.jsonl"
DEFAULT_OUT_DIR = ROOT / "out" / "spec_code_user_qa_benchmark"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def clean_label(label: str) -> str:
    return label.replace("component:", "").replace("topic:", "").strip()


def norm_path(path: str) -> str:
    return path.replace("\\", "/")


def path_tail(path: str, depth: int = 5) -> str:
    parts = [part for part in re.split(r"[\\/]+", path) if part]
    return "/".join(parts[-depth:]) if parts else path


def first_node(row: dict[str, Any], key: str) -> dict[str, Any]:
    values = row.get(key, [])
    return values[0] if values else {}


def component_from(row: dict[str, Any]) -> str:
    for node in row.get("gold_spec_nodes", []):
        label = clean_label(str(node.get("label", "")))
        if label and not label.endswith((".hjson", ".md", ".sv", ".v")):
            return label
    spec = first_node(row, "gold_spec_nodes")
    label = clean_label(str(spec.get("label", "")))
    if label:
        return label
    source = norm_path(str(spec.get("source_file", "")))
    for marker in ("/ip_autogen/", "/hw/ip/", "/ip_templates/"):
        if marker in source:
            return source.split(marker, 1)[1].split("/", 1)[0]
    return "the target block"


def answer_text(row: dict[str, Any]) -> str:
    spec = first_node(row, "gold_spec_nodes")
    code = first_node(row, "gold_code_nodes")
    component = component_from(row)
    spec_label = clean_label(str(spec.get("label", "")))
    code_label = clean_label(str(code.get("label", "")))
    spec_path = norm_path(str(spec.get("source_file", "")))
    code_path = norm_path(str(code.get("source_file", "")))
    relation = ", ".join(row.get("gold_bridge_relations", [])) or "spec-code bridge"

    return (
        f"`{component}`는 spec 문서 `{spec_label}`와 code artifact `{code_label}`를 같이 봐야 합니다. "
        f"Spec 근거는 `{spec_path}`이고, 구현/검증 쪽 근거는 `{code_path}`입니다. "
        f"KG에서는 `{relation}` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다."
    )


def user_question(row: dict[str, Any], index: int) -> tuple[str, str]:
    spec = first_node(row, "gold_spec_nodes")
    code = first_node(row, "gold_code_nodes")
    component = component_from(row)
    spec_label = clean_label(str(spec.get("label", "")))
    code_label = clean_label(str(code.get("label", "")))
    spec_tail = path_tail(str(spec.get("source_file", "")), 5)
    code_tail = path_tail(str(code.get("source_file", "")), 5)

    templates = [
        (
            "user_spec_to_code_explain",
            f"`{component}` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `{spec_label}` 쪽이고, 구현 근거 파일도 같이 알려줘.",
        ),
        (
            "user_code_to_spec_why",
            f"`{code_label}`가 왜 필요한지 spec 기준으로 설명해줘. `{code_tail}`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.",
        ),
        (
            "user_review_trace",
            f"리뷰할 때 `{component}`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.",
        ),
        (
            "user_verification_coverage",
            f"`{component}` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `{spec_tail}`와 연결된 code 쪽도 알려줘.",
        ),
        (
            "user_change_impact",
            f"`{component}` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.",
        ),
        (
            "user_disambiguation",
            f"이름만 보면 헷갈리는데 `{component}`는 `{spec_tail}` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.",
        ),
    ]
    return templates[index % len(templates)]


def convert(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for idx, row in enumerate(rows):
        qtype, question = user_question(row, idx)
        item = dict(row)
        item["task_id"] = f"userqa_{idx + 1:03d}"
        item["source_task_id"] = row.get("task_id", "")
        item["type"] = qtype
        item["original_traceability_type"] = row.get("type", "")
        item["question"] = question
        item["expected_answer"] = answer_text(row)
        item["answer_style"] = "Korean user-facing answer with spec evidence, code evidence, and bridge rationale"
        item["evaluation_focus"] = [
            "answer should identify a spec/document anchor",
            "answer should identify a code/RTL/DV artifact",
            "answer should explain why spec-code linkage matters",
        ]
        item["notes"] = "User-style QA: intended to evaluate retrieval plus natural answer grounding, not only graph node lookup."
        out.append(item)
    return out


def write_prompts(path: Path, rows: list[dict[str, Any]]) -> None:
    prompts = [
        {
            "task_id": row["task_id"],
            "type": row["type"],
            "question": row["question"],
            "expected_answer": row["expected_answer"],
        }
        for row in rows
    ]
    write_jsonl(path, prompts)


def write_catalog(path: Path, rows: list[dict[str, Any]]) -> None:
    by_type: dict[str, int] = {}
    for row in rows:
        by_type[row["type"]] = by_type.get(row["type"], 0) + 1

    lines = [
        "# Spec-Code User QA Benchmark",
        "",
        f"- Questions: {len(rows)}",
        "- Language: Korean user-style questions",
        "- Purpose: evaluate whether answers can combine spec evidence and code evidence.",
        "",
        "## Distribution",
        "",
        "| Type | Count |",
        "|---|---:|",
    ]
    for qtype, count in sorted(by_type.items()):
        lines.append(f"| {qtype} | {count} |")

    lines.extend(["", "## Sample", ""])
    for row in rows[:10]:
        lines.extend(
            [
                f"### {row['task_id']} - {row['type']}",
                "",
                f"**Question**: {row['question']}",
                "",
                f"**Expected answer**: {row['expected_answer']}",
                "",
            ]
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    args = parser.parse_args()

    rows = convert(read_jsonl(args.source))
    args.out_dir.mkdir(parents=True, exist_ok=True)

    questions_path = args.out_dir / "user_qa_questions_all.jsonl"
    prompts_path = args.out_dir / "user_qa_prompts_only.jsonl"
    catalog_path = args.out_dir / "catalog.md"
    write_jsonl(questions_path, rows)
    write_prompts(prompts_path, rows)
    write_catalog(catalog_path, rows)

    print(
        json.dumps(
            {
                "status": "ok",
                "questions": len(rows),
                "outputs": {
                    "questions": str(questions_path),
                    "prompts": str(prompts_path),
                    "catalog": str(catalog_path),
                },
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
