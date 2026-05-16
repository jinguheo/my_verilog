#!/usr/bin/env python3
"""Build OpenKB-ready KB variants from spec docs and the current code graph.

Variants:
- spec-only: normalized spec documents only
- code-only: current Graphify code graph artifacts only
- spec-code: both normalized spec documents and code graph artifacts

This script prepares OpenKB workspaces without invoking the LLM-backed
``openkb add`` command by default.  The raw corpus is normalized to Markdown so
OpenKB can ingest it later once an LLM API key is available.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SPEC_ROOT = ROOT / "out" / "spec_documents_20260514_204108"
DEFAULT_GRAPH_ROOT = ROOT / "dbs" / "graphify-out"
DEFAULT_OUT_ROOT = DEFAULT_GRAPH_ROOT / "kb-variants"
DEFAULT_GRAPH = DEFAULT_GRAPH_ROOT / "graph.json"
TEXT_EXTENSIONS = {".md", ".rst", ".hjson", ".txt"}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def slugify(text: str, max_len: int = 80) -> str:
    stem = re.sub(r"[^A-Za-z0-9._-]+", "_", text).strip("._-")
    stem = re.sub(r"_+", "_", stem)
    return (stem or "item")[:max_len]


def load_agents_md() -> str:
    schema = ROOT / "tools" / "OpenKB" / "openkb" / "schema.py"
    fallback = "# Wiki Schema\n\nMaintain sources, summaries, concepts, explorations, and reports.\n"
    if not schema.exists():
        return fallback
    text = schema.read_text(encoding="utf-8", errors="replace")
    marker = 'AGENTS_MD = """'
    start = text.find(marker)
    if start < 0:
        return fallback
    start += len(marker)
    end = text.find('"""', start)
    if end <= start:
        return fallback
    return text[start:end]


def init_openkb_skeleton(kb_dir: Path, title: str) -> None:
    wiki = kb_dir / "wiki"
    openkb = kb_dir / ".openkb"
    for path in [
        kb_dir / "raw",
        wiki / "sources" / "images",
        wiki / "summaries",
        wiki / "concepts",
        wiki / "explorations",
        wiki / "reports",
        openkb,
    ]:
        path.mkdir(parents=True, exist_ok=True)
    (openkb / "config.yaml").write_text(
        "model: gpt-5.4-mini\nlanguage: en\npageindex_threshold: 20\n",
        encoding="utf-8",
    )
    (openkb / "hashes.json").write_text("{}\n", encoding="utf-8")
    (kb_dir / ".env.example").write_text("LLM_API_KEY=<your key>\n", encoding="utf-8")
    (wiki / "AGENTS.md").write_text(load_agents_md(), encoding="utf-8")
    (wiki / "index.md").write_text(
        f"# {title}\n\n## Documents\n\n## Concepts\n\n## Explorations\n",
        encoding="utf-8",
    )
    (wiki / "log.md").write_text("# Operations Log\n\n", encoding="utf-8")


def load_spec_manifest(spec_root: Path) -> list[dict[str, Any]]:
    manifest = spec_root / "manifest.csv"
    rows: list[dict[str, Any]] = []
    if manifest.exists():
        with manifest.open("r", encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                copied = Path(row["copied_to"])
                if copied.exists() and copied.suffix.lower() in TEXT_EXTENSIONS:
                    rows.append({
                        "kind": row.get("kind", "doc"),
                        "source": row.get("source", ""),
                        "path": copied,
                        "bytes": int(row.get("bytes") or copied.stat().st_size),
                    })
    if rows:
        return rows

    for path in sorted(spec_root.rglob("*")):
        if path.is_file() and path.name not in {"manifest.csv", "SUMMARY.txt"} and path.suffix.lower() in TEXT_EXTENSIONS:
            rows.append({
                "kind": "doc",
                "source": "",
                "path": path,
                "bytes": path.stat().st_size,
            })
    return rows


def project_for_spec_path(spec_root: Path, path: Path) -> str:
    rel = path.relative_to(spec_root)
    return rel.parts[0] if rel.parts else "unknown"


def normalize_spec_docs(spec_root: Path, raw_dir: Path) -> dict[str, Any]:
    docs = load_spec_manifest(spec_root)
    out_dir = raw_dir / "spec_documents"
    out_dir.mkdir(parents=True, exist_ok=True)

    by_project: Counter[str] = Counter()
    by_ext: Counter[str] = Counter()
    normalized_rows = []
    for idx, item in enumerate(docs, 1):
        src_path = Path(item["path"])
        rel = src_path.relative_to(spec_root)
        project = project_for_spec_path(spec_root, src_path)
        by_project[project] += 1
        by_ext[src_path.suffix.lower() or "<none>"] += 1
        digest = hashlib.sha1(str(rel).encode("utf-8")).hexdigest()[:10]
        out_name = f"{idx:04d}_{slugify(src_path.stem, 64)}_{digest}.md"
        out_path = out_dir / out_name
        text = src_path.read_text(encoding="utf-8", errors="replace")
        if src_path.suffix.lower() == ".md":
            body = text
        else:
            lang = src_path.suffix.lower().lstrip(".") or "text"
            body = f"```{lang}\n{text.rstrip()}\n```\n"
        out_path.write_text(
            "\n".join([
                f"# Spec Document: {rel.as_posix()}",
                "",
                f"- Project: `{project}`",
                f"- Original source: `{item.get('source') or ''}`",
                f"- Exported path: `{src_path}`",
                f"- Original extension: `{src_path.suffix.lower() or '<none>'}`",
                f"- Original bytes: {item.get('bytes')}",
                "",
                "## Content",
                "",
                body,
            ]),
            encoding="utf-8",
        )
        normalized_rows.append({
            "raw_file": str(out_path.relative_to(raw_dir)),
            "exported_path": str(src_path),
            "relative_path": rel.as_posix(),
            "source": item.get("source") or "",
            "project": project,
            "bytes": item.get("bytes"),
            "extension": src_path.suffix.lower() or "<none>",
        })

    index_lines = [
        "# Spec Documents Index",
        "",
        f"- Source export: `{spec_root}`",
        f"- Documents: {len(normalized_rows)}",
        "",
        "## By Project",
        "",
        "| Project | Documents |",
        "|---|---:|",
    ]
    for project, count in by_project.most_common():
        index_lines.append(f"| {project} | {count} |")
    index_lines += ["", "## By Extension", "", "| Extension | Documents |", "|---|---:|"]
    for ext, count in by_ext.most_common():
        index_lines.append(f"| {ext} | {count} |")
    (raw_dir / "spec_documents_index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    write_json(raw_dir / "spec_documents_manifest.json", normalized_rows)
    return {
        "source": str(spec_root),
        "documents": len(normalized_rows),
        "bytes": sum(int(row.get("bytes") or 0) for row in normalized_rows),
        "by_project": dict(by_project.most_common()),
        "by_extension": dict(by_ext.most_common()),
        "raw_dir": str(out_dir),
        "manifest": str(raw_dir / "spec_documents_manifest.json"),
    }


def summarize_graph(graph: dict[str, Any]) -> dict[str, Any]:
    nodes = graph.get("nodes", [])
    links = graph.get("links", [])
    source_projects: Counter[str] = Counter()
    source_extensions: Counter[str] = Counter()
    module_nodes = []
    for node in nodes:
        source_file = str(node.get("source_file") or "")
        if source_file:
            parts = re.split(r"[\\/]+", source_file)
            if parts and parts[0]:
                source_projects[parts[0]] += 1
            source_extensions[Path(source_file).suffix.lower() or "<none>"] += 1
        label = str(node.get("label") or "")
        if source_file.lower().endswith((".sv", ".v", ".svh", ".vh")) and label and "." not in label:
            module_nodes.append(node)
    return {
        "nodes": len(nodes),
        "links": len(links),
        "communities": len({n.get("community") for n in nodes if n.get("community") is not None}),
        "file_types": dict(Counter(str(n.get("file_type", "")) for n in nodes).most_common()),
        "relations": dict(Counter(str(e.get("relation") or e.get("type") or "related") for e in links).most_common()),
        "source_projects": dict(source_projects.most_common(30)),
        "source_extensions": dict(source_extensions.most_common(30)),
        "module_like_nodes": len(module_nodes),
    }


def build_markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(cell).replace("|", "/") for cell in row) + " |")
    return "\n".join(lines)


def write_code_graph_artifacts(graph_root: Path, graph_path: Path, raw_dir: Path) -> dict[str, Any]:
    graph = read_json(graph_path)
    summary = summarize_graph(graph)
    code_dir = raw_dir / "code_graph"
    code_dir.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Code Graph Summary",
        "",
        f"- Graph JSON: `{graph_path}`",
        f"- Graph report: `{graph_root / 'GRAPH_REPORT.md'}`",
        f"- Nodes: {summary['nodes']}",
        f"- Links: {summary['links']}",
        f"- Communities: {summary['communities']}",
        f"- Module-like RTL nodes: {summary['module_like_nodes']}",
        "",
        "## Source Projects",
        "",
        build_markdown_table(["Project", "Graph nodes"], [[k, v] for k, v in summary["source_projects"].items()]),
        "",
        "## Source Extensions",
        "",
        build_markdown_table(["Extension", "Graph nodes"], [[k, v] for k, v in summary["source_extensions"].items()]),
        "",
        "## Top Relations",
        "",
        build_markdown_table(["Relation", "Links"], [[k, v] for k, v in list(summary["relations"].items())[:30]]),
    ]
    (code_dir / "code_graph_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    report = graph_root / "GRAPH_REPORT.md"
    if report.exists():
        shutil.copyfile(report, code_dir / "GRAPH_REPORT.md")
    large_report = graph_root / "large-communities" / "top20_large_communities_report.md"
    if large_report.exists():
        shutil.copyfile(large_report, code_dir / "top20_large_communities_report.md")

    modules_by_project: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for node in graph.get("nodes", []):
        source_file = str(node.get("source_file") or "")
        label = str(node.get("label") or "")
        if not source_file.lower().endswith((".sv", ".v", ".svh", ".vh")) or not label or "." in label:
            continue
        project = re.split(r"[\\/]+", source_file)[0] if source_file else "unknown"
        modules_by_project[project].append({
            "label": label,
            "source_file": source_file,
            "location": node.get("source_location", ""),
            "community": node.get("community", ""),
        })

    module_rows = []
    for project, rows in sorted(modules_by_project.items()):
        for row in sorted(rows, key=lambda r: (r["label"], r["source_file"])):
            module_rows.append([project, row["label"], row["source_file"], row["location"], row["community"]])

    chunk_size = 1000
    module_files = []
    for chunk_idx in range(0, len(module_rows), chunk_size):
        chunk = module_rows[chunk_idx: chunk_idx + chunk_size]
        path = code_dir / f"rtl_module_index_{chunk_idx // chunk_size + 1:02d}.md"
        path.write_text(
            "\n".join([
                f"# RTL Module Index {chunk_idx // chunk_size + 1}",
                "",
                build_markdown_table(["Project", "Module", "Source file", "Location", "Community"], chunk),
                "",
            ]),
            encoding="utf-8",
        )
        module_files.append(str(path.relative_to(raw_dir)))

    relation_samples: dict[str, list[list[str]]] = defaultdict(list)
    nodes_by_id = {str(n.get("id")): n for n in graph.get("nodes", [])}
    for edge in graph.get("links", []):
        rel = str(edge.get("relation") or edge.get("type") or "related")
        if len(relation_samples[rel]) >= 50:
            continue
        src = nodes_by_id.get(str(edge.get("source") or edge.get("_src")), {})
        tgt = nodes_by_id.get(str(edge.get("target") or edge.get("_tgt")), {})
        relation_samples[rel].append([
            str(src.get("label") or edge.get("source") or edge.get("_src")),
            str(tgt.get("label") or edge.get("target") or edge.get("_tgt")),
            str(edge.get("source_file") or ""),
            str(edge.get("source_location") or ""),
        ])

    sample_lines = ["# Code Graph Relation Samples", ""]
    for rel, rows in sorted(relation_samples.items()):
        sample_lines += [
            f"## {rel}",
            "",
            build_markdown_table(["Source", "Target", "Evidence file", "Location"], rows),
            "",
        ]
    (code_dir / "code_relation_samples.md").write_text("\n".join(sample_lines), encoding="utf-8")

    artifact_files = sorted(str(path.relative_to(raw_dir)) for path in code_dir.glob("*.md"))
    return {
        "graph": str(graph_path),
        "summary": summary,
        "raw_dir": str(code_dir),
        "raw_files": artifact_files,
        "module_index_files": module_files,
    }


def write_runbook(kb_dir: Path, variant: str, include_specs: bool, include_code: bool) -> None:
    lines = [
        f"# {variant} OpenKB Runbook",
        "",
        "This workspace is OpenKB-ready. Raw inputs are normalized to Markdown.",
        "",
        "## Content",
        "",
        f"- Includes spec documents: {include_specs}",
        f"- Includes code graph artifacts: {include_code}",
        "",
        "## Optional LLM-backed indexing",
        "",
        "Set an LLM key, then run:",
        "",
        "```powershell",
        "$env:PYTHONIOENCODING='utf-8'",
        "$env:LITELLM_LOCAL_MODEL_COST_MAP='True'",
        "$env:LLM_API_KEY='<your key>'",
        f"D:\\MyWork\\verilog\\.venv-graphify\\Scripts\\openkb.exe --kb-dir {kb_dir} add {kb_dir / 'raw'}",
        f"D:\\MyWork\\verilog\\.venv-graphify\\Scripts\\openkb.exe --kb-dir {kb_dir} status",
        "```",
        "",
        "No LLM indexing is run by this preparation script.",
        "",
    ]
    (kb_dir / "RUNBOOK.md").write_text("\n".join(lines), encoding="utf-8")


def count_raw_files(kb_dir: Path) -> int:
    raw = kb_dir / "raw"
    return sum(1 for path in raw.rglob("*") if path.is_file())


def build_variant(
    out_root: Path,
    variant: str,
    spec_root: Path,
    graph_root: Path,
    graph_path: Path,
    include_specs: bool,
    include_code: bool,
) -> dict[str, Any]:
    kb_dir = out_root / variant / "kb"
    init_openkb_skeleton(kb_dir, f"{variant} Knowledge Base")
    raw_dir = kb_dir / "raw"

    spec_info = normalize_spec_docs(spec_root, raw_dir) if include_specs else None
    code_info = write_code_graph_artifacts(graph_root, graph_path, raw_dir) if include_code else None
    write_runbook(kb_dir, variant, include_specs, include_code)

    manifest = {
        "variant": variant,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "kb_dir": str(kb_dir),
        "raw_dir": str(raw_dir),
        "raw_files": count_raw_files(kb_dir),
        "includes": {
            "spec_documents": include_specs,
            "code_graph": include_code,
        },
        "spec": spec_info,
        "code": code_info,
        "status": "prepared_offline",
        "note": "OpenKB add/query are LLM-backed and are intentionally not run here.",
    }
    write_json(out_root / variant / "variant_manifest.json", manifest)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Build spec/code OpenKB variants")
    parser.add_argument("--spec-root", type=Path, default=DEFAULT_SPEC_ROOT)
    parser.add_argument("--graph-root", type=Path, default=DEFAULT_GRAPH_ROOT)
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH)
    parser.add_argument("--out-root", type=Path, default=DEFAULT_OUT_ROOT)
    args = parser.parse_args()

    spec_root = args.spec_root.resolve()
    graph_root = args.graph_root.resolve()
    graph_path = args.graph.resolve()
    out_root = args.out_root.resolve()
    if not spec_root.exists():
        raise FileNotFoundError(spec_root)
    if not graph_path.exists():
        raise FileNotFoundError(graph_path)
    out_root.mkdir(parents=True, exist_ok=True)

    variants = [
        build_variant(out_root, "spec-only", spec_root, graph_root, graph_path, True, False),
        build_variant(out_root, "code-only", spec_root, graph_root, graph_path, False, True),
        build_variant(out_root, "spec-code", spec_root, graph_root, graph_path, True, True),
    ]
    top_manifest = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "spec_root": str(spec_root),
        "graph": str(graph_path),
        "out_root": str(out_root),
        "variants": variants,
    }
    write_json(out_root / "kb_variants_manifest.json", top_manifest)
    print(json.dumps({
        "status": "ok",
        "out_root": str(out_root),
        "variants": [
            {
                "variant": item["variant"],
                "raw_files": item["raw_files"],
                "spec_docs": item["spec"]["documents"] if item.get("spec") else 0,
                "code_raw_files": len(item["code"]["raw_files"]) if item.get("code") else 0,
            }
            for item in variants
        ],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
