. "$PSScriptRoot\_common.ps1"

Write-Host "=== ontology-first multi-project pipeline ==="
& "$PSScriptRoot\generate_seed_and_labels.ps1"
Write-Host "Done. Next: review merged labels and create embeddings."
