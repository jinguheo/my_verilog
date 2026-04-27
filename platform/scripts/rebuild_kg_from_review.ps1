##############################################################################
# rebuild_kg_from_review.ps1
#
# 사용자가 Review Console에서 Export한 decisions 파일을 받아
# KG 전체를 재빌드하고 Review Console 데이터를 갱신합니다.
#
# 사용법:
#   .\rebuild_kg_from_review.ps1 -Decisions "C:\...\user_decisions_2026-04-27.jsonl"
#
# 수행 순서:
#   1. apply_user_decisions.py  → label_approval/ 갱신
#   2. build_full_kg_snapshot.py → kg_full/ 재빌드
#   3. build_full_review_data.py → review_full/ 갱신 (UI 데이터 갱신)
##############################################################################
param(
    [Parameter(Mandatory=$true)]
    [string]$Decisions
)

$ErrorActionPreference = "Stop"

$Root        = "D:\MyWork\verilog"
$PlatformDir = "$Root\platform"
$OutDir      = "$Root\out"
$EvalDir     = "$PlatformDir\eval"
$IngestDir   = "$PlatformDir\ingest"
$ScriptsDir  = "$PlatformDir\scripts"

function Step($n, $msg) {
    Write-Host ""
    Write-Host "[$n] $msg" -ForegroundColor Cyan
}

# ── 0. 입력 파일 확인 ───────────────────────────────────────────────────────
if (-not (Test-Path $Decisions)) {
    Write-Error "decisions 파일을 찾을 수 없습니다: $Decisions"
    exit 1
}
$DecisionsAbs = (Resolve-Path $Decisions).Path
Write-Host "Decisions file: $DecisionsAbs" -ForegroundColor Green

# ── 1. 사용자 결정 반영 ─────────────────────────────────────────────────────
Step 1 "apply_user_decisions.py — label_approval/ 갱신"
python "$IngestDir\apply_user_decisions.py" `
    --decisions "$DecisionsAbs" `
    --approval-dir "$OutDir\label_approval"
if ($LASTEXITCODE -ne 0) { throw "apply_user_decisions 실패" }

# ── 2. KG 재빌드 ────────────────────────────────────────────────────────────
Step 2 "build_full_kg_snapshot.py — KG 재빌드"
Push-Location $EvalDir
python "build_full_kg_snapshot.py" `
    --seed "$OutDir\merged_ontology_seed.jsonl" `
    --labels "$OutDir\merged_labels.jsonl" `
    --out-dir "$OutDir\kg_full" `
    --approved-labels "$OutDir\label_approval\auto_approved_labels.jsonl"
if ($LASTEXITCODE -ne 0) { Pop-Location; throw "build_full_kg_snapshot 실패" }
Pop-Location

# ── 3. Review Console 데이터 갱신 ───────────────────────────────────────────
Step 3 "build_full_review_data.py — review_full/ 갱신"
python "$ScriptsDir\build_full_review_data.py"
if ($LASTEXITCODE -ne 0) { throw "build_full_review_data 실패" }

# ── 완료 ────────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "완료!" -ForegroundColor Green
Write-Host "브라우저에서 Review Console을 새로고침하면 변경 사항이 반영됩니다." -ForegroundColor Yellow
Write-Host "  http://127.0.0.1:8000/platform/ui/review-console/index.html"
