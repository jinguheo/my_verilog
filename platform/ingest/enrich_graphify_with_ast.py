#!/usr/bin/env python3
"""
Enrich a graphify code-only graph.json with AST nodes extracted by
extract_ast_nodes.py.

Matching strategy:
  For each graphify symbol node (non-L1, file_type=code):
    1. Normalize its source_file path to a relative suffix  (ibex/rtl/ibex_alu.sv)
    2. Find AST rows where path ends with that suffix AND name == node label
    3. If matched: add ast_port / ast_param / ast_always / ast_function sub-nodes
       and connect them with AST_HAS_* edges

New node kinds added to the graph:
  ast_port, ast_param, ast_always, ast_function

New edge relations added:
  HAS_AST        — graphify_symbol → ast_module_summary
  AST_HAS_PORT   — ast_module_summary → ast_port
  AST_HAS_PARAM  — ast_module_summary → ast_param
  AST_HAS_ALWAYS — ast_module_summary → ast_always
  AST_HAS_FN     — ast_module_summary → ast_function

Usage:
  python enrich_graphify_with_ast.py \
    --graph     dbs/graphify-out/code-only-graphify/graph.json \
    --ast-nodes out/ast/ibex_ast_nodes.jsonl \
    --out       dbs/graphify-out/code-only-graphify/graph.json
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from collections import Counter


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def normalize_path(p: str) -> str:
    """Lower-case, forward slashes, strip drive/abs prefix."""
    return p.replace("\\", "/").lower()


def build_ast_index(ast_rows: list[dict]) -> dict:
    """
    Returns: { (norm_path_suffix, module_name): ast_row }
    Suffix = last N path components for fuzzy matching.
    """
    index: dict[tuple[str, str], dict] = {}
    for row in ast_rows:
        if row["kind"] != "module":
            continue
        npath = normalize_path(row["file"])
        # Strip leading dbs/ prefix (relative paths) or everything up to /dbs/ (absolute)
        if npath.startswith("dbs/"):
            suffix = npath[4:]           # "dbs/ibex/..." → "ibex/..."
        elif "/dbs/" in npath:
            suffix = npath.split("/dbs/", 1)[1]
        else:
            suffix = npath
        key = (suffix, row["name"].lower())
        index[key] = row
    return index


def match_graphify_node(gnode: dict, ast_index: dict) -> dict | None:
    """Try to find an AST module row for a graphify symbol node."""
    src = normalize_path(gnode.get("source_file", ""))
    label = gnode.get("label", "").lower()

    # Direct suffix match
    key = (src, label)
    if key in ast_index:
        return ast_index[key]

    # Fallback: match by label where the project prefix of source_file matches
    src_project = src.split("/")[0] if "/" in src else ""
    for (_, aname), row in ast_index.items():
        norm_file = normalize_path(row["file"])
        dbs_part  = norm_file.split("/dbs/")[1] if "/dbs/" in norm_file else norm_file
        row_project = dbs_part.split("/")[0]
        if aname == label and (not src_project or src_project == row_project):
            return row

    return None


def make_id(prefix: str, *parts: str) -> str:
    clean = "_".join(p.replace(" ", "_").replace("/", "_").replace("\\", "_")
                      .replace(".", "_").replace(":", "_") for p in parts)
    return f"{prefix}_{clean}"


def enrich(graph: dict, ast_rows: list[dict]) -> dict:
    nodes: list[dict] = list(graph.get("nodes", []))
    links: list[dict] = list(graph.get("links", []))
    existing_ids = {n["id"] for n in nodes}

    ast_modules = [r for r in ast_rows if r["kind"] == "module"]
    ast_index   = build_ast_index(ast_modules)

    stats = Counter()
    matched_modules: set[str] = set()

    # Only process symbol nodes (non-L1 file_type=code)
    symbol_nodes = [
        n for n in nodes
        if n.get("source_location", "L1") != "L1"
        and n.get("file_type") == "code"
    ]

    for gnode in symbol_nodes:
        ast_row = match_graphify_node(gnode, ast_index)
        if not ast_row:
            continue

        gid = gnode["id"]
        mkey = ast_row["file"] + "::" + ast_row["name"]
        if mkey in matched_modules:
            continue
        matched_modules.add(mkey)
        stats["matched_modules"] += 1

        # AST summary node (lightweight — no sub-nodes duplicated)
        ast_mid = make_id("ast_mod", ast_row["project"], ast_row["name"])
        if ast_mid not in existing_ids:
            nodes.append({
                "id":           ast_mid,
                "label":        ast_row["name"],
                "file_type":    "ast_module",
                "source_file":  ast_row["file"],
                "source_location": f"L{ast_row['line_start']}",
                "community":    gnode.get("community", 0),
                "norm_label":   ast_row["name"],
                "port_count":   len(ast_row["ports"]),
                "param_count":  len(ast_row["params"]),
                "always_count": len(ast_row["always_blocks"]),
                "fn_count":     len(ast_row["functions"]),
                "parse_errors": ast_row["parse_errors"],
            })
            existing_ids.add(ast_mid)

        # HAS_AST edge: graphify symbol → ast_module
        links.append({
            "source":      gid,
            "target":      ast_mid,
            "relation":    "has_ast",
            "confidence":  "EXTRACTED",
            "weight":      1.0,
            "source_file": ast_row["file"],
            "source_location": f"L{ast_row['line_start']}",
        })
        stats["has_ast_edges"] += 1

        # ── ports ────────────────────────────────────────────────────────
        for port in ast_row["ports"]:
            pid = make_id("ast_port", ast_row["project"], ast_row["name"], port["name"])
            if pid not in existing_ids:
                nodes.append({
                    "id":           pid,
                    "label":        port["name"],
                    "file_type":    "ast_port",
                    "source_file":  ast_row["file"],
                    "source_location": f"L{ast_row['line_start']}",
                    "community":    gnode.get("community", 0),
                    "norm_label":   port["name"],
                    "direction":    port["direction"],
                    "dtype":        port["dtype"],
                    "width":        port["width"],
                    "module":       ast_row["name"],
                })
                existing_ids.add(pid)
                stats["ast_port_nodes"] += 1
            links.append({
                "source":      ast_mid,
                "target":      pid,
                "relation":    "ast_has_port",
                "confidence":  "EXTRACTED",
                "weight":      1.0,
                "source_file": ast_row["file"],
                "source_location": f"L{ast_row['line_start']}",
            })

        # ── parameters ───────────────────────────────────────────────────
        for param in ast_row["params"]:
            if not param.get("name"):
                continue
            pmid = make_id("ast_param", ast_row["project"], ast_row["name"], param["name"])
            if pmid not in existing_ids:
                nodes.append({
                    "id":           pmid,
                    "label":        param["name"],
                    "file_type":    "ast_param",
                    "source_file":  ast_row["file"],
                    "source_location": f"L{ast_row['line_start']}",
                    "community":    gnode.get("community", 0),
                    "norm_label":   param["name"],
                    "dtype":        param["dtype"],
                    "default":      param["default"],
                    "module":       ast_row["name"],
                })
                existing_ids.add(pmid)
                stats["ast_param_nodes"] += 1
            links.append({
                "source":      ast_mid,
                "target":      pmid,
                "relation":    "ast_has_param",
                "confidence":  "EXTRACTED",
                "weight":      1.0,
                "source_file": ast_row["file"],
                "source_location": f"L{ast_row['line_start']}",
            })

        # ── always blocks ─────────────────────────────────────────────────
        for idx, ab in enumerate(ast_row["always_blocks"]):
            aid = make_id("ast_always", ast_row["project"], ast_row["name"], str(idx))
            if aid not in existing_ids:
                nodes.append({
                    "id":           aid,
                    "label":        f"{ast_row['name']}.always_{idx}",
                    "file_type":    "ast_always",
                    "source_file":  ast_row["file"],
                    "source_location": f"L{ast_row['line_start']}",
                    "community":    gnode.get("community", 0),
                    "norm_label":   ab["kind"] or "always",
                    "always_kind":  ab["kind"],
                    "lhs_signals":  ab["lhs_signals"],
                    "module":       ast_row["name"],
                })
                existing_ids.add(aid)
                stats["ast_always_nodes"] += 1
            links.append({
                "source":      ast_mid,
                "target":      aid,
                "relation":    "ast_has_always",
                "confidence":  "EXTRACTED",
                "weight":      1.0,
                "source_file": ast_row["file"],
                "source_location": f"L{ast_row['line_start']}",
            })

        # ── functions ─────────────────────────────────────────────────────
        for fn in ast_row["functions"]:
            if not fn.get("name"):
                continue
            fid = make_id("ast_fn", ast_row["project"], ast_row["name"], fn["name"])
            if fid not in existing_ids:
                nodes.append({
                    "id":           fid,
                    "label":        fn["name"],
                    "file_type":    "ast_function",
                    "source_file":  ast_row["file"],
                    "source_location": f"L{ast_row['line_start']}",
                    "community":    gnode.get("community", 0),
                    "norm_label":   fn["name"],
                    "return_type":  fn["return_type"],
                    "module":       ast_row["name"],
                })
                existing_ids.add(fid)
                stats["ast_fn_nodes"] += 1
            links.append({
                "source":      ast_mid,
                "target":      fid,
                "relation":    "ast_has_fn",
                "confidence":  "EXTRACTED",
                "weight":      1.0,
                "source_file": ast_row["file"],
                "source_location": f"L{ast_row['line_start']}",
            })

    return {"nodes": nodes, "links": links}, dict(stats)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--graph",     required=True, help="graphify graph.json")
    ap.add_argument("--ast-nodes", required=True, help="ibex_ast_nodes.jsonl")
    ap.add_argument("--out",       required=True, help="output graph.json path")
    args = ap.parse_args()

    print(f"Loading graph: {args.graph}")
    with open(args.graph, encoding="utf-8") as f:
        graph = json.load(f)

    ast_rows = read_jsonl(Path(args.ast_nodes))
    print(f"AST rows: {len(ast_rows)}")
    print(f"Existing nodes: {len(graph.get('nodes',[]))}  links: {len(graph.get('links',[]))}")

    enriched, stats = enrich(graph, ast_rows)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(enriched, f, ensure_ascii=False, separators=(",", ":"))

    result = {
        "status":       "ok",
        "output":       str(out),
        "nodes_before": len(graph.get("nodes", [])),
        "nodes_after":  len(enriched["nodes"]),
        "links_before": len(graph.get("links", [])),
        "links_after":  len(enriched["links"]),
        "new_nodes":    len(enriched["nodes"]) - len(graph.get("nodes", [])),
        "new_links":    len(enriched["links"]) - len(graph.get("links", [])),
        **stats,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
