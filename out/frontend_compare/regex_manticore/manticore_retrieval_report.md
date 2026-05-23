# Manticore Retrieval Analysis

This compares parser+LSP retrieval against a Manticore Search-style BM25F index.

## Inputs

- modules indexed: 1088
- questions: 175
- manticore repo: .\tools\manticoresearch
- analysis note: Local BM25F model of Manticore Search over parser+LSP fields; schema/documents are emitted for real server loading.

## Aggregate

| Mode | hit@1 | hit@3 | MRR | weighted hit@1 | avg query ms |
|---|---:|---:|---:|---:|---:|
| baseline | 0.8514 | 0.8629 | 0.8576 | 0.8453 | 107.121 |
| kg | 0.8571 | 0.8686 | 0.8629 | 0.8534 | 82.352 |
| manticore_parser_lsp | 0.8571 | 0.9029 | 0.88 | 0.8404 | 80.571 |
| manticore_hybrid | 0.8514 | 0.9029 | 0.8754 | 0.8323 | 72.831 |

## By Level

| Mode | L1 | L2 | L3 | L4 | L5 |
|---|---:|---:|---:|---:|---:|
| baseline | 0.8 | 1.0 | 0.8571 | 0.7429 | 0.8571 |
| kg | 0.8 | 1.0 | 0.8571 | 0.7429 | 0.8857 |
| manticore_parser_lsp | 0.9429 | 1.0 | 0.7714 | 0.7143 | 0.8571 |
| manticore_hybrid | 0.9429 | 1.0 | 0.7714 | 0.7143 | 0.8286 |

## Interpretation

- `baseline` is the existing parser+LSP overlap scorer.
- `manticore_parser_lsp` indexes only parser+LSP fields: module name, project, path, ports, instances, and instance names.
- `manticore_hybrid` keeps the Manticore-style ranker but also indexes KG labels, summaries, and reverse parent context.
- This run models Manticore ranking locally and writes load-ready documents/schema; it does not start a Manticore server.
