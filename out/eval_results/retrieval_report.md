# Retrieval Benchmark Report

This report compares two retrieval conditions:

- `kg`: uses field-aware module facts, labels, summaries, reverse graph hints, query expansion, and approved label context when available.
- `baseline`: uses parser/LSP style file-local clues such as module name, path, ports, and instances.

## Aggregate

### baseline

- hit@1: 0.8067
- hit@3: 0.8467
- mrr: 0.8303
- weighted hit@1: 0.7822
- proxy VerilogEval score (/100): 81.44

### kg

- hit@1: 0.8467
- hit@3: 0.8667
- mrr: 0.8612
- weighted hit@1: 0.8356
- proxy VerilogEval score (/100): 85.16

## Retrieval Inputs

- modules indexed: 1012
- approved labels: D:\MyWork\verilog\out\label_approval\auto_approved_labels.jsonl
- module labels added: 22
- IP context labels added: 115

## VerilogEval Adapter

- status: unavailable
- detail: verilogeval package or runner was not available in this workspace; generated proxy-only score and adapter metadata.

The proxy score is not an official VerilogEval number. It is a local readiness score derived from weighted retrieval accuracy.
