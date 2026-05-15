#!/usr/bin/env python3
"""Render the current custom RTL KG as an interactive local HTML graph."""

from __future__ import annotations

import argparse
import html
import json
import math
import re
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_KG = ROOT / "out" / "kg_full" / "kg_full_nodes_edges.json"
DEFAULT_SUMMARY = ROOT / "out" / "kg_full" / "kg_full_summary.json"
DEFAULT_OUT = ROOT / "out" / "kg_full" / "kg_full_graph.html"


def safe_text(value: Any) -> str:
    return html.escape(str(value or ""), quote=True)


def infer_ip_from_path(path: str) -> str:
    normalized = path.replace("\\", "/")
    match = re.search(r"/hw/ip/([^/]+)/", normalized)
    if match:
        return match.group(1)
    match = re.search(r"/vendor/([^/]+)/", normalized)
    if match:
        return f"vendor/{match.group(1)}"
    match = re.search(r"/dv/([^/]+)/", normalized)
    if match:
        return f"dv/{match.group(1)}"
    return "unknown"


def compact_graph(payload: dict[str, Any]) -> dict[str, Any]:
    nodes = payload["nodes"]
    edges = payload["edges"]
    node_by_id = {node["id"]: node for node in nodes}

    degree = Counter()
    in_degree = Counter()
    out_degree = Counter()
    edge_types = Counter()
    for edge in edges:
        degree[edge["source"]] += 1
        degree[edge["target"]] += 1
        out_degree[edge["source"]] += 1
        in_degree[edge["target"]] += 1
        edge_types[edge["type"]] += 1

    module_to_ip: dict[str, str] = {}
    for node in nodes:
        if node.get("kind") == "module":
            module_to_ip[node["id"]] = infer_ip_from_path(node.get("path", ""))

    rendered_nodes = []
    for node in nodes:
        kind = node.get("kind", "unknown")
        rendered_nodes.append(
            {
                "id": node["id"],
                "kind": kind,
                "name": node.get("name", node["id"]),
                "project": node.get("project", ""),
                "path": node.get("path", ""),
                "module": node.get("module", ""),
                "direction": node.get("direction", ""),
                "summary": node.get("summary", ""),
                "ip": module_to_ip.get(node["id"], node.get("name", "") if kind == "ip_block" else ""),
                "degree": degree[node["id"]],
                "inDegree": in_degree[node["id"]],
                "outDegree": out_degree[node["id"]],
                "portCount": node.get("port_count", 0),
                "instanceCount": node.get("instance_count", 0),
            }
        )

    rendered_edges = [
        {
            "source": edge["source"],
            "target": edge["target"],
            "type": edge["type"],
            "instanceName": edge.get("instance_name", ""),
        }
        for edge in edges
        if edge["source"] in node_by_id and edge["target"] in node_by_id
    ]

    node_types = Counter(node["kind"] for node in rendered_nodes)
    top_modules = sorted(
        [node for node in rendered_nodes if node["kind"] == "module"],
        key=lambda item: (item["degree"], item["instanceCount"], item["portCount"]),
        reverse=True,
    )[:60]

    adjacency = defaultdict(list)
    for edge in rendered_edges:
        adjacency[edge["source"]].append(edge["target"])
        adjacency[edge["target"]].append(edge["source"])

    focus_ids = {node["id"] for node in top_modules}
    for module in list(focus_ids):
        for neighbor in adjacency[module][:80]:
            focus_ids.add(neighbor)
            if node_by_id.get(neighbor, {}).get("kind") == "module":
                for second in adjacency[neighbor][:35]:
                    focus_ids.add(second)

    return {
        "nodes": rendered_nodes,
        "edges": rendered_edges,
        "summary": {
            "nodeTypes": dict(sorted(node_types.items())),
            "edgeTypes": dict(sorted(edge_types.items())),
            "totalNodes": len(rendered_nodes),
            "totalEdges": len(rendered_edges),
            "topModules": [
                {
                    "id": node["id"],
                    "name": node["name"],
                    "project": node["project"],
                    "ip": node["ip"],
                    "degree": node["degree"],
                    "instances": node["instanceCount"],
                    "ports": node["portCount"],
                }
                for node in top_modules[:25]
            ],
            "focusIds": sorted(focus_ids),
        },
    }


def write_html(path: Path, graph: dict[str, Any], kg_summary: dict[str, Any]) -> None:
    data = json.dumps(graph, ensure_ascii=False)
    summary_json = json.dumps(kg_summary, ensure_ascii=False)
    html_text = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Current RTL KG Graph</title>
<style>
  :root {{
    --bg: #f5f5f2;
    --panel: #ffffff;
    --ink: #17202a;
    --muted: #64748b;
    --line: rgba(23,32,42,.14);
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; font-family: Arial, Helvetica, sans-serif; background: var(--bg); color: var(--ink); }}
  header {{ padding: 16px 22px 12px; background: var(--panel); border-bottom: 1px solid var(--line); }}
  h1 {{ margin: 0 0 8px; font-size: 22px; letter-spacing: 0; }}
  .meta {{ display: flex; flex-wrap: wrap; gap: 12px; color: var(--muted); font-size: 13px; }}
  .shell {{ display: grid; grid-template-columns: 330px 1fr; height: calc(100vh - 76px); min-height: 680px; }}
  aside {{ overflow: auto; background: var(--panel); border-right: 1px solid var(--line); padding: 14px; }}
  main {{ position: relative; overflow: hidden; }}
  canvas {{ width: 100%; height: 100%; display: block; background: #fbfaf7; }}
  h2 {{ margin: 16px 0 8px; font-size: 12px; text-transform: uppercase; color: var(--muted); }}
  h2:first-child {{ margin-top: 0; }}
  input[type="text"], select {{ width: 100%; padding: 8px 9px; border: 1px solid var(--line); border-radius: 6px; background: white; }}
  label {{ display: flex; align-items: center; gap: 7px; margin: 7px 0; font-size: 13px; }}
  button {{ border: 1px solid var(--line); border-radius: 6px; background: #fff; padding: 7px 9px; cursor: pointer; }}
  button:hover {{ background: #f0f3f6; }}
  .row {{ display: grid; grid-template-columns: 1fr auto; gap: 8px; padding: 4px 0; font-size: 13px; }}
  .hint {{ font-size: 12px; color: var(--muted); line-height: 1.45; }}
  .top-item {{ padding: 7px 0; border-bottom: 1px solid var(--line); font-size: 12px; cursor: pointer; }}
  .top-item strong {{ display: block; font-size: 13px; color: var(--ink); }}
  .swatch {{ width: 11px; height: 11px; border-radius: 50%; display: inline-block; }}
  #tip {{ position: absolute; pointer-events: none; display: none; max-width: 430px; padding: 9px 10px; background: #fff; border: 1px solid var(--line); border-radius: 6px; box-shadow: 0 8px 22px rgba(0,0,0,.14); font-size: 12px; line-height: 1.4; }}
  #detail {{ position: absolute; right: 14px; top: 14px; width: min(460px, calc(100% - 28px)); max-height: calc(100% - 28px); overflow: auto; background: rgba(255,255,255,.96); border: 1px solid var(--line); border-radius: 8px; padding: 12px; display: none; box-shadow: 0 8px 26px rgba(0,0,0,.16); }}
  #detail h3 {{ margin: 0 0 8px; font-size: 15px; }}
  #detail pre {{ white-space: pre-wrap; word-break: break-word; margin: 8px 0 0; font-size: 11px; color: #334155; }}
</style>
</head>
<body>
<header>
  <h1>Current RTL Knowledge Graph</h1>
  <div class="meta">
    <span>Modules: {safe_text(kg_summary.get("modules"))}</span>
    <span>Ports: {safe_text(kg_summary.get("ports"))}</span>
    <span>IP blocks: {safe_text(kg_summary.get("ip_blocks"))}</span>
    <span>Labels: {safe_text(kg_summary.get("labels"))}</span>
    <span>Edges: {safe_text(kg_summary.get("total_edges"))}</span>
  </div>
</header>
<div class="shell">
  <aside>
    <h2>View</h2>
    <select id="viewMode">
      <option value="focus" selected>Architecture focus</option>
      <option value="modules">Modules and hierarchy</option>
      <option value="all">All nodes</option>
    </select>
    <p class="hint">Architecture focus keeps the graph responsive by showing high-degree modules and their neighbors. Use search to expand around a specific module.</p>

    <h2>Search</h2>
    <input id="search" type="text" placeholder="module, port, label, IP">

    <h2>Node Types</h2>
    <div id="nodeFilters"></div>

    <h2>Edge Types</h2>
    <div id="edgeFilters"></div>

    <h2>Counts</h2>
    <div id="counts"></div>

    <h2>Top Connected Modules</h2>
    <div id="topModules"></div>
  </aside>
  <main>
    <canvas id="graph"></canvas>
    <div id="tip"></div>
    <div id="detail"></div>
  </main>
</div>
<script>
const graph = {data};
const sourceSummary = {summary_json};
const colors = {{
  module: "#2563eb",
  port: "#64748b",
  label: "#f97316",
  ip_block: "#16a34a"
}};
const edgeColors = {{
  HAS_PORT: "rgba(100,116,139,.23)",
  HAS_LABEL: "rgba(249,115,22,.34)",
  INSTANTIATES: "rgba(37,99,235,.48)"
}};
const nodeById = new Map(graph.nodes.map(n => [n.id, n]));
let enabledKinds = new Set(["module", "label", "ip_block"]);
let enabledEdges = new Set(Object.keys(graph.summary.edgeTypes));
let search = "";
let viewMode = "focus";
let selectedId = null;
let transform = {{ x: 0, y: 0, scale: 1 }};
let positioned = [];
let positionedMap = new Map();

const canvas = document.getElementById("graph");
const ctx = canvas.getContext("2d");
const tip = document.getElementById("tip");
const detail = document.getElementById("detail");

function nodeVisibleBase(node) {{
  if (!enabledKinds.has(node.kind)) return false;
  if (viewMode === "focus" && !graph.summary.focusIds.includes(node.id) && !matchesSearchNeighborhood(node)) return false;
  if (viewMode === "modules" && !["module", "label", "ip_block"].includes(node.kind)) return false;
  return true;
}}

function matchesSearch(node) {{
  if (!search) return false;
  const hay = `${{node.name}} ${{node.project}} ${{node.ip}} ${{node.module}} ${{node.direction}} ${{node.summary}} ${{node.path}}`.toLowerCase();
  return hay.includes(search);
}}

function matchesSearchNeighborhood(node) {{
  if (!search) return false;
  if (matchesSearch(node)) return true;
  for (const edge of graph.edges) {{
    if (edge.source === node.id && matchesSearch(nodeById.get(edge.target) || {{}})) return true;
    if (edge.target === node.id && matchesSearch(nodeById.get(edge.source) || {{}})) return true;
  }}
  return false;
}}

function visibleNodes() {{
  return graph.nodes.filter(node => nodeVisibleBase(node) && (!search || matchesSearchNeighborhood(node)));
}}

function visibleEdges(nodes) {{
  const ids = new Set(nodes.map(n => n.id));
  return graph.edges.filter(edge => enabledEdges.has(edge.type) && ids.has(edge.source) && ids.has(edge.target));
}}

function computeLayout() {{
  const nodes = visibleNodes();
  const edges = visibleEdges(nodes);
  const rect = canvas.getBoundingClientRect();
  const width = Math.max(900, rect.width);
  const height = Math.max(680, rect.height);
  const byKind = Object.groupBy ? Object.groupBy(nodes, n => n.kind) : groupByKind(nodes);
  const projectAngles = new Map();
  const projects = [...new Set(nodes.map(n => n.project || "shared"))].sort();
  projects.forEach((project, index) => projectAngles.set(project, Math.PI * 2 * index / Math.max(1, projects.length) - Math.PI / 2));

  const positions = new Map();
  for (const node of nodes) {{
    const project = node.project || "shared";
    const angle = projectAngles.get(project) || 0;
    const cx = width / 2 + Math.cos(angle) * width * .22;
    const cy = height / 2 + Math.sin(angle) * height * .20;
    let radius = 90;
    if (node.kind === "module") radius = 220 + Math.min(180, node.degree * 2.5);
    if (node.kind === "port") radius = 340;
    if (node.kind === "label") radius = 95;
    if (node.kind === "ip_block") radius = 30;
    const group = byKind[node.kind] || [];
    const i = group.indexOf(node);
    const localAngle = angle + Math.PI * 2 * i / Math.max(1, group.length);
    positions.set(node.id, {{ x: cx + Math.cos(localAngle) * radius, y: cy + Math.sin(localAngle) * radius }});
  }}

  const largeGraph = nodes.length > 2400;
  const iterations = largeGraph ? 0 : 120;
  for (let iter = 0; iter < iterations; iter++) {{
    const forces = new Map(nodes.map(n => [n.id, {{ x: 0, y: 0 }}]));
    for (let i = 0; i < nodes.length; i++) {{
      for (let j = i + 1; j < nodes.length; j++) {{
        const a = positions.get(nodes[i].id);
        const b = positions.get(nodes[j].id);
        let dx = a.x - b.x;
        let dy = a.y - b.y;
        const dist2 = Math.max(80, dx * dx + dy * dy);
        const force = Math.min(4.5, 1800 / dist2);
        const dist = Math.sqrt(dist2);
        dx /= dist; dy /= dist;
        forces.get(nodes[i].id).x += dx * force;
        forces.get(nodes[i].id).y += dy * force;
        forces.get(nodes[j].id).x -= dx * force;
        forces.get(nodes[j].id).y -= dy * force;
      }}
    }}
    for (const edge of edges) {{
      const a = positions.get(edge.source);
      const b = positions.get(edge.target);
      if (!a || !b) continue;
      const dx = b.x - a.x;
      const dy = b.y - a.y;
      const dist = Math.max(1, Math.sqrt(dx * dx + dy * dy));
      const target = edge.type === "HAS_PORT" ? 85 : edge.type === "HAS_LABEL" ? 140 : 190;
      const force = (dist - target) * 0.006;
      forces.get(edge.source).x += dx / dist * force;
      forces.get(edge.source).y += dy / dist * force;
      forces.get(edge.target).x -= dx / dist * force;
      forces.get(edge.target).y -= dy / dist * force;
    }}
    for (const node of nodes) {{
      const p = positions.get(node.id);
      const f = forces.get(node.id);
      p.x = Math.max(30, Math.min(width - 30, p.x + f.x));
      p.y = Math.max(30, Math.min(height - 30, p.y + f.y));
    }}
  }}

  positioned = nodes.map(node => ({{ ...node, x: positions.get(node.id).x, y: positions.get(node.id).y }}));
  positionedMap = new Map(positioned.map(n => [n.id, n]));
}}

function groupByKind(nodes) {{
  const grouped = {{}};
  for (const node of nodes) {{
    grouped[node.kind] ||= [];
    grouped[node.kind].push(node);
  }}
  return grouped;
}}

function sx(x) {{ return x * transform.scale + transform.x; }}
function sy(y) {{ return y * transform.scale + transform.y; }}

function radius(node) {{
  const base = node.kind === "module" ? 5 : node.kind === "port" ? 2.5 : 6;
  return base + Math.min(12, Math.sqrt(node.degree || 1) * 1.3);
}}

function draw() {{
  const rect = canvas.getBoundingClientRect();
  ctx.clearRect(0, 0, rect.width, rect.height);
  const edges = visibleEdges(positioned);
  ctx.lineCap = "round";
  for (const edge of edges) {{
    const a = positionedMap.get(edge.source);
    const b = positionedMap.get(edge.target);
    if (!a || !b) continue;
    ctx.beginPath();
    ctx.strokeStyle = edgeColors[edge.type] || "rgba(0,0,0,.18)";
    ctx.lineWidth = edge.type === "INSTANTIATES" ? 1.4 : .7;
    ctx.moveTo(sx(a.x), sy(a.y));
    ctx.lineTo(sx(b.x), sy(b.y));
    ctx.stroke();
  }}
  for (const node of positioned) {{
    const r = radius(node);
    ctx.beginPath();
    ctx.fillStyle = selectedId === node.id ? "#111827" : colors[node.kind] || "#475569";
    ctx.arc(sx(node.x), sy(node.y), r, 0, Math.PI * 2);
    ctx.fill();
    if (selectedId === node.id || search || node.kind === "ip_block" || (node.kind === "module" && node.degree > 30)) {{
      ctx.font = "12px Arial";
      ctx.fillStyle = "#111827";
      ctx.fillText(node.name.slice(0, 52), sx(node.x) + r + 4, sy(node.y) + 4);
    }}
  }}
}}

function relayout() {{
  computeLayout();
  draw();
}}

function resize() {{
  const rect = canvas.getBoundingClientRect();
  canvas.width = Math.floor(rect.width * devicePixelRatio);
  canvas.height = Math.floor(rect.height * devicePixelRatio);
  ctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
  relayout();
}}

function initControls() {{
  const nodeFilters = document.getElementById("nodeFilters");
  for (const [kind, count] of Object.entries(graph.summary.nodeTypes)) {{
    const checked = enabledKinds.has(kind) ? "checked" : "";
    nodeFilters.insertAdjacentHTML("beforeend", `<label><input type="checkbox" data-kind="${{kind}}" ${{checked}}> <span class="swatch" style="background:${{colors[kind] || "#555"}}"></span> ${{kind}} (${{count}})</label>`);
  }}
  nodeFilters.addEventListener("change", event => {{
    const kind = event.target.dataset.kind;
    if (!kind) return;
    if (event.target.checked) enabledKinds.add(kind); else enabledKinds.delete(kind);
    relayout();
  }});

  const edgeFilters = document.getElementById("edgeFilters");
  for (const [type, count] of Object.entries(graph.summary.edgeTypes)) {{
    edgeFilters.insertAdjacentHTML("beforeend", `<label><input type="checkbox" data-edge="${{type}}" checked> ${{type}} (${{count}})</label>`);
  }}
  edgeFilters.addEventListener("change", event => {{
    const type = event.target.dataset.edge;
    if (!type) return;
    if (event.target.checked) enabledEdges.add(type); else enabledEdges.delete(type);
    draw();
  }});

  document.getElementById("viewMode").addEventListener("change", event => {{
    viewMode = event.target.value;
    if (viewMode === "all") enabledKinds.add("port");
    relayout();
  }});
  document.getElementById("search").addEventListener("input", event => {{
    search = event.target.value.trim().toLowerCase();
    relayout();
  }});

  const counts = document.getElementById("counts");
  counts.innerHTML = `
    <div class="row"><span>Total nodes</span><strong>${{graph.summary.totalNodes}}</strong></div>
    <div class="row"><span>Total edges</span><strong>${{graph.summary.totalEdges}}</strong></div>
    <div class="row"><span>Instance edges</span><strong>${{sourceSummary.instance_edges}}</strong></div>
  `;

  const top = document.getElementById("topModules");
  for (const item of graph.summary.topModules) {{
    const div = document.createElement("div");
    div.className = "top-item";
    div.innerHTML = `<strong>${{item.name}}</strong>${{item.project}} / ${{item.ip}} · degree ${{item.degree}} · inst ${{item.instances}} · ports ${{item.ports}}`;
    div.addEventListener("click", () => {{
      selectedId = item.id;
      search = item.name.toLowerCase();
      document.getElementById("search").value = item.name;
      relayout();
      showDetail(nodeById.get(item.id));
    }});
    top.appendChild(div);
  }}
}}

function hitTest(event) {{
  const rect = canvas.getBoundingClientRect();
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;
  for (let i = positioned.length - 1; i >= 0; i--) {{
    const node = positioned[i];
    const dx = sx(node.x) - x;
    const dy = sy(node.y) - y;
    if (Math.sqrt(dx * dx + dy * dy) <= radius(node) + 3) return node;
  }}
  return null;
}}

function showDetail(node) {{
  if (!node) {{ detail.style.display = "none"; return; }}
  const related = graph.edges
    .filter(edge => edge.source === node.id || edge.target === node.id)
    .slice(0, 80)
    .map(edge => {{
      const other = nodeById.get(edge.source === node.id ? edge.target : edge.source);
      return `${{edge.type}} -> ${{other ? other.name : "unknown"}}`;
    }});
  detail.style.display = "block";
  detail.innerHTML = `
    <h3>${{node.name}}</h3>
    <div class="hint">${{node.kind}} · ${{node.project || "shared"}} · degree ${{node.degree}}</div>
    <pre>${{JSON.stringify({{
      ip: node.ip,
      module: node.module,
      direction: node.direction,
      summary: node.summary,
      path: node.path,
      related: related
    }}, null, 2).replace(/[&<>]/g, c => ({{"&":"&amp;","<":"&lt;",">":"&gt;"}}[c]))}}</pre>
  `;
}}

canvas.addEventListener("mousemove", event => {{
  const node = hitTest(event);
  if (!node) {{ tip.style.display = "none"; return; }}
  const rect = canvas.getBoundingClientRect();
  tip.style.display = "block";
  tip.style.left = `${{event.clientX - rect.left + 12}}px`;
  tip.style.top = `${{event.clientY - rect.top + 12}}px`;
  tip.innerHTML = `<strong>${{node.kind}}</strong><br>${{node.name}}<br>degree: ${{node.degree}}`;
}});

canvas.addEventListener("click", event => {{
  const node = hitTest(event);
  selectedId = node ? node.id : null;
  showDetail(node);
  draw();
}});

canvas.addEventListener("wheel", event => {{
  event.preventDefault();
  const factor = event.deltaY < 0 ? 1.08 : 0.92;
  transform.scale = Math.max(0.18, Math.min(4, transform.scale * factor));
  draw();
}}, {{ passive: false }});

let drag = null;
canvas.addEventListener("mousedown", event => {{ drag = {{ x: event.clientX, y: event.clientY, tx: transform.x, ty: transform.y }}; }});
window.addEventListener("mouseup", () => {{ drag = null; }});
window.addEventListener("mousemove", event => {{
  if (!drag) return;
  transform.x = drag.tx + event.clientX - drag.x;
  transform.y = drag.ty + event.clientY - drag.y;
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
    parser = argparse.ArgumentParser(description="Render the current custom KG as HTML.")
    parser.add_argument("--kg", type=Path, default=DEFAULT_KG)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    payload = json.loads(args.kg.read_text(encoding="utf-8"))
    kg_summary = json.loads(args.summary.read_text(encoding="utf-8"))
    graph = compact_graph(payload)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    write_html(args.out, graph, kg_summary)
    printable = {key: value for key, value in graph["summary"].items() if key != "focusIds"}
    printable["focus_nodes"] = len(graph["summary"]["focusIds"])
    print(json.dumps({"out": str(args.out), **printable}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
