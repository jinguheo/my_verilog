# Spec-Code Graphify Variant Evaluation

- Questions: 150
- Benchmark: `out\spec_code_user_qa_benchmark\user_qa_questions_all.jsonl`

## Overall

| Variant | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 | joint MRR |
|---|---:|---:|---:|---:|---:|
| spec-only | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| code-only | 0.0 | 0.06 | 0.0 | 0.0 | 0.0 |
| spec-code | 0.9133 | 0.3 | 0.2733 | 0.4533 | 0.1192 |

## By Type

### spec-only

| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |
|---|---:|---:|---:|---:|
| user_change_impact | 1.0 | 0.0 | 0.0 | 0.0 |
| user_code_to_spec_why | 1.0 | 0.0 | 0.0 | 0.0 |
| user_disambiguation | 1.0 | 0.0 | 0.0 | 0.0 |
| user_review_trace | 1.0 | 0.0 | 0.0 | 0.0 |
| user_spec_to_code_explain | 1.0 | 0.0 | 0.0 | 0.0 |
| user_verification_coverage | 1.0 | 0.0 | 0.0 | 0.0 |

### code-only

| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |
|---|---:|---:|---:|---:|
| user_change_impact | 0.0 | 0.0 | 0.0 | 0.0 |
| user_code_to_spec_why | 0.0 | 0.2 | 0.0 | 0.0 |
| user_disambiguation | 0.0 | 0.0 | 0.0 | 0.0 |
| user_review_trace | 0.0 | 0.0 | 0.0 | 0.0 |
| user_spec_to_code_explain | 0.0 | 0.0 | 0.0 | 0.0 |
| user_verification_coverage | 0.0 | 0.16 | 0.0 | 0.0 |

### spec-code

| Type | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 |
|---|---:|---:|---:|---:|
| user_change_impact | 1.0 | 0.32 | 0.32 | 0.6 |
| user_code_to_spec_why | 0.8 | 0.44 | 0.32 | 0.44 |
| user_disambiguation | 0.84 | 0.32 | 0.28 | 0.4 |
| user_review_trace | 1.0 | 0.32 | 0.32 | 0.56 |
| user_spec_to_code_explain | 1.0 | 0.12 | 0.12 | 0.36 |
| user_verification_coverage | 0.84 | 0.28 | 0.28 | 0.36 |
