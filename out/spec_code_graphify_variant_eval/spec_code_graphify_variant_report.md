# Spec-Code Graphify Variant Evaluation

- Questions: 150
- Benchmark: `D:\MyWork\verilog\out\spec_code_retrieval_benchmark\questions_all.jsonl`

## Overall

| Variant | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 | joint MRR |
|---|---:|---:|---:|---:|---:|
| spec-only | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| code-only | 0.0 | 0.1267 | 0.0 | 0.0 | 0.0 |
| spec-code | 0.8933 | 0.3 | 0.2533 | 0.3867 | 0.1132 |

## By Type

### spec-only

| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |
|---|---:|---:|---:|---:|
| bridge_disambiguation | 1.0 | 0.0 | 0.0 | 0.0 |
| code_to_spec_trace | 1.0 | 0.0 | 0.0 | 0.0 |
| requirement_to_rtl | 1.0 | 0.0 | 0.0 | 0.0 |
| spec_to_code_trace | 1.0 | 0.0 | 0.0 | 0.0 |
| verification_trace | 1.0 | 0.0 | 0.0 | 0.0 |

### code-only

| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |
|---|---:|---:|---:|---:|
| bridge_disambiguation | 0.0 | 0.2 | 0.0 | 0.0 |
| code_to_spec_trace | 0.0 | 0.1667 | 0.0 | 0.0 |
| requirement_to_rtl | 0.0 | 0.0333 | 0.0 | 0.0 |
| spec_to_code_trace | 0.0 | 0.2 | 0.0 | 0.0 |
| verification_trace | 0.0 | 0.0333 | 0.0 | 0.0 |

### spec-code

| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |
|---|---:|---:|---:|---:|
| bridge_disambiguation | 0.8333 | 0.3333 | 0.2667 | 0.4 |
| code_to_spec_trace | 0.8333 | 0.4667 | 0.3667 | 0.4667 |
| requirement_to_rtl | 1.0 | 0.1667 | 0.1667 | 0.3333 |
| spec_to_code_trace | 0.8 | 0.3333 | 0.2667 | 0.4 |
| verification_trace | 1.0 | 0.2 | 0.2 | 0.3333 |
