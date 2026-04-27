#!/usr/bin/env python3
"""
Apply user review decisions exported from the Review Console.
Supports multiple reviewer files with conflict resolution.

Usage (single reviewer):
  python apply_user_decisions.py \
    --decisions user_decisions_alice.jsonl \
    --approval-dir out/label_approval

Usage (multiple reviewers):
  python apply_user_decisions.py \
    --decisions user_decisions_alice.jsonl user_decisions_bob.jsonl user_decisions_carol.jsonl \
    --approval-dir out/label_approval

Merge rules (per item):
  - 1 reviewer only          → force auto_approved  (single voice = benefit of the doubt)
  - N reviewers, all same    → use that decision    (consensus)
  - N reviewers, conflicting → review_again         (disputed, stays in queue)
"""
import argparse
import json
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone


def read_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def entry_key(row):
    return (
        row.get("project", ""),
        row.get("target_name") or row.get("module", ""),
        row.get("label", ""),
        row.get("path", ""),
    )


def merge_reviewer_decisions(rows_by_reviewer: list[dict]) -> dict:
    """
    rows_by_reviewer: list of decision rows, one per reviewer for the same item.

    Returns a single merged row with:
      - decision / review_state updated per merge rules
      - merge_info added for traceability
    """
    base = rows_by_reviewer[0].copy()
    n = len(rows_by_reviewer)
    reviewer_decisions = [r.get("decision", "") for r in rows_by_reviewer]
    reviewer_files     = [r.get("_source_file", "?") for r in rows_by_reviewer]

    if n == 1:
        # Single reviewer → auto-approve regardless of their decision
        base["decision"]     = "auto_approved"
        base["review_state"] = "approved"
        base["merge_info"] = {
            "rule":      "single_reviewer_auto_approve",
            "reviewers": reviewer_files,
            "original":  reviewer_decisions[0],
        }
        return base

    unique_decisions = set(reviewer_decisions)
    if len(unique_decisions) == 1:
        # All reviewers agree → use consensus decision
        base["decision"]    = reviewer_decisions[0]
        base["review_state"] = (
            "approved"  if base["decision"] == "auto_approved"  else
            "rejected"  if base["decision"] == "auto_rejected"  else
            "needs_review"
        )
        base["merge_info"] = {
            "rule":      f"consensus_{n}_reviewers",
            "reviewers": reviewer_files,
            "decision":  reviewer_decisions[0],
        }
        return base

    # Conflicting decisions → review_again
    base["decision"]     = "needs_review"
    base["review_state"] = "review_again"
    base["merge_info"] = {
        "rule":      "conflict",
        "reviewers": reviewer_files,
        "votes":     dict(zip(reviewer_files, reviewer_decisions)),
    }
    return base


def load_all_decisions(decision_files: list[str]) -> dict:
    """
    Load all reviewer files. Returns {entry_key: [row, ...]} grouped by item.
    Each row gets a _source_file tag.
    """
    by_item = defaultdict(list)
    for path in decision_files:
        rows = read_jsonl(path)
        for row in rows:
            row["_source_file"] = Path(path).name
            k = entry_key(row)
            by_item[k].append(row)
    return by_item


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--decisions",
        nargs="+",
        required=True,
        help="One or more exported user_decisions_*.jsonl files (space-separated)",
    )
    ap.add_argument("--approval-dir", required=True, help="out/label_approval directory")
    args = ap.parse_args()

    approval_dir = Path(args.approval_dir)
    now = datetime.now(timezone.utc).isoformat()

    # ── Load and merge all reviewer files ────────────────────────────────────
    print(f"Loading {len(args.decisions)} decisions file(s):")
    for f in args.decisions:
        rows = read_jsonl(f)
        print(f"  {Path(f).name}: {len(rows)} rows")

    by_item = load_all_decisions(args.decisions)
    print(f"Unique items across all files: {len(by_item)}")

    # ── Apply merge rules ─────────────────────────────────────────────────────
    merged_approved   = {}   # key → merged row
    merged_rejected   = {}
    merged_conflicts  = {}   # review_again

    for k, reviewer_rows in by_item.items():
        merged = merge_reviewer_decisions(reviewer_rows)
        merged["merged_at"] = now
        d = merged.get("decision", "")
        if d == "auto_approved":
            merged_approved[k] = merged
        elif d == "auto_rejected":
            merged_rejected[k] = merged
        else:
            merged_conflicts[k] = merged

    total = len(by_item)
    print(
        f"\nMerge results:"
        f"\n  auto_approved : {len(merged_approved)}"
        f"\n  auto_rejected : {len(merged_rejected)}"
        f"\n  review_again  : {len(merged_conflicts)}"
    )

    if merged_conflicts:
        print("\nConflicted items (need another round of review):")
        for k, row in list(merged_conflicts.items())[:20]:
            votes = row.get("merge_info", {}).get("votes", {})
            print(f"  [{k[1]} / {k[2]}]  votes={votes}")
        if len(merged_conflicts) > 20:
            print(f"  ... and {len(merged_conflicts) - 20} more")

    # ── Load existing approval files ──────────────────────────────────────────
    approved_path = approval_dir / "auto_approved_labels.jsonl"
    rejected_path = approval_dir / "auto_rejected_labels.jsonl"
    queue_path    = approval_dir / "review_queue.jsonl"

    existing_approved = read_jsonl(approved_path) if approved_path.exists() else []
    existing_rejected = read_jsonl(rejected_path) if rejected_path.exists() else []
    existing_queue    = read_jsonl(queue_path)    if queue_path.exists()    else []

    already_approved = {entry_key(r) for r in existing_approved}
    already_rejected = {entry_key(r) for r in existing_rejected}

    # ── Apply to existing files ───────────────────────────────────────────────
    new_approved = [
        row for k, row in merged_approved.items() if k not in already_approved
    ]
    new_rejected = [
        row for k, row in merged_rejected.items() if k not in already_rejected
    ]

    decided_keys = set(merged_approved) | set(merged_rejected)

    # Conflicts: update review_state in queue to "review_again"
    conflict_keys = set(merged_conflicts)
    updated_queue = []
    for r in existing_queue:
        k = entry_key(r)
        if k in decided_keys:
            continue  # resolved
        if k in conflict_keys:
            r = r.copy()
            r["review_state"] = "review_again"
            r["merge_info"] = merged_conflicts[k].get("merge_info", {})
        updated_queue.append(r)

    # Append conflict items not already in queue
    existing_queue_keys = {entry_key(r) for r in existing_queue}
    for k, row in merged_conflicts.items():
        if k not in existing_queue_keys:
            updated_queue.append(row)

    updated_approved = existing_approved + new_approved
    updated_rejected = existing_rejected + new_rejected

    # ── Write back ────────────────────────────────────────────────────────────
    write_jsonl(approved_path, updated_approved)
    write_jsonl(rejected_path, updated_rejected)
    write_jsonl(queue_path,    updated_queue)

    all_decisions = updated_approved + updated_rejected + updated_queue
    write_jsonl(approval_dir / "all_label_decisions.jsonl", all_decisions)

    by_decision = Counter(r.get("decision", "unknown") for r in all_decisions)
    summary = {
        "total_entries":   len(all_decisions),
        "by_decision":     dict(by_decision),
        "applied_from":    args.decisions,
        "reviewer_count":  len(args.decisions),
        "new_approved":    len(new_approved),
        "new_rejected":    len(new_rejected),
        "conflicts":       len(merged_conflicts),
        "queue_remaining": len(updated_queue),
    }
    with open(approval_dir / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(json.dumps({"status": "ok", **summary}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
