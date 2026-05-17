#!/usr/bin/env python3
"""Benchmark long graph-relation queries with in-memory graph indexes vs SQLite recursive CTE."""

from __future__ import annotations

import csv
import json
import re
import sqlite3
import statistics
import time
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Callable


REPO_ROOT = Path(__file__).resolve().parents[2]
TTL_PATH = REPO_ROOT / "dbs" / "graphify-out" / "opentology-current" / ".opentology" / "data" / "current_graph.ttl"
OUT_DIR = REPO_ROOT / "out" / "long_relation_sqlite_eval"

NODE_START_RE = re.compile(r"^<urn:graphify-node:([^>]+)>\s+rdf:type\s+")
NODE_EDGE_RE = re.compile(r"^<urn:graphify-node:([^>]+)>\s+<https://(?:opentology|graphify)\.dev/vocab#([^>]+)>\s+<urn:graphify-node:([^>]+)>\s+\.")
LITERAL_RE = re.compile(r";\s+(?:otx|gfy):([A-Za-z]+)\s+\"([^\"]*)\"")
COMMUNITY_RE = re.compile(r";\s+gfy:community\s+\"?([0-9]+)")


def load_ttl() -> tuple[dict[str, dict], list[tuple[str, str, str]]]:
    nodes: dict[str, dict] = {}
    edges: list[tuple[str, str, str]] = []
    current_id: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_id, current_lines
        if current_id is None:
            return
        block = "\n".join(current_lines)
        node = {"id": current_id}
        for key, value in LITERAL_RE.findall(block):
            if key == "title":
                node["label"] = value
            elif key == "graphifyId":
                node["id"] = value
            elif key == "sourceFile":
                node["source_file"] = value
            elif key == "sourceLocation":
                node["source_location"] = value
        community = COMMUNITY_RE.search(block)
        if community:
            node["community"] = int(community.group(1))
        nodes[node["id"]] = node
        current_id = None
        current_lines = []

    with TTL_PATH.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            line = line.rstrip("\n")
            edge = NODE_EDGE_RE.match(line)
            if edge:
                flush()
                edges.append(edge.groups())
                continue
            start = NODE_START_RE.match(line)
            if start:
                flush()
                current_id = start.group(1)
                current_lines = [line]
                if line.endswith(" ."):
                    flush()
                continue
            if current_id is not None:
                current_lines.append(line)
                if line.endswith(" ."):
                    flush()
    flush()
    return nodes, edges


class MemoryGraph:
    def __init__(self, nodes: dict[str, dict], edges: list[tuple[str, str, str]]) -> None:
        self.nodes = nodes
        self.edges = edges
        self.out: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
        self.inc: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
        for source, relation, target in edges:
            self.out[source][relation].add(target)
            self.inc[target][relation].add(source)

    def label(self, node_id: str) -> str:
        return str(self.nodes.get(node_id, {}).get("label") or node_id)

    def reachable(self, start: str, relation: str, max_depth: int) -> set[str]:
        seen = set()
        queue = deque([(start, 0)])
        while queue:
            node, depth = queue.popleft()
            if depth >= max_depth:
                continue
            for nxt in self.out.get(node, {}).get(relation, set()):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, depth + 1))
        return seen

    def reverse_reachable(self, start: str, relation: str, max_depth: int) -> set[str]:
        seen = set()
        queue = deque([(start, 0)])
        while queue:
            node, depth = queue.popleft()
            if depth >= max_depth:
                continue
            for prev in self.inc.get(node, {}).get(relation, set()):
                if prev not in seen:
                    seen.add(prev)
                    queue.append((prev, depth + 1))
        return seen

    def mixed_reachable(self, start: str, relations: set[str], max_depth: int) -> set[str]:
        seen = set()
        queue = deque([(start, 0)])
        while queue:
            node, depth = queue.popleft()
            if depth >= max_depth:
                continue
            for relation in relations:
                for nxt in self.out.get(node, {}).get(relation, set()):
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append((nxt, depth + 1))
        return seen


def build_sqlite(nodes: dict[str, dict], edges: list[tuple[str, str, str]]) -> tuple[sqlite3.Connection, float]:
    start = time.perf_counter()
    con = sqlite3.connect(":memory:")
    con.execute("PRAGMA temp_store=MEMORY")
    con.execute("PRAGMA journal_mode=OFF")
    con.execute("CREATE TABLE nodes(id TEXT PRIMARY KEY, label TEXT, source_file TEXT, community INTEGER)")
    con.execute("CREATE TABLE edges(source TEXT, relation TEXT, target TEXT)")
    con.executemany(
        "INSERT INTO nodes(id, label, source_file, community) VALUES (?, ?, ?, ?)",
        (
            (
                node_id,
                node.get("label", ""),
                node.get("source_file", ""),
                node.get("community"),
            )
            for node_id, node in nodes.items()
        ),
    )
    con.executemany("INSERT INTO edges(source, relation, target) VALUES (?, ?, ?)", edges)
    con.execute("CREATE INDEX idx_edges_source_relation ON edges(source, relation)")
    con.execute("CREATE INDEX idx_edges_target_relation ON edges(target, relation)")
    con.execute("CREATE INDEX idx_edges_relation ON edges(relation)")
    con.commit()
    return con, time.perf_counter() - start


def sql_reachable(con: sqlite3.Connection, start: str, relation: str, max_depth: int, reverse: bool = False) -> set[str]:
    if reverse:
        join_col, next_col = "target", "source"
    else:
        join_col, next_col = "source", "target"
    query = f"""
    WITH RECURSIVE walk(node, depth) AS (
      SELECT ?, 0
      UNION
      SELECT e.{next_col}, walk.depth + 1
      FROM edges e
      JOIN walk ON e.{join_col} = walk.node
      WHERE e.relation = ? AND walk.depth < ?
    )
    SELECT DISTINCT node FROM walk WHERE depth > 0
    """
    return {row[0] for row in con.execute(query, (start, relation, max_depth))}


def sql_mixed_reachable(con: sqlite3.Connection, start: str, relations: list[str], max_depth: int) -> set[str]:
    placeholders = ",".join("?" for _ in relations)
    query = f"""
    WITH RECURSIVE walk(node, depth) AS (
      SELECT ?, 0
      UNION
      SELECT e.target, walk.depth + 1
      FROM edges e
      JOIN walk ON e.source = walk.node
      WHERE e.relation IN ({placeholders}) AND walk.depth < ?
    )
    SELECT DISTINCT node FROM walk WHERE depth > 0
    """
    return {row[0] for row in con.execute(query, (start, *relations, max_depth))}


def median_time(fn: Callable[[], set[str]], repeats: int = 3) -> tuple[float, set[str]]:
    times = []
    result = set()
    for _ in range(repeats):
        start = time.perf_counter()
        result = fn()
        times.append((time.perf_counter() - start) * 1000)
    return statistics.median(times), result


def top_sources(graph: MemoryGraph, relation: str, n: int) -> list[str]:
    counts = [(node_id, len(graph.out.get(node_id, {}).get(relation, set()))) for node_id in graph.nodes]
    return [node_id for node_id, count in sorted(counts, key=lambda x: (-x[1], x[0]))[:n] if count > 0]


def top_targets(graph: MemoryGraph, relation: str, n: int) -> list[str]:
    counts = [(node_id, len(graph.inc.get(node_id, {}).get(relation, set()))) for node_id in graph.nodes]
    return [node_id for node_id, count in sorted(counts, key=lambda x: (-x[1], x[0]))[:n] if count > 0]


def moderate_sources(graph: MemoryGraph, relation: str, n: int, min_degree: int = 2, max_degree: int = 80) -> list[str]:
    counts = [(node_id, len(graph.out.get(node_id, {}).get(relation, set()))) for node_id in graph.nodes]
    candidates = [(node_id, count) for node_id, count in counts if min_degree <= count <= max_degree]
    return [node_id for node_id, _ in sorted(candidates, key=lambda x: (-x[1], x[0]))[:n]]


def moderate_targets(graph: MemoryGraph, relation: str, n: int, min_degree: int = 2, max_degree: int = 80) -> list[str]:
    counts = [(node_id, len(graph.inc.get(node_id, {}).get(relation, set()))) for node_id in graph.nodes]
    candidates = [(node_id, count) for node_id, count in counts if min_degree <= count <= max_degree]
    return [node_id for node_id, _ in sorted(candidates, key=lambda x: (-x[1], x[0]))[:n]]


def jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    start = time.perf_counter()
    nodes, edges = load_ttl()
    ttl_load_s = time.perf_counter() - start
    graph = MemoryGraph(nodes, edges)
    con, sql_build_s = build_sqlite(nodes, edges)

    cases = []
    for relation in ["contains", "method", "instantiates"]:
        for node_id in moderate_sources(graph, relation, 4, min_degree=2, max_degree=40):
            for depth in [2, 3, 4, 5]:
                cases.append(("forward", relation, node_id, depth))
    for relation in ["contains", "instantiates"]:
        for node_id in moderate_targets(graph, relation, 4, min_degree=2, max_degree=40):
            for depth in [2, 3, 4, 5]:
                cases.append(("reverse", relation, node_id, depth))
    mixed_relations = ["contains", "method", "instantiates", "dependsOn"]
    for node_id in moderate_sources(graph, "contains", 4, min_degree=2, max_degree=20):
        for depth in [2, 3, 4]:
            cases.append(("mixed_forward", "+".join(mixed_relations), node_id, depth))

    rows = []
    for mode, relation, node_id, depth in cases:
        if mode == "forward":
            mem_ms, mem_result = median_time(lambda node_id=node_id, relation=relation, depth=depth: graph.reachable(node_id, relation, depth))
            sql_ms, sql_result = median_time(lambda node_id=node_id, relation=relation, depth=depth: sql_reachable(con, node_id, relation, depth))
        elif mode == "reverse":
            mem_ms, mem_result = median_time(lambda node_id=node_id, relation=relation, depth=depth: graph.reverse_reachable(node_id, relation, depth))
            sql_ms, sql_result = median_time(lambda node_id=node_id, relation=relation, depth=depth: sql_reachable(con, node_id, relation, depth, reverse=True))
        else:
            mem_ms, mem_result = median_time(lambda node_id=node_id, depth=depth: graph.mixed_reachable(node_id, set(mixed_relations), depth))
            sql_ms, sql_result = median_time(lambda node_id=node_id, depth=depth: sql_mixed_reachable(con, node_id, mixed_relations, depth))
        rows.append(
            {
                "mode": mode,
                "relation": relation,
                "node_id": node_id,
                "label": graph.label(node_id),
                "depth": depth,
                "memory_ms": mem_ms,
                "sqlite_ms": sql_ms,
                "sqlite_vs_memory": sql_ms / mem_ms if mem_ms else None,
                "memory_count": len(mem_result),
                "sqlite_count": len(sql_result),
                "jaccard": jaccard(mem_result, sql_result),
            }
        )

    with (OUT_DIR / "long_relation_sqlite_eval_rows.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    summary = {}
    for mode in sorted({row["mode"] for row in rows}):
        subset = [row for row in rows if row["mode"] == mode]
        summary[mode] = {
            "cases": len(subset),
            "memory_median_ms": statistics.median(row["memory_ms"] for row in subset),
            "sqlite_median_ms": statistics.median(row["sqlite_ms"] for row in subset),
            "sqlite_vs_memory_median": statistics.median(row["sqlite_vs_memory"] for row in subset if row["sqlite_vs_memory"] is not None),
            "mean_result_count": statistics.mean(row["memory_count"] for row in subset),
            "mean_jaccard": statistics.mean(row["jaccard"] for row in subset),
        }
    by_depth = {}
    for depth in sorted({row["depth"] for row in rows}):
        subset = [row for row in rows if row["depth"] == depth]
        by_depth[str(depth)] = {
            "cases": len(subset),
            "memory_median_ms": statistics.median(row["memory_ms"] for row in subset),
            "sqlite_median_ms": statistics.median(row["sqlite_ms"] for row in subset),
            "sqlite_vs_memory_median": statistics.median(row["sqlite_vs_memory"] for row in subset if row["sqlite_vs_memory"] is not None),
            "mean_result_count": statistics.mean(row["memory_count"] for row in subset),
        }
    result = {
        "source": str(TTL_PATH),
        "nodes": len(nodes),
        "edges": len(edges),
        "ttl_load_seconds": ttl_load_s,
        "sqlite_build_seconds": sql_build_s,
        "summary_by_mode": summary,
        "summary_by_depth": by_depth,
        "rows": rows,
    }
    (OUT_DIR / "long_relation_sqlite_eval.json").write_text(json.dumps(result, indent=2), encoding="utf-8")

    lines = [
        "# Long Relation Query: OpenTology Graph vs SQLite",
        "",
        "This benchmark focuses on long graph relationships: recursive forward traversal, reverse impact traversal, and mixed structural traversal. It compares an in-memory OpenTology-style adjacency index with SQLite recursive CTE queries over the same edges.",
        "",
        "## Dataset",
        "",
        f"- Nodes: {len(nodes):,}",
        f"- Edges: {len(edges):,}",
        f"- Turtle parse/load: {ttl_load_s:.3f} s",
        f"- SQLite in-memory build + indexes: {sql_build_s:.3f} s",
        f"- Query cases: {len(rows)}",
        "",
        "## By Query Mode",
        "",
        "| Mode | Cases | Memory median | SQLite median | SQLite / Memory | Mean results | Jaccard |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for mode, item in summary.items():
        lines.append(
            f"| {mode} | {item['cases']} | {item['memory_median_ms']:.4f} ms | "
            f"{item['sqlite_median_ms']:.4f} ms | {item['sqlite_vs_memory_median']:.2f}x | "
            f"{item['mean_result_count']:.1f} | {item['mean_jaccard']:.3f} |"
        )
    lines.extend(["", "## By Depth", "", "| Depth | Cases | Memory median | SQLite median | SQLite / Memory | Mean results |", "|---:|---:|---:|---:|---:|---:|"])
    for depth, item in by_depth.items():
        lines.append(
            f"| {depth} | {item['cases']} | {item['memory_median_ms']:.4f} ms | "
            f"{item['sqlite_median_ms']:.4f} ms | {item['sqlite_vs_memory_median']:.2f}x | {item['mean_result_count']:.1f} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- For interactive single-session retrieval, the in-memory graph index is faster for long traversals because it avoids recursive SQL execution overhead.",
            "- SQLite becomes attractive when you want persistence, repeatable SQL reports, joins with metadata tables, filtering/sorting/aggregation, or running many ad-hoc relation queries without custom Python code.",
            "- For very long or heavily filtered queries, SQL can be operationally cleaner even when raw latency is slower.",
            "- A practical hybrid is best: keep Graphify/OpenTology adjacency for fast online traversal, and export edges to SQLite/DuckDB for analytics, dashboards, batch reports, and long relation audits.",
        ]
    )
    report = "\n".join(lines) + "\n"
    (OUT_DIR / "long_relation_sqlite_eval.md").write_text(report, encoding="utf-8")
    html = report.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    html = re.sub(r"^# (.*)$", r"<h1>\1</h1>", html, flags=re.MULTILINE)
    html = re.sub(r"^## (.*)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    (OUT_DIR / "long_relation_sqlite_eval.html").write_text(
        f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Long Relation SQLite Eval</title>
<style>body{{font-family:Segoe UI,Arial,sans-serif;background:#f7f8fb;color:#17202a;letter-spacing:0}}main{{max-width:1100px;margin:0 auto;padding:30px}}table{{border-collapse:collapse;width:100%;background:white}}td,th{{border:1px solid #d8dee8;padding:8px}}th{{background:#edf2f7}}</style>
</head><body><main>{html}</main></body></html>""",
        encoding="utf-8",
    )
    print(json.dumps({k: result[k] for k in ["nodes", "edges", "ttl_load_seconds", "sqlite_build_seconds", "summary_by_mode", "summary_by_depth"]}, indent=2))


if __name__ == "__main__":
    main()
