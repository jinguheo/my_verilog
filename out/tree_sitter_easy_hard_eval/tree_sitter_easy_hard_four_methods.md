# Tree-sitter Frontend and Four-method Easy/Hard Evaluation

This report verifies whether tree-sitter is available and whether the current seed uses tree-sitter, then summarizes easy and hard retrieval performance for four methods.

## Tree-sitter Verification

- `tree_sitter` import: True
- `tree_sitter_verilog` import: True
- Current seed frontend counts: `{'tree-sitter': 1433}`

## Regex vs Tree-sitter

| Mode | Hit@1 Delta | Hit@3 Delta | MRR Delta | Weighted Hit@1 Delta |
|---|---:|---:|---:|---:|
| baseline | +0.0115 | +0.0114 | +0.0248 | +0.0148 |
| kg | +0.0115 | +0.0114 | +0.0104 | +0.0149 |
| manticore_parser_lsp | +0.0058 | -0.0058 | +0.0135 | +0.0019 |
| manticore_hybrid | +0.0115 | -0.0058 | +0.0027 | +0.0100 |

## Four Methods: Easy Questions

| Method | Count | Hit@1 | Hit@3 | MRR |
|---|---:|---:|---:|---:|
| parser_lsp | 50 | 1.0000 | 1.0000 | 1.0000 |
| kg | 50 | 0.9800 | 1.0000 | 0.9900 |
| graphify | 50 | 0.8800 | 0.9800 | 0.9233 |
| manticore | 50 | 1.0000 | 1.0000 | 1.0000 |

## Four Methods: Hard Questions

| Method | Count | Hit@1 | Hit@3 | MRR |
|---|---:|---:|---:|---:|
| parser_lsp | 50 | 0.7800 | 0.9000 | 0.8380 |
| kg | 50 | 0.8800 | 0.9200 | 0.9047 |
| graphify | 50 | 0.0000 | 0.2200 | 0.1539 |
| manticore | 50 | 0.0000 | 0.2000 | 0.1523 |

## Reading

- Tree-sitter is available and the current merged seed is tree-sitter-based.
- Regex-to-tree-sitter improves most Hit@1/MRR metrics, but Manticore Hit@3 is slightly higher with regex in the older frontend comparison snapshot.
- On the current 150-question easy/hard benchmark, KG is strongest on hard questions; Graphify is strong on easy exact/module navigation but weak on hard exact retrieval.
