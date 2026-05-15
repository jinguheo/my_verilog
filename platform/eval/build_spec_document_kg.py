#!/usr/bin/env python3
"""Build a document-only knowledge graph from extracted spec anchors.

The graph is intentionally separate from the code KG. It captures stable
document entities and binding keys that can later be joined to code by the
late-binding layer.
"""

from __future__ import annotations

import argparse
import html
import json
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ANCHORS = ROOT / "out" / "spec_code_late_binding_eval" / "spec_doc_anchors.json"
DEFAULT_OUT = ROOT / "out" / "spec_doc_kg"


@dataclass
class Node:
    id: str
    label: str
    type: str
    properties: dict[str, Any] = field(default_factory=dict)


@dataclass
class Edge:
    source: str
    target: str
    type: str
    weight: float = 1.0
    properties: dict[str, Any] = field(default_factory=dict)


def slug(value: str) -> str:
    clean = value.replace("\\", "/").strip().lower()
    clean = re.sub(r"[^a-z0-9_./#:-]+", "_", clean)
    return re.sub(r"_+", "_", clean).strip("_")


def add_node(nodes: dict[str, Node], node: Node) -> None:
    if node.id not in nodes:
        nodes[node.id] = node
        return
    nodes[node.id].properties.update(node.properties)


def add_edge(edges: dict[tuple[str, str, str], Edge], edge: Edge) -> None:
    key = (edge.source, edge.target, edge.type)
    if key in edges:
        edges[key].weight += edge.weight
        return
    edges[key] = edge


def build_graph(anchors: list[dict[str, Any]]) -> tuple[list[Node], list[Edge], dict[str, Any]]:
    nodes: dict[str, Node] = {}
    edges: dict[tuple[str, str, str], Edge] = {}

    project_docs: Counter[str] = Counter()
    ip_docs: Counter[str] = Counter()
    doc_kind_counts: Counter[str] = Counter()

    for anchor in anchors:
        doc_id = anchor["doc_id"].replace("\\", "/")
        project = anchor.get("project") or "unknown"
        ip_block = anchor.get("ip_block") or "unknown"
        doc_kind = anchor.get("doc_kind") or "unknown"

        doc_node = f"doc:{slug(doc_id)}"
        project_node = f"project:{slug(project)}"
        ip_node = f"ip:{slug(project)}:{slug(ip_block)}"

        project_docs[project] += 1
        ip_docs[f"{project}/{ip_block}"] += 1
        doc_kind_counts[doc_kind] += 1

        add_node(
            nodes,
            Node(
                id=doc_node,
                label=doc_id,
                type="document",
                properties={
                    "path": anchor.get("path"),
                    "project": project,
                    "doc_kind": doc_kind,
                    "ip_block": ip_block,
                    "token_count": anchor.get("token_count", 0),
                },
            ),
        )
        add_node(nodes, Node(project_node, project, "project"))
        add_node(nodes, Node(ip_node, ip_block, "ip_block", {"project": project}))

        add_edge(edges, Edge(doc_node, project_node, "IN_PROJECT"))
        add_edge(edges, Edge(doc_node, ip_node, "ABOUT_IP"))
        add_edge(edges, Edge(ip_node, project_node, "PART_OF_PROJECT"))

        for section in anchor.get("spec_sections", []):
            section_node = f"section:{slug(project)}:{slug(doc_id)}:{slug(section)}"
            add_node(
                nodes,
                Node(
                    section_node,
                    section,
                    "spec_section",
                    {"document": doc_id, "project": project, "ip_block": ip_block},
                ),
            )
            add_edge(edges, Edge(doc_node, section_node, "HAS_SECTION"))

        for module_name in anchor.get("module_mentions", []):
            module_node = f"module:{slug(module_name)}"
            add_node(nodes, Node(module_node, module_name, "module_mention"))
            add_edge(edges, Edge(doc_node, module_node, "MENTIONS_MODULE"))
            add_edge(edges, Edge(module_node, ip_node, "MENTIONED_IN_IP_DOC"))

        for ip_mention in anchor.get("ip_mentions", []):
            mention_node = f"ip_mention:{slug(ip_mention)}"
            add_node(nodes, Node(mention_node, ip_mention, "ip_mention"))
            add_edge(edges, Edge(doc_node, mention_node, "MENTIONS_IP_NAME"))

        for label in anchor.get("label_mentions", []):
            label_node = f"label:{slug(label)}"
            add_node(nodes, Node(label_node, label, "approved_label"))
            add_edge(edges, Edge(doc_node, label_node, "MENTIONS_LABEL"))

    degree = Counter()
    for edge in edges.values():
        degree[edge.source] += 1
        degree[edge.target] += 1
    for node in nodes.values():
        node.properties["degree"] = degree[node.id]

    summary = {
        "documents": sum(1 for node in nodes.values() if node.type == "document"),
        "nodes": len(nodes),
        "edges": len(edges),
        "projects": dict(sorted(project_docs.items())),
        "top_ip_blocks": ip_docs.most_common(25),
        "doc_kinds": dict(sorted(doc_kind_counts.items())),
        "node_types": dict(sorted(Counter(node.type for node in nodes.values()).items())),
        "edge_types": dict(sorted(Counter(edge.type for edge in edges.values()).items())),
    }
    return list(nodes.values()), list(edges.values()), summary


def write_json(path: Path, nodes: list[Node], edges: list[Edge], summary: dict[str, Any]) -> None:
    payload = {
        "schema": "spec-document-kg/v1",
        "summary": summary,
        "nodes": [node.__dict__ for node in nodes],
        "edges": [edge.__dict__ for edge in edges],
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def ttl_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def iri(value: str) -> str:
    return "kg:" + re.sub(r"[^A-Za-z0-9_:-]+", "_", value)


def write_ttl(path: Path, nodes: list[Node], edges: list[Edge]) -> None:
    lines = [
        "@prefix kg: <https://example.local/spec-doc-kg/> .",
        "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .",
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
        "",
    ]
    for node in nodes:
        lines.append(f'{iri(node.id)} rdf:type kg:{node.type} ; rdfs:label "{ttl_escape(node.label)}" .')
    lines.append("")
    for edge in edges:
        lines.append(f"{iri(edge.source)} kg:{edge.type} {iri(edge.target)} .")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_summary(path: Path, summary: dict[str, Any]) -> None:
    top_ip = "\n".join(f"- {name}: {count}" for name, count in summary["top_ip_blocks"][:15])
    node_types = "\n".join(f"- {name}: {count}" for name, count in summary["node_types"].items())
    edge_types = "\n".join(f"- {name}: {count}" for name, count in summary["edge_types"].items())
    text = f"""# Spec Document KG Summary

## Scope

This graph is built from extracted spec document anchors only. It is separate
from the code KG and is intended to connect to code through late-binding keys:
`ip_block`, `module_name`, `spec_section`, `doc_anchor`, and `approved_label`.

## Counts

- Documents: {summary["documents"]}
- Nodes: {summary["nodes"]}
- Edges: {summary["edges"]}

## Node Types

{node_types}

## Edge Types

{edge_types}

## Top IP Blocks

{top_ip}

## Outputs

- `spec_doc_kg.json`: full graph for programmatic use
- `spec_doc_kg.ttl`: RDF/Turtle export for OpenTology/SPARQL-style workflows
- `spec_doc_kg.html`: local interactive overview
"""
    path.write_text(text, encoding="utf-8")


def layout(nodes: list[Node], edges: list[Edge]) -> dict[str, dict[str, float]]:
    by_project: dict[str, list[Node]] = defaultdict(list)
    node_by_id = {node.id: node for node in nodes}
    doc_project: dict[str, str] = {}
    for edge in edges:
        if edge.type == "IN_PROJECT":
            project = node_by_id[edge.target].label
            doc_project[edge.source] = project
    for node in nodes:
        project = node.properties.get("project") or doc_project.get(node.id) or node.label
        if node.type == "project":
            project = node.label
        by_project[project].append(node)

    positions: dict[str, dict[str, float]] = {}
    projects = sorted(by_project)
    center_x, center_y = 900, 620
    project_radius = 380
    for p_index, project in enumerate(projects):
        angle = (2 * math.pi * p_index / max(1, len(projects))) - math.pi / 2
        px = center_x + project_radius * math.cos(angle)
        py = center_y + project_radius * math.sin(angle)
        project_nodes = by_project[project]
        for node in project_nodes:
            if node.type == "project":
                positions[node.id] = {"x": px, "y": py}
                break
        typed = defaultdict(list)
        for node in project_nodes:
            typed[node.type].append(node)
        rings = [
            ("ip_block", 80),
            ("document", 180),
            ("spec_section", 270),
            ("module_mention", 340),
            ("approved_label", 410),
            ("ip_mention", 470),
        ]
        for type_name, radius in rings:
            group = sorted(typed.get(type_name, []), key=lambda item: item.label)
            for index, node in enumerate(group):
                a = angle + (2 * math.pi * index / max(1, len(group)))
                positions[node.id] = {"x": px + radius * math.cos(a), "y": py + radius * math.sin(a)}
    return positions


def write_html(path: Path, nodes: list[Node], edges: list[Edge], summary: dict[str, Any]) -> None:
    positions = layout(nodes, edges)
    max_degree = max((node.properties.get("degree", 1) for node in nodes), default=1)
    data = {
        "summary": summary,
        "nodes": [
            {
                "id": node.id,
                "label": node.label,
                "type": node.type,
                "degree": node.properties.get("degree", 0),
                "x": positions.get(node.id, {}).get("x", 900),
                "y": positions.get(node.id, {}).get("y", 620),
            }
            for node in nodes
        ],
        "edges": [edge.__dict__ for edge in edges],
        "maxDegree": max_degree,
    }
    payload = json.dumps(data, ensure_ascii=False)
    html_text = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Spec Document Knowledge Graph</title>
<style>
  :root {{
    --bg: #f7f7f4;
    --ink: #1f2933;
    --muted: #697586;
    --line: rgba(31,41,51,.14);
    --panel: #ffffff;
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; font-family: Arial, Helvetica, sans-serif; background: var(--bg); color: var(--ink); }}
  header {{ padding: 18px 24px 12px; border-bottom: 1px solid var(--line); background: var(--panel); }}
  h1 {{ margin: 0 0 8px; font-size: 22px; letter-spacing: 0; }}
  .meta {{ display: flex; flex-wrap: wrap; gap: 10px; color: var(--muted); font-size: 13px; }}
  .shell {{ display: grid; grid-template-columns: 300px 1fr; min-height: calc(100vh - 82px); }}
  aside {{ padding: 16px; border-right: 1px solid var(--line); background: var(--panel); overflow: auto; }}
  main {{ position: relative; overflow: hidden; }}
  canvas {{ width: 100%; height: 100%; display: block; background: #fbfaf7; }}
  label {{ display: flex; align-items: center; gap: 8px; margin: 8px 0; font-size: 13px; }}
  input[type="text"] {{ width: 100%; padding: 8px 10px; border: 1px solid var(--line); border-radius: 6px; }}
  .section {{ margin: 0 0 18px; }}
  .section h2 {{ margin: 0 0 8px; font-size: 13px; text-transform: uppercase; color: var(--muted); }}
  .stat {{ display: grid; grid-template-columns: 1fr auto; gap: 8px; padding: 5px 0; font-size: 13px; }}
  .legend {{ display: grid; gap: 5px; font-size: 13px; }}
  .swatch {{ width: 11px; height: 11px; border-radius: 50%; display: inline-block; margin-right: 7px; }}
  #tip {{ position: absolute; pointer-events: none; padding: 8px 10px; border: 1px solid var(--line); background: #fff; border-radius: 6px; font-size: 12px; max-width: 360px; box-shadow: 0 6px 20px rgba(0,0,0,.12); display: none; }}
</style>
</head>
<body>
<header>
  <h1>Spec Document Knowledge Graph</h1>
  <div class="meta">
    <span>Documents: {summary["documents"]}</span>
    <span>Nodes: {summary["nodes"]}</span>
    <span>Edges: {summary["edges"]}</span>
    <span>Source: spec_doc_anchors.json</span>
  </div>
</header>
<div class="shell">
  <aside>
    <div class="section">
      <h2>Search</h2>
      <input id="search" type="text" placeholder="Filter by node label">
    </div>
    <div class="section">
      <h2>Node Types</h2>
      <div id="filters"></div>
    </div>
    <div class="section">
      <h2>Counts</h2>
      <div id="counts"></div>
    </div>
    <div class="section">
      <h2>Legend</h2>
      <div class="legend" id="legend"></div>
    </div>
  </aside>
  <main>
    <canvas id="graph"></canvas>
    <div id="tip"></div>
  </main>
</div>
<script>
const graph = {payload};
const colors = {{
  project: "#1f77b4",
  ip_block: "#2ca02c",
  document: "#222222",
  spec_section: "#9467bd",
  module_mention: "#d62728",
  approved_label: "#ff7f0e",
  ip_mention: "#17becf"
}};
const enabled = new Set(Object.keys(colors));
const canvas = document.getElementById("graph");
const ctx = canvas.getContext("2d");
const tip = document.getElementById("tip");
let scale = 1;
let offsetX = 0;
let offsetY = 0;
let search = "";

function resize() {{
  const rect = canvas.getBoundingClientRect();
  canvas.width = Math.floor(rect.width * devicePixelRatio);
  canvas.height = Math.floor(rect.height * devicePixelRatio);
  ctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
  draw();
}}

function visibleNode(node) {{
  return enabled.has(node.type) && (!search || node.label.toLowerCase().includes(search));
}}

function sx(x) {{ return x * scale + offsetX; }}
function sy(y) {{ return y * scale + offsetY; }}

function draw() {{
  const rect = canvas.getBoundingClientRect();
  ctx.clearRect(0, 0, rect.width, rect.height);
  const nodes = new Map(graph.nodes.filter(visibleNode).map(node => [node.id, node]));
  ctx.lineWidth = 0.6;
  ctx.strokeStyle = "rgba(70,70,70,.11)";
  for (const edge of graph.edges) {{
    const a = nodes.get(edge.source);
    const b = nodes.get(edge.target);
    if (!a || !b) continue;
    ctx.beginPath();
    ctx.moveTo(sx(a.x), sy(a.y));
    ctx.lineTo(sx(b.x), sy(b.y));
    ctx.stroke();
  }}
  for (const node of nodes.values()) {{
    const radius = 3 + Math.sqrt(node.degree / graph.maxDegree) * 14;
    ctx.beginPath();
    ctx.fillStyle = colors[node.type] || "#555";
    ctx.arc(sx(node.x), sy(node.y), radius, 0, Math.PI * 2);
    ctx.fill();
    if (node.type === "project" || node.degree > 18 || search) {{
      ctx.font = "12px Arial";
      ctx.fillStyle = "#17202a";
      ctx.fillText(node.label.slice(0, 48), sx(node.x) + radius + 4, sy(node.y) + 4);
    }}
  }}
}}

function initControls() {{
  const filters = document.getElementById("filters");
  const counts = document.getElementById("counts");
  const legend = document.getElementById("legend");
  for (const [type, count] of Object.entries(graph.summary.node_types)) {{
    const label = document.createElement("label");
    label.innerHTML = `<input type="checkbox" checked data-type="${{type}}"> ${{type}} (${{count}})`;
    filters.appendChild(label);
    counts.insertAdjacentHTML("beforeend", `<div class="stat"><span>${{type}}</span><strong>${{count}}</strong></div>`);
    legend.insertAdjacentHTML("beforeend", `<div><span class="swatch" style="background:${{colors[type] || "#555"}}"></span>${{type}}</div>`);
  }}
  filters.addEventListener("change", event => {{
    const type = event.target.dataset.type;
    if (!type) return;
    if (event.target.checked) enabled.add(type); else enabled.delete(type);
    draw();
  }});
  document.getElementById("search").addEventListener("input", event => {{
    search = event.target.value.trim().toLowerCase();
    draw();
  }});
}}

canvas.addEventListener("mousemove", event => {{
  const rect = canvas.getBoundingClientRect();
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;
  let hit = null;
  for (const node of graph.nodes) {{
    if (!visibleNode(node)) continue;
    const radius = 5 + Math.sqrt(node.degree / graph.maxDegree) * 14;
    const dx = sx(node.x) - x;
    const dy = sy(node.y) - y;
    if (Math.sqrt(dx * dx + dy * dy) <= radius) {{ hit = node; break; }}
  }}
  if (!hit) {{ tip.style.display = "none"; return; }}
  tip.style.display = "block";
  tip.style.left = `${{event.clientX - rect.left + 12}}px`;
  tip.style.top = `${{event.clientY - rect.top + 12}}px`;
  tip.innerHTML = `<strong>${{hit.type}}</strong><br>${{hit.label.replace(/[&<>]/g, c => ({{"&":"&amp;","<":"&lt;",">":"&gt;"}}[c]))}}<br>degree: ${{hit.degree}}`;
}});

canvas.addEventListener("wheel", event => {{
  event.preventDefault();
  const factor = event.deltaY < 0 ? 1.08 : 0.92;
  scale = Math.max(0.15, Math.min(5, scale * factor));
  draw();
}}, {{ passive: false }});

let drag = null;
canvas.addEventListener("mousedown", event => {{ drag = {{ x: event.clientX, y: event.clientY, ox: offsetX, oy: offsetY }}; }});
window.addEventListener("mouseup", () => {{ drag = null; }});
window.addEventListener("mousemove", event => {{
  if (!drag) return;
  offsetX = drag.ox + event.clientX - drag.x;
  offsetY = drag.oy + event.clientY - drag.y;
  draw();
}});

initControls();
resize();
window.addEventListener("resize", resize);
</script>
</body>
</html>
"""
    path.write_text(html_text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a spec-document knowledge graph.")
    parser.add_argument("--anchors", type=Path, default=DEFAULT_ANCHORS)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    anchors = json.loads(args.anchors.read_text(encoding="utf-8"))
    args.out.mkdir(parents=True, exist_ok=True)

    nodes, edges, summary = build_graph(anchors)
    write_json(args.out / "spec_doc_kg.json", nodes, edges, summary)
    write_ttl(args.out / "spec_doc_kg.ttl", nodes, edges)
    write_summary(args.out / "SPEC_DOC_KG_SUMMARY.md", summary)
    write_html(args.out / "spec_doc_kg.html", nodes, edges, summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
