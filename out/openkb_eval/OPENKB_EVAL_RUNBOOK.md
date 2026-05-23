# OpenKB Evaluation Runbook

## Repository

- Source: https://github.com/VectifyAI/OpenKB
- Local checkout: `tools/OpenKB`
- Installed into: `.venv-graphify`

## Environment

PowerShell:

```powershell
$env:PYTHONIOENCODING='utf-8'
$env:LITELLM_LOCAL_MODEL_COST_MAP='True'
$env:LLM_API_KEY='<your key>'
```

## Build OpenKB Wiki

The KB skeleton is already initialized by `prepare_openkb_eval.py`.
If you want to recreate it interactively, run `openkb init`; otherwise start from `openkb add`.

```powershell
cd out\openkb_eval\kb
..\..\..\.venv-graphify\Scripts\openkb.exe add .\raw
..\..\..\.venv-graphify\Scripts\openkb.exe status
```

The raw files are already staged in:

```text
D:\MyWork\verilog\out\openkb_eval\kb\raw
```

## Query Evaluation

Questions: `D:\MyWork\verilog\out\openkb_eval\openkb_eval_questions.jsonl`

For each row, run:

```powershell
..\..\..\.venv-graphify\Scripts\openkb.exe query "<question>"
```

Score as hit@1-style success when the answer explicitly names at least one `gold_modules` value.

## Notes

- OpenKB is LLM-backed; evaluation cannot be completed offline without `LLM_API_KEY`.
- OpenKB's value here is compiled wiki/context synthesis, not direct Verilog simulation.
- Compare against existing Parser/LSP, Manticore, KG, and Graphify context-readiness reports.
