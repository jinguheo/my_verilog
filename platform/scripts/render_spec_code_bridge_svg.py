#!/usr/bin/env python3
"""Render a static SVG overview of the spec-code bridge-only graph."""

from __future__ import annotations

import html
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
BRIDGE_JSON = ROOT / "dbs" / "graphify-out" / "html-views" / "spec-code-bridge-only.json"
OUT_SVG = ROOT / "dbs" / "graphify-out" / "html-views" / "spec-code-bridge-only-overview.svg"


def esc(value: Any) -> str:
    return html.escape(str(value or ""), quote=True)


def main() -> None:
    data = json.loads(BRIDGE_JSON.read_text(encoding="utf-8"))
    nodes = {node["id"]: node for node in data["nodes"]}
    links = data["links"]
    top_components = [row["component"] for row in data["summary"]["top_components"][:16]]
    component_links: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for edge in links:
        if edge.get("component") in top_components:
            component_links[edge["component"]].append(edge)

    width, height = 1800, 1100
    center_x, center_y = width / 2, height / 2 + 30
    ring_r = 390
    component_pos: dict[str, tuple[float, float]] = {}
    for idx, component in enumerate(top_components):
        angle = -math.pi / 2 + (math.tau * idx / len(top_components))
        component_pos[component] = (center_x + math.cos(angle) * ring_r, center_y + math.sin(angle) * ring_r)

    bridge_degree = Counter()
    for edge in links:
        bridge_degree[edge["source"]] += 1
        bridge_degree[edge["target"]] += 1

    parts: list[str] = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1100" viewBox="0 0 1800 1100">',
        "<defs>",
        '<style><![CDATA[text{font-family:Arial,Helvetica,sans-serif}.title{font-size:34px;font-weight:700;fill:#17202a}.sub{font-size:18px;fill:#667085}.label{font-size:15px;fill:#17202a}.small{font-size:12px;fill:#667085}.component{font-size:18px;font-weight:700;fill:#17202a}.edge{stroke:#b7791f;stroke-opacity:.18;stroke-width:1.1}.edge-strong{stroke:#b7791f;stroke-opacity:.42;stroke-width:2}.spec{fill:#2f6fed}.code{fill:#16875f}.hub{fill:#fff;stroke:#17202a;stroke-width:1.5}.card{fill:#fff;stroke:#d7dde7;stroke-width:1}.muted{fill:#eef2f7}]]></style>',
        '<filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#17202a" flood-opacity=".14"/></filter>',
        "</defs>",
        '<rect width="1800" height="1100" fill="#f6f7f9"/>',
        '<text x="70" y="70" class="title">Spec-Code Bridge-Only Graph</text>',
        f'<text x="70" y="104" class="sub">Only relationships that require both spec and code graphs: {data["summary"]["total_bridge_links"]:,} bridge links total, {data["summary"]["displayed_bridge_links"]:,} shown in HTML view</text>',
        '<g transform="translate(70,140)">',
        '<rect class="card" width="410" height="116" rx="8" filter="url(#shadow)"/>',
        '<circle cx="34" cy="38" r="10" class="spec"/><text x="54" y="43" class="label">Spec document / component node</text>',
        '<circle cx="34" cy="72" r="10" class="code"/><text x="54" y="77" class="label">Code module / file node</text>',
        '<line x1="24" y1="98" x2="44" y2="98" class="edge-strong"/><text x="54" y="103" class="label">Bridge edge visible only in spec-code</text>',
        "</g>",
    ]

    # Draw central hub and component spokes.
    parts += [
        f'<circle cx="{center_x:.1f}" cy="{center_y:.1f}" r="92" class="hub" filter="url(#shadow)"/>',
        f'<text x="{center_x:.1f}" y="{center_y - 8:.1f}" text-anchor="middle" class="component">spec-code</text>',
        f'<text x="{center_x:.1f}" y="{center_y + 20:.1f}" text-anchor="middle" class="small">bridge-only view</text>',
    ]
    for component, (x, y) in component_pos.items():
        count = len(component_links[component])
        parts.append(f'<line x1="{center_x:.1f}" y1="{center_y:.1f}" x2="{x:.1f}" y2="{y:.1f}" class="edge-strong"/>')
        radius = 35 + min(26, math.sqrt(count) * 1.8)
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius:.1f}" class="hub" filter="url(#shadow)"/>')
        parts.append(f'<text x="{x:.1f}" y="{y - 4:.1f}" text-anchor="middle" class="component">{esc(component)[:22]}</text>')
        parts.append(f'<text x="{x:.1f}" y="{y + 20:.1f}" text-anchor="middle" class="small">{count} bridge edges</text>')

    # For each component, draw a few spec/code pairs around the component node.
    for component, edges in component_links.items():
        cx, cy = component_pos[component]
        sample_edges = sorted(
            edges,
            key=lambda e: -(bridge_degree[e["source"]] + bridge_degree[e["target"]]),
        )[:10]
        for idx, edge in enumerate(sample_edges):
            angle = -math.pi * 0.72 + (math.pi * 1.44 * idx / max(1, len(sample_edges) - 1))
            spec_node = nodes[edge["source"]]
            code_node = nodes[edge["target"]]
            if spec_node.get("file_type") != "document":
                spec_node, code_node = code_node, spec_node
            sx = cx + math.cos(angle) * 118
            sy = cy + math.sin(angle) * 80
            tx = cx + math.cos(angle) * 175
            ty = cy + math.sin(angle) * 120
            parts.append(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" class="edge"/>')
            parts.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="6" class="spec"/>')
            parts.append(f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="6" class="code"/>')

    # Summary cards.
    rels = data["summary"]["relations"]
    parts += [
        '<g transform="translate(1310,140)">',
        '<rect class="card" width="410" height="205" rx="8" filter="url(#shadow)"/>',
        '<text x="22" y="38" class="component">Bridge relation counts</text>',
    ]
    y = 76
    for rel in rels:
        parts.append(f'<text x="22" y="{y}" class="label">{esc(rel["name"])}</text>')
        parts.append(f'<text x="370" y="{y}" text-anchor="end" class="label">{rel["count"]:,}</text>')
        y += 32
    parts += [
        '<text x="22" y="170" class="small">These edges do not exist in code-only or spec-only views</text>',
        "</g>",
        '<g transform="translate(70,930)">',
        '<rect class="card" width="1660" height="105" rx="8" filter="url(#shadow)"/>',
        '<text x="24" y="38" class="component">What this picture means</text>',
        '<text x="24" y="68" class="label">Blue dots are spec-side anchors, green dots are code-side artifacts, and brown lines are late-binding bridge relations.</text>',
        '<text x="24" y="92" class="small">This graph intentionally hides normal code-code and spec-spec edges so only spec-code-only information remains visible.</text>',
        "</g>",
        "</svg>",
    ]
    OUT_SVG.write_text("\n".join(parts), encoding="utf-8")
    print(json.dumps({"status": "ok", "svg": str(OUT_SVG)}, indent=2))


if __name__ == "__main__":
    main()
