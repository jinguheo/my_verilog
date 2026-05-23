# Manticore Retrieval Analysis

Use this flow to add Manticore Search as the fourth retrieval evaluation method
after parser+LSP processing.

## What It Compares

| Mode | Meaning |
|---|---|
| `baseline` | Existing parser+LSP overlap scorer over module name, path, ports, and instances |
| `kg` | Existing KG-aware scorer with labels, summaries, and graph context |
| `manticore_parser_lsp` | BM25F-style full-text ranker over parser+LSP fields only |
| `manticore_hybrid` | BM25F-style full-text ranker over parser+LSP fields plus KG labels, summaries, and parents |

The standalone Manticore runner models Manticore Search ranking locally so it
does not need a running `searchd` service. It also writes load-ready Manticore
documents and a SQL schema for later server-backed experiments.

The final comparison report uses exactly four methods:

1. `parser_lsp`
2. `kg`
3. `graphify`
4. `manticore`

## Command

```powershell
.\.venv-graphify\Scripts\python.exe platform\eval\run_manticore_retrieval_analysis.py `
  --seed out\merged_ontology_seed.jsonl `
  --questions out\multiaxis_benchmark\questions_all.jsonl `
  --out-dir out\manticore_analysis `
  --manticore-repo tools\manticoresearch

.\.venv-graphify\Scripts\python.exe platform\eval\run_four_method_retrieval_comparison.py
```

## Outputs

| File | Purpose |
|---|---|
| `out\manticore_analysis\manticore_retrieval_report.md` | Human-readable aggregate report |
| `out\manticore_analysis\manticore_retrieval_report.json` | Metrics by mode, level, and question type |
| `out\manticore_analysis\manticore_detailed_runs.json` | Top-k results and reasons per question |
| `out\manticore_analysis\manticore_documents.jsonl` | Parser+LSP documents that can be loaded into Manticore |
| `out\manticore_analysis\manticore_schema.sql` | Manticore table schema and example query |
| `out\reports\retrieval_methods_comparison.md` | Final four-method comparison report |
| `out\reports\retrieval_methods_comparison.json` | Final four-method comparison data |

## Current Result

On the 175-question multiaxis benchmark with 1012 indexed modules from the
tree-sitter-verilog seed frontend:

| Mode | hit@1 | hit@3 | MRR | weighted hit@1 |
|---|---:|---:|---:|---:|
| `baseline` | 0.8629 | 0.8743 | 0.8824 | 0.8601 |
| `kg` | 0.8686 | 0.8800 | 0.8733 | 0.8683 |
| `manticore_parser_lsp` | 0.8629 | 0.8971 | 0.8935 | 0.8423 |
| `manticore_hybrid` | 0.8629 | 0.8971 | 0.8781 | 0.8423 |

The final four-method comparison is:

| Method | hit@1 | hit@3 | MRR | weighted hit@1 |
|---|---:|---:|---:|---:|
| `parser_lsp` | 0.8629 | 0.8743 | 0.8824 | 0.8601 |
| `kg` | 0.8686 | 0.8800 | 0.8733 | 0.8683 |
| `graphify` | 0.6914 | 0.8971 | 0.7950 | 0.6913 |
| `manticore` | 0.8629 | 0.8971 | 0.8935 | 0.8423 |

In this run, the KG scorer has the best weighted hit@1, while the Manticore
parser/LSP ranker has the best hit@3 and MRR. Graphify is still useful for broad
codebase navigation, but it is weaker for exact Verilog module retrieval in this
benchmark.
