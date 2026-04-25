. "$PSScriptRoot\_common.ps1"

$seed = Join-Path $OutRoot "merged_ontology_seed.jsonl"
$labels = Join-Path $OutRoot "merged_labels.jsonl"
$labelApprovalOut = Join-Path $OutRoot "label_approval"
$reviewCandidates = Join-Path $labelApprovalOut "review_queue.jsonl"
Assert-PathExists $seed "Merged ontology seed"
Assert-PathExists $labels "Merged labels"

Invoke-PythonScript (Join-Path $IngestRoot "auto_approve_labels.py") @(
  "--seed", $seed,
  "--labels", $labels,
  "--out-dir", $labelApprovalOut
)
Write-Host "Auto-approval completed."
Write-Host "Review queue: $reviewCandidates"
