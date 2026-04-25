# Retrieval Benchmark Report

This report compares two retrieval conditions:

- `kg`: uses field-aware module facts, labels, summaries, reverse graph hints, query expansion, and approved label context when available.
- `baseline`: uses parser/LSP style file-local clues such as module name, path, ports, and instances.

## Aggregate

### baseline

- hit@1: 0.78
- hit@3: 0.82
- mrr: 0.8019
- weighted hit@1: 0.7511
- proxy VerilogEval score (/100): 78.54

### kg

- hit@1: 0.7933
- hit@3: 0.8333
- mrr: 0.8169
- weighted hit@1: 0.7644
- proxy VerilogEval score (/100): 79.9

## Retrieval Inputs

- modules indexed: 732
- approved labels: out\label_approval\auto_approved_labels.jsonl
- module labels added: 24
- IP context labels added: 69

## VerilogEval Adapter

- status: unavailable
- detail: verilogeval package or runner was not available in this workspace; generated proxy-only score and adapter metadata.

The proxy score is not an official VerilogEval number. It is a local readiness score derived from weighted retrieval accuracy.
