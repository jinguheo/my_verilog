# Graphify Retrieval Evaluation

- Questions: 117
- Question file: `out\adversarial_retrieval_benchmark\questions_all.jsonl`
- Graph: `D:\MyWork\verilog\graphify-out\graph.json`

## Overall

| Method | hit@1 | hit@3 | hit@5 | MRR | Misses |
|---|---:|---:|---:|---:|---:|
| Graphify | 0.0085 | 0.0342 | 0.0427 | 0.0253 | 110 |

## By Level

| Level | Count | hit@1 | hit@3 | hit@5 | MRR |
|---|---:|---:|---:|---:|---:|
| L4 | 59 | 0.0169 | 0.0508 | 0.0678 | 0.0417 |
| L5 | 58 | 0.0 | 0.0172 | 0.0172 | 0.0086 |

## By Type

| Type | Count | hit@1 | hit@3 | hit@5 | MRR |
|---|---:|---:|---:|---:|---:|
| adversarial_label_ambiguity | 22 | 0.0455 | 0.1364 | 0.1818 | 0.1023 |
| adversarial_parent_from_shared_child | 50 | 0.0 | 0.0 | 0.0 | 0.0 |
| adversarial_sibling_disambiguation | 45 | 0.0 | 0.0222 | 0.0222 | 0.0158 |
