#!/usr/bin/env python3
"""Build a separate spec-code late-binding KG visualization."""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
ANCHORS = ROOT / "out" / "spec_code_late_binding_eval" / "spec_doc_anchors.json"
CODE_KG = ROOT / "out" / "kg_full" / "kg_full_nodes_edges.json"
CODE_SUMMARY = ROOT / "out" / "kg_full" / "kg_full_summary.json"
SPEC_ONLY_HTML = ROOT / "out" / "spec_doc_only_kg" / "spec_only_kg.html"
CODE_ONLY_HTML = ROOT / "out" / "kg_full" / "kg_full_graph.html"
OUT = ROOT / "out" / "kg_three_views"


@dataclass
class Node:
    id: str
    label: str
    type: str
    properties: dict[str, Any]


@dataclass
class Edge:
    source: str
    target: str
    type: str
    weight: int = 1


def slug(value: str) -> str:
    value = value.replace("\\", "/").lower()
    value = re.sub(r"[^a-z0-9_./#:-]+", "_", value)
    return re.sub(r"_+", "_", value).strip("_")


def infer_ip_from_path(path: str) -> str:
    normalized = path.replace("\\", "/").lower()
    for marker in ("/hw/ip/", "/ip_autogen/"):
        if marker in normalized:
            tail = normalized.split(marker, 1)[1]
            return tail.split("/", 1)[0]
    if "/rv_core_ibex/" in normalized:
        return "rv_core_ibex"
    if "/lowrisc_ibex/" in normalized or "/dbs/ibex/" in normalized:
        return "ibex"
    return ""


def add_node(nodes: dict[str, Node], node: Node) -> None:
    if node.id not in nodes:
        nodes[node.id] = node
    else:
        nodes[node.id].properties.update({k: v for k, v in node.properties.items() if v not in ("", None, [])})


def add_edge(edges: dict[tuple[str, str, str], Edge], edge: Edge) -> None:
    key = (edge.source, edge.target, edge.type)
    if key in edges:
        edges[key].weight += edge.weight
    else:
        edges[key] = edge


def load_code_modules(code_kg: Path) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    payload = json.loads(code_kg.read_text(encoding="utf-8"))
    label_by_module: dict[str, set[str]] = defaultdict(set)
    node_by_id = {node["id"]: node for node in payload["nodes"]}
    for edge in payload["edges"]:
        if edge.get("type") == "HAS_LABEL" and edge["target"].startswith("label:"):
            label_by_module[edge["source"]].add(edge["target"].split(":", 1)[1])

    modules = []
    by_name: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for node in payload["nodes"]:
        if node.get("kind") != "module":
            continue
        module = {
            "id": node["id"],
            "name": node.get("name", ""),
            "project": node.get("project", ""),
            "path": node.get("path", ""),
            "ip_block": infer_ip_from_path(node.get("path", "")),
            "port_count": node.get("port_count", 0),
            "instance_count": node.get("instance_count", 0),
            "labels": sorted(label_by_module.get(node["id"], [])),
        }
        modules.append(module)
        by_name[module["name"]].append(module)
    return modules, by_name


def build(anchors_path: Path, code_kg: Path) -> tuple[list[Node], list[Edge], dict[str, Any]]:
    anchors = json.loads(anchors_path.read_text(encoding="utf-8"))
    modules, modules_by_name = load_code_modules(code_kg)
    modules_by_ip: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    modules_by_label: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for module in modules:
        if module["ip_block"]:
            modules_by_ip[(module["project"], module["ip_block"])].append(module)
        for label in module["labels"]:
            modules_by_label[label].append(module)

    nodes: dict[str, Node] = {}
    edges: dict[tuple[str, str, str], Edge] = {}
    edge_counts = Counter()

    for module in modules:
        module_id = f"code_module:{slug(module['project'])}:{slug(module['name'])}:{slug(module['path'])}"
        add_node(
            nodes,
            Node(
                module_id,
                module["name"],
                "code_module",
                {
                    "project": module["project"],
                    "ip_block": module["ip_block"],
                    "path": module["path"],
                    "ports": module["port_count"],
                    "instances": module["instance_count"],
                    "labels": module["labels"],
                },
            ),
        )
        if module["ip_block"]:
            ip_id = f"ip:{slug(module['project'])}:{slug(module['ip_block'])}"
            add_node(nodes, Node(ip_id, module["ip_block"], "ip_block", {"project": module["project"]}))
            add_edge(edges, Edge(module_id, ip_id, "CODE_IN_IP"))

    for anchor in anchors:
        doc_id_raw = anchor["doc_id"].replace("\\", "/")
        project = anchor.get("project") or "unknown"
        ip_block = anchor.get("ip_block") or ""
        doc_id = f"spec_doc:{slug(doc_id_raw)}"
        project_id = f"project:{slug(project)}"
        add_node(
            nodes,
            Node(
                doc_id,
                doc_id_raw,
                "spec_document",
                {
                    "project": project,
                    "ip_block": ip_block,
                    "doc_kind": anchor.get("doc_kind", ""),
                    "token_count": anchor.get("token_count", 0),
                    "path": anchor.get("path", ""),
                },
            ),
        )
        add_node(nodes, Node(project_id, project, "project", {}))
        add_edge(edges, Edge(doc_id, project_id, "SPEC_IN_PROJECT"))
        if ip_block:
            ip_id = f"ip:{slug(project)}:{slug(ip_block)}"
            add_node(nodes, Node(ip_id, ip_block, "ip_block", {"project": project}))
            add_edge(edges, Edge(doc_id, ip_id, "SPEC_ABOUT_IP"))

        exact_linked = set()
        for module_name in anchor.get("module_mentions", []):
            for module in modules_by_name.get(module_name, []):
                if module["project"] != project:
                    continue
                module_id = f"code_module:{slug(module['project'])}:{slug(module['name'])}:{slug(module['path'])}"
                add_edge(edges, Edge(doc_id, module_id, "EXACT_MODULE_LINK", 5))
                exact_linked.add(module_id)
                edge_counts["exact"] += 1

        if ip_block and ip_block not in {"unknown", "unassigned"}:
            candidates = modules_by_ip.get((project, ip_block), [])
            candidates = sorted(candidates, key=lambda item: (item["instance_count"], item["port_count"]), reverse=True)
            for module in candidates[:80]:
                module_id = f"code_module:{slug(module['project'])}:{slug(module['name'])}:{slug(module['path'])}"
                if module_id in exact_linked:
                    continue
                add_edge(edges, Edge(doc_id, module_id, "IP_BLOCK_LINK", 2))
                edge_counts["ip"] += 1

        for label in anchor.get("label_mentions", []):
            label_id = f"label:{slug(label)}"
            add_node(nodes, Node(label_id, label, "approved_label", {}))
            add_edge(edges, Edge(doc_id, label_id, "SPEC_MENTIONS_LABEL"))
            for module in modules_by_label.get(label, [])[:80]:
                if module["project"] != project:
                    continue
                module_id = f"code_module:{slug(module['project'])}:{slug(module['name'])}:{slug(module['path'])}"
                add_edge(edges, Edge(label_id, module_id, "LABEL_TO_CODE_MODULE"))
                edge_counts["label"] += 1

    degree = Counter()
    for edge in edges.values():
        degree[edge.source] += edge.weight
        degree[edge.target] += edge.weight
    for node in nodes.values():
        node.properties["degree"] = degree[node.id]

    summary = {
        "spec_docs": len(anchors),
        "code_modules": len(modules),
        "nodes": len(nodes),
        "edges": len(edges),
        "node_types": dict(sorted(Counter(node.type for node in nodes.values()).items())),
        "edge_types": dict(sorted(Counter(edge.type for edge in edges.values()).items())),
        "late_binding_edges": dict(edge_counts),
        "meaning": "spec documents and code modules are separate nodes joined by late-binding edges",
    }
    return list(nodes.values()), list(edges.values()), summary


def write_json(out_dir: Path, nodes: list[Node], edges: list[Edge], summary: dict[str, Any]) -> None:
    payload = {
        "schema": "spec-code-late-binding-kg/v1",
        "summary": summary,
        "nodes": [asdict(node) for node in nodes],
        "edges": [asdict(edge) for edge in edges],
    }
    (out_dir / "spec_code_kg.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def write_html(out_dir: Path, nodes: list[Node], edges: list[Edge], summary: dict[str, Any]) -> None:
    payload = json.dumps({"summary": summary, "nodes": [asdict(n) for n in nodes], "edges": [asdict(e) for e in edges]}, ensure_ascii=False)
    html_text = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Spec-Code Late Binding KG</title>
<style>
body {{ margin:0; font-family:Arial, Helvetica, sans-serif; background:#f7f7f4; color:#17202a; }}
header {{ padding:16px 22px; background:#fff; border-bottom:1px solid rgba(0,0,0,.12); }}
h1 {{ margin:0 0 8px; font-size:22px; }}
.meta {{ display:flex; gap:12px; flex-wrap:wrap; color:#64748b; font-size:13px; }}
.shell {{ display:grid; grid-template-columns:330px 1fr; height:calc(100vh - 76px); }}
aside {{ background:#fff; border-right:1px solid rgba(0,0,0,.12); padding:14px; overflow:auto; }}
main {{ position:relative; overflow:hidden; }}
canvas {{ width:100%; height:100%; display:block; background:#fbfaf7; }}
h2 {{ font-size:12px; color:#64748b; text-transform:uppercase; margin:16px 0 8px; }}
input {{ width:100%; padding:8px 9px; border:1px solid rgba(0,0,0,.16); border-radius:6px; }}
label {{ display:flex; gap:7px; align-items:center; margin:7px 0; font-size:13px; }}
.row {{ display:grid; grid-template-columns:1fr auto; gap:8px; padding:4px 0; font-size:13px; }}
.swatch {{ width:11px; height:11px; border-radius:50%; display:inline-block; }}
#tip {{ position:absolute; display:none; pointer-events:none; background:#fff; border:1px solid rgba(0,0,0,.14); border-radius:6px; padding:8px 10px; box-shadow:0 8px 22px rgba(0,0,0,.14); max-width:460px; font-size:12px; }}
</style>
</head>
<body>
<header>
  <h1>Spec-Code Late Binding KG</h1>
  <div class="meta">
    <span>Spec docs: {summary["spec_docs"]}</span>
    <span>Code modules: {summary["code_modules"]}</span>
    <span>Nodes: {summary["nodes"]}</span>
    <span>Edges: {summary["edges"]}</span>
  </div>
</header>
<div class="shell">
<aside>
  <h2>Search</h2>
  <input id="search" placeholder="aes, ibex_top, reset, spec path">
  <h2>Node Types</h2>
  <div id="filters"></div>
  <h2>Edge Types</h2>
  <div id="edgeFilters"></div>
  <h2>Counts</h2>
  <div id="counts"></div>
</aside>
<main><canvas id="graph"></canvas><div id="tip"></div></main>
</div>
<script>
const data = {payload};
const colors = {{
  spec_document:"#111827", code_module:"#2563eb", ip_block:"#16a34a", approved_label:"#f97316", project:"#7c3aed"
}};
const edgeColors = {{
  EXACT_MODULE_LINK:"rgba(220,38,38,.62)", IP_BLOCK_LINK:"rgba(22,163,74,.28)",
  LABEL_TO_CODE_MODULE:"rgba(249,115,22,.22)", SPEC_MENTIONS_LABEL:"rgba(249,115,22,.32)",
  SPEC_ABOUT_IP:"rgba(22,163,74,.35)", CODE_IN_IP:"rgba(37,99,235,.25)", SPEC_IN_PROJECT:"rgba(124,58,237,.18)"
}};
let enabled = new Set(Object.keys(colors));
let enabledEdges = new Set(Object.keys(data.summary.edge_types));
let search = "";
let positions = new Map();
const canvas = document.getElementById("graph");
const ctx = canvas.getContext("2d");
const tip = document.getElementById("tip");
const nodeById = new Map(data.nodes.map(n => [n.id,n]));
function visible(n) {{
  if (!enabled.has(n.type)) return false;
  if (!search) return n.type !== "project";
  const p = n.properties || {{}};
  return `${{n.label}} ${{n.type}} ${{p.project || ""}} ${{p.ip_block || ""}} ${{p.path || ""}} ${{(p.labels || []).join(" ")}}`.toLowerCase().includes(search);
}}
function neighborhoodIds() {{
  if (!search) return null;
  const ids = new Set(data.nodes.filter(visible).map(n => n.id));
  for (const e of data.edges) {{
    if (ids.has(e.source)) ids.add(e.target);
    if (ids.has(e.target)) ids.add(e.source);
  }}
  return ids;
}}
function layout() {{
  const keep = neighborhoodIds();
  const nodes = data.nodes.filter(n => keep ? keep.has(n.id) && enabled.has(n.type) : visible(n));
  const rect = canvas.getBoundingClientRect();
  const w = Math.max(1000, rect.width), h = Math.max(700, rect.height);
  const groups = {{}};
  for (const n of nodes) {{ (groups[n.type] ||= []).push(n); }}
  const specs = groups.spec_document || [], code = groups.code_module || [];
  positions = new Map();
  for (let i=0;i<specs.length;i++) {{
    const y = 60 + (h-120) * i / Math.max(1, specs.length-1);
    positions.set(specs[i].id, {{x:w*.23 + Math.sin(i)*70, y}});
  }}
  for (let i=0;i<code.length;i++) {{
    const y = 60 + (h-120) * i / Math.max(1, code.length-1);
    positions.set(code[i].id, {{x:w*.76 + Math.cos(i)*70, y}});
  }}
  for (const type of ["ip_block","approved_label","project"]) {{
    const arr = groups[type] || [];
    for (let i=0;i<arr.length;i++) {{
      const a = Math.PI*2*i/Math.max(1,arr.length) - Math.PI/2;
      const radius = type === "ip_block" ? 190 : type === "approved_label" ? 260 : 90;
      positions.set(arr[i].id, {{x:w*.5 + Math.cos(a)*radius, y:h*.5 + Math.sin(a)*radius}});
    }}
  }}
}}
function draw() {{
  const rect = canvas.getBoundingClientRect();
  ctx.clearRect(0,0,rect.width,rect.height);
  const ids = new Set([...positions.keys()]);
  for (const e of data.edges) {{
    if (!enabledEdges.has(e.type) || !ids.has(e.source) || !ids.has(e.target)) continue;
    const a = positions.get(e.source), b = positions.get(e.target);
    ctx.beginPath();
    ctx.strokeStyle = edgeColors[e.type] || "rgba(0,0,0,.12)";
    ctx.lineWidth = e.type === "EXACT_MODULE_LINK" ? 1.7 : e.type === "IP_BLOCK_LINK" ? .8 : .6;
    ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); ctx.stroke();
  }}
  for (const [id,p] of positions.entries()) {{
    const n = nodeById.get(id);
    const r = 3 + Math.min(13, Math.sqrt(n.properties?.degree || 1)*0.45);
    ctx.beginPath(); ctx.fillStyle = colors[n.type] || "#555"; ctx.arc(p.x,p.y,r,0,Math.PI*2); ctx.fill();
    if (search || n.type === "ip_block" || n.type === "approved_label" || (n.properties?.degree || 0) > 90) {{
      ctx.font = "12px Arial"; ctx.fillStyle = "#17202a"; ctx.fillText(n.label.slice(0,56), p.x+r+4, p.y+4);
    }}
  }}
}}
function relayout() {{ layout(); draw(); }}
function resize() {{
  const rect = canvas.getBoundingClientRect();
  canvas.width = Math.floor(rect.width * devicePixelRatio);
  canvas.height = Math.floor(rect.height * devicePixelRatio);
  ctx.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0);
  relayout();
}}
const filters = document.getElementById("filters");
for (const [type,count] of Object.entries(data.summary.node_types)) {{
  const checked = type === "project" ? "" : "checked";
  if (type === "project") enabled.delete(type);
  filters.insertAdjacentHTML("beforeend", `<label><input type="checkbox" data-type="${{type}}" ${{checked}}><span class="swatch" style="background:${{colors[type] || "#555"}}"></span>${{type}} (${{count}})</label>`);
}}
filters.addEventListener("change", e => {{ const t=e.target.dataset.type; if(!t)return; if(e.target.checked)enabled.add(t); else enabled.delete(t); relayout(); }});
const edgeFilters = document.getElementById("edgeFilters");
for (const [type,count] of Object.entries(data.summary.edge_types)) {{
  edgeFilters.insertAdjacentHTML("beforeend", `<label><input type="checkbox" data-edge="${{type}}" checked>${{type}} (${{count}})</label>`);
}}
edgeFilters.addEventListener("change", e => {{ const t=e.target.dataset.edge; if(!t)return; if(e.target.checked)enabledEdges.add(t); else enabledEdges.delete(t); draw(); }});
document.getElementById("search").addEventListener("input", e => {{ search=e.target.value.trim().toLowerCase(); relayout(); }});
const counts = document.getElementById("counts");
for (const [type,count] of Object.entries(data.summary.node_types)) counts.insertAdjacentHTML("beforeend", `<div class="row"><span>${{type}}</span><strong>${{count}}</strong></div>`);
for (const [type,count] of Object.entries(data.summary.edge_types)) counts.insertAdjacentHTML("beforeend", `<div class="row"><span>${{type}}</span><strong>${{count}}</strong></div>`);
canvas.addEventListener("mousemove", e => {{
  const rect = canvas.getBoundingClientRect(), x=e.clientX-rect.left, y=e.clientY-rect.top;
  let hit=null;
  for (const [id,p] of positions.entries()) {{
    const n=nodeById.get(id), r=6+Math.min(13, Math.sqrt(n.properties?.degree || 1)*0.45);
    if (Math.hypot(p.x-x,p.y-y)<=r) {{ hit=n; break; }}
  }}
  if(!hit){{tip.style.display="none";return;}}
  tip.style.display="block"; tip.style.left=`${{x+12}}px`; tip.style.top=`${{y+12}}px`;
  const p=hit.properties||{{}};
  tip.innerHTML=`<strong>${{hit.type}}</strong><br>${{hit.label.replace(/[&<>]/g,c=>({{"&":"&amp;","<":"&lt;",">":"&gt;"}}[c]))}}<br>project: ${{p.project||""}}<br>ip: ${{p.ip_block||""}}<br>degree: ${{p.degree||0}}`;
}});
resize(); window.addEventListener("resize", resize);
</script>
</body>
</html>
"""
    (out_dir / "spec_code_kg.html").write_text(html_text, encoding="utf-8")


def write_summary(out_dir: Path, summary: dict[str, Any]) -> None:
    text = f"""# Three KG Views

## 1. Spec-Only

Input: spec documents only.

- HTML: `spec_only_kg.html`
- No code dependency.

## 2. Spec-Code

Input: spec document anchors plus code module KG.

- HTML: `spec_code_kg.html`
- JSON: `spec_code_kg.json`
- Meaning: spec and code are separate nodes joined by late-binding edges.

Counts:

- Spec documents: {summary["spec_docs"]}
- Code modules: {summary["code_modules"]}
- Nodes: {summary["nodes"]}
- Edges: {summary["edges"]}
- Edge types: {summary["edge_types"]}

## 3. Code-Only

Input: custom RTL code KG only.

- HTML: `code_only_kg.html`
- No spec document nodes.
"""
    (out_dir / "README.md").write_text(text, encoding="utf-8")


def write_index(out_dir: Path) -> None:
    html_text = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>KG Three Views</title>
<style>
body{margin:0;font-family:Arial,Helvetica,sans-serif;background:#f7f7f4;color:#17202a}
main{max-width:980px;margin:0 auto;padding:36px 22px}
h1{font-size:28px;margin:0 0 18px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}
a{display:block;text-decoration:none;color:#17202a;background:#fff;border:1px solid rgba(0,0,0,.12);border-radius:8px;padding:18px;min-height:142px}
a:hover{background:#f1f5f9}
h2{margin:0 0 8px;font-size:18px}
p{margin:0;color:#64748b;line-height:1.45}
</style>
</head>
<body><main>
<h1>KG Three Views</h1>
<div class="grid">
<a href="spec_only_kg.html"><h2>Spec-Only KG</h2><p>Spec documents only. No code, no module graph.</p></a>
<a href="spec_code_kg.html"><h2>Spec-Code KG</h2><p>Spec documents and code modules connected by late-binding edges.</p></a>
<a href="code_only_kg.html"><h2>Code-Only KG</h2><p>Custom RTL code KG with modules, ports, labels, and instantiation edges.</p></a>
</div>
</main></body></html>
"""
    (out_dir / "index.html").write_text(html_text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build three separate KG views.")
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    nodes, edges, summary = build(ANCHORS, CODE_KG)
    write_json(args.out, nodes, edges, summary)
    write_html(args.out, nodes, edges, summary)
    write_summary(args.out, summary)
    write_index(args.out)

    if SPEC_ONLY_HTML.exists():
        shutil.copy2(SPEC_ONLY_HTML, args.out / "spec_only_kg.html")
    if CODE_ONLY_HTML.exists():
        shutil.copy2(CODE_ONLY_HTML, args.out / "code_only_kg.html")
    if CODE_SUMMARY.exists():
        shutil.copy2(CODE_SUMMARY, args.out / "code_only_summary.json")

    print(json.dumps({"out": str(args.out), **summary}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
