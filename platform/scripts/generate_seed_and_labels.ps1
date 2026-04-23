. "$PSScriptRoot\_common.ps1"

Ensure-OutRoot

$opentitan = Join-Path $DbRoot "opentitan"
$ibex = Join-Path $DbRoot "ibex"
Assert-PathExists $opentitan "OpenTitan RTL DB"
Assert-PathExists $ibex "Ibex RTL DB"

$opentitanSeed = Join-Path $OutRoot "opentitan_ontology_seed.jsonl"
$ibexSeed = Join-Path $OutRoot "ibex_ontology_seed.jsonl"
$opentitanLabels = Join-Path $OutRoot "opentitan_labels.jsonl"
$ibexLabels = Join-Path $OutRoot "ibex_labels.jsonl"
$mergedSeed = Join-Path $OutRoot "merged_ontology_seed.jsonl"
$mergedLabels = Join-Path $OutRoot "merged_labels.jsonl"
$embeddingRows = Join-Path $OutRoot "embedding_rows.json"

Invoke-PythonScript (Join-Path $IngestRoot "generate_ontology_seed.py") @("--root", $opentitan, "--out", $opentitanSeed)
Invoke-PythonScript (Join-Path $IngestRoot "generate_ontology_seed.py") @("--root", $ibex, "--out", $ibexSeed)

Invoke-PythonScript (Join-Path $IngestRoot "extract_opentitan_labels.py") @("--root", $opentitan, "--out", $opentitanLabels)
Invoke-PythonScript (Join-Path $IngestRoot "extract_ibex_labels.py") @("--root", $ibex, "--out", $ibexLabels)

Invoke-PythonScript (Join-Path $IngestRoot "merge_jsonl.py") @("--inputs", $opentitanSeed, $ibexSeed, "--out", $mergedSeed)
Invoke-PythonScript (Join-Path $IngestRoot "merge_jsonl.py") @("--inputs", $opentitanLabels, $ibexLabels, "--out", $mergedLabels)

Invoke-PythonScript (Join-Path $IngestRoot "prepare_embedding_rows.py") @("--seed", $mergedSeed, "--outfile", $embeddingRows)
Write-Host "OpenTitan + Ibex seed, labels, merged seed, merged labels, and embedding rows generated."
