#!/usr/bin/env python3
"""Build and evaluate an OpenTology-friendly relation/query benchmark."""

from __future__ import annotations

import csv
import json
import re
import statistics
import time
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Callable


REPO_ROOT = Path(__file__).resolve().parents[2]
TTL_PATH = REPO_ROOT / "dbs" / "graphify-out" / "opentology-current" / ".opentology" / "data" / "current_graph.ttl"
OUT_DIR = REPO_ROOT / "out" / "opentology_relation_query_eval"

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

    with TTL_PATH.open("r", encoding="utf-8", errors="replace") as handle:
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


class Store:
    def __init__(self, nodes: dict[str, dict], edges: list[tuple[str, str, str]]) -> None:
        self.nodes = nodes
        self.edges = edges
        self.out: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
        self.inc: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
        self.communities: dict[str, set[str]] = defaultdict(set)
        for source, relation, target in edges:
            self.out[source][relation].add(target)
            self.inc[target][relation].add(source)
        for node_id, node in nodes.items():
            if node.get("community") is not None:
                self.communities[str(node["community"])].add(node_id)

    def label(self, node_id: str) -> str:
        node = self.nodes.get(node_id, {})
        return str(node.get("label") or node.get("title") or node_id)

    def source(self, node_id: str) -> str:
        node = self.nodes.get(node_id, {})
        source = str(node.get("source_file") or "")
        loc = str(node.get("source_location") or "")
        return f"{source}:{loc}" if loc else source

    def direct(self, source: str, relation: str) -> set[str]:
        return set(self.out.get(source, {}).get(relation, set()))

    def reverse(self, target: str, relation: str) -> set[str]:
        return set(self.inc.get(target, {}).get(relation, set()))

    def reachable(self, source: str, relation: str, depth: int = 3, limit: int = 1000) -> set[str]:
        seen = set()
        queue = deque([(source, 0)])
        while queue and len(seen) < limit:
            current, dist = queue.popleft()
            if dist >= depth:
                continue
            for nxt in self.direct(current, relation):
                if nxt in seen:
                    continue
                seen.add(nxt)
                queue.append((nxt, dist + 1))
        return seen

    def reverse_reachable(self, target: str, relation: str, depth: int = 3, limit: int = 1000) -> set[str]:
        seen = set()
        queue = deque([(target, 0)])
        while queue and len(seen) < limit:
            current, dist = queue.popleft()
            if dist >= depth:
                continue
            for prev in self.reverse(current, relation):
                if prev in seen:
                    continue
                seen.add(prev)
                queue.append((prev, dist + 1))
        return seen

    def shortest_path(self, source: str, target: str, relations: set[str], max_depth: int = 4) -> list[str]:
        queue = deque([[source]])
        seen = {source}
        while queue:
            path = queue.popleft()
            current = path[-1]
            if len(path) > max_depth + 1:
                continue
            for relation in relations:
                for nxt in self.direct(current, relation):
                    if nxt == target:
                        return path + [nxt]
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append(path + [nxt])
        return []

    def community_peers(self, node_id: str, limit: int = 25) -> set[str]:
        community = self.nodes.get(node_id, {}).get("community")
        if community is None:
            return set()
        peers = set(self.communities.get(str(community), set()))
        peers.discard(node_id)
        return set(sorted(peers)[:limit])


def sparql_for(kind: str, node_id: str, relation: str | None = None, target_id: str | None = None) -> str:
    uri = f"<urn:graphify-node:{node_id}>"
    pred = f"otx:{relation}" if relation in {"contains", "calls", "dependsOn", "defines", "inherits"} else f"gfy:{relation}"
    if kind == "direct":
        return f"SELECT ?target WHERE {{ {uri} {pred} ?target . }}"
    if kind == "reverse":
        return f"SELECT ?source WHERE {{ ?source {pred} {uri} . }}"
    if kind == "reachable":
        return f"SELECT ?target WHERE {{ {uri} {pred}+ ?target . }}"
    if kind == "reverse_reachable":
        return f"SELECT ?source WHERE {{ ?source {pred}+ {uri} . }}"
    if kind == "community":
        return f"SELECT ?peer WHERE {{ {uri} gfy:community ?c . ?peer gfy:community ?c . FILTER(?peer != {uri}) }}"
    if kind == "path" and target_id:
        return f"ASK {{ {uri} (otx:contains|gfy:method|otx:dependsOn|gfy:instantiates)+ <urn:graphify-node:{target_id}> . }}"
    return "SELECT * WHERE { ?s ?p ?o } LIMIT 10"


def top_sources(store: Store, relation: str, n: int) -> list[str]:
    items = [(node_id, len(store.direct(node_id, relation))) for node_id in store.nodes]
    return [node_id for node_id, count in sorted(items, key=lambda x: (-x[1], x[0]))[:n] if count > 0]


def top_targets(store: Store, relation: str, n: int) -> list[str]:
    items = [(node_id, len(store.reverse(node_id, relation))) for node_id in store.nodes]
    return [node_id for node_id, count in sorted(items, key=lambda x: (-x[1], x[0]))[:n] if count > 0]


def timed(fn: Callable[[], set[str] | list[str]], repeats: int = 7) -> tuple[float, set[str] | list[str]]:
    times = []
    result: set[str] | list[str] = set()
    for _ in range(repeats):
        start = time.perf_counter()
        result = fn()
        times.append((time.perf_counter() - start) * 1000)
    return statistics.median(times), result


def build_questions(store: Store) -> list[dict]:
    questions: list[dict] = []

    for relation in ["calls", "instantiates", "contains", "method", "inherits", "defines"]:
        for node_id in top_sources(store, relation, 6):
            questions.append(
                {
                    "id": f"direct_{relation}_{len(questions)+1:03d}",
                    "category": "direct_relation",
                    "question": f"Which nodes does `{store.label(node_id)}` directly `{relation}`?",
                    "node_id": node_id,
                    "relation": relation,
                    "sparql": sparql_for("direct", node_id, relation),
                    "answer_ids": sorted(store.direct(node_id, relation)),
                }
            )

    for relation in ["calls", "instantiates", "contains", "inherits"]:
        for node_id in top_targets(store, relation, 6):
            questions.append(
                {
                    "id": f"reverse_{relation}_{len(questions)+1:03d}",
                    "category": "reverse_relation",
                    "question": f"Which nodes directly point to `{store.label(node_id)}` via `{relation}`?",
                    "node_id": node_id,
                    "relation": relation,
                    "sparql": sparql_for("reverse", node_id, relation),
                    "answer_ids": sorted(store.reverse(node_id, relation)),
                }
            )

    for relation in ["calls", "contains", "method"]:
        for node_id in top_sources(store, relation, 5):
            questions.append(
                {
                    "id": f"reachable_{relation}_{len(questions)+1:03d}",
                    "category": "transitive_reachable",
                    "question": f"Within depth 3, what can `{store.label(node_id)}` reach through repeated `{relation}` edges?",
                    "node_id": node_id,
                    "relation": relation,
                    "sparql": sparql_for("reachable", node_id, relation),
                    "answer_ids": sorted(store.reachable(node_id, relation, depth=3)),
                }
            )

    for relation in ["calls", "contains"]:
        for node_id in top_targets(store, relation, 6):
            questions.append(
                {
                    "id": f"impact_{relation}_{len(questions)+1:03d}",
                    "category": "impact_reverse_reachable",
                    "question": f"Within depth 3, what upstream nodes could be impacted by changing `{store.label(node_id)}` through `{relation}` edges?",
                    "node_id": node_id,
                    "relation": relation,
                    "sparql": sparql_for("reverse_reachable", node_id, relation),
                    "answer_ids": sorted(store.reverse_reachable(node_id, relation, depth=3)),
                }
            )

    path_sources = top_sources(store, "contains", 12)
    for source in path_sources:
        reachable = sorted(store.reachable(source, "contains", depth=3))
        if not reachable:
            continue
        target = reachable[min(len(reachable) - 1, 3)]
        path = store.shortest_path(source, target, {"contains", "method", "dependsOn", "instantiates"}, max_depth=4)
        questions.append(
            {
                "id": f"path_{len(questions)+1:03d}",
                "category": "path_query",
                "question": f"Is there a short structural path from `{store.label(source)}` to `{store.label(target)}`?",
                "node_id": source,
                "target_id": target,
                "relation": "mixed_path",
                "sparql": sparql_for("path", source, target_id=target),
                "answer_ids": path,
            }
        )

    for node_id in top_sources(store, "contains", 12):
        questions.append(
            {
                "id": f"community_{len(questions)+1:03d}",
                "category": "community_peers",
                "question": f"Which nodes are in the same Graphify community as `{store.label(node_id)}`?",
                "node_id": node_id,
                "relation": "community",
                "sparql": sparql_for("community", node_id),
                "answer_ids": sorted(store.community_peers(node_id, limit=25)),
            }
        )

    return questions[:120]


def evaluate_question(store: Store, q: dict) -> tuple[float, list[str]]:
    category = q["category"]
    relation = q.get("relation")
    node_id = q["node_id"]
    if category == "direct_relation":
        ms, result = timed(lambda: store.direct(node_id, relation))
    elif category == "reverse_relation":
        ms, result = timed(lambda: store.reverse(node_id, relation))
    elif category == "transitive_reachable":
        ms, result = timed(lambda: store.reachable(node_id, relation, depth=3))
    elif category == "impact_reverse_reachable":
        ms, result = timed(lambda: store.reverse_reachable(node_id, relation, depth=3))
    elif category == "community_peers":
        ms, result = timed(lambda: store.community_peers(node_id, limit=25))
    elif category == "path_query":
        target = q["target_id"]
        ms, result = timed(lambda: store.shortest_path(node_id, target, {"contains", "method", "dependsOn", "instantiates"}, max_depth=4))
    else:
        ms, result = 0.0, []
    return ms, sorted(result) if isinstance(result, set) else list(result)


def write_outputs(store: Store, questions: list[dict], rows: list[dict], load_seconds: float) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "opentology_relation_questions.json").write_text(json.dumps(questions, indent=2), encoding="utf-8")
    (OUT_DIR / "opentology_relation_eval_results.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")

    with (OUT_DIR / "opentology_relation_eval_results.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "id",
                "category",
                "question",
                "relation",
                "answer_count",
                "eval_ms",
                "top_answers",
                "sparql",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    category_counts = Counter(q["category"] for q in questions)
    category_stats = {}
    for category in category_counts:
        subset = [row for row in rows if row["category"] == category]
        category_stats[category] = {
            "questions": len(subset),
            "median_eval_ms": statistics.median(float(row["eval_ms"]) for row in subset),
            "mean_answer_count": statistics.mean(int(row["answer_count"]) for row in subset),
        }

    examples = rows[:12]
    lines = [
        "# OpenTology-Friendly Relation Query Benchmark",
        "",
        "This benchmark is intentionally shaped around what OpenTology should be good at: exact graph relation queries, reverse impact queries, transitive reachability, path checks, and community/typed graph lookups.",
        "",
        "No LLM/API calls were used. The benchmark uses the local OpenTology Turtle export.",
        "",
        "## Summary",
        "",
        f"- Source: `{TTL_PATH}`",
        f"- Nodes: {len(store.nodes):,}",
        f"- Edges: {len(store.edges):,}",
        f"- Load time: {load_seconds:.3f} s",
        f"- Questions: {len(questions)}",
        "",
        "## Question Mix",
        "",
        "| Category | Questions | Median eval time | Mean answer count |",
        "|---|---:|---:|---:|",
    ]
    for category, stats in category_stats.items():
        lines.append(
            f"| {category} | {stats['questions']} | {stats['median_eval_ms']:.4f} ms | {stats['mean_answer_count']:.1f} |"
        )
    lines.extend(
        [
            "",
            "## Example Questions",
            "",
            "| ID | Category | Question | Answers |",
            "|---|---|---|---:|",
        ]
    )
    for row in examples:
        question = row["question"].replace("|", "\\|")
        lines.append(f"| {row['id']} | {row['category']} | {question} | {row['answer_count']} |")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- These questions are better suited to OpenTology than broad semantic retrieval because they can be expressed as exact RDF/SPARQL patterns.",
            "- Strong categories: direct relation lookup, reverse relation lookup, transitive reachability, impact-style reverse traversal, and explicit path existence.",
            "- Weak categories remain natural-language design explanation, fuzzy spec-code matching, and Verilog generation context; those still need Graphify/custom KG plus retrieval scoring.",
            "- In the current workspace, OpenTology facts are derived from Graphify, so this benchmark evaluates the query/ontology layer, not new extraction quality.",
        ]
    )
    report = "\n".join(lines) + "\n"
    (OUT_DIR / "opentology_relation_query_benchmark.md").write_text(report, encoding="utf-8")

    html = report.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    html = re.sub(r"^# (.*)$", r"<h1>\1</h1>", html, flags=re.MULTILINE)
    html = re.sub(r"^## (.*)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    html = re.sub(r"^- (.*)$", r"<li>\1</li>", html, flags=re.MULTILINE)
    (OUT_DIR / "opentology_relation_query_benchmark.html").write_text(
        f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>OpenTology Relation Query Benchmark</title>
  <style>
    body {{ margin: 0; font-family: Segoe UI, Arial, sans-serif; background: #f7f8fb; color: #17202a; letter-spacing: 0; }}
    main {{ max-width: 1100px; margin: 0 auto; padding: 30px; }}
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
    start = time.perf_counter()
    nodes, edges = load_opentology_ttl()
    load_seconds = time.perf_counter() - start
    store = Store(nodes, edges)
    questions = build_questions(store)
    rows = []
    for q in questions:
        ms, actual = evaluate_question(store, q)
        top = []
        for answer_id in actual[:8]:
            label = store.label(answer_id)
            source = store.source(answer_id)
            top.append(f"{label} [{answer_id}] {source}".strip())
        rows.append(
            {
                "id": q["id"],
                "category": q["category"],
                "question": q["question"],
                "relation": q.get("relation", ""),
                "answer_count": len(actual),
                "eval_ms": f"{ms:.6f}",
                "top_answers": " ; ".join(top),
                "sparql": q["sparql"],
            }
        )
    write_outputs(store, questions, rows, load_seconds)
    print(json.dumps(
        {
            "out_dir": str(OUT_DIR),
            "questions": len(questions),
            "load_seconds": load_seconds,
            "category_counts": Counter(q["category"] for q in questions),
        },
        indent=2,
    ))


if __name__ == "__main__":
    main()
