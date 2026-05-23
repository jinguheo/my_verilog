#!/usr/bin/env python3
"""Render connections only visible when spec-only, HDD, and code-ast are integrated."""

from __future__ import annotations

import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
GRAPH_PATH = ROOT / "dbs" / "graphify-out" / "spec-hdd-code-ast-graphify" / "graph.json"
OUT_DIR = ROOT / "dbs" / "graphify-out" / "code-ast-hdd-spec-bridge"
SPEC_BRIDGE_RELATIONS = {"spec_component_matches_code", "spec_path_matches_code_path"}
AST_RELATIONS = {"ast_has_port", "ast_has_param", "ast_has_always", "ast_has_fn"}


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def esc(value: Any) -> str:
    return html.escape(str(value or ""), quote=True)


def safe_json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")


def relation(edge: dict[str, Any]) -> str:
    return str(edge.get("relation") or edge.get("type") or "related")


def edge_source(edge: dict[str, Any]) -> str:
    return str(edge.get("source") or edge.get("_src") or "")


def edge_target(edge: dict[str, Any]) -> str:
    return str(edge.get("target") or edge.get("_tgt") or "")


def norm_path(value: str) -> str:
    value = str(value or "").replace("/", "\\").lower()
    if value.startswith("dbs\\"):
        value = value[4:]
    return value


def path_parts(value: str) -> list[str]:
    return [part for part in re.split(r"[\\/]+", str(value or "")) if part]


def component_key(node: dict[str, Any]) -> str:
    label = str(node.get("label") or "")
    if label.startswith("component:"):
        return label.split(":", 1)[1]
    parts = path_parts(str(node.get("source_file") or ""))
    if parts and parts[0] == "dbs":
        parts = parts[1:]
    for marker in ("ip_autogen", "ip"):
        if marker in parts:
            idx = parts.index(marker)
            if idx + 1 < len(parts):
                return parts[idx + 1]
    for part in parts:
        if re.search(r"ibex|rstmgr|otp|ctrl|mgr|handler|prim|core|stage|decoder|alu|lsu|csr|icache|controller", part):
            return part
    return "unknown"


def line_number(source_location: str) -> int | None:
    match = re.search(r"L(\d+)", str(source_location or ""))
    return int(match.group(1)) if match else None


def resolve_path(source_file: str) -> Path | None:
    candidates = []
    source_file = str(source_file or "")
    if not source_file:
        return None
    p = Path(source_file)
    if p.is_absolute():
        candidates.append(p)
    candidates.append(ROOT / source_file.replace("/", "\\"))
    if source_file.startswith("dbs\\") or source_file.startswith("dbs/"):
        candidates.append(ROOT / source_file.replace("/", "\\"))
    else:
        candidates.append(ROOT / "dbs" / source_file.replace("/", "\\"))
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def snippet(path: Path | None, line: int | None, radius: int = 6) -> str:
    if path is None or line is None:
        return ""
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return ""
    start = max(1, line - radius)
    end = min(len(lines), line + radius)
    out = []
    for idx in range(start, end + 1):
        marker = ">" if idx == line else " "
        out.append(f"{marker} {idx:5d}: {lines[idx - 1]}")
    return "\n".join(out)


def compact(node: dict[str, Any]) -> dict[str, Any]:
    out = {
        "id": str(node.get("id") or ""),
        "label": str(node.get("label") or ""),
        "file_type": str(node.get("file_type") or ""),
        "role": str(node.get("role") or ""),
        "source_file": str(node.get("source_file") or ""),
        "source_location": str(node.get("source_location") or ""),
        "community": str(node.get("community") or ""),
    }
    for key in (
        "direction",
        "dtype",
        "width",
        "default",
        "module",
        "always_kind",
        "lhs_signals",
        "return_type",
        "port_count",
        "param_count",
        "always_count",
        "fn_count",
        "parse_errors",
        "verify_status",
        "pass_rate",
        "spec_refs",
    ):
        if key in node:
            out[key] = node[key]
    return out


def add_unique(rows: list[dict[str, Any]], row: dict[str, Any], limit: int = 80) -> None:
    key = (row.get("id"), row.get("label"), row.get("source_file"), row.get("source_location"))
    seen = {(r.get("id"), r.get("label"), r.get("source_file"), r.get("source_location")) for r in rows}
    if key not in seen and len(rows) < limit:
        rows.append(row)


def build_view() -> dict[str, Any]:
    graph = read_json(GRAPH_PATH)
    nodes = {str(node["id"]): node for node in graph.get("nodes", [])}
    links = graph.get("links", graph.get("edges", []))

    hdd_nodes = {node_id: node for node_id, node in nodes.items() if node.get("file_type") == "hdd_module"}
    ast_to_hdd: dict[str, str] = {}
    hdd_to_ast: dict[str, str] = {}
    ast_children: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    spec_edges = []
    relation_counts = Counter()

    for edge in links:
        rel = relation(edge)
        relation_counts[rel] += 1
        src, tgt = edge_source(edge), edge_target(edge)
        src_node, tgt_node = nodes.get(src), nodes.get(tgt)
        if not src_node or not tgt_node:
            continue
        if rel == "HAS_HDD":
            ast = src_node if src_node.get("file_type") == "ast_module" else tgt_node if tgt_node.get("file_type") == "ast_module" else None
            hdd = src_node if src_node.get("file_type") == "hdd_module" else tgt_node if tgt_node.get("file_type") == "hdd_module" else None
            if ast and hdd:
                ast_to_hdd[str(ast["id"])] = str(hdd["id"])
                hdd_to_ast[str(hdd["id"])] = str(ast["id"])
        elif rel in AST_RELATIONS:
            if src_node.get("file_type") == "ast_module":
                ast_children[src][rel].append(compact(tgt_node))
            elif tgt_node.get("file_type") == "ast_module":
                ast_children[tgt][rel].append(compact(src_node))
        elif rel in SPEC_BRIDGE_RELATIONS:
            if src_node.get("file_type") == "document" and tgt_node.get("file_type") != "document":
                spec_edges.append((rel, src_node, tgt_node))
            elif tgt_node.get("file_type") == "document" and src_node.get("file_type") != "document":
                spec_edges.append((rel, tgt_node, src_node))

    hdd_by_path: dict[str, list[str]] = defaultdict(list)
    hdd_by_label: dict[str, list[str]] = defaultdict(list)
    hdd_by_component: dict[str, list[str]] = defaultdict(list)
    for hdd_id, hdd in hdd_nodes.items():
        hdd_by_path[norm_path(str(hdd.get("source_file") or ""))].append(hdd_id)
        hdd_by_label[str(hdd.get("label") or "").lower()].append(hdd_id)
        hdd_by_component[component_key(hdd)].append(hdd_id)

    records: dict[str, dict[str, Any]] = {}
    match_counts = Counter()
    for rel, spec, code in spec_edges:
        candidates: list[str] = []
        code_path = norm_path(str(code.get("source_file") or ""))
        code_label = str(code.get("label") or "").lower().replace(".sv", "")
        comp = component_key(code)
        if code_path in hdd_by_path:
            candidates.extend(hdd_by_path[code_path])
            match_counts["same_source_file"] += 1
        if code_label in hdd_by_label:
            candidates.extend(hdd_by_label[code_label])
            match_counts["same_label"] += 1
        if comp in hdd_by_component:
            candidates.extend(hdd_by_component[comp][:5])
            match_counts["same_component"] += 1
        for hdd_id in dict.fromkeys(candidates):
            hdd = hdd_nodes[hdd_id]
            ast_id = hdd_to_ast.get(hdd_id)
            if not ast_id:
                continue
            ast = nodes.get(ast_id, {})
            record = records.setdefault(
                hdd_id,
                {
                    "hdd": compact(hdd),
                    "ast": compact(ast),
                    "component": component_key(hdd),
                    "spec_anchors": [],
                    "code_bridge_nodes": [],
                    "relations": Counter(),
                    "ports": [],
                    "params": [],
                    "always_blocks": [],
                    "functions": [],
                },
            )
            record["relations"][rel] += 1
            add_unique(record["spec_anchors"], compact(spec), 120)
            add_unique(record["code_bridge_nodes"], compact(code), 80)

    for hdd_id, record in records.items():
        ast_id = hdd_to_ast.get(hdd_id)
        record["ports"] = ast_children[ast_id].get("ast_has_port", [])[:80]
        record["params"] = ast_children[ast_id].get("ast_has_param", [])[:60]
        record["always_blocks"] = ast_children[ast_id].get("ast_has_always", [])[:60]
        record["functions"] = ast_children[ast_id].get("ast_has_fn", [])[:60]
        source_path = resolve_path(record["ast"].get("source_file", ""))
        record["source_path"] = str(source_path or "")
        record["snippet"] = snippet(source_path, line_number(record["ast"].get("source_location", "")), 8)
        record["score"] = (
            len(record["spec_anchors"]) * 3
            + len(record["code_bridge_nodes"]) * 2
            + len(record["ports"])
            + len(record["params"])
            + len(record["always_blocks"])
            + len(record["functions"])
        )
        record["relations"] = dict(record["relations"])

    items = sorted(records.values(), key=lambda r: (-r["score"], r["hdd"]["label"]))[:240]
    summary = {
        "source_graph": str(GRAPH_PATH),
        "integrated_records": len(items),
        "all_hdd_modules": len(hdd_nodes),
        "has_hdd_edges": len(hdd_to_ast),
        "spec_bridge_edges": len(spec_edges),
        "match_counts": match_counts.most_common(),
        "relations": relation_counts.most_common(30),
        "total_spec_anchors": sum(len(item["spec_anchors"]) for item in items),
        "total_code_bridge_nodes": sum(len(item["code_bridge_nodes"]) for item in items),
        "total_ports": sum(len(item["ports"]) for item in items),
        "total_params": sum(len(item["params"]) for item in items),
        "total_always": sum(len(item["always_blocks"]) for item in items),
        "total_functions": sum(len(item["functions"]) for item in items),
    }
    return {"summary": summary, "records": items}


def write_markdown(path: Path, data: dict[str, Any]) -> None:
    lines = [
        "# Code-AST + HDD + Spec-Only Bridge",
        "",
        "This report lists information that is not visible from code-ast-only or spec-only alone. Each row connects spec anchors to HDD modules and then to AST internals such as ports, params, always blocks, and functions.",
        "",
        f"- Integrated records: {data['summary']['integrated_records']}",
        f"- Spec bridge edges considered: {data['summary']['spec_bridge_edges']}",
        f"- HAS_HDD edges: {data['summary']['has_hdd_edges']}",
        "",
        "## Top Integrated Modules",
        "",
        "| HDD / AST module | Component | Spec anchors | Code bridge nodes | Ports | Params | Always | Functions |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for record in data["records"][:120]:
        lines.append(
            f"| `{record['hdd']['label']}` | `{record['component']}` | {len(record['spec_anchors'])} | "
            f"{len(record['code_bridge_nodes'])} | {len(record['ports'])} | {len(record['params'])} | "
            f"{len(record['always_blocks'])} | {len(record['functions'])} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_html(path: Path, data: dict[str, Any]) -> None:
    payload = safe_json(data)
    html_text = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Code-AST HDD Spec Bridge</title>
<style>
:root{--bg:#f6f7f9;--panel:#fff;--ink:#17202a;--muted:#667085;--line:#d7dde7;--spec:#2f6fed;--hdd:#b7791f;--ast:#16875f}
*{box-sizing:border-box}body{margin:0;font-family:Arial,Helvetica,sans-serif;background:var(--bg);color:var(--ink)}
header{padding:16px 20px 12px;background:var(--panel);border-bottom:1px solid var(--line)}
h1{margin:0 0 7px;font-size:23px}.meta{display:flex;gap:12px;flex-wrap:wrap;color:var(--muted);font-size:13px}
.shell{display:grid;grid-template-columns:430px 1fr;height:calc(100vh - 76px);min-height:760px}
aside{overflow:auto;background:var(--panel);border-right:1px solid var(--line);padding:14px}
main{overflow:auto;padding:18px 24px 48px}
input{width:100%;padding:8px;border:1px solid var(--line);border-radius:6px;background:#fff;margin-bottom:8px}
h2{font-size:13px;text-transform:uppercase;color:var(--muted);margin:16px 0 8px}h3{font-size:20px;margin:0 0 8px}
.rec{border-bottom:1px solid var(--line);padding:8px 4px;cursor:pointer}.rec:hover{background:#f1f5f9}.rec strong{display:block;font-size:13px}.rec span{display:block;color:var(--muted);font-size:12px;line-height:1.35}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(175px,1fr));gap:10px;margin:10px 0 18px}.metric{background:#fff;border:1px solid var(--line);border-radius:8px;padding:12px}.metric strong{display:block;font-size:24px}
.card{background:#fff;border:1px solid var(--line);border-radius:8px;padding:14px;margin:12px 0}pre{white-space:pre-wrap;word-break:break-word;background:#0f172a;color:#dbeafe;border-radius:8px;padding:10px;font-size:12px;line-height:1.35;max-height:300px;overflow:auto}
table{width:100%;border-collapse:collapse;background:#fff;border:1px solid var(--line);border-radius:8px;overflow:hidden;margin-bottom:12px}th,td{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;font-size:13px;vertical-align:top}th{background:#eef2f7}
.pill{display:inline-block;border:1px solid var(--line);border-radius:999px;padding:3px 8px;margin:2px;font-size:12px;background:#fff}.muted{color:var(--muted)}code{background:#eef2f7;padding:2px 4px;border-radius:4px}.path{font-size:12px;color:var(--muted)}
.legend span{display:inline-block;margin-right:10px}.dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:5px}.spec{background:var(--spec)}.hdd{background:var(--hdd)}.ast{background:var(--ast)}
@media(max-width:960px){.shell{grid-template-columns:1fr;height:auto}aside{max-height:500px}main{padding:16px}}
</style>
</head>
<body>
<header><h1>Code-AST + HDD + Spec-Only Bridge</h1><div class="meta" id="meta"></div></header>
<div class="shell">
<aside>
  <input id="q" placeholder="Search module, spec, port, param, signal, file">
  <div class="legend"><span><i class="dot spec"></i>Spec anchor</span><span><i class="dot hdd"></i>HDD module</span><span><i class="dot ast"></i>AST internals</span></div>
  <h2>Integrated Records</h2>
  <div id="list"></div>
</aside>
<main id="content"></main>
</div>
<script>
const data=__DATA__;
const q=document.getElementById('q'), list=document.getElementById('list'), content=document.getElementById('content');
function esc(s){return String(s??'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}
function arrText(rows, keys){return rows.map(r=>keys.map(k=>Array.isArray(r[k])?r[k].join(' '):r[k]).join(' ')).join(' ')}
function textOf(r){return [r.hdd.label,r.ast.label,r.component,r.hdd.source_file,r.ast.source_file,arrText(r.spec_anchors,['label','source_file']),arrText(r.code_bridge_nodes,['label','source_file']),arrText(r.ports,['label','direction','dtype','width']),arrText(r.params,['label','dtype','default']),arrText(r.always_blocks,['label','always_kind','lhs_signals']),arrText(r.functions,['label','return_type'])].join(' ').toLowerCase()}
document.getElementById('meta').innerHTML=`<span>Integrated records: ${data.summary.integrated_records}</span><span>Spec anchors: ${data.summary.total_spec_anchors}</span><span>Code bridge nodes: ${data.summary.total_code_bridge_nodes}</span><span>AST ports: ${data.summary.total_ports}</span><span>AST params: ${data.summary.total_params}</span>`;
function filtered(){const term=q.value.trim().toLowerCase();return data.records.filter(r=>!term||textOf(r).includes(term)).sort((a,b)=>b.score-a.score||a.hdd.label.localeCompare(b.hdd.label))}
function renderList(){const rows=filtered().slice(0,500);list.innerHTML=rows.map(r=>`<div class="rec" data-i="${data.records.indexOf(r)}"><strong>${esc(r.hdd.label)}</strong><span>${esc(r.component)} · spec ${r.spec_anchors.length} · code ${r.code_bridge_nodes.length} · ports ${r.ports.length} · params ${r.params.length} · always ${r.always_blocks.length}</span><span>${esc(r.hdd.source_file)}</span></div>`).join('')||'<p class="muted">No matches</p>'}
function table(headers, rows, render){if(!rows.length)return '<p class="muted">None</p>';return `<table><thead><tr>${headers.map(h=>`<th>${h}</th>`).join('')}</tr></thead><tbody>${rows.map(render).join('')}</tbody></table>`}
function renderPage(r){
 const spec=table(['Spec anchor','Location'],r.spec_anchors.slice(0,80),x=>`<tr><td><code>${esc(x.label)}</code></td><td><span class="path">${esc(x.source_file)} ${esc(x.source_location)}</span></td></tr>`);
 const code=table(['Code bridge node','Location'],r.code_bridge_nodes.slice(0,60),x=>`<tr><td><code>${esc(x.label)}</code></td><td><span class="path">${esc(x.source_file)} ${esc(x.source_location)}</span></td></tr>`);
 const ports=table(['Port','Dir','Type','Width'],r.ports,x=>`<tr><td><code>${esc(x.label)}</code></td><td>${esc(x.direction)}</td><td>${esc(x.dtype)}</td><td>${esc(x.width)}</td></tr>`);
 const params=table(['Param','Type','Default'],r.params,x=>`<tr><td><code>${esc(x.label)}</code></td><td>${esc(x.dtype)}</td><td>${esc(x.default)}</td></tr>`);
 const always=table(['Always','Kind','LHS / assigned signals'],r.always_blocks,x=>`<tr><td><code>${esc(x.label)}</code></td><td>${esc(x.always_kind)}</td><td>${esc((x.lhs_signals||[]).join(', '))}</td></tr>`);
 const fns=table(['Function','Return type'],r.functions,x=>`<tr><td><code>${esc(x.label)}</code></td><td>${esc(x.return_type)}</td></tr>`);
 content.innerHTML=`<h3>${esc(r.hdd.label)}</h3><p class="muted">${esc(r.hdd.source_file)}</p><div class="grid"><div class="metric">Spec anchors<strong>${r.spec_anchors.length}</strong></div><div class="metric">Code bridge nodes<strong>${r.code_bridge_nodes.length}</strong></div><div class="metric">Ports<strong>${r.ports.length}</strong></div><div class="metric">Params<strong>${r.params.length}</strong></div><div class="metric">Always<strong>${r.always_blocks.length}</strong></div><div class="metric">Functions<strong>${r.functions.length}</strong></div></div><div class="card"><h2>Why this is integrated-only</h2><p>Spec-only can show the spec anchors below. Code-AST-only can show the module internals below. This page shows the missing connection: <code>Spec anchor -> code bridge node -> HDD module -> AST ports/params/always/functions</code>.</p><span class="pill">verify_status: ${esc(r.hdd.verify_status)}</span><span class="pill">pass_rate: ${esc(r.hdd.pass_rate)}</span><span class="pill">spec_refs: ${esc(r.hdd.spec_refs)}</span></div><div class="card"><h2>Source Snippet</h2>${r.snippet?`<pre>${esc(r.snippet)}</pre>`:'<p class="muted">No source snippet found.</p>'}</div><div class="card"><h2>Spec Anchors</h2>${spec}<h2>Code Bridge Nodes</h2>${code}<h2>AST Ports</h2>${ports}<h2>AST Parameters</h2>${params}<h2>AST Always Blocks</h2>${always}<h2>AST Functions</h2>${fns}</div>`;
}
list.addEventListener('click',e=>{const item=e.target.closest('.rec');if(!item)return;renderPage(data.records[Number(item.dataset.i)])});
q.addEventListener('input',renderList);
content.innerHTML=`<h3>Integrated-only information</h3><p>This view removes ordinary community browsing and focuses on what becomes visible only when code-ast, HDD, and spec-only data are connected.</p><div class="grid"><div class="metric">Records<strong>${data.summary.integrated_records}</strong></div><div class="metric">Spec anchors<strong>${data.summary.total_spec_anchors}</strong></div><div class="metric">Code bridge nodes<strong>${data.summary.total_code_bridge_nodes}</strong></div><div class="metric">AST internals<strong>${data.summary.total_ports+data.summary.total_params+data.summary.total_always+data.summary.total_functions}</strong></div></div><p class="muted">Search for ibex_top, cs_registers, bus, compressed_decoder, clk_i, rst_ni, PMP, or a spec document name.</p>`;
renderList();
</script>
</body>
</html>"""
    path.write_text(html_text.replace("__DATA__", payload), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    data = build_view()
    (OUT_DIR / "code_ast_hdd_spec_bridge.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_markdown(OUT_DIR / "index.md", data)
    write_html(OUT_DIR / "index.html", data)
    print(
        json.dumps(
            {
                "status": "ok",
                "out_dir": str(OUT_DIR),
                "html": str(OUT_DIR / "index.html"),
                "json": str(OUT_DIR / "code_ast_hdd_spec_bridge.json"),
                "markdown": str(OUT_DIR / "index.md"),
                "summary": data["summary"],
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
