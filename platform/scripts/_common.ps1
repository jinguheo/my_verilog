$ErrorActionPreference = "Stop"

$Script:PlatformRoot = Split-Path -Parent $PSScriptRoot
$Script:WorkspaceRoot = Split-Path -Parent $Script:PlatformRoot
$Script:DbRoot = Join-Path $Script:WorkspaceRoot "dbs"
$Script:OutRoot = Join-Path $Script:WorkspaceRoot "out"
$Script:RuntimeRoot = Join-Path $Script:PlatformRoot "runtime"
$Script:IngestRoot = Join-Path $Script:PlatformRoot "ingest"
$Script:SchemaRoot = Join-Path $Script:PlatformRoot "schema"

function Assert-PathExists {
  param(
    [Parameter(Mandatory=$true)][string]$Path,
    [Parameter(Mandatory=$true)][string]$Purpose
  )
  if (-not (Test-Path -LiteralPath $Path)) {
    throw "$Purpose not found: $Path"
  }
}

function Invoke-PythonScript {
  param(
    [Parameter(Mandatory=$true)][string]$Script,
    [string[]]$Args = @()
  )
  Assert-PathExists $Script "Python script"
  & python $Script @Args
  if ($LASTEXITCODE -ne 0) {
    throw "Python script failed: $Script"
  }
}

function Ensure-OutRoot {
  New-Item -ItemType Directory -Force -Path $Script:OutRoot | Out-Null
}

function Ensure-PlatformEnv {
  $envPath = Join-Path $Script:PlatformRoot ".env"
  $examplePath = Join-Path $Script:PlatformRoot ".env.example"
  if (-not (Test-Path -LiteralPath $envPath)) {
    Copy-Item -LiteralPath $examplePath -Destination $envPath
  }
  return $envPath
}

function Assert-CommandExists {
  param(
    [Parameter(Mandatory=$true)][string]$Command,
    [Parameter(Mandatory=$true)][string]$InstallHint
  )
  if (-not (Get-Command $Command -ErrorAction SilentlyContinue)) {
    throw "$Command is not available. $InstallHint"
  }
}
