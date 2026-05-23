#!/usr/bin/env python3
"""
Build and render 4 graph variant HTML views.

Variants:
  1. code-only          existing graphify code graph
  2. code-ast           code + tree-sitter AST nodes
  3. code-hdd           code + AST + HDD document nodes
  4. spec-hdd-code-ast  spec + HDD + code + AST (full stack)

Output: out/graph-views/
  code-only.html
  code-ast.html
  code-hdd.html
  spec-hdd-code-ast.html
  index.html

Usage:
  python build_graph_views.py
  python build_graph_views.py --out-dir out/graph-views --max-nodes 2000
"""
from __future__ import annotations

import argparse
import json
import math
import os
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]

# ── source paths ─────────────────────────────────────────────────────────────
CODE_ONLY_GRAPH    = ROOT / "dbs/graphify-out/code-only-graphify/graph.json"
SPEC_CODE_GRAPH    = ROOT / "dbs/graphify-out/spec-code-graphify/graph.json"
CODE_AST_GRAPH     = ROOT / "out/ast/code-only-ast-enriched.json"
HDD_DIR            = ROOT / "out/hdd"
HDD_INDEX          = HDD_DIR / "index.json"

# ── color palette ─────────────────────────────────────────────────────────────
COLORS: dict[str, str] = {
    "code":         "#2563eb",
    "document":     "#374151",
    "rationale":    "#7c3aed",
    "ast_module":   "#0f766e",
    "ast_port":     "#0891b2",
    "ast_param":    "#f97316",
    "ast_always":   "#d97706",
    "ast_function": "#db2777",
    "ast_package":  "#7c3aed",
    "hdd_module":   "#16a34a",
    "<none>":       "#94a3b8",
}

RELATION_COLORS: dict[str, str] = {
    "spec_component_matches_code":  "rgba(220,38,38,.75)",
    "spec_path_matches_code_path":  "rgba(249,115,22,.55)",
    "instantiates":                 "rgba(37,99,235,.55)",
    "calls":                        "rgba(37,99,235,.22)",
    "contains":                     "rgba(100,116,139,.22)",
    "references_component":         "rgba(22,163,74,.32)",
    "documents_component":          "rgba(22,163,74,.28)",
    "has_ast":                      "rgba(15,118,110,.65)",
    "ast_has_port":                 "rgba(8,145,178,.38)",
    "ast_has_param":                "rgba(249,115,22,.38)",
    "ast_has_always":               "rgba(217,119,6,.38)",
    "ast_has_fn":                   "rgba(219,39,119,.38)",
    "HAS_HDD":                      "rgba(22,163,74,.70)",
    "SPEC_LINKED":                  "rgba(220,38,38,.55)",
    "AST_SAME_AS_ONTOLOGY":         "rgba(15,118,110,.45)",
}

BRIDGE_RELS = {"spec_component_matches_code", "spec_path_matches_code_path"}
CODE_RELS   = {"instantiates", "defines", "contains", "calls", "uses", "method"}
SPEC_RELS   = {"contains", "documents_component", "references_component"}
AST_RELS    = {"has_ast", "ast_has_port", "ast_has_param", "ast_has_always", "ast_has_fn"}
HDD_RELS    = {"HAS_HDD", "SPEC_LINKED"}


# ── helpers ───────────────────────────────────────────────────────────────────

def rj(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def safe_json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")

def rel_of(e: dict) -> str:
    return str(e.get("relation") or e.get("type") or "related")

def src_of(e: dict) -> str:
    return str(e.get("source") or e.get("_src") or "")

def tgt_of(e: dict) -> str:
    return str(e.get("target") or e.get("_tgt") or "")


# ── graph builders ────────────────────────────────────────────────────────────

def load_code_ast() -> dict:
    """code-only-ast-enriched graph (code + AST nodes)."""
    return rj(CODE_AST_GRAPH)


def build_code_hdd(code_ast: dict) -> dict:
    """Add HDD module nodes to the code-ast graph."""
    if not HDD_INDEX.exists():
        raise FileNotFoundError(f"HDD index not found: {HDD_INDEX}")

    index = rj(HDD_INDEX)
    nodes = list(code_ast["nodes"])
    links = list(code_ast["links"])
    existing_ids = {n["id"] for n in nodes}

    # Index ast_module nodes by module name
    ast_mod_by_name: dict[str, str] = {}
    for n in nodes:
        if n.get("file_type") == "ast_module":
            ast_mod_by_name[n.get("label", "").lower()] = n["id"]

    for entry in index.get("modules", []):
        name    = entry["module"]
        hid     = f"hdd_{name}"
        if hid in existing_ids:
            continue

        # Load HDD doc for verification status
        json_path = Path(entry.get("json", ""))
        ver_status = "NOT_RUN"
        pass_rate  = 0.0
        spec_refs  = 0
        if json_path.exists():
            try:
                doc = rj(json_path)
                ver = doc.get("verification", {})
                ver_status = ver.get("status", "NOT_RUN")
                total      = ver.get("total", 1) or 1
                pass_rate  = round(ver.get("pass", 0) / total, 3)
                spec_refs  = len(doc.get("spec_references", []))
            except Exception:
                pass

        nodes.append({
            "id":           hid,
            "label":        name,
            "file_type":    "hdd_module",
            "role":         "hdd",
            "source_file":  entry.get("source_file", ""),
            "source_location": "L0",
            "community":    "",
            "norm_label":   name,
            "port_count":   entry.get("port_count", 0),
            "param_count":  entry.get("param_count", 0),
            "parse_errors": entry.get("parse_errors", False),
            "verify_status": ver_status,
            "pass_rate":    pass_rate,
            "spec_refs":    spec_refs,
        })
        existing_ids.add(hid)

        # HAS_HDD: ast_module → hdd_module
        ast_id = ast_mod_by_name.get(name.lower())
        if ast_id:
            links.append({
                "source":      ast_id,
                "target":      hid,
                "relation":    "HAS_HDD",
                "weight":      2.0,
                "source_file": entry.get("source_file", ""),
                "source_location": "L0",
            })

        # SPEC_LINKED: hdd_module → (implied spec presence)
        if spec_refs > 0:
            links.append({
                "source":      hid,
                "target":      hid,   # self-loop marker (filtered in draw)
                "relation":    "SPEC_LINKED",
                "weight":      1.0,
                "source_file": "",
                "source_location": "",
                "spec_refs":   spec_refs,
            })

    return {"nodes": nodes, "links": links}


def build_spec_hdd_code_ast(code_hdd: dict) -> dict:
    """
    Merge spec-code graphify with the code-hdd graph.
    Result: spec + code + AST + HDD all in one graph.
    """
    spec_code = rj(SPEC_CODE_GRAPH)
    existing_ids = {n["id"] for n in code_hdd["nodes"]}

    nodes = list(code_hdd["nodes"])
    links = list(code_hdd["links"])

    # Add spec (document) nodes from spec-code graph
    for n in spec_code["nodes"]:
        if n.get("file_type") == "document" and n["id"] not in existing_ids:
            nodes.append({
                "id":           n["id"],
                "label":        n.get("label", ""),
                "file_type":    "document",
                "role":         n.get("role", ""),
                "source_file":  n.get("source_file", ""),
                "source_location": n.get("source_location", ""),
                "community":    str(n.get("community", "")),
                "norm_label":   n.get("norm_label", n.get("label", "")),
            })
            existing_ids.add(n["id"])

    all_ids = existing_ids

    # Add spec bridge links (spec → code)
    for e in spec_code["links"]:
        rel = rel_of(e)
        if rel in BRIDGE_RELS:
            s, t = src_of(e), tgt_of(e)
            if s in all_ids and t in all_ids:
                links.append({
                    "source":      s,
                    "target":      t,
                    "relation":    rel,
                    "weight":      e.get("weight", 1.0),
                    "source_file": e.get("source_file", ""),
                    "source_location": e.get("source_location", ""),
                })

    # Add spec→HDD links via HDD spec_references
    if HDD_INDEX.exists():
        index = rj(HDD_INDEX)
        hdd_by_name = {e["module"]: f"hdd_{e['module']}" for e in index.get("modules", [])}
        for entry in index.get("modules", []):
            hid = f"hdd_{entry['module']}"
            if hid not in all_ids:
                continue
            json_path = Path(entry.get("json", ""))
            if not json_path.exists():
                continue
            try:
                doc = rj(json_path)
                for ref in doc.get("spec_references", [])[:10]:
                    spec_id = ref.get("spec_id", "")
                    if spec_id and spec_id in all_ids:
                        links.append({
                            "source":      spec_id,
                            "target":      hid,
                            "relation":    "spec_path_matches_code_path",
                            "weight":      1.0,
                            "source_file": ref.get("spec_file", ""),
                            "source_location": "",
                        })
            except Exception:
                pass

    return {"nodes": nodes, "links": links}


# ── view selector ─────────────────────────────────────────────────────────────

PRIORITY_RELS = {
    "code-only":         CODE_RELS,
    "code-ast":          CODE_RELS | AST_RELS,
    "code-hdd":          CODE_RELS | AST_RELS | HDD_RELS,
    "spec-hdd-code-ast": CODE_RELS | AST_RELS | HDD_RELS | BRIDGE_RELS | SPEC_RELS,
}


def choose_nodes(variant: str, nodes: list, links: list, max_nodes: int):
    degree: Counter = Counter()
    bridge_ids: set[str] = set()
    adj: dict[str, set[str]] = defaultdict(set)

    for e in links:
        s, t, r = src_of(e), tgt_of(e), rel_of(e)
        if not s or not t or s == t:
            continue
        w = 6 if r in BRIDGE_RELS | HDD_RELS else 2 if r in AST_RELS else 1
        degree[s] += w
        degree[t] += w
        adj[s].add(t)
        adj[t].add(s)
        if r in BRIDGE_RELS | HDD_RELS:
            bridge_ids.add(s)
            bridge_ids.add(t)

    nbi = {n["id"]: n for n in nodes}
    selected: set[str] = set()

    # 1. Seed with bridge / HDD nodes
    ranked_bridge = sorted(bridge_ids & set(nbi), key=lambda i: degree[i], reverse=True)
    selected.update(ranked_bridge[: max_nodes // 3])

    # 2. BFS expand
    queue = deque(selected)
    while queue and len(selected) < max_nodes:
        cur = queue.popleft()
        for nb in sorted(adj[cur], key=lambda i: degree[i], reverse=True)[:12]:
            if nb not in selected and nb in nbi:
                selected.add(nb)
                queue.append(nb)
            if len(selected) >= max_nodes:
                break

    # 3. Fill with high-degree nodes
    prel = PRIORITY_RELS.get(variant, CODE_RELS)
    if len(selected) < max_nodes:
        pcounts: Counter = Counter()
        for e in links:
            if rel_of(e) in prel:
                pcounts[src_of(e)] += 1
                pcounts[tgt_of(e)] += 1
        for nid, _ in pcounts.most_common(max_nodes):
            if nid in nbi:
                selected.add(nid)
            if len(selected) >= max_nodes:
                break

    if len(selected) < max_nodes:
        for nid, _ in degree.most_common(max_nodes):
            if nid in nbi:
                selected.add(nid)
            if len(selected) >= max_nodes:
                break

    return selected, dict(degree)


def build_view(variant: str, graph: dict, max_nodes: int) -> dict:
    nodes = graph.get("nodes", [])
    links = graph.get("links", graph.get("edges", []))
    selected, degree = choose_nodes(variant, nodes, links, max_nodes)
    nbi = {n["id"]: n for n in nodes}

    view_links = []
    rel_counter: Counter = Counter()
    for e in links:
        s, t, r = src_of(e), tgt_of(e), rel_of(e)
        rel_counter[r] += 1
        if s in selected and t in selected and s != t:
            view_links.append({
                "source":   s,
                "target":   t,
                "relation": r,
                "weight":   e.get("weight", 1),
            })

    ft_counter  = Counter(str(n.get("file_type") or "<none>") for n in nodes)
    role_counter = Counter(str(n.get("role") or "<none>") for n in nodes)

    view_nodes = []
    for nid in selected:
        n = nbi[nid]
        view_nodes.append({
            "id":              nid,
            "label":           str(n.get("label") or nid),
            "file_type":       str(n.get("file_type") or "<none>"),
            "role":            str(n.get("role") or ""),
            "source_file":     str(n.get("source_file") or ""),
            "source_location": str(n.get("source_location") or ""),
            "community":       str(n.get("community") or ""),
            "variant":         variant,
            "degree":          degree.get(nid, 0),
            # extra metadata
            "verify_status":   str(n.get("verify_status") or ""),
            "pass_rate":       n.get("pass_rate", 0),
            "spec_refs":       n.get("spec_refs", 0),
            "port_count":      n.get("port_count", 0),
            "always_kind":     str(n.get("always_kind") or ""),
        })

    summary = {
        "variant":      variant,
        "total_nodes":  len(nodes),
        "total_links":  len(links),
        "view_nodes":   len(view_nodes),
        "view_links":   len(view_links),
        "file_types":   [{"name": k, "count": v} for k, v in ft_counter.most_common(20)],
        "relations":    [{"name": k, "count": v} for k, v in rel_counter.most_common(20)],
        "bridge_links": sum(v for k, v in rel_counter.items() if k in BRIDGE_RELS),
        "hdd_links":    sum(v for k, v in rel_counter.items() if k in HDD_RELS),
        "ast_links":    sum(v for k, v in rel_counter.items() if k in AST_RELS),
    }
    return {"summary": summary, "nodes": view_nodes, "links": view_links}


# ── HTML renderer ─────────────────────────────────────────────────────────────

VARIANT_LABELS = {
    "code-only":         "Code Only",
    "code-ast":          "Code + AST",
    "code-hdd":          "Code + AST + HDD",
    "spec-hdd-code-ast": "Spec + HDD + Code + AST",
}

VARIANT_DESCRIPTIONS = {
    "code-only":         "Graphify code graph — files, symbols, calls, instantiations",
    "code-ast":          "Code graph enriched with tree-sitter AST nodes (ports, params, always blocks, functions)",
    "code-hdd":          "Code + AST + HDD document nodes with verification status",
    "spec-hdd-code-ast": "Full stack: spec documents, HDD docs, code symbols, and AST nodes",
}


def write_html(path: Path, view: dict) -> None:
    payload  = safe_json(view)
    variant  = view["summary"]["variant"]
    title    = f"Graphify — {VARIANT_LABELS.get(variant, variant)}"
    desc     = VARIANT_DESCRIPTIONS.get(variant, "")
    s        = view["summary"]

    colors_js       = json.dumps(COLORS, ensure_ascii=False)
    rel_colors_js   = json.dumps(RELATION_COLORS, ensure_ascii=False)

    nav_links = " | ".join(
        f'<a href="{v}.html" style="color:{"#fff" if v==variant else "#94a3b8"}">'
        f'{VARIANT_LABELS.get(v,v)}</a>'
        for v in ["code-only", "code-ast", "code-hdd", "spec-hdd-code-ast"]
    )

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>
  :root{{--bg:#f7f7f4;--panel:#fff;--ink:#17202a;--muted:#64748b;--line:rgba(23,32,42,.13)}}
  *{{box-sizing:border-box;margin:0;padding:0}}
  html,body{{height:100%;overflow:hidden}}
  body{{font-family:Arial,Helvetica,sans-serif;background:var(--bg);color:var(--ink);display:flex;flex-direction:column}}
  header{{background:#172033;color:#fff;padding:12px 20px;display:flex;flex-direction:column;gap:6px;flex-shrink:0}}
  header h1{{font-size:19px;font-weight:600}}
  .nav{{font-size:12px;opacity:.85}}
  .meta{{display:flex;flex-wrap:wrap;gap:10px;font-size:12px;color:#94a3b8}}
  .shell{{display:grid;grid-template-columns:300px 1fr;flex:1;min-height:0}}
  aside{{overflow-y:auto;background:var(--panel);border-right:1px solid var(--line);padding:12px}}
  main{{position:relative;overflow:hidden}}
  canvas{{position:absolute;top:0;left:0;width:100%;height:100%;background:#fafaf7}}
  h2{{font-size:11px;text-transform:uppercase;color:var(--muted);margin:14px 0 6px;letter-spacing:.04em}}
  h2:first-child{{margin-top:0}}
  input[type=text]{{width:100%;padding:7px 9px;border:1px solid var(--line);border-radius:5px;font-size:13px}}
  label{{display:flex;align-items:center;gap:6px;margin:5px 0;font-size:12px;cursor:pointer}}
  .swatch{{display:inline-block;width:10px;height:10px;border-radius:50%;flex-shrink:0}}
  .row{{display:grid;grid-template-columns:1fr auto;gap:8px;padding:3px 0;font-size:12px}}
  .topnode{{padding:5px 0;border-bottom:1px solid var(--line);font-size:12px;cursor:pointer}}
  .topnode strong{{display:block;font-size:13px}}
  .topnode:hover{{background:#f1f5f9}}
  #tip{{position:absolute;display:none;pointer-events:none;background:#fff;border:1px solid var(--line);
        border-radius:6px;padding:8px 10px;box-shadow:0 6px 18px rgba(0,0,0,.13);max-width:400px;font-size:12px;z-index:10}}
  #detail{{position:absolute;right:12px;top:12px;width:min(460px,calc(100% - 24px));max-height:calc(100% - 24px);
           overflow:auto;background:rgba(255,255,255,.97);border:1px solid var(--line);border-radius:8px;
           padding:12px;display:none;box-shadow:0 8px 26px rgba(0,0,0,.15);z-index:20}}
  #detail h3{{font-size:14px;margin-bottom:6px}}
  #detail pre{{white-space:pre-wrap;word-break:break-word;font-size:11px;color:#334155;max-height:60vh;overflow:auto}}
  #detail button{{margin-top:8px;border:1px solid var(--line);background:#f8fafc;border-radius:4px;
                  padding:4px 8px;cursor:pointer;font-size:12px}}
  .badge{{display:inline-block;padding:2px 6px;border-radius:999px;font-size:11px;font-weight:600}}
  .pass{{background:#dcfce7;color:#15803d}}.fail{{background:#fee2e2;color:#b91c1c}}
  .notrun{{background:#f1f5f9;color:#475569}}
  @media(max-width:780px){{.shell{{grid-template-columns:1fr}}aside{{display:none}}}}
</style>
</head>
<body>
<header>
  <h1>{title}</h1>
  <div class="nav">{nav_links}</div>
  <div class="meta">
    <span>Nodes: {s["total_nodes"]:,}</span>
    <span>Links: {s["total_links"]:,}</span>
    <span>Displayed: {s["view_nodes"]:,} nodes · {s["view_links"]:,} links</span>
    {f'<span>Bridge: {s["bridge_links"]:,}</span>' if s["bridge_links"] else ""}
    {f'<span>AST: {s["ast_links"]:,}</span>' if s.get("ast_links") else ""}
    {f'<span>HDD: {s["hdd_links"]:,}</span>' if s.get("hdd_links") else ""}
  </div>
</header>
<div class="shell">
  <aside>
    <h2>Search</h2>
    <input type="text" id="search" placeholder="label, file, relation …">
    <h2>Node Types</h2>
    <div id="typeFilters"></div>
    <h2>Relations</h2>
    <div id="relFilters"></div>
    <h2>Stats</h2>
    <div id="stats"></div>
    <h2>Top Nodes</h2>
    <div id="topNodes"></div>
  </aside>
  <main>
    <canvas id="g"></canvas>
    <div id="tip"></div>
    <div id="detail"></div>
  </main>
</div>
<script>
const data  = {payload};
const C     = {colors_js};
const RC    = {rel_colors_js};
const nodesById = new Map(data.nodes.map(n => [n.id, n]));
let enabledTypes = new Set(data.nodes.map(n => n.file_type));
let enabledRels  = new Set(data.links.map(e => e.relation));
let search = "", selected = null;
let positions = new Map(), transform = {{x:0,y:0,scale:1}};
const canvas = document.getElementById("g");
const ctx    = canvas.getContext("2d");
const tip    = document.getElementById("tip");
const detail = document.getElementById("detail");

function esc(s){{return String(s??"").replace(/[&<>"]/g,c=>({{
  "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"
}}[c]))}}

function nodeColor(n){{
  if(n.file_type==="hdd_module"){{
    if(n.verify_status==="PASS") return "#16a34a";
    if(n.verify_status==="FAIL") return "#dc2626";
    return "#6b7280";
  }}
  return C[n.file_type]||"#94a3b8";
}}

function visible(n){{
  if(!enabledTypes.has(n.file_type)) return false;
  if(!search) return true;
  return `${{n.label}} ${{n.file_type}} ${{n.role}} ${{n.source_file}} ${{n.community}}`.toLowerCase().includes(search);
}}
function visIds(){{
  const ids = new Set(data.nodes.filter(visible).map(n=>n.id));
  if(search){{
    for(const e of data.links){{
      if(!enabledRels.has(e.relation)) continue;
      if(ids.has(e.source)) ids.add(e.target);
      if(ids.has(e.target)) ids.add(e.source);
    }}
  }}
  return ids;
}}
function layout(){{
  const ids   = visIds();
  const nodes = data.nodes.filter(n=>ids.has(n.id)&&enabledTypes.has(n.file_type));
  const rect  = canvas.getBoundingClientRect();
  const w = Math.max(rect.width,900), h = Math.max(rect.height,680);
  const groups = {{}};
  for(const n of nodes){{(groups[n.file_type]||=[]).push(n);}}
  const keys = Object.keys(groups).sort();
  positions = new Map();
  keys.forEach((key,gi)=>{{
    const cx = w*(0.15+0.7*(gi/Math.max(1,keys.length-1)));
    const cy = h*0.5;
    const arr = groups[key].sort((a,b)=>b.degree-a.degree);
    arr.forEach((n,i)=>{{
      const a  = Math.PI*2*i/Math.max(1,arr.length) - Math.PI/2;
      const r  = 60 + Math.sqrt(i+1)*22;
      positions.set(n.id,{{x:cx+Math.cos(a)*r, y:cy+Math.sin(a)*r}});
    }});
  }});
}}
function sx(x){{return x*transform.scale+transform.x;}}
function sy(y){{return y*transform.scale+transform.y;}}
function nr(n){{return 3+Math.min(16,Math.sqrt(n.degree||1)*0.75);}}
function draw(){{
  ctx.clearRect(0,0,canvas.width/devicePixelRatio,canvas.height/devicePixelRatio);
  const ids = new Set(positions.keys());
  // edges
  for(const e of data.links){{
    if(!enabledRels.has(e.relation)||!ids.has(e.source)||!ids.has(e.target)||e.source===e.target) continue;
    const a=positions.get(e.source), b=positions.get(e.target);
    ctx.beginPath();
    ctx.strokeStyle = RC[e.relation]||"rgba(80,80,80,.15)";
    ctx.lineWidth   = e.relation.startsWith("spec_")||e.relation==="HAS_HDD" ? 1.8 : 0.7;
    ctx.moveTo(sx(a.x),sy(a.y)); ctx.lineTo(sx(b.x),sy(b.y)); ctx.stroke();
  }}
  // nodes
  for(const id of ids){{
    const n=nodesById.get(id), p=positions.get(id), r=nr(n);
    ctx.beginPath();
    ctx.fillStyle = selected===id ? "#000" : nodeColor(n);
    ctx.arc(sx(p.x),sy(p.y),r,0,Math.PI*2); ctx.fill();
    // label for high-degree or when searching
    if(search || n.degree>60 || n.file_type==="hdd_module" || (n.file_type==="document"&&n.degree>30)){{
      ctx.font="11px Arial"; ctx.fillStyle="#17202a";
      ctx.fillText(n.label.slice(0,52), sx(p.x)+r+3, sy(p.y)+4);
    }}
  }}
}}
function relayout(){{layout();draw();}}
function resize(){{
  const main = canvas.parentElement;
  const w = main.clientWidth  || window.innerWidth  - 300;
  const h = main.clientHeight || window.innerHeight - 100;
  const dpr = window.devicePixelRatio || 1;
  canvas.width  = Math.floor(w * dpr);
  canvas.height = Math.floor(h * dpr);
  canvas.style.width  = w + "px";
  canvas.style.height = h + "px";
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  relayout();
}}

function initControls(){{
  // type filters
  const typeCounts = new Map();
  data.nodes.forEach(n=>typeCounts.set(n.file_type,(typeCounts.get(n.file_type)||0)+1));
  for(const [type,count] of [...typeCounts.entries()].sort()){{
    document.getElementById("typeFilters").insertAdjacentHTML("beforeend",
      `<label><input type="checkbox" data-type="${{esc(type)}}" checked>
       <span class="swatch" style="background:${{C[type]||"#94a3b8"}}"></span>
       ${{esc(type)}} (${{count}})</label>`);
  }}
  document.getElementById("typeFilters").addEventListener("change",e=>{{
    const t=e.target.dataset.type; if(!t) return;
    if(e.target.checked) enabledTypes.add(t); else enabledTypes.delete(t);
    relayout();
  }});
  // relation filters
  const relCounts = new Map();
  data.links.forEach(e=>relCounts.set(e.relation,(relCounts.get(e.relation)||0)+1));
  for(const [rel,count] of [...relCounts.entries()].sort((a,b)=>b[1]-a[1]).slice(0,30)){{
    document.getElementById("relFilters").insertAdjacentHTML("beforeend",
      `<label><input type="checkbox" data-rel="${{esc(rel)}}" checked>
       ${{esc(rel)}} (${{count}})</label>`);
  }}
  document.getElementById("relFilters").addEventListener("change",e=>{{
    const r=e.target.dataset.rel; if(!r) return;
    if(e.target.checked) enabledRels.add(r); else enabledRels.delete(r);
    draw();
  }});
  // search
  document.getElementById("search").addEventListener("input",e=>{{
    search=e.target.value.trim().toLowerCase(); relayout();
  }});
  // stats
  document.getElementById("stats").innerHTML=`
    <div class="row"><span>Total nodes</span><strong>${{data.summary.total_nodes.toLocaleString()}}</strong></div>
    <div class="row"><span>Total links</span><strong>${{data.summary.total_links.toLocaleString()}}</strong></div>
    <div class="row"><span>Shown nodes</span><strong>${{data.summary.view_nodes.toLocaleString()}}</strong></div>
    ${{data.summary.bridge_links ? `<div class="row"><span>Bridge links</span><strong>${{data.summary.bridge_links.toLocaleString()}}</strong></div>` : ""}}
    ${{data.summary.ast_links ? `<div class="row"><span>AST links</span><strong>${{data.summary.ast_links.toLocaleString()}}</strong></div>` : ""}}
    ${{data.summary.hdd_links ? `<div class="row"><span>HDD links</span><strong>${{data.summary.hdd_links.toLocaleString()}}</strong></div>` : ""}}
  `;
  // top nodes
  for(const n of [...data.nodes].sort((a,b)=>b.degree-a.degree).slice(0,25)){{
    const d = document.createElement("div");
    d.className="topnode";
    const badge = n.verify_status ? `<span class="badge ${{n.verify_status==="PASS"?"pass":n.verify_status==="FAIL"?"fail":"notrun"}}">${{n.verify_status}}</span>` : "";
    d.innerHTML=`<strong>${{esc(n.label)}}</strong>${{esc(n.file_type)}} · deg ${{n.degree}} ${{badge}}`;
    d.onclick=()=>{{selected=n.id;search=n.label.toLowerCase();document.getElementById("search").value=n.label;showDetail(n);relayout();}};
    document.getElementById("topNodes").appendChild(d);
  }}
}}

function showDetail(n){{
  if(!n){{detail.style.display="none";return;}}
  const related=data.links.filter(e=>e.source===n.id||e.target===n.id).slice(0,60).map(e=>{{
    const other=nodesById.get(e.source===n.id?e.target:e.source);
    return `${{e.relation}} → ${{other?other.label:"?"}}`
  }});
  const extra = n.file_type==="hdd_module" ? `
    verify: ${{n.verify_status}} (${{Math.round(n.pass_rate*100)}}% pass)
    spec_refs: ${{n.spec_refs}}
    ports: ${{n.port_count}}  params: ${{n.param_count}}` :
    n.file_type.startsWith("ast_") ? `
    port_count: ${{n.port_count}}
    always_kind: ${{n.always_kind}}` : "";
  detail.style.display="block";
  detail.innerHTML=`
    <h3>${{esc(n.label)}}</h3>
    <pre>${{esc(JSON.stringify({{type:n.file_type,role:n.role,community:n.community,
      source_file:n.source_file,degree:n.degree}})+extra+"\n\nRelations:\n"+related.join("\n"))}}</pre>
    <button onclick="detail.style.display='none'">Close</button>`;
}}

canvas.addEventListener("mousemove",e=>{{
  const n=hitTest(e),rect=canvas.getBoundingClientRect();
  if(!n){{tip.style.display="none";return;}}
  tip.style.display="block";
  tip.style.left=`${{e.clientX-rect.left+14}}px`;
  tip.style.top=`${{e.clientY-rect.top+14}}px`;
  const badge=n.verify_status?` | ${{n.verify_status}} ${{Math.round(n.pass_rate*100)}}%`:"";
  tip.innerHTML=`<strong>${{esc(n.file_type)}}</strong> ${{esc(n.label)}}<br>deg ${{n.degree}}${{badge}}<br><span style="color:#64748b">${{esc(n.source_file)}}</span>`;
}});
canvas.addEventListener("click",e=>{{const n=hitTest(e);selected=n?.id||null;showDetail(n);draw();}});
canvas.addEventListener("wheel",e=>{{e.preventDefault();transform.scale=Math.max(.1,Math.min(5,transform.scale*(e.deltaY<0?1.09:.92)));draw();}},{{passive:false}});
let drag=null;
canvas.addEventListener("mousedown",e=>{{drag={{x:e.clientX,y:e.clientY,tx:transform.x,ty:transform.y}};}});
window.addEventListener("mouseup",()=>{{drag=null;}});
window.addEventListener("mousemove",e=>{{if(!drag)return;transform.x=drag.tx+e.clientX-drag.x;transform.y=drag.ty+e.clientY-drag.y;draw();}});

function hitTest(e){{
  const rect=canvas.getBoundingClientRect();
  const x=e.clientX-rect.left, y=e.clientY-rect.top;
  for(const [id,p] of positions){{
    const n=nodesById.get(id);
    if(Math.hypot(sx(p.x)-x,sy(p.y)-y)<=nr(n)+4) return n;
  }}
  return null;
}}

initControls();
window.addEventListener("resize", resize);
setTimeout(resize, 0);
</script>
</body>
</html>"""
    path.write_text(html, encoding="utf-8")


def write_index(out_dir: Path, views: list[dict]) -> None:
    cards = []
    for v in views:
        s  = v["summary"]
        vr = s["variant"]
        lb = VARIANT_LABELS.get(vr, vr)
        ds = VARIANT_DESCRIPTIONS.get(vr, "")
        extras = []
        if s.get("bridge_links"): extras.append(f"Bridge: {s['bridge_links']:,}")
        if s.get("ast_links"):    extras.append(f"AST links: {s['ast_links']:,}")
        if s.get("hdd_links"):    extras.append(f"HDD links: {s['hdd_links']:,}")
        extra_str = " · ".join(extras)
        cards.append(f"""
          <a href="{vr}.html">
            <h2>{lb}</h2>
            <p>{ds}</p>
            <div class="stats">{s['total_nodes']:,} nodes · {s['total_links']:,} links
              · {s['view_nodes']:,} displayed{" · " + extra_str if extra_str else ""}</div>
          </a>""")

    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Graphify Graph Views</title>
<style>
  body{{margin:0;font-family:Arial,Helvetica,sans-serif;background:#f7f7f4;color:#17202a}}
  header{{background:#172033;color:#fff;padding:24px 28px}}
  header h1{{font-size:26px;margin:0 0 6px}}
  header p{{color:#94a3b8;font-size:14px;margin:0}}
  main{{max-width:1060px;margin:0 auto;padding:32px 22px}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin-top:24px}}
  a{{display:block;text-decoration:none;color:#17202a;background:#fff;border:1px solid rgba(0,0,0,.11);
     border-radius:10px;padding:20px;transition:box-shadow .15s}}
  a:hover{{box-shadow:0 4px 18px rgba(0,0,0,.10)}}
  h2{{margin:0 0 8px;font-size:17px}}
  p{{color:#475569;font-size:13px;line-height:1.5;margin:0 0 10px}}
  .stats{{font-size:12px;color:#94a3b8}}
</style></head><body>
<header>
  <h1>Graphify Graph Views</h1>
  <p>Four graph variants — code, AST, HDD, and spec — in interactive HTML</p>
</header>
<main>
  <div class="grid">{''.join(cards)}</div>
</main></body></html>"""
    (out_dir / "index.html").write_text(html, encoding="utf-8")


# ── main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir",   type=Path, default=ROOT / "out/graph-views")
    ap.add_argument("--max-nodes", type=int,  default=2000)
    args = ap.parse_args()

    out_dir = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    variants: list[tuple[str, dict]] = []

    print("[1/4] code-only …")
    variants.append(("code-only", rj(CODE_ONLY_GRAPH)))

    print("[2/4] code-ast …")
    code_ast = load_code_ast()
    variants.append(("code-ast", code_ast))

    print("[3/4] code-hdd …")
    code_hdd = build_code_hdd(code_ast)
    variants.append(("code-hdd", code_hdd))

    print("[4/4] spec-hdd-code-ast …")
    full = build_spec_hdd_code_ast(code_hdd)
    variants.append(("spec-hdd-code-ast", full))

    views = []
    for name, graph in variants:
        print(f"  rendering {name} ({len(graph['nodes'])} nodes) …")
        view = build_view(name, graph, args.max_nodes)
        write_html(out_dir / f"{name}.html", view)
        views.append(view)

    write_index(out_dir, views)

    print(json.dumps({
        "status":  "ok",
        "out_dir": str(out_dir),
        "views": [{
            "variant":     v["summary"]["variant"],
            "total_nodes": v["summary"]["total_nodes"],
            "total_links": v["summary"]["total_links"],
            "view_nodes":  v["summary"]["view_nodes"],
            "view_links":  v["summary"]["view_links"],
        } for v in views],
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
