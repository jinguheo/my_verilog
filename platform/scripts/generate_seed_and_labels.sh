#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/_common.sh"
ensure_out_root

assert_path "$DB_ROOT/opentitan" "OpenTitan RTL DB"
assert_path "$DB_ROOT/ibex"      "Ibex RTL DB"

OPENTITAN_SEED="$OUT_ROOT/opentitan_ontology_seed.jsonl"
IBEX_SEED="$OUT_ROOT/ibex_ontology_seed.jsonl"
OPENTITAN_LABELS="$OUT_ROOT/opentitan_labels.jsonl"
IBEX_LABELS="$OUT_ROOT/ibex_labels.jsonl"
MERGED_SEED="$OUT_ROOT/merged_ontology_seed.jsonl"
MERGED_LABELS="$OUT_ROOT/merged_labels.jsonl"
EMBEDDING_ROWS="$OUT_ROOT/embedding_rows.json"

step "1/7" "OpenTitan 온톨로지 시드 생성"
run_python "$INGEST_ROOT/generate_ontology_seed.py" --root "$DB_ROOT/opentitan" --out "$OPENTITAN_SEED"

step "2/7" "Ibex 온톨로지 시드 생성"
run_python "$INGEST_ROOT/generate_ontology_seed.py" --root "$DB_ROOT/ibex" --out "$IBEX_SEED"

step "3/7" "OpenTitan 레이블 추출"
run_python "$INGEST_ROOT/extract_opentitan_labels.py" --root "$DB_ROOT/opentitan" --out "$OPENTITAN_LABELS"

step "4/7" "Ibex 레이블 추출"
run_python "$INGEST_ROOT/extract_ibex_labels.py" --root "$DB_ROOT/ibex" --out "$IBEX_LABELS"

step "5/7" "시드 병합"
run_python "$INGEST_ROOT/merge_jsonl.py" --inputs "$OPENTITAN_SEED" "$IBEX_SEED" --out "$MERGED_SEED"

step "6/7" "레이블 병합"
run_python "$INGEST_ROOT/merge_jsonl.py" --inputs "$OPENTITAN_LABELS" "$IBEX_LABELS" --out "$MERGED_LABELS"

step "7/7" "임베딩 행 준비"
run_python "$INGEST_ROOT/prepare_embedding_rows.py" --seed "$MERGED_SEED" --outfile "$EMBEDDING_ROWS"

ok "OpenTitan + Ibex 시드, 레이블, 병합 파일, 임베딩 행 생성 완료"
