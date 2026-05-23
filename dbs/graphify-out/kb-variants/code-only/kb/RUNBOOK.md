# code-only OpenKB Runbook

This workspace is OpenKB-ready. Raw inputs are normalized to Markdown.

## Content

- Includes spec documents: False
- Includes code graph artifacts: True

## Optional LLM-backed indexing

Set an LLM key, then run:

```powershell
$env:PYTHONIOENCODING='utf-8'
$env:LITELLM_LOCAL_MODEL_COST_MAP='True'
$env:LLM_API_KEY='<your key>'
D:\MyWork\verilog\.venv-graphify\Scripts\openkb.exe --kb-dir D:\MyWork\verilog\dbs\graphify-out\kb-variants\code-only\kb add D:\MyWork\verilog\dbs\graphify-out\kb-variants\code-only\kb\raw
D:\MyWork\verilog\.venv-graphify\Scripts\openkb.exe --kb-dir D:\MyWork\verilog\dbs\graphify-out\kb-variants\code-only\kb status
```

No LLM indexing is run by this preparation script.
