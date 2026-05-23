#!/usr/bin/env python3
"""Render a spec-code-only bridge graph view.

This view keeps only relationships that require spec and code to coexist:
`spec_component_matches_code` and `spec_path_matches_code_path`.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
GRAPH_PATH = ROOT / "dbs" / "graphify-out" / "spec-code-graphify" / "graph.json"
OUT_DIR = ROOT / "dbs" / "graphify-out" / "html-views"
BRIDGE_RELATIONS = {"spec_component_matches_code", "spec_path_matches_code_path"}


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


def component_key(node: dict[str, Any]) -> str:
    label = str(node.get("label") or "")
    if label.startswith("component:"):
        return label.split(":", 1)[1]
    source = str(node.get("source_file") or "")
    parts = re.split(r"[\\/]+", source)
    for marker in ("ip_autogen", "ip"):
        if marker in parts:
            idx = parts.index(marker)
            if idx + 1 < len(parts):
                return parts[idx + 1]
    for part in parts:
        if part in {"rtl", "dv", "data", "doc"}:
            continue
        if re.search(r"ctrl|mgr|handler|ibex|aes|uart|spi|i2c|gpio|rv_|sensor|alert", part):
            return part
    return "unknown"


def node_kind(node: dict[str, Any]) -> str:
    if node.get("file_type") == "document":
        role = str(node.get("role") or "document")
        return f"spec:{role}"
    return "code"


def build_bridge_view(graph_path: Path, max_edges: int) -> dict[str, Any]:
    graph = read_json(graph_path)
    all_nodes = {str(node["id"]): node for node in graph.get("nodes", [])}
    all_links = graph.get("links", graph.get("edges", []))

    bridge_links = []
    bridge_degree: Counter[str] = Counter()
    component_counter: Counter[str] = Counter()
    relation_counter: Counter[str] = Counter()
    examples_by_component: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for edge in all_links:
        rel = relation(edge)
        if rel not in BRIDGE_RELATIONS:
            continue
        src, tgt = edge_source(edge), edge_target(edge)
        if src not in all_nodes or tgt not in all_nodes:
            continue
        source_node, target_node = all_nodes[src], all_nodes[tgt]
        if source_node.get("file_type") == target_node.get("file_type"):
            continue
        component = component_key(source_node if source_node.get("file_type") == "document" else target_node)
        if component == "unknown":
            component = component_key(target_node if source_node.get("file_type") == "document" else source_node)
        relation_counter[rel] += 1
        component_counter[component] += 1
        bridge_degree[src] += 1
        bridge_degree[tgt] += 1
        bridge_links.append(
            {
                "source": src,
                "target": tgt,
                "relation": rel,
                "component": component,
                "weight": edge.get("weight", 1),
            }
        )
        if len(examples_by_component[component]) < 8:
            examples_by_component[component].append(
                {
                    "relation": rel,
                    "spec": source_node if source_node.get("file_type") == "document" else target_node,
                    "code": target_node if source_node.get("file_type") == "document" else source_node,
                }
            )

    ranked_edges = sorted(
        bridge_links,
        key=lambda edge: (
            -component_counter[edge["component"]],
            -bridge_degree[edge["source"]] - bridge_degree[edge["target"]],
            edge["component"],
            edge["source"],
            edge["target"],
        ),
    )[:max_edges]

    selected_nodes = {edge["source"] for edge in ranked_edges} | {edge["target"] for edge in ranked_edges}
    nodes = []
    for node_id in selected_nodes:
        node = all_nodes[node_id]
        nodes.append(
            {
                "id": node_id,
                "label": str(node.get("label") or node_id),
                "kind": node_kind(node),
                "file_type": str(node.get("file_type") or ""),
                "role": str(node.get("role") or ""),
                "source_file": str(node.get("source_file") or ""),
                "source_location": str(node.get("source_location") or ""),
                "community": str(node.get("community") or ""),
                "component": component_key(node),
                "bridge_degree": bridge_degree[node_id],
            }
        )

    component_rows = []
    for component, count in component_counter.most_common(40):
        examples = examples_by_component[component]
        component_rows.append(
            {
                "component": component,
                "bridge_edges": count,
                "sample_spec": str(examples[0]["spec"].get("label") or ""),
                "sample_code": str(examples[0]["code"].get("label") or ""),
                "sample_code_file": str(examples[0]["code"].get("source_file") or ""),
            }
        )

    summary = {
        "source_graph": str(graph_path),
        "total_spec_code_nodes": len(all_nodes),
        "total_spec_code_links": len(all_links),
        "total_bridge_links": len(bridge_links),
        "displayed_bridge_links": len(ranked_edges),
        "displayed_nodes": len(nodes),
        "relations": [{"name": rel, "count": count} for rel, count in relation_counter.most_common()],
        "top_components": component_rows,
    }
    return {"summary": summary, "nodes": nodes, "links": ranked_edges}


def write_markdown(path: Path, view: dict[str, Any]) -> None:
    lines = [
        "# Spec-Code Only Bridge Summary",
        "",
        "This report keeps only relationships that require both spec and code graphs.",
        "",
        f"- Source graph: `{view['summary']['source_graph']}`",
        f"- Total bridge links: {view['summary']['total_bridge_links']}",
        f"- Displayed bridge links: {view['summary']['displayed_bridge_links']}",
        f"- Displayed nodes: {view['summary']['displayed_nodes']}",
        "",
        "## Bridge Relations",
        "",
        "| Relation | Count |",
        "|---|---:|",
    ]
    for row in view["summary"]["relations"]:
        lines.append(f"| `{row['name']}` | {row['count']} |")
    lines += [
        "",
        "## Top Components",
        "",
        "| Component | Bridge edges | Sample spec | Sample code | Sample code file |",
        "|---|---:|---|---|---|",
    ]
    for row in view["summary"]["top_components"]:
        lines.append(
            f"| `{row['component']}` | {row['bridge_edges']} | `{row['sample_spec']}` | "
            f"`{row['sample_code']}` | `{row['sample_code_file']}` |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_html(path: Path, view: dict[str, Any]) -> None:
    payload = safe_json(view)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Spec-Code Only Bridge Graph</title>
<style>
:root {{ --bg:#f6f7f9; --panel:#fff; --ink:#17202a; --muted:#667085; --line:#d7dde7; --spec:#2f6fed; --code:#16875f; --bridge:#b7791f; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family:Arial,Helvetica,sans-serif; background:var(--bg); color:var(--ink); }}
header {{ padding:16px 20px 12px; background:var(--panel); border-bottom:1px solid var(--line); }}
h1 {{ margin:0 0 7px; font-size:22px; }}
.meta {{ display:flex; flex-wrap:wrap; gap:12px; color:var(--muted); font-size:13px; }}
.shell {{ display:grid; grid-template-columns:360px 1fr; height:calc(100vh - 75px); min-height:700px; }}
aside {{ overflow:auto; padding:14px; background:var(--panel); border-right:1px solid var(--line); }}
main {{ position:relative; overflow:hidden; }}
canvas {{ display:block; width:100%; height:100%; background:#fbfaf7; }}
h2 {{ margin:16px 0 8px; font-size:12px; text-transform:uppercase; color:var(--muted); }}
h2:first-child {{ margin-top:0; }}
input, select {{ width:100%; padding:8px; border:1px solid var(--line); border-radius:6px; background:#fff; }}
.row {{ display:grid; grid-template-columns:1fr auto; gap:8px; font-size:13px; padding:4px 0; }}
.legend {{ display:flex; gap:12px; flex-wrap:wrap; font-size:13px; color:var(--muted); }}
.dot {{ display:inline-block; width:11px; height:11px; border-radius:50%; margin-right:5px; vertical-align:-1px; }}
.spec {{ background:var(--spec); }} .code {{ background:var(--code); }} .bridge {{ background:var(--bridge); }}
.component {{ border-top:1px solid var(--line); padding:8px 0; cursor:pointer; }}
.component strong {{ display:block; font-size:13px; }}
.component span {{ display:block; color:var(--muted); font-size:12px; margin-top:2px; }}
#tip {{ position:absolute; display:none; pointer-events:none; background:#fff; border:1px solid var(--line); border-radius:6px; box-shadow:0 8px 22px rgba(0,0,0,.14); padding:8px 10px; max-width:460px; font-size:12px; }}
#detail {{ position:absolute; right:14px; top:14px; width:min(520px,calc(100% - 28px)); max-height:calc(100% - 28px); overflow:auto; display:none; background:rgba(255,255,255,.97); border:1px solid var(--line); border-radius:8px; box-shadow:0 8px 26px rgba(0,0,0,.16); padding:12px; }}
#detail h3 {{ margin:0 0 8px; font-size:15px; }}
#detail pre {{ white-space:pre-wrap; word-break:break-word; font-size:11px; color:#344054; }}
@media (max-width:900px) {{ .shell {{ grid-template-columns:1fr; height:auto; }} main {{ height:680px; }} }}
</style>
</head>
<body>
<header>
  <h1>Spec-Code Only Bridge Graph</h1>
  <div class="meta">
    <span>Total bridge links: {view['summary']['total_bridge_links']}</span>
    <span>Displayed bridge links: {view['summary']['displayed_bridge_links']}</span>
    <span>Displayed nodes: {view['summary']['displayed_nodes']}</span>
    <span>Relations: spec_component_matches_code, spec_path_matches_code_path</span>
  </div>
</header>
<div class="shell">
<aside>
  <h2>Filter</h2>
  <input id="search" placeholder="Search component, spec, code, file">
  <h2>Legend</h2>
  <div class="legend"><span><i class="dot spec"></i>Spec</span><span><i class="dot code"></i>Code</span><span><i class="dot bridge"></i>Spec-code bridge</span></div>
  <h2>Bridge Relations</h2>
  <div id="relations"></div>
  <h2>Top Components</h2>
  <div id="components"></div>
</aside>
<main>
  <canvas id="canvas"></canvas>
  <div id="tip"></div>
  <div id="detail"></div>
</main>
</div>
<script>
const data = {payload};
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const tip = document.getElementById("tip");
const detail = document.getElementById("detail");
const search = document.getElementById("search");
const nodeById = new Map(data.nodes.map(n => [n.id, n]));
const links = data.links.filter(e => nodeById.has(e.source) && nodeById.has(e.target));
const nodes = data.nodes;
let selectedComponent = "";
let transform = {{x:0,y:0,k:1}};
let drag = null;
function esc(s) {{ return String(s ?? "").replace(/[&<>]/g, c => ({{"&":"&amp;","<":"&lt;",">":"&gt;"}}[c])); }}
function color(n) {{ return n.file_type === "document" ? "#2f6fed" : "#16875f"; }}
function radius(n) {{ return 4 + Math.min(13, Math.sqrt(n.bridge_degree || 1) * 0.9); }}
function resize() {{ const rect = canvas.parentElement.getBoundingClientRect(); canvas.width = Math.floor(rect.width * devicePixelRatio); canvas.height = Math.floor(rect.height * devicePixelRatio); canvas.style.width = rect.width+"px"; canvas.style.height = rect.height+"px"; ctx.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0); layout(); draw(); }}
function layout() {{
  const rect = canvas.getBoundingClientRect();
  const comps = [...new Set(nodes.map(n => n.component || "unknown"))].sort();
  const centers = new Map();
  comps.forEach((c,i) => {{
    const angle = (Math.PI*2*i)/Math.max(1, comps.length);
    centers.set(c, {{x:rect.width/2 + Math.cos(angle)*rect.width*0.28, y:rect.height/2 + Math.sin(angle)*rect.height*0.32}});
  }});
  const perComp = new Map();
  for (const n of nodes) {{ const c=n.component||"unknown"; if(!perComp.has(c)) perComp.set(c, []); perComp.get(c).push(n); }}
  for (const [comp, arr] of perComp) {{
    const center = centers.get(comp);
    arr.sort((a,b) => (a.file_type === b.file_type ? 0 : a.file_type === "document" ? -1 : 1) || b.bridge_degree - a.bridge_degree);
    arr.forEach((n,i) => {{
      const side = n.file_type === "document" ? -1 : 1;
      const band = Math.floor(i / 18);
      const pos = i % 18;
      n.x = center.x + side * (70 + band*42);
      n.y = center.y + (pos - 8.5) * 14;
      n.vx = 0; n.vy = 0;
    }});
  }}
  for (let step=0; step<120; step++) {{
    for (const e of links) {{
      const a=nodeById.get(e.source), b=nodeById.get(e.target);
      const dx=b.x-a.x, dy=b.y-a.y, dist=Math.max(1, Math.hypot(dx,dy));
      const force=(dist-95)*0.002;
      a.x += dx*force; a.y += dy*force; b.x -= dx*force; b.y -= dy*force;
    }}
  }}
}}
function isVisible(n) {{
  const q = search.value.trim().toLowerCase();
  const text = [n.label,n.kind,n.source_file,n.component].join(" ").toLowerCase();
  return (!selectedComponent || n.component === selectedComponent) && (!q || text.includes(q));
}}
function draw() {{
  const rect = canvas.getBoundingClientRect();
  ctx.clearRect(0,0,rect.width,rect.height);
  ctx.save(); ctx.translate(transform.x, transform.y); ctx.scale(transform.k, transform.k);
  ctx.lineWidth = 1 / transform.k;
  for (const e of links) {{
    const a=nodeById.get(e.source), b=nodeById.get(e.target);
    const visible = isVisible(a) && isVisible(b);
    ctx.strokeStyle = visible ? "rgba(183,121,31,.48)" : "rgba(110,118,129,.08)";
    ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); ctx.stroke();
  }}
  for (const n of nodes) {{
    const visible = isVisible(n);
    ctx.globalAlpha = visible ? 1 : 0.12;
    ctx.fillStyle = color(n);
    ctx.beginPath(); ctx.arc(n.x,n.y,radius(n),0,Math.PI*2); ctx.fill();
    if (visible && (n.bridge_degree > 12 || search.value)) {{
      ctx.fillStyle = "#17202a"; ctx.font = `${{11/transform.k}}px Arial`; ctx.fillText(n.label.slice(0,34), n.x + radius(n) + 3, n.y + 3);
    }}
  }}
  ctx.restore(); ctx.globalAlpha = 1;
}}
function hitTest(evt) {{
  const rect = canvas.getBoundingClientRect();
  const x=(evt.clientX-rect.left-transform.x)/transform.k, y=(evt.clientY-rect.top-transform.y)/transform.k;
  let best=null, bestD=Infinity;
  for (const n of nodes) {{
    const d=Math.hypot(n.x-x,n.y-y);
    if (d < radius(n)+5 && d < bestD) {{ best=n; bestD=d; }}
  }}
  return best;
}}
canvas.addEventListener("mousemove", evt => {{
  if (drag) {{ transform.x = drag.tx + evt.clientX - drag.x; transform.y = drag.ty + evt.clientY - drag.y; draw(); return; }}
  const n=hitTest(evt);
  if (!n) {{ tip.style.display="none"; return; }}
  tip.style.display="block"; tip.style.left=evt.clientX-canvas.getBoundingClientRect().left+12+"px"; tip.style.top=evt.clientY-canvas.getBoundingClientRect().top+12+"px";
  tip.innerHTML = `<strong>${{esc(n.kind)}}</strong><br>${{esc(n.label)}}<br>component: ${{esc(n.component)}}<br>bridge degree: ${{n.bridge_degree}}<br>${{esc(n.source_file)}}`;
}});
canvas.addEventListener("mousedown", evt => {{ drag={{x:evt.clientX,y:evt.clientY,tx:transform.x,ty:transform.y}}; }});
window.addEventListener("mouseup", () => drag=null);
canvas.addEventListener("click", evt => {{
  const n=hitTest(evt); if(!n) return;
  detail.style.display="block";
  const connected = links.filter(e => e.source===n.id || e.target===n.id).slice(0,80).map(e => {{
    const other=nodeById.get(e.source===n.id?e.target:e.source);
    return `${{e.relation}} -> ${{other.label}} (${{other.file_type}})`;
  }}).join("\\n");
  detail.innerHTML = `<h3>${{esc(n.label)}}</h3><pre>${{esc(JSON.stringify(n,null,2))}}\\n\\nConnected bridge edges:\\n${{esc(connected)}}</pre>`;
}});
canvas.addEventListener("wheel", evt => {{ evt.preventDefault(); const f=evt.deltaY<0?1.08:.92; transform.k=Math.max(.25,Math.min(4,transform.k*f)); draw(); }}, {{passive:false}});
search.addEventListener("input", draw);
document.getElementById("relations").innerHTML = data.summary.relations.map(r => `<div class="row"><span>${{esc(r.name)}}</span><strong>${{r.count}}</strong></div>`).join("");
document.getElementById("components").innerHTML = data.summary.top_components.map(r => `<div class="component" data-c="${{esc(r.component)}}"><strong>${{esc(r.component)}} · ${{r.bridge_edges}}</strong><span>${{esc(r.sample_spec)}} -> ${{esc(r.sample_code)}}</span></div>`).join("");
document.getElementById("components").addEventListener("click", evt => {{ const item=evt.target.closest(".component"); if(!item)return; selectedComponent = selectedComponent===item.dataset.c ? "" : item.dataset.c; draw(); }});
resize(); window.addEventListener("resize", resize);
</script>
</body>
</html>
"""
    path.write_text(html, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph", type=Path, default=GRAPH_PATH)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    parser.add_argument("--max-edges", type=int, default=2400)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    view = build_bridge_view(args.graph, args.max_edges)
    html_path = args.out_dir / "spec-code-bridge-only.html"
    json_path = args.out_dir / "spec-code-bridge-only.json"
    md_path = args.out_dir / "spec-code-bridge-only.md"
    write_html(html_path, view)
    write_markdown(md_path, view)
    json_path.write_text(json.dumps(view, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "ok",
                "html": str(html_path),
                "json": str(json_path),
                "markdown": str(md_path),
                "summary": view["summary"],
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
