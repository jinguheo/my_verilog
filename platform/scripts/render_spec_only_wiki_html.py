#!/usr/bin/env python3
"""Render a wiki-style browser view for the Graphify spec-only graph."""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_GRAPH = ROOT / "dbs" / "graphify-out" / "spec-only-graphify" / "graph.json"
_DEFAULT_OUT   = ROOT / "dbs" / "graphify-out" / "spec-only-wiki"

# resolved at runtime via _parse_args()
GRAPH_PATH: Path
OUT_DIR: Path


def _parse_args() -> None:
    global GRAPH_PATH, OUT_DIR
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph", type=Path, default=_DEFAULT_GRAPH,
                        help="Path to graph.json (default: spec-only-graphify/graph.json)")
    parser.add_argument("--out", type=Path, default=_DEFAULT_OUT,
                        help="Output directory for wiki files")
    args = parser.parse_args()
    GRAPH_PATH = args.graph
    OUT_DIR = args.out


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


def resolve_original_path(node: dict[str, Any]) -> Path | None:
    original = str(node.get("original_source") or "")
    if original:
        p = Path(original)
        if p.exists():
            return p
    source_file = str(node.get("source_file") or "")
    if source_file and not source_file.startswith("__"):
        p = ROOT / "dbs" / source_file.replace("/", "\\")
        if p.exists():
            return p
    return None


def snippet(path: Path | None, line: int | None, radius: int = 5) -> str:
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
    parts = re.split(r"[\\/]+", source_file)
    return parts[0] if parts and parts[0] else "unknown"


def doc_kind(source_file: str) -> str:
    source = source_file.lower()
    if "testplan" in source:
        return "testplan"
    if "checklist" in source:
        return "checklist"
    if "theory" in source:
        return "theory"
    if "interface" in source:
        return "interface"
    if source.endswith(".hjson"):
        return "hjson"
    if source.endswith((".md", ".rst", ".adoc")):
        return "doc"
    return "other"


def compact_node(node: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": str(node.get("id") or ""),
        "label": str(node.get("label") or ""),
        "role": str(node.get("role") or ""),
        "source_file": str(node.get("source_file") or ""),
        "source_location": str(node.get("source_location") or ""),
        "community": str(node.get("community") or ""),
    }


def build_wiki() -> dict[str, Any]:
    graph = read_json(GRAPH_PATH)
    nodes = {str(node["id"]): node for node in graph.get("nodes", [])}
    links = graph.get("links", graph.get("edges", []))

    docs = [node for node in nodes.values() if node.get("role") == "document"]
    sections_by_file: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for node in nodes.values():
        if node.get("role") == "section":
            sections_by_file[str(node.get("source_file") or "")].append(node)

    components_by_file: dict[str, Counter[str]] = defaultdict(Counter)
    topics_by_file: dict[str, Counter[str]] = defaultdict(Counter)
    relation_counts = Counter()

    for edge in links:
        rel = relation(edge)
        relation_counts[rel] += 1
        src = nodes.get(edge_source(edge), {})
        tgt = nodes.get(edge_target(edge), {})
        pair = [src, tgt]
        component = next((n for n in pair if n.get("role") == "component"), None)
        topic = next((n for n in pair if n.get("role") == "topic"), None)
        for node in pair:
            source_file = str(node.get("source_file") or "")
            if source_file and not source_file.startswith("__"):
                if component:
                    components_by_file[source_file][str(component.get("label") or "")] += 1
                if topic:
                    topics_by_file[source_file][str(topic.get("label") or "")] += 1

    pages = []
    for doc in sorted(docs, key=lambda n: str(n.get("source_file") or "")):
        source_file = str(doc.get("source_file") or "")
        original_path = resolve_original_path(doc)
        sections = sorted(
            sections_by_file.get(source_file, []),
            key=lambda n: line_number(str(n.get("source_location") or "")) or 0,
        )
        section_rows = []
        for section in sections:
            lno = line_number(str(section.get("source_location") or ""))
            section_rows.append(
                {
                    **compact_node(section),
                    "line": lno,
                    "snippet": snippet(original_path, lno, 4),
                }
            )
        pages.append(
            {
                **compact_node(doc),
                "project": str(doc.get("project") or project_from_path(source_file)),
                "kind": doc_kind(source_file),
                "bytes": int(doc.get("bytes") or 0),
                "original_source": str(original_path or doc.get("original_source") or ""),
                "sections": section_rows,
                "components": [
                    {"label": label, "count": count}
                    for label, count in components_by_file[source_file].most_common(24)
                ],
                "topics": [
                    {"label": label, "count": count}
                    for label, count in topics_by_file[source_file].most_common(12)
                ],
            }
        )

    components = sorted(
        [compact_node(node) for node in nodes.values() if node.get("role") == "component"],
        key=lambda n: n["label"],
    )
    topics = sorted(
        [compact_node(node) for node in nodes.values() if node.get("role") == "topic"],
        key=lambda n: n["label"],
    )
    role_counts = Counter(str(node.get("role") or "<none>") for node in nodes.values())
    kind_counts = Counter(page["kind"] for page in pages)
    project_counts = Counter(page["project"] for page in pages)
    summary = {
        "source_graph": str(GRAPH_PATH),
        "documents": len(pages),
        "sections": sum(len(page["sections"]) for page in pages),
        "components": len(components),
        "topics": len(topics),
        "roles": role_counts.most_common(),
        "document_kinds": kind_counts.most_common(),
        "projects": project_counts.most_common(),
        "relations": relation_counts.most_common(),
    }
    return {"summary": summary, "pages": pages, "components": components, "topics": topics}


def write_markdown(path: Path, data: dict[str, Any]) -> None:
    lines = [
        "# Spec-Only Wiki",
        "",
        "This wiki is generated from the Graphify spec-only graph. It shows document nodes, internal section nodes, component links, topic links, and source snippets around extracted section lines.",
        "",
        f"- Documents: {data['summary']['documents']}",
        f"- Sections: {data['summary']['sections']}",
        f"- Components: {data['summary']['components']}",
        f"- Topics: {data['summary']['topics']}",
        "",
        "## Document Kinds",
        "",
        "| Kind | Count |",
        "|---|---:|",
    ]
    for kind, count in data["summary"]["document_kinds"]:
        lines.append(f"| `{kind}` | {count} |")
    lines += ["", "## Top Documents By Section Count", "", "| Document | Project | Kind | Sections | Components |", "|---|---|---|---:|---|"]
    top_pages = sorted(data["pages"], key=lambda p: len(p["sections"]), reverse=True)[:80]
    for page in top_pages:
        comps = ", ".join(item["label"] for item in page["components"][:4])
        lines.append(
            f"| `{page['source_file']}` | `{page['project']}` | `{page['kind']}` | {len(page['sections'])} | {comps} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_html(path: Path, data: dict[str, Any]) -> None:
    payload = safe_json(data)
    html_text = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Spec-Only Wiki</title>
<style>
:root{--bg:#f6f7f9;--panel:#fff;--ink:#17202a;--muted:#667085;--line:#d7dde7;--blue:#2f6fed;--green:#16875f;--amber:#b7791f}
*{box-sizing:border-box}body{margin:0;font-family:Arial,Helvetica,sans-serif;background:var(--bg);color:var(--ink)}
header{padding:16px 20px 12px;background:var(--panel);border-bottom:1px solid var(--line)}
h1{margin:0 0 7px;font-size:23px}.meta{display:flex;gap:12px;flex-wrap:wrap;color:var(--muted);font-size:13px}
.shell{display:grid;grid-template-columns:390px 1fr;height:calc(100vh - 76px);min-height:720px}
aside{overflow:auto;background:var(--panel);border-right:1px solid var(--line);padding:14px}
main{overflow:auto;padding:18px 24px 48px}
input,select{width:100%;padding:8px;border:1px solid var(--line);border-radius:6px;background:#fff;margin-bottom:8px}
h2{font-size:13px;text-transform:uppercase;color:var(--muted);margin:16px 0 8px}h3{font-size:20px;margin:0 0 8px}
.doc{border-bottom:1px solid var(--line);padding:8px 4px;cursor:pointer}.doc:hover{background:#f1f5f9}.doc strong{display:block;font-size:13px}.doc span{display:block;color:var(--muted);font-size:12px;line-height:1.35}
.pill{display:inline-block;border:1px solid var(--line);border-radius:999px;padding:3px 8px;margin:2px;font-size:12px;background:#fff}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px;margin:10px 0 18px}.metric{background:#fff;border:1px solid var(--line);border-radius:8px;padding:12px}.metric strong{display:block;font-size:24px}
.card{background:#fff;border:1px solid var(--line);border-radius:8px;padding:14px;margin:12px 0}pre{white-space:pre-wrap;word-break:break-word;background:#0f172a;color:#dbeafe;border-radius:8px;padding:10px;font-size:12px;line-height:1.35;max-height:280px;overflow:auto}
table{width:100%;border-collapse:collapse;background:#fff;border:1px solid var(--line);border-radius:8px;overflow:hidden}th,td{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;font-size:13px;vertical-align:top}th{background:#eef2f7}
a{color:#2457c5}.muted{color:var(--muted)}code{background:#eef2f7;padding:2px 4px;border-radius:4px}
@media(max-width:900px){.shell{grid-template-columns:1fr;height:auto}aside{max-height:460px}main{padding:16px}}
</style>
</head>
<body>
<header>
<h1>Spec-Only Wiki</h1>
<div class="meta" id="meta"></div>
</header>
<div class="shell">
<aside>
  <input id="q" placeholder="Search file, section, component, topic">
  <select id="kind"></select>
  <select id="project"></select>
  <h2>Documents</h2>
  <div id="list"></div>
</aside>
<main id="content"></main>
</div>
<script>
const data=__DATA__;
const q=document.getElementById('q'), kind=document.getElementById('kind'), project=document.getElementById('project'), list=document.getElementById('list'), content=document.getElementById('content');
function esc(s){return String(s??'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}
function textOf(p){return [p.label,p.source_file,p.project,p.kind,...p.sections.map(s=>s.label),...p.components.map(c=>c.label),...p.topics.map(t=>t.label)].join(' ').toLowerCase()}
document.getElementById('meta').innerHTML=`<span>Documents: ${data.summary.documents}</span><span>Sections: ${data.summary.sections}</span><span>Components: ${data.summary.components}</span><span>Topics: ${data.summary.topics}</span>`;
function fillSelect(el,label,values){el.innerHTML=`<option value="">${label}: all</option>`+values.map(v=>`<option value="${esc(v)}">${esc(v)}</option>`).join('')}
fillSelect(kind,'Kind',[...new Set(data.pages.map(p=>p.kind))].sort());
fillSelect(project,'Project',[...new Set(data.pages.map(p=>p.project))].sort());
function filtered(){const term=q.value.trim().toLowerCase();return data.pages.filter(p=>(!kind.value||p.kind===kind.value)&&(!project.value||p.project===project.value)&&(!term||textOf(p).includes(term))).sort((a,b)=>b.sections.length-a.sections.length||a.source_file.localeCompare(b.source_file))}
function renderList(){const pages=filtered().slice(0,400);list.innerHTML=pages.map((p,i)=>`<div class="doc" data-i="${data.pages.indexOf(p)}"><strong>${esc(p.label)}</strong><span>${esc(p.project)} · ${esc(p.kind)} · sections ${p.sections.length} · components ${p.components.length}</span><span>${esc(p.source_file)}</span></div>`).join('')||'<p class="muted">No matches</p>'}
function renderPage(p){const comps=p.components.map(c=>`<span class="pill">${esc(c.label)} · ${c.count}</span>`).join('')||'<span class="muted">None</span>';const topics=p.topics.map(t=>`<span class="pill">${esc(t.label)} · ${t.count}</span>`).join('')||'<span class="muted">None</span>';const rows=p.sections.map(s=>`<tr><td>${esc(s.source_location)}</td><td><strong>${esc(s.label)}</strong>${s.snippet?`<pre>${esc(s.snippet)}</pre>`:''}</td></tr>`).join('');
content.innerHTML=`<h3>${esc(p.label)}</h3><p class="muted">${esc(p.source_file)}<br>${esc(p.original_source)}</p><div class="grid"><div class="metric">Sections<strong>${p.sections.length}</strong></div><div class="metric">Components<strong>${p.components.length}</strong></div><div class="metric">Topics<strong>${p.topics.length}</strong></div><div class="metric">Bytes<strong>${p.bytes||0}</strong></div></div><div class="card"><h2>Components</h2>${comps}<h2>Topics</h2>${topics}</div><div class="card"><h2>Internal Sections and Source Snippets</h2><table><thead><tr><th>Line</th><th>Section / snippet</th></tr></thead><tbody>${rows}</tbody></table></div>`}
list.addEventListener('click',e=>{const item=e.target.closest('.doc');if(!item)return;renderPage(data.pages[Number(item.dataset.i)])});
q.addEventListener('input',renderList);kind.addEventListener('change',renderList);project.addEventListener('change',renderList);
content.innerHTML=`<h3>Spec document internals</h3><p>This view proves spec-only is not just filenames: it shows extracted document sections, component/topic references, and snippets from original files.</p><div class="grid"><div class="metric">Documents<strong>${data.summary.documents}</strong></div><div class="metric">Sections<strong>${data.summary.sections}</strong></div><div class="metric">Components<strong>${data.summary.components}</strong></div><div class="metric">Topics<strong>${data.summary.topics}</strong></div></div><p class="muted">Select a document on the left or search for terms such as rstmgr, testpoints, checklist, covergroups, interfaces.</p>`;
renderList();
</script>
</body>
</html>"""
    path.write_text(html_text.replace("__DATA__", payload), encoding="utf-8")


def main() -> None:
    _parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    data = build_wiki()
    (OUT_DIR / "spec_only_wiki.json").write_text(
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
                "json": str(OUT_DIR / "spec_only_wiki.json"),
                "markdown": str(OUT_DIR / "index.md"),
                "summary": data["summary"],
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
