# Retrieval Benchmark Report

This report compares two retrieval conditions:

- `kg`: uses field-aware module facts, labels, summaries, reverse graph hints, query expansion, and approved label context when available.
- `baseline`: uses parser/LSP style file-local clues such as module name, path, ports, and instances.

## Aggregate

### baseline

- hit@1: 0.5733
- hit@3: 0.6867
- mrr: 0.6378
- weighted hit@1: 0.48
- proxy VerilogEval score (/100): 58.39

### kg

- hit@1: 0.58
- hit@3: 0.7
- mrr: 0.6446
- weighted hit@1: 0.4867
- proxy VerilogEval score (/100): 59.29

## Retrieval Inputs

- modules indexed: 732
- approved labels: D:\MyWork\verilog\out\label_approval\auto_approved_labels.jsonl
- module labels added: 24
- IP context labels added: 69

## VerilogEval Adapter

- status: unavailable
- detail: verilogeval package or runner was not available in this workspace; generated proxy-only score and adapter metadata.

The proxy score is not an official VerilogEval number. It is a local readiness score derived from weighted retrieval accuracy.
