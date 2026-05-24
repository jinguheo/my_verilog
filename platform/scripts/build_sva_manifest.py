#!/usr/bin/env python3
"""Parse SVA (.sv) files and produce a per-component SVA manifest JSON.

For each SVA file the script extracts:
  - assert property / cover property declarations
  - The sva.* id comment directly above each assertion (if present)
  - The SPEC/REF comment block above each property definition
  - The property name and type (assert / cover / assume)

Output: dbs/graphify-out/sva-manifest/sva_manifest.json
        dbs/graphify-out/sva-manifest/sva_manifest.md  (human-readable)

Usage:
    python build_sva_manifest.py [--sva-dir platform/sva] [--out dbs/graphify-out/sva-manifest]
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SVA_DIR = ROOT / "platform" / "sva"
DEFAULT_OUT = ROOT / "dbs" / "graphify-out" / "sva-manifest"


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

_PROP_DEF  = re.compile(r"\bproperty\s+(\w+)\s*[(\;]")
_ASSERT    = re.compile(r"\bassert\s+property\s*\(\s*(\w+)")
_COVER     = re.compile(r"\bcover\s+property\s*\(\s*(\w+)")
_ASSUME    = re.compile(r"\bassume\s+property\s*\(\s*(\w+)")
_SVA_ID    = re.compile(r"//\s*(sva\.\S+)")
_SPEC_REF  = re.compile(r"//\s*(?:SPEC|REF):\s*(.+)")
_MOD_DECL  = re.compile(r"\bmodule\s+(\w+)")
_BIND_DECL = re.compile(r"\bbind\s+(\w+)\s+(\w+)")


def _strip_comment(line: str) -> str:
    return line.split("//")[0].strip()


def parse_sv_file(path: Path) -> dict:
    """Return structured info extracted from one .sv file."""
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    module_name = ""
    bind_target = ""
    properties: dict[str, dict] = {}   # prop_name -> {lines, spec, ref, sva_id}
    assertions: list[dict] = []        # [{kind, prop_name, sva_id, spec_ref, line_no}]

    # --- Pass 1: module / bind names ---
    for ln in lines:
        m = _MOD_DECL.search(ln)
        if m and not module_name:
            module_name = m.group(1)
        m = _BIND_DECL.search(ln)
        if m:
            bind_target = m.group(1)

    # --- Pass 2: property defs with their preceding comment block ---
    i = 0
    while i < len(lines):
        ln = lines[i]

        m = _PROP_DEF.search(ln)
        if m:
            prop_name = m.group(1)
            # Collect comment block immediately before this line
            spec_lines, ref_lines, sva_ids = [], [], []
            j = i - 1
            while j >= 0 and (lines[j].strip().startswith("//") or lines[j].strip() == ""):
                raw = lines[j].strip()
                sm = _SPEC_REF.match(raw)
                if sm:
                    key = raw.split(":")[0].replace("//", "").strip()
                    val = sm.group(1).strip()
                    if key == "SPEC":
                        spec_lines.insert(0, val)
                    elif key == "REF":
                        ref_lines.insert(0, val)
                idm = _SVA_ID.match(raw)
                if idm:
                    sva_ids.insert(0, idm.group(1))
                j -= 1
            properties[prop_name] = {
                "spec": " ".join(spec_lines),
                "ref": " ".join(ref_lines),
                "sva_id": sva_ids[0] if sva_ids else "",
                "line_no": i + 1,
            }
        i += 1

    # --- Pass 3: assert/cover/assume property usages ---
    for i, ln in enumerate(lines):
        # Gather sva_id from adjacent comment on same or preceding line
        sva_id = ""
        idm = _SVA_ID.search(ln)
        if idm:
            sva_id = idm.group(1)
        elif i > 0:
            idm = _SVA_ID.search(lines[i - 1])
            if idm:
                sva_id = idm.group(1)

        for kind, pattern in [("assert", _ASSERT), ("cover", _COVER), ("assume", _ASSUME)]:
            m = pattern.search(ln)
            if m:
                prop_name = m.group(1)
                prop_meta = properties.get(prop_name, {})
                assertions.append({
                    "kind": kind,
                    "prop_name": prop_name,
                    "sva_id": sva_id or prop_meta.get("sva_id", ""),
                    "spec": prop_meta.get("spec", ""),
                    "ref": prop_meta.get("ref", ""),
                    "line_no": i + 1,
                    "file": str(path),
                })

    # Also capture inline anonymous assert/cover property(...) blocks
    for i, ln in enumerate(lines):
        # anonymous: assert property (@(...) expr) — no named property ref
        if re.search(r"\b(?:assert|cover)\s+property\s*\(@", ln):
            kind = "assert" if "assert" in ln else "cover"
            sva_id = ""
            # look for comment on same line or above
            idm = _SVA_ID.search(ln)
            if idm:
                sva_id = idm.group(1)
            elif i > 0:
                idm = _SVA_ID.search(lines[i - 1])
                if idm:
                    sva_id = idm.group(1)
            spec_ref = ""
            if i > 0:
                sm = _SPEC_REF.search(lines[i - 1])
                if sm:
                    spec_ref = sm.group(1).strip()
            assertions.append({
                "kind": kind,
                "prop_name": sva_id.split(".")[-1] if sva_id else f"anon_ln{i+1}",
                "sva_id": sva_id,
                "spec": spec_ref,
                "ref": "",
                "line_no": i + 1,
                "file": str(path),
            })

    return {
        "file": str(path),
        "module": module_name,
        "bind_target": bind_target,
        "property_defs": len(properties),
        "assertions": assertions,
    }


# ---------------------------------------------------------------------------
# Component → SVA file mapping
# ---------------------------------------------------------------------------

def _component_from_path(p: Path) -> str:
    """Derive component name from SVA file path (parent directory name)."""
    return p.parent.name


# ---------------------------------------------------------------------------
# Manifest builder
# ---------------------------------------------------------------------------

def build_manifest(sva_dir: Path) -> dict:
    sv_files = sorted(sva_dir.rglob("*.sv"))
    by_component: dict[str, list[dict]] = defaultdict(list)

    for sv_path in sv_files:
        parsed = parse_sv_file(sv_path)
        comp = _component_from_path(sv_path)
        by_component[comp].append(parsed)

    components = []
    for comp, files in sorted(by_component.items()):
        all_assertions = []
        for f in files:
            all_assertions.extend(f["assertions"])

        asserts = [a for a in all_assertions if a["kind"] == "assert"]
        covers  = [a for a in all_assertions if a["kind"] == "cover"]
        assumes = [a for a in all_assertions if a["kind"] == "assume"]

        components.append({
            "component": comp,
            "files": [f["file"] for f in files],
            "bind_targets": [f["bind_target"] for f in files if f["bind_target"]],
            "totals": {
                "assert": len(asserts),
                "cover": len(covers),
                "assume": len(assumes),
                "total": len(all_assertions),
            },
            "assertions": all_assertions,
        })

    return {
        "sva_dir": str(sva_dir),
        "components": components,
        "summary": {
            "component_count": len(components),
            "total_assertions": sum(c["totals"]["assert"] for c in components),
            "total_covers": sum(c["totals"]["cover"] for c in components),
        },
    }


# ---------------------------------------------------------------------------
# Markdown report
# ---------------------------------------------------------------------------

def write_markdown(out: Path, manifest: dict) -> None:
    lines = [
        "# SVA Manifest",
        "",
        f"Generated from `{manifest['sva_dir']}`.",
        "",
        f"- Components: {manifest['summary']['component_count']}",
        f"- Assert properties: {manifest['summary']['total_assertions']}",
        f"- Cover properties: {manifest['summary']['total_covers']}",
        "",
    ]
    for comp in manifest["components"]:
        lines += [f"## {comp['component']}", ""]
        if comp["bind_targets"]:
            lines.append(f"**Bound to:** `{'`, `'.join(comp['bind_targets'])}`")
            lines.append("")
        lines += [
            f"| Kind | ID | Spec reference | File:line |",
            "|------|-----|----------------|-----------|",
        ]
        for a in comp["assertions"]:
            rel_file = Path(a["file"]).name
            sva_id = a.get("sva_id") or a["prop_name"]
            spec = (a.get("spec") or "")[:80]
            lines.append(f"| `{a['kind']}` | `{sva_id}` | {spec} | `{rel_file}:{a['line_no']}` |")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sva-dir", type=Path, default=DEFAULT_SVA_DIR)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    manifest = build_manifest(args.sva_dir)

    json_path = args.out / "sva_manifest.json"
    json_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    md_path = args.out / "sva_manifest.md"
    write_markdown(md_path, manifest)

    print(json.dumps({
        "status": "ok",
        "out_dir": str(args.out),
        "json": str(json_path),
        "markdown": str(md_path),
        "components": manifest["summary"]["component_count"],
        "assertions": manifest["summary"]["total_assertions"],
        "covers": manifest["summary"]["total_covers"],
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
