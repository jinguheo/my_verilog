#!/usr/bin/env python3
"""Remove deterministic document nodes from a Graphify graph and rebuild report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def rebuild_report(graph_path: Path, root: Path) -> None:
    from graphify.analyze import god_nodes, suggest_questions, surprising_connections
    from graphify.build import build_from_json
    from graphify.cluster import cluster, score_all
    from graphify.export import to_json
    from graphify.report import generate

    raw = json.loads(graph_path.read_text(encoding="utf-8"))
    graph = build_from_json(raw)
    communities = cluster(graph)
    cohesion = score_all(graph, communities)
    labels = {cid: f"Community {cid}" for cid in communities}
    questions = suggest_questions(graph, communities, labels)
    report = generate(
        graph,
        communities,
        cohesion,
        labels,
        god_nodes(graph),
        surprising_connections(graph, communities),
        {
            "total_files": len({n.get("source_file") for n in raw.get("nodes", []) if n.get("source_file")}),
            "total_words": 0,
            "warning": "Document nodes removed; code/rationale graph retained.",
        },
        {"input": 0, "output": 0},
        str(root),
        suggested_questions=questions,
    )
    (graph_path.parent / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    to_json(graph, communities, str(graph_path))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph", required=True)
    parser.add_argument("--root", required=True)
    parser.add_argument("--rebuild-report", action="store_true")
    args = parser.parse_args()

    graph_path = Path(args.graph)
    raw = json.loads(graph_path.read_text(encoding="utf-8"))
    nodes = raw.get("nodes", [])
    links = raw.get("links", [])

    remove_ids = {node.get("id") for node in nodes if node.get("file_type") == "document"}
    raw["nodes"] = [node for node in nodes if node.get("id") not in remove_ids]
    raw["links"] = [
        edge
        for edge in links
        if edge.get("source") not in remove_ids and edge.get("target") not in remove_ids
    ]

    graph_path.write_text(json.dumps(raw, ensure_ascii=False), encoding="utf-8")
    if args.rebuild_report:
        rebuild_report(graph_path, Path(args.root))

    print(
        json.dumps(
            {
                "status": "ok",
                "removed_nodes": len(remove_ids),
                "removed_links": len(links) - len(raw["links"]),
                "remaining_nodes": len(raw["nodes"]),
                "remaining_links": len(raw["links"]),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
