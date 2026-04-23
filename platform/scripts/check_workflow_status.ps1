. "$PSScriptRoot\_common.ps1"

$paths = @(
  @{Name="OpenTitan DB"; Path=(Join-Path $DbRoot "opentitan")},
  @{Name="Ibex DB"; Path=(Join-Path $DbRoot "ibex")},
  @{Name="sv-tests DB"; Path=(Join-Path $DbRoot "sv-tests")},
  @{Name="RTLLM DB"; Path=(Join-Path $DbRoot "RTLLM")},
  @{Name="Review demo data"; Path=(Join-Path $OutRoot "review_demo_100\review_console_data.json")},
  @{Name="Merged ontology seed"; Path=(Join-Path $OutRoot "merged_ontology_seed.jsonl")},
  @{Name="Merged labels"; Path=(Join-Path $OutRoot "merged_labels.jsonl")},
  @{Name="Platform env"; Path=(Join-Path $PlatformRoot ".env")}
)

$rows = foreach ($item in $paths) {
  [PSCustomObject]@{
    Item = $item.Name
    Exists = Test-Path -LiteralPath $item.Path
    Path = $item.Path
  }
}

$rows | Format-Table -AutoSize

Write-Host ""
Write-Host "Expected quick review command:"
Write-Host "  powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step demo"
