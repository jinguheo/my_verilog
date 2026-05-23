# Code-Only Low Score Diagnostic

## Summary

The low `code-only` result is not caused by missing code graph nodes or a failed tree-sitter extraction.

- Questions: 150
- Gold code nodes: 150
- Gold code paths missing from `code-only` graph: 0
- Exact gold code nodes missing from `code-only` graph: 0
- `tree_sitter` import: OK
- `tree_sitter_verilog` import: OK
- Current ontology seed frontend count: `tree-sitter = 1433 / 1433`

The main problem is the current evaluation ranking formula for the `code-only` graph. It starts with lexical matches, then propagates score to neighboring nodes. In the code-only graph, frequently reused RTL primitives and packages act as hubs and receive too much propagated score.

## Ranking Mode Comparison

Same graph, same 150 questions, same gold code nodes:

| Code-only ranking mode | Hit@1 | Hit@3 | Hit@5 | Hit@10 | MRR | Miss@10 |
|---|---:|---:|---:|---:|---:|---:|
| Current lexical + graph propagation | 0.0000 | 0.0333 | 0.1267 | 0.2067 | 0.0614 | 119 |
| Base lexical node score only | 0.4333 | 0.4933 | 0.5533 | 0.6067 | 0.4972 | 59 |
| Degree-normalized propagation | 0.0000 | 0.1467 | 0.2200 | 0.3333 | 0.1110 | 100 |

This shows that the graph content is usable, but the current propagation step hurts `code-only` ranking.

## By Query Type, Base Lexical Only

| Type | Hit@1 | Hit@3 | Hit@5 | Hit@10 | MRR |
|---|---:|---:|---:|---:|---:|
| spec_to_code_trace | 0.2667 | 0.3000 | 0.4667 | 0.5000 | 0.3530 |
| code_to_spec_trace | 0.8000 | 0.9000 | 0.9000 | 0.9000 | 0.8562 |
| requirement_to_rtl | 0.0667 | 0.1000 | 0.1000 | 0.2000 | 0.1268 |
| bridge_disambiguation | 0.8667 | 0.9333 | 0.9333 | 0.9667 | 0.9048 |
| verification_trace | 0.1667 | 0.2333 | 0.3667 | 0.4667 | 0.2450 |

## Hub Nodes Causing Ranking Drift

Examples of nodes that receive too much propagated score:

| Label | Source file | Degree | Main relation |
|---|---|---:|---|
| `prim_mubi_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` | 196 | `imports_from` |
| `prim_flop_2sync` | `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv` | 110 | `instantiates` |
| `prim_flop` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv` | 87 | `instantiates` |
| `tlul_rsp_intg_gen` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` | 78 | `instantiates` |
| `prim_reg_we_check` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` | 68 | `instantiates` |

## Interpretation

`code-only` performs poorly in the published table because the current retrieval evaluation is tuned for a mixed spec-code bridge graph. On a code-only graph, broad structural propagation rewards shared primitives and packages instead of the exact module/file target.

The better interpretation is:

- `code-only` graph coverage is OK.
- tree-sitter extraction appears OK.
- Current `code-only` ranking is under-estimated by the evaluation method.
- For code-only evaluation, use either:
  - base lexical ranking,
  - BM25/TF-IDF over code node label + source path,
  - graph propagation only after top lexical candidates,
  - degree-normalized or relation-filtered propagation that suppresses high-degree primitive/package hubs.

## Recommendation

Keep tree-sitter as the default code graph frontend, but revise the code-only evaluator so it does not use unrestricted one-hop propagation. For the current benchmark, report both values:

- strict current Graphify propagation score: `code hit@5 = 0.1267`
- corrected code-only lexical baseline: `code hit@5 = 0.5533`
