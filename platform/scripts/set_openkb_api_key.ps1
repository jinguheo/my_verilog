param(
  [string]$Key = "",
  [switch]$PersistUserEnv
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$kbDirs = @(
  (Join-Path -Path $repoRoot -ChildPath "dbs\graphify-out\kb-variants\spec-only\kb"),
  (Join-Path -Path $repoRoot -ChildPath "dbs\graphify-out\kb-variants\spec-code\kb")
)

if ([string]::IsNullOrWhiteSpace($Key)) {
  $secure = Read-Host "Enter LLM_API_KEY for OpenKB" -AsSecureString
  $ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
  try {
    $Key = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr)
  } finally {
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr)
  }
}

if ([string]::IsNullOrWhiteSpace($Key)) {
  throw "No API key was provided."
}

foreach ($kb in $kbDirs) {
  if (-not (Test-Path $kb)) {
    throw "KB directory not found: $kb"
  }
  $envPath = Join-Path $kb ".env"
  $envLines = @(
    "LLM_API_KEY=$Key",
    "OPENAI_API_KEY=$Key"
  )
  $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
  [System.IO.File]::WriteAllLines($envPath, $envLines, $utf8NoBom)
  Write-Host "Wrote $envPath"
}

if ($PersistUserEnv) {
  [Environment]::SetEnvironmentVariable("LLM_API_KEY", $Key, "User")
  [Environment]::SetEnvironmentVariable("OPENAI_API_KEY", $Key, "User")
  Write-Host "Stored LLM_API_KEY and OPENAI_API_KEY in the current user's environment."
}

Write-Host "Done. .env is ignored by Git."
