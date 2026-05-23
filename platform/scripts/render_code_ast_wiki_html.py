#!/usr/bin/env python3
"""Render a wiki-style browser view for the Graphify code-ast graph."""

from __future__ import annotations

import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
GRAPH_PATH = ROOT / "dbs" / "graphify-out" / "code-ast-graphify" / "graph.json"
OUT_DIR = ROOT / "dbs" / "graphify-out" / "code-ast-wiki"

AST_RELATIONS = {"has_ast", "ast_has_port", "ast_has_param", "ast_has_always", "ast_has_fn"}


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


def line_number(source_location: str) -> int | None:
    match = re.search(r"L(\d+)", str(source_location or ""))
    return int(match.group(1)) if match else None


def resolve_path(source_file: str) -> Path | None:
    source_file = str(source_file or "")
    if not source_file:
        return None
    candidates = []
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


def snippet(path: Path | None, line: int | None, radius: int = 8) -> str:
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


def project_from_path(source_file: str) -> str:
    parts = re.split(r"[\\/]+", str(source_file or ""))
    if parts and parts[0] == "dbs" and len(parts) > 1:
        return parts[1]
    return parts[0] if parts and parts[0] else "unknown"


def code_kind(source_file: str, label: str) -> str:
    source = str(source_file or "").lower()
    label = str(label or "").lower()
    if "\\dv\\" in source or "/dv/" in source:
        if "sva" in source or "assert" in label:
            return "dv/sva"
        if "formal" in source or "\\fpv\\" in source or "/fpv/" in source:
            return "dv/formal"
        return "dv"
    if "\\rtl\\" in source or "/rtl/" in source:
        return "rtl"
    if "test" in source or "tb" in label:
        return "testbench"
    return "other"


def compact(node: dict[str, Any]) -> dict[str, Any]:
    out = {
        "id": str(node.get("id") or ""),
        "label": str(node.get("label") or ""),
        "file_type": str(node.get("file_type") or ""),
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
    ):
        if key in node:
            out[key] = node[key]
    return out


def sort_by_label(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(rows, key=lambda row: (str(row.get("source_location") or ""), str(row.get("label") or "")))


def build_wiki() -> dict[str, Any]:
    graph = read_json(GRAPH_PATH)
    nodes = {str(node["id"]): node for node in graph.get("nodes", [])}
    links = graph.get("links", graph.get("edges", []))

    children: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    code_parent: dict[str, dict[str, Any]] = {}
    relation_counts = Counter()
    for edge in links:
        rel = relation(edge)
        if rel not in AST_RELATIONS:
            continue
        relation_counts[rel] += 1
        src, tgt = edge_source(edge), edge_target(edge)
        src_node, tgt_node = nodes.get(src), nodes.get(tgt)
        if not src_node or not tgt_node:
            continue
        if rel == "has_ast":
            if tgt_node.get("file_type") == "ast_module":
                code_parent[tgt] = compact(src_node)
            elif src_node.get("file_type") == "ast_module":
                code_parent[src] = compact(tgt_node)
            continue
        if src_node.get("file_type") == "ast_module":
            module_id = src
            child = tgt_node
        elif tgt_node.get("file_type") == "ast_module":
            module_id = tgt
            child = src_node
        else:
            continue
        children[module_id][rel].append(compact(child))

    modules = []
    for module_node in nodes.values():
        if module_node.get("file_type") != "ast_module":
            continue
        module = compact(module_node)
        source_file = module["source_file"]
        lno = line_number(module["source_location"])
        source_path = resolve_path(source_file)
        module["project"] = project_from_path(source_file)
        module["kind"] = code_kind(source_file, module["label"])
        module["source_path"] = str(source_path or "")
        module["snippet"] = snippet(source_path, lno, 10)
        module["code_parent"] = code_parent.get(module["id"], {})
        module["ports"] = sort_by_label(children[module["id"]].get("ast_has_port", []))
        module["params"] = sort_by_label(children[module["id"]].get("ast_has_param", []))
        module["always_blocks"] = sort_by_label(children[module["id"]].get("ast_has_always", []))
        module["functions"] = sort_by_label(children[module["id"]].get("ast_has_fn", []))
        modules.append(module)

    modules.sort(
        key=lambda item: (
            -int(item.get("port_count") or 0),
            -int(item.get("param_count") or 0),
            item["source_file"],
            item["label"],
        )
    )
    type_counts = Counter(str(node.get("file_type") or "<none>") for node in nodes.values())
    project_counts = Counter(module["project"] for module in modules)
    kind_counts = Counter(module["kind"] for module in modules)
    parse_counts = Counter("parse_errors" if module.get("parse_errors") else "ok" for module in modules)
    summary = {
        "source_graph": str(GRAPH_PATH),
        "nodes": len(nodes),
        "links": len(links),
        "modules": len(modules),
        "ports": sum(len(module["ports"]) for module in modules),
        "params": sum(len(module["params"]) for module in modules),
        "always_blocks": sum(len(module["always_blocks"]) for module in modules),
        "functions": sum(len(module["functions"]) for module in modules),
        "file_types": type_counts.most_common(),
        "projects": project_counts.most_common(),
        "kinds": kind_counts.most_common(),
        "parse_status": parse_counts.most_common(),
        "ast_relations": relation_counts.most_common(),
    }
    return {"summary": summary, "modules": modules}


def write_markdown(path: Path, data: dict[str, Any]) -> None:
    lines = [
        "# Code-AST Wiki",
        "",
        "This wiki is generated from the Graphify code-ast graph. It shows module-level AST details instead of community-level clusters.",
        "",
        f"- Modules: {data['summary']['modules']}",
        f"- Ports: {data['summary']['ports']}",
        f"- Params: {data['summary']['params']}",
        f"- Always blocks: {data['summary']['always_blocks']}",
        f"- Functions: {data['summary']['functions']}",
        "",
        "## Module Kinds",
        "",
        "| Kind | Count |",
        "|---|---:|",
    ]
    for kind, count in data["summary"]["kinds"]:
        lines.append(f"| `{kind}` | {count} |")
    lines += [
        "",
        "## Top Modules By Interface Size",
        "",
        "| Module | Project | Kind | Ports | Params | Always | Functions | File |",
        "|---|---|---|---:|---:|---:|---:|---|",
    ]
    for module in data["modules"][:120]:
        lines.append(
            f"| `{module['label']}` | `{module['project']}` | `{module['kind']}` | "
            f"{len(module['ports'])} | {len(module['params'])} | {len(module['always_blocks'])} | "
            f"{len(module['functions'])} | `{module['source_file']}` |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_html(path: Path, data: dict[str, Any]) -> None:
    payload = safe_json(data)
    html_text = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Code-AST Wiki</title>
<style>
:root{--bg:#f6f7f9;--panel:#fff;--ink:#17202a;--muted:#667085;--line:#d7dde7;--green:#16875f;--blue:#2f6fed;--amber:#b7791f}
*{box-sizing:border-box}body{margin:0;font-family:Arial,Helvetica,sans-serif;background:var(--bg);color:var(--ink)}
header{padding:16px 20px 12px;background:var(--panel);border-bottom:1px solid var(--line)}
h1{margin:0 0 7px;font-size:23px}.meta{display:flex;gap:12px;flex-wrap:wrap;color:var(--muted);font-size:13px}
.shell{display:grid;grid-template-columns:410px 1fr;height:calc(100vh - 76px);min-height:740px}
aside{overflow:auto;background:var(--panel);border-right:1px solid var(--line);padding:14px}
main{overflow:auto;padding:18px 24px 48px}
input,select{width:100%;padding:8px;border:1px solid var(--line);border-radius:6px;background:#fff;margin-bottom:8px}
h2{font-size:13px;text-transform:uppercase;color:var(--muted);margin:16px 0 8px}h3{font-size:20px;margin:0 0 8px}
.mod{border-bottom:1px solid var(--line);padding:8px 4px;cursor:pointer}.mod:hover{background:#f1f5f9}.mod strong{display:block;font-size:13px}.mod span{display:block;color:var(--muted);font-size:12px;line-height:1.35}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(175px,1fr));gap:10px;margin:10px 0 18px}.metric{background:#fff;border:1px solid var(--line);border-radius:8px;padding:12px}.metric strong{display:block;font-size:24px}
.card{background:#fff;border:1px solid var(--line);border-radius:8px;padding:14px;margin:12px 0}pre{white-space:pre-wrap;word-break:break-word;background:#0f172a;color:#dbeafe;border-radius:8px;padding:10px;font-size:12px;line-height:1.35;max-height:320px;overflow:auto}
table{width:100%;border-collapse:collapse;background:#fff;border:1px solid var(--line);border-radius:8px;overflow:hidden;margin-bottom:12px}th,td{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;font-size:13px;vertical-align:top}th{background:#eef2f7}
.pill{display:inline-block;border:1px solid var(--line);border-radius:999px;padding:3px 8px;margin:2px;font-size:12px;background:#fff}.warn{color:#b42318;font-weight:700}.muted{color:var(--muted)}
code{background:#eef2f7;padding:2px 4px;border-radius:4px}
@media(max-width:940px){.shell{grid-template-columns:1fr;height:auto}aside{max-height:480px}main{padding:16px}}
</style>
</head>
<body>
<header><h1>Code-AST Wiki</h1><div class="meta" id="meta"></div></header>
<div class="shell">
<aside>
  <input id="q" placeholder="Search module, port, param, signal, file">
  <select id="kind"></select>
  <select id="project"></select>
  <h2>Modules</h2>
  <div id="list"></div>
</aside>
<main id="content"></main>
</div>
<script>
const data=__DATA__;
const q=document.getElementById('q'), kind=document.getElementById('kind'), project=document.getElementById('project'), list=document.getElementById('list'), content=document.getElementById('content');
function esc(s){return String(s??'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}
function arrText(rows, keys){return rows.map(r=>keys.map(k=>Array.isArray(r[k])?r[k].join(' '):r[k]).join(' ')).join(' ')}
function textOf(m){return [m.label,m.source_file,m.project,m.kind,arrText(m.ports,['label','direction','dtype','width']),arrText(m.params,['label','dtype','default']),arrText(m.always_blocks,['label','always_kind','lhs_signals']),arrText(m.functions,['label','return_type'])].join(' ').toLowerCase()}
document.getElementById('meta').innerHTML=`<span>Modules: ${data.summary.modules}</span><span>Ports: ${data.summary.ports}</span><span>Params: ${data.summary.params}</span><span>Always: ${data.summary.always_blocks}</span><span>Functions: ${data.summary.functions}</span>`;
function fillSelect(el,label,values){el.innerHTML=`<option value="">${label}: all</option>`+values.map(v=>`<option value="${esc(v)}">${esc(v)}</option>`).join('')}
fillSelect(kind,'Kind',[...new Set(data.modules.map(m=>m.kind))].sort());
fillSelect(project,'Project',[...new Set(data.modules.map(m=>m.project))].sort());
function filtered(){const term=q.value.trim().toLowerCase();return data.modules.filter(m=>(!kind.value||m.kind===kind.value)&&(!project.value||m.project===project.value)&&(!term||textOf(m).includes(term))).sort((a,b)=>(b.ports.length-a.ports.length)||(b.params.length-a.params.length)||a.label.localeCompare(b.label))}
function renderList(){const rows=filtered().slice(0,500);list.innerHTML=rows.map(m=>`<div class="mod" data-i="${data.modules.indexOf(m)}"><strong>${esc(m.label)} ${m.parse_errors?'<span class="warn">parse warning</span>':''}</strong><span>${esc(m.project)} · ${esc(m.kind)} · ports ${m.ports.length} · params ${m.params.length} · always ${m.always_blocks.length} · fn ${m.functions.length}</span><span>${esc(m.source_file)}</span></div>`).join('')||'<p class="muted">No matches</p>'}
function table(headers, rows, render){if(!rows.length)return '<p class="muted">None</p>';return `<table><thead><tr>${headers.map(h=>`<th>${h}</th>`).join('')}</tr></thead><tbody>${rows.map(render).join('')}</tbody></table>`}
function renderPage(m){
 const ports=table(['Name','Dir','Type','Width'],m.ports,r=>`<tr><td><code>${esc(r.label)}</code></td><td>${esc(r.direction)}</td><td>${esc(r.dtype)}</td><td>${esc(r.width)}</td></tr>`);
 const params=table(['Name','Type','Default'],m.params,r=>`<tr><td><code>${esc(r.label)}</code></td><td>${esc(r.dtype)}</td><td>${esc(r.default)}</td></tr>`);
 const always=table(['Block','Kind','Assigned/LHS signals'],m.always_blocks,r=>`<tr><td><code>${esc(r.label)}</code></td><td>${esc(r.always_kind)}</td><td>${esc((r.lhs_signals||[]).join(', '))}</td></tr>`);
 const fns=table(['Function','Return type'],m.functions,r=>`<tr><td><code>${esc(r.label)}</code></td><td>${esc(r.return_type)}</td></tr>`);
 content.innerHTML=`<h3>${esc(m.label)} ${m.parse_errors?'<span class="warn">parse warning</span>':''}</h3><p class="muted">${esc(m.source_file)} ${esc(m.source_location)}<br>${esc(m.source_path)}</p><div class="grid"><div class="metric">Ports<strong>${m.ports.length}</strong></div><div class="metric">Params<strong>${m.params.length}</strong></div><div class="metric">Always<strong>${m.always_blocks.length}</strong></div><div class="metric">Functions<strong>${m.functions.length}</strong></div></div><div class="card"><h2>Module Summary</h2><span class="pill">project: ${esc(m.project)}</span><span class="pill">kind: ${esc(m.kind)}</span><span class="pill">community: ${esc(m.community)}</span><span class="pill">parse_errors: ${esc(m.parse_errors)}</span></div><div class="card"><h2>Source Snippet</h2>${m.snippet?`<pre>${esc(m.snippet)}</pre>`:'<p class="muted">No source snippet found.</p>'}</div><div class="card"><h2>Ports</h2>${ports}<h2>Parameters</h2>${params}<h2>Always Blocks</h2>${always}<h2>Functions</h2>${fns}</div>`;
}
list.addEventListener('click',e=>{const item=e.target.closest('.mod');if(!item)return;renderPage(data.modules[Number(item.dataset.i)])});
q.addEventListener('input',renderList);kind.addEventListener('change',renderList);project.addEventListener('change',renderList);
content.innerHTML=`<h3>Code AST internals</h3><p>This view shows code-level details extracted from tree-sitter/AST nodes: modules, ports, parameters, always blocks, functions, and source snippets.</p><div class="grid"><div class="metric">Modules<strong>${data.summary.modules}</strong></div><div class="metric">Ports<strong>${data.summary.ports}</strong></div><div class="metric">Params<strong>${data.summary.params}</strong></div><div class="metric">Always<strong>${data.summary.always_blocks}</strong></div></div><p class="muted">Search for terms such as clk_i, rst_ni, rstmgr, ibex_core, always_ff, SVA, or a source file.</p>`;
renderList();
</script>
</body>
</html>"""
    path.write_text(html_text.replace("__DATA__", payload), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    data = build_wiki()
    (OUT_DIR / "code_ast_wiki.json").write_text(
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
                "json": str(OUT_DIR / "code_ast_wiki.json"),
                "markdown": str(OUT_DIR / "index.md"),
                "summary": data["summary"],
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
