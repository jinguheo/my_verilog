#!/usr/bin/env python3
"""
Build an AST-enriched KG from extract_ast_nodes.py output.

Adds to the existing kg_full/ graph:
  New node kinds  : ast_module, ast_port, ast_param, ast_always, ast_function, ast_package
  New edge types  : AST_HAS_PORT, AST_HAS_PARAM, AST_HAS_ALWAYS, AST_HAS_FUNCTION,
                    AST_INSTANTIATES, AST_IN_PACKAGE

The AST nodes are kept separate from the ontology module/port nodes so the two
layers can be compared and merged gradually.

Usage:
  python build_ast_kg.py \
    --ast-nodes  out/ast/ibex_ast_nodes.jsonl \
    --kg-in      out/kg_full/kg_full_nodes_edges.json \
    --out-dir    out/kg_full
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def _mod_id(row: dict) -> str:
    return f"ast_module:{row['project']}:{row['name']}:{row['file']}"


def _port_id(mod_row: dict, port: dict) -> str:
    return f"ast_port:{mod_row['project']}:{mod_row['name']}:{port['name']}"


def _param_id(mod_row: dict, param: dict) -> str:
    return f"ast_param:{mod_row['project']}:{mod_row['name']}:{param['name']}"


def _always_id(mod_row: dict, idx: int, kind: str) -> str:
    return f"ast_always:{mod_row['project']}:{mod_row['name']}:{idx}:{kind}"


def _fn_id(mod_row: dict, fn: dict) -> str:
    return f"ast_fn:{mod_row['project']}:{mod_row['name']}:{fn['name']}"


def _pkg_id(row: dict) -> str:
    return f"ast_package:{row['project']}:{row['name']}:{row['file']}"


def build(ast_rows: list[dict], existing_kg: dict) -> dict:
    nodes: list[dict] = []
    edges: list[dict] = []
    stats = Counter()

    # Index existing module nodes for cross-linking
    existing_modules: dict[str, str] = {}   # (project, name) → existing node id
    for n in existing_kg.get("nodes", []):
        if n.get("kind") == "module":
            existing_modules[(n.get("project", ""), n.get("name", ""))] = n["id"]

    modules = [r for r in ast_rows if r["kind"] == "module"]
    packages = [r for r in ast_rows if r["kind"] == "package"]

    # ── modules ──────────────────────────────────────────────────────────────
    for row in modules:
        mid = _mod_id(row)
        nodes.append({
            "id":            mid,
            "kind":          "ast_module",
            "name":          row["name"],
            "project":       row["project"],
            "file":          row["file"],
            "line_start":    row["line_start"],
            "line_end":      row["line_end"],
            "port_count":    len(row["ports"]),
            "param_count":   len(row["params"]),
            "always_count":  len(row["always_blocks"]),
            "fn_count":      len(row["functions"]),
            "parse_errors":  row["parse_errors"],
        })
        stats["ast_module"] += 1

        # Cross-link to existing ontology module node
        existing_id = existing_modules.get((row["project"], row["name"]))
        if existing_id:
            edges.append({
                "source": mid,
                "target": existing_id,
                "type":   "AST_SAME_AS_ONTOLOGY",
            })
            stats["AST_SAME_AS_ONTOLOGY"] += 1

        # ── ports ─────────────────────────────────────────────────────────
        for port in row["ports"]:
            pid = _port_id(row, port)
            nodes.append({
                "id":        pid,
                "kind":      "ast_port",
                "name":      port["name"],
                "direction": port["direction"],
                "dtype":     port["dtype"],
                "width":     port["width"],
                "module":    row["name"],
                "project":   row["project"],
            })
            edges.append({"source": mid, "target": pid, "type": "AST_HAS_PORT"})
            stats["ast_port"] += 1

        # ── parameters ────────────────────────────────────────────────────
        for param in row["params"]:
            if not param.get("name"):
                continue
            pmid = _param_id(row, param)
            nodes.append({
                "id":      pmid,
                "kind":    "ast_param",
                "name":    param["name"],
                "dtype":   param["dtype"],
                "default": param["default"],
                "module":  row["name"],
                "project": row["project"],
            })
            edges.append({"source": mid, "target": pmid, "type": "AST_HAS_PARAM"})
            stats["ast_param"] += 1

        # ── always blocks ─────────────────────────────────────────────────
        for idx, ab in enumerate(row["always_blocks"]):
            aid = _always_id(row, idx, ab["kind"])
            nodes.append({
                "id":          aid,
                "kind":        "ast_always",
                "always_kind": ab["kind"],
                "lhs_signals": ab["lhs_signals"],
                "sensitivity": ab["sensitivity"],
                "module":      row["name"],
                "project":     row["project"],
            })
            edges.append({"source": mid, "target": aid, "type": "AST_HAS_ALWAYS"})
            stats["ast_always"] += 1

        # ── functions ─────────────────────────────────────────────────────
        for fn in row["functions"]:
            if not fn.get("name"):
                continue
            fid = _fn_id(row, fn)
            nodes.append({
                "id":          fid,
                "kind":        "ast_function",
                "name":        fn["name"],
                "return_type": fn["return_type"],
                "port_count":  len(fn["ports"]),
                "module":      row["name"],
                "project":     row["project"],
            })
            edges.append({"source": mid, "target": fid, "type": "AST_HAS_FUNCTION"})
            stats["ast_function"] += 1

        # ── instantiation edges ────────────────────────────────────────────
        for inst_group in row["instances"]:
            child_type = inst_group["module_type"]
            for hier in inst_group["instances"]:
                inst_name = hier["instance_name"]
                # Try to find the child ast_module node
                child_matches = [
                    _mod_id(r) for r in modules
                    if r["name"] == child_type and r["project"] == row["project"]
                ]
                target = child_matches[0] if child_matches else (
                    existing_modules.get((row["project"], child_type), f"unknown:{child_type}")
                )
                edges.append({
                    "source":        mid,
                    "target":        target,
                    "type":          "AST_INSTANTIATES",
                    "instance_name": inst_name,
                })
                stats["AST_INSTANTIATES"] += 1

    # ── packages ─────────────────────────────────────────────────────────────
    for row in packages:
        pkid = _pkg_id(row)
        nodes.append({
            "id":         pkid,
            "kind":       "ast_package",
            "name":       row["name"],
            "project":    row["project"],
            "file":       row["file"],
            "typedef_count": len(row["typedefs"]),
            "param_count":   len(row["params"]),
        })
        stats["ast_package"] += 1

        for param in row["params"]:
            if not param.get("name"):
                continue
            pmid = f"ast_pkg_param:{row['project']}:{row['name']}:{param['name']}"
            nodes.append({
                "id":      pmid,
                "kind":    "ast_param",
                "name":    param["name"],
                "dtype":   param["dtype"],
                "default": param["default"],
                "package": row["name"],
                "project": row["project"],
            })
            edges.append({"source": pkid, "target": pmid, "type": "AST_HAS_PARAM"})

    return {
        "nodes": existing_kg.get("nodes", []) + nodes,
        "edges": existing_kg.get("edges", []) + edges,
        "ast_stats": dict(stats),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ast-nodes", required=True, help="out/ast/ibex_ast_nodes.jsonl")
    ap.add_argument("--kg-in",     required=True, help="existing kg_full_nodes_edges.json")
    ap.add_argument("--out-dir",   required=True, help="output directory (kg_full/)")
    args = ap.parse_args()

    ast_rows = read_jsonl(Path(args.ast_nodes))
    with open(args.kg_in, encoding="utf-8") as f:
        existing_kg = json.load(f)

    print(f"AST rows     : {len(ast_rows)}")
    print(f"Existing nodes: {len(existing_kg.get('nodes', []))}")
    print(f"Existing edges: {len(existing_kg.get('edges', []))}")

    merged = build(ast_rows, existing_kg)

    out = Path(args.out_dir)
    write_json(out / "kg_full_nodes_edges.json", {
        "nodes": merged["nodes"],
        "edges": merged["edges"],
    })

    # Update summary
    summary_path = out / "kg_full_summary.json"
    if summary_path.exists():
        with open(summary_path, encoding="utf-8") as f:
            summary = json.load(f)
    else:
        summary = {}

    ast_stats = merged["ast_stats"]
    summary["ast_enrichment"] = {
        "ast_modules":   ast_stats.get("ast_module", 0),
        "ast_ports":     ast_stats.get("ast_port", 0),
        "ast_params":    ast_stats.get("ast_param", 0),
        "ast_always":    ast_stats.get("ast_always", 0),
        "ast_functions": ast_stats.get("ast_function", 0),
        "ast_packages":  ast_stats.get("ast_package", 0),
        "cross_links":   ast_stats.get("AST_SAME_AS_ONTOLOGY", 0),
        "inst_edges":    ast_stats.get("AST_INSTANTIATES", 0),
    }
    summary["total_nodes"] = len(merged["nodes"])
    summary["total_edges"] = len(merged["edges"])
    write_json(summary_path, summary)

    result = {
        "status":          "ok",
        "new_nodes":       len(merged["nodes"]) - len(existing_kg.get("nodes", [])),
        "new_edges":       len(merged["edges"]) - len(existing_kg.get("edges", [])),
        "total_nodes":     len(merged["nodes"]),
        "total_edges":     len(merged["edges"]),
        **summary["ast_enrichment"],
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
