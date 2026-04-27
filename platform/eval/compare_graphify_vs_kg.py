"""Compare the repo's RTL KG retrieval with a Graphify AST graph.

The comparison is intentionally retrieval-oriented:
- Current KG numbers come from the existing benchmark reports.
- Graphify is built from the same RTL module source files used by the KG.
- Token cost is estimated from the context each method would pass to an LLM.
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
GRAPHIFY_SRC = ROOT / "tools" / "graphify"
if str(GRAPHIFY_SRC) not in sys.path:
    sys.path.insert(0, str(GRAPHIFY_SRC))

KG_FULL = ROOT / "out" / "kg_full" / "kg_full_nodes_edges.json"
KG_REPORT = ROOT / "out" / "reports" / "kg_eval_report.json"
GENERAL_BENCH = ROOT / "out" / "eval_benchmark" / "benchmark_all.jsonl"
GENERAL_RUNS = ROOT / "out" / "eval_results" / "detailed_runs.json"
MULTI_BENCH = ROOT / "out" / "multiaxis_benchmark" / "questions_all.jsonl"
MULTI_RUNS = ROOT / "out" / "multiaxis_eval_results" / "multiaxis_detailed_runs.json"
OUT_DIR = ROOT / "out" / "graphify_compare"
GRAPHIFY_OUT = ROOT / "graphify-out"

CHARS_PER_TOKEN = 4


def norm_path(path: str | Path) -> str:
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    try:
        p = p.resolve()
    except OSError:
        p = p.absolute()
    return str(p).replace("/", "\\").lower()


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // CHARS_PER_TOKEN)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def load_kg() -> dict[str, Any]:
    data = json.loads(KG_FULL.read_text(encoding="utf-8"))
    nodes = data["nodes"]
    edges = data["edges"]
    by_id = {node["id"]: node for node in nodes}

    modules = [
        node
        for node in nodes
        if node.get("kind") == "module"
        and node.get("project") in {"ibex", "opentitan"}
        and node.get("path")
        and Path(node["path"]).exists()
    ]
    module_ids = {node["id"] for node in modules}

    labels: dict[str, list[str]] = defaultdict(list)
    ports: dict[str, list[str]] = defaultdict(list)
    instances: dict[str, list[str]] = defaultdict(list)
    fanin: dict[str, list[str]] = defaultdict(list)

    for edge in edges:
        src = edge.get("source")
        tgt = edge.get("target")
        if edge.get("type") == "HAS_LABEL" and src in module_ids and isinstance(tgt, str):
            labels[src].append(tgt.split(":", 1)[-1])
        elif edge.get("type") == "HAS_PORT" and src in module_ids and tgt in by_id:
            ports[src].append(by_id[tgt].get("name", ""))
        elif edge.get("type") == "INSTANTIATES" and src in module_ids and tgt in by_id:
            instances[src].append(by_id[tgt].get("name", ""))
            fanin[tgt].append(by_id[src].get("name", ""))

    records: list[dict[str, Any]] = []
    for node in modules:
        record = dict(node)
        record["labels"] = sorted(set(labels[node["id"]]))
        record["ports"] = sorted(p for p in set(ports[node["id"]]) if p)
        record["instances"] = sorted(i for i in set(instances[node["id"]]) if i)
        record["fanin"] = sorted(i for i in set(fanin[node["id"]]) if i)
        records.append(record)

    by_name_project: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    by_path: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_name: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_name_project[(record["name"].lower(), record["project"].lower())].append(record)
        by_path[norm_path(record["path"])].append(record)
        by_name[record["name"].lower()].append(record)

    return {
        "records": records,
        "by_id": by_id,
        "by_name_project": by_name_project,
        "by_path": by_path,
        "by_name": by_name,
    }


def card(record: dict[str, Any], max_ports: int = 16, max_instances: int = 12) -> dict[str, Any]:
    return {
        "name": record.get("name"),
        "project": record.get("project"),
        "path": record.get("path"),
        "summary": record.get("summary"),
        "labels": record.get("labels", []),
        "ports": record.get("ports", [])[:max_ports],
        "instances": record.get("instances", [])[:max_instances],
        "fanin": record.get("fanin", [])[:max_instances],
    }


def serialize_kg_context(topk: list[dict[str, Any]], kg: dict[str, Any]) -> str:
    cards = []
    for item in topk[:3]:
        candidates = kg["by_name_project"].get((item.get("name", "").lower(), item.get("project", "").lower()), [])
        if candidates:
            cards.append(card(candidates[0]))
    return json.dumps(cards, ensure_ascii=False, sort_keys=True)


def load_or_build_graphify(kg: dict[str, Any], rebuild: bool):
    from graphify.analyze import god_nodes, suggest_questions, surprising_connections
    from graphify.build import build_from_json
    from graphify.cluster import cluster, score_all
    from graphify.export import to_html, to_json
    from graphify.extract import extract
    from graphify.report import generate
    from networkx.readwrite import json_graph

    graph_path = GRAPHIFY_OUT / "graph.json"
    metadata_path = OUT_DIR / "graphify_build_metadata.json"
    source_paths = sorted({Path(record["path"]) for record in kg["records"]})

    if graph_path.exists() and metadata_path.exists() and not rebuild:
        data = json.loads(graph_path.read_text(encoding="utf-8"))
        try:
            graph = json_graph.node_link_graph(data, edges="links")
        except TypeError:
            graph = json_graph.node_link_graph(data)
        return graph, json.loads(metadata_path.read_text(encoding="utf-8"))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    GRAPHIFY_OUT.mkdir(parents=True, exist_ok=True)
    extraction = extract(source_paths, cache_root=OUT_DIR / "cache")
    graph = build_from_json(extraction)
    communities = cluster(graph)
    for cid, node_ids in communities.items():
        for node_id in node_ids:
            graph.nodes[node_id]["community"] = cid

    community_labels: dict[int, str] = {}
    for cid, node_ids in communities.items():
        ranked = sorted(node_ids, key=lambda nid: graph.degree(nid), reverse=True)
        community_labels[cid] = graph.nodes[ranked[0]].get("label", ranked[0]) if ranked else f"Community {cid}"

    cohesion = score_all(graph, communities)
    to_json(graph, communities, str(graph_path), force=True)
    to_html(graph, communities, str(GRAPHIFY_OUT / "graph.html"), community_labels=community_labels)

    detection = {
        "total_files": len(source_paths),
        "total_words": sum(
            len(re.findall(r"\S+", Path(path).read_text(encoding="utf-8", errors="ignore")))
            for path in source_paths
        ),
    }
    report = generate(
        graph,
        communities,
        cohesion,
        community_labels,
        god_nodes(graph, top_n=12),
        surprising_connections(graph, communities, top_n=8),
        detection,
        {"input": extraction.get("input_tokens", 0), "output": extraction.get("output_tokens", 0)},
        str(ROOT),
        suggested_questions=suggest_questions(graph, communities, community_labels, top_n=7),
    )
    (GRAPHIFY_OUT / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")

    metadata = {
        "source_files": len(source_paths),
        "nodes": graph.number_of_nodes(),
        "edges": graph.number_of_edges(),
        "communities": len(communities),
        "graph_path": str(graph_path),
        "report_path": str(GRAPHIFY_OUT / "GRAPH_REPORT.md"),
        "html_path": str(GRAPHIFY_OUT / "graph.html"),
        "verilog_patch": "module/instantiation fallback extraction plus path-qualified module ids",
    }
    metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
    return graph, metadata


TERM_RE = re.compile(r"[A-Za-z0-9_]+")


def question_terms(question: str) -> list[str]:
    stop = {
        "which",
        "module",
        "modules",
        "named",
        "should",
        "returned",
        "from",
        "current",
        "knowledge",
        "find",
        "the",
        "rtl",
        "and",
        "for",
        "with",
        "that",
        "what",
        "does",
        "db",
    }
    return [t.lower() for t in TERM_RE.findall(question) if len(t) > 2 and t.lower() not in stop]


def score_graphify_nodes(graph, question: str) -> list[tuple[float, str]]:
    terms = question_terms(question)
    scored: list[tuple[float, str]] = []
    for node_id, data in graph.nodes(data=True):
        label = str(data.get("label", "")).lower()
        source = str(data.get("source_file", "")).lower().replace("\\", "/")
        score = 0.0
        for term in terms:
            if term == label:
                score += 8.0
            elif term in label:
                score += 3.0
            if term in source:
                score += 1.5
        if label.endswith(".sv") or label.endswith(".v"):
            score *= 0.92
        if score > 0:
            scored.append((score, node_id))
    return sorted(scored, key=lambda item: (-item[0], item[1]))


def graphify_candidates(graph, kg: dict[str, Any], question: str, limit: int = 10) -> tuple[list[dict[str, Any]], str]:
    seen: set[tuple[str, str, str]] = set()
    candidates: list[dict[str, Any]] = []
    scored = score_graphify_nodes(graph, question)

    for score, node_id in scored:
        data = graph.nodes[node_id]
        mapped: list[dict[str, Any]] = []
        label = str(data.get("label", "")).lower()
        source = data.get("source_file")
        if source:
            mapped.extend(kg["by_path"].get(norm_path(source), []))
        if label:
            mapped.extend(kg["by_name"].get(label, []))
            if label.endswith((".sv", ".v")) and source:
                mapped.extend(kg["by_path"].get(norm_path(source), []))
        for record in mapped:
            key = (record["name"].lower(), record["project"].lower(), norm_path(record["path"]))
            if key in seen:
                continue
            seen.add(key)
            candidates.append(
                {
                    "name": record["name"],
                    "project": record["project"],
                    "path": record["path"],
                    "score": round(score, 3),
                    "node": node_id,
                    "node_label": data.get("label"),
                }
            )
            if len(candidates) >= limit:
                break
        if len(candidates) >= limit:
            break

    context = graphify_context(graph, [node_id for _, node_id in scored[:3]])
    return candidates, context


def graphify_context(graph, start_nodes: list[str], depth: int = 2, token_budget: int = 2000) -> str:
    from graphify.serve import _bfs, _subgraph_to_text

    if not start_nodes:
        return ""
    nodes, edges = _bfs(graph, start_nodes, depth)
    return _subgraph_to_text(graph, nodes, edges, token_budget=token_budget)


def gold_match(candidate: dict[str, Any], row: dict[str, Any]) -> bool:
    gold_paths = {norm_path(path) for path in row.get("gold_paths", []) or []}
    if row.get("gold_path"):
        gold_paths.add(norm_path(row["gold_path"]))
    gold_modules = {name.lower() for name in row.get("gold_modules", [])}
    gold_projects = {p.lower() for p in row.get("gold_projects", []) or []}
    if row.get("gold_project"):
        gold_projects.add(str(row["gold_project"]).lower())

    if gold_paths and norm_path(candidate.get("path", "")) in gold_paths:
        return True
    if candidate.get("name", "").lower() in gold_modules:
        return not gold_projects or candidate.get("project", "").lower() in gold_projects
    return False


def rank_of(candidates: list[dict[str, Any]], row: dict[str, Any]) -> int | None:
    for idx, candidate in enumerate(candidates, 1):
        if gold_match(candidate, row):
            return idx
    return None


def summarize_ranks(rows: list[dict[str, Any]], ranks: list[int | None], group_key: str | None = None) -> dict[str, Any]:
    def metrics(indexes: list[int]) -> dict[str, Any]:
        local = [ranks[i] for i in indexes]
        count = len(local)
        return {
            "count": count,
            "hit_at_1": round(sum(1 for rank in local if rank == 1) / count, 4) if count else 0.0,
            "hit_at_3": round(sum(1 for rank in local if rank is not None and rank <= 3) / count, 4) if count else 0.0,
            "mrr": round(sum((1 / rank) if rank else 0 for rank in local) / count, 4) if count else 0.0,
        }

    summary: dict[str, Any] = metrics(list(range(len(rows))))
    if group_key:
        grouped: dict[str, list[int]] = defaultdict(list)
        for idx, row in enumerate(rows):
            grouped[str(row.get(group_key, "unknown"))].append(idx)
        summary[f"by_{group_key}"] = {key: metrics(indexes) for key, indexes in sorted(grouped.items())}
    return summary


def token_stats(values: list[int]) -> dict[str, Any]:
    if not values:
        return {"avg": 0, "median": 0, "p90": 0}
    ordered = sorted(values)
    p90_idx = min(len(ordered) - 1, int(len(ordered) * 0.9))
    return {
        "avg": round(statistics.mean(values), 1),
        "median": round(statistics.median(values), 1),
        "p90": ordered[p90_idx],
    }


def raw_gold_context_tokens(rows: list[dict[str, Any]]) -> list[int]:
    values = []
    for row in rows:
        paths = row.get("gold_paths") or ([row["gold_path"]] if row.get("gold_path") else [])
        chunks = []
        for path in paths[:3]:
            p = Path(path)
            if p.exists():
                chunks.append(p.read_text(encoding="utf-8", errors="ignore"))
        values.append(estimate_tokens("\n".join(chunks)) if chunks else 0)
    return values


def compare_set(
    name: str,
    rows: list[dict[str, Any]],
    kg_runs: list[dict[str, Any]],
    graph,
    kg: dict[str, Any],
    group_key: str,
) -> dict[str, Any]:
    ranks: list[int | None] = []
    graphify_tokens: list[int] = []
    kg_tokens: list[int] = []
    predictions: list[dict[str, Any]] = []

    for row, kg_run in zip(rows, kg_runs):
        candidates, context = graphify_candidates(graph, kg, row["question"], limit=10)
        rank = rank_of(candidates, row)
        ranks.append(rank)
        graphify_tokens.append(estimate_tokens(context))
        kg_context = serialize_kg_context(kg_run.get("topk", []), kg)
        kg_tokens.append(estimate_tokens(kg_context))
        predictions.append(
            {
                "question": row["question"],
                "gold_modules": row.get("gold_modules"),
                "gold_paths": row.get("gold_paths") or ([row.get("gold_path")] if row.get("gold_path") else []),
                "gold_rank": rank,
                "topk": candidates[:5],
                "graphify_context_tokens": graphify_tokens[-1],
                "kg_context_tokens": kg_tokens[-1],
            }
        )

    raw_tokens = raw_gold_context_tokens(rows)
    summary = summarize_ranks(rows, ranks, group_key=group_key)
    token_summary = {
        "current_kg_context": token_stats(kg_tokens),
        "graphify_query_context": token_stats(graphify_tokens),
        "raw_gold_source": token_stats(raw_tokens),
    }
    kg_avg = token_summary["current_kg_context"]["avg"] or 1
    graphify_avg = token_summary["graphify_query_context"]["avg"] or 1
    raw_avg = token_summary["raw_gold_source"]["avg"] or 1
    token_summary["graphify_vs_current_kg_avg_ratio"] = round(graphify_avg / kg_avg, 2)
    token_summary["current_kg_reduction_vs_raw"] = round(raw_avg / kg_avg, 2)
    token_summary["graphify_reduction_vs_raw"] = round(raw_avg / graphify_avg, 2)

    (OUT_DIR / f"{name}_graphify_predictions.json").write_text(
        json.dumps(predictions, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return {"performance": summary, "tokens": token_summary}


def write_markdown(report: dict[str, Any], path: Path) -> None:
    general = report["comparison"]["general"]
    multi = report["comparison"]["multiaxis"]
    kg_perf = report["current_kg"]
    lines = [
        "# Current RTL KG vs Graphify",
        "",
        "## Scope",
        "",
        f"- Source files compared: {report['graphify_build']['source_files']}",
        f"- Graphify graph: {report['graphify_build']['nodes']} nodes / {report['graphify_build']['edges']} edges",
        f"- Graphify output: `{report['graphify_build']['graph_path']}`",
        f"- Current KG: {kg_perf['kg_summary']['total_nodes']} nodes / {kg_perf['kg_summary']['total_edges']} edges",
        "",
        "## Retrieval Performance",
        "",
        "| Benchmark | Method | Hit@1 | Hit@3 | MRR |",
        "|---|---:|---:|---:|---:|",
        f"| General 150 | Current KG | {kg_perf['retrieval_report']['by_mode']['kg']['hit_at_1']:.4f} | {kg_perf['retrieval_report']['by_mode']['kg']['hit_at_3']:.4f} | {kg_perf['retrieval_report']['by_mode']['kg']['mrr']:.4f} |",
        f"| General 150 | Graphify | {general['performance']['hit_at_1']:.4f} | {general['performance']['hit_at_3']:.4f} | {general['performance']['mrr']:.4f} |",
        f"| Multi-axis 175 | Current KG | {kg_perf['multiaxis_report']['by_mode']['kg']['hit_at_1']:.4f} | {kg_perf['multiaxis_report']['by_mode']['kg']['hit_at_3']:.4f} | {kg_perf['multiaxis_report']['by_mode']['kg']['mrr']:.4f} |",
        f"| Multi-axis 175 | Graphify | {multi['performance']['hit_at_1']:.4f} | {multi['performance']['hit_at_3']:.4f} | {multi['performance']['mrr']:.4f} |",
        "",
        "## Token Use",
        "",
        "Average tokens are estimated as characters / 4.",
        "",
        "| Benchmark | Method | Avg context tokens | Reduction vs raw gold source |",
        "|---|---:|---:|---:|",
        f"| General 150 | Current KG cards | {general['tokens']['current_kg_context']['avg']} | {general['tokens']['current_kg_reduction_vs_raw']}x |",
        f"| General 150 | Graphify query subgraph | {general['tokens']['graphify_query_context']['avg']} | {general['tokens']['graphify_reduction_vs_raw']}x |",
        f"| Multi-axis 175 | Current KG cards | {multi['tokens']['current_kg_context']['avg']} | {multi['tokens']['current_kg_reduction_vs_raw']}x |",
        f"| Multi-axis 175 | Graphify query subgraph | {multi['tokens']['graphify_query_context']['avg']} | {multi['tokens']['graphify_reduction_vs_raw']}x |",
        "",
        "## Reading",
        "",
        "- Current KG is better for RTL module retrieval because it stores Verilog-specific labels, ports, project identity, and instance edges.",
        "- Graphify now works as a general code graph for this workspace, but its Verilog AST output is still thinner than the custom KG: module/file/import/instantiation structure, not domain labels or ports.",
        "- Graphify is most useful as a broad architecture/navigation layer and as a persistent graph skill; the current KG remains the stronger retrieval engine for VerilogEval-style module lookup.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rebuild", action="store_true", help="rebuild graphify-out/graph.json")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    kg = load_kg()
    graph, build_metadata = load_or_build_graphify(kg, rebuild=args.rebuild)

    kg_report = json.loads(KG_REPORT.read_text(encoding="utf-8"))
    general_rows = read_jsonl(GENERAL_BENCH)
    general_runs = json.loads(GENERAL_RUNS.read_text(encoding="utf-8"))["kg"]
    multi_rows = read_jsonl(MULTI_BENCH)
    multi_runs = json.loads(MULTI_RUNS.read_text(encoding="utf-8"))["kg"]

    comparison = {
        "general": compare_set("general", general_rows, general_runs, graph, kg, "difficulty"),
        "multiaxis": compare_set("multiaxis", multi_rows, multi_runs, graph, kg, "type"),
    }

    report = {
        "graphify_build": build_metadata,
        "current_kg": kg_report,
        "comparison": comparison,
        "token_estimate": "characters / 4",
        "notes": [
            "Graphify was compared on the same RTL module source files as the current KG.",
            "Graphify context uses a BFS query subgraph with a 2000-token budget.",
            "Current KG context uses top-3 structured module cards from existing KG retrieval output.",
        ],
    }

    report_path = OUT_DIR / "comparison_report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    write_markdown(report, ROOT / "docs" / "GRAPHIFY_KG_COMPARISON.md")
    print(json.dumps({
        "report": str(report_path),
        "markdown": str(ROOT / "docs" / "GRAPHIFY_KG_COMPARISON.md"),
        "graphify_graph": build_metadata["graph_path"],
        "general_graphify": comparison["general"]["performance"],
        "multiaxis_graphify": comparison["multiaxis"]["performance"],
        "general_tokens": comparison["general"]["tokens"],
        "multiaxis_tokens": comparison["multiaxis"]["tokens"],
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
