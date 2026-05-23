# Verilog Knowledge Base Evaluation Snapshot

This file is prepared as OpenKB raw input. It summarizes the current local RTL knowledge-base benchmark state.

## KG Snapshot

| Metric | Value |
| --- | --- |
| modules | 1433 |
| ports | 16766 |
| instance_edges | 2103 |
| total_nodes | 18251 |
| total_edges | 22630 |

## Project Modules

| Project | Modules |
| --- | --- |
| opentitan | 1142 |
| ibex | 291 |

## Current Retrieval Metrics

| Mode | hit@1 | hit@3 | MRR | weighted hit@1 |
| --- | --- | --- | --- | --- |
| baseline | 0.8629 | 0.8743 | 0.8824 | 0.8601 |
| kg | 0.8686 | 0.88 | 0.8733 | 0.8683 |
| manticore_parser_lsp | 0.8629 | 0.8971 | 0.8935 | 0.8423 |
| manticore_hybrid | 0.8629 | 0.8971 | 0.8781 | 0.8423 |

## Regex vs Tree-Sitter Frontend

Tree-sitter is the default frontend for methods 1-3. Regex remains a fallback.

