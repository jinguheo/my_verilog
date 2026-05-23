#!/usr/bin/env python3
"""Render a portable Verilog module schematic viewer from Graphify code graph."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
GRAPH = ROOT / "dbs" / "graphify-out" / "code-only-graphify" / "graph.json"
OUT_DIR = ROOT / "dbs" / "graphify-out" / "schematic"
OUT_HTML = OUT_DIR / "verilog_module_schematic.html"
OUT_DATA = OUT_DIR / "verilog_module_schematic_data.json"
VERILOG_EXT = (".sv", ".v", ".svh", ".vh")


def is_verilog_node(node: dict[str, Any]) -> bool:
    source = str(node.get("source_file", "")).lower()
    label = str(node.get("label", ""))
    if not source.endswith(VERILOG_EXT):
        return False
    if not label or len(label) > 96:
        return False
    return bool(re.match(r"^[A-Za-z_][A-Za-z0-9_$]*$", label))


def edge_endpoint(edge: dict[str, Any], key: str, fallback: str) -> str:
    return str(edge.get(key) or edge.get(fallback) or "")


def path_kind(path: str) -> str:
    norm = path.replace("\\", "/").lower()
    if "/dv/sva/" in norm or "sva" in norm or "bind" in norm:
        return "SVA"
    if "/dv/" in norm or "/tb/" in norm or norm.endswith("/tb.sv") or "test" in norm:
        return "DV/TB"
    if "/rtl/" in norm or norm.endswith((".sv", ".v")):
        return "RTL"
    return "SV"


def short_path(path: str, depth: int = 5) -> str:
    parts = [part for part in re.split(r"[\\/]+", path) if part]
    return "/".join(parts[-depth:]) if parts else path


def descendant_count(root: str, children: dict[str, set[str]], limit: int = 600) -> int:
    seen: set[str] = set()
    todo = deque(children.get(root, set()))
    while todo and len(seen) < limit:
        node = todo.popleft()
        if node in seen or node == root:
            continue
        seen.add(node)
        todo.extend(children.get(node, set()) - seen)
    return len(seen)


def neighborhood(root: str, children: dict[str, set[str]], max_depth: int = 4, max_nodes: int = 180) -> tuple[list[str], list[dict[str, str]]]:
    levels: dict[str, int] = {root: 0}
    queue = deque([root])
    edges: list[dict[str, str]] = []
    while queue and len(levels) < max_nodes:
        parent = queue.popleft()
        level = levels[parent]
        if level >= max_depth:
            continue
        for child in sorted(children.get(parent, set())):
            edges.append({"source": parent, "target": child})
            if child not in levels and len(levels) < max_nodes:
                levels[child] = level + 1
                queue.append(child)
    ordered = sorted(levels, key=lambda item: (levels[item], item))
    return ordered, edges


def build_payload() -> dict[str, Any]:
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    raw_nodes = {str(node["id"]): node for node in graph.get("nodes", []) if is_verilog_node(node)}
    children: dict[str, set[str]] = defaultdict(set)
    parents: dict[str, set[str]] = defaultdict(set)
    edge_pairs: set[tuple[str, str]] = set()

    for edge in graph.get("links", []):
        if edge.get("relation") != "instantiates":
            continue
        src = edge_endpoint(edge, "source", "_src")
        tgt = edge_endpoint(edge, "target", "_tgt")
        if src not in raw_nodes or tgt not in raw_nodes or src == tgt:
            continue
        edge_pairs.add((src, tgt))
        children[src].add(tgt)
        parents[tgt].add(src)

    used_ids = {item for pair in edge_pairs for item in pair}
    nodes = {
        node_id: {
            "id": node_id,
            "label": raw_nodes[node_id].get("label", ""),
            "source_file": raw_nodes[node_id].get("source_file", ""),
            "source_location": raw_nodes[node_id].get("source_location", ""),
            "community": raw_nodes[node_id].get("community", ""),
            "kind": path_kind(str(raw_nodes[node_id].get("source_file", ""))),
            "short_path": short_path(str(raw_nodes[node_id].get("source_file", ""))),
            "out_degree": len(children.get(node_id, set())),
            "in_degree": len(parents.get(node_id, set())),
        }
        for node_id in used_ids
    }

    for node_id, node in nodes.items():
        node["descendants"] = descendant_count(node_id, children)

    top_candidates = [
        node
        for node in nodes.values()
        if node["out_degree"] > 0 and node["in_degree"] == 0
    ]
    if len(top_candidates) < 20:
        top_candidates = [node for node in nodes.values() if node["out_degree"] > 0]
    top_candidates.sort(key=lambda n: (-int(n["descendants"]), -int(n["out_degree"]), str(n["label"])))

    focus_ids = [node["id"] for node in top_candidates[:120]]
    for node in sorted(nodes.values(), key=lambda n: (-int(n["descendants"]), str(n["label"])))[:80]:
        if node["id"] not in focus_ids:
            focus_ids.append(node["id"])

    views = {}
    view_node_ids: set[str] = set()
    for node_id in focus_ids:
        node_list, edge_list = neighborhood(node_id, children)
        views[node_id] = {"nodes": node_list, "edges": edge_list}
        view_node_ids.update(node_list)

    relation_edges = [
        {"source": src, "target": tgt}
        for src, tgt in sorted(edge_pairs)
        if src in view_node_ids and tgt in view_node_ids
    ]

    by_kind = Counter(node["kind"] for node in nodes.values())
    return {
        "summary": {
            "graph": str(GRAPH.relative_to(ROOT)),
            "verilog_nodes_with_instantiation": len(nodes),
            "instantiation_edges": len(edge_pairs),
            "top_candidates": len(top_candidates),
            "kind_counts": dict(sorted(by_kind.items())),
        },
        "nodes": nodes,
        "edges": relation_edges,
        "top_modules": top_candidates[:200],
        "views": views,
    }


def write_html() -> None:
    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Verilog Module Schematic</title>
<style>
body{margin:0;font-family:Arial,Helvetica,sans-serif;background:#f7f8fb;color:#17202a}
header{padding:18px 22px;border-bottom:1px solid #d7dde7;background:#fff;position:sticky;top:0;z-index:5}
h1{font-size:22px;margin:0 0 8px}.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
input,select,button{font:inherit;border:1px solid #b8c2d0;background:#fff;border-radius:6px;padding:8px 10px}
button{cursor:pointer;background:#eef4fb}button:hover{background:#dfeaf7}
main{display:grid;grid-template-columns:360px 1fr;gap:0;min-height:calc(100vh - 86px)}
aside{border-right:1px solid #d7dde7;background:#fff;overflow:auto;max-height:calc(100vh - 86px);padding:14px}
.stats{font-size:13px;color:#526173;line-height:1.45;margin-bottom:12px}
.module{border:1px solid #d7dde7;border-radius:8px;padding:10px;margin:8px 0;background:#fff;cursor:pointer}
.module:hover{background:#f1f6fd}.module.active{border-color:#2368a2;background:#eaf3ff}
.module strong{display:block;font-size:14px}.module span{display:block;color:#64748b;font-size:12px;margin-top:4px}
#canvasWrap{overflow:auto;position:relative;background:#fbfcfe}.hint{padding:18px;color:#64748b}
svg{display:block;min-width:960px;min-height:620px}.node rect{fill:#fff;stroke:#38546f;stroke-width:1.2;rx:6}
.node.rtl rect{fill:#eef8f0}.node.dv rect{fill:#fff7e6}.node.sva rect{fill:#fceef3}.node text{font-size:12px;fill:#17202a}
.edge{stroke:#64748b;stroke-width:1.2;fill:none;marker-end:url(#arrow)}.badge{font-size:10px;fill:#64748b}
.toolbar{padding:12px 14px;border-bottom:1px solid #d7dde7;background:#fff}.details{font-size:13px;color:#475569}
@media(max-width:900px){main{grid-template-columns:1fr}aside{max-height:320px;border-right:0;border-bottom:1px solid #d7dde7}}
</style>
</head>
<body>
<header>
<h1>Verilog Module Schematic</h1>
<div class="row">
<input id="search" placeholder="Search module or path" size="34">
<select id="kind"><option value="">All kinds</option><option>RTL</option><option>DV/TB</option><option>SVA</option></select>
<button id="fit">Fit selected</button>
</div>
</header>
<main>
<aside>
<div id="stats" class="stats"></div>
<div id="list"></div>
</aside>
<section>
<div class="toolbar"><strong id="title">Select a module</strong><div id="details" class="details"></div></div>
<div id="canvasWrap"><div class="hint">Choose a top module or search for a module to draw its instantiation schematic.</div></div>
</section>
</main>
<script id="schematic-data" type="application/json">__DATA__</script>
<script>
const data = JSON.parse(document.getElementById('schematic-data').textContent);
const nodes = data.nodes;
let selected = data.top_modules[0]?.id || Object.keys(nodes)[0];
const list = document.getElementById('list');
const search = document.getElementById('search');
const kind = document.getElementById('kind');
const wrap = document.getElementById('canvasWrap');
document.getElementById('stats').innerHTML =
  `${data.summary.verilog_nodes_with_instantiation} Verilog nodes with instantiation edges<br>`+
  `${data.summary.instantiation_edges} instantiation edges<br>`+
  `${data.summary.top_candidates} top/module roots detected<br>`+
  `Kinds: ${Object.entries(data.summary.kind_counts).map(([k,v])=>`${k} ${v}`).join(', ')}`;

function moduleRows(){
  const q = search.value.toLowerCase();
  const k = kind.value;
  const ids = new Set(data.top_modules.map(n=>n.id));
  for (const id of Object.keys(nodes)) {
    const n = nodes[id];
    if ((n.label || '').toLowerCase().includes(q) || (n.source_file || '').toLowerCase().includes(q)) ids.add(id);
  }
  return [...ids].map(id=>nodes[id]).filter(n => {
    const text = `${n.label} ${n.source_file}`.toLowerCase();
    return (!q || text.includes(q)) && (!k || n.kind === k);
  }).sort((a,b)=>(b.descendants-a.descendants)||(b.out_degree-a.out_degree)||a.label.localeCompare(b.label)).slice(0,240);
}

function renderList(){
  list.innerHTML = '';
  for (const n of moduleRows()) {
    const div = document.createElement('div');
    div.className = 'module' + (n.id===selected ? ' active':'');
    div.innerHTML = `<strong>${escapeHtml(n.label)}</strong><span>${n.kind} · children ${n.out_degree} · descendants ${n.descendants}</span><span>${escapeHtml(n.short_path)}</span>`;
    div.onclick = () => { selected = n.id; renderList(); draw(); };
    list.appendChild(div);
  }
}

function viewFor(id){
  if (data.views[id]) return data.views[id];
  const edges = data.edges.filter(e=>e.source===id || e.target===id);
  const ids = [...new Set([id, ...edges.flatMap(e=>[e.source,e.target])])];
  return {nodes: ids, edges};
}

function draw(){
  const root = nodes[selected];
  if (!root) return;
  const view = viewFor(selected);
  document.getElementById('title').textContent = root.label;
  document.getElementById('details').textContent = `${root.kind} · ${root.source_file} · ${root.source_location || ''}`;
  const level = {[selected]:0};
  const outgoing = {};
  for (const e of view.edges) (outgoing[e.source] ||= []).push(e.target);
  const queue = [selected];
  while(queue.length){
    const id = queue.shift();
    for(const child of outgoing[id] || []){
      if(level[child] === undefined){ level[child] = level[id] + 1; queue.push(child); }
    }
  }
  for (const id of view.nodes) if(level[id] === undefined) level[id] = 1;
  const groups = {};
  for (const id of view.nodes) (groups[level[id]] ||= []).push(id);
  const colW = 250, rowH = 92, boxW = 190, boxH = 58;
  const positions = {};
  const levels = Object.keys(groups).map(Number).sort((a,b)=>a-b);
  let maxRows = 1;
  for (const l of levels) {
    groups[l].sort((a,b)=>nodes[a].label.localeCompare(nodes[b].label));
    maxRows = Math.max(maxRows, groups[l].length);
    groups[l].forEach((id,i)=> positions[id] = {x: 40 + l*colW, y: 36 + i*rowH});
  }
  const width = Math.max(960, 90 + (Math.max(...levels)+1)*colW);
  const height = Math.max(620, 90 + maxRows*rowH);
  let svg = `<svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}"><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/></marker></defs>`;
  for (const e of view.edges) {
    const a = positions[e.source], b = positions[e.target];
    if(!a || !b) continue;
    const x1 = a.x + boxW, y1 = a.y + boxH/2, x2 = b.x, y2 = b.y + boxH/2;
    const mx = (x1+x2)/2;
    svg += `<path class="edge" d="M${x1},${y1} C${mx},${y1} ${mx},${y2} ${x2},${y2}"/>`;
  }
  for (const id of view.nodes) {
    const n = nodes[id], p = positions[id]; if(!p) continue;
    const cls = n.kind === 'SVA' ? 'sva' : (n.kind === 'DV/TB' ? 'dv' : 'rtl');
    svg += `<g class="node ${cls}" transform="translate(${p.x},${p.y})"><rect width="${boxW}" height="${boxH}"/>`+
      `<text x="10" y="20">${escapeSvg(trim(n.label,24))}</text>`+
      `<text class="badge" x="10" y="38">${n.kind} · out ${n.out_degree} · in ${n.in_degree}</text>`+
      `<text class="badge" x="10" y="52">${escapeSvg(trim(n.short_path,32))}</text></g>`;
  }
  svg += '</svg>';
  wrap.innerHTML = svg;
}

function trim(s,n){ return (s||'').length>n ? s.slice(0,n-1)+'…' : (s||''); }
function escapeHtml(s){ return (s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function escapeSvg(s){ return escapeHtml(s); }
search.oninput = renderList; kind.onchange = renderList;
document.getElementById('fit').onclick = () => wrap.scrollTo({top:0,left:0,behavior:'smooth'});
renderList(); draw();
</script>
</body>
</html>
"""
    payload = build_payload()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DATA.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_HTML.write_text(html.replace("__DATA__", json.dumps(payload, ensure_ascii=False)), encoding="utf-8")
    print(json.dumps({"status": "ok", "html": str(OUT_HTML), "data": str(OUT_DATA), "summary": payload["summary"]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    write_html()
