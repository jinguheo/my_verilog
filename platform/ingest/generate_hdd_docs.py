#!/usr/bin/env python3
"""
Generate Hardware Design Documents (HDD) from AST-enriched graphify graph.

For each ast_module node in the enriched graph:
  1. Pulls ports, params, always blocks, functions from AST sub-nodes
  2. Pulls graphify relationships (calls, instantiates, imports_from, defines)
  3. Writes:
     - out/hdd/<project>/<module>.json   — machine-readable, verifiable claims
     - out/hdd/<project>/<module>.md     — human-readable markdown

Each claim in the JSON has:
  { "id": "<claim_id>", "value": <value>, "source_ref": "<file>:<line>", "verified": null }

Usage:
  python generate_hdd_docs.py \
    --graph   out/ast/code-only-ast-enriched.json \
    --out-dir out/hdd
"""
from __future__ import annotations
import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


# ── helpers ──────────────────────────────────────────────────────────────────

def load_graph(path: Path) -> tuple[dict, dict, list]:
    with open(path, encoding="utf-8") as f:
        g = json.load(f)
    node_by_id = {n["id"]: n for n in g["nodes"]}
    # adjacency: source_id → [(relation, target_node)]
    adj: dict[str, list] = defaultdict(list)
    radj: dict[str, list] = defaultdict(list)
    for l in g["links"]:
        src, tgt, rel = l.get("source",""), l.get("target",""), l.get("relation","")
        if src in node_by_id and tgt in node_by_id:
            adj[src].append((rel, node_by_id[tgt], l))
            radj[tgt].append((rel, node_by_id[src], l))
    return node_by_id, adj, radj


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


# ── claim builders ────────────────────────────────────────────────────────────

def claim(cid: str, value, src_file: str, src_line: int | str) -> dict:
    return {
        "id":         cid,
        "value":      value,
        "source_ref": f"{src_file}:{src_line}",
        "verified":   None,   # filled by verify_hdd_docs.py
    }


# ── document builder ──────────────────────────────────────────────────────────

def build_hdd(ast_mod: dict, adj: dict, radj: dict, node_by_id: dict) -> dict:
    mid    = ast_mod["id"]
    name   = ast_mod["label"]
    project= ast_mod.get("project", "")  # may not be set on graphify nodes
    src    = ast_mod.get("source_file", "")
    lstart = ast_mod.get("source_location", "L?").lstrip("L")
    now    = datetime.now(timezone.utc).isoformat()

    # ── collect AST sub-nodes ─────────────────────────────────────────────────
    ports:    list[dict] = []
    params:   list[dict] = []
    always:   list[dict] = []
    functions: list[dict] = []

    for rel, tgt, lnk in adj.get(mid, []):
        ft = tgt.get("file_type", "")
        if rel == "ast_has_port":
            ports.append(tgt)
        elif rel == "ast_has_param":
            params.append(tgt)
        elif rel == "ast_has_always":
            always.append(tgt)
        elif rel == "ast_has_fn":
            functions.append(tgt)

    # ── graphify relationships ────────────────────────────────────────────────
    # Find the graphify code symbol node (has_ast → this ast_mod)
    gf_syms = [n for rel, n, _ in radj.get(mid, []) if rel == "has_ast"]
    gf_sym  = gf_syms[0] if gf_syms else None
    gf_id   = gf_sym["id"] if gf_sym else None

    calls_out:    list[str] = []
    instantiates: list[str] = []
    imported_by:  list[str] = []
    imports_from: list[str] = []

    if gf_id:
        for rel, tgt, _ in adj.get(gf_id, []):
            lbl = tgt.get("label", "?")
            if rel == "calls":
                calls_out.append(lbl)
            elif rel == "instantiates":
                instantiates.append(lbl)
            elif rel == "imports_from":
                imports_from.append(lbl)
        for rel, src_n, _ in radj.get(gf_id, []):
            if rel == "calls":
                imported_by.append(src_n.get("label", "?"))

    # ── claims list ──────────────────────────────────────────────────────────
    claims: list[dict] = []

    # structural claims
    claims.append(claim("port_count",        len(ports),    src, lstart))
    claims.append(claim("param_count",       len(params),   src, lstart))
    claims.append(claim("always_ff_count",   sum(1 for a in always if a.get("always_kind") == "always_ff"),   src, lstart))
    claims.append(claim("always_comb_count", sum(1 for a in always if a.get("always_kind") == "always_comb"), src, lstart))
    claims.append(claim("function_count",    len(functions), src, lstart))

    # per-port claims
    for p in ports:
        claims.append(claim(
            f"port_{p['label']}",
            {"direction": p.get("direction",""), "dtype": p.get("dtype",""), "width": p.get("width","")},
            src, lstart,
        ))

    # per-param claims
    for p in params:
        claims.append(claim(
            f"param_{p['label']}",
            {"dtype": p.get("dtype",""), "default": p.get("default","")},
            src, lstart,
        ))

    return {
        "module":         name,
        "project":        project,
        "source_file":    src,
        "line_start":     lstart,
        "generated_at":   now,
        "parse_errors":   ast_mod.get("parse_errors", False),
        "summary": {
            "port_count":    len(ports),
            "param_count":   len(params),
            "always_ff":     sum(1 for a in always if a.get("always_kind") == "always_ff"),
            "always_comb":   sum(1 for a in always if a.get("always_kind") == "always_comb"),
            "always_latch":  sum(1 for a in always if a.get("always_kind") == "always_latch"),
            "function_count": len(functions),
        },
        "ports":     [{"name": p["label"], "direction": p.get("direction",""), "dtype": p.get("dtype",""), "width": p.get("width","")} for p in ports],
        "params":    [{"name": p["label"], "dtype": p.get("dtype",""), "default": p.get("default","")} for p in params],
        "always":    [{"kind": a.get("always_kind",""), "lhs_signals": a.get("lhs_signals",[])} for a in always],
        "functions": [{"name": f["label"], "return_type": f.get("return_type","")} for f in functions],
        "graphify_relations": {
            "calls":        calls_out[:20],
            "instantiates": instantiates[:20],
            "imports_from": imports_from[:20],
            "called_by":    imported_by[:20],
        },
        "claims": claims,
        "verification": {
            "status":    "NOT_RUN",
            "pass":      0,
            "fail":      0,
            "total":     len(claims),
            "run_at":    None,
        },
    }


# ── markdown renderer ─────────────────────────────────────────────────────────

def render_md(doc: dict) -> str:
    s = doc["summary"]
    rel = doc["graphify_relations"]
    lines = [
        f"# {doc['module']}",
        "",
        f"**File**: `{doc['source_file']}` (L{doc['line_start']})",
        f"**Project**: {doc['project'] or '—'}",
        f"**Generated**: {doc['generated_at'][:19].replace('T', ' ')} UTC",
        f"**Parse errors**: {'⚠ yes' if doc['parse_errors'] else '✓ none'}",
        "",
        "## Summary",
        "",
        f"| Item | Count |",
        f"|---|---:|",
        f"| Ports | {s['port_count']} |",
        f"| Parameters | {s['param_count']} |",
        f"| always_ff | {s['always_ff']} |",
        f"| always_comb | {s['always_comb']} |",
        f"| always_latch | {s['always_latch']} |",
        f"| Functions | {s['function_count']} |",
        "",
    ]

    # Parameters
    if doc["params"]:
        lines += ["## Parameters", "", "| Name | Type | Default |", "|---|---|---|"]
        for p in doc["params"]:
            lines.append(f"| `{p['name']}` | {p['dtype']} | `{p['default']}` |")
        lines.append("")

    # Ports
    if doc["ports"]:
        lines += ["## Port Interface", "", "| Name | Direction | Type | Width |", "|---|---|---|---|"]
        for p in sorted(doc["ports"], key=lambda x: (x["direction"] != "input", x["name"])):
            lines.append(f"| `{p['name']}` | {p['direction']} | {p['dtype']} | `{p['width'] or '1'}` |")
        lines.append("")

    # Always blocks
    if doc["always"]:
        lines += ["## Behavior", ""]
        ff   = [a for a in doc["always"] if a["kind"] == "always_ff"]
        comb = [a for a in doc["always"] if a["kind"] == "always_comb"]
        ltch = [a for a in doc["always"] if a["kind"] == "always_latch"]
        if ff:
            lines.append(f"**Clocked (always_ff)** — {len(ff)} block(s)  ")
            for a in ff[:3]:
                sigs = ", ".join(f"`{s}`" for s in a["lhs_signals"][:6])
                lines.append(f"- drives: {sigs or '—'}")
        if comb:
            lines.append(f"\n**Combinational (always_comb)** — {len(comb)} block(s)  ")
            for a in comb[:3]:
                sigs = ", ".join(f"`{s}`" for s in a["lhs_signals"][:6])
                lines.append(f"- drives: {sigs or '—'}")
        if ltch:
            lines.append(f"\n**Latch (always_latch)** — {len(ltch)} block(s)")
        lines.append("")

    # Functions
    if doc["functions"]:
        lines += ["## Functions", "", "| Name | Return Type |", "|---|---|"]
        for f in doc["functions"]:
            lines.append(f"| `{f['name']}` | {f['return_type'] or '—'} |")
        lines.append("")

    # Graphify relations
    lines += ["## Relationships (from graphify)", ""]
    if rel["instantiates"]:
        lines.append("**Instantiates**: " + ", ".join(f"`{x}`" for x in rel["instantiates"]))
    if rel["imports_from"]:
        lines.append("**Imports from**: " + ", ".join(f"`{x}`" for x in rel["imports_from"]))
    if rel["calls"]:
        lines.append("**Calls**: " + ", ".join(f"`{x}`" for x in rel["calls"][:10]))
    if rel["called_by"]:
        lines.append("**Called by**: " + ", ".join(f"`{x}`" for x in rel["called_by"][:10]))
    lines.append("")

    # Verification status
    v = doc["verification"]
    lines += [
        "## Verification Status",
        "",
        f"**Status**: {v['status']}  ",
        f"**Claims**: {v['total']} total · {v['pass']} pass · {v['fail']} fail  ",
        f"**Last run**: {v['run_at'] or 'never'}",
        "",
    ]

    return "\n".join(lines)


# ── main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--graph",   required=True, help="code-only-ast-enriched.json")
    ap.add_argument("--out-dir", required=True, help="output directory for HDD docs")
    ap.add_argument("--filter",  default="",    help="only process modules matching this substring")
    args = ap.parse_args()

    print(f"Loading graph: {args.graph}")
    node_by_id, adj, radj = load_graph(Path(args.graph))

    ast_mods = [n for n in node_by_id.values() if n.get("file_type") == "ast_module"]
    print(f"ast_module nodes: {len(ast_mods)}")
    if args.filter:
        ast_mods = [n for n in ast_mods if args.filter.lower() in n.get("label","").lower()]
        print(f"  filtered to: {len(ast_mods)}")

    out_dir = Path(args.out_dir)
    written = 0

    index: list[dict] = []

    for mod in sorted(ast_mods, key=lambda n: n.get("label","")):
        doc  = build_hdd(mod, adj, radj, node_by_id)
        name = doc["module"]
        proj = doc["project"] or "unknown"

        sub = out_dir / proj
        write_json(sub / f"{name}.json", doc)
        write_text(sub / f"{name}.md",   render_md(doc))
        written += 1

        index.append({
            "module":     name,
            "project":    proj,
            "source_file": doc["source_file"],
            "port_count": doc["summary"]["port_count"],
            "param_count": doc["summary"]["param_count"],
            "parse_errors": doc["parse_errors"],
            "claims":     len(doc["claims"]),
            "json":       str(sub / f"{name}.json"),
            "md":         str(sub / f"{name}.md"),
        })

    write_json(out_dir / "index.json", {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total": written,
        "modules": index,
    })

    print(json.dumps({
        "status":       "ok",
        "docs_written": written,
        "out_dir":      str(out_dir),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
