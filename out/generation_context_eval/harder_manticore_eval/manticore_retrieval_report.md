# Manticore Retrieval Analysis

This compares parser+LSP retrieval against a Manticore Search-style BM25F index.

## Inputs

- modules indexed: 1012
- questions: 77
- manticore repo: tools/manticoresearch
- analysis note: Local BM25F model of Manticore Search over parser+LSP fields; schema/documents are emitted for real server loading.

## Aggregate

| Mode | hit@1 | hit@3 | MRR | weighted hit@1 | avg query ms |
|---|---:|---:|---:|---:|---:|
| baseline | 0.7532 | 0.9481 | 0.8457 | 0.7497 | 483.503 |
| kg | 0.7662 | 0.9481 | 0.8478 | 0.761 | 368.347 |
| manticore_parser_lsp | 0.3117 | 0.4286 | 0.3721 | 0.3119 | 220.175 |
| manticore_hybrid | 0.2208 | 0.3766 | 0.3152 | 0.2176 | 223.407 |

## By Level

| Mode | L4 | L5 |
|---|---:|---:|
| baseline | 0.8077 | 0.7255 |
| kg | 0.8462 | 0.7255 |
| manticore_parser_lsp | 0.3077 | 0.3137 |
| manticore_hybrid | 0.2692 | 0.1961 |

## Interpretation

- `baseline` is the existing parser+LSP overlap scorer.
- `manticore_parser_lsp` indexes only parser+LSP fields: module name, project, path, ports, instances, and instance names.
- `manticore_hybrid` keeps the Manticore-style ranker but also indexes KG labels, summaries, and reverse parent context.
- This run models Manticore ranking locally and writes load-ready documents/schema; it does not start a Manticore server.
