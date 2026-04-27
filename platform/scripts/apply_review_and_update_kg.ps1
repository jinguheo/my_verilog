##############################################################################
# apply_review_and_update_kg.ps1
#
# 여러 작업자가 Export한 decisions 파일을 합산하여 전체 파이프라인 실행.
#
# 병합 규칙:
#   - 1명만 결정  → 무조건 auto_approved
#   - N명 동일    → 해당 결정 사용 (consensus)
#   - N명 충돌    → review_again (큐에 잔류)
#
# 사용법 (단일):
#   .\apply_review_and_update_kg.ps1 -Decisions "C:\...\alice.jsonl"
#
# 사용법 (복수):
#   .\apply_review_and_update_kg.ps1 `
#       -Decisions "C:\...\alice.jsonl","C:\...\bob.jsonl","C:\...\carol.jsonl" `
#       -Notes "4월 합산 리뷰"
##############################################################################
param(
    [Parameter(Mandatory=$true)]
    [string[]]$Decisions,       # 배열 — 여러 파일 허용

    [string]$Notes = "",

    [switch]$SkipDB
)

$ErrorActionPreference = "Stop"

$Root        = "D:\MyWork\verilog"
$PlatformDir = "$Root\platform"
$OutDir      = "$Root\out"
$EvalDir     = "$PlatformDir\eval"
$IngestDir   = "$PlatformDir\ingest"
$ScriptsDir  = "$PlatformDir\scripts"

$POSTGRES_URL = "postgresql://postgres:postgres@localhost:5432/verilog"
$NEO4J_URI    = "neo4j://localhost:7687"
$NEO4J_USER   = "neo4j"
$NEO4J_PASS   = "neo4jpassword"

function Step($n, $msg) {
    Write-Host ""
    Write-Host "[$n/6] $msg" -ForegroundColor Cyan
}
function OK($msg)   { Write-Host "      OK: $msg"   -ForegroundColor Green  }
function SKIP($msg) { Write-Host "      SKIP: $msg" -ForegroundColor Yellow }
function WARN($msg) { Write-Host "      WARN: $msg" -ForegroundColor Yellow }

function Test-DockerContainer($name) {
    $running = docker ps --filter "name=$name" --filter "status=running" -q 2>$null
    return ($null -ne $running -and $running -ne "")
}

# ── 0. 입력 확인 ────────────────────────────────────────────────────────────
$DecisionsAbs = @()
foreach ($d in $Decisions) {
    if (-not (Test-Path $d)) {
        Write-Error "decisions 파일을 찾을 수 없습니다: $d"
        exit 1
    }
    $DecisionsAbs += (Resolve-Path $d).Path
}

Write-Host ""
Write-Host "=== RTL Ontology KG Update Pipeline ===" -ForegroundColor White
Write-Host "Decisions ($($DecisionsAbs.Count)개):"
foreach ($d in $DecisionsAbs) { Write-Host "  - $d" }
Write-Host "Notes   : $(if ($Notes) { $Notes } else { '(없음)' })"
Write-Host "Skip DB : $SkipDB"

# ── 1. label_approval/ 갱신 ─────────────────────────────────────────────────
Step 1 "label_approval/ 갱신 (apply_user_decisions.py)"
$decArgs = $DecisionsAbs | ForEach-Object { $_ }
python "$IngestDir\apply_user_decisions.py" `
    --decisions @decArgs `
    --approval-dir "$OutDir\label_approval"
if ($LASTEXITCODE -ne 0) { throw "apply_user_decisions 실패" }
OK "label_approval/ 갱신 완료"

# ── 2. KG JSON 재빌드 ───────────────────────────────────────────────────────
Step 2 "KG JSON 재빌드 (build_full_kg_snapshot.py)"
Push-Location $EvalDir
python "build_full_kg_snapshot.py" `
    --seed    "$OutDir\merged_ontology_seed.jsonl" `
    --labels  "$OutDir\merged_labels.jsonl" `
    --out-dir "$OutDir\kg_full" `
    --approved-labels "$OutDir\label_approval\auto_approved_labels.jsonl"
if ($LASTEXITCODE -ne 0) { Pop-Location; throw "build_full_kg_snapshot 실패" }
Pop-Location
OK "kg_full/ 재빌드 완료"

# ── 3. KG 버전 스냅샷 생성 ──────────────────────────────────────────────────
Step 3 "KG 버전 스냅샷 생성 (build_kg_version.py)"
# decisions 인자: 첫 번째 파일만 메타데이터로 기록 (여러 개는 notes에 명시)
$notesWithFiles = "$Notes [files: $($DecisionsAbs -join ', ')]".Trim(" []")
python "$IngestDir\build_kg_version.py" `
    --kg-dir       "$OutDir\kg_full" `
    --ver-dir      "$OutDir\kg_versions" `
    --approval-dir "$OutDir\label_approval" `
    --decisions    $DecisionsAbs[0] `
    --notes        $notesWithFiles
if ($LASTEXITCODE -ne 0) { throw "build_kg_version 실패" }

$VersionTag = (Get-Content "$OutDir\kg_versions\current_version.txt" -Raw).Trim()
OK "버전 스냅샷 생성: $VersionTag  →  $OutDir\kg_versions\$VersionTag\"

# ── 4. PostgreSQL 업데이트 ──────────────────────────────────────────────────
Step 4 "PostgreSQL 업데이트"
if ($SkipDB) {
    SKIP "-SkipDB 플래그 지정됨"
} elseif (-not (Test-DockerContainer "verilog-postgres")) {
    WARN "verilog-postgres 미실행 → 건너뜁니다."
} else {
    Get-Content -Raw "$PlatformDir\schema\kg_version_schema.sql" |
        docker exec -i verilog-postgres psql -U postgres -d verilog 2>$null
    # 모든 파일을 하나씩 적용 (merged 결과만 DB에 반영)
    foreach ($d in $DecisionsAbs) {
        python "$IngestDir\apply_labels_to_postgres.py" `
            --decisions "$d" --version-tag "$VersionTag" --db-url "$POSTGRES_URL"
    }
    if ($LASTEXITCODE -ne 0) { WARN "PostgreSQL 업데이트 실패 (계속 진행)" }
    else { OK "PostgreSQL 업데이트 완료" }
}

# ── 5. Neo4j 업데이트 ───────────────────────────────────────────────────────
Step 5 "Neo4j 업데이트"
if ($SkipDB) {
    SKIP "-SkipDB 플래그 지정됨"
} elseif (-not (Test-DockerContainer "verilog-neo4j")) {
    WARN "verilog-neo4j 미실행 → 건너뜁니다."
} else {
    foreach ($d in $DecisionsAbs) {
        python "$IngestDir\apply_labels_to_neo4j.py" `
            --decisions "$d" --version-tag "$VersionTag" `
            --uri "$NEO4J_URI" --user "$NEO4J_USER" --password "$NEO4J_PASS"
    }
    if ($LASTEXITCODE -ne 0) { WARN "Neo4j 업데이트 실패 (계속 진행)" }
    else { OK "Neo4j 업데이트 완료" }
}

# ── 6. Review Console 데이터 갱신 ───────────────────────────────────────────
Step 6 "Review Console 데이터 갱신"
python "$ScriptsDir\build_full_review_data.py"
if ($LASTEXITCODE -ne 0) { throw "build_full_review_data 실패" }
OK "review_full/ 갱신 완료"

# ── 버전 히스토리 ────────────────────────────────────────────────────────────
$indexPath = "$OutDir\kg_versions\index.json"
if (Test-Path $indexPath) {
    $index = Get-Content $indexPath -Raw | ConvertFrom-Json
    Write-Host ""
    Write-Host "  버전     생성일                    모듈    레이블   엣지   승인추가" -ForegroundColor White
    Write-Host "  -------  ------------------------  ------  -------  -----  --------" -ForegroundColor DarkGray
    foreach ($v in $index.versions) {
        $cur = if ($v.version_tag -eq $VersionTag) { " ◄ current" } else { "" }
        Write-Host ("  {0,-8} {1,-25} {2,6}  {3,7}  {4,5}  {5,8}{6}" -f `
            $v.version_tag,
            ($v.created_at -replace "T"," " -replace "\.\d+Z",""),
            $v.modules_total, $v.labels_total, $v.edges_total,
            $v.approved_added, $cur)
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host " KG 업데이트 완료: $VersionTag" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "버전 지정 평가:" -ForegroundColor Yellow
Write-Host "  cd $EvalDir"
Write-Host "  python run_retrieval_benchmark.py --version $VersionTag"
Write-Host "브라우저 새로고침: http://127.0.0.1:8000/platform/ui/review-console/index.html"
