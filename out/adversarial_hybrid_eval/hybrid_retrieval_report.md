# Hybrid Retrieval Evaluation

- Questions: 117
- Fusion: {'type': 'weighted reciprocal rank fusion plus light normalized score', 'rrf_k': 60, 'score_alpha': 0.015, 'weights': {'parser_lsp': 1.0, 'kg': 1.25, 'manticore': 0.45, 'graphify': 0.35}, 'combinations': {'hybrid_parser_kg_manticore': ['parser_lsp', 'kg', 'manticore'], 'hybrid_parser_kg_graphify': ['parser_lsp', 'kg', 'graphify'], 'hybrid_kg_manticore_graphify': ['kg', 'manticore', 'graphify'], 'hybrid_all_4': ['parser_lsp', 'kg', 'manticore', 'graphify']}}

## Overall

| Method | hit@1 | hit@3 | hit@5 | MRR | weighted hit@1 | misses |
|---|---:|---:|---:|---:|---:|---:|
| hybrid_parser_kg_manticore | 0.2991 | 0.6838 | 0.7521 | 0.4745 | 0.2968 | 29 |
| hybrid_parser_kg_graphify | 0.3333 | 0.7009 | 0.7692 | 0.5040 | 0.3311 | 27 |
| hybrid_kg_manticore_graphify | 0.2991 | 0.6410 | 0.7607 | 0.4745 | 0.2951 | 28 |
| hybrid_all_4 | 0.2991 | 0.6838 | 0.7692 | 0.4798 | 0.2968 | 27 |

## By Type

### hybrid_parser_kg_manticore

| Type | count | hit@1 | hit@3 | hit@5 | MRR |
|---|---:|---:|---:|---:|---:|
| adversarial_label_ambiguity | 22 | 0.1818 | 0.6818 | 0.7273 | 0.4129 |
| adversarial_parent_from_shared_child | 50 | 0.4600 | 0.7400 | 0.8200 | 0.5947 |
| adversarial_sibling_disambiguation | 45 | 0.1778 | 0.6222 | 0.6889 | 0.3711 |

### hybrid_parser_kg_graphify

| Type | count | hit@1 | hit@3 | hit@5 | MRR |
|---|---:|---:|---:|---:|---:|
| adversarial_label_ambiguity | 22 | 0.1818 | 0.7727 | 0.8182 | 0.4508 |
| adversarial_parent_from_shared_child | 50 | 0.4800 | 0.7600 | 0.8200 | 0.6140 |
| adversarial_sibling_disambiguation | 45 | 0.2444 | 0.6000 | 0.6889 | 0.4078 |

### hybrid_kg_manticore_graphify

| Type | count | hit@1 | hit@3 | hit@5 | MRR |
|---|---:|---:|---:|---:|---:|
| adversarial_label_ambiguity | 22 | 0.1818 | 0.7727 | 0.8182 | 0.4356 |
| adversarial_parent_from_shared_child | 50 | 0.4600 | 0.7400 | 0.8200 | 0.5957 |
| adversarial_sibling_disambiguation | 45 | 0.1778 | 0.4667 | 0.6667 | 0.3589 |

### hybrid_all_4

| Type | count | hit@1 | hit@3 | hit@5 | MRR |
|---|---:|---:|---:|---:|---:|
| adversarial_label_ambiguity | 22 | 0.1818 | 0.7273 | 0.8182 | 0.4394 |
| adversarial_parent_from_shared_child | 50 | 0.4600 | 0.7400 | 0.8200 | 0.5980 |
| adversarial_sibling_disambiguation | 45 | 0.1778 | 0.6000 | 0.6889 | 0.3681 |
