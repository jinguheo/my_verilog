# Regex vs Tree-sitter Saved Summary

Generated: 2026-05-20

## Default Frontend Status

The current seed workflow keeps tree-sitter as the default effective frontend:

- `platform/ingest/generate_ontology_seed.py` default argument: `--frontend auto`
- `auto` resolves to `tree-sitter` when `tree_sitter` and `tree_sitter_verilog` are installed
- Current environment imports both packages successfully
- Current `out/merged_ontology_seed.jsonl` metadata contains only `tree-sitter` frontend rows

Current seed frontend count:

| Frontend | Rows |
|---|---:|
| tree-sitter | 1433 |

## Regex vs Tree-sitter Extraction Size

| Frontend | Raw modules | Indexed modules |
|---|---:|---:|
| regex | 1544 | 1088 |
| tree-sitter | 1433 | 1012 |

Tree-sitter extracts fewer modules, but the extracted structure is cleaner and improves most retrieval quality metrics.

## Retrieval Delta: Tree-sitter Minus Regex

| Mode | Hit@1 Delta | Hit@3 Delta | MRR Delta | Weighted Hit@1 Delta |
|---|---:|---:|---:|---:|
| baseline | +0.0115 | +0.0114 | +0.0248 | +0.0148 |
| kg | +0.0115 | +0.0114 | +0.0104 | +0.0149 |
| manticore_parser_lsp | +0.0058 | -0.0058 | +0.0135 | +0.0019 |
| manticore_hybrid | +0.0115 | -0.0058 | +0.0027 | +0.0100 |

## Interpretation

- Tree-sitter should remain the default frontend.
- Regex should remain as a fallback only, mainly for environments where tree-sitter is unavailable.
- Regex can occasionally improve Hit@3 for Manticore-style broad full-text ranking because it extracts more modules, but this comes with more noise.
- Tree-sitter is better for high-confidence module, port, instance, and source-location structure.

## Related Files

- Detailed report: `out/tree_sitter_easy_hard_eval/tree_sitter_easy_hard_four_methods.md`
- Detailed JSON: `out/tree_sitter_easy_hard_eval/tree_sitter_easy_hard_four_methods.json`
- Original frontend comparison: `out/frontend_compare/regex_vs_tree_sitter_eval.json`
- Current seed: `out/merged_ontology_seed.jsonl`
