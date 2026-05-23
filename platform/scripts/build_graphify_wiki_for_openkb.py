#!/usr/bin/env python3
"""Build a compact Graphify-derived spec wiki that can be used as OpenKB input."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_GRAPH = REPO_ROOT / "dbs" / "graphify-out" / "spec-only-graphify" / "graph.json"
_DEFAULT_OUT   = REPO_ROOT / "dbs" / "graphify-out" / "kb-variants" / "spec-graphify-wiki" / "kb"

# resolved at runtime via _parse_args()
GRAPH_JSON: Path
OUT_ROOT: Path
RAW_ROOT: Path
WIKI_EXPORT: Path
HTML_OUT: Path


def _parse_args() -> None:
    global GRAPH_JSON, OUT_ROOT, RAW_ROOT, WIKI_EXPORT, HTML_OUT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph", type=Path, default=_DEFAULT_GRAPH,
                        help="Path to graph.json (default: spec-only-graphify/graph.json)")
    parser.add_argument("--out", type=Path, default=_DEFAULT_OUT,
                        help="Output OpenKB kb root directory")
    args = parser.parse_args()
    GRAPH_JSON = args.graph
    OUT_ROOT   = args.out
    RAW_ROOT   = OUT_ROOT / "raw"
    WIKI_EXPORT = OUT_ROOT.parent / "html-preview"
    HTML_OUT    = WIKI_EXPORT / "graphify_derived_wiki.html"


def slug(text: str) -> str:
    text = text.lower()
    text = re.sub(r"^component:", "", text)
    text = re.sub(r"^topic:", "", text)
    text = re.sub(r"[^a-z0-9_./-]+", "-", text)
    text = text.strip("-").replace("/", "_").replace(".", "_")
    return text or "item"


def clean_label(label: str) -> str:
    return re.sub(r"^(component|topic):", "", label).replace("_", " ").strip()


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_graph() -> tuple[list[dict], list[dict]]:
    data = json.loads(GRAPH_JSON.read_text(encoding="utf-8"))
    return data["nodes"], data["links"]


def build_indexes(nodes: list[dict], links: list[dict]) -> tuple[dict[str, dict], dict[str, list[dict]], dict[str, list[dict]]]:
    by_id = {node["id"]: node for node in nodes}
    outgoing: dict[str, list[dict]] = defaultdict(list)
    incoming: dict[str, list[dict]] = defaultdict(list)
    for edge in links:
        source = edge.get("source") or edge.get("_src")
        target = edge.get("target") or edge.get("_tgt")
        if not source or not target:
            continue
        outgoing[source].append(edge)
        incoming[target].append(edge)
    return by_id, outgoing, incoming


def linked_nodes(node_id: str, relation: str, edges: list[dict], by_id: dict[str, dict], reverse: bool = False) -> list[dict]:
    found = []
    seen = set()
    for edge in edges:
        if edge.get("relation") != relation:
            continue
        other_id = edge.get("source") if reverse else edge.get("target")
        if other_id in by_id and other_id not in seen:
            found.append(by_id[other_id])
            seen.add(other_id)
    return found


def bullet_nodes(nodes: list[dict], limit: int = 12) -> str:
    if not nodes:
        return "- None recorded in the Graphify spec graph."
    lines = []
    for node in nodes[:limit]:
        label = clean_label(node.get("label", node["id"]))
        source = node.get("source_file", "")
        loc = node.get("source_location", "")
        suffix = f" ({source}{':' + loc if loc else ''})" if source else ""
        lines.append(f"- {label}{suffix}")
    if len(nodes) > limit:
        lines.append(f"- ... {len(nodes) - limit} more")
    return "\n".join(lines)


def make_component_page(component: dict, incoming: dict[str, list[dict]], by_id: dict[str, dict]) -> str:
    node_id = component["id"]
    label = clean_label(component.get("label", node_id))
    inbound = incoming.get(node_id, [])
    docs = linked_nodes(node_id, "documents_component", inbound, by_id, reverse=True)
    sections = linked_nodes(node_id, "references_component", inbound, by_id, reverse=True)
    community = component.get("community", "unknown")
    return f"""# Component: {label}

## OpenKB Purpose
This page is a compact Graphify-derived view of a spec/code entity candidate. It is intended as lower-token OpenKB input, not as raw source truth.

## Graphify Identity
- Node id: `{node_id}`
- Role: `{component.get("role", "")}`
- Community: `{community}`
- Confidence score: `{component.get("confidence_score", "")}`

## Referencing Documents
{bullet_nodes(docs, limit=10)}

## Referencing Sections
{bullet_nodes(sections, limit=18)}

## OpenKB Curation Hints
- Treat this as a component/entity anchor.
- Preserve exact names and source paths.
- Use linked sections as evidence for requirements, verification topics, and integration constraints.
"""


def make_topic_page(topic: dict, incoming: dict[str, list[dict]], by_id: dict[str, dict]) -> str:
    node_id = topic["id"]
    label = clean_label(topic.get("label", node_id))
    sections = linked_nodes(node_id, "mentions_topic", incoming.get(node_id, []), by_id, reverse=True)
    return f"""# Topic: {label}

## OpenKB Purpose
This page summarizes a Graphify topic cluster extracted from the spec graph.

## Graphify Identity
- Node id: `{node_id}`
- Community: `{topic.get("community", "unknown")}`

## Mentioning Sections
{bullet_nodes(sections, limit=24)}

## OpenKB Curation Hints
- Convert repeated section references into a stable concept page.
- Keep source paths as traceability anchors.
"""


def make_document_page(document: dict, outgoing: dict[str, list[dict]], by_id: dict[str, dict]) -> str:
    node_id = document["id"]
    label = document.get("label", node_id)
    children = []
    for edge in outgoing.get(node_id, []):
        if edge.get("relation") == "contains":
            target = by_id.get(edge.get("target"))
            if target:
                children.append(target)
    return f"""# Document: {label}

## Source
- Graphify source file: `{document.get("source_file", "")}`
- Original source: `{document.get("original_source", "")}`
- Project: `{document.get("project", "")}`
- Bytes: `{document.get("bytes", "")}`
- Community: `{document.get("community", "unknown")}`

## Sections
{bullet_nodes(children, limit=30)}

## OpenKB Curation Hints
- This page is a source map, not a prose summary.
- Use sections as anchors back to the raw specification corpus.
"""


def render_html(markdown_files: list[Path]) -> str:
    rows = []
    for path in markdown_files:
        rel = path.relative_to(RAW_ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        first = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), path.stem)
        preview = " ".join(line.strip("#- ` ") for line in text.splitlines()[1:8] if line.strip())[:280]
        rows.append((rel, first, preview))
    cards = "\n".join(
        f"<article><h2>{escape(title)}</h2><p>{escape(preview)}</p><code>{escape(rel)}</code></article>"
        for rel, title, preview in rows
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Graphify-derived OpenKB Input Wiki</title>
  <style>
    body {{ margin: 0; font-family: Segoe UI, Arial, sans-serif; background: #f6f8fb; color: #17202a; letter-spacing: 0; }}
    header {{ padding: 28px clamp(18px, 4vw, 52px); background: #ffffff; border-bottom: 1px solid #d7dee8; }}
    main {{ padding: 24px clamp(18px, 4vw, 52px); display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; }}
    h1 {{ margin: 0 0 8px; font-size: 26px; }}
    p {{ line-height: 1.55; color: #4e5b6a; }}
    article {{ background: #ffffff; border: 1px solid #d7dee8; border-radius: 8px; padding: 16px; }}
    h2 {{ font-size: 17px; margin: 0 0 8px; }}
    code {{ display: block; overflow-wrap: anywhere; background: #eef3f7; padding: 8px; border-radius: 6px; color: #234; }}
  </style>
</head>
<body>
  <header>
    <h1>Graphify-derived OpenKB Input Wiki</h1>
    <p>Compact Markdown pages generated from the spec-only Graphify graph. These pages are intended as lower-token OpenKB raw input.</p>
  </header>
  <main>{cards}</main>
</body>
</html>
"""


def escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def main() -> None:
    _parse_args()
    nodes, links = load_graph()
    by_id, outgoing, incoming = build_indexes(nodes, links)

    components = [node for node in nodes if node.get("role") == "component"]
    topics = [node for node in nodes if node.get("role") == "topic"]
    documents = [node for node in nodes if node.get("role") == "document"]

    degree = Counter()
    for edge in links:
        if edge.get("relation") in {"documents_component", "references_component", "mentions_topic"}:
            degree[edge.get("target")] += 1
            degree[edge.get("source")] += 1

    top_components = sorted(components, key=lambda n: (-degree[n["id"]], n.get("label", "")))[:60]
    top_documents = sorted(documents, key=lambda n: (-degree[n["id"]], n.get("source_file", "")))[:30]

    if RAW_ROOT.exists():
        shutil.rmtree(RAW_ROOT)
    RAW_ROOT.mkdir(parents=True, exist_ok=True)
    (OUT_ROOT / ".openkb").mkdir(parents=True, exist_ok=True)
    (OUT_ROOT / "wiki").mkdir(parents=True, exist_ok=True)
    write(OUT_ROOT / ".openkb" / "config.yaml", "model: gpt-5.4-mini\nlanguage: en\npageindex_threshold: 20\n")

    index_lines = [
        "# Graphify-derived Spec Wiki",
        "",
        "This compact wiki was generated from `spec-only-graphify/graph.json` and is intended as low-token OpenKB input.",
        "",
        "## Counts",
        f"- Source graph nodes: {len(nodes)}",
        f"- Source graph links: {len(links)}",
        f"- Exported component pages: {len(top_components)}",
        f"- Exported topic pages: {len(topics)}",
        f"- Exported document map pages: {len(top_documents)}",
        "",
        "## Strategy",
        "- Keep exact Graphify node ids, component names, source files, and section anchors.",
        "- Use OpenKB only as a curator over this compact graph-derived wiki.",
        "- Avoid sending the full raw spec corpus unless a topic needs deeper evidence.",
    ]
    write(RAW_ROOT / "00_graphify_spec_wiki_index.md", "\n".join(index_lines))

    for component in top_components:
        write(RAW_ROOT / "components" / f"{slug(component.get('label', component['id']))}.md", make_component_page(component, incoming, by_id))
    for topic in sorted(topics, key=lambda n: n.get("label", "")):
        write(RAW_ROOT / "topics" / f"{slug(topic.get('label', topic['id']))}.md", make_topic_page(topic, incoming, by_id))
    for document in top_documents:
        source_slug = slug(document.get("source_file", document["id"]))
        write(RAW_ROOT / "documents" / f"{source_slug}.md", make_document_page(document, outgoing, by_id))

    files = sorted(RAW_ROOT.rglob("*.md"))
    WIKI_EXPORT.mkdir(parents=True, exist_ok=True)
    HTML_OUT.write_text(render_html(files), encoding="utf-8")
    manifest = {
        "source_graph": str(GRAPH_JSON),
        "openkb_kb": str(OUT_ROOT),
        "raw_dir": str(RAW_ROOT),
        "html_preview": str(HTML_OUT),
        "pages": len(files),
        "components": len(top_components),
        "topics": len(topics),
        "documents": len(top_documents),
    }
    write(WIKI_EXPORT / "manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False))
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
