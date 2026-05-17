#!/usr/bin/env python3
"""Build an ultra-compact single-file OpenKB input from the Graphify spec graph."""

from __future__ import annotations

import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
GRAPH_JSON = REPO_ROOT / "dbs" / "graphify-out" / "spec-only-graphify" / "graph.json"
OUT_ROOT = REPO_ROOT / "dbs" / "graphify-out" / "kb-variants" / "spec-graphify-ultra-minimal" / "kb"
RAW_ROOT = OUT_ROOT / "raw"
OUT_MD = RAW_ROOT / "graphify_ultra_minimal_spec_knowledge.md"
PREVIEW_ROOT = REPO_ROOT / "dbs" / "graphify-out" / "graphify-openkb-bridge"
OUT_HTML = PREVIEW_ROOT / "graphify_ultra_minimal_spec_knowledge.html"
OUT_MANIFEST = PREVIEW_ROOT / "ultra_minimal_manifest.json"


STOP_COMPONENTS = {
    "readme",
    "checklist",
    "opentitan",
    "lowrisc",
    "theory_of_operation",
    "programmers_guide",
    "interfaces",
    "software",
    "documentation",
    "development_stages",
}


def clean(label: str) -> str:
    label = re.sub(r"^(component|topic):", "", label)
    return label.strip()


def good_component(node: dict) -> bool:
    name = clean(node.get("label", "")).lower()
    if name in STOP_COMPONENTS:
        return False
    if len(name) < 3:
        return False
    return True


def refs_for(node_id: str, relation: str, outgoing: dict[str, list[dict]], by_id: dict[str, dict], max_refs: int) -> list[str]:
    refs = []
    seen = set()
    for edge in outgoing.get(node_id, []):
        if edge.get("relation") != relation:
            continue
        target = by_id.get(edge.get("target"))
        if not target:
            continue
        source_file = target.get("source_file", "")
        loc = target.get("source_location", "")
        key = (source_file, loc)
        if key in seen:
            continue
        seen.add(key)
        label = clean(target.get("label", target["id"]))
        refs.append(f"{label} <{source_file}{':' + loc if loc else ''}>")
        if len(refs) >= max_refs:
            break
    return refs


def html_preview(markdown: str) -> str:
    body = (
        markdown.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    body = re.sub(r"^### (.*)$", r"<h3>\1</h3>", body, flags=re.MULTILINE)
    body = re.sub(r"^## (.*)$", r"<h2>\1</h2>", body, flags=re.MULTILINE)
    body = re.sub(r"^# (.*)$", r"<h1>\1</h1>", body, flags=re.MULTILINE)
    body = re.sub(r"^- (.*)$", r"<li>\1</li>", body, flags=re.MULTILINE)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Graphify Ultra Minimal Spec Knowledge</title>
  <style>
    body {{ margin: 0; font-family: Segoe UI, Arial, sans-serif; background: #f7f8fb; color: #17202a; letter-spacing: 0; }}
    main {{ max-width: 980px; margin: 0 auto; padding: 28px; }}
    h1 {{ font-size: 28px; }}
    h2 {{ margin-top: 28px; padding-bottom: 8px; border-bottom: 1px solid #d8dee8; }}
    h3 {{ margin-top: 20px; color: #005f68; }}
    li {{ line-height: 1.55; margin: 4px 0; }}
    code {{ background: #edf2f7; border-radius: 5px; padding: 2px 5px; }}
  </style>
</head>
<body><main>{body}</main></body>
</html>
"""


def main() -> None:
    data = json.loads(GRAPH_JSON.read_text(encoding="utf-8"))
    nodes = data["nodes"]
    links = data["links"]
    by_id = {node["id"]: node for node in nodes}
    outgoing: dict[str, list[dict]] = defaultdict(list)
    degree = Counter()

    for edge in links:
        source = edge.get("source") or edge.get("_src")
        target = edge.get("target") or edge.get("_tgt")
        if not source or not target:
            continue
        outgoing[source].append(edge)
        if edge.get("relation") in {"documents_component", "references_component", "mentions_topic"}:
            degree[source] += 1
            degree[target] += 1

    components = sorted(
        [node for node in nodes if node.get("role") == "component" and good_component(node)],
        key=lambda node: (-degree[node["id"]], node.get("label", "")),
    )[:15]
    topics = sorted(
        [node for node in nodes if node.get("role") == "topic"],
        key=lambda node: (-degree[node["id"]], node.get("label", "")),
    )[:10]
    documents = sorted(
        [node for node in nodes if node.get("role") == "document"],
        key=lambda node: (-degree[node["id"]], node.get("source_file", "")),
    )[:10]

    lines = [
        "# Graphify Ultra Minimal Spec Knowledge",
        "",
        "Single-file OpenKB input compressed from Graphify spec-only graph. Use this as a low-cost curator seed.",
        "",
        "## Graph",
        f"- Nodes: {len(nodes)}",
        f"- Links: {len(links)}",
        "- Keep Graphify ids and source anchors as late-binding keys for code/spec integration.",
        "",
        "## Components",
    ]

    for node in components:
        refs = refs_for(node["id"], "references_component", outgoing, by_id, 2)
        docs = refs_for(node["id"], "documents_component", outgoing, by_id, 1)
        lines.extend(
            [
                f"### {clean(node.get('label', node['id']))}",
                f"- id: `{node['id']}`, community: {node.get('community', 'unknown')}",
                f"- evidence: {'; '.join(refs) if refs else 'none'}",
                f"- source: {'; '.join(docs) if docs else 'none'}",
                "",
            ]
        )

    lines.append("## Topics")
    for node in topics:
        refs = refs_for(node["id"], "mentions_topic", outgoing, by_id, 3)
        lines.extend(
            [
                f"### {clean(node.get('label', node['id']))}",
                f"- id: `{node['id']}`, community: {node.get('community', 'unknown')}",
                f"- anchors: {'; '.join(refs) if refs else 'none'}",
                "",
            ]
        )

    lines.append("## Source Maps")
    for node in documents:
        sections = refs_for(node["id"], "contains", outgoing, by_id, 4)
        lines.extend(
            [
                f"### {node.get('label', node['id'])}",
                f"- id: `{node['id']}`",
                f"- file: `{node.get('source_file', '')}`",
                f"- sections: {'; '.join(sections) if sections else 'none'}",
                "",
            ]
        )

    lines.extend(
        [
            "## OpenKB Rule",
            "- Build compact concept pages only from the anchors above.",
            "- Do not infer detailed requirements unless the referenced source file is consulted.",
        ]
    )
    markdown = "\n".join(lines).rstrip() + "\n"

    if RAW_ROOT.exists():
        shutil.rmtree(RAW_ROOT)
    RAW_ROOT.mkdir(parents=True, exist_ok=True)
    (OUT_ROOT / ".openkb").mkdir(parents=True, exist_ok=True)
    (OUT_ROOT / "wiki").mkdir(parents=True, exist_ok=True)
    (OUT_ROOT / ".openkb" / "config.yaml").write_text(
        "model: gpt-5.4-mini\nlanguage: en\npageindex_threshold: 20\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(markdown, encoding="utf-8")
    PREVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    OUT_HTML.write_text(html_preview(markdown), encoding="utf-8")
    manifest = {
        "source_graph": str(GRAPH_JSON),
        "openkb_kb": str(OUT_ROOT),
        "raw_markdown": str(OUT_MD),
        "html_preview": str(OUT_HTML),
        "files": 1,
        "bytes": OUT_MD.stat().st_size,
        "components": len(components),
        "topics": len(topics),
        "documents": len(documents),
    }
    OUT_MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
