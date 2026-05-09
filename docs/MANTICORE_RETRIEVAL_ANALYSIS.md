# Manticore Retrieval Analysis

Use this flow to analyze parser+LSP retrieval after indexing the extracted RTL
module facts with a Manticore Search-style full-text ranker.

## What It Compares

| Mode | Meaning |
|---|---|
| `baseline` | Existing parser+LSP overlap scorer over module name, path, ports, and instances |
| `kg` | Existing KG-aware scorer with labels, summaries, and graph context |
| `manticore_parser_lsp` | BM25F-style full-text ranker over parser+LSP fields only |
| `manticore_hybrid` | BM25F-style full-text ranker over parser+LSP fields plus KG labels, summaries, and parents |

The current runner models Manticore Search ranking locally so it does not need a
running `searchd` service. It also writes load-ready Manticore documents and a
SQL schema for later server-backed experiments.

## Command

```powershell
.\.venv-graphify\Scripts\python.exe platform\eval\run_manticore_retrieval_analysis.py `
  --seed out\merged_ontology_seed.jsonl `
  --questions out\multiaxis_benchmark\questions_all.jsonl `
  --out-dir out\manticore_analysis `
  --manticore-repo tools\manticoresearch
```

## Outputs

| File | Purpose |
|---|---|
| `out\manticore_analysis\manticore_retrieval_report.md` | Human-readable aggregate report |
| `out\manticore_analysis\manticore_retrieval_report.json` | Metrics by mode, level, and question type |
| `out\manticore_analysis\manticore_detailed_runs.json` | Top-k results and reasons per question |
| `out\manticore_analysis\manticore_documents.jsonl` | Parser+LSP documents that can be loaded into Manticore |
| `out\manticore_analysis\manticore_schema.sql` | Manticore table schema and example query |

## Current Result

On the 175-question multiaxis benchmark with 732 indexed modules:

| Mode | hit@1 | hit@3 | MRR | weighted hit@1 |
|---|---:|---:|---:|---:|
| `baseline` | 0.8514 | 0.8629 | 0.8686 | 0.8393 |
| `kg` | 0.8514 | 0.8629 | 0.8562 | 0.8423 |
| `manticore_parser_lsp` | 0.8629 | 0.8914 | 0.8857 | 0.8401 |
| `manticore_hybrid` | 0.8686 | 0.8914 | 0.8781 | 0.8479 |

The parser+LSP fields benefit from BM25F-style ranking: `manticore_parser_lsp`
improves hit@1 over the baseline by 1.15 percentage points and hit@3 by 2.85
points. Adding KG fields into the Manticore-style ranker improves hit@1 a bit
more, but still leaves difficult L4 function/structure questions as the main
weak point.
