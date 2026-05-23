#!/usr/bin/env python3
"""Merge exported spec documents into a Graphify graph.

This is a deterministic, no-LLM pass. It adds document file nodes, section
nodes for Markdown/RST headings, and references from documents to existing
code/module nodes when a module/IP label appears verbatim in the document.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Iterable


COMMON_LABELS = {
    "all",
    "and",
    "api",
    "bit",
    "bus",
    "clk",
    "code",
    "core",
    "data",
    "doc",
    "end",
    "file",
    "for",
    "get",
    "has",
    "id",
    "int",
    "key",
    "log",
    "new",
    "not",
    "out",
    "reg",
    "run",
    "set",
    "test",
    "the",
    "top",
    "use",
    "val",
}

DOC_EXTENSIONS = {".adoc", ".hjson", ".html", ".md", ".rst", ".txt"}
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")
IDENT_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_$]*")


def make_id(*parts: str) -> str:
    combined = "_".join(p.strip("_.") for p in parts if p)
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", combined)
    return cleaned.strip("_").lower()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def rel_source(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path)


def default_backup_roots(root: Path) -> list[Path]:
    parent = root.resolve().parent
    backup_roots: list[Path] = []
    for child in parent.iterdir():
        if not child.is_dir():
            continue
        name = child.name.lower()
        if name == root.name.lower():
            continue
        if ("dbs" in name and ("backup" in name or "bak" in name)) or name in {"dbs backup", "dbs_backup"}:
            backup_roots.append(child)
    return backup_roots


def resolve_source(source: Path, root: Path, backup_roots: list[Path]) -> Path | None:
    if source.exists():
        return source
    try:
        rel = source.resolve().relative_to(root.resolve())
    except ValueError:
        rel = Path(*source.parts[-2:]) if len(source.parts) >= 2 else source.name
    for backup_root in backup_roots:
        candidate = backup_root / rel
        if candidate.exists():
            return candidate
    return None


def iter_manifest_sources(manifest: Path) -> Iterable[Path]:
    with manifest.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            raw = row.get("source") or row.get("original_source") or row.get("saved_to")
            if raw:
                yield Path(raw)


def markdown_headings(lines: list[str]) -> list[tuple[int, str]]:
    headings: list[tuple[int, str]] = []
    for idx, line in enumerate(lines, start=1):
        match = HEADING_RE.match(line)
        if match:
            headings.append((idx, match.group(1).strip(" #")))
    return headings


def rst_headings(lines: list[str]) -> list[tuple[int, str]]:
    headings: list[tuple[int, str]] = []
    underline_chars = set("=-~^\"'")
    for idx in range(len(lines) - 1):
        title = lines[idx].strip()
        underline = lines[idx + 1].strip()
        if not title or len(underline) < max(3, len(title) // 2):
            continue
        if len(set(underline)) == 1 and underline[0] in underline_chars:
            headings.append((idx + 1, title))
    return headings


def extract_headings(path: Path, text: str) -> list[tuple[int, str]]:
    lines = text.splitlines()
    if path.suffix.lower() in {".md", ".txt", ".adoc"}:
        return markdown_headings(lines)[:25]
    if path.suffix.lower() == ".rst":
        return rst_headings(lines)[:25]
    return []


def code_label_index(nodes: list[dict], links: list[dict]) -> dict[str, list[str]]:
    defined_targets = {edge.get("target") for edge in links if edge.get("relation") == "defines"}
    index: dict[str, list[str]] = {}
    for node in nodes:
        label = str(node.get("label") or "")
        if not label or node.get("id") not in defined_targets:
            continue
        lower = label.lower()
        if len(lower) < 3 or lower in COMMON_LABELS:
            continue
        if not re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_$]*", label):
            continue
        index.setdefault(lower, []).append(str(node["id"]))
    return index


def add_node(nodes: list[dict], seen: set[str], node: dict) -> None:
    if node["id"] in seen:
        return
    seen.add(node["id"])
    nodes.append(node)


def add_edge(links: list[dict], seen: set[tuple[str, str, str, str]], edge: dict) -> None:
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
    links.append(edge)


def rebuild_report(graph_path: Path, root: Path) -> None:
    from graphify.analyze import god_nodes, suggest_questions, surprising_connections
    from graphify.build import build_from_json
    from graphify.cluster import cluster, score_all
    from graphify.export import to_json
    from graphify.report import generate

    raw = json.loads(graph_path.read_text(encoding="utf-8"))
    graph = build_from_json(raw)
    communities = cluster(graph)
    cohesion = score_all(graph, communities)
    labels = {cid: f"Community {cid}" for cid in communities}
    questions = suggest_questions(graph, communities, labels)
    report = generate(
        graph,
        communities,
        cohesion,
        labels,
        god_nodes(graph),
        surprising_connections(graph, communities),
        {
            "total_files": len({n.get("source_file") for n in raw.get("nodes", []) if n.get("source_file")}),
            "total_words": 0,
            "warning": "Spec docs merged deterministically; semantic LLM extraction not run.",
        },
        {"input": 0, "output": 0},
        str(root),
        suggested_questions=questions,
    )
    (graph_path.parent / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    to_json(graph, communities, str(graph_path))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--root", required=True)
    parser.add_argument(
        "--allow-spec-documents",
        action="store_true",
        help="Allow manifests from out/spec_documents_*; disabled by default to avoid broad exports.",
    )
    parser.add_argument(
        "--backup-root",
        action="append",
        default=[],
        help="Fallback dbs backup root. Can be passed more than once.",
    )
    parser.add_argument("--max-refs-per-doc", type=int, default=40)
    parser.add_argument("--rebuild-report", action="store_true")
    args = parser.parse_args()

    graph_path = Path(args.graph)
    manifest = Path(args.manifest)
    root = Path(args.root)
    if "spec_documents" in str(manifest).lower() and not args.allow_spec_documents:
        raise SystemExit(
            "Refusing spec_documents manifest by default. Use a narrower manifest "
            "such as related_hdd_documents_clean, or pass --allow-spec-documents explicitly."
        )
    backup_roots = [Path(p) for p in args.backup_root] or default_backup_roots(root)
    raw = json.loads(graph_path.read_text(encoding="utf-8"))

    nodes = raw.setdefault("nodes", [])
    links = raw.setdefault("links", [])
    node_ids = {str(node.get("id")) for node in nodes}
    edge_keys = {
        (str(edge.get("source")), str(edge.get("target")), str(edge.get("relation")), str(edge.get("source_file")))
        for edge in links
    }
    labels = code_label_index(nodes, links)

    files_seen: set[Path] = set()
    doc_count = 0
    backup_doc_count = 0
    missing_count = 0
    section_count = 0
    reference_count = 0

    for source in iter_manifest_sources(manifest):
        resolved_source = resolve_source(source, root, backup_roots)
        if resolved_source is None:
            missing_count += 1
            continue
        if resolved_source.suffix.lower() not in DOC_EXTENSIONS:
            continue
        resolved = resolved_source.resolve()
        if resolved in files_seen:
            continue
        files_seen.add(resolved)

        text = read_text(resolved)
        rel = rel_source(resolved, root)
        doc_id = "doc_" + make_id(rel)
        add_node(
            nodes,
            node_ids,
            {
                "id": doc_id,
                "label": source.name,
                "file_type": "document",
                "source_file": rel,
                "source_location": "L1",
                "confidence_score": 1.0,
            },
        )
        doc_count += 1
        if not source.exists():
            backup_doc_count += 1

        for line, heading in extract_headings(resolved, text):
            heading_id = "section_" + make_id(rel, heading)
            add_node(
                nodes,
                node_ids,
                {
                    "id": heading_id,
                    "label": heading,
                    "file_type": "document",
                    "source_file": rel,
                    "source_location": f"L{line}",
                    "confidence_score": 1.0,
                },
            )
            add_edge(
                links,
                edge_keys,
                {
                    "source": doc_id,
                    "target": heading_id,
                    "relation": "contains",
                    "confidence": "EXTRACTED",
                    "confidence_score": 1.0,
                    "source_file": rel,
                    "source_location": f"L{line}",
                    "weight": 1.0,
                },
            )
            section_count += 1

        matched: set[str] = set()
        for token in IDENT_RE.findall(text):
            lower = token.lower()
            if lower in labels:
                matched.add(lower)
            if len(matched) >= args.max_refs_per_doc:
                break

        for lower in sorted(matched):
            for target in labels[lower][:3]:
                add_edge(
                    links,
                    edge_keys,
                    {
                        "source": doc_id,
                        "target": target,
                        "relation": "references",
                        "confidence": "EXTRACTED",
                        "confidence_score": 1.0,
                        "source_file": rel,
                        "source_location": "L1",
                        "weight": 1.0,
                    },
                )
                reference_count += 1

    graph_path.write_text(json.dumps(raw, ensure_ascii=False), encoding="utf-8")
    if args.rebuild_report:
        rebuild_report(graph_path, root)

    print(
        json.dumps(
            {
                "status": "ok",
                "documents": doc_count,
                "backup_documents": backup_doc_count,
                "missing_sources": missing_count,
                "sections": section_count,
                "references": reference_count,
                "backup_roots": [str(p) for p in backup_roots],
                "graph": str(graph_path),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
