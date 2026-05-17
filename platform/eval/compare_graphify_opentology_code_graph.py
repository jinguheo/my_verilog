#!/usr/bin/env python3
"""Compare Graphify code graph and OpenTology RDF export for code-graph retrieval tasks."""

from __future__ import annotations

import csv
import json
import re
import statistics
import time
import tracemalloc
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Callable


REPO_ROOT = Path(__file__).resolve().parents[2]
GRAPHIFY_JSON = REPO_ROOT / "dbs" / "graphify-out" / "code-only-graphify" / "graph.json"
OPENTOLOGY_TTL = REPO_ROOT / "dbs" / "graphify-out" / "opentology-current" / ".opentology" / "data" / "current_graph.ttl"
OUT_DIR = REPO_ROOT / "out" / "opentology_graphify_code_eval"

RELATIONS = ["contains", "calls", "instantiates", "defines", "method", "inherits"]
SEARCH_TERMS = ["rv_core_ibex", "ibex", "alert_handler", "uart", "pwrmgr", "rstmgr", "cosim", "csr", "sva", "testplan"]


class GraphStore:
    def __init__(self, name: str, nodes: dict[str, dict], edges: list[tuple[str, str, str]], load_seconds: float, peak_mb: float):
        self.name = name
        self.nodes = nodes
        self.edges = edges
        self.load_seconds = load_seconds
        self.peak_mb = peak_mb
        self.out: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
        self.inc: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
        self.by_community: dict[str, set[str]] = defaultdict(set)
        for source, relation, target in edges:
            self.out[source][relation].add(target)
            self.inc[target][relation].add(source)
        for node_id, node in nodes.items():
            community = node.get("community")
            if community is not None:
                self.by_community[str(community)].add(node_id)

    def outgoing(self, node_id: str, relation: str) -> set[str]:
        return set(self.out.get(node_id, {}).get(relation, set()))

    def incoming(self, node_id: str, relation: str) -> set[str]:
        return set(self.inc.get(node_id, {}).get(relation, set()))

    def search(self, term: str) -> set[str]:
        term = term.lower()
        hits = set()
        for node_id, node in self.nodes.items():
            haystack = " ".join(
                str(node.get(key, ""))
                for key in ("label", "title", "source_file", "sourceFile", "id")
            ).lower()
            if term in haystack:
                hits.add(node_id)
        return hits

    def community(self, node_id: str) -> set[str]:
        community = self.nodes.get(node_id, {}).get("community")
        if community is None:
            return set()
        return set(self.by_community.get(str(community), set()))

    def reverse_reachable(self, node_id: str, relation: str, depth: int = 2, limit: int = 5000) -> set[str]:
        seen = set()
        queue = deque([(node_id, 0)])
        while queue and len(seen) < limit:
            current, dist = queue.popleft()
            if dist >= depth:
                continue
            for parent in self.incoming(current, relation):
                if parent in seen:
                    continue
                seen.add(parent)
                queue.append((parent, dist + 1))
        return seen


def timed_load(name: str, loader: Callable[[], tuple[dict[str, dict], list[tuple[str, str, str]]]]) -> GraphStore:
    tracemalloc.start()
    start = time.perf_counter()
    nodes, edges = loader()
    elapsed = time.perf_counter() - start
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return GraphStore(name, nodes, edges, elapsed, peak / (1024 * 1024))


def load_graphify() -> tuple[dict[str, dict], list[tuple[str, str, str]]]:
    data = json.loads(GRAPHIFY_JSON.read_text(encoding="utf-8"))
    nodes = {}
    for node in data["nodes"]:
        copied = dict(node)
        copied.setdefault("title", copied.get("label", ""))
        nodes[copied["id"]] = copied
    edges = []
    for edge in data.get("links", []):
        source = edge.get("source") or edge.get("_src")
        target = edge.get("target") or edge.get("_tgt")
        relation = edge.get("relation")
        if source and target and relation:
            edges.append((source, relation, target))
    return nodes, edges


NODE_START_RE = re.compile(r"^<urn:graphify-node:([^>]+)>\s+rdf:type\s+")
NODE_EDGE_RE = re.compile(r"^<urn:graphify-node:([^>]+)>\s+<https://(?:opentology|graphify)\.dev/vocab#([^>]+)>\s+<urn:graphify-node:([^>]+)>\s+\.")
LITERAL_RE = re.compile(r";\s+(?:otx|gfy):([A-Za-z]+)\s+\"([^\"]*)\"")
COMMUNITY_RE = re.compile(r";\s+gfy:community\s+\"?([0-9]+)")


def load_opentology_ttl() -> tuple[dict[str, dict], list[tuple[str, str, str]]]:
    nodes: dict[str, dict] = {}
    edges: list[tuple[str, str, str]] = []
    current_id: str | None = None
    current_lines: list[str] = []

    def flush_node() -> None:
        nonlocal current_id, current_lines
        if current_id is None:
            return
        block = "\n".join(current_lines)
        node = {"id": current_id}
        for key, value in LITERAL_RE.findall(block):
            if key == "title":
                node["label"] = value
                node["title"] = value
            elif key == "graphifyId":
                node["id"] = value
            elif key == "sourceFile":
                node["source_file"] = value
            elif key == "sourceLocation":
                node["source_location"] = value
            elif key == "fileType":
                node["file_type"] = value
        community = COMMUNITY_RE.search(block)
        if community:
            node["community"] = int(community.group(1))
        nodes[node["id"]] = node
        current_id = None
        current_lines = []

    with OPENTOLOGY_TTL.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            line = line.rstrip("\n")
            edge_match = NODE_EDGE_RE.match(line)
            if edge_match:
                flush_node()
                edges.append(edge_match.groups())
                continue
            start_match = NODE_START_RE.match(line)
            if start_match:
                flush_node()
                current_id = start_match.group(1)
                current_lines = [line]
                if line.endswith(" ."):
                    flush_node()
                continue
            if current_id is not None:
                current_lines.append(line)
                if line.endswith(" ."):
                    flush_node()
    flush_node()
    return nodes, edges


def median_ms(fn: Callable[[], set[str]], repeats: int = 9) -> tuple[float, set[str]]:
    times = []
    result = set()
    for _ in range(repeats):
        start = time.perf_counter()
        result = fn()
        times.append((time.perf_counter() - start) * 1000)
    return statistics.median(times), result


def jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def choose_relation_cases(store: GraphStore) -> list[tuple[str, str]]:
    cases: list[tuple[str, str]] = []
    for relation in RELATIONS:
        sources = sorted(
            ((node_id, len(targets)) for node_id, targets in ((nid, store.out.get(nid, {}).get(relation, set())) for nid in store.nodes)),
            key=lambda item: (-item[1], item[0]),
        )
        for node_id, count in sources[:10]:
            if count > 0:
                cases.append((relation, node_id))
    return cases


def choose_reverse_cases(store: GraphStore) -> list[tuple[str, str]]:
    cases: list[tuple[str, str]] = []
    for relation in ["calls", "instantiates", "contains"]:
        targets = sorted(
            ((node_id, len(store.inc.get(node_id, {}).get(relation, set()))) for node_id in store.nodes),
            key=lambda item: (-item[1], item[0]),
        )
        for node_id, count in targets[:8]:
            if count > 0:
                cases.append((relation, node_id))
    return cases


def evaluate() -> dict:
    graphify = timed_load("Graphify JSON", load_graphify)
    opentology = timed_load("OpenTology Turtle", load_opentology_ttl)

    relation_cases = choose_relation_cases(graphify)
    reverse_cases = choose_reverse_cases(graphify)
    community_cases = [node_id for _, node_id in relation_cases[:20]]

    rows = []
    summary_by_task: dict[str, list[dict]] = defaultdict(list)

    def record(task: str, query: str, gf_fn: Callable[[], set[str]], ot_fn: Callable[[], set[str]]) -> None:
        gf_ms, gf_result = median_ms(gf_fn)
        ot_ms, ot_result = median_ms(ot_fn)
        row = {
            "task": task,
            "query": query,
            "graphify_ms": gf_ms,
            "opentology_ms": ot_ms,
            "speedup_graphify_vs_opentology": (ot_ms / gf_ms) if gf_ms else None,
            "graphify_count": len(gf_result),
            "opentology_count": len(ot_result),
            "intersection": len(gf_result & ot_result),
            "jaccard": jaccard(gf_result, ot_result),
        }
        rows.append(row)
        summary_by_task[task].append(row)

    for relation, node_id in relation_cases:
        record(
            "direct_relation",
            f"{relation} outgoing from {node_id}",
            lambda relation=relation, node_id=node_id: graphify.outgoing(node_id, relation),
            lambda relation=relation, node_id=node_id: opentology.outgoing(node_id, relation),
        )

    for term in SEARCH_TERMS:
        record(
            "label_source_search",
            term,
            lambda term=term: graphify.search(term),
            lambda term=term: opentology.search(term),
        )

    for relation, node_id in reverse_cases:
        record(
            "reverse_reachable_depth2",
            f"{relation} reverse depth<=2 to {node_id}",
            lambda relation=relation, node_id=node_id: graphify.reverse_reachable(node_id, relation, depth=2),
            lambda relation=relation, node_id=node_id: opentology.reverse_reachable(node_id, relation, depth=2),
        )

    for node_id in community_cases:
        record(
            "community_lookup",
            node_id,
            lambda node_id=node_id: graphify.community(node_id),
            lambda node_id=node_id: opentology.community(node_id),
        )

    task_summary = {}
    for task, task_rows in summary_by_task.items():
        task_summary[task] = {
            "cases": len(task_rows),
            "graphify_median_ms": statistics.median(row["graphify_ms"] for row in task_rows),
            "opentology_median_ms": statistics.median(row["opentology_ms"] for row in task_rows),
            "median_speedup_graphify_vs_opentology": statistics.median(row["speedup_graphify_vs_opentology"] for row in task_rows if row["speedup_graphify_vs_opentology"] is not None),
            "mean_jaccard": statistics.mean(row["jaccard"] for row in task_rows),
            "mean_graphify_count": statistics.mean(row["graphify_count"] for row in task_rows),
            "mean_opentology_count": statistics.mean(row["opentology_count"] for row in task_rows),
        }

    result = {
        "inputs": {
            "graphify_json": str(GRAPHIFY_JSON),
            "opentology_ttl": str(OPENTOLOGY_TTL),
            "graphify_json_bytes": GRAPHIFY_JSON.stat().st_size,
            "opentology_ttl_bytes": OPENTOLOGY_TTL.stat().st_size,
        },
        "stores": {
            "graphify": {
                "nodes": len(graphify.nodes),
                "edges": len(graphify.edges),
                "load_seconds": graphify.load_seconds,
                "peak_load_mb": graphify.peak_mb,
                "relation_counts": dict(Counter(relation for _, relation, _ in graphify.edges).most_common()),
            },
            "opentology": {
                "nodes": len(opentology.nodes),
                "edges": len(opentology.edges),
                "load_seconds": opentology.load_seconds,
                "peak_load_mb": opentology.peak_mb,
                "relation_counts": dict(Counter(relation for _, relation, _ in opentology.edges).most_common()),
            },
        },
        "task_summary": task_summary,
        "rows": rows,
        "notes": [
            "OpenTology here is evaluated as the local RDF/Turtle export generated from the Graphify code graph.",
            "The OpenTology CLI SPARQL smoke query took about 70 seconds and returned 0 triples in this workspace state, so detailed query timing uses a direct Turtle parser over current_graph.ttl.",
            "Both stores were converted into in-memory adjacency indexes after load; load cost and query cost are reported separately.",
        ],
    }
    return result


def write_report(result: dict) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "graphify_vs_opentology_code_eval.json").write_text(json.dumps(result, indent=2), encoding="utf-8")

    with (OUT_DIR / "graphify_vs_opentology_code_eval_rows.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(result["rows"][0].keys()))
        writer.writeheader()
        writer.writerows(result["rows"])

    lines = [
        "# Graphify vs OpenTology Code Graph Evaluation",
        "",
        "This evaluation compares the local Graphify code graph JSON with the local OpenTology RDF/Turtle export generated from that graph. No LLM/API calls were used.",
        "",
        "## Input Size and Load Cost",
        "",
        "| Metric | Graphify JSON | OpenTology Turtle |",
        "|---|---:|---:|",
        f"| File size | {result['inputs']['graphify_json_bytes'] / (1024*1024):.2f} MB | {result['inputs']['opentology_ttl_bytes'] / (1024*1024):.2f} MB |",
        f"| Nodes parsed | {result['stores']['graphify']['nodes']:,} | {result['stores']['opentology']['nodes']:,} |",
        f"| Edges parsed | {result['stores']['graphify']['edges']:,} | {result['stores']['opentology']['edges']:,} |",
        f"| Load time | {result['stores']['graphify']['load_seconds']:.3f} s | {result['stores']['opentology']['load_seconds']:.3f} s |",
        f"| Peak Python load memory | {result['stores']['graphify']['peak_load_mb']:.1f} MB | {result['stores']['opentology']['peak_load_mb']:.1f} MB |",
        "",
        "## Query Performance",
        "",
        "| Task | Cases | Graphify median | OpenTology median | Graphify speedup | Mean result Jaccard |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for task, summary in result["task_summary"].items():
        lines.append(
            f"| {task} | {summary['cases']} | {summary['graphify_median_ms']:.4f} ms | "
            f"{summary['opentology_median_ms']:.4f} ms | {summary['median_speedup_graphify_vs_opentology']:.2f}x | "
            f"{summary['mean_jaccard']:.3f} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Graphify is the better default for fast retrieval and exploration because its JSON graph already carries the original extraction metadata, relation confidence, weights, communities, and HTML/graph-view tooling.",
            "- OpenTology is better when you need a typed ontology layer, RDF interoperability, SPARQL-style governance queries, persistent project memory, decisions, issues, and agent workflow hooks.",
            "- In this workspace, OpenTology is not adding new code facts beyond the Graphify-derived export; it mainly changes the representation and query model.",
            "- For Verilog module lookup, instantiation navigation, and spec-code retrieval, Graphify/custom KG should remain the primary engine.",
            "- For impact analysis, exact dependency/path queries, and future session/decision memory, OpenTology can be useful as an auxiliary layer once the local triplestore query path is stable.",
            "",
            "## Caveats",
            "",
            "- The OpenTology CLI SPARQL smoke query was slow and returned zero triples in the current local workspace state, so the detailed timing uses a direct parser over `current_graph.ttl`.",
            "- The comparison is therefore a storage/query-model benchmark, not a full OpenTology MCP-agent workflow benchmark.",
            "- Because OpenTology was generated from Graphify here, retrieval quality cannot exceed the underlying Graphify extraction unless additional OpenTology memory/decision data is added later.",
        ]
    )
    report = "\n".join(lines) + "\n"
    (OUT_DIR / "graphify_vs_opentology_code_eval.md").write_text(report, encoding="utf-8")

    html = report
    html = html.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    html = re.sub(r"^# (.*)$", r"<h1>\1</h1>", html, flags=re.MULTILINE)
    html = re.sub(r"^## (.*)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    html = re.sub(r"^- (.*)$", r"<li>\1</li>", html, flags=re.MULTILINE)
    html = html.replace("\n\n", "\n")
    (OUT_DIR / "graphify_vs_opentology_code_eval.html").write_text(
        f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Graphify vs OpenTology Code Evaluation</title>
  <style>
    body {{ margin: 0; font-family: Segoe UI, Arial, sans-serif; background: #f7f8fb; color: #17202a; letter-spacing: 0; }}
    main {{ max-width: 1080px; margin: 0 auto; padding: 30px; }}
    h1 {{ font-size: 28px; }}
    h2 {{ margin-top: 28px; border-bottom: 1px solid #d8dee8; padding-bottom: 8px; }}
    table {{ border-collapse: collapse; width: 100%; background: white; }}
    th, td {{ border: 1px solid #d8dee8; padding: 8px 10px; text-align: left; }}
    th {{ background: #edf2f7; }}
    li {{ line-height: 1.55; margin: 5px 0; }}
  </style>
</head>
<body><main>{html}</main></body>
</html>
""",
        encoding="utf-8",
    )


def main() -> None:
    result = evaluate()
    write_report(result)
    print(json.dumps(
        {
            "out_dir": str(OUT_DIR),
            "graphify_load_s": result["stores"]["graphify"]["load_seconds"],
            "opentology_load_s": result["stores"]["opentology"]["load_seconds"],
            "task_summary": result["task_summary"],
        },
        indent=2,
    ))


if __name__ == "__main__":
    main()
