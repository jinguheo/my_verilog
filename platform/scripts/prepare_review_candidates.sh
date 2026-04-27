#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/_common.sh"

assert_path "$OUT_ROOT/merged_ontology_seed.jsonl" "Merged ontology seed"
assert_path "$OUT_ROOT/merged_labels.jsonl"         "Merged labels"

LABEL_APPROVAL_OUT="$OUT_ROOT/label_approval"

run_python "$INGEST_ROOT/auto_approve_labels.py" \
    --seed    "$OUT_ROOT/merged_ontology_seed.jsonl" \
    --labels  "$OUT_ROOT/merged_labels.jsonl" \
    --out-dir "$LABEL_APPROVAL_OUT"

ok "자동 승인 완료"
echo "  Review queue: $LABEL_APPROVAL_OUT/review_queue.jsonl"
