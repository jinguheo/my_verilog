#!/usr/bin/env python3
"""Build intermediate hardware description documents from Graphify spec-code data.

The generated documents are meant to sit between spec-only and code-only graphs:
spec document nodes <-> hardware description <-> code nodes.
"""

from __future__ import annotations

import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
GRAPH_PATH = ROOT / "dbs" / "graphify-out" / "spec-code-graphify" / "graph.json"
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
        if part not in {"hw", "sw", "dv", "rtl", "data", "doc", "docs", "src", "tests", "autogen", "top_earlgrey", "top_darjeeling", "top_englishbreakfast"}
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


def build() -> dict[str, Any]:
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
                row["bridge_edges"].append(
                    {
                        "relation": rel,
                        "spec": node_ref(spec),
                        "code": node_ref(code),
                    }
                )
        elif rel in CODE_RELATIONS:
            src_comp, tgt_comp = node_component.get(src, "unknown"), node_component.get(tgt, "unknown")
            if src_comp == tgt_comp and src_comp != "unknown":
                components[src_comp]["code_relations"][rel] += 1
            elif src_comp != "unknown" and tgt_comp != "unknown":
                components[src_comp]["neighbors"][tgt_comp] += 1
                components[tgt_comp]["neighbors"][src_comp] += 1

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
        "components": rows,
        "summary": {
            "components": len(rows),
            "total_bridge_edges": sum(sum(row["bridge_relations"].values()) for row in rows),
            "total_code_refs": sum(len(row["code_nodes"]) for row in rows),
            "total_spec_refs": sum(len(row["spec_nodes"]) for row in rows),
        },
    }


def md_list(title: str, rows: list[dict[str, Any]], limit: int = 30) -> list[str]:
    out = [f"## {title}", ""]
    if not rows:
        return out + ["- None", ""]
    for row in rows[:limit]:
        loc = row.get("source_location")
        suffix = f" ({loc})" if loc else ""
        out.append(f"- `{row['label']}`{suffix} - `{row['source_file']}`")
    out.append("")
    return out


def write_component_md(out: Path, row: dict[str, Any]) -> None:
    comp = row["component"]
    bridge_count = sum(row["bridge_relations"].values())
    code_cats = ", ".join(f"{k}: {v}" for k, v in row["code_categories"].most_common())
    spec_cats = ", ".join(f"{k}: {v}" for k, v in row["spec_categories"].most_common())
    rels = ", ".join(f"{k}: {v}" for k, v in row["bridge_relations"].most_common())
    lines = [
        f"# Hardware Description: {comp}",
        "",
        "This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.",
        "",
        "## Bridge Keys",
        "",
        f"- `ip_block`: `{comp}`",
        f"- `approved_label`: `pending:{comp}`",
        f"- `doc_anchor`: `{comp}`",
        f"- `module_name_prefix`: `{comp}`",
        f"- `bridge_edge_count`: {bridge_count}",
        "",
        "## Inferred Hardware Role",
        "",
        f"`{comp}` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.",
        "",
        "## Evidence Summary",
        "",
        f"- Spec categories: {spec_cats or 'none'}",
        f"- Code categories: {code_cats or 'none'}",
        f"- Bridge relations: {rels or 'none'}",
        "",
    ]
    lines += md_list("Spec Anchors", row["spec_nodes"], 35)
    lines += md_list("Code Evidence", row["code_nodes"], 45)
    lines += [
        "## Direct Spec-Code Bridges",
        "",
        "| Relation | Spec anchor | Code artifact | Code file |",
        "|---|---|---|---|",
    ]
    for edge in row["bridge_edges"][:80]:
        lines.append(
            f"| `{edge['relation']}` | `{edge['spec']['label']}` | `{edge['code']['label']}` | `{edge['code']['source_file']}` |"
        )
    lines += [
        "",
        "## Retrieval Guidance",
        "",
        f"- When a code-only query mentions `{comp}`, use this hardware description to expand toward spec anchors.",
        "- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.",
        "- Human review can replace `pending:*` with an approved label after validating the connection.",
        "",
    ]
    out.write_text("\n".join(lines), encoding="utf-8")


def write_index_md(out: Path, data: dict[str, Any]) -> None:
    lines = [
        "# Hardware Descriptions From Graphify",
        "",
        "These intermediate documents are generated from code/spec bridge evidence. They are intended to help code-only retrieval infer likely spec document anchors.",
        "",
        f"- Components: {data['summary']['components']}",
        f"- Bridge edges represented: {data['summary']['total_bridge_edges']}",
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
        lines.append(
            f"| `{comp}` | {sum(row['bridge_relations'].values())} | {len(row['code_nodes'])} | {len(row['spec_nodes'])} | [{md_name}]({md_name}) |"
        )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_html_index(out: Path, data: dict[str, Any]) -> None:
    cards = []
    for row in data["components"][:120]:
        comp = row["component"]
        bridge_count = sum(row["bridge_relations"].values())
        code_samples = ", ".join(item["label"] for item in row["code_nodes"][:4])
        spec_samples = ", ".join(item["label"] for item in row["spec_nodes"][:3])
        cards.append(
            f"""<a class="card" href="blocks/{slug(comp)}.md"><strong>{esc(comp)}</strong>
<span>{bridge_count} bridge edges · {len(row['code_nodes'])} code refs · {len(row['spec_nodes'])} spec refs</span>
<small>Spec: {esc(spec_samples)}<br>Code: {esc(code_samples)}</small></a>"""
        )
    html_text = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hardware Descriptions</title>
<style>
body{{margin:0;font-family:Arial,Helvetica,sans-serif;background:#f6f7f9;color:#17202a}}
main{{max-width:1180px;margin:0 auto;padding:32px 22px 48px}}
h1{{margin:0 0 8px;font-size:28px}}p{{color:#667085;line-height:1.5}}
.metrics{{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin:18px 0}}
.metric,.card{{background:#fff;border:1px solid #d7dde7;border-radius:8px;padding:14px}}
.metric strong{{display:block;font-size:25px;margin-top:4px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px;margin-top:16px}}
a.card{{display:block;text-decoration:none;color:#17202a;min-height:150px}}
.card:hover{{background:#f1f5f9}}.card strong{{font-size:18px;display:block;margin-bottom:8px}}
.card span{{display:block;color:#344054;font-size:13px;margin-bottom:8px}}.card small{{color:#667085;line-height:1.4}}
.links a{{margin-right:12px;color:#2457c5}}
</style>
</head>
<body><main>
<h1>Intermediate Hardware Descriptions</h1>
<p>Generated from Graphify spec-code bridge evidence. These pages act as a middle layer so code-only retrieval can infer likely spec anchors.</p>
<div class="links"><a href="../html-views/spec-code-bridge-only.html">Spec-code bridge graph</a><a href="hardware-description-bridge.html">Hardware description bridge graph</a><a href="index.md">Markdown index</a><a href="hardware_descriptions.json">JSON data</a></div>
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
        nodes.append({"id": hd_id, "label": comp, "type": "hardware_description", "count": sum(row["bridge_relations"].values())})
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
body{margin:0;font-family:Arial,Helvetica,sans-serif;background:#f6f7f9;color:#17202a}header{padding:16px 20px;background:#fff;border-bottom:1px solid #d7dde7}h1{margin:0;font-size:22px}canvas{display:block;width:100vw;height:calc(100vh - 62px);background:#fbfaf7}#tip{position:absolute;display:none;background:#fff;border:1px solid #d7dde7;border-radius:6px;padding:8px 10px;box-shadow:0 8px 22px rgba(0,0,0,.14);font-size:12px;max-width:420px}
</style></head><body><header><h1>Spec -> Hardware Description -> Code Bridge</h1></header><canvas id="c"></canvas><div id="tip"></div>
<script>
const data=__PAYLOAD__; const c=document.getElementById('c'), ctx=c.getContext('2d'), tip=document.getElementById('tip');
const nodes=[...new Map(data.nodes.map(n=>[n.id,n])).values()], links=data.links;
const byId=new Map(nodes.map(n=>[n.id,n])); let w=0,h=0;
function color(t){return t==='spec'?'#2f6fed':t==='code'?'#16875f':'#b7791f'}
function layout(){w=c.clientWidth;h=c.clientHeight;c.width=w*devicePixelRatio;c.height=h*devicePixelRatio;ctx.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0);
 const specs=nodes.filter(n=>n.type==='spec'), hds=nodes.filter(n=>n.type==='hardware_description'), codes=nodes.filter(n=>n.type==='code');
 specs.forEach((n,i)=>{n.x=180+(i%4)*88;n.y=50+Math.floor(i/4)*34});
 hds.forEach((n,i)=>{n.x=w/2+(i%3-1)*135;n.y=70+Math.floor(i/3)*64});
 codes.forEach((n,i)=>{n.x=w-420+(i%6)*68;n.y=50+Math.floor(i/6)*30});
 draw();}
function draw(){ctx.clearRect(0,0,w,h);ctx.lineWidth=1;for(const e of links){const a=byId.get(e.source),b=byId.get(e.target);if(!a||!b)continue;ctx.strokeStyle=e.relation==='describes'?'rgba(47,111,237,.22)':'rgba(22,135,95,.22)';ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();}
 for(const n of nodes){const r=n.type==='hardware_description'?10:5;ctx.fillStyle=color(n.type);ctx.beginPath();ctx.arc(n.x,n.y,r,0,Math.PI*2);ctx.fill(); if(n.type==='hardware_description'){ctx.fillStyle='#17202a';ctx.font='12px Arial';ctx.fillText(n.label,n.x+13,n.y+4);}}}
c.addEventListener('mousemove',e=>{const r=c.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top;let hit=null;for(const n of nodes){if(Math.hypot(n.x-x,n.y-y)<12)hit=n} if(!hit){tip.style.display='none';return} tip.style.display='block';tip.style.left=e.clientX-r.left+12+'px';tip.style.top=e.clientY-r.top+12+'px';tip.innerHTML=`<strong>${hit.type}</strong><br>${hit.label}<br>${hit.file||''}`;});
window.addEventListener('resize',layout);layout();
</script></body></html>"""
    html_text = html_text.replace("__PAYLOAD__", payload)
    out.write_text(html_text, encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "blocks").mkdir(parents=True, exist_ok=True)
    data = build()
    for row in data["components"]:
        write_component_md(OUT_DIR / "blocks" / f"{slug(row['component'])}.md", row)
    (OUT_DIR / "hardware_descriptions.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_index_md(OUT_DIR / "index.md", data)
    write_html_index(OUT_DIR / "index.html", data)
    write_bridge_html(OUT_DIR / "hardware-description-bridge.html", data)
    print(
        json.dumps(
            {
                "status": "ok",
                "out_dir": str(OUT_DIR),
                "index_html": str(OUT_DIR / "index.html"),
                "bridge_html": str(OUT_DIR / "hardware-description-bridge.html"),
                "components": data["summary"]["components"],
                "bridge_edges": data["summary"]["total_bridge_edges"],
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
