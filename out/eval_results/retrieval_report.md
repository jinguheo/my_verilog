# Retrieval Benchmark Report

This report compares two retrieval conditions:

- `kg`: uses labels, summaries, reverse graph hints, and query expansion.
- `baseline`: uses parser/LSP style file-local clues such as module name, path, ports, and instances.

## Aggregate

### baseline

- hit@1: 0.1533
- hit@3: 0.3533
- mrr: 0.254
- weighted hit@1: 0.1356
- proxy VerilogEval score (/100): 23.55

### kg

- hit@1: 0.2333
- hit@3: 0.42
- mrr: 0.3392
- weighted hit@1: 0.2111
- proxy VerilogEval score (/100): 30.98

## VerilogEval Adapter

- status: unavailable
- detail: verilogeval package or runner was not available in this workspace; generated proxy-only score and adapter metadata.

The proxy score is not an official VerilogEval number. It is a local readiness score derived from weighted retrieval accuracy.
