. "$PSScriptRoot\_common.ps1"

$seed = Join-Path $OutRoot "merged_ontology_seed.jsonl"
$labels = Join-Path $OutRoot "merged_labels.jsonl"
$kgOut = Join-Path $OutRoot "kg_full"
$benchmarkOut = Join-Path $OutRoot "eval_benchmark"
$resultsOut = Join-Path $OutRoot "eval_results"
$multiaxisOut = Join-Path $OutRoot "multiaxis_benchmark"
$multiaxisResultsOut = Join-Path $OutRoot "multiaxis_eval_results"
$pdfOut = Join-Path $OutRoot "reports\kg_eval_report.pdf"
$pdfJsonOut = Join-Path $OutRoot "reports\kg_eval_report.json"

Assert-PathExists $seed "Merged ontology seed"
Assert-PathExists $labels "Merged labels"

Invoke-PythonScript (Join-Path $PlatformRoot "eval\build_full_kg_snapshot.py") @(
  "--seed", $seed,
  "--labels", $labels,
  "--out-dir", $kgOut
)

Invoke-PythonScript (Join-Path $PlatformRoot "eval\build_qa_benchmark.py") @(
  "--seed", $seed,
  "--labels", $labels,
  "--out-dir", $benchmarkOut,
  "--count-per-level", "50"
)

Invoke-PythonScript (Join-Path $PlatformRoot "eval\build_multiaxis_benchmark.py") @(
  "--seed", $seed,
  "--labels", $labels,
  "--out-dir", $multiaxisOut,
  "--per-cell", "5"
)

Invoke-PythonScript (Join-Path $PlatformRoot "eval\run_retrieval_benchmark.py") @(
  "--seed", $seed,
  "--benchmark", (Join-Path $benchmarkOut "benchmark_all.jsonl"),
  "--out-dir", $resultsOut
)

Invoke-PythonScript (Join-Path $PlatformRoot "eval\run_multiaxis_retrieval_benchmark.py") @(
  "--seed", $seed,
  "--questions", (Join-Path $multiaxisOut "questions_all.jsonl"),
  "--out-dir", $multiaxisResultsOut
)

Invoke-PythonScript (Join-Path $PlatformRoot "eval\render_eval_pdf.py") @(
  "--kg-summary", (Join-Path $kgOut "kg_full_summary.json"),
  "--benchmark-summary", (Join-Path $benchmarkOut "benchmark_summary.json"),
  "--retrieval-report", (Join-Path $resultsOut "retrieval_report.json"),
  "--multiaxis-summary", (Join-Path $multiaxisOut "summary.json"),
  "--multiaxis-report", (Join-Path $multiaxisResultsOut "multiaxis_report.json"),
  "--out-pdf", $pdfOut,
  "--out-json", $pdfJsonOut
)

Write-Host "Benchmark generated."
Write-Host "Full KG:    $kgOut"
Write-Host "Questions: $benchmarkOut"
Write-Host "Results:   $resultsOut"
Write-Host "MultiAxis: $multiaxisResultsOut"
Write-Host "PDF:       $pdfOut"
