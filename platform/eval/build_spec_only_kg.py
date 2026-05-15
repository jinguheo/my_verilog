#!/usr/bin/env python3
"""Build a spec-document-only KG without code-derived module bindings."""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SPEC_ROOT = ROOT / "out" / "spec_documents_20260514_204108"
DEFAULT_OUT = ROOT / "out" / "spec_doc_only_kg"

DOC_SUFFIXES = {".md", ".rst", ".txt", ".hjson", ".json", ".yaml", ".yml"}
STOP_TERMS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "this",
    "that",
    "are",
    "not",
    "can",
    "will",
    "shall",
    "must",
    "into",
    "using",
    "section",
    "overview",
    "introduction",
    "description",
}


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
    text = value.replace("\\", "/").lower()
    text = re.sub(r"[^a-z0-9_./#:-]+", "_", text)
    return re.sub(r"_+", "_", text).strip("_")


def add_node(nodes: dict[str, Node], node_id: str, label: str, node_type: str, **props: Any) -> None:
    if node_id not in nodes:
        nodes[node_id] = Node(node_id, label, node_type, props)
    else:
        nodes[node_id].properties.update({k: v for k, v in props.items() if v not in (None, "", [])})


def add_edge(edges: dict[tuple[str, str, str], Edge], source: str, target: str, edge_type: str, weight: int = 1) -> None:
    key = (source, target, edge_type)
    if key in edges:
        edges[key].weight += weight
    else:
        edges[key] = Edge(source, target, edge_type, weight)


def project_for(path: Path, spec_root: Path) -> str:
    try:
        parts = path.relative_to(spec_root).parts
        return parts[0] if len(parts) > 1 else "unknown"
    except Exception:
        return "unknown"


def doc_kind(path: Path) -> str:
    parts = [part.lower() for part in path.parts]
    name = path.name.lower()
    if "testplan" in name or "testplan" in parts:
        return "testplan"
    if name.endswith(".hjson"):
        return "hjson_spec"
    if "doc" in parts:
        return "spec_doc"
    if name == "readme.md":
        return "readme"
    return "document"


def infer_ip(path: Path) -> str:
    parts = [part.lower() for part in path.parts]
    for marker in ("ip", "ip_autogen"):
        if marker in parts:
            idx = parts.index(marker)
            if idx + 1 < len(parts):
                return parts[idx + 1]
    if "rv_core_ibex" in parts:
        return "rv_core_ibex"
    if "ibex" in parts:
        return "ibex"
    return "unassigned"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def extract_sections(path: Path, text: str) -> list[str]:
    sections: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if path.suffix.lower() == ".md" and stripped.startswith("#"):
            title = stripped.lstrip("#").strip()
            if title:
                sections.append(title)
        elif path.suffix.lower() == ".rst":
            if len(stripped) >= 4 and not re.search(r"[{}[\]();,]", stripped):
                if re.match(r"^[A-Z0-9][A-Za-z0-9 _:/().,-]{2,90}$", stripped):
                    sections.append(stripped)
        elif path.suffix.lower() == ".hjson":
            match = re.match(r"\s*(name|title|desc|clock_primary|bus_interfaces|interrupt_list)\s*:", line)
            if match:
                sections.append(match.group(1))
    seen = set()
    unique = []
    for section in sections:
        key = section.lower()
        if key not in seen:
            unique.append(section[:120])
            seen.add(key)
    return unique[:40]


def extract_topics(path: Path, text: str, sections: list[str]) -> list[str]:
    source = " ".join([path.stem.replace("_", " "), *sections, text[:4000]])
    candidates = re.findall(r"\b[a-zA-Z][a-zA-Z0-9_]{2,}\b", source.lower())
    counts = Counter(
        token
        for token in candidates
        if token not in STOP_TERMS
        and not token.isdigit()
        and not token.startswith("http")
        and len(token) <= 32
    )
    preferred = [
        "register",
        "interrupt",
        "alert",
        "clock",
        "reset",
        "bus",
        "tlul",
        "memory",
        "fifo",
        "crypto",
        "debug",
        "security",
        "verification",
        "interface",
        "protocol",
        "counter",
        "timer",
        "power",
        "entropy",
        "lifecycle",
    ]
    ranked = sorted(counts, key=lambda term: (term not in preferred, -counts[term], term))
    return ranked[:12]


def build(spec_root: Path) -> tuple[list[Node], list[Edge], dict[str, Any]]:
    nodes: dict[str, Node] = {}
    edges: dict[tuple[str, str, str], Edge] = {}
    docs = [path for path in spec_root.rglob("*") if path.is_file() and path.suffix.lower() in DOC_SUFFIXES]

    for path in docs:
        rel = path.relative_to(spec_root).as_posix()
        project = project_for(path, spec_root)
        kind = doc_kind(path)
        ip = infer_ip(path)
        folder = str(Path(rel).parent).replace("\\", "/")
        text = read_text(path)
        sections = extract_sections(path, text)
        topics = extract_topics(path, text, sections)

        doc_id = f"doc:{slug(rel)}"
        project_id = f"project:{slug(project)}"
        kind_id = f"doc_kind:{slug(kind)}"
        folder_id = f"folder:{slug(folder)}"
        ip_id = f"ip:{slug(project)}:{slug(ip)}"

        add_node(nodes, doc_id, rel, "document", path=str(path), bytes=path.stat().st_size, doc_kind=kind, project=project, ip_block=ip)
        add_node(nodes, project_id, project, "project")
        add_node(nodes, kind_id, kind, "doc_kind")
        add_node(nodes, folder_id, folder, "folder", project=project)
        add_node(nodes, ip_id, ip, "ip_block", project=project)

        add_edge(edges, doc_id, project_id, "IN_PROJECT")
        add_edge(edges, doc_id, kind_id, "HAS_DOC_KIND")
        add_edge(edges, doc_id, folder_id, "IN_FOLDER")
        add_edge(edges, doc_id, ip_id, "ABOUT_IP")

        previous_section_id = ""
        for index, section in enumerate(sections):
            section_id = f"section:{slug(rel)}:{index}:{slug(section)}"
            add_node(nodes, section_id, section, "spec_section", document=rel, project=project, ip_block=ip)
            add_edge(edges, doc_id, section_id, "HAS_SECTION")
            if previous_section_id:
                add_edge(edges, previous_section_id, section_id, "NEXT_SECTION")
            previous_section_id = section_id

        for topic in topics:
            topic_id = f"topic:{slug(topic)}"
            add_node(nodes, topic_id, topic, "topic")
            add_edge(edges, doc_id, topic_id, "MENTIONS_TOPIC")

    degree = Counter()
    for edge in edges.values():
        degree[edge.source] += edge.weight
        degree[edge.target] += edge.weight
    for node in nodes.values():
        node.properties["degree"] = degree[node.id]

    summary = {
        "source": str(spec_root),
        "documents": len(docs),
        "nodes": len(nodes),
        "edges": len(edges),
        "node_types": dict(sorted(Counter(node.type for node in nodes.values()).items())),
        "edge_types": dict(sorted(Counter(edge.type for edge in edges.values()).items())),
        "projects": dict(sorted(Counter(project_for(path, spec_root) for path in docs).items())),
        "doc_kinds": dict(sorted(Counter(doc_kind(path) for path in docs).items())),
        "top_topics": Counter(edge.target.replace("topic:", "") for edge in edges.values() if edge.type == "MENTIONS_TOPIC").most_common(25),
        "code_dependency": "none",
    }
    return list(nodes.values()), list(edges.values()), summary


def write_json(out_dir: Path, nodes: list[Node], edges: list[Edge], summary: dict[str, Any]) -> None:
    payload = {
        "schema": "spec-only-kg/v1",
        "summary": summary,
        "nodes": [asdict(node) for node in nodes],
        "edges": [asdict(edge) for edge in edges],
    }
    (out_dir / "spec_only_kg.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def write_summary(out_dir: Path, summary: dict[str, Any]) -> None:
    node_types = "\n".join(f"- {key}: {value}" for key, value in summary["node_types"].items())
    edge_types = "\n".join(f"- {key}: {value}" for key, value in summary["edge_types"].items())
    topics = "\n".join(f"- {topic}: {count}" for topic, count in summary["top_topics"][:15])
    text = f"""# Spec-Only KG Summary

This KG is built only from files under `{summary["source"]}`.

It does not read the Verilog codebase, the custom code KG, Graphify, or module-name binding tables.

## Counts

- Documents: {summary["documents"]}
- Nodes: {summary["nodes"]}
- Edges: {summary["edges"]}
- Code dependency: none

## Node Types

{node_types}

## Edge Types

{edge_types}

## Top Document Topics

{topics}
"""
    (out_dir / "SPEC_ONLY_KG_SUMMARY.md").write_text(text, encoding="utf-8")


def write_html(out_dir: Path, nodes: list[Node], edges: list[Edge], summary: dict[str, Any]) -> None:
    data = {
        "summary": summary,
        "nodes": [asdict(node) for node in nodes],
        "edges": [asdict(edge) for edge in edges],
    }
    payload = json.dumps(data, ensure_ascii=False)
    html_text = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Spec-Only Knowledge Graph</title>
<style>
body {{ margin:0; font-family:Arial, Helvetica, sans-serif; background:#f7f7f4; color:#17202a; }}
header {{ padding:16px 22px; background:#fff; border-bottom:1px solid rgba(0,0,0,.12); }}
h1 {{ margin:0 0 8px; font-size:22px; }}
.meta {{ display:flex; gap:12px; flex-wrap:wrap; color:#64748b; font-size:13px; }}
.shell {{ display:grid; grid-template-columns:310px 1fr; height:calc(100vh - 76px); }}
aside {{ background:#fff; border-right:1px solid rgba(0,0,0,.12); padding:14px; overflow:auto; }}
main {{ position:relative; overflow:hidden; }}
canvas {{ width:100%; height:100%; display:block; background:#fbfaf7; }}
h2 {{ font-size:12px; color:#64748b; text-transform:uppercase; margin:16px 0 8px; }}
input {{ width:100%; padding:8px 9px; border:1px solid rgba(0,0,0,.16); border-radius:6px; }}
label {{ display:flex; gap:7px; align-items:center; margin:7px 0; font-size:13px; }}
.row {{ display:grid; grid-template-columns:1fr auto; gap:8px; padding:4px 0; font-size:13px; }}
.swatch {{ width:11px; height:11px; border-radius:50%; display:inline-block; }}
#tip {{ position:absolute; display:none; pointer-events:none; background:#fff; border:1px solid rgba(0,0,0,.14); border-radius:6px; padding:8px 10px; box-shadow:0 8px 22px rgba(0,0,0,.14); max-width:420px; font-size:12px; }}
</style>
</head>
<body>
<header>
  <h1>Spec-Only Knowledge Graph</h1>
  <div class="meta">
    <span>Documents: {summary["documents"]}</span>
    <span>Nodes: {summary["nodes"]}</span>
    <span>Edges: {summary["edges"]}</span>
    <span>Code dependency: none</span>
  </div>
</header>
<div class="shell">
<aside>
  <h2>Search</h2>
  <input id="search" placeholder="document, IP, section, topic">
  <h2>Node Types</h2>
  <div id="filters"></div>
  <h2>Counts</h2>
  <div id="counts"></div>
</aside>
<main><canvas id="graph"></canvas><div id="tip"></div></main>
</div>
<script>
const data = {payload};
const colors = {{
  project:"#2563eb", document:"#1f2937", folder:"#94a3b8", ip_block:"#16a34a",
  spec_section:"#7c3aed", topic:"#f97316", doc_kind:"#0891b2"
}};
let enabled = new Set(Object.keys(colors));
let search = "";
let positions = new Map();
const canvas = document.getElementById("graph");
const ctx = canvas.getContext("2d");
const tip = document.getElementById("tip");

function group(nodes, key) {{
  const out = {{}};
  for (const node of nodes) {{
    const value = key(node);
    out[value] ||= [];
    out[value].push(node);
  }}
  return out;
}}
function visible(node) {{
  if (!enabled.has(node.type)) return false;
  if (!search) return true;
  const props = node.properties || {{}};
  return `${{node.label}} ${{node.type}} ${{props.project || ""}} ${{props.ip_block || ""}}`.toLowerCase().includes(search);
}}
function layout() {{
  const nodes = data.nodes.filter(visible);
  const rect = canvas.getBoundingClientRect();
  const w = Math.max(900, rect.width), h = Math.max(680, rect.height);
  const byType = group(nodes, n => n.type);
  const rings = [["project",70],["ip_block",150],["doc_kind",220],["folder",290],["document",380],["topic",470],["spec_section",560]];
  positions = new Map();
  for (const [type, radius] of rings) {{
    const arr = byType[type] || [];
    for (let i = 0; i < arr.length; i++) {{
      const a = Math.PI * 2 * i / Math.max(1, arr.length) - Math.PI / 2;
      positions.set(arr[i].id, {{x:w/2 + Math.cos(a)*radius, y:h/2 + Math.sin(a)*radius}});
    }}
  }}
}}
function draw() {{
  const rect = canvas.getBoundingClientRect();
  ctx.clearRect(0,0,rect.width,rect.height);
  const ids = new Set([...positions.keys()]);
  ctx.strokeStyle = "rgba(60,60,60,.12)";
  ctx.lineWidth = .7;
  for (const edge of data.edges) {{
    if (!ids.has(edge.source) || !ids.has(edge.target)) continue;
    const a = positions.get(edge.source), b = positions.get(edge.target);
    ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); ctx.stroke();
  }}
  const nodeById = new Map(data.nodes.map(n => [n.id,n]));
  for (const [id,p] of positions.entries()) {{
    const node = nodeById.get(id);
    const degree = node.properties?.degree || 1;
    const r = 3 + Math.min(12, Math.sqrt(degree)*0.5);
    ctx.beginPath(); ctx.fillStyle = colors[node.type] || "#555"; ctx.arc(p.x,p.y,r,0,Math.PI*2); ctx.fill();
    if (search || node.type === "project" || node.type === "ip_block" || degree > 80) {{
      ctx.font = "12px Arial"; ctx.fillStyle = "#17202a"; ctx.fillText(node.label.slice(0,54), p.x + r + 4, p.y + 4);
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
  filters.insertAdjacentHTML("beforeend", `<label><input type="checkbox" checked data-type="${{type}}"><span class="swatch" style="background:${{colors[type] || "#555"}}"></span>${{type}} (${{count}})</label>`);
}}
filters.addEventListener("change", e => {{
  const type = e.target.dataset.type;
  if (!type) return;
  if (e.target.checked) enabled.add(type); else enabled.delete(type);
  relayout();
}});
document.getElementById("search").addEventListener("input", e => {{ search = e.target.value.trim().toLowerCase(); relayout(); }});
const counts = document.getElementById("counts");
for (const [type,count] of Object.entries(data.summary.node_types)) {{
  counts.insertAdjacentHTML("beforeend", `<div class="row"><span>${{type}}</span><strong>${{count}}</strong></div>`);
}}
canvas.addEventListener("mousemove", e => {{
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left, y = e.clientY - rect.top;
  const nodeById = new Map(data.nodes.map(n => [n.id,n]));
  let hit = null;
  for (const [id,p] of positions.entries()) {{
    const n = nodeById.get(id), r = 5 + Math.min(12, Math.sqrt(n.properties?.degree || 1)*0.5);
    if (Math.hypot(p.x-x,p.y-y) <= r) {{ hit = n; break; }}
  }}
  if (!hit) {{ tip.style.display = "none"; return; }}
  tip.style.display = "block"; tip.style.left = `${{x+12}}px`; tip.style.top = `${{y+12}}px`;
  tip.innerHTML = `<strong>${{hit.type}}</strong><br>${{hit.label.replace(/[&<>]/g,c=>({{"&":"&amp;","<":"&lt;",">":"&gt;"}}[c]))}}<br>degree: ${{hit.properties?.degree || 0}}`;
}});
resize();
window.addEventListener("resize", resize);
</script>
</body>
</html>
"""
    (out_dir / "spec_only_kg.html").write_text(html_text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a code-free spec document KG.")
    parser.add_argument("--spec-root", type=Path, default=DEFAULT_SPEC_ROOT)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    nodes, edges, summary = build(args.spec_root)
    write_json(args.out, nodes, edges, summary)
    write_summary(args.out, summary)
    write_html(args.out, nodes, edges, summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
