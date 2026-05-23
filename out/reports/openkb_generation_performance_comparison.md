# OpenKB Generation Performance Comparison

Generated: 2026-05-09T21:19:42

## Result Table

| Method | Status | Questions | hit@1 | hit@3 | hit@5 | MRR | Notes |
|---|---|---:|---:|---:|---:|---:|---|
| 1. Parser + LSP | measured | 77 | 0.9481 | 1.0000 | 1.0000 | 0.9675 | Hard Verilog generation-context readiness benchmark |
| 2. Parser + LSP + Manticore | measured | 77 | 0.8312 | 0.8961 | 0.9481 | 0.8645 | Hard Verilog generation-context readiness benchmark |
| 3. KG | measured | 77 | 0.9481 | 0.9870 | 1.0000 | 0.9658 | Hard Verilog generation-context readiness benchmark |
| 4. Graphify | measured | 77 | 0.9740 | 0.9740 | 0.9740 | 0.9740 | Hard Verilog generation-context readiness benchmark |
| 5. OpenKB | prepared, not measured | 80 | N/A | N/A | N/A | N/A | OpenKB raw docs staged, KB skeleton initialized, but indexed documents=0 and LLM_API_KEY is not set |

## OpenKB Status

- Raw documents staged: 3
- Indexed documents: 0
- Evaluation questions prepared: 80
- LLM_API_KEY present: false

## Interpretation

- Graphify is currently best among measured methods on hit@1 and MRR.
- Parser + LSP and KG are tied on hit@1 and both achieve perfect hit@5.
- Manticore Parser/LSP is weaker on hard L4/L5 generation prompts.
- OpenKB cannot be fairly compared until raw docs are compiled with an LLM API key and OpenKB query outputs are scored.

## To Complete OpenKB Measurement

```powershell
$env:PYTHONIOENCODING='utf-8'
$env:LITELLM_LOCAL_MODEL_COST_MAP='True'
$env:LLM_API_KEY='<your key>'
cd D:\MyWork\verilog\out\openkb_eval\kb
..\..\..\.venv-graphify\Scripts\openkb.exe add .\raw
cd D:\MyWork\verilog
.\.venv-graphify\Scripts\python.exe .\platform\eval\run_openkb_eval.py
```
