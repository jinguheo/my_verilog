param(
  [int]$Limit = 100,
  [int]$Port = 8765,
  [switch]$SkipBrowser
)

. "$PSScriptRoot\_common.ps1"

Assert-PathExists (Join-Path $DbRoot "opentitan") "OpenTitan RTL DB"
Assert-PathExists (Join-Path $DbRoot "ibex") "Ibex RTL DB"
Ensure-OutRoot

$demoOut = Join-Path $OutRoot "review_demo_100"
$builder = Join-Path $IngestRoot "build_review_demo_100.py"

Invoke-PythonScript $builder @(
  "--db-root", $DbRoot,
  "--out-dir", $demoOut,
  "--limit", "$Limit"
)

$existing = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
if ($existing) {
  Write-Host "Port $Port is already in use. Reusing existing server if it serves this workspace."
} else {
  Start-Process -FilePath python -ArgumentList @("-m", "http.server", "$Port") -WorkingDirectory $WorkspaceRoot -WindowStyle Hidden
  Start-Sleep -Seconds 2
}

$url = "http://localhost:$Port/platform/ui/review-console/index.html"
$check = Invoke-WebRequest -UseBasicParsing $url
if ($check.StatusCode -ne 200) {
  throw "Review console did not respond: $url"
}

if (-not $SkipBrowser) {
  Start-Process $url
}

Write-Host "Review demo generated."
Write-Host "Console: $url"
Write-Host "Data: $demoOut"
