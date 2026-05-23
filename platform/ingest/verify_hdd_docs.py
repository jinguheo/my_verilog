#!/usr/bin/env python3
"""
Verify HDD documents against current source files using tree-sitter.

For each <module>.json in out/hdd/:
  1. Re-parses the source file via tree-sitter
  2. Checks every claim in doc["claims"] against re-extracted AST
  3. Updates doc["verification"] with PASS / FAIL / STALE per claim
  4. Writes a verification report

Claim verification logic:
  port_count          → re-count ports from AST == doc value
  param_count         → re-count params from AST == doc value
  always_ff_count     → re-count always_ff blocks
  always_comb_count   → re-count always_comb blocks
  function_count      → re-count functions
  port_<name>         → port still exists with same direction/dtype/width
  param_<name>        → param still exists with same default

Usage:
  python verify_hdd_docs.py \
    --hdd-dir  out/hdd \
    --rtl-root dbs/ibex \
    --out      out/hdd/verification_report.json
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

try:
    import tree_sitter_verilog as tsverilog
    from tree_sitter import Language, Parser, Node
    _LANG   = Language(tsverilog.language())
    _PARSER = Parser(_LANG)
    HAS_TS  = True
except ImportError:
    HAS_TS = False


# ── re-use extraction helpers from extract_ast_nodes ─────────────────────────

def _text(node: Node, src: bytes) -> str:
    return src[node.start_byte:node.end_byte].decode("utf-8", errors="replace").strip()

def _find_first(node: Node, *types: str):
    if node.type in types:
        return node
    for c in node.children:
        r = _find_first(c, *types)
        if r:
            return r
    return None

def _find_all(node: Node, *types: str) -> list:
    r = []
    if node.type in types:
        r.append(node)
    for c in node.children:
        r.extend(_find_all(c, *types))
    return r

def _identifier(node: Node, src: bytes) -> str:
    ident = _find_first(node, "simple_identifier", "escaped_identifier")
    return _text(ident, src) if ident else ""


def reextract_module(src_file: Path, module_name: str) -> dict | None:
    """Re-parse src_file and extract the named module's AST facts."""
    if not HAS_TS:
        return None
    try:
        src = src_file.read_bytes()
    except OSError:
        return None
    src_clean = re.sub(
        rb"^\s*`\s*(include|define|ifdef|ifndef|elsif|else|endif|undef|timescale)[^\n]*",
        b"", src, flags=re.MULTILINE,
    )
    try:
        tree = _PARSER.parse(src_clean)
    except Exception:
        return None

    for mod_node in _find_all(tree.root_node, "module_declaration"):
        header = _find_first(mod_node, "module_header", "module_ansi_header")
        if not header:
            continue
        mid = _find_first(header, "simple_identifier", "escaped_identifier")
        if not mid or _text(mid, src_clean) != module_name:
            continue

        # ports
        ports: list[dict] = []
        for pd in _find_all(mod_node, "ansi_port_declaration"):
            dir_n = _find_first(pd, "port_direction")
            direction = _text(dir_n, src_clean) if dir_n else ""
            dim = _find_first(pd, "packed_dimension")
            width = ""
            if dim:
                cr = _find_first(dim, "constant_range")
                width = _text(cr, src_clean) if cr else _text(dim, src_clean)
            dt = _find_first(pd, "integer_vector_type", "integer_atom_type")
            dtype = ""
            if dt:
                kw = _find_first(dt, "logic","wire","reg","bit","integer","int")
                dtype = _text(kw, src_clean) if kw else _text(dt, src_clean).split()[0]
            name_n = _find_first(pd, "port_identifier")
            pname = _identifier(name_n, src_clean) if name_n else _identifier(pd, src_clean)
            if pname:
                ports.append({"name": pname, "direction": direction, "dtype": dtype, "width": width})

        # params
        params: list[dict] = []
        for pdecl in _find_all(mod_node, "parameter_declaration"):
            name_n = _find_first(pdecl, "parameter_identifier")
            pname = _identifier(name_n, src_clean) if name_n else ""
            default = ""
            assign_n = _find_first(pdecl, "param_assignment")
            if assign_n:
                eq_seen = False
                for ch in assign_n.children:
                    if ch.type == "=":
                        eq_seen = True
                        continue
                    if eq_seen:
                        default = _text(ch, src_clean)
                        break
            dt = _find_first(pdecl, "data_type_or_implicit1", "data_type")
            dtype = _text(dt, src_clean).split()[0] if dt else ""
            if pname:
                params.append({"name": pname, "dtype": dtype, "default": default})

        # always blocks
        always_kinds = [_text(_find_first(ab, "always_keyword"), src_clean) if _find_first(ab, "always_keyword") else "always"
                        for ab in _find_all(mod_node, "always_construct")]
        ak_counter = Counter(always_kinds)

        # functions
        fns = []
        for fn in _find_all(mod_node, "function_declaration"):
            body = _find_first(fn, "function_body_declaration")
            fn_id = _find_first(body, "function_identifier") if body else None
            fname = _identifier(fn_id, src_clean) if fn_id else ""
            if fname:
                fns.append(fname)

        return {
            "ports":       ports,
            "params":      params,
            "always_ff":   ak_counter.get("always_ff", 0),
            "always_comb": ak_counter.get("always_comb", 0),
            "functions":   fns,
        }
    return None


def verify_claims(claims: list[dict], current: dict) -> list[dict]:
    """Compare each claim against re-extracted values. Returns updated claims."""
    port_by_name  = {p["name"]: p for p in current.get("ports",  [])}
    param_by_name = {p["name"]: p for p in current.get("params", [])}
    updated = []

    for c in claims:
        cid   = c["id"]
        expected = c["value"]
        result = c.copy()
        result["current_value"] = None

        if cid == "port_count":
            cur = len(current["ports"])
            result["current_value"] = cur
            result["verified"]      = (cur == expected)
            result["status"]        = "PASS" if cur == expected else "FAIL"

        elif cid == "param_count":
            cur = len(current["params"])
            result["current_value"] = cur
            result["verified"]      = (cur == expected)
            result["status"]        = "PASS" if cur == expected else "FAIL"

        elif cid == "always_ff_count":
            cur = current["always_ff"]
            result["current_value"] = cur
            result["verified"]      = (cur == expected)
            result["status"]        = "PASS" if cur == expected else "FAIL"

        elif cid == "always_comb_count":
            cur = current["always_comb"]
            result["current_value"] = cur
            result["verified"]      = (cur == expected)
            result["status"]        = "PASS" if cur == expected else "FAIL"

        elif cid == "function_count":
            cur = len(current["functions"])
            result["current_value"] = cur
            result["verified"]      = (cur == expected)
            result["status"]        = "PASS" if cur == expected else "FAIL"

        elif cid.startswith("port_"):
            pname = cid[5:]
            cur_port = port_by_name.get(pname)
            if cur_port is None:
                result["verified"]      = False
                result["status"]        = "FAIL"
                result["current_value"] = None
                result["detail"]        = "port no longer exists"
            else:
                match = (cur_port["direction"] == expected.get("direction","")
                         and cur_port["dtype"]     == expected.get("dtype","")
                         and cur_port["width"]     == expected.get("width",""))
                result["current_value"] = cur_port
                result["verified"]      = match
                result["status"]        = "PASS" if match else "FAIL"

        elif cid.startswith("param_"):
            pname = cid[6:]
            cur_p = param_by_name.get(pname)
            if cur_p is None:
                result["verified"]      = False
                result["status"]        = "FAIL"
                result["current_value"] = None
                result["detail"]        = "param no longer exists"
            else:
                match = cur_p["default"] == expected.get("default","")
                result["current_value"] = cur_p
                result["verified"]      = match
                result["status"]        = "PASS" if match else "FAIL"

        else:
            result["status"]   = "SKIP"
            result["verified"] = None

        updated.append(result)
    return updated


# ── main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hdd-dir",  required=True, help="out/hdd directory")
    ap.add_argument("--rtl-root", required=True, help="dbs/ibex (RTL source root)")
    ap.add_argument("--out",      required=True, help="verification_report.json output path")
    ap.add_argument("--filter",   default="",    help="only verify modules matching substring")
    args = ap.parse_args()

    if not HAS_TS:
        sys.exit("tree-sitter-verilog not installed")

    hdd_dir  = Path(args.hdd_dir)
    rtl_root = Path(args.rtl_root)
    now_str  = datetime.now(timezone.utc).isoformat()

    doc_files = sorted(hdd_dir.rglob("*.json"))
    doc_files = [p for p in doc_files
                 if p.name != "index.json"
                 and "verification" not in p.name]
    if args.filter:
        doc_files = [p for p in doc_files if args.filter.lower() in p.stem.lower()]

    print(f"Verifying {len(doc_files)} HDD docs against {rtl_root} …")

    report_rows: list[dict] = []
    total_pass = total_fail = total_skip = 0

    for doc_path in sorted(doc_files):
        with open(doc_path, encoding="utf-8") as f:
            doc = json.load(f)

        module_name = doc["module"]
        src_file_rel = doc.get("source_file", "")

        # Resolve source file: try relative to rtl_root first, then absolute
        src_path = rtl_root / src_file_rel
        if not src_path.exists():
            # strip leading "ibex/" or "dbs/ibex/"
            for strip in ("dbs/ibex/", "ibex/", "dbs\\ibex\\", "ibex\\"):
                candidate = rtl_root / src_file_rel.replace("\\","/").lstrip("/").split("/",1)[-1]
                if candidate.exists():
                    src_path = candidate
                    break
            else:
                # search by filename
                hits = list(rtl_root.rglob(Path(src_file_rel).name))
                src_path = hits[0] if hits else None

        if not src_path or not src_path.exists():
            row = {
                "module": module_name,
                "status": "SOURCE_NOT_FOUND",
                "pass": 0, "fail": 0, "skip": len(doc["claims"]),
                "source_file": str(src_file_rel),
            }
            report_rows.append(row)
            total_skip += len(doc["claims"])
            continue

        current = reextract_module(src_path, module_name)
        if current is None:
            row = {
                "module": module_name,
                "status": "PARSE_FAILED",
                "pass": 0, "fail": 0, "skip": len(doc["claims"]),
                "source_file": str(src_path),
            }
            report_rows.append(row)
            total_skip += len(doc["claims"])
            continue

        updated_claims = verify_claims(doc["claims"], current)
        n_pass = sum(1 for c in updated_claims if c.get("status") == "PASS")
        n_fail = sum(1 for c in updated_claims if c.get("status") == "FAIL")
        n_skip = sum(1 for c in updated_claims if c.get("status") == "SKIP")
        total  = len(updated_claims)
        status = "PASS" if n_fail == 0 and n_pass > 0 else ("FAIL" if n_fail > 0 else "SKIP")

        # Update doc in-place
        doc["claims"] = updated_claims
        doc["verification"] = {
            "status":  status,
            "pass":    n_pass,
            "fail":    n_fail,
            "skip":    n_skip,
            "total":   total,
            "run_at":  now_str,
            "source_resolved": str(src_path),
        }
        with open(doc_path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)

        # Re-render markdown with updated verification status
        md_path = doc_path.with_suffix(".md")
        if md_path.exists():
            lines = md_path.read_text(encoding="utf-8").split("\n")
            # Replace verification section
            try:
                vi = next(i for i, l in enumerate(lines) if l.startswith("## Verification"))
                lines = lines[:vi] + [
                    "## Verification Status",
                    "",
                    f"**Status**: {status}  ",
                    f"**Claims**: {total} total · {n_pass} pass · {n_fail} fail · {n_skip} skip  ",
                    f"**Last run**: {now_str[:19].replace('T',' ')} UTC",
                    "",
                ]
                if n_fail > 0:
                    lines.append("### Failed Claims")
                    lines.append("")
                    for c in updated_claims:
                        if c.get("status") == "FAIL":
                            lines.append(f"- `{c['id']}`: expected `{c['value']}` — got `{c.get('current_value','?')}`{' — ' + c['detail'] if c.get('detail') else ''}")
                    lines.append("")
                md_path.write_text("\n".join(lines), encoding="utf-8")
            except StopIteration:
                pass

        total_pass += n_pass
        total_fail += n_fail
        total_skip += n_skip
        report_rows.append({
            "module":      module_name,
            "status":      status,
            "pass":        n_pass,
            "fail":        n_fail,
            "skip":        n_skip,
            "total":       total,
            "pass_rate":   round(n_pass / total, 3) if total else 0.0,
            "source_file": str(src_path),
        })
        if n_fail:
            print(f"  FAIL  {module_name}: {n_fail}/{total} claims failed")

    overall_total = total_pass + total_fail + total_skip
    report = {
        "run_at":      now_str,
        "rtl_root":    str(rtl_root),
        "total_docs":  len(doc_files),
        "total_claims": overall_total,
        "total_pass":  total_pass,
        "total_fail":  total_fail,
        "total_skip":  total_skip,
        "pass_rate":   round(total_pass / (total_pass + total_fail), 4) if (total_pass + total_fail) > 0 else 0.0,
        "modules":     report_rows,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(json.dumps({
        "status":      "ok",
        "pass_rate":   report["pass_rate"],
        "total_pass":  total_pass,
        "total_fail":  total_fail,
        "total_skip":  total_skip,
        "report":      str(out),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
