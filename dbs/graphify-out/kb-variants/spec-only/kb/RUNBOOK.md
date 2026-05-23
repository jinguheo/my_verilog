# spec-only OpenKB Runbook

This workspace is OpenKB-ready. Raw inputs are normalized to Markdown.

## Content

- Includes spec documents: True
- Includes code graph artifacts: False

## Optional LLM-backed indexing

Set an LLM key, then run:

```powershell
$env:PYTHONIOENCODING='utf-8'
$env:LITELLM_LOCAL_MODEL_COST_MAP='True'
$env:LLM_API_KEY='<your key>'
D:\MyWork\verilog\.venv-graphify\Scripts\openkb.exe --kb-dir D:\MyWork\verilog\dbs\graphify-out\kb-variants\spec-only\kb add D:\MyWork\verilog\dbs\graphify-out\kb-variants\spec-only\kb\raw
D:\MyWork\verilog\.venv-graphify\Scripts\openkb.exe --kb-dir D:\MyWork\verilog\dbs\graphify-out\kb-variants\spec-only\kb status
```

No LLM indexing is run by this preparation script.
