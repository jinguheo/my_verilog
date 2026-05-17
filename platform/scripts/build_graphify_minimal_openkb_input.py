#!/usr/bin/env python3
"""Build a single-file, minimal Graphify-derived OpenKB input document."""

from __future__ import annotations

import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
GRAPH_JSON = REPO_ROOT / "dbs" / "graphify-out" / "spec-only-graphify" / "graph.json"
OUT_ROOT = REPO_ROOT / "dbs" / "graphify-out" / "kb-variants" / "spec-graphify-minimal" / "kb"
RAW_ROOT = OUT_ROOT / "raw"
OUT_MD = RAW_ROOT / "graphify_minimal_spec_knowledge.md"
PREVIEW_ROOT = REPO_ROOT / "dbs" / "graphify-out" / "graphify-openkb-bridge"
OUT_HTML = PREVIEW_ROOT / "graphify_minimal_spec_knowledge.html"
OUT_MANIFEST = PREVIEW_ROOT / "minimal_manifest.json"


def clean(label: str) -> str:
    label = re.sub(r"^(component|topic):", "", label)
    return label.strip()


def limit(items: list[str], n: int) -> list[str]:
    return items[:n] + ([f"... {len(items) - n} more"] if len(items) > n else [])


def main() -> None:
    data = json.loads(GRAPH_JSON.read_text(encoding="utf-8"))
    nodes = data["nodes"]
    links = data["links"]
    by_id = {node["id"]: node for node in nodes}
    incoming: dict[str, list[dict]] = defaultdict(list)
    outgoing: dict[str, list[dict]] = defaultdict(list)
    degree = Counter()

    for edge in links:
        source = edge.get("source") or edge.get("_src")
        target = edge.get("target") or edge.get("_tgt")
        if not source or not target:
            continue
        incoming[target].append(edge)
        outgoing[source].append(edge)
        if edge.get("relation") in {"documents_component", "references_component", "mentions_topic"}:
            degree[source] += 1
            degree[target] += 1

    components = sorted(
        [node for node in nodes if node.get("role") == "component"],
        key=lambda node: (-degree[node["id"]], node.get("label", "")),
    )[:30]
    topics = sorted(
        [node for node in nodes if node.get("role") == "topic"],
        key=lambda node: (-degree[node["id"]], node.get("label", "")),
    )
    documents = sorted(
        [node for node in nodes if node.get("role") == "document"],
        key=lambda node: (-degree[node["id"]], node.get("source_file", "")),
    )[:20]

    def section_refs(source_id: str, relation: str) -> list[str]:
        refs = []
        for edge in outgoing.get(source_id, []):
            if edge.get("relation") != relation:
                continue
            target = by_id.get(edge.get("target"))
            if not target:
                continue
            label = clean(target.get("label", target["id"]))
            source_file = target.get("source_file", "")
            loc = target.get("source_location", "")
            refs.append(f"{label} [{source_file}{':' + loc if loc else ''}]")
        return refs

    lines = [
        "# Graphify Minimal Spec Knowledge",
        "",
        "This is a single-file, low-token OpenKB input generated from the spec-only Graphify graph.",
        "It is intentionally compact: use it as a curated bridge, not as a replacement for raw source truth.",
        "",
        "## Source Graph",
        f"- Source graph: `{GRAPH_JSON}`",
        f"- Nodes: {len(nodes)}",
        f"- Links: {len(links)}",
        "- Export strategy: top graph entities only, preserving source anchors and Graphify ids.",
        "",
        "## Top Components",
    ]

    for component in components:
        name = clean(component.get("label", component["id"]))
        refs = section_refs(component["id"], "references_component")
        docs = section_refs(component["id"], "documents_component")
        lines.extend(
            [
                f"### Component: {name}",
                f"- Graphify id: `{component['id']}`",
                f"- Community: {component.get('community', 'unknown')}",
                f"- Evidence sections: {'; '.join(limit(refs, 4)) if refs else 'None in compact export'}",
                f"- Evidence documents: {'; '.join(limit(docs, 3)) if docs else 'None in compact export'}",
                "",
            ]
        )

    lines.append("## Topics")
    for topic in topics:
        name = clean(topic.get("label", topic["id"]))
        refs = section_refs(topic["id"], "mentions_topic")
        lines.extend(
            [
                f"### Topic: {name}",
                f"- Graphify id: `{topic['id']}`",
                f"- Community: {topic.get('community', 'unknown')}",
                f"- Mentioning sections: {'; '.join(limit(refs, 6)) if refs else 'None in compact export'}",
                "",
            ]
        )

    lines.append("## High-Value Source Documents")
    for document in documents:
        child_sections = []
        for edge in outgoing.get(document["id"], []):
            if edge.get("relation") != "contains":
                continue
            child = by_id.get(edge.get("target"))
            if child:
                child_sections.append(clean(child.get("label", child["id"])))
        lines.extend(
            [
                f"### Document: {document.get('label', document['id'])}",
                f"- Graphify id: `{document['id']}`",
                f"- Source file: `{document.get('source_file', '')}`",
                f"- Original source: `{document.get('original_source', '')}`",
                f"- Community: {document.get('community', 'unknown')}",
                f"- Sections: {'; '.join(limit(child_sections, 8)) if child_sections else 'None recorded'}",
                "",
            ]
        )

    lines.extend(
        [
            "## OpenKB Instructions",
            "- Build concept pages from this compact graph-derived input.",
            "- Preserve Graphify ids, exact component names, source paths, and source locations.",
            "- If a question needs detailed wording, route back to the original source file rather than inventing details.",
            "- Prefer component/topic/source anchors as late-binding keys for code KG integration.",
        ]
    )

    if RAW_ROOT.exists():
        shutil.rmtree(RAW_ROOT)
    RAW_ROOT.mkdir(parents=True, exist_ok=True)
    (OUT_ROOT / ".openkb").mkdir(parents=True, exist_ok=True)
    (OUT_ROOT / "wiki").mkdir(parents=True, exist_ok=True)
    (OUT_ROOT / ".openkb" / "config.yaml").write_text(
        "model: gpt-5.4-mini\nlanguage: en\npageindex_threshold: 20\n",
        encoding="utf-8",
    )
    OUT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    preview = OUT_MD.read_text(encoding="utf-8")
    html_body = (
        preview.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    html_body = re.sub(r"^### (.*)$", r"<h3>\1</h3>", html_body, flags=re.MULTILINE)
    html_body = re.sub(r"^## (.*)$", r"<h2>\1</h2>", html_body, flags=re.MULTILINE)
    html_body = re.sub(r"^# (.*)$", r"<h1>\1</h1>", html_body, flags=re.MULTILINE)
    html_body = re.sub(r"^- (.*)$", r"<li>\1</li>", html_body, flags=re.MULTILINE)
    html_body = html_body.replace("\n\n", "\n")
    PREVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    OUT_HTML.write_text(
        f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Graphify Minimal Spec Knowledge</title>
  <style>
    body {{ margin: 0; font-family: Segoe UI, Arial, sans-serif; background: #f7f8fb; color: #17202a; letter-spacing: 0; }}
    main {{ max-width: 1040px; margin: 0 auto; padding: 28px; }}
    h1 {{ font-size: 28px; }}
    h2 {{ margin-top: 30px; padding-bottom: 8px; border-bottom: 1px solid #d8dee8; }}
    h3 {{ margin-top: 22px; color: #005f68; }}
    li {{ line-height: 1.55; margin: 4px 0; }}
    code {{ background: #edf2f7; border-radius: 5px; padding: 2px 5px; }}
  </style>
</head>
<body><main>{html_body}</main></body>
</html>
""",
        encoding="utf-8",
    )

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
