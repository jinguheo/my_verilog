#!/usr/bin/env python3
"""
Tree-sitter based AST extractor for Verilog / SystemVerilog.

Extracts structured AST nodes from .sv/.v files:
  - modules       (name, params, ports, line range)
  - ports         (direction, type, width expression, name)
  - parameters    (name, type, default value)
  - instances     (module type, instance name, port connections)
  - always_blocks (kind: ff/comb/latch/generic, sensitivity list)
  - functions     (name, return type, input ports)
  - packages      (name, contents summary)
  - assigns       (lhs signal name, one-liner)

Output: JSONL, one row per AST entity.

Usage:
  python extract_ast_nodes.py \
    --root  dbs/ibex \
    --project ibex \
    --out   out/ast/ibex_ast_nodes.jsonl
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import tree_sitter_verilog as tsverilog
    from tree_sitter import Language, Parser, Node
except ImportError:
    sys.exit("tree-sitter-verilog not installed. pip install tree-sitter tree-sitter-verilog")

# ── tree-sitter setup ────────────────────────────────────────────────────────
_LANG   = Language(tsverilog.language())
_PARSER = Parser(_LANG)


# ── helpers ──────────────────────────────────────────────────────────────────

def _text(node: Node, src: bytes) -> str:
    return src[node.start_byte:node.end_byte].decode("utf-8", errors="replace").strip()


def _find_first(node: Node, *types: str) -> Node | None:
    if node.type in types:
        return node
    for child in node.children:
        found = _find_first(child, *types)
        if found:
            return found
    return None


def _find_all(node: Node, *types: str) -> list[Node]:
    results: list[Node] = []
    if node.type in types:
        results.append(node)
    for child in node.children:
        results.extend(_find_all(child, *types))
    return results


def _identifier(node: Node, src: bytes) -> str:
    ident = _find_first(node, "simple_identifier", "escaped_identifier")
    return _text(ident, src) if ident else ""


# ── port extraction ──────────────────────────────────────────────────────────

def _extract_port(node: Node, src: bytes) -> dict[str, Any]:
    direction = ""
    dir_node = _find_first(node, "port_direction")
    if dir_node:
        direction = _text(dir_node, src)

    # width: look for packed_dimension → constant_range
    width = ""
    dim = _find_first(node, "packed_dimension")
    if dim:
        cr = _find_first(dim, "constant_range")
        width = _text(cr, src) if cr else _text(dim, src)

    # data type keyword (logic, wire, reg, …)
    dtype = ""
    dt = _find_first(node, "integer_vector_type", "integer_atom_type",
                     "net_type", "data_type")
    if dt:
        kw = _find_first(dt, "logic", "wire", "reg", "bit",
                         "integer", "int", "byte", "longint",
                         "shortint", "real", "realtime", "time")
        dtype = _text(kw, src) if kw else _text(dt, src).split()[0]

    name_node = _find_first(node, "port_identifier")
    name = _identifier(name_node, src) if name_node else _identifier(node, src)

    return {
        "direction": direction,
        "dtype":     dtype,
        "width":     width,
        "name":      name,
    }


# ── parameter extraction ─────────────────────────────────────────────────────

def _extract_param(node: Node, src: bytes) -> dict[str, Any]:
    name_node = _find_first(node, "parameter_identifier")
    name = _identifier(name_node, src) if name_node else ""

    default = ""
    assign_node = _find_first(node, "param_assignment")
    if assign_node:
        # value after "="
        eq_seen = False
        for ch in assign_node.children:
            if ch.type == "=":
                eq_seen = True
                continue
            if eq_seen:
                default = _text(ch, src)
                break

    dtype = ""
    dt = _find_first(node, "data_type_or_implicit1", "data_type")
    if dt:
        dtype = _text(dt, src).split()[0] if dt else ""

    return {"name": name, "dtype": dtype, "default": default}


# ── module instantiation extraction ─────────────────────────────────────────

def _extract_instance(node: Node, src: bytes) -> dict[str, Any]:
    # module_instantiation: first child is the module type name
    # Grammar may use module_identifier or bare simple_identifier
    mod_id = _find_first(node, "module_identifier")
    if mod_id:
        mod_type = _identifier(mod_id, src)
    else:
        # direct simple_identifier as first named child
        for ch in node.children:
            if ch.type == "simple_identifier":
                mod_type = _text(ch, src)
                break
        else:
            mod_type = ""

    instances: list[dict[str, str]] = []
    for hier in _find_all(node, "hierarchical_instance"):
        inst_id = _find_first(hier, "name_of_instance")
        inst_name = _identifier(inst_id, src) if inst_id else ""
        # port connections (named: .port(expr))
        connections: list[dict[str, str]] = []
        for conn in _find_all(hier, "named_port_connection"):
            port_id = _find_first(conn, "port_identifier")
            pname = _identifier(port_id, src) if port_id else ""
            # expression after the port name
            exprs = [ch for ch in conn.children
                     if ch.type not in (".", ",", "(", ")", "port_identifier")]
            expr_text = _text(exprs[0], src) if exprs else ""
            connections.append({"port": pname, "expr": expr_text})
        instances.append({"instance_name": inst_name, "connections": connections})

    return {"module_type": mod_type, "instances": instances}


# ── always block extraction ──────────────────────────────────────────────────

def _extract_always(node: Node, src: bytes) -> dict[str, Any]:
    kw_node = _find_first(node, "always_keyword")
    kind = _text(kw_node, src) if kw_node else "always"   # always_ff/comb/latch

    # sensitivity list for plain always
    sens: list[str] = []
    el = _find_first(node, "event_expression")
    if el:
        for ev in _find_all(el, "event_expression"):
            t = _text(ev, src)
            if t not in sens:
                sens.append(t)

    # collect signals referenced on LHS (blocking/nonblocking assignments)
    lhs_signals: list[str] = []
    for asgn in _find_all(node, "blocking_assignment", "nonblocking_assignment"):
        lv = _find_first(asgn, "variable_lvalue")
        if lv:
            sig = _identifier(_find_first(lv, "simple_identifier") or lv, src)
            if sig and sig not in lhs_signals:
                lhs_signals.append(sig)

    return {
        "kind":        kind,
        "sensitivity": sens,
        "lhs_signals": lhs_signals[:16],   # cap for size
    }


# ── function extraction ──────────────────────────────────────────────────────

def _extract_function(node: Node, src: bytes) -> dict[str, Any]:
    body = _find_first(node, "function_body_declaration")
    if not body:
        return {}
    fn_id = _find_first(body, "function_identifier")
    name = _identifier(fn_id, src) if fn_id else ""

    ret_type = ""
    rt = _find_first(body, "function_data_type_or_implicit1")
    if rt:
        ret_type = _text(rt, src).strip()

    ports: list[dict[str, str]] = []
    for tp in _find_all(body, "tf_port_item1"):
        pdir_node = _find_first(tp, "port_direction")
        pdir = _text(pdir_node, src) if pdir_node else "input"
        pid  = _find_first(tp, "port_identifier")
        pname = _identifier(pid, src) if pid else ""
        ports.append({"direction": pdir, "name": pname})

    return {"name": name, "return_type": ret_type, "ports": ports}


# ── module extraction ────────────────────────────────────────────────────────

def _extract_module(node: Node, src: bytes, file_path: str, project: str) -> dict[str, Any]:
    header = _find_first(node, "module_header", "module_ansi_header")
    name = ""
    if header:
        mid = _find_first(header, "simple_identifier", "escaped_identifier")
        name = _text(mid, src) if mid else ""
    if not name:
        name = _identifier(node, src)

    # parameters
    params: list[dict] = []
    for pdecl in _find_all(node, "parameter_declaration"):
        p = _extract_param(pdecl, src)
        if p.get("name"):
            params.append(p)

    # ports (ANSI style)
    ports: list[dict] = []
    for pdecl in _find_all(node, "ansi_port_declaration"):
        p = _extract_port(pdecl, src)
        if p.get("name"):
            ports.append(p)

    # instances
    instances: list[dict] = []
    for inst in _find_all(node, "module_instantiation"):
        i = _extract_instance(inst, src)
        if i.get("module_type"):
            instances.append(i)

    # always blocks
    always_blocks: list[dict] = []
    for ab in _find_all(node, "always_construct"):
        always_blocks.append(_extract_always(ab, src))

    # functions
    functions: list[dict] = []
    for fn in _find_all(node, "function_declaration"):
        f = _extract_function(fn, src)
        if f.get("name"):
            functions.append(f)

    # assign statements — just lhs names
    assigns: list[str] = []
    for ca in _find_all(node, "continuous_assign"):
        for na in _find_all(ca, "net_assignment"):
            lv = _find_first(na, "net_lvalue")
            if lv:
                sig = _identifier(_find_first(lv, "simple_identifier") or lv, src)
                if sig and sig not in assigns:
                    assigns.append(sig)

    return {
        "kind":         "module",
        "name":         name,
        "project":      project,
        "file":         file_path,
        "line_start":   node.start_point[0] + 1,
        "line_end":     node.end_point[0] + 1,
        "params":       params,
        "ports":        ports,
        "instances":    instances,
        "always_blocks": always_blocks,
        "functions":    functions,
        "assigns":      assigns[:32],
        "parse_errors": node.has_error,
    }


# ── package extraction ───────────────────────────────────────────────────────

def _extract_package(node: Node, src: bytes, file_path: str, project: str) -> dict[str, Any]:
    name = ""
    pkg_id = _find_first(node, "package_identifier")
    if pkg_id:
        name = _identifier(pkg_id, src)

    typedefs: list[str] = []
    for td in _find_all(node, "type_declaration"):
        tid = _find_first(td, "simple_identifier")
        if tid:
            typedefs.append(_text(tid, src))

    params: list[dict] = []
    for pdecl in _find_all(node, "parameter_declaration"):
        p = _extract_param(pdecl, src)
        if p.get("name"):
            params.append(p)

    return {
        "kind":      "package",
        "name":      name,
        "project":   project,
        "file":      file_path,
        "line_start": node.start_point[0] + 1,
        "line_end":   node.end_point[0] + 1,
        "typedefs":  typedefs,
        "params":    params,
    }


# ── file parser ──────────────────────────────────────────────────────────────

def parse_file(path: Path, project: str) -> list[dict[str, Any]]:
    try:
        src = path.read_bytes()
    except OSError:
        return []

    # strip `include and `define lines that confuse the parser
    src_clean = re.sub(rb"^\s*`\s*(include|define|ifdef|ifndef|elsif|else|endif|undef|timescale)[^\n]*",
                       b"", src, flags=re.MULTILINE)

    try:
        tree = _PARSER.parse(src_clean)
    except Exception:
        return []

    root = tree.root_node
    file_str = str(path)
    entities: list[dict] = []

    for node in _find_all(root, "module_declaration"):
        entities.append(_extract_module(node, src_clean, file_str, project))

    for node in _find_all(root, "package_declaration"):
        entities.append(_extract_package(node, src_clean, file_str, project))

    return entities


# ── main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root",    required=True, help="RTL source root directory")
    ap.add_argument("--project", required=True, help="project name tag")
    ap.add_argument("--out",     required=True, help="output JSONL path")
    ap.add_argument("--exts",    default=".sv,.v", help="comma-separated file extensions")
    args = ap.parse_args()

    root = Path(args.root)
    out  = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    exts = set(args.exts.split(","))

    files = [p for p in root.rglob("*") if p.suffix in exts and p.is_file()]
    print(f"Parsing {len(files)} files from {root} …")

    total_modules = total_packages = total_errors = 0
    written = 0

    with out.open("w", encoding="utf-8") as fout:
        for i, path in enumerate(sorted(files), 1):
            entities = parse_file(path, args.project)
            for ent in entities:
                fout.write(json.dumps(ent, ensure_ascii=False) + "\n")
                written += 1
                if ent["kind"] == "module":
                    total_modules += 1
                    if ent.get("parse_errors"):
                        total_errors += 1
                elif ent["kind"] == "package":
                    total_packages += 1
            if i % 100 == 0:
                print(f"  {i}/{len(files)} files …")

    summary = {
        "project":        args.project,
        "files_parsed":   len(files),
        "modules":        total_modules,
        "packages":       total_packages,
        "parse_errors":   total_errors,
        "output":         str(out),
    }
    summary_path = out.with_suffix(".summary.json")
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
