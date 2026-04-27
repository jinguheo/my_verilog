#!/usr/bin/env python3
"""
KG version snapshot manager.

Creates a versioned copy of kg_full/ under out/kg_versions/vXXX/ and
updates the version index.  Works file-only (no Docker required).

Usage:
  python build_kg_version.py \
    --kg-dir    out/kg_full \
    --ver-dir   out/kg_versions \
    --decisions out/label_approval/user_decisions_<ts>.jsonl \
    [--notes "Human reviewed 42 labels"]
"""
import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json(path, payload, indent=2):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=indent)


def next_version_tag(ver_dir: Path) -> str:
    index_path = ver_dir / "index.json"
    if not index_path.exists():
        return "v001"
    index = read_json(index_path)
    versions = index.get("versions", [])
    if not versions:
        return "v001"
    last_tag = versions[-1]["version_tag"]          # "v042"
    num = int(last_tag.lstrip("v")) + 1
    return f"v{num:03d}"


def load_index(ver_dir: Path) -> dict:
    index_path = ver_dir / "index.json"
    if index_path.exists():
        return read_json(index_path)
    return {"versions": [], "current": None}


def diff_summary(prev_summary: dict | None, cur_summary: dict) -> dict:
    if not prev_summary:
        return {"first_version": True}
    return {
        "modules_delta":  cur_summary.get("modules", 0)  - prev_summary.get("modules", 0),
        "labels_delta":   cur_summary.get("labels", 0)   - prev_summary.get("labels", 0),
        "edges_delta":    cur_summary.get("total_edges",0)- prev_summary.get("total_edges",0),
    }


def count_decisions(decisions_path: str | None) -> tuple[int, int]:
    if not decisions_path:
        return 0, 0
    p = Path(decisions_path)
    if not p.exists():
        return 0, 0
    approved = rejected = 0
    with open(p, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            d = row.get("decision", "")
            if d == "auto_approved":
                approved += 1
            elif d == "auto_rejected":
                rejected += 1
    return approved, rejected


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kg-dir",         required=True, help="out/kg_full")
    ap.add_argument("--ver-dir",        required=True, help="out/kg_versions")
    ap.add_argument("--decisions",      default=None,  help="user_decisions_*.jsonl")
    ap.add_argument("--approval-dir",   default=None,  help="out/label_approval (to snapshot approved labels)")
    ap.add_argument("--seed",           default=None,  help="merged_ontology_seed.jsonl path to snapshot")
    ap.add_argument("--notes",          default="",    help="free-text annotation")
    args = ap.parse_args()

    kg_dir  = Path(args.kg_dir)
    ver_dir = Path(args.ver_dir)
    ver_dir.mkdir(parents=True, exist_ok=True)

    nodes_path   = kg_dir / "kg_full_nodes_edges.json"
    summary_path = kg_dir / "kg_full_summary.json"
    if not nodes_path.exists() or not summary_path.exists():
        raise FileNotFoundError(f"KG files not found in {kg_dir}")

    cur_summary = read_json(summary_path)
    index       = load_index(ver_dir)

    # Previous version summary for diff
    prev_summary = None
    if index["versions"]:
        prev_tag = index["versions"][-1]["version_tag"]
        prev_sum_path = ver_dir / prev_tag / "kg_full_summary.json"
        if prev_sum_path.exists():
            prev_summary = read_json(prev_sum_path)

    version_tag = next_version_tag(ver_dir)
    snap_dir    = ver_dir / version_tag
    snap_dir.mkdir(parents=True, exist_ok=True)

    # Copy KG files into versioned snapshot
    shutil.copy2(nodes_path,   snap_dir / "kg_full_nodes_edges.json")
    shutil.copy2(summary_path, snap_dir / "kg_full_summary.json")

    # Copy approved labels (needed for version-specific eval)
    if args.approval_dir:
        ap_dir = Path(args.approval_dir)
        for fname in ("auto_approved_labels.jsonl", "review_queue.jsonl", "summary.json"):
            src = ap_dir / fname
            if src.exists():
                shutil.copy2(src, snap_dir / fname)

    # Copy seed snapshot (large; only if explicitly requested)
    if args.seed:
        seed_src = Path(args.seed)
        if seed_src.exists():
            shutil.copy2(seed_src, snap_dir / "merged_ontology_seed.jsonl")

    approved_added, rejected_added = count_decisions(args.decisions)
    diff = diff_summary(prev_summary, cur_summary)

    version_meta = {
        "version_tag":     version_tag,
        "created_at":      datetime.now(timezone.utc).isoformat(),
        "modules_total":   cur_summary.get("modules", 0),
        "labels_total":    cur_summary.get("labels", 0),
        "edges_total":     cur_summary.get("total_edges", 0),
        "approved_added":  approved_added,
        "rejected_added":  rejected_added,
        "decisions_file":  str(args.decisions) if args.decisions else None,
        "diff_from_prev":  diff,
        "notes":           args.notes,
    }
    write_json(snap_dir / "version_meta.json", version_meta)

    # Update index
    index["versions"].append({
        "version_tag":   version_tag,
        "created_at":    version_meta["created_at"],
        "modules_total": version_meta["modules_total"],
        "labels_total":  version_meta["labels_total"],
        "edges_total":   version_meta["edges_total"],
        "approved_added":approved_added,
        "notes":         args.notes,
    })
    index["current"] = version_tag
    write_json(ver_dir / "index.json", index)

    # current_version.txt for easy scripting
    (ver_dir / "current_version.txt").write_text(version_tag, encoding="utf-8")

    result = {"status": "ok", "version_tag": version_tag, "snapshot_dir": str(snap_dir), **version_meta}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
