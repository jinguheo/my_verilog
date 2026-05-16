#!/usr/bin/env python3
"""Assemble three Graphify-compatible KG variants.

Outputs:
- spec-only-graphify: deterministic spec document graph
- code-only-graphify: current code/rationale Graphify graph snapshot
- spec-code-graphify: merged spec + code graph with late-binding edges
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_GRAPHIFY_ROOT = ROOT / "dbs" / "graphify-out"
DEFAULT_SPEC_GRAPH = DEFAULT_GRAPHIFY_ROOT / "spec-only-graphify" / "graph.json"
DEFAULT_CODE_GRAPH = DEFAULT_GRAPHIFY_ROOT / "graph.json"

GENERIC_COMPONENTS = {
    "about",
    "api",
    "build",
    "checklist",
    "code",
    "common",
    "config",
    "configuration",
    "contributing",
    "data",
    "debug",
    "design",
    "doc",
    "docs",
    "example",
    "examples",
    "file",
    "getting_started",
    "hardware",
    "index",
    "integration",
    "interfaces",
    "license",
    "lowrisc",
    "opentitan",
    "overview",
    "readme",
    "registers",
    "security",
    "setup",
    "software",
    "specification",
    "style",
    "system",
    "test",
    "testing",
    "tools",
    "verification",
}


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9_]+", "_", text.lower()).strip("_")


def source_tokens(source_file: str) -> set[str]:
    source = source_file.replace("\\", "/").lower()
    parts = re.split(r"[^a-z0-9_]+", source)
    tokens = {part for part in parts if len(part) >= 3}
    for marker in ("/hw/ip/", "/ip_autogen/", "/vendor/"):
        if marker in source:
            tail = source.split(marker, 1)[1]
            first = tail.split("/", 1)[0]
            if first:
                tokens.add(first)
    return tokens


def edge_key(edge: dict[str, Any]) -> tuple[str, str, str]:
    src = str(edge.get("source") or edge.get("_src"))
    tgt = str(edge.get("target") or edge.get("_tgt"))
    rel = str(edge.get("relation") or edge.get("type") or "related")
    return src, tgt, rel


def prefix_spec_graph(spec_graph: dict[str, Any], prefix: str = "spec__") -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    nodes = []
    for node in spec_graph.get("nodes", []):
        copied = dict(node)
        copied["id"] = prefix + str(node["id"])
        copied["graph_variant"] = "spec"
        copied["source_file"] = str(copied.get("source_file") or "").replace("\\", "/")
        if "community" in copied and isinstance(copied["community"], int):
            copied["community"] = copied["community"] + 100000
        nodes.append(copied)

    links = []
    for edge in spec_graph.get("links", []):
        copied = dict(edge)
        src = prefix + str(edge.get("source") or edge.get("_src"))
        tgt = prefix + str(edge.get("target") or edge.get("_tgt"))
        copied["_src"] = src
        copied["_tgt"] = tgt
        copied["source"] = src
        copied["target"] = tgt
        copied["graph_variant"] = "spec"
        copied["source_file"] = str(copied.get("source_file") or "").replace("\\", "/")
        links.append(copied)
    return nodes, links


def copy_code_graph(code_graph: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    nodes = []
    for node in code_graph.get("nodes", []):
        copied = dict(node)
        copied["graph_variant"] = "code"
        nodes.append(copied)
    links = []
    for edge in code_graph.get("links", []):
        copied = dict(edge)
        copied["graph_variant"] = "code"
        links.append(copied)
    return nodes, links


def make_late_binding_edges(spec_nodes: list[dict[str, Any]], code_nodes: list[dict[str, Any]], max_per_component: int) -> list[dict[str, Any]]:
    code_by_token: dict[str, list[dict[str, Any]]] = defaultdict(list)
    code_by_label: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for node in code_nodes:
        label = str(node.get("label") or "")
        source_file = str(node.get("source_file") or "")
        file_type = str(node.get("file_type") or "")
        if file_type not in {"code", "rationale"}:
            continue
        code_by_label[norm(label)].append(node)
        for token in source_tokens(source_file):
            code_by_token[token].append(node)

    edges: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()

    def add(src: str, tgt: str, relation: str, source_file: str, weight: float, confidence_score: float) -> None:
        key = (src, tgt, relation)
        if key in seen:
            return
        seen.add(key)
        edges.append(
            {
                "relation": relation,
                "confidence": "INFERRED",
                "confidence_score": confidence_score,
                "source_file": source_file,
                "source_location": "L1",
                "weight": weight,
                "_src": src,
                "_tgt": tgt,
                "source": src,
                "target": tgt,
                "graph_variant": "spec-code",
            }
        )

    component_nodes = [
        node
        for node in spec_nodes
        if node.get("role") == "component" and str(node.get("label", "")).startswith("component:")
    ]
    for spec_node in component_nodes:
        component = str(spec_node["label"]).split(":", 1)[1]
        token = norm(component)
        if not token or token in GENERIC_COMPONENTS:
            continue
        candidates = list(code_by_token.get(token, []))
        candidates += code_by_label.get(token, [])
        unique = {str(node["id"]): node for node in candidates}
        ranked = sorted(
            unique.values(),
            key=lambda node: (
                str(node.get("source_file", "")).lower().endswith((".sv", ".v", ".svh", ".vh")),
                token in norm(str(node.get("label", ""))),
                len(str(node.get("source_file", ""))),
            ),
            reverse=True,
        )
        for code_node in ranked[:max_per_component]:
            add(
                str(spec_node["id"]),
                str(code_node["id"]),
                "spec_component_matches_code",
                str(spec_node.get("source_file") or ""),
                1.8,
                0.76,
            )

    # Link exact spec document stems to code source files when the same IP/module
    # token appears in both paths. This catches docs that do not produce clean
    # component nodes.
    spec_docs = [node for node in spec_nodes if node.get("role") == "document"]
    code_files_by_token: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for node in code_nodes:
        source_file = str(node.get("source_file") or "")
        if not source_file.lower().endswith((".sv", ".v", ".svh", ".vh")):
            continue
        for token in source_tokens(source_file):
            if token not in GENERIC_COMPONENTS:
                code_files_by_token[token].append(node)

    for spec_doc in spec_docs:
        spec_source = str(spec_doc.get("source_file") or "")
        tokens = [token for token in source_tokens(spec_source) if token not in GENERIC_COMPONENTS]
        linked = 0
        for token in tokens:
            for code_node in code_files_by_token.get(token, [])[:8]:
                add(
                    str(spec_doc["id"]),
                    str(code_node["id"]),
                    "spec_path_matches_code_path",
                    spec_source,
                    1.2,
                    0.68,
                )
                linked += 1
                if linked >= 16:
                    break
            if linked >= 16:
                break
    return edges


def summarize_graph(nodes: list[dict[str, Any]], links: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "nodes": len(nodes),
        "links": len(links),
        "file_types": dict(Counter(str(node.get("file_type") or "") for node in nodes).most_common()),
        "roles": dict(Counter(str(node.get("role") or "") for node in nodes if node.get("role")).most_common(20)),
        "relations": dict(Counter(str(edge.get("relation") or edge.get("type") or "related") for edge in links).most_common()),
        "variants": dict(Counter(str(node.get("graph_variant") or "") for node in nodes).most_common()),
        "communities": len({node.get("community") for node in nodes if node.get("community") is not None}),
    }


def write_report(path: Path, title: str, summary: dict[str, Any], notes: list[str]) -> None:
    lines = [
        f"# {title}",
        "",
        f"- Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"- Nodes: {summary['nodes']}",
        f"- Links: {summary['links']}",
        f"- Communities: {summary['communities']}",
        "",
        "## Notes",
        "",
    ]
    lines.extend(f"- {note}" for note in notes)
    lines += [
        "",
        "## Relations",
        "",
        "| Relation | Links |",
        "|---|---:|",
    ]
    for relation, count in summary["relations"].items():
        lines.append(f"| {relation} | {count} |")
    lines += ["", "## File Types", "", "| File type | Nodes |", "|---|---:|"]
    for file_type, count in summary["file_types"].items():
        lines.append(f"| {file_type or '<none>'} | {count} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def prepare_code_only(code_graph_path: Path, graphify_root: Path) -> dict[str, Any]:
    out_dir = graphify_root / "code-only-graphify"
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(code_graph_path, out_dir / "graph.json")
    report = graphify_root / "GRAPH_REPORT.md"
    if report.exists():
        shutil.copy2(report, out_dir / "GRAPH_REPORT.md")
    graph = read_json(code_graph_path)
    summary = summarize_graph(graph.get("nodes", []), graph.get("links", []))
    manifest = {
        "status": "ok",
        "variant": "code-only",
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "out_dir": str(out_dir),
        "graph_json": str(out_dir / "graph.json"),
        "report": str(out_dir / "GRAPH_REPORT.md"),
        "html": "not generated; graph is too large for Graphify HTML viz",
        **summary,
    }
    write_json(out_dir / "code_only_graphify_manifest.json", manifest)
    return manifest


def build_spec_code(spec_graph_path: Path, code_graph_path: Path, graphify_root: Path, max_per_component: int) -> dict[str, Any]:
    out_dir = graphify_root / "spec-code-graphify"
    out_dir.mkdir(parents=True, exist_ok=True)
    spec_graph = read_json(spec_graph_path)
    code_graph = read_json(code_graph_path)

    code_nodes, code_links = copy_code_graph(code_graph)
    spec_nodes, spec_links = prefix_spec_graph(spec_graph)
    bridge_links = make_late_binding_edges(spec_nodes, code_nodes, max_per_component)

    nodes = code_nodes + spec_nodes
    links_by_key: dict[tuple[str, str, str], dict[str, Any]] = {}
    for edge in code_links + spec_links + bridge_links:
        links_by_key[edge_key(edge)] = edge
    links = list(links_by_key.values())

    payload = {
        "directed": False,
        "multigraph": False,
        "graph": {
            "variant": "spec-code",
            "created_at": datetime.now().isoformat(timespec="seconds"),
            "late_binding": "spec component/path nodes connected to code nodes by inferred edges",
        },
        "nodes": nodes,
        "links": links,
        "hyperedges": [],
    }
    write_json(out_dir / "graph.json", payload)
    summary = summarize_graph(nodes, links)
    summary["bridge_links"] = dict(Counter(str(edge.get("relation")) for edge in bridge_links))

    write_report(
        out_dir / "GRAPH_REPORT.md",
        "Spec-Code Graphify KG",
        summary,
        [
            "This is a Graphify-compatible merged graph.",
            "Code nodes come from the current code-only Graphify graph.",
            "Spec nodes come from the deterministic spec-only Graphify graph and are prefixed with spec__.",
            "Late-binding edges are inferred from component names, source paths, and exact label/path token overlap.",
            "HTML visualization is not generated because the merged graph is too large for Graphify's HTML exporter.",
        ],
    )
    (out_dir / "HTML_SKIPPED.txt").write_text(
        "Graph is too large for Graphify HTML viz. Use graph.json or graph.graphml-compatible tools.\n",
        encoding="utf-8",
    )
    manifest = {
        "status": "ok",
        "variant": "spec-code",
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "out_dir": str(out_dir),
        "graph_json": str(out_dir / "graph.json"),
        "report": str(out_dir / "GRAPH_REPORT.md"),
        "html": "skipped: merged graph is too large for Graphify HTML viz",
        **summary,
    }
    write_json(out_dir / "spec_code_graphify_manifest.json", manifest)
    return manifest


def write_top_manifest(graphify_root: Path, manifests: list[dict[str, Any]]) -> None:
    write_json(
        graphify_root / "graphify_three_variants_manifest.json",
        {
            "status": "ok",
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "variants": manifests,
        },
    )
    rows = []
    for item in manifests:
        rows.append(
            "| {variant} | {nodes} | {links} | {graph} | {report} |".format(
                variant=item["variant"],
                nodes=item.get("nodes", item.get("edges", "")),
                links=item.get("links", item.get("edges", "")),
                graph=Path(item["graph_json"]).relative_to(graphify_root),
                report=Path(item["report"]).relative_to(graphify_root),
            )
        )
    readme = [
        "# Graphify Three KG Variants",
        "",
        "This directory contains three Graphify-compatible KG variants.",
        "",
        "| Variant | Nodes | Links/Edges | Graph JSON | Report |",
        "|---|---:|---:|---|---|",
        *rows,
        "",
        "## Variant Meaning",
        "",
        "- `spec-only-graphify`: spec documents only, built deterministically from exported spec files.",
        "- `code-only-graphify`: current code/rationale Graphify graph snapshot.",
        "- `spec-code-graphify`: merged spec + code graph with inferred late-binding edges.",
        "",
        "## Spec-Code Binding Edges",
        "",
        "- `spec_component_matches_code`: spec component node matched to code node by component/path/label tokens.",
        "- `spec_path_matches_code_path`: spec document path token matched to RTL/code source path token.",
        "",
        "Large HTML visualization is skipped for these graphs because they exceed Graphify's HTML node limit.",
        "Use `graph.json`, `GRAPH_REPORT.md`, or GraphML-capable tools for inspection.",
        "",
    ]
    (graphify_root / "GRAPHIFY_THREE_VARIANTS.md").write_text("\n".join(readme), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graphify-root", type=Path, default=DEFAULT_GRAPHIFY_ROOT)
    parser.add_argument("--spec-graph", type=Path, default=DEFAULT_SPEC_GRAPH)
    parser.add_argument("--code-graph", type=Path, default=DEFAULT_CODE_GRAPH)
    parser.add_argument("--max-per-component", type=int, default=40)
    args = parser.parse_args()

    graphify_root = args.graphify_root.resolve()
    spec_graph = args.spec_graph.resolve()
    code_graph = args.code_graph.resolve()
    if not spec_graph.exists():
        raise FileNotFoundError(spec_graph)
    if not code_graph.exists():
        raise FileNotFoundError(code_graph)

    spec_manifest = read_json(spec_graph.parent / "spec_only_graphify_manifest.json")
    spec_manifest["variant"] = "spec-only"
    code_manifest = prepare_code_only(code_graph, graphify_root)
    spec_code_manifest = build_spec_code(spec_graph, code_graph, graphify_root, args.max_per_component)
    manifests = [spec_manifest, code_manifest, spec_code_manifest]
    write_top_manifest(graphify_root, manifests)
    print(json.dumps({"status": "ok", "variants": manifests}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
