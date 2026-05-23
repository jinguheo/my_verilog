# Regex vs Tree-Sitter Retrieval Evaluation

Generated: 2026-05-09T20:40:07

The comparison fixes the same 175-question multiaxis benchmark and changes only the Verilog/SystemVerilog seed frontend.

## Corpus

| Frontend | Raw extracted modules | Clean indexed modules | Seed |
|---|---:|---:|---|
| regex | 1544 | 1088 | `regex_merged_ontology_seed.jsonl` |
| tree-sitter | 1433 | 1012 | `tree-sitter_merged_ontology_seed.jsonl` |

## Metrics

| Mode | Frontend | hit@1 | hit@3 | MRR | weighted hit@1 |
|---|---|---:|---:|---:|---:|
| `baseline` | regex | 0.8514 | 0.8629 | 0.8576 | 0.8453 |
| `baseline` | tree-sitter | 0.8629 | 0.8743 | 0.8824 | 0.8601 |
| `kg` | regex | 0.8571 | 0.8686 | 0.8629 | 0.8534 |
| `kg` | tree-sitter | 0.8686 | 0.8800 | 0.8733 | 0.8683 |
| `manticore_parser_lsp` | regex | 0.8571 | 0.9029 | 0.8800 | 0.8404 |
| `manticore_parser_lsp` | tree-sitter | 0.8629 | 0.8971 | 0.8935 | 0.8423 |
| `manticore_hybrid` | regex | 0.8514 | 0.9029 | 0.8754 | 0.8323 |
| `manticore_hybrid` | tree-sitter | 0.8629 | 0.8971 | 0.8781 | 0.8423 |

## Delta: Tree-Sitter Minus Regex

| Mode | hit@1 | hit@3 | MRR | weighted hit@1 |
|---|---:|---:|---:|---:|
| `baseline` | +0.0115 | +0.0114 | +0.0248 | +0.0148 |
| `kg` | +0.0115 | +0.0114 | +0.0104 | +0.0149 |
| `manticore_parser_lsp` | +0.0058 | -0.0058 | +0.0135 | +0.0019 |
| `manticore_hybrid` | +0.0115 | -0.0058 | +0.0027 | +0.0100 |

## Interpretation

- Tree-sitter extracts fewer raw modules, but the cleaner AST-derived corpus improves baseline and KG hit@1.
- Regex has slightly better hit@3 for Manticore modes, likely because the larger/noisier corpus still puts more possible targets somewhere in the top 3.
- Tree-sitter has better MRR for baseline, KG, and parser/LSP Manticore, meaning correct answers tend to appear higher when they are found.
- For production seed generation, tree-sitter is the better default because it improves precision-oriented metrics and avoids regex false positives.
