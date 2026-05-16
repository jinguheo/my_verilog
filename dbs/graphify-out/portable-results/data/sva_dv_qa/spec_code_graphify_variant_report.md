# Spec-Code Graphify Variant Evaluation

- Questions: 47
- Benchmark: `out\spec_code_sva_dv_user_qa_benchmark\sva_dv_user_qa_questions_all.jsonl`

## Overall

| Variant | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 | joint MRR |
|---|---:|---:|---:|---:|---:|
| spec-only | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| code-only | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| spec-code | 1.0 | 0.1915 | 0.1915 | 0.2553 | 0.1131 |

## By Type

### spec-only

| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |
|---|---:|---:|---:|---:|
| user_verification_dv_testbench | 1.0 | 0.0 | 0.0 | 0.0 |
| user_verification_sva | 1.0 | 0.0 | 0.0 | 0.0 |

### code-only

| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |
|---|---:|---:|---:|---:|
| user_verification_dv_testbench | 0.0 | 0.0 | 0.0 | 0.0 |
| user_verification_sva | 0.0 | 0.0 | 0.0 | 0.0 |

### spec-code

| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |
|---|---:|---:|---:|---:|
| user_verification_dv_testbench | 1.0 | 0.3103 | 0.3103 | 0.4138 |
| user_verification_sva | 1.0 | 0.0 | 0.0 | 0.0 |
