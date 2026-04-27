#!/usr/bin/env bash
##############################################################################
# apply_review_and_update_kg.sh
#
# 여러 작업자가 Export한 decisions 파일을 합산하여 전체 파이프라인 실행.
#
# 병합 규칙:
#   - 1명만 결정  → 무조건 auto_approved
#   - N명 동일    → 해당 결정 사용 (consensus)
#   - N명 충돌    → review_again (큐에 잔류)
#
# 사용법 (단일):
#   ./apply_review_and_update_kg.sh -d /path/to/alice.jsonl
#
# 사용법 (복수):
#   ./apply_review_and_update_kg.sh \
#       -d /path/to/alice.jsonl \
#       -d /path/to/bob.jsonl \
#       -d /path/to/carol.jsonl \
#       -n "4월 합산 리뷰"
##############################################################################
source "$(dirname "${BASH_SOURCE[0]}")/_common.sh"

DECISIONS=()    # 배열 — 여러 파일 허용
NOTES=""
SKIP_DB=false

usage() {
    echo "Usage: $0 -d <file1.jsonl> [-d <file2.jsonl> ...] [-n <notes>] [--skip-db]"
    exit 1
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -d|--decisions) DECISIONS+=("$2"); shift 2 ;;
        -n|--notes)     NOTES="$2";        shift 2 ;;
        --skip-db)      SKIP_DB=true;      shift   ;;
        -h|--help)      usage ;;
        *) echo "Unknown option: $1"; usage ;;
    esac
done

[[ ${#DECISIONS[@]} -eq 0 ]] && usage

# Resolve to absolute paths and validate
DECISIONS_ABS=()
for d in "${DECISIONS[@]}"; do
    [[ -f "$d" ]] || err "decisions 파일을 찾을 수 없습니다: $d"
    DECISIONS_ABS+=("$(cd "$(dirname "$d")" && pwd)/$(basename "$d")")
done

echo ""
echo "=== RTL Ontology KG Update Pipeline ==="
echo "Decisions (${#DECISIONS_ABS[@]}개):"
for d in "${DECISIONS_ABS[@]}"; do echo "  - $d"; done
echo "Notes   : ${NOTES:-(없음)}"
echo "Skip DB : $SKIP_DB"

# ── 1. label_approval/ 갱신 ─────────────────────────────────────────────────
step "1/6" "label_approval/ 갱신 (다중 리뷰어 병합)"
run_python "$INGEST_ROOT/apply_user_decisions.py" \
    --decisions "${DECISIONS_ABS[@]}" \
    --approval-dir "$OUT_ROOT/label_approval"
ok "label_approval/ 갱신 완료"

# ── 2. KG JSON 재빌드 ───────────────────────────────────────────────────────
step "2/6" "KG JSON 재빌드"
pushd "$EVAL_ROOT" > /dev/null
run_python "build_full_kg_snapshot.py" \
    --seed    "$OUT_ROOT/merged_ontology_seed.jsonl" \
    --labels  "$OUT_ROOT/merged_labels.jsonl" \
    --out-dir "$OUT_ROOT/kg_full" \
    --approved-labels "$OUT_ROOT/label_approval/auto_approved_labels.jsonl"
popd > /dev/null
ok "kg_full/ 재빌드 완료"

# ── 3. KG 버전 스냅샷 생성 ──────────────────────────────────────────────────
step "3/6" "KG 버전 스냅샷 생성"
# notes에 파일 목록 포함
FILES_LIST="$(IFS=', '; echo "${DECISIONS_ABS[*]}")"
NOTES_WITH_FILES="${NOTES:+$NOTES }[files: $FILES_LIST]"
run_python "$INGEST_ROOT/build_kg_version.py" \
    --kg-dir       "$OUT_ROOT/kg_full" \
    --ver-dir      "$OUT_ROOT/kg_versions" \
    --approval-dir "$OUT_ROOT/label_approval" \
    --decisions    "${DECISIONS_ABS[0]}" \
    --notes        "$NOTES_WITH_FILES"

VERSION_TAG="$(cat "$OUT_ROOT/kg_versions/current_version.txt")"
ok "버전 스냅샷 생성: $VERSION_TAG  →  $OUT_ROOT/kg_versions/$VERSION_TAG/"

# ── 4. PostgreSQL 업데이트 ──────────────────────────────────────────────────
step "4/6" "PostgreSQL 업데이트"
if $SKIP_DB; then
    skip "--skip-db 옵션 지정됨"
elif ! docker_container_running "verilog-postgres"; then
    warn "verilog-postgres 미실행 → 건너뜁니다."
    warn "실행하려면: cd $RUNTIME_ROOT && docker compose up -d postgres"
else
    docker exec -i verilog-postgres psql -U postgres -d verilog \
        < "$SCHEMA_ROOT/kg_version_schema.sql" 2>/dev/null || true
    PG_OK=true
    for d in "${DECISIONS_ABS[@]}"; do
        "$PYTHON" "$INGEST_ROOT/apply_labels_to_postgres.py" \
            --decisions "$d" --version-tag "$VERSION_TAG" --db-url "$POSTGRES_URL" \
            || PG_OK=false
    done
    $PG_OK && ok "PostgreSQL 업데이트 완료" || warn "PostgreSQL 업데이트 일부 실패 (계속 진행)"
fi

# ── 5. Neo4j 업데이트 ───────────────────────────────────────────────────────
step "5/6" "Neo4j 업데이트"
if $SKIP_DB; then
    skip "--skip-db 옵션 지정됨"
elif ! docker_container_running "verilog-neo4j"; then
    warn "verilog-neo4j 미실행 → 건너뜁니다."
    warn "실행하려면: cd $RUNTIME_ROOT && docker compose up -d neo4j"
else
    NEO4J_OK=true
    for d in "${DECISIONS_ABS[@]}"; do
        "$PYTHON" "$INGEST_ROOT/apply_labels_to_neo4j.py" \
            --decisions "$d" --version-tag "$VERSION_TAG" \
            --uri "$NEO4J_URI" --user "$NEO4J_USER" --password "$NEO4J_PASSWORD" \
            || NEO4J_OK=false
    done
    $NEO4J_OK && ok "Neo4j 업데이트 완료" || warn "Neo4j 업데이트 일부 실패 (계속 진행)"
fi

# ── 6. Review Console 데이터 갱신 ───────────────────────────────────────────
step "6/6" "Review Console 데이터 갱신"
run_python "$PLATFORM_DIR/scripts/build_full_review_data.py"
ok "review_full/ 갱신 완료"

# ── 버전 히스토리 출력 ───────────────────────────────────────────────────────
INDEX="$OUT_ROOT/kg_versions/index.json"
if [[ -f "$INDEX" ]]; then
    echo ""
    printf "  %-8s  %-25s  %6s  %7s  %6s  %s\n" \
        "버전" "생성일" "모듈" "레이블" "엣지" "승인추가"
    printf "  %-8s  %-25s  %6s  %7s  %6s  %s\n" \
        "-------" "------------------------" "------" "-------" "------" "--------"
    "$PYTHON" - "$INDEX" "$VERSION_TAG" <<'PYEOF'
import json, sys
index = json.load(open(sys.argv[1]))
cur = sys.argv[2]
for v in index["versions"]:
    tag    = v["version_tag"]
    ts     = v["created_at"].replace("T"," ").split(".")[0]
    marker = " ◄ current" if tag == cur else ""
    print(f"  {tag:<8}  {ts:<25}  {v.get('modules_total',0):>6}  "
          f"{v.get('labels_total',0):>7}  {v.get('edges_total',0):>6}  "
          f"{v.get('approved_added',0):>8}{marker}")
PYEOF
fi

# ── 완료 ────────────────────────────────────────────────────────────────────
echo ""
echo -e "\033[32m========================================\033[0m"
echo -e "\033[32m KG 업데이트 완료: $VERSION_TAG\033[0m"
echo -e "\033[32m========================================\033[0m"
echo ""
echo "버전 지정 평가:"
echo "  cd $EVAL_ROOT"
echo "  $PYTHON run_retrieval_benchmark.py \\"
echo "    --seed $OUT_ROOT/merged_ontology_seed.jsonl \\"
echo "    --benchmark $OUT_ROOT/eval_benchmark/benchmark_all.jsonl \\"
echo "    --out-dir $OUT_ROOT/eval_results \\"
echo "    --ver-dir $OUT_ROOT/kg_versions \\"
echo "    --version $VERSION_TAG"
