#!/usr/bin/env python3
"""Build a Graphify spec-only knowledge graph from exported spec documents.

This is intentionally deterministic and local-only. Graphify's CLI update path
currently rebuilds code AST graphs, so spec-only document graphs need a small
builder that emits Graphify-compatible nodes/edges and then reuses Graphify's
cluster, report, and export modules.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
GRAPHIFY_ROOT = REPO_ROOT / "tools" / "graphify"
if str(GRAPHIFY_ROOT) not in sys.path:
    sys.path.insert(0, str(GRAPHIFY_ROOT))


DOC_EXTENSIONS = {".adoc", ".hjson", ".html", ".md", ".rst", ".txt"}
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")
RST_UNDERLINE_CHARS = set("=-~^\"'")
HJSON_KEY_RE = re.compile(r"^\s*\"?([A-Za-z_][A-Za-z0-9_.$-]*)\"?\s*:")
IDENT_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_.$-]*")


COMMON_TERMS = {
    "about",
    "access",
    "after",
    "against",
    "all",
    "also",
    "and",
    "are",
    "bit",
    "bits",
    "block",
    "bus",
    "can",
    "case",
    "chapter",
    "code",
    "com",
    "common",
    "config",
    "configuration",
    "control",
    "data",
    "default",
    "description",
    "design",
    "device",
    "doc",
    "docs",
    "during",
    "each",
    "enable",
    "end",
    "example",
    "field",
    "file",
    "files",
    "for",
    "from",
    "guide",
    "has",
    "have",
    "header",
    "index",
    "input",
    "interface",
    "internal",
    "into",
    "list",
    "logic",
    "module",
    "name",
    "not",
    "note",
    "only",
    "open",
    "output",
    "overview",
    "page",
    "param",
    "parameter",
    "register",
    "registers",
    "reset",
    "section",
    "signal",
    "signals",
    "spec",
    "table",
    "test",
    "that",
    "the",
    "this",
    "top",
    "type",
    "used",
    "user",
    "using",
    "value",
    "with",
}


TOPIC_ALIASES = {
    "alert": {"alert", "alerts", "alert_handler"},
    "bus": {"bus", "tlul", "tl-ul", "tilelink"},
    "clock": {"clock", "clocks", "clocking", "clk"},
    "coverage": {"coverage", "covergroup", "coverpoints"},
    "crypto": {"aes", "crypto", "hmac", "keymgr", "sha", "sha2", "kmac"},
    "debug": {"debug", "jtag", "rv_dm"},
    "entropy": {"csrng", "edn", "entropy"},
    "fifo": {"fifo", "queue"},
    "interrupt": {"interrupt", "interrupts", "irq"},
    "lifecycle": {"lc_ctrl", "lifecycle", "life_cycle"},
    "memory": {"flash", "memory", "otp", "ram", "rom", "sram"},
    "power": {"pwrmgr", "power", "sleep", "wakeup"},
    "registers": {"csr", "csrs", "reg", "regs", "register", "registers"},
    "reset": {"reset", "resets", "rst"},
    "security": {"countermeasure", "countermeasures", "security", "secure"},
    "testplan": {"testplan", "test_plan", "verification", "dv"},
}


def make_id(*parts: str) -> str:
    combined = "_".join(p.strip("_.") for p in parts if p)
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", combined)
    return cleaned.strip("_").lower() or "node"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def relpath(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def project_from_rel(rel: str) -> str:
    first = Path(rel).parts[0] if Path(rel).parts else "spec"
    return make_id(first)


def iter_manifest_files(spec_root: Path) -> Iterable[tuple[Path, str | None]]:
    manifest = spec_root / "manifest.csv"
    if not manifest.exists():
        return
    with manifest.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            raw = row.get("copied_to") or row.get("saved_to") or row.get("source")
            if not raw:
                continue
            copied = Path(raw)
            if not copied.is_absolute():
                copied = spec_root / copied
            original = row.get("source") or row.get("original_source")
            yield copied, original


def iter_spec_files(spec_root: Path) -> list[tuple[Path, str | None]]:
    seen: set[Path] = set()
    result: list[tuple[Path, str | None]] = []

    for path, original in iter_manifest_files(spec_root):
        if path.suffix.lower() not in DOC_EXTENSIONS or not path.exists():
            continue
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        result.append((resolved, original))

    if result:
        return sorted(result, key=lambda item: str(item[0]).lower())

    for path in spec_root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in DOC_EXTENSIONS:
            continue
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        result.append((resolved, None))
    return sorted(result, key=lambda item: str(item[0]).lower())


def markdown_headings(lines: list[str]) -> list[tuple[int, str]]:
    headings: list[tuple[int, str]] = []
    for idx, line in enumerate(lines, start=1):
        match = HEADING_RE.match(line)
        if match:
            headings.append((idx, clean_label(match.group(1))))
    return headings


def rst_headings(lines: list[str]) -> list[tuple[int, str]]:
    headings: list[tuple[int, str]] = []
    for idx in range(len(lines) - 1):
        title = lines[idx].strip()
        underline = lines[idx + 1].strip()
        if not title or len(underline) < max(3, len(title) // 2):
            continue
        if len(set(underline)) == 1 and underline[0] in RST_UNDERLINE_CHARS:
            headings.append((idx + 1, clean_label(title)))
    return headings


def hjson_keys(lines: list[str]) -> list[tuple[int, str]]:
    keys: list[tuple[int, str]] = []
    seen: set[str] = set()
    for idx, line in enumerate(lines, start=1):
        match = HJSON_KEY_RE.match(line)
        if not match:
            continue
        key = clean_label(match.group(1))
        key_norm = make_id(key)
        if len(key_norm) < 3 or key_norm in COMMON_TERMS or key_norm in seen:
            continue
        seen.add(key_norm)
        keys.append((idx, key))
    return keys


def extract_sections(path: Path, text: str, max_sections: int) -> list[tuple[int, str]]:
    lines = text.splitlines()
    suffix = path.suffix.lower()
    if suffix in {".md", ".txt", ".adoc"}:
        sections = markdown_headings(lines)
    elif suffix == ".rst":
        sections = rst_headings(lines)
    elif suffix == ".hjson":
        sections = hjson_keys(lines)
    else:
        sections = []

    clean: list[tuple[int, str]] = []
    seen: set[str] = set()
    for line, title in sections:
        title = title[:120].strip()
        key = make_id(title)
        if not title or key in seen:
            continue
        seen.add(key)
        clean.append((line, title))
        if len(clean) >= max_sections:
            break
    return clean


def clean_label(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"[`*_#{}\[\]()]|https?://\S+", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip(" -:\t\r\n")


def term_tokens(*texts: str) -> list[str]:
    tokens: list[str] = []
    for text in texts:
        for raw in IDENT_RE.findall(text):
            token = raw.strip("_.$-").lower().replace("-", "_")
            if len(token) < 3 or token in COMMON_TERMS or token.isdigit():
                continue
            tokens.append(token)
    return tokens


def canonical_topic(token: str) -> str | None:
    lower = token.lower().replace("-", "_")
    for topic, aliases in TOPIC_ALIASES.items():
        if lower in aliases:
            return topic
    return None


def infer_path_components(rel: str) -> set[str]:
    parts = [p.lower() for p in Path(rel).parts]
    components: set[str] = set()
    for idx, part in enumerate(parts):
        if part in {"ip", "ip_templates", "ip_autogen"} and idx + 1 < len(parts):
            components.add(parts[idx + 1])
        if part.startswith("top_") and idx + 2 < len(parts) and parts[idx + 1] in {"ip", "ip_autogen"}:
            components.add(parts[idx + 2])
    stem = Path(rel).stem.lower()
    if stem and stem not in COMMON_TERMS:
        for chunk in re.split(r"[^a-zA-Z0-9_]+", stem):
            if len(chunk) >= 3 and chunk not in COMMON_TERMS:
                components.add(chunk)
    return {make_id(c) for c in components if len(c) >= 3 and c not in COMMON_TERMS}


def add_node(nodes: list[dict], seen: set[str], node: dict) -> None:
    if node["id"] in seen:
        return
    seen.add(node["id"])
    nodes.append(node)


def add_edge(edges: list[dict], seen: set[tuple[str, str, str, str]], edge: dict) -> None:
    key = (
        str(edge.get("source")),
        str(edge.get("target")),
        str(edge.get("relation")),
        str(edge.get("source_file")),
    )
    if key in seen:
        return
    seen.add(key)
    edge.setdefault("_src", edge["source"])
    edge.setdefault("_tgt", edge["target"])
    edge.setdefault("confidence", "EXTRACTED")
    edge.setdefault("confidence_score", 1.0)
    edge.setdefault("weight", 1.0)
    edges.append(edge)


def build_extraction(
    spec_root: Path,
    files: list[tuple[Path, str | None]],
    max_sections_per_doc: int,
    max_topics_per_doc: int,
    max_component_refs_per_doc: int,
) -> tuple[dict, dict]:
    nodes: list[dict] = []
    edges: list[dict] = []
    node_ids: set[str] = set()
    edge_keys: set[tuple[str, str, str, str]] = set()
    stats: dict = {
        "documents": 0,
        "sections": 0,
        "components": 0,
        "topics": 0,
        "total_words": 0,
        "extensions": Counter(),
        "projects": Counter(),
        "relations": Counter(),
        "component_mentions": Counter(),
        "topic_mentions": Counter(),
    }

    def node(
        node_id: str,
        label: str,
        source_file: str,
        source_location: str = "L1",
        role: str = "document",
        original_source: str = "",
        snippet: str = "",
    ) -> None:
        add_node(
            nodes,
            node_ids,
            {
                "id": node_id,
                "label": label,
                "file_type": "document",
                "source_file": source_file,
                "source_location": source_location,
                "confidence_score": 1.0,
                "role": role,
                "original_source": original_source,
                "snippet": snippet,
            },
        )

    def edge(source: str, target: str, relation: str, source_file: str, source_location: str = "L1", weight: float = 1.0) -> None:
        add_edge(
            edges,
            edge_keys,
            {
                "source": source,
                "target": target,
                "relation": relation,
                "confidence": "EXTRACTED",
                "confidence_score": 1.0,
                "source_file": source_file,
                "source_location": source_location,
                "weight": weight,
            },
        )
        stats["relations"][relation] += 1

    corpus_id = "spec_corpus"
    node(corpus_id, "Spec Documents Corpus", "__graphify_spec_only__/index.md", role="corpus")

    known_components = sorted({c for path, _ in files for c in infer_path_components(relpath(path, spec_root))})
    component_source = "__graphify_spec_only__/components.md"
    for component in known_components:
        component_id = "component_" + make_id(component)
        node(component_id, f"component:{component}", component_source, role="component")
    stats["components"] = len(known_components)
    known_component_set = set(known_components)

    for path, original in files:
        rel = relpath(path, spec_root)
        text = read_text(path)
        headings = extract_sections(path, text, max_sections_per_doc)
        project = project_from_rel(rel)
        project_id = "project_" + make_id(project)
        category = Path(rel).parts[1] if len(Path(rel).parts) > 1 else "root"
        category_id = "category_" + make_id(project, category)
        doc_id = "doc_" + make_id(rel)

        stats["documents"] += 1
        stats["extensions"][path.suffix.lower()] += 1
        stats["projects"][project] += 1
        stats["total_words"] += len(re.findall(r"\S+", text))

        node(project_id, f"project:{project}", "__graphify_spec_only__/projects.md", role="project")
        node(category_id, f"{project}/{category}", "__graphify_spec_only__/categories.md", role="category")
        edge(corpus_id, project_id, "contains", "__graphify_spec_only__/index.md")
        edge(project_id, category_id, "contains", "__graphify_spec_only__/projects.md")

        doc_node = {
            "id": doc_id,
            "label": Path(rel).name,
            "file_type": "document",
            "source_file": rel,
            "source_location": "L1",
            "confidence_score": 1.0,
            "role": "document",
            "project": project,
            "original_source": original or "",
            "bytes": path.stat().st_size,
        }
        add_node(nodes, node_ids, doc_node)
        edge(category_id, doc_id, "contains", rel)

        path_components = infer_path_components(rel)
        content_component_hits = [
            component
            for component in known_components
            if component in path_components or re.search(rf"\b{re.escape(component)}\b", text, flags=re.IGNORECASE)
        ][:max_component_refs_per_doc]
        for component in content_component_hits:
            component_id = "component_" + make_id(component)
            edge(doc_id, component_id, "documents_component", rel, weight=1.4)
            stats["component_mentions"][component] += 1

        doc_token_counter = Counter(term_tokens(rel, " ".join(title for _, title in headings)))
        topic_hits: list[str] = []
        for token, _ in doc_token_counter.most_common():
            topic = canonical_topic(token)
            if topic and topic not in topic_hits:
                topic_hits.append(topic)
            if len(topic_hits) >= max_topics_per_doc:
                break

        for topic in topic_hits:
            topic_id = "topic_" + make_id(topic)
            node(topic_id, f"topic:{topic}", "__graphify_spec_only__/topics.md", role="topic")
            edge(doc_id, topic_id, "mentions_topic", rel)
            stats["topic_mentions"][topic] += 1

        lines_list = text.splitlines()
        for line, heading in headings:
            section_id = "section_" + make_id(rel, str(line), heading)
            radius = 8
            start = max(0, line - 1 - radius)
            end = min(len(lines_list), line - 1 + radius)
            snip = "\n".join(lines_list[start:end]).strip()
            node(section_id, heading, rel, f"L{line}", role="section",
                 original_source=str(path), snippet=snip)
            edge(doc_id, section_id, "contains", rel, f"L{line}", weight=1.2)
            stats["sections"] += 1

            section_tokens = set(term_tokens(heading))
            for topic in sorted({canonical_topic(token) for token in section_tokens if canonical_topic(token)}):
                topic_id = "topic_" + make_id(topic)
                node(topic_id, f"topic:{topic}", "__graphify_spec_only__/topics.md", role="topic")
                edge(section_id, topic_id, "mentions_topic", rel, f"L{line}")
                stats["topic_mentions"][topic] += 1

            for component in sorted(path_components & known_component_set):
                component_id = "component_" + make_id(component)
                edge(section_id, component_id, "references_component", rel, f"L{line}", weight=0.8)

    stats["topics"] = len({n["id"] for n in nodes if str(n.get("id", "")).startswith("topic_")})
    extraction = {
        "nodes": nodes,
        "edges": edges,
        "hyperedges": [],
        "input_tokens": 0,
        "output_tokens": 0,
    }
    return extraction, stats


def label_communities(graph, communities: dict[int, list[str]]) -> dict[int, str]:
    labels: dict[int, str] = {}
    degree = dict(graph.degree())
    for cid, members in communities.items():
        scored = sorted(
            members,
            key=lambda node_id: (
                graph.nodes[node_id].get("role") in {"component", "topic", "project", "category"},
                degree.get(node_id, 0),
            ),
            reverse=True,
        )
        picked: list[str] = []
        for node_id in scored:
            label = str(graph.nodes[node_id].get("label", node_id))
            if label.startswith("section_") or not label:
                continue
            picked.append(label)
            if len(picked) >= 3:
                break
        labels[cid] = ", ".join(picked) if picked else f"Community {cid}"
    return labels


def build_outputs(extraction: dict, stats: dict, spec_root: Path, out_dir: Path) -> dict:
    from graphify.analyze import god_nodes, suggest_questions, surprising_connections
    from graphify.build import build_from_json
    from graphify.cluster import cluster, score_all
    from graphify.export import to_graphml, to_html, to_json
    from graphify.report import generate

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / ".graphify_extract.json").write_text(json.dumps(extraction, indent=2), encoding="utf-8")

    graph = build_from_json(extraction)
    communities = cluster(graph)
    cohesion = score_all(graph, communities)
    labels = label_communities(graph, communities)
    questions = suggest_questions(graph, communities, labels)
    surprises = surprising_connections(graph, communities)

    detection = {
        "total_files": stats["documents"],
        "total_words": stats["total_words"],
        "warning": "Spec-only graph built deterministically from exported spec documents; no LLM/OpenKB ingest was run.",
    }
    report = generate(
        graph,
        communities,
        cohesion,
        labels,
        god_nodes(graph),
        surprises,
        detection,
        {"input": 0, "output": 0},
        str(spec_root),
        suggested_questions=questions,
    )

    (out_dir / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    to_json(graph, communities, str(out_dir / "graph.json"), force=True)
    to_graphml(graph, communities, str(out_dir / "graph.graphml"))

    html_status = "written"
    try:
        to_html(graph, communities, str(out_dir / "graph.html"), community_labels=labels)
    except ValueError as exc:
        html_status = f"skipped: {exc}"
        (out_dir / "HTML_SKIPPED.txt").write_text(str(exc) + "\n", encoding="utf-8")

    detect_payload = {
        "root": str(spec_root),
        "total_files": stats["documents"],
        "total_words": stats["total_words"],
        "files": {"documents": stats["documents"], "code": 0, "paper": 0, "image": 0},
        "warning": detection["warning"],
    }
    (out_dir / ".graphify_detect.json").write_text(json.dumps(detect_payload, indent=2), encoding="utf-8")

    def counter_dict(counter: Counter) -> dict:
        return dict(sorted(counter.items(), key=lambda item: (-item[1], item[0])))

    manifest = {
        "status": "ok",
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "spec_root": str(spec_root),
        "out_dir": str(out_dir),
        "graph_json": str(out_dir / "graph.json"),
        "report": str(out_dir / "GRAPH_REPORT.md"),
        "html": html_status,
        "nodes": graph.number_of_nodes(),
        "edges": graph.number_of_edges(),
        "communities": len(communities),
        "documents": stats["documents"],
        "sections": stats["sections"],
        "components": stats["components"],
        "topics": stats["topics"],
        "total_words": stats["total_words"],
        "extensions": counter_dict(stats["extensions"]),
        "projects": counter_dict(stats["projects"]),
        "relations": counter_dict(stats["relations"]),
    }
    manifest["top_components"] = list(counter_dict(stats["component_mentions"]).items())[:20]
    manifest["top_topics"] = list(counter_dict(stats["topic_mentions"]).items())[:20]
    (out_dir / "spec_only_graphify_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    readme = [
        "# Spec-only Graphify KB",
        "",
        f"- Source: `{spec_root}`",
        f"- Graph: `{out_dir / 'graph.json'}`",
        f"- Report: `{out_dir / 'GRAPH_REPORT.md'}`",
        f"- Nodes: {graph.number_of_nodes()}",
        f"- Edges: {graph.number_of_edges()}",
        f"- Communities: {len(communities)}",
        "",
        "This KB is deterministic and spec-only. It does not include RTL/code nodes",
        "and it did not run OpenKB or an LLM ingestion step.",
        "",
        "Query example:",
        "",
        "```powershell",
        f"& {REPO_ROOT / '.venv-graphify' / 'Scripts' / 'graphify.exe'} query \"ibex registers\" --graph {out_dir / 'graph.json'}",
        "```",
    ]
    (out_dir / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec-root", required=True, help="Exported spec_documents_* directory.")
    parser.add_argument("--out-dir", required=True, help="Output directory for Graphify spec-only artifacts.")
    parser.add_argument("--max-sections-per-doc", type=int, default=10)
    parser.add_argument("--max-topics-per-doc", type=int, default=8)
    parser.add_argument("--max-component-refs-per-doc", type=int, default=24)
    args = parser.parse_args()

    spec_root = Path(args.spec_root).resolve()
    out_dir = Path(args.out_dir).resolve()
    if not spec_root.exists():
        raise SystemExit(f"spec root not found: {spec_root}")

    files = iter_spec_files(spec_root)
    if not files:
        raise SystemExit(f"no spec document files found under: {spec_root}")

    extraction, stats = build_extraction(
        spec_root,
        files,
        max_sections_per_doc=args.max_sections_per_doc,
        max_topics_per_doc=args.max_topics_per_doc,
        max_component_refs_per_doc=args.max_component_refs_per_doc,
    )
    manifest = build_outputs(extraction, stats, spec_root, out_dir)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
