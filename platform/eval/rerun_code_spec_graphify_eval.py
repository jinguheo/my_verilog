#!/usr/bin/env python3
"""Re-evaluate Graphify code-only and spec-code retrieval with ranking diagnostics."""

from __future__ import annotations

import argparse
import html
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_QUESTIONS = ROOT / "out" / "spec_code_retrieval_benchmark" / "questions_all.jsonl"
DEFAULT_OUT = ROOT / "out" / "code_spec_graphify_rerun_tree_sitter_20260520"
GRAPHS = {
    "code-only": ROOT / "dbs" / "graphify-out" / "code-only-graphify" / "graph.json",
    "spec-code": ROOT / "dbs" / "graphify-out" / "spec-code-graphify" / "graph.json",
}

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
}
BRIDGE_RELATIONS = {"spec_component_matches_code", "spec_path_matches_code_path"}


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


def norm_path(path: str) -> str:
    return path.replace("/", "\\").lower()


def node_text(node: dict[str, Any]) -> str:
    return " ".join(
        str(node.get(key, ""))
        for key in ("label", "file_type", "role", "source_file", "source_location", "community", "graph_variant")
    )


def relation(edge: dict[str, Any]) -> str:
    return str(edge.get("relation") or edge.get("type") or "related")


def edge_source(edge: dict[str, Any]) -> str:
    return str(edge.get("source") or edge.get("_src") or "")


def edge_target(edge: dict[str, Any]) -> str:
    return str(edge.get("target") or edge.get("_tgt") or "")


def load_graph(path: Path) -> dict[str, Any]:
    graph = read_json(path)
    nodes = {str(node["id"]): node for node in graph.get("nodes", [])}
    links = graph.get("links", graph.get("edges", []))
    adjacency: dict[str, list[tuple[str, dict[str, Any]]]] = defaultdict(list)
    degree: Counter[str] = Counter()
    for edge in links:
        src, tgt = edge_source(edge), edge_target(edge)
        if src in nodes and tgt in nodes:
            adjacency[src].append((tgt, edge))
            adjacency[tgt].append((src, edge))
            degree[src] += 1
            degree[tgt] += 1
    token_index = {node_id: tokenize(node_text(node)) for node_id, node in nodes.items()}
    return {"nodes": nodes, "links": links, "adjacency": adjacency, "degree": degree, "token_index": token_index}


def overlap_score(query: Counter[str], doc: Counter[str]) -> float:
    score = 0.0
    for token, q_count in query.items():
        if token in doc:
            score += 1.0 + min(q_count, doc[token]) * 0.25
    return score


def propagation_factor(rel: str) -> float:
    if rel in BRIDGE_RELATIONS:
        return 0.9
    if rel in {"documents_component", "references_component", "contains"}:
        return 0.35
    if rel in {"instantiates", "defines", "calls"}:
        return 0.25
    return 0.15


def retrieve(graph: dict[str, Any], question: str, mode: str, limit: int) -> list[dict[str, Any]]:
    query = tokenize(question)
    base: dict[str, float] = {}
    for node_id, tokens in graph["token_index"].items():
        score = overlap_score(query, tokens)
        if score:
            base[node_id] = score

    scores = dict(base)
    if mode != "base":
        for node_id, score in list(base.items()):
            neighbors = graph["adjacency"].get(node_id, [])
            for nbr, edge in neighbors:
                factor = propagation_factor(relation(edge))
                if mode == "degree_norm":
                    factor /= math.sqrt(max(1, len(neighbors)))
                scores[nbr] = scores.get(nbr, 0.0) + score * factor

    ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))[:limit]
    out = []
    for node_id, score in ranked:
        node = graph["nodes"][node_id]
        out.append(
            {
                "id": node_id,
                "label": node.get("label", ""),
                "file_type": node.get("file_type", ""),
                "role": node.get("role", ""),
                "source_file": node.get("source_file", ""),
                "community": node.get("community", ""),
                "degree": graph["degree"].get(node_id, 0),
                "score": round(score, 4),
            }
        )
    return out


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


def check_gold_coverage(graph: dict[str, Any], questions: list[dict[str, Any]]) -> dict[str, Any]:
    exact = set()
    paths = set()
    for node in graph["nodes"].values():
        path = norm_path(str(node.get("source_file", "")))
        label = str(node.get("label", "")).lower()
        file_type = str(node.get("file_type", ""))
        paths.add(path)
        exact.add((path, label, file_type))
    total = missing_path = missing_exact = 0
    for row in questions:
        for gold in row.get("gold_code_nodes", []):
            total += 1
            path = norm_path(str(gold.get("source_file", "")))
            label = str(gold.get("label", "")).lower()
            file_type = str(gold.get("file_type", ""))
            if path not in paths:
                missing_path += 1
            if (path, label, file_type) not in exact:
                missing_exact += 1
    return {"gold_code_nodes": total, "missing_path": missing_path, "missing_exact": missing_exact}


def top_hubs(graph: dict[str, Any], limit: int = 20) -> list[dict[str, Any]]:
    rows = []
    for node_id, degree in graph["degree"].most_common(limit):
        node = graph["nodes"][node_id]
        rows.append(
            {
                "id": node_id,
                "label": node.get("label", ""),
                "file_type": node.get("file_type", ""),
                "source_file": node.get("source_file", ""),
                "degree": degree,
            }
        )
    return rows


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    lines = [
        "# Code-Only vs Spec-Code Graphify Re-evaluation",
        "",
        f"- Questions: {report['questions']}",
        f"- Benchmark: `{report['benchmark']}`",
        "- Ranking modes: current propagation, base lexical, degree-normalized propagation",
        "",
        "## Overall",
        "",
        "| Variant | Mode | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 | joint MRR |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for variant, modes in report["performance"].items():
        for mode, perf in modes.items():
            lines.append(
                f"| {variant} | {mode} | {perf['spec']['hit_at_5']} | {perf['code']['hit_at_5']} | "
                f"{perf['joint']['hit_at_5']} | {perf['joint']['hit_at_10']} | {perf['joint']['mrr']} |"
            )
    lines += ["", "## Code Gold Coverage", "", "| Variant | gold code nodes | missing paths | missing exact nodes |", "|---|---:|---:|---:|"]
    for variant, cov in report["coverage"].items():
        lines.append(f"| {variant} | {cov['gold_code_nodes']} | {cov['missing_path']} | {cov['missing_exact']} |")
    lines += ["", "## Top Code-Only Hubs", "", "| Label | File type | Degree | Source file |", "|---|---|---:|---|"]
    for hub in report["top_code_only_hubs"][:10]:
        lines.append(f"| `{hub['label']}` | {hub['file_type']} | {hub['degree']} | `{hub['source_file']}` |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_html(path: Path, report: dict[str, Any]) -> None:
    perf_rows = []
    chart_items = []
    for variant, modes in report["performance"].items():
        for mode, perf in modes.items():
            row = {
                "variant": variant,
                "mode": mode,
                "spec5": perf["spec"]["hit_at_5"],
                "code5": perf["code"]["hit_at_5"],
                "joint5": perf["joint"]["hit_at_5"],
                "joint10": perf["joint"]["hit_at_10"],
                "mrr": perf["joint"]["mrr"],
            }
            chart_items.append(row)
            perf_rows.append(
                "<tr>"
                f"<td>{html.escape(variant)}</td><td>{html.escape(mode)}</td>"
                f"<td>{row['spec5']:.4f}</td><td>{row['code5']:.4f}</td>"
                f"<td>{row['joint5']:.4f}</td><td>{row['joint10']:.4f}</td><td>{row['mrr']:.4f}</td>"
                "</tr>"
            )
    coverage_rows = []
    for variant, cov in report["coverage"].items():
        coverage_rows.append(
            f"<tr><td>{html.escape(variant)}</td><td>{cov['gold_code_nodes']}</td><td>{cov['missing_path']}</td><td>{cov['missing_exact']}</td></tr>"
        )
    hub_rows = []
    for hub in report["top_code_only_hubs"][:12]:
        hub_rows.append(
            "<tr>"
            f"<td>{html.escape(str(hub['label']))}</td><td>{html.escape(str(hub['file_type']))}</td>"
            f"<td>{hub['degree']}</td><td>{html.escape(str(hub['source_file']))}</td>"
            "</tr>"
        )

    data = json.dumps(chart_items, ensure_ascii=False)
    html_text = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Graphify Code/Spec Re-evaluation</title>
<style>
:root {{ color-scheme: light; --ink:#1f2937; --muted:#667085; --line:#d9dee7; --panel:#ffffff; --bg:#f6f7f9; --blue:#2f6fed; --green:#16875f; --amber:#b7791f; }}
body {{ margin:0; font-family: Arial, Helvetica, sans-serif; background:var(--bg); color:var(--ink); }}
main {{ max-width:1180px; margin:0 auto; padding:30px 22px 48px; }}
h1 {{ margin:0 0 8px; font-size:28px; }}
h2 {{ margin:28px 0 10px; font-size:18px; }}
p {{ color:var(--muted); line-height:1.5; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:12px; margin:18px 0; }}
.metric {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:14px; }}
.metric strong {{ display:block; font-size:24px; margin-top:4px; }}
table {{ width:100%; border-collapse:collapse; background:var(--panel); border:1px solid var(--line); border-radius:8px; overflow:hidden; }}
th,td {{ padding:10px 11px; border-bottom:1px solid var(--line); text-align:left; font-size:13px; vertical-align:top; }}
th {{ background:#eef2f7; color:#344054; }}
.chart {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:16px; }}
.barrow {{ display:grid; grid-template-columns:220px 1fr 70px; align-items:center; gap:10px; margin:9px 0; }}
.track {{ height:18px; background:#eef2f7; border-radius:4px; overflow:hidden; }}
.bar {{ height:100%; background:var(--blue); }}
.bar.code {{ background:var(--green); }}
.bar.joint {{ background:var(--amber); }}
.links a {{ display:inline-block; margin-right:10px; color:#2457c5; }}
code {{ background:#eef2f7; padding:2px 4px; border-radius:4px; }}
</style>
</head>
<body>
<main>
<h1>Graphify Code-Only vs Spec-Code Re-evaluation</h1>
<p>Stored Graphify graph JSON files were used. No graphify update was run. This page compares the original propagation ranking with safer alternatives for code-side retrieval.</p>
<div class="links">
  <a href="../../dbs/graphify-out/html-views/code-only.html">Open code-only graph view</a>
  <a href="../../dbs/graphify-out/html-views/spec-code.html">Open spec-code graph view</a>
</div>
<div class="grid">
  <div class="metric">Code-only current code hit@5<strong>{report['performance']['code-only']['current']['code']['hit_at_5']:.4f}</strong></div>
  <div class="metric">Code-only base code hit@5<strong>{report['performance']['code-only']['base']['code']['hit_at_5']:.4f}</strong></div>
  <div class="metric">Spec-code current joint hit@5<strong>{report['performance']['spec-code']['current']['joint']['hit_at_5']:.4f}</strong></div>
  <div class="metric">Spec-code base joint hit@5<strong>{report['performance']['spec-code']['base']['joint']['hit_at_5']:.4f}</strong></div>
</div>
<h2>Code hit@5</h2>
<div class="chart" id="codeChart"></div>
<h2>Joint hit@5</h2>
<div class="chart" id="jointChart"></div>
<h2>Overall Metrics</h2>
<table><thead><tr><th>Variant</th><th>Mode</th><th>Spec hit@5</th><th>Code hit@5</th><th>Joint hit@5</th><th>Joint hit@10</th><th>Joint MRR</th></tr></thead><tbody>{''.join(perf_rows)}</tbody></table>
<h2>Gold Coverage</h2>
<table><thead><tr><th>Variant</th><th>Gold code nodes</th><th>Missing paths</th><th>Missing exact nodes</th></tr></thead><tbody>{''.join(coverage_rows)}</tbody></table>
<h2>High-degree code-only hubs</h2>
<p>These nodes explain why unrestricted graph propagation can push generic reused modules above the exact target.</p>
<table><thead><tr><th>Label</th><th>Type</th><th>Degree</th><th>Source file</th></tr></thead><tbody>{''.join(hub_rows)}</tbody></table>
</main>
<script>
const rows = {data};
function renderChart(id, key, cls) {{
  const root = document.getElementById(id);
  root.innerHTML = rows.map(r => {{
    const v = r[key];
    const label = `${{r.variant}} / ${{r.mode}}`;
    return `<div class="barrow"><div>${{label}}</div><div class="track"><div class="bar ${{cls}}" style="width:${{Math.max(1, v*100)}}%"></div></div><div>${{v.toFixed(4)}}</div></div>`;
  }}).join("");
}}
renderChart("codeChart", "code5", "code");
renderChart("jointChart", "joint5", "joint");
</script>
</body>
</html>
"""
    path.write_text(html_text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--questions", type=Path, default=DEFAULT_QUESTIONS)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--limit", type=int, default=30)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    questions = read_jsonl(args.questions)
    graphs = {name: load_graph(path) for name, path in GRAPHS.items()}
    modes = ["current", "base", "degree_norm"]

    details: dict[str, dict[str, list[dict[str, Any]]]] = {}
    performance: dict[str, dict[str, Any]] = {}
    for variant, graph in graphs.items():
        details[variant] = {}
        performance[variant] = {}
        for mode in modes:
            runs = []
            for row in questions:
                topk = retrieve(graph, row["question"], mode, args.limit)
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
            details[variant][mode] = runs
            performance[variant][mode] = aggregate(questions, runs)

    report = {
        "questions": len(questions),
        "benchmark": str(args.questions),
        "graphs": {name: str(path) for name, path in GRAPHS.items()},
        "modes": modes,
        "performance": performance,
        "coverage": {name: check_gold_coverage(graph, questions) for name, graph in graphs.items()},
        "top_code_only_hubs": top_hubs(graphs["code-only"], 20),
    }
    (args.out_dir / "code_spec_graphify_rerun_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (args.out_dir / "code_spec_graphify_rerun_predictions.json").write_text(
        json.dumps(details, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_markdown(args.out_dir / "code_spec_graphify_rerun_report.md", report)
    write_html(args.out_dir / "code_spec_graphify_rerun_report.html", report)
    print(json.dumps({"status": "ok", "out_dir": str(args.out_dir), "performance": performance}, ensure_ascii=False))


if __name__ == "__main__":
    main()
