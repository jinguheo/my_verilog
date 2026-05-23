# Knowledge DB Evaluation

This document describes how the RTL knowledge DB retrieval benchmark is built
and evaluated in this workspace.

## Purpose

The benchmark compares four retrieval modes:

1. `baseline`
   - tree-sitter-verilog seed extraction
   - module name
   - file path
   - ports
   - instances
   - parser/LSP-style local structural signals

2. `kg`
   - the same tree-sitter seed
   - inferred labels
   - summaries
   - reverse graph hints
   - semantic query expansion

3. `graphify`
   - Graphify AST graph
   - BFS query subgraph context
   - graph node matches mapped back to RTL modules

4. `manticore`
   - the same tree-sitter seed
   - Manticore Search-style BM25F ranking over parser/LSP fields

Methods 1, 2, and 4 share the same parser/LSP frontend:

```text
platform/ingest/generate_ontology_seed.py --frontend auto
```

When `.venv-graphify\Scripts\python.exe` is available, the workflow uses that
interpreter so `tree_sitter` and `tree_sitter_verilog` are available. Regex
module extraction remains as a fallback for environments without tree-sitter.

## Generated Questions

The benchmark creates 150 standard questions:

- easy 50
- medium 50
- hard 50

The multiaxis benchmark creates 175 questions across five levels and seven
question types.

Question examples include:

- exact module lookup
- unique port lookup
- label plus port combined lookup
- parent-child retrieval
- path plus interface clue
- reverse graph query
- multi-hop wrapper query
- semantic bridge query

## Run

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step seed
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step benchmark
```

## Outputs

```text
out\eval_benchmark\benchmark_easy.jsonl
out\eval_benchmark\benchmark_medium.jsonl
out\eval_benchmark\benchmark_hard.jsonl
out\eval_benchmark\benchmark_all.jsonl
out\eval_benchmark\benchmark_summary.json

out\eval_results\retrieval_report.json
out\eval_results\retrieval_report.md
out\eval_results\detailed_runs.json
out\eval_results\predictions_for_verilogeval.json
out\eval_results\verilogeval_adapter.json

out\multiaxis_benchmark\questions_all.jsonl
out\multiaxis_eval_results\multiaxis_report.json

out\manticore_analysis\manticore_retrieval_report.json
out\manticore_analysis\manticore_retrieval_report.md
out\manticore_analysis\manticore_detailed_runs.json
out\manticore_analysis\manticore_documents.jsonl
out\manticore_analysis\manticore_schema.sql

out\reports\kg_eval_report.pdf
out\reports\retrieval_methods_comparison.pdf
out\reports\retrieval_software_blocks_comparison.pdf
```

## Current Tree-Sitter Run

The current KG snapshot contains:

- 1433 modules
- 16766 ports
- 2103 instance edges
- 18251 nodes
- 22630 edges

Current multiaxis retrieval metrics:

| Mode | hit@1 | hit@3 | MRR | weighted hit@1 |
|---|---:|---:|---:|---:|
| `baseline` | 0.8629 | 0.8743 | 0.8824 | 0.8601 |
| `kg` | 0.8686 | 0.8800 | 0.8733 | 0.8683 |
| `graphify` | 0.6914 | 0.8971 | 0.7950 | 0.6913 |
| `manticore` | 0.8629 | 0.8971 | 0.8935 | 0.8423 |

## VerilogEval

The official VerilogEval runner is not bundled in this workspace. The benchmark
therefore provides two local artifacts:

1. an adapter-style prediction file that can be connected to an official runner
   later
2. a local proxy VerilogEval readiness score based on retrieval quality

The proxy score is not an official VerilogEval score. It is a normalized
readiness indicator for local retrieval quality.
