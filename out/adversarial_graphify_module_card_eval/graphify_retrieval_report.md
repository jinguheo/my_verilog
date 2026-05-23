# Graphify Retrieval Evaluation

- Questions: 117
- Question file: `out\adversarial_retrieval_benchmark\questions_all.jsonl`
- Graph: `D:\MyWork\verilog\graphify-out\graph.json`

## Overall

| Method | hit@1 | hit@3 | hit@5 | MRR | Misses |
|---|---:|---:|---:|---:|---:|
| Graphify | 0.0427 | 0.1026 | 0.1538 | 0.0875 | 94 |

## By Level

| Level | Count | hit@1 | hit@3 | hit@5 | MRR |
|---|---:|---:|---:|---:|---:|
| L4 | 59 | 0.0508 | 0.1186 | 0.1695 | 0.1013 |
| L5 | 58 | 0.0345 | 0.0862 | 0.1379 | 0.0735 |

## By Type

| Type | Count | hit@1 | hit@3 | hit@5 | MRR |
|---|---:|---:|---:|---:|---:|
| adversarial_label_ambiguity | 22 | 0.1364 | 0.2727 | 0.4091 | 0.2375 |
| adversarial_parent_from_shared_child | 50 | 0.04 | 0.12 | 0.18 | 0.0981 |
| adversarial_sibling_disambiguation | 45 | 0.0 | 0.0 | 0.0 | 0.0025 |
