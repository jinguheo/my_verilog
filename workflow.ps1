param(
  [ValidateSet("demo", "seed", "review", "benchmark", "stack", "schema", "neo4j", "module-api", "vector-api", "generator", "full", "status")]
  [string]$Step = "demo",
  [int]$Limit = 100,
  [int]$Port = 8765,
  [switch]$SkipBrowser
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Scripts = Join-Path $Root "platform\scripts"

function Invoke-Step {
  param([string]$Script, [string[]]$Args = @())
  $Path = Join-Path $Scripts $Script
  if (-not (Test-Path -LiteralPath $Path)) {
    throw "Missing workflow script: $Path"
  }
  & powershell -NoProfile -ExecutionPolicy Bypass -File $Path @Args
}

switch ($Step) {
  "demo" {
    $args = @("-Limit", "$Limit", "-Port", "$Port")
    if ($SkipBrowser) {
      $args += "-SkipBrowser"
    }
    Invoke-Step "build_review_demo.ps1" $args
  }
  "seed" {
    Invoke-Step "generate_seed_and_labels.ps1"
  }
  "review" {
    Invoke-Step "prepare_review_candidates.ps1"
  }
  "benchmark" {
    Invoke-Step "run_benchmark_eval.ps1"
  }
  "stack" {
    Invoke-Step "start_stack.ps1"
  }
  "schema" {
    Invoke-Step "load_postgres_schema.ps1"
  }
  "neo4j" {
    Invoke-Step "load_neo4j.ps1"
  }
  "module-api" {
    Invoke-Step "run_module_qa_api.ps1"
  }
  "vector-api" {
    Invoke-Step "run_vector_search_api.ps1"
  }
  "generator" {
    Invoke-Step "run_generation_orchestrator.ps1"
  }
  "full" {
    Invoke-Step "full_bootstrap.ps1"
  }
  "status" {
    Invoke-Step "check_workflow_status.ps1"
  }
}
