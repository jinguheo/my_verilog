. "$PSScriptRoot\_common.ps1"

$seed = Join-Path $OutRoot "merged_ontology_seed.jsonl"
$labels = Join-Path $OutRoot "merged_labels.jsonl"
Assert-PathExists $seed "Merged ontology seed"
Assert-PathExists $labels "Merged labels"

Invoke-PythonScript (Join-Path $IngestRoot "load_ontology_to_neo4j.py") @(
  "--seed", $seed,
  "--labels", $labels,
  "--uri", "neo4j://localhost:7687",
  "--user", "neo4j",
  "--password", "neo4jpassword"
)
Write-Host "Neo4j loaded from merged OpenTitan + Ibex artifacts."
