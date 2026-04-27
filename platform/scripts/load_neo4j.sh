#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/_common.sh"

assert_path "$OUT_ROOT/merged_ontology_seed.jsonl" "Merged ontology seed"
assert_path "$OUT_ROOT/merged_labels.jsonl"         "Merged labels"

run_python "$INGEST_ROOT/load_ontology_to_neo4j.py" \
    --seed     "$OUT_ROOT/merged_ontology_seed.jsonl" \
    --labels   "$OUT_ROOT/merged_labels.jsonl" \
    --uri      "$NEO4J_URI" \
    --user     "$NEO4J_USER" \
    --password "$NEO4J_PASSWORD"

ok "Neo4j 로드 완료 (OpenTitan + Ibex)"
