#!/usr/bin/env python3
"""Run current Graphify DB artifacts through OpenTology and OpenKB wrappers.

The current graph is already built by Graphify.  This script keeps the run
non-destructive: it creates tool-specific output workspaces under
``dbs/graphify-out`` instead of initializing hooks or project files at repo root.

OpenTology is exercised by exporting the Graphify node-link graph to Turtle,
tracking that Turtle file from an embedded OpenTology config, and running a few
SPARQL queries through the actual OpenTology CLI.

OpenKB is LLM-backed.  Without an LLM API key, this script prepares a KB
skeleton and raw Markdown inputs, then runs the non-LLM OpenKB status/list
commands.  It intentionally skips ``openkb add`` unless ``--allow-openkb-add``
is passed and an API key is present.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DB_ROOT = ROOT / "dbs"
DEFAULT_GRAPH = DEFAULT_DB_ROOT / "graphify-out" / "graph.json"
DEFAULT_OUT_ROOT = DEFAULT_DB_ROOT / "graphify-out"
DEFAULT_OPENTOLOGY_CLI = ROOT / "tools" / "opentology" / "dist" / "index.js"
DEFAULT_OPENKB = ROOT / ".venv-graphify" / "Scripts" / "openkb.exe"

RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
XSD = "http://www.w3.org/2001/XMLSchema#"
OTX = "https://opentology.dev/vocab#"
GFY = "https://graphify.dev/vocab#"

RELATION_TO_PROPERTY = {
    "contains": f"{OTX}contains",
    "defines": f"{OTX}defines",
    "imports": f"{OTX}dependsOn",
    "imports_from": f"{OTX}dependsOn",
    "calls": f"{OTX}calls",
    "inherits": f"{OTX}inherits",
    "instantiates": f"{GFY}instantiates",
    "method": f"{GFY}method",
    "uses": f"{GFY}uses",
    "rationale_for": f"{GFY}rationaleFor",
}


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def turtle_literal(value: Any) -> str:
    text = "" if value is None else str(value)
    text = (
        text.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\r", "\\r")
        .replace("\t", "\\t")
    )
    return f'"{text}"'


def typed_literal(value: int | float, datatype: str) -> str:
    return f'"{value}"^^<{datatype}>'


def uri_for_node(node_id: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9._~-]+", "_", str(node_id)).strip("_")
    if not safe:
        safe = "node"
    return f"urn:graphify-node:{safe}"


def predicate_for_relation(relation: str) -> str:
    if relation in RELATION_TO_PROPERTY:
        return RELATION_TO_PROPERTY[relation]
    safe = re.sub(r"[^A-Za-z0-9]+", "_", relation).strip("_") or "related"
    return f"{GFY}{safe}"


def summarize_graph(data: dict[str, Any]) -> dict[str, Any]:
    nodes = data.get("nodes", [])
    links = data.get("links", [])
    source_projects: Counter[str] = Counter()
    source_extensions: Counter[str] = Counter()
    for node in nodes:
        source_file = str(node.get("source_file") or "")
        if not source_file:
            continue
        parts = re.split(r"[\\/]+", source_file)
        if parts and parts[0]:
            source_projects[parts[0]] += 1
        suffix = Path(source_file).suffix.lower() or "<none>"
        source_extensions[suffix] += 1
    return {
        "nodes": len(nodes),
        "links": len(links),
        "file_types": dict(Counter(str(n.get("file_type", "")) for n in nodes)),
        "relations": dict(Counter(str(e.get("relation") or e.get("type") or "related") for e in links)),
        "communities": len({n.get("community") for n in nodes if n.get("community") is not None}),
        "source_projects": dict(source_projects.most_common(30)),
        "source_extensions": dict(source_extensions.most_common(30)),
        "sample_labels": [n.get("label") for n in nodes[:10]],
    }


def export_turtle(data: dict[str, Any], ttl_path: Path) -> dict[str, Any]:
    nodes = data.get("nodes", [])
    links = data.get("links", [])
    id_to_uri = {str(node.get("id")): uri_for_node(str(node.get("id"))) for node in nodes}

    ttl_path.parent.mkdir(parents=True, exist_ok=True)
    module_like = 0
    with ttl_path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n")
        handle.write("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n")
        handle.write("@prefix otx: <https://opentology.dev/vocab#> .\n")
        handle.write("@prefix gfy: <https://graphify.dev/vocab#> .\n\n")

        for node in nodes:
            node_id = str(node.get("id"))
            uri = id_to_uri[node_id]
            label = str(node.get("label") or node_id)
            source_file = str(node.get("source_file") or "")
            predicates = [
                f"<{uri}> rdf:type gfy:Node",
                f"    ; otx:title {turtle_literal(label)}",
                f"    ; gfy:graphifyId {turtle_literal(node_id)}",
            ]
            if source_file:
                predicates.append(f"    ; gfy:sourceFile {turtle_literal(source_file)}")
            if node.get("source_location"):
                predicates.append(f"    ; gfy:sourceLocation {turtle_literal(node.get('source_location'))}")
            if node.get("file_type"):
                predicates.append(f"    ; gfy:fileType {turtle_literal(node.get('file_type'))}")
            if node.get("community") is not None:
                predicates.append(f"    ; gfy:community {typed_literal(int(node.get('community')), XSD + 'integer')}")
            if node.get("confidence_score") is not None:
                predicates.append(f"    ; gfy:confidenceScore {typed_literal(float(node.get('confidence_score')), XSD + 'double')}")

            looks_like_module = source_file.lower().endswith((".sv", ".v", ".svh", ".vh")) and label and "." not in label
            if looks_like_module:
                predicates.insert(1, "    ; rdf:type otx:Module")
                module_like += 1
            handle.write("\n".join(predicates) + " .\n\n")

        for edge in links:
            src = id_to_uri.get(str(edge.get("source") or edge.get("_src")))
            tgt = id_to_uri.get(str(edge.get("target") or edge.get("_tgt")))
            if not src or not tgt or src == tgt:
                continue
            relation = str(edge.get("relation") or edge.get("type") or "related")
            predicate = predicate_for_relation(relation)
            handle.write(f"<{src}> <{predicate}> <{tgt}> .\n")

    return {
        "turtle": str(ttl_path),
        "nodes_exported": len(nodes),
        "links_exported": len(links),
        "module_like_nodes": module_like,
    }


def init_opentology_workspace(out_dir: Path, turtle_rel: str, graph_uri: str) -> Path:
    config = {
        "projectId": "verilog-current-graph",
        "mode": "embedded",
        "graphUri": graph_uri,
        "graphs": {"context": f"{graph_uri}/context"},
        "files": {f"{graph_uri}/context": [turtle_rel]},
        "prefixes": {
            "rdf": RDF,
            "xsd": XSD,
            "otx": OTX,
            "gfy": GFY,
        },
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    config_path = out_dir / ".opentology.json"
    write_json(config_path, config)
    return config_path


def label_uri_map(data: dict[str, Any], labels: list[str]) -> dict[str, str]:
    wanted = set(labels)
    found: dict[str, str] = {}
    for node in data.get("nodes", []):
        label = str(node.get("label") or "")
        if label in wanted and label not in found:
            found[label] = uri_for_node(str(node.get("id")))
    return found


def run_opentology_queries(
    opentology_cli: Path,
    out_dir: Path,
    graph_uri: str,
    timeout: int,
    data: dict[str, Any],
) -> dict[str, Any]:
    uri_by_label = label_uri_map(data, ["ibex_core", "prim_sha2", "prim_sha2_pad"])
    ibex_core_uri = uri_by_label.get("ibex_core", "urn:graphify-node:missing_ibex_core")
    sha2_values = " ".join(f"<{uri}>" for label, uri in uri_by_label.items() if label.startswith("prim_sha2"))
    if not sha2_values:
        sha2_values = "<urn:graphify-node:missing_prim_sha2>"
    queries = {
        "triple_count": f"SELECT (COUNT(*) AS ?count) WHERE {{ GRAPH <{graph_uri}/context> {{ ?s ?p ?o }} }}",
        "type_counts": f"SELECT ?type (COUNT(?s) AS ?count) WHERE {{ GRAPH <{graph_uri}/context> {{ ?s a ?type }} }} GROUP BY ?type ORDER BY DESC(?count)",
        "top_predicates": f"SELECT ?p (COUNT(*) AS ?count) WHERE {{ GRAPH <{graph_uri}/context> {{ ?s ?p ?o }} }} GROUP BY ?p ORDER BY DESC(?count) LIMIT 20",
        "ibex_core_neighborhood": f"SELECT ?p ?o WHERE {{ GRAPH <{graph_uri}/context> {{ <{ibex_core_uri}> ?p ?o }} }} LIMIT 30",
        "sha2_modules": f"SELECT ?s ?title ?file WHERE {{ GRAPH <{graph_uri}/context> {{ VALUES ?s {{ {sha2_values} }} ?s a otx:Module ; otx:title ?title ; gfy:sourceFile ?file }} }} LIMIT 20",
    }
    results: dict[str, Any] = {}
    for name, sparql in queries.items():
        proc = subprocess.run(
            ["node", str(opentology_cli), "query", sparql, "--format", "json", "--raw"],
            cwd=str(out_dir),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            errors="replace",
            timeout=timeout,
        )
        try:
            parsed = json.loads(proc.stdout) if proc.stdout.strip() else None
        except json.JSONDecodeError:
            parsed = None
        results[name] = {
            "returncode": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "parsed": parsed,
        }
    write_json(out_dir / "opentology_query_results.json", results)
    return results


def build_inventory_markdown(db_root: Path, graph_path: Path, summary: dict[str, Any]) -> str:
    project_counts = Counter(summary.get("source_projects", {}))
    ext_counts = Counter(summary.get("source_extensions", {}))
    lines = [
        "# Current DB Inventory",
        "",
        f"- DB root: `{db_root}`",
        f"- Graph: `{graph_path}`",
        f"- Graph nodes: {summary['nodes']}",
        f"- Graph links: {summary['links']}",
        f"- Graph communities: {summary['communities']}",
        "",
        "## Top Projects",
        "",
        "| Project | Files |",
        "|---|---:|",
    ]
    for project, count in project_counts.most_common(20):
        lines.append(f"| {project} | {count} |")
    lines += ["", "## File Extensions", "", "| Extension | Files |", "|---|---:|"]
    for ext, count in ext_counts.most_common(30):
        lines.append(f"| {ext} | {count} |")
    lines += ["", "## Graph Relations", "", "| Relation | Count |", "|---|---:|"]
    for rel, count in Counter(summary["relations"]).most_common(30):
        lines.append(f"| {rel} | {count} |")
    return "\n".join(lines) + "\n"


def build_graph_summary_markdown(graph_path: Path, report_path: Path, summary: dict[str, Any]) -> str:
    lines = [
        "# Current Graphify Graph Summary",
        "",
        f"- Graph JSON: `{graph_path}`",
        f"- Graph report: `{report_path}`",
        f"- Nodes: {summary['nodes']}",
        f"- Links: {summary['links']}",
        f"- Communities: {summary['communities']}",
        "",
        "## File Types",
        "",
        "| File type | Nodes |",
        "|---|---:|",
    ]
    for file_type, count in Counter(summary["file_types"]).most_common():
        lines.append(f"| {file_type or '<missing>'} | {count} |")
    lines += ["", "## Top Relations", "", "| Relation | Links |", "|---|---:|"]
    for relation, count in Counter(summary["relations"]).most_common(30):
        lines.append(f"| {relation} | {count} |")
    return "\n".join(lines) + "\n"


def init_openkb_workspace(kb_dir: Path, db_root: Path, graph_path: Path, graph_report: Path, summary: dict[str, Any]) -> dict[str, Any]:
    raw_dir = kb_dir / "raw"
    wiki_dir = kb_dir / "wiki"
    openkb_dir = kb_dir / ".openkb"
    for path in [
        raw_dir,
        wiki_dir / "sources" / "images",
        wiki_dir / "summaries",
        wiki_dir / "concepts",
        wiki_dir / "explorations",
        wiki_dir / "reports",
        openkb_dir,
    ]:
        path.mkdir(parents=True, exist_ok=True)

    (openkb_dir / "config.yaml").write_text(
        "model: gpt-5.4-mini\nlanguage: en\npageindex_threshold: 20\n",
        encoding="utf-8",
    )
    (openkb_dir / "hashes.json").write_text("{}\n", encoding="utf-8")
    (kb_dir / ".env.example").write_text("LLM_API_KEY=<your key>\n", encoding="utf-8")

    schema_src = ROOT / "tools" / "OpenKB" / "openkb" / "schema.py"
    agents_md = "# OpenKB Wiki Instructions\n\nMaintain summaries, concepts, and source links.\n"
    if schema_src.exists():
        text = schema_src.read_text(encoding="utf-8", errors="replace")
        marker = 'AGENTS_MD = """'
        start = text.find(marker)
        if start >= 0:
            start += len(marker)
            end = text.find('"""', start)
            if end > start:
                agents_md = text[start:end]
    (wiki_dir / "AGENTS.md").write_text(agents_md, encoding="utf-8")
    (wiki_dir / "index.md").write_text(
        "# Knowledge Base Index\n\n## Documents\n\n## Concepts\n\n## Explorations\n",
        encoding="utf-8",
    )
    (wiki_dir / "log.md").write_text("# Operations Log\n\n", encoding="utf-8")

    copied_report = raw_dir / "current_graph_report.md"
    if graph_report.exists():
        shutil.copyfile(graph_report, copied_report)
    (raw_dir / "current_graph_summary.md").write_text(
        build_graph_summary_markdown(graph_path, graph_report, summary),
        encoding="utf-8",
    )
    (raw_dir / "current_db_inventory.md").write_text(
        build_inventory_markdown(db_root, graph_path, summary),
        encoding="utf-8",
    )

    return {
        "kb_dir": str(kb_dir),
        "raw_dir": str(raw_dir),
        "raw_files": sorted(p.name for p in raw_dir.glob("*")),
    }


def run_openkb_command(openkb: Path, kb_dir: Path, command: str, timeout: int) -> dict[str, Any]:
    env = dict(os.environ)
    env.setdefault("PYTHONIOENCODING", "utf-8")
    env.setdefault("LITELLM_LOCAL_MODEL_COST_MAP", "True")
    try:
        proc = subprocess.run(
            [str(openkb), "--kb-dir", str(kb_dir), command],
            cwd=str(ROOT),
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            errors="replace",
            timeout=timeout,
        )
        return {"returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr, "timed_out": False}
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode("utf-8", errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = exc.stderr.decode("utf-8", errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        return {
            "returncode": None,
            "stdout": stdout,
            "stderr": stderr,
            "timed_out": True,
            "timeout_seconds": timeout,
        }


def fallback_openkb_status(kb_dir: Path) -> str:
    wiki = kb_dir / "wiki"
    rows = []
    for name, path in [
        ("sources", wiki / "sources"),
        ("summaries", wiki / "summaries"),
        ("concepts", wiki / "concepts"),
        ("reports", wiki / "reports"),
        ("raw", kb_dir / "raw"),
    ]:
        count = sum(1 for item in path.rglob("*") if item.is_file()) if path.exists() else 0
        rows.append((name, count))
    hashes_path = kb_dir / ".openkb" / "hashes.json"
    indexed = 0
    if hashes_path.exists():
        try:
            indexed = len(json.loads(hashes_path.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            indexed = 0

    lines = ["Knowledge Base Status:", "  Directory            Files     ", "  -------------------- ----------"]
    for name, count in rows:
        lines.append(f"  {name:<20} {count:<10}")
    lines += ["", f"  Total indexed: {indexed} document(s)", ""]
    return "\n".join(lines)


def fallback_openkb_list(kb_dir: Path) -> str:
    hashes_path = kb_dir / ".openkb" / "hashes.json"
    if not hashes_path.exists():
        return "No documents indexed yet.\n"
    try:
        hashes = json.loads(hashes_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        hashes = {}
    if not hashes:
        return "No documents indexed yet.\n"
    lines = [f"Documents ({len(hashes)}):"]
    for meta in hashes.values():
        lines.append(f"  - {meta.get('name', 'unknown')}")
    return "\n".join(lines) + "\n"


def run_openkb(openkb: Path, kb_dir: Path, allow_add: bool, timeout: int) -> dict[str, Any]:
    key_present = any(os.environ.get(k) for k in ("LLM_API_KEY", "OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GEMINI_API_KEY"))
    commands = {
        "status": run_openkb_command(openkb, kb_dir, "status", timeout),
        "list": run_openkb_command(openkb, kb_dir, "list", timeout),
    }
    if not commands["status"].get("stdout"):
        commands["status"]["stdout"] = fallback_openkb_status(kb_dir)
        commands["status"]["fallback"] = "local_status"
    if not commands["list"].get("stdout"):
        commands["list"]["stdout"] = fallback_openkb_list(kb_dir)
        commands["list"]["fallback"] = "local_list"
    add_result: dict[str, Any] | None = None
    if allow_add and key_present:
        env = dict(os.environ)
        env.setdefault("PYTHONIOENCODING", "utf-8")
        env.setdefault("LITELLM_LOCAL_MODEL_COST_MAP", "True")
        try:
            proc = subprocess.run(
                [str(openkb), "--kb-dir", str(kb_dir), "add", str(kb_dir / "raw")],
                cwd=str(ROOT),
                env=env,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                errors="replace",
                timeout=timeout,
            )
            add_result = {"returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr, "timed_out": False}
        except subprocess.TimeoutExpired as exc:
            stdout = exc.stdout.decode("utf-8", errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
            stderr = exc.stderr.decode("utf-8", errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
            add_result = {
                "returncode": None,
                "stdout": stdout,
                "stderr": stderr,
                "timed_out": True,
                "timeout_seconds": timeout,
            }
    return {
        "llm_key_present": key_present,
        "add_attempted": bool(add_result),
        "add_result": add_result,
        "commands": commands,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run current Graphify DB through OpenTology and OpenKB outputs")
    parser.add_argument("--db-root", type=Path, default=DEFAULT_DB_ROOT)
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH)
    parser.add_argument("--out-root", type=Path, default=DEFAULT_OUT_ROOT)
    parser.add_argument("--opentology-cli", type=Path, default=DEFAULT_OPENTOLOGY_CLI)
    parser.add_argument("--openkb", type=Path, default=DEFAULT_OPENKB)
    parser.add_argument("--timeout", type=int, default=240)
    parser.add_argument("--opentology-timeout", type=int, default=0)
    parser.add_argument("--openkb-timeout", type=int, default=0)
    parser.add_argument("--allow-openkb-add", action="store_true")
    parser.add_argument("--skip-opentology", action="store_true")
    args = parser.parse_args()
    opentology_timeout = args.opentology_timeout or args.timeout
    openkb_timeout = args.openkb_timeout or args.timeout

    graph_path = args.graph.resolve()
    db_root = args.db_root.resolve()
    out_root = args.out_root.resolve()
    if not graph_path.exists():
        raise FileNotFoundError(graph_path)
    if "spec_documents" in str(graph_path).lower() or "spec_documents" in str(db_root).lower():
        raise SystemExit("Refusing to run spec_documents input. Use the current DB graph under dbs/graphify-out.")

    data = read_json(graph_path)
    summary = summarize_graph(data)
    generated_at = datetime.now().isoformat(timespec="seconds")

    opentology_dir = out_root / "opentology-current"
    graph_uri = "https://opentology.dev/verilog-current-graph"
    opentology_manifest_path = opentology_dir / "opentology_manifest.json"
    if args.skip_opentology and opentology_manifest_path.exists():
        opentology_manifest = read_json(opentology_manifest_path)
    else:
        ttl_path = opentology_dir / ".opentology" / "data" / "current_graph.ttl"
        turtle_info = export_turtle(data, ttl_path)
        config_path = init_opentology_workspace(
            opentology_dir,
            ".opentology/data/current_graph.ttl",
            graph_uri,
        )
        run_opentology_queries(args.opentology_cli.resolve(), opentology_dir, graph_uri, opentology_timeout, data)
        opentology_manifest = {
            "generated_at": generated_at,
            "graph": str(graph_path),
            "workspace": str(opentology_dir),
            "config": str(config_path),
            "summary": summary,
            "turtle": turtle_info,
            "query_results": str(opentology_dir / "opentology_query_results.json"),
        }
        write_json(opentology_manifest_path, opentology_manifest)

    openkb_dir = out_root / "openkb-current" / "kb"
    graph_report = graph_path.parent / "GRAPH_REPORT.md"
    openkb_info = init_openkb_workspace(openkb_dir, db_root, graph_path, graph_report, summary)
    openkb_results = run_openkb(args.openkb.resolve(), openkb_dir, args.allow_openkb_add, openkb_timeout)
    write_json(openkb_dir.parent / "openkb_run_results.json", openkb_results)
    openkb_manifest = {
        "generated_at": generated_at,
        "graph": str(graph_path),
        "workspace": str(openkb_dir.parent),
        "summary": summary,
        "kb": openkb_info,
        "run_results": str(openkb_dir.parent / "openkb_run_results.json"),
        "status": "prepared_offline" if not openkb_results["add_attempted"] else "add_attempted",
        "note": "OpenKB add/query require an LLM API key; status/list were run without LLM calls.",
    }
    write_json(openkb_dir.parent / "openkb_manifest.json", openkb_manifest)

    combined = {
        "status": "ok",
        "generated_at": generated_at,
        "graph": str(graph_path),
        "summary": summary,
        "opentology": opentology_manifest,
        "openkb": openkb_manifest,
    }
    write_json(out_root / "open_tools_run_manifest.json", combined)
    print(json.dumps({
        "status": "ok",
        "graph": str(graph_path),
        "nodes": summary["nodes"],
        "links": summary["links"],
        "opentology_dir": str(opentology_dir),
        "openkb_dir": str(openkb_dir.parent),
        "openkb_add_attempted": openkb_results["add_attempted"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
