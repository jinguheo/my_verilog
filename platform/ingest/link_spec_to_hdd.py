#!/usr/bin/env python3
"""
Link spec-only graphify nodes to HDD module documents.

Uses the spec-code graphify graph (spec_component_matches_code,
spec_path_matches_code_path) to find which spec documents / components
describe each HDD module.

Matching paths:
  Path A — component match:
    spec_component node  ─spec_component_matches_code──► code_symbol node
    code_symbol.label == hdd_module.name   → link spec_component to HDD

  Path B — path match:
    spec_doc node  ─spec_path_matches_code_path──► code_file/symbol node
    code node source_file suffix matches hdd_module source_file → link

Adds to each HDD JSON:
  "spec_references": [
    { "spec_id", "spec_label", "spec_file", "spec_role",
      "relation", "component", "confidence" }
  ]

Writes:
  - Updated out/hdd/<module>.json  (spec_references added)
  - Updated out/hdd/<module>.md   (Specification References section)
  - out/hdd/spec_link_report.json  (coverage stats)

Usage:
  python link_spec_to_hdd.py \
    --spec-code-graph  dbs/graphify-out/spec-code-graphify/graph.json \
    --hdd-dir          out/hdd
"""
from __future__ import annotations
import argparse
import json
import os
from collections import defaultdict, Counter
from datetime import datetime, timezone
from pathlib import Path


def normalize(p: str) -> str:
    return p.replace("\\", "/").lower()


def load_graph(path: Path):
    with open(path, encoding="utf-8") as f:
        g = json.load(f)
    nbi = {n["id"]: n for n in g["nodes"]}
    return nbi, g["links"]


def build_spec_index(nbi: dict, links: list) -> dict:
    """
    Returns two indexes:
      by_code_label[label_lower]   = list of (spec_node, relation, component)
      by_code_file[file_suffix]    = list of (spec_node, relation, component)
    """
    by_label: dict[str, list] = defaultdict(list)
    by_file:  dict[str, list] = defaultdict(list)

    for l in links:
        rel = l.get("relation", "")
        if rel not in ("spec_component_matches_code", "spec_path_matches_code_path"):
            continue

        src_n = nbi.get(l.get("source", ""), {})
        tgt_n = nbi.get(l.get("target", ""), {})
        if not src_n or not tgt_n:
            continue

        # Source must be a spec node, target a code node
        if src_n.get("file_type") != "document":
            src_n, tgt_n = tgt_n, src_n
        if src_n.get("file_type") != "document":
            continue

        spec_entry = {
            "spec_id":    src_n["id"],
            "spec_label": src_n.get("label", ""),
            "spec_file":  src_n.get("source_file", ""),
            "spec_role":  src_n.get("role", ""),
            "relation":   rel,
            "component":  src_n.get("label","").replace("component:","") if src_n.get("role") == "component" else None,
            "confidence": l.get("confidence_score", l.get("confidence", 1.0)),
        }

        # Index by code target label
        lbl = tgt_n.get("label", "").lower()
        if lbl:
            by_label[lbl].append(spec_entry)

        # Index by code target file suffix
        sf = normalize(tgt_n.get("source_file", ""))
        if sf:
            # strip project-level prefix for matching
            for sep in ("/dbs/", "dbs/"):
                if sep in sf:
                    sf = sf.split(sep, 1)[1]
                    break
            by_file[sf].append(spec_entry)

    return by_label, by_file


def find_spec_refs(module_name: str, hdd_src: str,
                   by_label: dict, by_file: dict) -> list[dict]:
    seen: set[str] = set()
    results: list[dict] = []

    def add(entry: dict):
        key = entry["spec_id"] + "|" + entry["relation"]
        if key not in seen:
            seen.add(key)
            results.append(entry)

    # Path A: label match
    for e in by_label.get(module_name.lower(), []):
        add(e)

    # Path B: file match (normalize HDD source path)
    norm_src = normalize(hdd_src)
    for sep in ("/dbs/", "dbs/"):
        if sep in norm_src:
            norm_src = norm_src.split(sep, 1)[1]
            break
    if norm_src.startswith("ibex/"):
        norm_src = norm_src  # already relative

    for e in by_file.get(norm_src, []):
        add(e)

    # Sort: component matches first, then by spec_label
    results.sort(key=lambda x: (x["relation"] != "spec_component_matches_code", x["spec_label"]))
    return results


def render_spec_section(refs: list[dict]) -> list[str]:
    if not refs:
        return []
    lines = ["## Specification References", ""]
    comp_refs = [r for r in refs if r["relation"] == "spec_component_matches_code"]
    path_refs = [r for r in refs if r["relation"] == "spec_path_matches_code_path"]

    if comp_refs:
        lines.append("### Component Matches")
        lines.append("")
        for r in comp_refs:
            lines.append(f"- **{r['spec_label']}** (`{r['spec_file']}`)")
        lines.append("")

    if path_refs:
        lines.append("### Referenced Spec Documents")
        lines.append("")
        # deduplicate by spec_label
        seen_labels: set[str] = set()
        for r in path_refs:
            if r["spec_label"] not in seen_labels:
                seen_labels.add(r["spec_label"])
                lines.append(f"- `{r['spec_label']}` — {r['spec_file']}")
        lines.append("")

    return lines


def update_md(md_path: Path, spec_lines: list[str]) -> None:
    if not md_path.exists():
        return
    text = md_path.read_text(encoding="utf-8")

    # Remove existing spec references section if present
    marker = "## Specification References"
    if marker in text:
        idx = text.index(marker)
        # find next ## after it
        next_h = text.find("\n## ", idx + len(marker))
        if next_h >= 0:
            text = text[:idx] + text[next_h + 1:]
        else:
            text = text[:idx]

    # Insert before Verification section (or at end)
    ver_marker = "## Verification Status"
    if ver_marker in text:
        idx = text.index(ver_marker)
        text = text[:idx] + "\n".join(spec_lines) + "\n" + text[idx:]
    else:
        text = text.rstrip() + "\n\n" + "\n".join(spec_lines)

    md_path.write_text(text, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec-code-graph", required=True)
    ap.add_argument("--hdd-dir",         required=True)
    args = ap.parse_args()

    print(f"Loading spec-code graph …")
    nbi, links = load_graph(Path(args.spec_code_graph))
    by_label, by_file = build_spec_index(nbi, links)
    print(f"  by_label index: {len(by_label)} keys")
    print(f"  by_file  index: {len(by_file)} keys")

    hdd_dir = Path(args.hdd_dir)
    doc_files = sorted(hdd_dir.rglob("*.json"))
    doc_files = [p for p in doc_files
                 if p.name not in ("index.json", "spec_link_report.json", "verification_report.json")]
    print(f"HDD docs: {len(doc_files)}")

    now_str = datetime.now(timezone.utc).isoformat()
    report_rows: list[dict] = []
    linked = unlinked = 0

    for doc_path in doc_files:
        with open(doc_path, encoding="utf-8") as f:
            doc = json.load(f)

        module_name = doc["module"]
        hdd_src     = doc.get("source_file", "")

        refs = find_spec_refs(module_name, hdd_src, by_label, by_file)
        doc["spec_references"] = refs
        doc["spec_linked_at"] = now_str

        with open(doc_path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)

        md_path = doc_path.with_suffix(".md")
        spec_lines = render_spec_section(refs)
        update_md(md_path, spec_lines)

        n_comp = sum(1 for r in refs if r["relation"] == "spec_component_matches_code")
        n_path = sum(1 for r in refs if r["relation"] == "spec_path_matches_code_path")

        if refs:
            linked += 1
        else:
            unlinked += 1

        report_rows.append({
            "module":            module_name,
            "spec_refs":         len(refs),
            "component_matches": n_comp,
            "path_matches":      n_path,
            "linked":            len(refs) > 0,
        })

    # Coverage report
    report = {
        "generated_at":  now_str,
        "total_modules": len(doc_files),
        "linked":        linked,
        "unlinked":      unlinked,
        "coverage":      round(linked / len(doc_files), 4) if doc_files else 0.0,
        "total_refs":    sum(r["spec_refs"] for r in report_rows),
        "modules":       sorted(report_rows, key=lambda x: -x["spec_refs"]),
    }
    report_path = hdd_dir / "spec_link_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(json.dumps({
        "status":        "ok",
        "linked":        linked,
        "unlinked":      unlinked,
        "coverage":      f"{report['coverage']*100:.1f}%",
        "total_refs":    report["total_refs"],
        "report":        str(report_path),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
