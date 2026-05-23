# Hard Verilog Generation Context Evaluation

This evaluates whether each method retrieves the RTL context needed for hard Verilog generation prompts. It is not an LLM code-generation pass rate.

Questions: 77

| Mode | hit@1 | hit@3 | hit@5 | MRR |
|---|---:|---:|---:|---:|
| `parser_lsp` | 0.9481 | 1.0000 | 1.0000 | 0.9675 |
| `manticore_parser_lsp` | 0.8312 | 0.8961 | 0.9481 | 0.8645 |
| `kg` | 0.9481 | 0.9870 | 1.0000 | 0.9658 |
| `graphify` | 0.9740 | 0.9740 | 0.9740 | 0.9740 |

## By Level

### parser_lsp
| Level | Count | hit@1 | hit@3 | MRR |
|---|---:|---:|---:|---:|
| L3 | 26 | 1.0000 | 1.0000 | 1.0000 |
| L4 | 26 | 0.8846 | 1.0000 | 0.9295 |
| L5 | 25 | 0.9600 | 1.0000 | 0.9733 |

### manticore_parser_lsp
| Level | Count | hit@1 | hit@3 | MRR |
|---|---:|---:|---:|---:|
| L3 | 26 | 1.0000 | 1.0000 | 1.0000 |
| L4 | 26 | 0.6923 | 0.8077 | 0.7654 |
| L5 | 25 | 0.8000 | 0.8800 | 0.8267 |

### kg
| Level | Count | hit@1 | hit@3 | MRR |
|---|---:|---:|---:|---:|
| L3 | 26 | 1.0000 | 1.0000 | 1.0000 |
| L4 | 26 | 0.8462 | 0.9615 | 0.8987 |
| L5 | 25 | 1.0000 | 1.0000 | 1.0000 |

### graphify
| Level | Count | hit@1 | hit@3 | MRR |
|---|---:|---:|---:|---:|
| L3 | 26 | 1.0000 | 1.0000 | 1.0000 |
| L4 | 26 | 0.9615 | 0.9615 | 0.9615 |
| L5 | 25 | 0.9600 | 0.9600 | 0.9600 |

## Interpretation

- The benchmark uses hard generation prompts that require finding the correct source RTL before code can be generated safely.
- `hit@1` is the strictest readiness metric: the first context block is the correct module.
- `hit@3` and `hit@5` measure whether a generator would likely see the right reference block inside a short context pack.
- Existing VerilogEval oracle-reference pass rates remain 100%, so they are harness checks only.
