# Four-Method Verilog Generation Evaluation

Generated: 2026-05-09T20:49:21

## Direct Functional Harness

Existing canonical candidate harness: 150/150 PASS, pass rate 1.0000.

This is a simulator/testbench sanity check because candidates are canonical RTL, not separately generated outputs.

## Hard Generation Context Readiness

This evaluates whether each method retrieves the correct source RTL context for difficult generation prompts.

| Method | hit@1 | hit@3 | hit@5 | MRR |
|---|---:|---:|---:|---:|
| `parser_lsp` | 0.9481 | 1.0000 | 1.0000 | 0.9675 |
| `manticore_parser_lsp` | 0.8312 | 0.8961 | 0.9481 | 0.8645 |
| `kg` | 0.9481 | 0.9870 | 1.0000 | 0.9658 |
| `graphify` | 0.9740 | 0.9740 | 0.9740 | 0.9740 |

## Readout

- `graphify` is best on hit@1 for this hard context benchmark.
- `parser_lsp` and `kg` are very close and have perfect hit@5.
- `manticore_parser_lsp` underperforms on L4/L5 generation prompts, so its field weights need tuning for generation use.
- These numbers do not claim final generated Verilog correctness; they measure context readiness before generation.
