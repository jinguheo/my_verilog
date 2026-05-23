#!/usr/bin/env python3
"""Render portable HTML summaries for Graphify KG variants.

The generated HTML files intentionally visualize representative subgraphs
instead of every node. Full graph data remains available in each variant's
`graph.json`.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_GRAPHIFY_ROOT = ROOT / "dbs" / "graphify-out"

VARIANTS = {
    "spec-only":              DEFAULT_GRAPHIFY_ROOT / "spec-only-graphify"              / "graph.json",
    "code-only":              DEFAULT_GRAPHIFY_ROOT / "code-only-graphify"              / "graph.json",
    "spec-code":              DEFAULT_GRAPHIFY_ROOT / "spec-code-graphify"              / "graph.json",
    "code-ast":               DEFAULT_GRAPHIFY_ROOT / "code-ast-graphify"               / "graph.json",
    "code-hdd":               DEFAULT_GRAPHIFY_ROOT / "code-hdd-graphify"               / "graph.json",
    "spec-hdd-code-ast":      DEFAULT_GRAPHIFY_ROOT / "spec-hdd-code-ast-graphify"      / "graph.json",
    # ibex mini comparison variants
    "ibex-mini-A":            DEFAULT_GRAPHIFY_ROOT / "ibex-mini-A"                     / "graph.json",
    "ibex-openkb-raw":        DEFAULT_GRAPHIFY_ROOT / "ibex-openkb-raw-graphify"        / "graph.json",
    "ibex-graphify-openkb":   DEFAULT_GRAPHIFY_ROOT / "ibex-graphify-openkb-graphify"   / "graph.json",
}

BRIDGE_RELATIONS = {"spec_component_matches_code", "spec_path_matches_code_path"}
CODE_RELATIONS = {"instantiates", "defines", "contains", "calls", "uses", "method"}
SPEC_RELATIONS = {"contains", "documents_component", "references_component", "mentions_topic"}


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def safe_json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")


def relation(edge: dict[str, Any]) -> str:
    return str(edge.get("relation") or edge.get("type") or "related")


def edge_source(edge: dict[str, Any]) -> str:
    return str(edge.get("source") or edge.get("_src") or "")


def edge_target(edge: dict[str, Any]) -> str:
    return str(edge.get("target") or edge.get("_tgt") or "")


def infer_project(source_file: str) -> str:
    parts = re.split(r"[\\/]+", source_file)
    return parts[0] if parts and parts[0] else "unknown"


def top_counts(counter: Counter, limit: int = 20) -> list[dict[str, Any]]:
    return [{"name": name, "count": count} for name, count in counter.most_common(limit)]


def choose_nodes(
    variant: str,
    nodes: list[dict[str, Any]],
    links: list[dict[str, Any]],
    max_nodes: int,
) -> tuple[set[str], dict[str, int]]:
    degree = Counter()
    bridge_nodes: set[str] = set()
    adjacency: dict[str, set[str]] = defaultdict(set)
    for edge in links:
        src, tgt = edge_source(edge), edge_target(edge)
        if not src or not tgt:
            continue
        rel = relation(edge)
        weight = 5 if rel in BRIDGE_RELATIONS else 1
        degree[src] += weight
        degree[tgt] += weight
        adjacency[src].add(tgt)
        adjacency[tgt].add(src)
        if rel in BRIDGE_RELATIONS:
            bridge_nodes.add(src)
            bridge_nodes.add(tgt)

    node_by_id = {str(node["id"]): node for node in nodes}
    selected: set[str] = set()

    if variant == "spec-code":
        ranked_bridge = sorted(bridge_nodes, key=lambda node_id: degree[node_id], reverse=True)
        selected.update(ranked_bridge[: max_nodes // 2])
        queue = deque(selected)
        while queue and len(selected) < max_nodes:
            current = queue.popleft()
            neighbors = sorted(adjacency[current], key=lambda node_id: degree[node_id], reverse=True)
            for neighbor in neighbors[:20]:
                if neighbor not in selected:
                    selected.add(neighbor)
                    queue.append(neighbor)
                if len(selected) >= max_nodes:
                    break

    if len(selected) < max_nodes:
        preferred_relations = SPEC_RELATIONS if variant == "spec-only" else CODE_RELATIONS
        relation_nodes = Counter()
        for edge in links:
            if relation(edge) in preferred_relations:
                relation_nodes[edge_source(edge)] += 1
                relation_nodes[edge_target(edge)] += 1
        for node_id, _ in relation_nodes.most_common(max_nodes):
            if node_id in node_by_id:
                selected.add(node_id)
            if len(selected) >= max_nodes:
                break

    if len(selected) < max_nodes:
        for node_id, _ in degree.most_common(max_nodes):
            if node_id in node_by_id:
                selected.add(node_id)
            if len(selected) >= max_nodes:
                break

    return selected, dict(degree)


def build_view(variant: str, graph_path: Path, max_nodes: int) -> dict[str, Any]:
    graph = read_json(graph_path)
    nodes = graph.get("nodes", [])
    links = graph.get("links", graph.get("edges", []))
    selected, degree = choose_nodes(variant, nodes, links, max_nodes)
    node_by_id = {str(node["id"]): node for node in nodes}

    view_links = []
    relation_counter = Counter()
    for edge in links:
        src, tgt = edge_source(edge), edge_target(edge)
        rel = relation(edge)
        relation_counter[rel] += 1
        if src in selected and tgt in selected:
            view_links.append(
                {
                    "source": src,
                    "target": tgt,
                    "relation": rel,
                    "confidence": edge.get("confidence", ""),
                    "source_file": edge.get("source_file", ""),
                    "weight": edge.get("weight", 1),
                }
            )

    file_type_counter = Counter(str(node.get("file_type") or "<none>") for node in nodes)
    role_counter = Counter(str(node.get("role") or "<none>") for node in nodes)
    project_counter = Counter(infer_project(str(node.get("source_file") or "")) for node in nodes)
    community_counter = Counter(str(node.get("community", "<none>")) for node in nodes)

    view_nodes = []
    for node_id in selected:
        node = node_by_id[node_id]
        view_nodes.append(
            {
                "id": node_id,
                "label": str(node.get("label") or node_id),
                "file_type": str(node.get("file_type") or "<none>"),
                "role": str(node.get("role") or ""),
                "source_file": str(node.get("source_file") or ""),
                "source_location": str(node.get("source_location") or ""),
                "community": str(node.get("community", "")),
                "variant": str(node.get("graph_variant") or variant),
                "degree": degree.get(node_id, 0),
            }
        )

    summary = {
        "variant": variant,
        "graph_json": str(graph_path),
        "total_nodes": len(nodes),
        "total_links": len(links),
        "view_nodes": len(view_nodes),
        "view_links": len(view_links),
        "file_types": top_counts(file_type_counter),
        "roles": top_counts(role_counter),
        "relations": top_counts(relation_counter),
        "projects": top_counts(project_counter),
        "communities": len(community_counter),
        "top_communities": top_counts(community_counter),
        "bridge_links": sum(count for rel, count in relation_counter.items() if rel in BRIDGE_RELATIONS),
    }
    return {"summary": summary, "nodes": view_nodes, "links": view_links}


def write_html(path: Path, view: dict[str, Any]) -> None:
    payload = safe_json(view)
    variant = view["summary"]["variant"]
    title = f"Graphify {variant} KG"
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  :root {{
    --bg:#f7f7f4; --panel:#fff; --ink:#17202a; --muted:#64748b; --line:rgba(23,32,42,.14);
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; font-family:Arial,Helvetica,sans-serif; background:var(--bg); color:var(--ink); }}
  header {{ padding:16px 22px 12px; background:var(--panel); border-bottom:1px solid var(--line); }}
  h1 {{ margin:0 0 8px; font-size:22px; letter-spacing:0; }}
  .meta {{ display:flex; flex-wrap:wrap; gap:12px; color:var(--muted); font-size:13px; }}
  .shell {{ display:grid; grid-template-columns:340px 1fr; height:calc(100vh - 76px); min-height:680px; }}
  aside {{ overflow:auto; background:var(--panel); border-right:1px solid var(--line); padding:14px; }}
  main {{ position:relative; overflow:hidden; }}
  canvas {{ display:block; width:100%; height:100%; background:#fbfaf7; }}
  h2 {{ margin:16px 0 8px; color:var(--muted); font-size:12px; text-transform:uppercase; }}
  h2:first-child {{ margin-top:0; }}
  input {{ width:100%; padding:8px 9px; border:1px solid var(--line); border-radius:6px; }}
  label {{ display:flex; align-items:center; gap:7px; margin:7px 0; font-size:13px; }}
  .row {{ display:grid; grid-template-columns:1fr auto; gap:8px; padding:4px 0; font-size:13px; }}
  .top {{ border-bottom:1px solid var(--line); padding:6px 0; font-size:12px; cursor:pointer; }}
  .top strong {{ display:block; font-size:13px; }}
  .swatch {{ display:inline-block; width:11px; height:11px; border-radius:50%; }}
  #tip {{ position:absolute; display:none; pointer-events:none; background:#fff; border:1px solid var(--line); border-radius:6px; padding:8px 10px; box-shadow:0 8px 22px rgba(0,0,0,.14); max-width:460px; font-size:12px; }}
  #detail {{ position:absolute; right:14px; top:14px; width:min(480px,calc(100% - 28px)); max-height:calc(100% - 28px); overflow:auto; background:rgba(255,255,255,.97); border:1px solid var(--line); border-radius:8px; padding:12px; display:none; box-shadow:0 8px 26px rgba(0,0,0,.16); }}
  #detail h3 {{ margin:0 0 8px; font-size:15px; }}
  #detail pre {{ white-space:pre-wrap; word-break:break-word; font-size:11px; color:#334155; }}
</style>
</head>
<body>
<header>
  <h1>{title}</h1>
  <div class="meta">
    <span>Total nodes: {view["summary"]["total_nodes"]}</span>
    <span>Total links: {view["summary"]["total_links"]}</span>
    <span>Displayed nodes: {view["summary"]["view_nodes"]}</span>
    <span>Displayed links: {view["summary"]["view_links"]}</span>
    <span>Bridge links: {view["summary"]["bridge_links"]}</span>
  </div>
</header>
<div class="shell">
  <aside>
    <h2>Search</h2>
    <input id="search" placeholder="label, source file, relation">
    <h2>Node Types</h2>
    <div id="typeFilters"></div>
    <h2>Relations</h2>
    <div id="relationFilters"></div>
    <h2>Counts</h2>
    <div id="counts"></div>
    <h2>Top Nodes</h2>
    <div id="topNodes"></div>
  </aside>
  <main>
    <canvas id="graph"></canvas>
    <div id="tip"></div>
    <div id="detail"></div>
  </main>
</div>
<script>
const data = {payload};
/* ── 카테고리별 색상 ────────────────────────────────────────────────
   BLUE  계열 = Code  (graphify 추출 코드 심볼)
   TEAL  계열 = AST   (tree-sitter 파싱 구조)
   GREEN 계열 = HDD   (검증 가능한 설계 문서)
   DARK  계열 = Spec  (사양 문서)
   ──────────────────────────────────────────────────────────────── */
const colors = {{
  /* Code */
  "code":         "#2563eb",   /* 파란색  — graphify 코드 심볼 */
  "rationale":    "#7c3aed",   /* 보라색  — graphify 추론 노드 */
  /* AST (teal 계열) */
  "ast_module":   "#0f766e",   /* 진한 teal */
  "ast_port":     "#0891b2",   /* 하늘색  — 포트 */
  "ast_param":    "#0d9488",   /* 중간 teal — 파라미터 */
  "ast_always":   "#f59e0b",   /* 앰버   — always 블록 */
  "ast_function": "#db2777",   /* 핑크   — 함수 */
  "ast_package":  "#8b5cf6",   /* 연보라 — 패키지 */
  /* HDD (green 계열) */
  "hdd_module":   "#16a34a",   /* 초록색  — HDD 문서 (PASS) */
  /* Spec (dark 계열) */
  "document":     "#1e3a5f",   /* 남색   — spec 문서 */
  "<none>":       "#94a3b8",   /* 회색   — 미분류 */
}};
const relationColors = {{
  /* Spec bridge */
  spec_component_matches_code:  "rgba(220,38,38,.75)",
  spec_path_matches_code_path:  "rgba(249,115,22,.60)",
  /* Code */
  instantiates:       "rgba(37,99,235,.60)",
  calls:              "rgba(37,99,235,.22)",
  contains:           "rgba(100,116,139,.22)",
  defines:            "rgba(37,99,235,.35)",
  imports_from:       "rgba(37,99,235,.18)",
  /* Spec */
  references_component: "rgba(30,58,95,.35)",
  documents_component:  "rgba(30,58,95,.28)",
  mentions_topic:       "rgba(124,58,237,.28)",
  /* AST */
  has_ast:            "rgba(15,118,110,.70)",
  ast_has_port:       "rgba(8,145,178,.45)",
  ast_has_param:      "rgba(13,148,136,.45)",
  ast_has_always:     "rgba(245,158,11,.50)",
  ast_has_fn:         "rgba(219,39,119,.45)",
  /* HDD */
  HAS_HDD:            "rgba(22,163,74,.75)",
}};
const nodesById = new Map(data.nodes.map(n => [n.id, n]));
let enabledTypes = new Set([...new Set(data.nodes.map(n => n.file_type))]);
let enabledRelations = new Set([...new Set(data.links.map(e => e.relation))]);
let search = "";
let selected = null;
let positions = new Map();
let transform = {{x:0,y:0,scale:1}};
const canvas = document.getElementById("graph");
const ctx = canvas.getContext("2d");
const tip = document.getElementById("tip");
const detail = document.getElementById("detail");

function esc(s) {{ return String(s ?? "").replace(/[&<>"]/g, c => ({{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}}[c])); }}
function visibleNode(n) {{
  if (!enabledTypes.has(n.file_type)) return false;
  if (!search) return true;
  const hay = `${{n.label}} ${{n.file_type}} ${{n.role}} ${{n.source_file}} ${{n.community}} ${{n.variant}}`.toLowerCase();
  return hay.includes(search);
}}
function visibleIds() {{
  const ids = new Set(data.nodes.filter(visibleNode).map(n => n.id));
  if (!search) return ids;
  for (const e of data.links) {{
    if (!enabledRelations.has(e.relation)) continue;
    if (ids.has(e.source)) ids.add(e.target);
    if (ids.has(e.target)) ids.add(e.source);
  }}
  return ids;
}}
function layout() {{
  const ids = visibleIds();
  const nodes = data.nodes.filter(n => ids.has(n.id) && enabledTypes.has(n.file_type));
  const rect = canvas.getBoundingClientRect();
  const w = Math.max(rect.width, 900), h = Math.max(rect.height, 680);
  const groups = {{}};
  for (const n of nodes) {{
    const key = n.variant || n.file_type;
    (groups[key] ||= []).push(n);
  }}
  const keys = Object.keys(groups).sort();
  positions = new Map();
  keys.forEach((key, gi) => {{
    const cx = w * (0.24 + 0.52 * (gi / Math.max(1, keys.length - 1)));
    const cy = h * 0.5;
    const arr = groups[key].sort((a,b) => b.degree - a.degree);
    for (let i=0;i<arr.length;i++) {{
      const a = Math.PI * 2 * i / Math.max(1, arr.length) - Math.PI/2;
      const r = 80 + Math.sqrt(i + 1) * 20;
      positions.set(arr[i].id, {{x:cx + Math.cos(a)*r, y:cy + Math.sin(a)*r}});
    }}
  }});
}}
function sx(x) {{ return x * transform.scale + transform.x; }}
function sy(y) {{ return y * transform.scale + transform.y; }}
function radius(n) {{ return 3 + Math.min(14, Math.sqrt(n.degree || 1) * 0.7); }}
function draw() {{
  const rect = canvas.getBoundingClientRect();
  ctx.clearRect(0,0,rect.width,rect.height);
  const ids = new Set([...positions.keys()]);
  for (const e of data.links) {{
    if (!enabledRelations.has(e.relation) || !ids.has(e.source) || !ids.has(e.target)) continue;
    const a = positions.get(e.source), b = positions.get(e.target);
    ctx.beginPath();
    ctx.strokeStyle = relationColors[e.relation] || "rgba(80,80,80,.18)";
    ctx.lineWidth = (e.relation.startsWith("spec_") || e.relation === "HAS_HDD") ? 2.0
                  : e.relation.startsWith("ast_") || e.relation === "has_ast" ? 1.2
                  : 0.75;
    ctx.moveTo(sx(a.x), sy(a.y)); ctx.lineTo(sx(b.x), sy(b.y)); ctx.stroke();
  }}
  for (const id of ids) {{
    const n = nodesById.get(id), p = positions.get(id), r = radius(n);
    ctx.beginPath();
    ctx.fillStyle = selected === id ? "#000" : (colors[n.file_type] || "#64748b");
    ctx.arc(sx(p.x), sy(p.y), r, 0, Math.PI*2); ctx.fill();
    const showLabel = search
      || n.degree > 80
      || (n.file_type === "document"   && n.degree > 40)
      || n.file_type === "hdd_module"
      || n.file_type === "ast_module";
    if (showLabel) {{
      ctx.font = "12px Arial"; ctx.fillStyle = "#17202a";
      ctx.fillText(n.label.slice(0,56), sx(p.x)+r+4, sy(p.y)+4);
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
function initControls() {{
  const typeCounts = new Map();
  for (const n of data.nodes) typeCounts.set(n.file_type, (typeCounts.get(n.file_type)||0)+1);
  for (const [type,count] of [...typeCounts.entries()].sort()) {{
    document.getElementById("typeFilters").insertAdjacentHTML("beforeend", `<label><input type="checkbox" data-type="${{esc(type)}}" checked><span class="swatch" style="background:${{colors[type]||"#64748b"}}"></span>${{esc(type)}} (${{count}})</label>`);
  }}
  document.getElementById("typeFilters").addEventListener("change", e => {{
    const type = e.target.dataset.type; if (!type) return;
    if (e.target.checked) enabledTypes.add(type); else enabledTypes.delete(type);
    relayout();
  }});
  const relCounts = new Map();
  for (const e of data.links) relCounts.set(e.relation, (relCounts.get(e.relation)||0)+1);
  for (const [rel,count] of [...relCounts.entries()].sort((a,b)=>b[1]-a[1]).slice(0,28)) {{
    document.getElementById("relationFilters").insertAdjacentHTML("beforeend", `<label><input type="checkbox" data-rel="${{esc(rel)}}" checked>${{esc(rel)}} (${{count}})</label>`);
  }}
  document.getElementById("relationFilters").addEventListener("change", e => {{
    const rel = e.target.dataset.rel; if (!rel) return;
    if (e.target.checked) enabledRelations.add(rel); else enabledRelations.delete(rel);
    draw();
  }});
  document.getElementById("search").addEventListener("input", e => {{ search = e.target.value.trim().toLowerCase(); relayout(); }});
  const counts = document.getElementById("counts");
  counts.innerHTML = `
    <div class="row"><span>Total nodes</span><strong>${{data.summary.total_nodes}}</strong></div>
    <div class="row"><span>Total links</span><strong>${{data.summary.total_links}}</strong></div>
    <div class="row"><span>Displayed nodes</span><strong>${{data.summary.view_nodes}}</strong></div>
    <div class="row"><span>Displayed links</span><strong>${{data.summary.view_links}}</strong></div>
    <div class="row"><span>Communities</span><strong>${{data.summary.communities}}</strong></div>
  `;
  for (const n of [...data.nodes].sort((a,b)=>b.degree-a.degree).slice(0,30)) {{
    const div = document.createElement("div");
    div.className = "top";
    div.innerHTML = `<strong>${{esc(n.label)}}</strong>${{esc(n.file_type)}} · degree ${{n.degree}} · community ${{esc(n.community)}}`;
    div.onclick = () => {{ selected = n.id; search = n.label.toLowerCase(); document.getElementById("search").value = n.label; showDetail(n); relayout(); }};
    document.getElementById("topNodes").appendChild(div);
  }}
}}
function hitTest(e) {{
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left, y = e.clientY - rect.top;
  for (const [id,p] of positions) {{
    const n = nodesById.get(id);
    if (Math.hypot(sx(p.x)-x, sy(p.y)-y) <= radius(n)+4) return n;
  }}
  return null;
}}
function showDetail(n) {{
  if (!n) {{ detail.style.display = "none"; return; }}
  const related = data.links.filter(e => e.source === n.id || e.target === n.id).slice(0,80).map(e => {{
    const other = nodesById.get(e.source === n.id ? e.target : e.source);
    return `${{e.relation}} -> ${{other ? other.label : "unknown"}}`;
  }});
  detail.style.display = "block";
  detail.innerHTML = `<h3>${{esc(n.label)}}</h3><pre>${{esc(JSON.stringify({{
    file_type:n.file_type, role:n.role, variant:n.variant, community:n.community,
    source_file:n.source_file, source_location:n.source_location, degree:n.degree,
    related
  }}, null, 2))}}</pre>`;
}}
canvas.addEventListener("mousemove", e => {{
  const n = hitTest(e), rect = canvas.getBoundingClientRect();
  if (!n) {{ tip.style.display = "none"; return; }}
  tip.style.display = "block"; tip.style.left = `${{e.clientX-rect.left+12}}px`; tip.style.top = `${{e.clientY-rect.top+12}}px`;
  tip.innerHTML = `<strong>${{esc(n.file_type)}}</strong><br>${{esc(n.label)}}<br>degree: ${{n.degree}}<br>${{esc(n.source_file)}}`;
}});
canvas.addEventListener("click", e => {{ const n = hitTest(e); selected = n?.id || null; showDetail(n); draw(); }});
canvas.addEventListener("wheel", e => {{ e.preventDefault(); transform.scale = Math.max(.18, Math.min(4, transform.scale * (e.deltaY < 0 ? 1.08 : .92))); draw(); }}, {{passive:false}});
let drag = null;
canvas.addEventListener("mousedown", e => {{ drag = {{x:e.clientX,y:e.clientY,tx:transform.x,ty:transform.y}}; }});
window.addEventListener("mouseup", () => {{ drag = null; }});
window.addEventListener("mousemove", e => {{ if (!drag) return; transform.x = drag.tx + e.clientX - drag.x; transform.y = drag.ty + e.clientY - drag.y; draw(); }});
initControls(); resize(); window.addEventListener("resize", resize);
</script>
</body>
</html>
"""
    path.write_text(html, encoding="utf-8")


def write_index(out_dir: Path, views: list[dict[str, Any]]) -> None:
    cards = []
    for view in views:
        s = view["summary"]
        cards.append(
            f"""<a href="{s['variant']}.html"><h2>{s['variant']}</h2><p>{s['total_nodes']} nodes, {s['total_links']} links. Displaying {s['view_nodes']} representative nodes.</p></a>"""
        )
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Graphify KG Variant HTML</title>
<style>
body{{margin:0;font-family:Arial,Helvetica,sans-serif;background:#f7f7f4;color:#17202a}}
main{{max-width:980px;margin:0 auto;padding:36px 22px}}
h1{{font-size:28px;margin:0 0 10px}}p{{color:#64748b;line-height:1.45}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin-top:18px}}
a{{display:block;text-decoration:none;color:#17202a;background:#fff;border:1px solid rgba(0,0,0,.12);border-radius:8px;padding:18px;min-height:142px}}
a:hover{{background:#f1f5f9}}h2{{margin:0 0 8px;font-size:18px}}
</style></head><body><main>
<h1>Graphify KG Variant HTML</h1>
<p>These views use Graphify graph.json node/link fields and show representative subgraphs for browser-friendly inspection. Full graph data remains in each variant folder.</p>
<div class="grid">{''.join(cards)}</div>
</main></body></html>"""
    (out_dir / "index.html").write_text(html, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graphify-root", type=Path, default=DEFAULT_GRAPHIFY_ROOT)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_GRAPHIFY_ROOT / "html-views")
    parser.add_argument("--max-nodes", type=int, default=1800)
    parser.add_argument("--variants", nargs="+", default=None,
                        help="Render only these variant names (default: all)")
    args = parser.parse_args()

    selected_variants = {
        k: v for k, v in VARIANTS.items()
        if args.variants is None or k in args.variants
    }

    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    views = []
    for variant, default_path in selected_variants.items():
        graph_path = args.graphify_root / default_path.relative_to(DEFAULT_GRAPHIFY_ROOT)
        view = build_view(variant, graph_path.resolve(), args.max_nodes)
        write_html(out_dir / f"{variant}.html", view)
        (out_dir / f"{variant}_view_manifest.json").write_text(
            json.dumps(view["summary"], indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        views.append(view)
    write_index(out_dir, views)
    print(json.dumps({"status": "ok", "out_dir": str(out_dir), "views": [v["summary"] for v in views]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
