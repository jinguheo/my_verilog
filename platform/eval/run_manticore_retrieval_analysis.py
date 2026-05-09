#!/usr/bin/env python3
"""Analyze parser+LSP retrieval with a Manticore Search-style index.

This script does not require a running Manticore server.  It models the part of
Manticore Search that matters for the current benchmark: full-text indexing over
parser/LSP fields with BM25-style ranking, exact field boosts, and an optional
hybrid variant that indexes KG fields too.  It also writes a Manticore SQL schema
and JSONL documents so the same corpus can be loaded into a real Manticore
instance later.
"""
from __future__ import annotations

import argparse
import json
import math
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from retrieval_common import (
    build_reverse_graph,
    extract_anchors,
    prepare_retrieval,
    rank_of,
    read_jsonl,
    retrieve,
    token_set,
    tokenize,
    write_json,
)


PARSER_LSP_FIELDS = {
    "name": 12.0,
    "path_file": 7.0,
    "ports": 4.5,
    "instances": 5.5,
    "instance_names": 2.5,
    "project": 1.2,
    "path": 1.0,
}

HYBRID_EXTRA_FIELDS = {
    "labels": 2.8,
    "summary": 1.5,
    "parents": 2.0,
}


def level_weight(level: str) -> float:
    return {"L1": 1.0, "L2": 1.2, "L3": 1.5, "L4": 1.8, "L5": 2.2}[level]


def field_text(module: dict[str, Any], child_to_parents: dict[str, list[str]]) -> dict[str, str]:
    path = Path(module.get("path", ""))
    return {
        "name": module.get("name", ""),
        "project": module.get("project", ""),
        "path": module.get("path", ""),
        "path_file": path.name,
        "ports": " ".join(port.get("name", "") for port in module.get("ports", [])),
        "instances": " ".join(inst.get("type", "") for inst in module.get("instances", [])),
        "instance_names": " ".join(inst.get("name", "") for inst in module.get("instances", [])),
        "labels": " ".join(module.get("labels", [])),
        "summary": module.get("summary", ""),
        "parents": " ".join(child_to_parents.get(module.get("name", ""), [])),
    }


def build_documents(modules: list[dict[str, Any]], include_kg_fields: bool) -> list[dict[str, Any]]:
    child_to_parents = build_reverse_graph(modules)
    weights = dict(PARSER_LSP_FIELDS)
    if include_kg_fields:
        weights.update(HYBRID_EXTRA_FIELDS)

    documents = []
    for idx, module in enumerate(modules, 1):
        text_by_field = field_text(module, child_to_parents)
        token_counts = {
            field: Counter(tokenize(text_by_field.get(field, "")))
            for field in weights
        }
        exact = {
            "name": module.get("name", "").lower(),
            "project": module.get("project", "").lower(),
            "path_file": Path(module.get("path", "")).name.lower(),
            "path_stem": Path(module.get("path", "")).stem.lower(),
            "ports": {port.get("name", "").lower() for port in module.get("ports", [])},
            "instances": {inst.get("type", "").lower() for inst in module.get("instances", [])},
            "labels": {label.lower() for label in module.get("labels", [])},
        }
        documents.append({
            "id": idx,
            "module": module,
            "fields": text_by_field,
            "token_counts": token_counts,
            "exact": exact,
        })
    return documents


def build_index(documents: list[dict[str, Any]], include_kg_fields: bool) -> dict[str, Any]:
    weights = dict(PARSER_LSP_FIELDS)
    if include_kg_fields:
        weights.update(HYBRID_EXTRA_FIELDS)

    df = {field: Counter() for field in weights}
    lengths = {field: [] for field in weights}
    for doc in documents:
        for field in weights:
            counts = doc["token_counts"].get(field, Counter())
            lengths[field].append(sum(counts.values()))
            for token in counts:
                df[field][token] += 1
    avgdl = {
        field: (sum(values) / len(values) if values else 0.0)
        for field, values in lengths.items()
    }
    return {
        "weights": weights,
        "df": df,
        "avgdl": avgdl,
        "documents": documents,
        "total_docs": max(1, len(documents)),
    }


def bm25(tf: int, df: int, total_docs: int, doc_len: int, avgdl: float) -> float:
    if tf <= 0:
        return 0.0
    k1 = 1.2
    b = 0.75
    avgdl = avgdl or 1.0
    idf = math.log(1.0 + (total_docs - df + 0.5) / (df + 0.5))
    denom = tf + k1 * (1.0 - b + b * (doc_len / avgdl))
    return idf * ((tf * (k1 + 1.0)) / denom)


def exact_boosts(doc: dict[str, Any], question: dict[str, Any], include_kg_fields: bool) -> tuple[float, list[str]]:
    query_text = question["question"]
    query_tokens = set(tokenize(query_text))
    target_anchors, child_anchors, path_anchors = extract_anchors(query_text)
    exact = doc["exact"]
    reasons = []
    score = 0.0

    if exact["name"] in target_anchors or exact["name"] in query_tokens:
        score += 18.0
        reasons.append("exact_module_name")
    if exact["path_file"] in path_anchors:
        score += 9.0
        reasons.append("exact_path_file")
    if exact["path_stem"] in target_anchors and exact["path_stem"] != exact["name"]:
        score += 7.0
        reasons.append("exact_path_stem")
    for anchor in target_anchors:
        if anchor in exact["ports"]:
            score += 4.0
            reasons.append(f"exact_port:{anchor}")
        if anchor in exact["instances"]:
            score += 5.0
            reasons.append(f"exact_instance:{anchor}")
        if include_kg_fields and anchor in exact["labels"]:
            score += 5.0
            reasons.append(f"exact_label:{anchor}")
    for child in child_anchors:
        if child in exact["instances"]:
            score += 20.0
            reasons.append(f"child_instance:{child}")
        if child == exact["name"]:
            score -= 50.0
            reasons.append("child_anchor_penalty")
    return score, reasons


def retrieve_manticore(question: dict[str, Any], index: dict[str, Any], include_kg_fields: bool, k: int) -> list[dict[str, Any]]:
    query_tokens = token_set(question["question"])
    results = []
    total_docs = index["total_docs"]
    for doc in index["documents"]:
        score = 0.0
        field_reasons = []
        for field, weight in index["weights"].items():
            counts = doc["token_counts"].get(field, Counter())
            doc_len = sum(counts.values())
            for token in query_tokens:
                tf = counts.get(token, 0)
                if not tf:
                    continue
                amount = weight * bm25(
                    tf,
                    index["df"][field].get(token, 0),
                    total_docs,
                    doc_len,
                    index["avgdl"][field],
                )
                score += amount
                if amount > 0:
                    field_reasons.append((amount, f"{field}:{token}"))
        boost, boost_reasons = exact_boosts(doc, question, include_kg_fields)
        score += boost
        if score > 0.1:
            module = doc["module"]
            reasons = [
                reason for _, reason in sorted(field_reasons, key=lambda item: -item[0])[:6]
            ] + boost_reasons[:4]
            results.append({
                "name": module["name"],
                "project": module["project"],
                "score": round(score, 3),
                "reasons": reasons[:8],
            })
    results.sort(key=lambda row: (-row["score"], row["project"], row["name"]))
    return results[:k]


def aggregate(questions: list[dict[str, Any]], runs_by_mode: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
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
            "by_level": summarize_groups(by_level),
            "by_type": summarize_groups(by_type),
        }
    return report


def summarize_groups(groups: dict[str, dict[str, float]]) -> dict[str, dict[str, Any]]:
    return {
        key: {
            "count": vals["count"],
            "hit_at_1": round(vals["hit1"] / vals["count"], 4),
            "hit_at_3": round(vals["hit3"] / vals["count"], 4),
            "mrr": round(vals["mrr"] / vals["count"], 4),
        }
        for key, vals in sorted(groups.items())
    }


def write_documents(path: Path, documents: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for doc in documents:
            module = doc["module"]
            row = {
                "id": doc["id"],
                "name": module.get("name", ""),
                "project": module.get("project", ""),
                "path": module.get("path", ""),
                "path_file": Path(module.get("path", "")).name,
                "ports": doc["fields"].get("ports", ""),
                "instances": doc["fields"].get("instances", ""),
                "instance_names": doc["fields"].get("instance_names", ""),
                "labels": doc["fields"].get("labels", ""),
                "summary": doc["fields"].get("summary", ""),
                "parents": doc["fields"].get("parents", ""),
            }
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_schema(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join([
            "DROP TABLE IF EXISTS rtl_parser_lsp;",
            "CREATE TABLE rtl_parser_lsp (",
            "  name text,",
            "  project text,",
            "  path text,",
            "  path_file text,",
            "  ports text,",
            "  instances text,",
            "  instance_names text,",
            "  labels text,",
            "  summary text,",
            "  parents text",
            ") morphology='stem_en' min_infix_len='2';",
            "",
            "-- Example query:",
            "-- SELECT id, WEIGHT(), name, project FROM rtl_parser_lsp",
            "-- WHERE MATCH('@name ibex_alu | @ports operand_a_i | @instances prim_fifo_sync')",
            "-- ORDER BY WEIGHT() DESC LIMIT 5;",
        ]) + "\n",
        encoding="utf-8",
    )


def build_markdown(report: dict[str, Any], metadata: dict[str, Any]) -> str:
    lines = [
        "# Manticore Retrieval Analysis",
        "",
        "This compares parser+LSP retrieval against a Manticore Search-style BM25F index.",
        "",
        "## Inputs",
        "",
        f"- modules indexed: {metadata['modules_indexed']}",
        f"- questions: {metadata['questions']}",
        f"- manticore repo: {metadata['manticore_repo']}",
        f"- analysis note: {metadata['note']}",
        "",
        "## Aggregate",
        "",
        "| Mode | hit@1 | hit@3 | MRR | weighted hit@1 | avg query ms |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for mode, metrics in report["by_mode"].items():
        latency = metadata["latency_ms"].get(mode, {})
        lines.append(
            f"| {mode} | {metrics['hit_at_1']} | {metrics['hit_at_3']} | "
            f"{metrics['mrr']} | {metrics['weighted_hit_at_1']} | {latency.get('avg_query_ms', 0)} |"
        )
    lines += [
        "",
        "## By Level",
        "",
        "| Mode | L1 | L2 | L3 | L4 | L5 |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for mode, metrics in report["by_mode"].items():
        levels = metrics["by_level"]
        lines.append(
            f"| {mode} | {levels['L1']['hit_at_1']} | {levels['L2']['hit_at_1']} | "
            f"{levels['L3']['hit_at_1']} | {levels['L4']['hit_at_1']} | {levels['L5']['hit_at_1']} |"
        )
    lines += [
        "",
        "## Interpretation",
        "",
        "- `baseline` is the existing parser+LSP overlap scorer.",
        "- `manticore_parser_lsp` indexes only parser+LSP fields: module name, project, path, ports, instances, and instance names.",
        "- `manticore_hybrid` keeps the Manticore-style ranker but also indexes KG labels, summaries, and reverse parent context.",
        "- This run models Manticore ranking locally and writes load-ready documents/schema; it does not start a Manticore server.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Manticore-style parser+LSP retrieval analysis")
    parser.add_argument("--seed", default="out/merged_ontology_seed.jsonl")
    parser.add_argument("--questions", default="out/multiaxis_benchmark/questions_all.jsonl")
    parser.add_argument("--approved-labels", default=None)
    parser.add_argument("--out-dir", default="out/manticore_analysis")
    parser.add_argument("--manticore-repo", default="tools/manticoresearch")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    questions = read_jsonl(args.questions)
    modules, idf_by_mode, known_projects, approved_summary = prepare_retrieval(
        args.seed,
        args.approved_labels,
    )
    for question in questions:
        question["_idf"] = idf_by_mode
        question["_known_projects"] = known_projects

    build_start = time.perf_counter()
    parser_docs = build_documents(modules, include_kg_fields=False)
    parser_index = build_index(parser_docs, include_kg_fields=False)
    hybrid_docs = build_documents(modules, include_kg_fields=True)
    hybrid_index = build_index(hybrid_docs, include_kg_fields=True)
    build_ms = round((time.perf_counter() - build_start) * 1000.0, 3)

    runs_by_mode: dict[str, list[dict[str, Any]]] = {
        "baseline": [],
        "kg": [],
        "manticore_parser_lsp": [],
        "manticore_hybrid": [],
    }
    latency_ms = {}

    for mode in ("baseline", "kg"):
        start = time.perf_counter()
        for question in questions:
            topk = retrieve(question, modules, mode, 5)
            runs_by_mode[mode].append({
                "level": question["level"],
                "type": question["type"],
                "gold_modules": question["gold_modules"],
                "gold_rank": rank_of(question["gold_modules"], topk),
                "topk": topk,
            })
        elapsed = (time.perf_counter() - start) * 1000.0
        latency_ms[mode] = {
            "total_ms": round(elapsed, 3),
            "avg_query_ms": round(elapsed / len(questions), 3),
        }

    for mode, index, include_kg in (
        ("manticore_parser_lsp", parser_index, False),
        ("manticore_hybrid", hybrid_index, True),
    ):
        start = time.perf_counter()
        for question in questions:
            topk = retrieve_manticore(question, index, include_kg, 5)
            runs_by_mode[mode].append({
                "level": question["level"],
                "type": question["type"],
                "gold_modules": question["gold_modules"],
                "gold_rank": rank_of(question["gold_modules"], topk),
                "topk": topk,
            })
        elapsed = (time.perf_counter() - start) * 1000.0
        latency_ms[mode] = {
            "total_ms": round(elapsed, 3),
            "avg_query_ms": round(elapsed / len(questions), 3),
        }

    report = aggregate(questions, runs_by_mode)
    metadata = {
        "modules_indexed": len(modules),
        "questions": len(questions),
        "seed": args.seed,
        "approved_labels": approved_summary,
        "manticore_repo": args.manticore_repo,
        "manticore_source": "https://github.com/manticoresoftware/manticoresearch",
        "index_build_ms": build_ms,
        "latency_ms": latency_ms,
        "note": "Local BM25F model of Manticore Search over parser+LSP fields; schema/documents are emitted for real server loading.",
    }

    write_json(out_dir / "manticore_retrieval_report.json", report)
    write_json(out_dir / "manticore_retrieval_metadata.json", metadata)
    write_json(out_dir / "manticore_detailed_runs.json", runs_by_mode)
    write_documents(out_dir / "manticore_documents.jsonl", parser_docs)
    write_schema(out_dir / "manticore_schema.sql")
    (out_dir / "manticore_retrieval_report.md").write_text(
        build_markdown(report, metadata),
        encoding="utf-8",
    )
    print(json.dumps({
        "status": "ok",
        "out_dir": str(out_dir),
        "modules_indexed": len(modules),
        "questions": len(questions),
        "baseline_hit_at_1": report["by_mode"]["baseline"]["hit_at_1"],
        "kg_hit_at_1": report["by_mode"]["kg"]["hit_at_1"],
        "manticore_parser_lsp_hit_at_1": report["by_mode"]["manticore_parser_lsp"]["hit_at_1"],
        "manticore_hybrid_hit_at_1": report["by_mode"]["manticore_hybrid"]["hit_at_1"],
        "index_build_ms": build_ms,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
