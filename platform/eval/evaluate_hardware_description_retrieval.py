#!/usr/bin/env python3
"""Evaluate retrieval after adding generated hardware-description documents."""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
QUESTIONS = ROOT / "out" / "spec_code_retrieval_benchmark" / "questions_all.jsonl"
HD_JSON = ROOT / "dbs" / "graphify-out" / "hardware-descriptions" / "hardware_descriptions.json"
PREV_PRED = ROOT / "out" / "code_spec_graphify_rerun_tree_sitter_20260520" / "code_spec_graphify_rerun_predictions.json"
OUT_DIR = ROOT / "out" / "hardware_description_retrieval_eval_20260520"

STOP = {
    "the",
    "and",
    "for",
    "that",
    "with",
    "from",
    "node",
    "nodes",
    "code",
    "spec",
    "side",
    "evidence",
    "relevant",
    "return",
    "retrieve",
    "graph",
    "connected",
    "implementation",
    "document",
    "artifact",
    "where",
    "review",
    "reviewer",
    "traceability",
    "checked",
    "concept",
    "clue",
    "area",
    "only",
    "both",
    "well",
    "should",
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def tokenize(text: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for raw in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", text.lower()):
        for token in [raw] + raw.split("_"):
            if len(token) >= 3 and token not in STOP:
                counts[token] += 1
    return counts


def overlap(query: Counter[str], doc: Counter[str]) -> float:
    score = 0.0
    for token, q_count in query.items():
        if token in doc:
            score += 1.0 + min(q_count, doc[token]) * 0.25
    return score


def norm_path(path: str) -> str:
    return path.replace("/", "\\").lower()


def node_key(node: dict[str, Any]) -> tuple[str, str, str]:
    return (
        norm_path(str(node.get("source_file", ""))),
        str(node.get("label", "")).lower(),
        str(node.get("file_type", "")),
    )


def gold_match(candidate: dict[str, Any], gold: dict[str, Any]) -> bool:
    cand_path = norm_path(str(candidate.get("source_file", "")))
    gold_path = norm_path(str(gold.get("source_file", "")))
    cand_label = str(candidate.get("label", "")).lower()
    gold_label = str(gold.get("label", "")).lower()
    if gold_path and cand_path == gold_path and cand_label == gold_label:
        return True
    if gold_path and cand_path == gold_path:
        return True
    return bool(gold_label and cand_label == gold_label and candidate.get("file_type") == gold.get("file_type"))


def rank_of(topk: list[dict[str, Any]], golds: list[dict[str, Any]]) -> int | None:
    for idx, candidate in enumerate(topk, 1):
        if any(gold_match(candidate, gold) for gold in golds):
            return idx
    return None


def joint_rank(spec_rank: int | None, code_rank: int | None) -> int | None:
    if spec_rank is None or code_rank is None:
        return None
    return max(spec_rank, code_rank)


def metrics(runs: list[dict[str, Any]], key: str) -> dict[str, Any]:
    ranks = [run.get(key) for run in runs]
    total = len(ranks)
    return {
        "count": total,
        "hit_at_1": round(sum(1 for rank in ranks if rank == 1) / total, 4) if total else 0,
        "hit_at_3": round(sum(1 for rank in ranks if rank is not None and rank <= 3) / total, 4) if total else 0,
        "hit_at_5": round(sum(1 for rank in ranks if rank is not None and rank <= 5) / total, 4) if total else 0,
        "hit_at_10": round(sum(1 for rank in ranks if rank is not None and rank <= 10) / total, 4) if total else 0,
        "mrr": round(sum((1 / rank) if rank else 0 for rank in ranks) / total, 4) if total else 0,
        "misses_at_10": sum(1 for rank in ranks if rank is None or rank > 10),
    }


def aggregate(questions: list[dict[str, Any]], runs: list[dict[str, Any]]) -> dict[str, Any]:
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for question, run in zip(questions, runs):
        by_type[str(question.get("type", "unknown"))].append(run)
    return {
        "spec": metrics(runs, "spec_rank"),
        "code": metrics(runs, "code_rank"),
        "joint": metrics(runs, "joint_rank"),
        "by_type": {
            qtype: {
                "spec": metrics(items, "spec_rank"),
                "code": metrics(items, "code_rank"),
                "joint": metrics(items, "joint_rank"),
            }
            for qtype, items in sorted(by_type.items())
        },
    }


def ref_text(ref: dict[str, Any]) -> str:
    return " ".join(
        str(ref.get(key, ""))
        for key in ("label", "file_type", "role", "source_file", "source_location", "community")
    )


def hd_text(row: dict[str, Any]) -> str:
    parts = [
        row["component"],
        f"ip_block {row['component']}",
        f"doc_anchor {row['component']}",
        f"module_name_prefix {row['component']}",
    ]
    parts += [ref_text(ref) for ref in row.get("spec_nodes", [])[:80]]
    parts += [ref_text(ref) for ref in row.get("code_nodes", [])[:80]]
    for edge in row.get("bridge_edges", [])[:120]:
        parts.append(edge.get("relation", ""))
        parts.append(ref_text(edge.get("spec", {})))
        parts.append(ref_text(edge.get("code", {})))
    return " ".join(parts)


def build_hd_index(data: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for row in data["components"]:
        rows.append(
            {
                "component": row["component"],
                "tokens": tokenize(hd_text(row)),
                "spec_nodes": row.get("spec_nodes", []),
                "code_nodes": row.get("code_nodes", []),
                "bridge_edges": row.get("bridge_edges", []),
                "bridge_count": sum(row.get("bridge_relations", {}).values()),
            }
        )
    return rows


def add_candidate(candidates: dict[tuple[str, str, str], dict[str, Any]], node: dict[str, Any], score: float, source: str) -> None:
    key = node_key(node)
    if not key[0] and not key[1]:
        return
    current = candidates.get(key)
    payload = {
        "id": node.get("id", ""),
        "label": node.get("label", ""),
        "file_type": node.get("file_type", ""),
        "role": node.get("role", ""),
        "source_file": node.get("source_file", ""),
        "community": node.get("community", ""),
        "score": round(score, 4),
        "retrieval_source": source,
    }
    if current is None or score > current["score"]:
        candidates[key] = payload


def retrieve_hd(index: list[dict[str, Any]], question: str, limit: int = 30) -> list[dict[str, Any]]:
    query = tokenize(question)
    ranked = []
    for row in index:
        score = overlap(query, row["tokens"])
        if score:
            score += min(8.0, row["bridge_count"] / 120.0)
            ranked.append((score, row))
    ranked.sort(key=lambda item: (-item[0], item[1]["component"]))

    candidates: dict[tuple[str, str, str], dict[str, Any]] = {}
    for hd_rank, (hd_score, row) in enumerate(ranked[:12], 1):
        hd_bonus = hd_score / (hd_rank + 2)
        for ref in row["spec_nodes"][:50]:
            score = hd_bonus * 0.55 + overlap(query, tokenize(ref_text(ref))) * 1.8
            add_candidate(candidates, ref, score, f"hd:{row['component']}")
        for ref in row["code_nodes"][:55]:
            score = hd_bonus * 0.65 + overlap(query, tokenize(ref_text(ref))) * 2.2
            add_candidate(candidates, ref, score, f"hd:{row['component']}")
        for edge in row["bridge_edges"][:80]:
            spec, code = edge.get("spec", {}), edge.get("code", {})
            add_candidate(candidates, spec, hd_bonus * 0.8 + overlap(query, tokenize(ref_text(spec))) * 1.8, f"hd_bridge:{row['component']}")
            add_candidate(candidates, code, hd_bonus * 0.9 + overlap(query, tokenize(ref_text(code))) * 2.2, f"hd_bridge:{row['component']}")
    return sorted(candidates.values(), key=lambda item: (-item["score"], item["source_file"], item["label"]))[:limit]


def previous_runs(pred: dict[str, Any], variant: str, mode: str) -> list[dict[str, Any]]:
    return pred[variant][mode]


def candidate_from_previous(item: dict[str, Any], rank: int, source: str) -> dict[str, Any]:
    out = dict(item)
    out["score"] = round(1.0 / (60 + rank), 6)
    out["retrieval_source"] = source
    return out


def rrf_fuse(previous_topk: list[dict[str, Any]], hd_topk: list[dict[str, Any]], limit: int = 30) -> list[dict[str, Any]]:
    scores: dict[tuple[str, str, str], float] = {}
    payloads: dict[tuple[str, str, str], dict[str, Any]] = {}
    for source, items in (("spec-code", previous_topk), ("hardware-description", hd_topk)):
        for rank, item in enumerate(items, 1):
            key = node_key(item)
            scores[key] = scores.get(key, 0.0) + 1.0 / (60 + rank)
            payload = dict(item)
            payload["retrieval_source"] = source
            payloads.setdefault(key, payload)
    out = []
    for key, score in scores.items():
        item = payloads[key]
        item["score"] = round(score, 6)
        out.append(item)
    return sorted(out, key=lambda item: (-item["score"], item.get("source_file", ""), item.get("label", "")))[:limit]


def evaluate_hd(questions: list[dict[str, Any]], hd_index: list[dict[str, Any]]) -> list[dict[str, Any]]:
    runs = []
    for row in questions:
        topk = retrieve_hd(hd_index, row["question"], 30)
        spec_rank = rank_of(topk, row.get("gold_spec_nodes", []))
        code_rank = rank_of(topk, row.get("gold_code_nodes", []))
        runs.append(
            {
                "task_id": row["task_id"],
                "type": row.get("type"),
                "spec_rank": spec_rank,
                "code_rank": code_rank,
                "joint_rank": joint_rank(spec_rank, code_rank),
                "topk": topk[:10],
            }
        )
    return runs


def evaluate_fusion(questions: list[dict[str, Any]], hd_index: list[dict[str, Any]], prev_spec_code: list[dict[str, Any]]) -> list[dict[str, Any]]:
    runs = []
    by_task = {run["task_id"]: run for run in prev_spec_code}
    for row in questions:
        prev_topk = by_task[row["task_id"]]["topk"]
        hd_topk = retrieve_hd(hd_index, row["question"], 30)
        topk = rrf_fuse(prev_topk, hd_topk, 30)
        spec_rank = rank_of(topk, row.get("gold_spec_nodes", []))
        code_rank = rank_of(topk, row.get("gold_code_nodes", []))
        runs.append(
            {
                "task_id": row["task_id"],
                "type": row.get("type"),
                "spec_rank": spec_rank,
                "code_rank": code_rank,
                "joint_rank": joint_rank(spec_rank, code_rank),
                "topk": topk[:10],
            }
        )
    return runs


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    lines = [
        "# Hardware Description Retrieval Evaluation",
        "",
        f"- Questions: {report['questions']}",
        f"- Hardware descriptions: `{report['hardware_descriptions']}`",
        "",
        "## Overall",
        "",
        "| Method | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 | joint MRR |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for method, perf in report["performance"].items():
        lines.append(
            f"| {method} | {perf['spec']['hit_at_5']} | {perf['code']['hit_at_5']} | "
            f"{perf['joint']['hit_at_5']} | {perf['joint']['hit_at_10']} | {perf['joint']['mrr']} |"
        )
    lines += ["", "## Interpretation", ""]
    lines += [
        "- `hardware-description` evaluates only the generated middle-layer documents.",
        "- `spec-code + hardware-description` fuses existing spec-code graph retrieval with the generated middle layer.",
        "- A useful improvement should mainly appear in code hit and joint hit, because the middle layer is intended to connect code evidence back to spec anchors.",
        "",
        "## By Type",
        "",
    ]
    for method, perf in report["performance"].items():
        lines += [f"### {method}", "", "| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |", "|---|---:|---:|---:|---:|"]
        for qtype, vals in perf["by_type"].items():
            lines.append(
                f"| {qtype} | {vals['spec']['hit_at_5']} | {vals['code']['hit_at_5']} | "
                f"{vals['joint']['hit_at_5']} | {vals['joint']['hit_at_10']} |"
            )
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_html(path: Path, report: dict[str, Any]) -> None:
    rows = []
    chart = []
    for method, perf in report["performance"].items():
        row = {
            "method": method,
            "spec5": perf["spec"]["hit_at_5"],
            "code5": perf["code"]["hit_at_5"],
            "joint5": perf["joint"]["hit_at_5"],
            "joint10": perf["joint"]["hit_at_10"],
            "mrr": perf["joint"]["mrr"],
        }
        chart.append(row)
        rows.append(
            "<tr>"
            f"<td>{html.escape(method)}</td><td>{row['spec5']:.4f}</td><td>{row['code5']:.4f}</td>"
            f"<td>{row['joint5']:.4f}</td><td>{row['joint10']:.4f}</td><td>{row['mrr']:.4f}</td>"
            "</tr>"
        )
    data = json.dumps(chart, ensure_ascii=False)
    html_text = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hardware Description Retrieval Evaluation</title>
<style>
body{{margin:0;font-family:Arial,Helvetica,sans-serif;background:#f6f7f9;color:#17202a}}main{{max-width:1120px;margin:0 auto;padding:32px 22px 48px}}h1{{margin:0 0 8px;font-size:28px}}p{{color:#667085;line-height:1.5}}table{{width:100%;border-collapse:collapse;background:#fff;border:1px solid #d7dde7;border-radius:8px;overflow:hidden}}th,td{{padding:10px 12px;border-bottom:1px solid #d7dde7;text-align:left;font-size:13px}}th{{background:#eef2f7}}.chart{{background:#fff;border:1px solid #d7dde7;border-radius:8px;padding:16px;margin:18px 0}}.barrow{{display:grid;grid-template-columns:280px 1fr 70px;gap:10px;align-items:center;margin:9px 0}}.track{{height:18px;background:#eef2f7;border-radius:4px;overflow:hidden}}.bar{{height:100%;background:#b7791f}}.code{{background:#16875f}}.spec{{background:#2f6fed}}a{{color:#2457c5}}
</style></head><body><main>
<h1>Hardware Description Retrieval Evaluation</h1>
<p>This compares existing graph retrieval against retrieval after adding generated intermediate hardware-description documents.</p>
<p><a href="../../dbs/graphify-out/hardware-descriptions/index.html">Open hardware descriptions</a> · <a href="../../dbs/graphify-out/hardware-descriptions/hardware-description-bridge.html">Open bridge graph</a></p>
<h2>Code hit@5</h2><div class="chart" id="code"></div>
<h2>Joint hit@5</h2><div class="chart" id="joint"></div>
<h2>Overall</h2>
<table><thead><tr><th>Method</th><th>Spec hit@5</th><th>Code hit@5</th><th>Joint hit@5</th><th>Joint hit@10</th><th>Joint MRR</th></tr></thead><tbody>{''.join(rows)}</tbody></table>
</main><script>
const rows={data};
function render(id,key,cls){{document.getElementById(id).innerHTML=rows.map(r=>`<div class="barrow"><div>${{r.method}}</div><div class="track"><div class="bar ${{cls}}" style="width:${{Math.max(1,r[key]*100)}}%"></div></div><div>${{r[key].toFixed(4)}}</div></div>`).join('')}}
render('code','code5','code'); render('joint','joint5','');
</script></body></html>"""
    path.write_text(html_text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--questions", type=Path, default=QUESTIONS)
    parser.add_argument("--hardware-descriptions", type=Path, default=HD_JSON)
    parser.add_argument("--previous-predictions", type=Path, default=PREV_PRED)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    questions = read_jsonl(args.questions)
    hd_data = read_json(args.hardware_descriptions)
    prev = read_json(args.previous_predictions)
    hd_index = build_hd_index(hd_data)

    runs = {
        "code-only current": previous_runs(prev, "code-only", "current"),
        "code-only base": previous_runs(prev, "code-only", "base"),
        "spec-code current": previous_runs(prev, "spec-code", "current"),
        "hardware-description": evaluate_hd(questions, hd_index),
    }
    runs["spec-code + hardware-description"] = evaluate_fusion(questions, hd_index, runs["spec-code current"])

    report = {
        "questions": len(questions),
        "benchmark": str(args.questions),
        "hardware_descriptions": str(args.hardware_descriptions),
        "previous_predictions": str(args.previous_predictions),
        "performance": {method: aggregate(questions, method_runs) for method, method_runs in runs.items()},
    }
    (args.out_dir / "hardware_description_retrieval_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (args.out_dir / "hardware_description_retrieval_predictions.json").write_text(
        json.dumps(runs, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_markdown(args.out_dir / "hardware_description_retrieval_report.md", report)
    write_html(args.out_dir / "hardware_description_retrieval_report.html", report)
    print(json.dumps({"status": "ok", "out_dir": str(args.out_dir), "performance": report["performance"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
