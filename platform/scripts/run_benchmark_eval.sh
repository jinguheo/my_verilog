#!/usr/bin/env bash
##############################################################################
# run_benchmark_eval.sh
#
# 사용법:
#   ./run_benchmark_eval.sh               # 최신 KG로 평가
#   ./run_benchmark_eval.sh --version v002  # 특정 버전으로 평가
##############################################################################
source "$(dirname "${BASH_SOURCE[0]}")/_common.sh"

VERSION_TAG=""
while [[ $# -gt 0 ]]; do
    case "$1" in
        --version|-v) VERSION_TAG="$2"; shift 2 ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

# 버전 미지정 시 현재 버전 사용
if [[ -z "$VERSION_TAG" ]]; then
    VER_FILE="$OUT_ROOT/kg_versions/current_version.txt"
    if [[ -f "$VER_FILE" ]]; then
        VERSION_TAG="$(cat "$VER_FILE")"
        echo "버전 미지정 → 현재 버전 사용: $VERSION_TAG"
    fi
fi

SEED="$OUT_ROOT/merged_ontology_seed.jsonl"
LABELS="$OUT_ROOT/merged_labels.jsonl"
KG_OUT="$OUT_ROOT/kg_full"
BENCHMARK_OUT="$OUT_ROOT/eval_benchmark"
RESULTS_OUT="$OUT_ROOT/eval_results"
MULTIAXIS_OUT="$OUT_ROOT/multiaxis_benchmark"
MULTIAXIS_RESULTS_OUT="$OUT_ROOT/multiaxis_eval_results"
MANTICORE_OUT="$OUT_ROOT/manticore_analysis"
MANTICORE_REPO="$ROOT/tools/manticoresearch"
PDF_OUT="$OUT_ROOT/reports/kg_eval_report.pdf"
PDF_JSON_OUT="$OUT_ROOT/reports/kg_eval_report.json"

assert_path "$SEED"   "Merged ontology seed"
assert_path "$LABELS" "Merged labels"

VERSION_ARGS=()
if [[ -n "$VERSION_TAG" ]]; then
    VERSION_ARGS=(--version "$VERSION_TAG" --ver-dir "$OUT_ROOT/kg_versions")
fi

step "1/6" "KG 스냅샷 빌드"
pushd "$EVAL_ROOT" > /dev/null
run_python "build_full_kg_snapshot.py" \
    --seed    "$SEED" \
    --labels  "$LABELS" \
    --out-dir "$KG_OUT" \
    --approved-labels "$OUT_ROOT/label_approval/auto_approved_labels.jsonl"
popd > /dev/null

step "2/6" "QA 벤치마크 빌드"
pushd "$EVAL_ROOT" > /dev/null
run_python "build_qa_benchmark.py" \
    --seed "$SEED" --labels "$LABELS" \
    --out-dir "$BENCHMARK_OUT" --count-per-level 50

step "3/6" "Multi-axis 벤치마크 빌드"
run_python "build_multiaxis_benchmark.py" \
    --seed "$SEED" --labels "$LABELS" \
    --out-dir "$MULTIAXIS_OUT" --per-cell 5
popd > /dev/null

step "4/6" "Retrieval benchmark 실행"
pushd "$EVAL_ROOT" > /dev/null
run_python "run_retrieval_benchmark.py" \
    --seed      "$SEED" \
    --benchmark "$BENCHMARK_OUT/benchmark_all.jsonl" \
    --out-dir   "$RESULTS_OUT" \
    "${VERSION_ARGS[@]}"

step "5/6" "Multi-axis benchmark 실행"
run_python "run_multiaxis_retrieval_benchmark.py" \
    --seed      "$SEED" \
    --questions "$MULTIAXIS_OUT/questions_all.jsonl" \
    --out-dir   "$MULTIAXIS_RESULTS_OUT" \
    "${VERSION_ARGS[@]}"

step "6/7" "Manticore Search retrieval benchmark 실행"
MANTICORE_ARGS=(
    --seed      "$SEED"
    --questions "$MULTIAXIS_OUT/questions_all.jsonl"
    --out-dir   "$MANTICORE_OUT"
)
if [[ -d "$MANTICORE_REPO" ]]; then
    MANTICORE_ARGS+=(--manticore-repo "$MANTICORE_REPO")
fi
run_python "run_manticore_retrieval_analysis.py" "${MANTICORE_ARGS[@]}"

step "7/7" "PDF 리포트 생성"
run_python "render_eval_pdf.py" \
    --kg-summary       "$KG_OUT/kg_full_summary.json" \
    --benchmark-summary "$BENCHMARK_OUT/benchmark_summary.json" \
    --retrieval-report "$RESULTS_OUT${VERSION_TAG:+/$VERSION_TAG}/retrieval_report.json" \
    --multiaxis-summary "$MULTIAXIS_OUT/summary.json" \
    --multiaxis-report "$MULTIAXIS_RESULTS_OUT${VERSION_TAG:+/$VERSION_TAG}/multiaxis_report.json" \
    --manticore-report "$MANTICORE_OUT/manticore_retrieval_report.json" \
    --manticore-metadata "$MANTICORE_OUT/manticore_retrieval_metadata.json" \
    --out-pdf  "$PDF_OUT" \
    --out-json "$PDF_JSON_OUT"
popd > /dev/null

echo ""
ok "평가 완료${VERSION_TAG:+ (버전: $VERSION_TAG)}"
echo "  KG:        $KG_OUT"
echo "  Results:   $RESULTS_OUT${VERSION_TAG:+/$VERSION_TAG}"
echo "  MultiAxis: $MULTIAXIS_RESULTS_OUT${VERSION_TAG:+/$VERSION_TAG}"
echo "  Manticore: $MANTICORE_OUT"
echo "  PDF:       $PDF_OUT"
