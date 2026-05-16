#!/usr/bin/env python3
"""Build a verification-focused user QA benchmark for SVA and DV artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCE = ROOT / "out" / "spec_code_user_qa_benchmark" / "user_qa_questions_all.jsonl"
DEFAULT_OUT_DIR = ROOT / "out" / "spec_code_sva_dv_user_qa_benchmark"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
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


def code_node(row: dict[str, Any]) -> dict[str, Any]:
    nodes = row.get("gold_code_nodes") or []
    return nodes[0] if nodes else {}


def spec_node(row: dict[str, Any]) -> dict[str, Any]:
    nodes = row.get("gold_spec_nodes") or []
    return nodes[0] if nodes else {}


def artifact_kind(row: dict[str, Any]) -> str:
    node = code_node(row)
    path = str(node.get("source_file", "")).replace("\\", "/").lower()
    label = str(node.get("label", "")).lower()
    if "/dv/sva/" in path or "sva" in path or "bind" in label:
        return "sva"
    if "/dv/" in path or "/tb/" in path or path.endswith("/tb.sv") or "test" in path:
        return "dv_testbench"
    return "rtl"


def component(row: dict[str, Any]) -> str:
    for node in row.get("gold_spec_nodes", []):
        label = str(node.get("label", "")).replace("component:", "").strip()
        if label and not label.endswith((".hjson", ".md", ".sv", ".v")):
            return label
    return str(spec_node(row).get("label", "target block")).replace("component:", "").strip()


def enrich(row: dict[str, Any], index: int) -> dict[str, Any]:
    item = dict(row)
    kind = artifact_kind(row)
    spec = spec_node(row)
    code = code_node(row)
    comp = component(row)
    spec_label = spec.get("label", "")
    spec_path = str(spec.get("source_file", "")).replace("\\", "/")
    code_label = code.get("label", "")
    code_path = str(code.get("source_file", "")).replace("\\", "/")
    relation = ", ".join(row.get("gold_bridge_relations", [])) or "spec-code bridge"

    if kind == "sva":
        question = (
            f"`{comp}` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? "
            f"spec 문서 `{spec_label}`와 연결되는 SVA bind/assertion artifact를 같이 알려줘."
        )
        expected = (
            f"`{comp}` 검증에서는 spec `{spec_label}`와 SVA artifact `{code_label}`를 같이 봐야 합니다. "
            f"Spec anchor는 `{spec_path}`이고 SVA/code evidence는 `{code_path}`입니다. "
            f"KG 연결 근거는 `{relation}`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다."
        )
    else:
        question = (
            f"`{comp}` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. "
            f"관련 spec 문서와 DV/testbench code artifact를 같이 알려줘."
        )
        expected = (
            f"`{comp}` 검증에서는 spec `{spec_label}`와 DV/testbench artifact `{code_label}`를 같이 봐야 합니다. "
            f"Spec anchor는 `{spec_path}`이고 testbench/code evidence는 `{code_path}`입니다. "
            f"KG 연결 근거는 `{relation}`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다."
        )

    item["task_id"] = f"svadv_{index + 1:03d}"
    item["source_task_id"] = row.get("task_id", "")
    item["type"] = f"user_verification_{kind}"
    item["verification_artifact_kind"] = kind
    item["question"] = question
    item["expected_answer"] = expected
    item["answer_style"] = "Korean user-facing verification answer with spec and SVA/DV evidence"
    item["evaluation_focus"] = [
        "identify the spec/document anchor",
        "identify the SVA/DV/testbench artifact",
        "explain the verification traceability relation",
    ]
    item["notes"] = "Verification-focused user QA: SVA and DV/testbench artifacts are treated as first-class code evidence."
    return item


def write_catalog(path: Path, rows: list[dict[str, Any]]) -> None:
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["verification_artifact_kind"]] = counts.get(row["verification_artifact_kind"], 0) + 1
    lines = [
        "# SVA/DV User QA Benchmark",
        "",
        f"- Questions: {len(rows)}",
        "- Purpose: evaluate spec-to-verification traceability, including SVA bind/assertion and DV/testbench artifacts.",
        "",
        "| Artifact kind | Count |",
        "|---|---:|",
    ]
    for kind, count in sorted(counts.items()):
        lines.append(f"| {kind} | {count} |")
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

    source_rows = read_jsonl(args.source)
    selected = [row for row in source_rows if artifact_kind(row) in {"sva", "dv_testbench"}]
    rows = [enrich(row, index) for index, row in enumerate(selected)]
    args.out_dir.mkdir(parents=True, exist_ok=True)
    questions = args.out_dir / "sva_dv_user_qa_questions_all.jsonl"
    prompts = args.out_dir / "sva_dv_user_qa_prompts_only.jsonl"
    catalog = args.out_dir / "catalog.md"
    write_jsonl(questions, rows)
    write_jsonl(
        prompts,
        [
            {
                "task_id": row["task_id"],
                "type": row["type"],
                "question": row["question"],
                "expected_answer": row["expected_answer"],
            }
            for row in rows
        ],
    )
    write_catalog(catalog, rows)
    print(
        json.dumps(
            {
                "status": "ok",
                "questions": len(rows),
                "outputs": {
                    "questions": str(questions),
                    "prompts": str(prompts),
                    "catalog": str(catalog),
                },
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
