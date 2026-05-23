# Manticore Retrieval Analysis

This compares parser+LSP retrieval against a Manticore Search-style BM25F index.

## Inputs

- modules indexed: 1012
- questions: 117
- manticore repo: tools/manticoresearch
- analysis note: Local BM25F model of Manticore Search over parser+LSP fields; schema/documents are emitted for real server loading.

## Aggregate

| Mode | hit@1 | hit@3 | MRR | weighted hit@1 | avg query ms |
|---|---:|---:|---:|---:|---:|
| baseline | 0.2821 | 0.5214 | 0.4168 | 0.278 | 259.3 |
| kg | 0.3162 | 0.5897 | 0.4557 | 0.3157 | 283.133 |
| manticore_parser_lsp | 0.0513 | 0.1624 | 0.1231 | 0.0496 | 395.788 |
| manticore_hybrid | 0.0513 | 0.1624 | 0.1197 | 0.0496 | 442.067 |

## By Level

| Mode | L4 | L5 |
|---|---:|---:|
| baseline | 0.322 | 0.2414 |
| kg | 0.322 | 0.3103 |
| manticore_parser_lsp | 0.0678 | 0.0345 |
| manticore_hybrid | 0.0678 | 0.0345 |

## Interpretation

- `baseline` is the existing parser+LSP overlap scorer.
- `manticore_parser_lsp` indexes only parser+LSP fields: module name, project, path, ports, instances, and instance names.
- `manticore_hybrid` keeps the Manticore-style ranker but also indexes KG labels, summaries, and reverse parent context.
- This run models Manticore ranking locally and writes load-ready documents/schema; it does not start a Manticore server.
