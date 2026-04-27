#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/_common.sh"

mkdir -p \
    "$OUT_ROOT/label_approval" \
    "$OUT_ROOT/kg_full" \
    "$OUT_ROOT/kg_versions" \
    "$OUT_ROOT/review_full" \
    "$OUT_ROOT/eval_benchmark" \
    "$OUT_ROOT/eval_results" \
    "$OUT_ROOT/multiaxis_benchmark" \
    "$OUT_ROOT/multiaxis_eval_results" \
    "$OUT_ROOT/reports" \
    "$RUNTIME_ROOT/volumes/postgres" \
    "$RUNTIME_ROOT/volumes/neo4j/data" \
    "$RUNTIME_ROOT/volumes/neo4j/logs"

ok "폴더 초기화 완료"
