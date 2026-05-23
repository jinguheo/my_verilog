# Manticore Retrieval Analysis

This compares parser+LSP retrieval against a Manticore Search-style BM25F index.

## Inputs

- modules indexed: 1012
- questions: 175
- manticore repo: .\tools\manticoresearch
- analysis note: Local BM25F model of Manticore Search over parser+LSP fields; schema/documents are emitted for real server loading.

## Aggregate

| Mode | hit@1 | hit@3 | MRR | weighted hit@1 | avg query ms |
|---|---:|---:|---:|---:|---:|
| baseline | 0.8629 | 0.8743 | 0.8824 | 0.8601 | 96.996 |
| kg | 0.8686 | 0.88 | 0.8733 | 0.8683 | 82.833 |
| manticore_parser_lsp | 0.8629 | 0.8971 | 0.8935 | 0.8423 | 75.049 |
| manticore_hybrid | 0.8629 | 0.8971 | 0.8781 | 0.8423 | 71.036 |

## By Level

| Mode | L1 | L2 | L3 | L4 | L5 |
|---|---:|---:|---:|---:|---:|
| baseline | 0.8 | 1.0 | 0.8571 | 0.7714 | 0.8857 |
| kg | 0.8 | 1.0 | 0.8571 | 0.7714 | 0.9143 |
| manticore_parser_lsp | 1.0 | 1.0 | 0.7429 | 0.7143 | 0.8571 |
| manticore_hybrid | 1.0 | 1.0 | 0.7429 | 0.7143 | 0.8571 |

## Interpretation

- `baseline` is the existing parser+LSP overlap scorer.
- `manticore_parser_lsp` indexes only parser+LSP fields: module name, project, path, ports, instances, and instance names.
- `manticore_hybrid` keeps the Manticore-style ranker but also indexes KG labels, summaries, and reverse parent context.
- This run models Manticore ranking locally and writes load-ready documents/schema; it does not start a Manticore server.
