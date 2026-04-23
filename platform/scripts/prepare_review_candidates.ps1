. "$PSScriptRoot\_common.ps1"

$labels = Join-Path $OutRoot "merged_labels.jsonl"
$reviewCandidates = Join-Path $OutRoot "review_candidates.jsonl"
Assert-PathExists $labels "Merged labels"

Invoke-PythonScript (Join-Path $IngestRoot "promote_reviewed_labels.py") @("--infile", $labels, "--outfile", $reviewCandidates)
Write-Host "Review candidate file prepared."
