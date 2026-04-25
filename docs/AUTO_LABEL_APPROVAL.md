# Auto Label Approval

This stage sits between raw label proposals and manual review.

## Goal

- auto-approve labels with strong evidence
- send ambiguous labels to a review queue
- auto-reject noisy alias-like labels

## Entry Point

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step review
```

## Input

- `D:\MyWork\verilog\out\merged_ontology_seed.jsonl`
- `D:\MyWork\verilog\out\merged_labels.jsonl`

## Output

- `D:\MyWork\verilog\out\label_approval\auto_approved_labels.jsonl`
- `D:\MyWork\verilog\out\label_approval\review_queue.jsonl`
- `D:\MyWork\verilog\out\label_approval\auto_rejected_labels.jsonl`
- `D:\MyWork\verilog\out\label_approval\all_label_decisions.jsonl`
- `D:\MyWork\verilog\out\label_approval\summary.json`

## Evidence Used

For each proposed label we score:

- name match
- path match
- port match
- instance match
- summary match
- seed label match
- same-project support

## Decision Policy

### Auto Approved

Typical cases:

- OpenTitan IP block with `path_match + summary_match + high source confidence`
- strong `role` or `protocol` label with repeated evidence
- clear project label such as `opentitan_ip` or `ibex_core`

### Needs Review

Typical cases:

- evidence exists but is not decisive
- project/vendor boundary is unclear
- role label is plausible but not yet strongly grounded

### Auto Rejected

Typical cases:

- alias-like label that only repeats the entity name
- generic label with no supporting evidence
- weak proposal with little or no cross-check support

## Operator Workflow

1. Check `summary.json` for the overall split.
2. Use `auto_approved_labels.jsonl` as the approved seed set.
3. Review `review_queue.jsonl` for ambiguous labels only.
4. Ignore `auto_rejected_labels.jsonl` unless you are tuning heuristics.
5. If many good labels land in review, tune rules in `platform\ingest\auto_approve_labels.py` and rerun.

## Current Behavior

The current rules intentionally favor:

- aggressive approval for strong project labels
- rejection of alias/noise labels
- smaller, higher-signal review queues than the raw proposal list
