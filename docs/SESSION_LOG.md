# Session Log

## 2026-05-23 Status Check

Workspace: `D:\MyWork\verilog`

Branch: `main`

Latest commit observed:

- `c0fe5af Add AST-based HDD generation and spec-code linkage pipeline`

Current state:

- `main` is aligned with `origin/main`, but the working tree still has many modified and untracked generated files.
- Several generated graph/evaluation artifacts are present but not all are committed.
- Git also reports repeated warnings about inaccessible global ignore file: `C:\Users\oem/.config/git/ignore`.

## Main Work Completed

### Graphify Spec/Code Variant Work

Built and inspected Graphify graph variants:

- `spec-only`
- `code-only`
- `spec-code`

Generated/updated browser HTML views:

- `dbs/graphify-out/html-views/spec-only.html`
- `dbs/graphify-out/html-views/code-only.html`
- `dbs/graphify-out/html-views/spec-code.html`
- `dbs/graphify-out/html-views/index.html`

Added a bridge-only view that keeps only spec-code relationships:

- `dbs/graphify-out/html-views/spec-code-bridge-only.html`
- `dbs/graphify-out/html-views/spec-code-bridge-only.json`
- `dbs/graphify-out/html-views/spec-code-bridge-only.md`
- `dbs/graphify-out/html-views/spec-code-bridge-only-overview.svg`

Bridge-only relation counts:

| Relation | Count |
|---|---:|
| `spec_path_matches_code_path` | 9,983 |
| `spec_component_matches_code` | 2,615 |

Total bridge links: `12,598`.

### Tree-Sitter / Code-Only Recheck

Confirmed the current code-side Graphify extraction path is tree-sitter based:

- `tree_sitter` import: OK
- `tree_sitter_verilog` import: OK
- ontology seed metadata: `tree-sitter = 1433 / 1433`

Re-evaluated `code-only` and `spec-code` with different ranking modes:

- Output folder: `out/code_spec_graphify_rerun_tree_sitter_20260520`
- Main HTML report: `out/code_spec_graphify_rerun_tree_sitter_20260520/code_spec_graphify_rerun_report.html`
- Script: `platform/eval/rerun_code_spec_graphify_eval.py`

Important result:

| Variant | Ranking | Spec hit@5 | Code hit@5 | Joint hit@5 | Joint hit@10 |
|---|---|---:|---:|---:|---:|
| code-only | current propagation | 0.0000 | 0.1267 | 0.0000 | 0.0000 |
| code-only | base lexical | 0.0000 | 0.5533 | 0.0000 | 0.0000 |
| spec-code | current propagation | 0.8933 | 0.3000 | 0.2533 | 0.3867 |

Finding:

- `code-only` low score was not caused by missing gold code nodes.
- Gold code paths missing from `code-only`: `0`
- Exact gold code nodes missing from `code-only`: `0`
- Main issue was unrestricted graph propagation over high-degree code hubs.

### Intermediate Hardware Description Layer

Generated a middle-layer Hardware Description document set from Graphify spec-code bridge data.

Purpose:

- Help code-only retrieval infer likely spec anchors.
- Provide a human-readable bridge between code evidence and spec/testplan/theory anchors.
- Serve as a lower-token, structured input for later OpenKB/LLM refinement.

Generated folder:

- `dbs/graphify-out/hardware-descriptions/`

Important files:

- `dbs/graphify-out/hardware-descriptions/index.html`
- `dbs/graphify-out/hardware-descriptions/index.md`
- `dbs/graphify-out/hardware-descriptions/hardware-description-bridge.html`
- `dbs/graphify-out/hardware-descriptions/hardware_descriptions.json`
- `dbs/graphify-out/hardware-descriptions/blocks/*.md`

Generation script:

- `platform/scripts/build_hardware_descriptions_from_graphify.py`

Generated data:

- Component documents: `129`
- Bridge edges represented: `12,598`
- Code references: `4,517`
- Spec references: `4,280`

Example component documents:

- `dbs/graphify-out/hardware-descriptions/blocks/rstmgr.md`
- `dbs/graphify-out/hardware-descriptions/blocks/otp_ctrl.md`
- `dbs/graphify-out/hardware-descriptions/blocks/pinmux.md`

Each component document includes:

- `ip_block`
- `approved_label`
- `doc_anchor`
- `module_name_prefix`
- spec anchors
- RTL/DV/SVA/testbench code evidence
- direct spec-code bridge table
- retrieval guidance

### Hardware Description Retrieval Evaluation

Evaluated whether adding the generated Hardware Description layer improves spec-code retrieval.

Output folder:

- `out/hardware_description_retrieval_eval_20260520`

Important files:

- `out/hardware_description_retrieval_eval_20260520/hardware_description_retrieval_report.html`
- `out/hardware_description_retrieval_eval_20260520/hardware_description_retrieval_report.md`
- `out/hardware_description_retrieval_eval_20260520/hardware_description_retrieval_report.json`
- `out/hardware_description_retrieval_eval_20260520/hardware_description_retrieval_predictions.json`

Evaluation script:

- `platform/eval/evaluate_hardware_description_retrieval.py`

Key result:

| Method | Spec hit@5 | Code hit@5 | Joint hit@5 | Joint hit@10 |
|---|---:|---:|---:|---:|
| code-only current | 0.0000 | 0.1267 | 0.0000 | 0.0000 |
| code-only base | 0.0000 | 0.5533 | 0.0000 | 0.0000 |
| spec-code current | 0.8933 | 0.3000 | 0.2533 | 0.3867 |
| hardware-description only | 0.2133 | 0.4933 | 0.0467 | 0.0600 |
| spec-code + hardware-description | 0.8733 | 0.5533 | 0.4667 | 0.5533 |

Interpretation:

- The Hardware Description layer improves joint spec-code retrieval when fused with existing spec-code graph retrieval.
- `joint hit@5` improved from `0.2533` to `0.4667`.
- `joint hit@10` improved from `0.3867` to `0.5533`.
- `code hit@5` improved from `0.3000` to `0.5533`.

Most improved query types:

| Type | spec-code joint@5 | spec-code + HD joint@5 |
|---|---:|---:|
| `bridge_disambiguation` | 0.2667 | 0.8333 |
| `code_to_spec_trace` | 0.3667 | 0.7333 |
| `spec_to_code_trace` | 0.2667 | 0.3333 |

## Current Important Paths

HTML entry points:

- `dbs/graphify-out/hardware-descriptions/index.html`
- `dbs/graphify-out/hardware-descriptions/hardware-description-bridge.html`
- `dbs/graphify-out/html-views/index.html`
- `dbs/graphify-out/html-views/spec-code-bridge-only.html`

Main generated data:

- `dbs/graphify-out/hardware-descriptions/hardware_descriptions.json`
- `dbs/graphify-out/html-views/spec-code-bridge-only.json`

Main evaluation reports:

- `out/hardware_description_retrieval_eval_20260520/hardware_description_retrieval_report.html`
- `out/code_spec_graphify_rerun_tree_sitter_20260520/code_spec_graphify_rerun_report.html`

## Open Items

- Decide which generated artifacts should be committed. The worktree contains many unrelated modified/untracked files.
- Avoid committing cache directories unless explicitly needed.
- Consider adding the Hardware Description layer to a formal retrieval pipeline rather than using it only as a post-processing fusion evaluator.
- Consider improving component inference for `unknown` and noisy generated names.
- Consider adding human-approved labels to replace `pending:*` in generated hardware description documents.
