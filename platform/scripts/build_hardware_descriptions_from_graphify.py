#!/usr/bin/env python3
"""Build intermediate hardware description documents from Graphify spec-code data.

The generated documents sit between spec-only and code-only graphs:
spec document nodes <-> hardware description <-> code nodes.

Improvements over v1:
- Spec section snippets pulled from spec-only-graphify graph
- Functional summary generated from top spec section titles + snippets
- Neighbor components listed with relationship counts
- Code module inventory grouped by category (rtl/dv/sva/package)
"""

from __future__ import annotations

import html
import json
import re
import textwrap
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
GRAPH_PATH = ROOT / "dbs" / "graphify-out" / "spec-code-graphify" / "graph.json"
SPEC_ONLY_GRAPH = ROOT / "dbs" / "graphify-out" / "spec-only-graphify" / "graph.json"
OUT_DIR = ROOT / "dbs" / "graphify-out" / "hardware-descriptions"
BRIDGE_RELATIONS = {"spec_component_matches_code", "spec_path_matches_code_path"}
CODE_RELATIONS = {"defines", "instantiates", "imports_from", "imports", "contains", "uses", "calls", "method"}


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def esc(value: Any) -> str:
    return html.escape(str(value or ""), quote=True)


def relation(edge: dict[str, Any]) -> str:
    return str(edge.get("relation") or edge.get("type") or "related")


def edge_source(edge: dict[str, Any]) -> str:
    return str(edge.get("source") or edge.get("_src") or "")


def edge_target(edge: dict[str, Any]) -> str:
    return str(edge.get("target") or edge.get("_tgt") or "")


def slug(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9_+.-]+", "_", value.strip().lower())
    return value.strip("_") or "unknown"


def path_parts(source_file: str) -> list[str]:
    return [part for part in re.split(r"[\\/]+", str(source_file or "")) if part]


def component_key(node: dict[str, Any]) -> str:
    label = str(node.get("label") or "")
    if label.startswith("component:"):
        return label.split(":", 1)[1]
    parts = path_parts(str(node.get("source_file") or ""))
    for marker in ("ip_autogen", "ip"):
        if marker in parts:
            idx = parts.index(marker)
            if idx + 1 < len(parts):
                return parts[idx + 1]
    for marker in ("vendor",):
        if marker in parts:
            idx = parts.index(marker)
            if idx + 1 < len(parts):
                return parts[idx + 1]
    candidates = [
        part
        for part in parts
        if part not in {"hw", "sw", "dv", "rtl", "data", "doc", "docs", "src", "tests", "autogen",
                        "top_earlgrey", "top_darjeeling", "top_englishbreakfast"}
    ]
    for part in candidates:
        if re.search(r"ctrl|mgr|handler|ibex|aes|uart|spi|i2c|gpio|rv_|sensor|alert|pwm|xbar|otp|prim", part):
            return part
    return "unknown"


def category_for_code(node: dict[str, Any]) -> str:
    label = str(node.get("label") or "")
    source = str(node.get("source_file") or "").lower()
    if "\\dv\\sva\\" in source or "/dv/sva/" in source or "sva" in label.lower() or "assert" in label.lower():
        return "sva"
    if "\\dv\\" in source or "/dv/" in source or "\\fpv\\" in source or "/fpv/" in source:
        return "dv"
    if "\\rtl\\" in source or "/rtl/" in source:
        return "rtl"
    if label.endswith("_pkg") or label.endswith("_pkg.sv") or "_pkg" in label:
        return "package"
    if source.endswith((".sv", ".v", ".svh", ".vh")):
        return "rtl"
    return "other_code"


def category_for_spec(node: dict[str, Any]) -> str:
    label = str(node.get("label") or "").lower()
    source = str(node.get("source_file") or "").lower()
    if "testplan" in label or "testplan" in source:
        return "testplan"
    if "theory" in label or "theory" in source:
        return "theory"
    if node.get("role") == "component":
        return "component"
    if "interface" in label or "interface" in source:
        return "interface"
    return "document"


def node_ref(node: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": str(node.get("id") or ""),
        "label": str(node.get("label") or ""),
        "file_type": str(node.get("file_type") or ""),
        "role": str(node.get("role") or ""),
        "source_file": str(node.get("source_file") or ""),
        "source_location": str(node.get("source_location") or ""),
        "community": str(node.get("community") or ""),
    }


def add_limited(bucket: list[dict[str, Any]], item: dict[str, Any], limit: int = 80) -> None:
    if len(bucket) < limit and item not in bucket:
        bucket.append(item)


# ---------------------------------------------------------------------------
# Spec snippet index: source_file -> list of (section_label, snippet)
# ---------------------------------------------------------------------------

def load_spec_snippets() -> dict[str, list[tuple[str, str]]]:
    """Load section snippets from spec-only-graphify, indexed by source_file."""
    if not SPEC_ONLY_GRAPH.exists():
        return {}
    data = read_json(SPEC_ONLY_GRAPH)
    index: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for node in data.get("nodes", []):
        snippet = str(node.get("snippet") or "").strip()
        if not snippet:
            continue
        src = str(node.get("source_file") or "").strip()
        label = str(node.get("label") or node.get("id") or "").strip()
        # Normalise source_file to forward-slash for consistent matching
        src_norm = src.replace("\\", "/")
        index[src_norm].append((label, snippet))
    return index


_PREFERRED_EXTS = {".rst", ".md", ".txt"}
# File basenames to deprioritise for functional summary (checklists, indices, etc.)
_LOW_PRIORITY_FILES = re.compile(r"(checklist|changelog|index|conf|__init__|glossary)", re.IGNORECASE)
_SKIP_LABELS = re.compile(
    r"^(human[\s_]name|one[\s_]line[\s_]desc|one[\s_]paragraph[\s_]desc|"
    r"clocking|reset_signal|scan_reset_only|bus_interfaces|registers|"
    r"param_list|features|copyright|spdx|license|name|version|"
    r"d[0-9]|s[0-9]|v[0-9]|checklist|design[\s_]checklist|dv[\s_]checklist)$",
    re.IGNORECASE,
)


def _src_priority(src: str) -> int:
    """Lower = higher priority. Prefer .rst/.md over .hjson; deprioritise checklists/indices."""
    ext = src.rsplit(".", 1)[-1].lower() if "." in src else ""
    base = src.rsplit("/", 1)[-1].rsplit("\\", 1)[-1]
    if ext not in ("rst", "md", "txt"):
        return 3
    if _LOW_PRIORITY_FILES.search(base):
        return 2
    return 0


def snippets_for_component(
    spec_nodes: list[dict[str, Any]],
    snippet_index: dict[str, list[tuple[str, str]]],
    max_per_file: int = 3,
    max_total: int = 8,
) -> list[tuple[str, str, str]]:
    """Return [(source_file, section_label, snippet), ...] for a component's spec nodes."""
    # Sort spec nodes: prefer .rst/.md files first
    sorted_nodes = sorted(
        spec_nodes,
        key=lambda n: _src_priority(n.get("source_file", "")),
    )
    seen_files: set[str] = set()
    results: list[tuple[str, str, str]] = []
    for node in sorted_nodes:
        src = node.get("source_file", "").replace("\\", "/")
        if src in seen_files:
            continue
        seen_files.add(src)
        pairs = snippet_index.get(src, [])
        count = 0
        for label, snip in pairs:
            if _SKIP_LABELS.match(label.strip()):
                continue
            results.append((src, label, snip))
            count += 1
            if count >= max_per_file or len(results) >= max_total:
                break
        if len(results) >= max_total:
            break
    return results


def make_functional_summary(snippets: list[tuple[str, str, str]]) -> str:
    """Produce a brief functional summary from top spec snippets."""
    if not snippets:
        return "_No spec snippet available. Derived from bridge evidence only._"
    lines: list[str] = []
    label_norm = re.compile(r"\s+")
    for src, label, snip in snippets[:3]:
        # Skip RST heading lines (the label itself) and underline markers (=, -, ~, ^)
        label_stripped = label_norm.sub(" ", label).strip().lower()
        body_lines = []
        for ln in snip.splitlines():
            stripped = ln.strip()
            if not stripped:
                continue
            # Skip RST underlines and markdown headings (# ...)
            if re.match(r"^[=\-~^*`]{3,}$", stripped) or re.match(r"^#{1,6}\s", stripped):
                continue
            # Skip HTML comments, table rows, and boilerplate
            if (stripped.startswith("<!--")
                    or stripped.startswith("|")
                    or re.match(r"^(//|#)\s*(copyright|licensed|spdx)", stripped, re.IGNORECASE)
                    or re.match(r"^\{", stripped)):  # hjson/json opening brace
                continue
            # Skip line if it matches the section label
            if label_norm.sub(" ", stripped.lstrip("#").strip()).lower() == label_stripped:
                continue
            body_lines.append(stripped)
        if body_lines:
            first = textwrap.shorten(body_lines[0], width=220, placeholder="…")
            lines.append(f"- **{label}**: {first}")
    return "\n".join(lines) if lines else "_Summary not extractable from available snippets._"


# ---------------------------------------------------------------------------
# Build component data
# ---------------------------------------------------------------------------

def build(snippet_index: dict[str, list[tuple[str, str]]]) -> dict[str, Any]:
    graph = read_json(GRAPH_PATH)
    nodes = {str(node["id"]): node for node in graph.get("nodes", [])}
    links = graph.get("links", graph.get("edges", []))

    components: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "component": "",
            "spec_nodes": [],
            "code_nodes": [],
            "bridge_edges": [],
            "code_relations": Counter(),
            "spec_categories": Counter(),
            "code_categories": Counter(),
            "bridge_relations": Counter(),
            "neighbors": Counter(),
            "neighbor_relations": defaultdict(Counter),  # neighbor -> {relation: count}
        }
    )
    node_component: dict[str, str] = {}

    for node_id, node in nodes.items():
        comp = component_key(node)
        node_component[node_id] = comp
        if comp == "unknown":
            continue
        row = components[comp]
        row["component"] = comp
        if node.get("file_type") == "document":
            add_limited(row["spec_nodes"], node_ref(node))
            row["spec_categories"][category_for_spec(node)] += 1
        elif node.get("file_type") == "code":
            add_limited(row["code_nodes"], node_ref(node))
            row["code_categories"][category_for_code(node)] += 1

    for edge in links:
        src, tgt = edge_source(edge), edge_target(edge)
        if src not in nodes or tgt not in nodes:
            continue
        rel = relation(edge)
        src_node, tgt_node = nodes[src], nodes[tgt]
        if rel in BRIDGE_RELATIONS and src_node.get("file_type") != tgt_node.get("file_type"):
            spec = src_node if src_node.get("file_type") == "document" else tgt_node
            code = tgt_node if src_node.get("file_type") == "document" else src_node
            comp = component_key(spec)
            if comp == "unknown":
                comp = component_key(code)
            row = components[comp]
            row["component"] = comp
            row["bridge_relations"][rel] += 1
            row["spec_categories"][category_for_spec(spec)] += 1
            row["code_categories"][category_for_code(code)] += 1
            add_limited(row["spec_nodes"], node_ref(spec))
            add_limited(row["code_nodes"], node_ref(code))
            if len(row["bridge_edges"]) < 160:
                row["bridge_edges"].append({"relation": rel, "spec": node_ref(spec), "code": node_ref(code)})
        elif rel in CODE_RELATIONS:
            src_comp = node_component.get(src, "unknown")
            tgt_comp = node_component.get(tgt, "unknown")
            if src_comp == tgt_comp and src_comp != "unknown":
                components[src_comp]["code_relations"][rel] += 1
            elif src_comp != "unknown" and tgt_comp != "unknown":
                components[src_comp]["neighbors"][tgt_comp] += 1
                components[tgt_comp]["neighbors"][src_comp] += 1
                components[src_comp]["neighbor_relations"][tgt_comp][rel] += 1
                components[tgt_comp]["neighbor_relations"][src_comp][rel] += 1

    # Attach snippets
    for comp, row in components.items():
        row["spec_snippets"] = snippets_for_component(row["spec_nodes"], snippet_index)

    rows = []
    for comp, row in components.items():
        bridge_count = sum(row["bridge_relations"].values())
        code_count = len(row["code_nodes"])
        spec_count = len(row["spec_nodes"])
        if bridge_count == 0 and (code_count < 5 or spec_count == 0):
            continue
        rows.append(row)
    rows.sort(key=lambda row: (-sum(row["bridge_relations"].values()), row["component"]))
    return {
        "source_graph": str(GRAPH_PATH),
        "spec_only_graph": str(SPEC_ONLY_GRAPH),
        "components": rows,
        "summary": {
            "components": len(rows),
            "total_bridge_edges": sum(sum(row["bridge_relations"].values()) for row in rows),
            "total_code_refs": sum(len(row["code_nodes"]) for row in rows),
            "total_spec_refs": sum(len(row["spec_nodes"]) for row in rows),
        },
    }


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def md_list(title: str, rows: list[dict[str, Any]], limit: int = 30) -> list[str]:
    out = [f"## {title}", ""]
    if not rows:
        return out + ["- None", ""]
    for row in rows[:limit]:
        loc = row.get("source_location")
        suffix = f" ({loc})" if loc else ""
        out.append(f"- `{row['label']}`{suffix} — `{row['source_file']}`")
    out.append("")
    return out


def md_code_by_category(code_nodes: list[dict[str, Any]], limit: int = 50) -> list[str]:
    """Group code nodes by rtl/dv/sva/package category."""
    by_cat: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for node in code_nodes[:limit]:
        by_cat[category_for_code(node)].append(node)
    order = ["rtl", "dv", "sva", "package", "other_code"]
    lines: list[str] = []
    for cat in order:
        items = by_cat.get(cat)
        if not items:
            continue
        lines.append(f"**{cat.upper()}** ({len(items)})")
        for item in items[:20]:
            loc = item.get("source_location")
            suffix = f":{loc}" if loc else ""
            lines.append(f"  - `{item['label']}`{suffix} — `{item['source_file']}`")
    return lines


def write_component_md(out: Path, row: dict[str, Any]) -> None:
    comp = row["component"]
    bridge_count = sum(row["bridge_relations"].values())
    code_cats = ", ".join(f"{k}: {v}" for k, v in row["code_categories"].most_common())
    spec_cats = ", ".join(f"{k}: {v}" for k, v in row["spec_categories"].most_common())
    rels_str = ", ".join(f"{k}: {v}" for k, v in row["bridge_relations"].most_common())

    snippets: list[tuple[str, str, str]] = row.get("spec_snippets", [])
    func_summary = make_functional_summary(snippets)

    # Neighbor section
    neighbor_lines: list[str] = []
    neighbor_rels: dict[str, Counter] = row.get("neighbor_relations", {})
    top_neighbors = row["neighbors"].most_common(12)
    for nbr, count in top_neighbors:
        nbr_rels = neighbor_rels.get(nbr, Counter())
        rel_summary = ", ".join(f"{r}×{c}" for r, c in nbr_rels.most_common(3))
        neighbor_lines.append(f"- `{nbr}` ({count} refs" + (f"; {rel_summary}" if rel_summary else "") + ")")

    lines = [
        f"# Hardware Description: {comp}",
        "",
        "_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._",
        "",
        "## Functional Summary",
        "",
        func_summary,
        "",
        "## Identity",
        "",
        f"- `ip_block`: `{comp}`",
        f"- `bridge_edge_count`: {bridge_count}",
        f"- Spec categories: {spec_cats or 'none'}",
        f"- Code categories: {code_cats or 'none'}",
        f"- Bridge relations: {rels_str or 'none'}",
        "",
    ]

    # Spec snippets section
    if snippets:
        lines += ["## Spec Excerpts", ""]
        for src, label, snip in snippets:
            short_snip = snip[:400].rstrip()
            if len(snip) > 400:
                short_snip += "\n…"
            lines += [
                f"### {label}",
                f"_Source: `{src}`_",
                "",
                "```",
                short_snip,
                "```",
                "",
            ]

    # Spec anchors list
    lines += md_list("Spec Anchors", row["spec_nodes"], 35)

    # Code evidence grouped by category
    lines += ["## Code Evidence", ""]
    lines += md_code_by_category(row["code_nodes"])
    lines += [""]

    # Neighbor components
    if neighbor_lines:
        lines += ["## Neighbor Components", ""]
        lines += neighbor_lines
        lines += [""]

    # Bridge table
    lines += [
        "## Direct Spec-Code Bridges",
        "",
        "| Relation | Spec anchor | Code artifact | Code file |",
        "|---|---|---|---|",
    ]
    for edge in row["bridge_edges"][:60]:
        lines.append(
            f"| `{edge['relation']}` | `{edge['spec']['label']}` | `{edge['code']['label']}` | `{edge['code']['source_file']}` |"
        )
    lines += [
        "",
        "## Retrieval Guidance",
        "",
        f"- For code-only queries mentioning `{comp}`, expand toward spec anchors via this description.",
        "- Spec Excerpts above show primary functional context — prefer these over raw file lists.",
        "- Bridge table maps the exact spec ↔ code correspondences found by Graphify.",
        "- Neighbor components listed above share code-level relationships with `{comp}`.".replace("{comp}", comp),
        "",
    ]

    out.write_text("\n".join(lines), encoding="utf-8")


def write_index_md(out: Path, data: dict[str, Any]) -> None:
    lines = [
        "# Hardware Descriptions From Graphify",
        "",
        "Intermediate documents generated from code/spec bridge evidence.",
        "Each page includes spec excerpts, code inventory (grouped by rtl/dv/sva), and neighbor components.",
        "",
        f"- Components: {data['summary']['components']}",
        f"- Bridge edges: {data['summary']['total_bridge_edges']}",
        f"- Code references: {data['summary']['total_code_refs']}",
        f"- Spec references: {data['summary']['total_spec_refs']}",
        "",
        "## Components",
        "",
        "| Component | Bridge edges | Code refs | Spec refs | Document |",
        "|---|---:|---:|---:|---|",
    ]
    for row in data["components"]:
        comp = row["component"]
        md_name = f"blocks/{slug(comp)}.md"
        has_snippets = "✓" if row.get("spec_snippets") else ""
        lines.append(
            f"| `{comp}` | {sum(row['bridge_relations'].values())} | {len(row['code_nodes'])} "
            f"| {len(row['spec_nodes'])} {has_snippets} | [{md_name}]({md_name}) |"
        )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_html_index(out: Path, data: dict[str, Any]) -> None:
    cards = []
    for row in data["components"][:120]:
        comp = row["component"]
        bridge_count = sum(row["bridge_relations"].values())
        code_samples = ", ".join(item["label"] for item in row["code_nodes"][:4])
        spec_samples = ", ".join(item["label"] for item in row["spec_nodes"][:3])
        snippet_badge = '<span class="badge">snippets</span>' if row.get("spec_snippets") else ""
        cards.append(
            f"""<a class="card" href="blocks/{slug(comp)}.md"><strong>{esc(comp)}</strong>{snippet_badge}
<span>{bridge_count} bridge edges · {len(row['code_nodes'])} code refs · {len(row['spec_nodes'])} spec refs</span>
<small>Spec: {esc(spec_samples)}<br>Code: {esc(code_samples)}</small></a>"""
        )
    html_text = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Hardware Descriptions</title>
  <style>
    body {{ margin: 0; font-family: Arial, Helvetica, sans-serif; background: #f6f7f9; color: #17202a; }}
    main {{ max-width: 1180px; margin: 0 auto; padding: 32px 22px 48px; }}
    h1 {{ margin: 0 0 8px; font-size: 28px; }} p {{ color: #667085; line-height: 1.5; }}
    .metrics {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 12px; margin: 18px 0; }}
    .metric, .card {{ background: #fff; border: 1px solid #d7dde7; border-radius: 8px; padding: 14px; }}
    .metric strong {{ display: block; font-size: 25px; margin-top: 4px; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; margin-top: 16px; }}
    a.card {{ display: block; text-decoration: none; color: #17202a; min-height: 130px; position: relative; }}
    .card:hover {{ background: #f1f5f9; }}
    .card strong {{ font-size: 17px; display: block; margin-bottom: 6px; }}
    .card span {{ display: block; color: #344054; font-size: 13px; margin-bottom: 6px; }}
    .card small {{ color: #667085; line-height: 1.4; }}
    .badge {{ background: #16875f; color: #fff; font-size: 10px; padding: 2px 6px; border-radius: 4px;
              margin-left: 8px; vertical-align: middle; }}
    .links a {{ margin-right: 12px; color: #2457c5; }}
  </style>
</head>
<body><main>
  <h1>Hardware Descriptions</h1>
  <p>Generated from Graphify spec-code bridge evidence. <span class="badge">snippets</span> = spec text excerpts available.</p>
  <div class="links">
    <a href="../html-views/spec-code-bridge-only.html">Spec-code bridge graph</a>
    <a href="hardware-description-bridge.html">Bridge visualization</a>
    <a href="index.md">Markdown index</a>
    <a href="hardware_descriptions.json">JSON</a>
  </div>
  <div class="metrics">
    <div class="metric">Components<strong>{data['summary']['components']}</strong></div>
    <div class="metric">Bridge edges<strong>{data['summary']['total_bridge_edges']}</strong></div>
    <div class="metric">Code refs<strong>{data['summary']['total_code_refs']}</strong></div>
    <div class="metric">Spec refs<strong>{data['summary']['total_spec_refs']}</strong></div>
  </div>
  <div class="grid">{''.join(cards)}</div>
</main></body></html>"""
    out.write_text(html_text, encoding="utf-8")


def write_bridge_html(out: Path, data: dict[str, Any]) -> None:
    components = data["components"][:36]
    nodes = []
    links = []
    for row in components:
        comp = row["component"]
        hd_id = f"hd:{comp}"
        nodes.append({"id": hd_id, "label": comp, "type": "hardware_description",
                      "count": sum(row["bridge_relations"].values()),
                      "has_snippets": bool(row.get("spec_snippets"))})
        for spec in row["spec_nodes"][:4]:
            sid = f"spec:{spec['id']}"
            nodes.append({"id": sid, "label": spec["label"], "type": "spec", "file": spec["source_file"]})
            links.append({"source": sid, "target": hd_id, "relation": "describes"})
        for code in row["code_nodes"][:6]:
            cid = f"code:{code['id']}"
            nodes.append({"id": cid, "label": code["label"], "type": "code", "file": code["source_file"]})
            links.append({"source": hd_id, "target": cid, "relation": "implemented_by"})
    payload = json.dumps({"nodes": nodes, "links": links}, ensure_ascii=False).replace("</", "<\\/")
    html_text = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hardware Description Bridge</title>
<style>
body{margin:0;font-family:Arial,Helvetica,sans-serif;background:#f6f7f9;color:#17202a}
header{padding:16px 20px;background:#fff;border-bottom:1px solid #d7dde7}
h1{margin:0;font-size:22px}
canvas{display:block;width:100vw;height:calc(100vh - 62px);background:#fbfaf7}
#tip{position:absolute;display:none;background:#fff;border:1px solid #d7dde7;border-radius:6px;padding:8px 10px;
     box-shadow:0 8px 22px rgba(0,0,0,.14);font-size:12px;max-width:420px;pointer-events:none}
</style></head>
<body>
<header><h1>Spec → Hardware Description → Code Bridge</h1></header>
<canvas id="c"></canvas><div id="tip"></div>
<script>
const data=__PAYLOAD__;
const c=document.getElementById('c'),ctx=c.getContext('2d'),tip=document.getElementById('tip');
const nodes=[...new Map(data.nodes.map(n=>[n.id,n])).values()],links=data.links;
const byId=new Map(nodes.map(n=>[n.id,n]));
let w=0,h=0;
function color(t,hasSnip){
  if(t==='spec') return '#2f6fed';
  if(t==='code') return '#16875f';
  return hasSnip?'#b7791f':'#c9a84c';
}
function layout(){
  w=c.clientWidth;h=c.clientHeight;
  c.width=w*devicePixelRatio;c.height=h*devicePixelRatio;
  ctx.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0);
  const specs=nodes.filter(n=>n.type==='spec');
  const hds=nodes.filter(n=>n.type==='hardware_description');
  const codes=nodes.filter(n=>n.type==='code');
  specs.forEach((n,i)=>{n.x=180+(i%4)*88;n.y=50+Math.floor(i/4)*34});
  hds.forEach((n,i)=>{n.x=w/2+(i%3-1)*135;n.y=70+Math.floor(i/3)*64});
  codes.forEach((n,i)=>{n.x=w-420+(i%6)*68;n.y=50+Math.floor(i/6)*30});
  draw();
}
function draw(){
  ctx.clearRect(0,0,w,h);ctx.lineWidth=1;
  for(const e of links){
    const a=byId.get(e.source),b=byId.get(e.target);
    if(!a||!b)continue;
    ctx.strokeStyle=e.relation==='describes'?'rgba(47,111,237,.22)':'rgba(22,135,95,.22)';
    ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();
  }
  for(const n of nodes){
    const r=n.type==='hardware_description'?10:5;
    ctx.fillStyle=color(n.type,n.has_snippets);
    ctx.beginPath();ctx.arc(n.x,n.y,r,0,Math.PI*2);ctx.fill();
    if(n.type==='hardware_description'){
      ctx.fillStyle='#17202a';ctx.font='12px Arial';ctx.fillText(n.label,n.x+13,n.y+4);
    }
  }
}
c.addEventListener('mousemove',e=>{
  const r=c.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top;
  let hit=null;
  for(const n of nodes){if(Math.hypot(n.x-x,n.y-y)<12)hit=n;}
  if(!hit){tip.style.display='none';return;}
  tip.style.display='block';
  tip.style.left=(e.clientX-r.left+12)+'px';
  tip.style.top=(e.clientY-r.top+12)+'px';
  tip.innerHTML=`<strong>${hit.type}</strong><br>${hit.label}${hit.has_snippets?' ✓ snippets':''}<br>${hit.file||''}`;
});
window.addEventListener('resize',layout);layout();
</script></body></html>"""
    html_text = html_text.replace("__PAYLOAD__", payload)
    out.write_text(html_text, encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "blocks").mkdir(parents=True, exist_ok=True)

    print("Loading spec snippets from spec-only-graphify...")
    snippet_index = load_spec_snippets()
    print(f"  Loaded snippets for {len(snippet_index)} source files")

    print("Building component data from spec-code graph...")
    data = build(snippet_index)

    with_snippets = sum(1 for row in data["components"] if row.get("spec_snippets"))
    print(f"  {data['summary']['components']} components, {with_snippets} have spec snippets")

    for row in data["components"]:
        write_component_md(OUT_DIR / "blocks" / f"{slug(row['component'])}.md", row)

    (OUT_DIR / "hardware_descriptions.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False, default=str) + "\n",
        encoding="utf-8",
    )
    write_index_md(OUT_DIR / "index.md", data)
    write_html_index(OUT_DIR / "index.html", data)
    write_bridge_html(OUT_DIR / "hardware-description-bridge.html", data)

    print(json.dumps({
        "status": "ok",
        "out_dir": str(OUT_DIR),
        "index_html": str(OUT_DIR / "index.html"),
        "components": data["summary"]["components"],
        "with_spec_snippets": with_snippets,
        "bridge_edges": data["summary"]["total_bridge_edges"],
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
