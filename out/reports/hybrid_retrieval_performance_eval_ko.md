# Hybrid Retrieval 성능 평가

## 목적

Parser/LSP, KG, Manticore, Graphify의 개별 검색 결과를 조합해 별도 hybrid retrieval 방식으로 평가했다.

Hybrid는 새 모델 학습이 아니라 기존 top-k 후보를 결합하는 rank-fusion 방식이다. 각 방법의 후보를 모듈명 기준으로 합치고, weighted reciprocal rank fusion과 약한 normalized score 보정을 적용했다.

## 평가 조건

- 벤치마크: `out/adversarial_retrieval_benchmark/questions_all.jsonl`
- 문항 수: 117
- 난이도: L4 59개, L5 58개
- Fusion: weighted RRF + light normalized score
- 산출물: `out/adversarial_hybrid_eval/`

## 단일 방법 대비 Hybrid 성능

| 방식 | hit@1 | hit@3 | hit@5 | MRR | 비고 |
|---|---:|---:|---:|---:|---|
| KG | 0.3162 | 0.5897 | 0.7265 | 0.4557 | 단일 방법 최고 |
| Parser/LSP baseline | 0.2821 | 0.5214 | 0.6923 | 0.4168 | 구조 필드 overlap |
| Manticore parser/LSP | 0.0513 | 0.1624 | 0.2906 | 0.1231 | BM25F-style |
| Graphify + module-card | 0.0427 | 0.1026 | 0.1538 | 0.0875 | Graphify 후보 rerank |
| Hybrid Parser+KG+Manticore | 0.2991 | 0.6838 | 0.7521 | 0.4745 | Top-k recall 개선 |
| Hybrid Parser+KG+Graphify | 0.3333 | 0.7009 | 0.7692 | 0.5040 | 전체 최고 |
| Hybrid KG+Manticore+Graphify | 0.2991 | 0.6410 | 0.7607 | 0.4745 | Parser 제외 시 hit@1 하락 |
| Hybrid All-4 | 0.2991 | 0.6838 | 0.7692 | 0.4798 | Manticore 추가가 hit@1에는 불리 |

## 가장 좋은 조합

현재 adversarial retrieval 기준 최고 성능은 `Hybrid Parser+KG+Graphify`다.

- hit@1: 0.3333
- hit@3: 0.7009
- hit@5: 0.7692
- MRR: 0.5040

KG 단독과 비교하면 다음과 같이 개선됐다.

| 지표 | KG | Hybrid Parser+KG+Graphify | 차이 |
|---|---:|---:|---:|
| hit@1 | 0.3162 | 0.3333 | +0.0171 |
| hit@3 | 0.5897 | 0.7009 | +0.1112 |
| hit@5 | 0.7265 | 0.7692 | +0.0427 |
| MRR | 0.4557 | 0.5040 | +0.0483 |

## 유형별 결과

| 유형 | KG hit@1 | Hybrid Parser+KG+Graphify hit@1 | 해석 |
|---|---:|---:|---|
| label ambiguity | 0.2727 | 0.1818 | Graphify/Parser 후보가 일부 KG 정답 순위를 밀어내며 hit@1은 하락 |
| shared child parent | 0.4400 | 0.4800 | parent-child 구조 문제에서 개선 |
| sibling disambiguation | 0.2000 | 0.2444 | sibling 구분에서 개선 |

## 해석

Hybrid가 KG 단독보다 전체 성능은 좋다. 특히 hit@3와 MRR이 크게 개선됐는데, 이는 KG가 놓친 후보를 Parser/LSP 또는 Graphify가 상위권에 보완해주는 경우가 있었기 때문이다.

다만 모든 축에서 무조건 좋은 것은 아니다. `label ambiguity`에서는 KG 단독 hit@1이 더 높았다. Graphify와 Parser/LSP 후보가 추가되면서 비슷한 label/path 후보가 섞여 들어와 정답을 2~3위로 밀어내는 경우가 생긴다.

Manticore를 포함한 조합은 hit@3/hit@5에는 도움이 되지만 hit@1에는 오히려 불리했다. Manticore BM25F는 공통 RTL utility 토큰을 강하게 끌어올리는 경향이 있어서, 최상위 정렬에서는 noise가 된다.

## 결론

현재 기준 최선의 hybrid는 `Parser/LSP + KG + Graphify(module-card)`다.

단일 방법으로는 KG가 가장 좋지만, 실제 retrieval 시스템으로는 KG를 중심으로 두고 Parser/LSP와 Graphify 후보를 낮은 가중치로 보강하는 hybrid가 더 좋다.

권장 구조:

1. 1차 후보 생성: Parser/LSP + KG
2. 보조 후보 확장: Graphify module-card
3. 최종 정렬: KG score를 중심으로 weighted RRF 적용
4. Manticore: 최상위 ranker보다는 recall 보강 또는 fallback 검색에 제한적으로 사용

이 방식은 KG 단독보다 hit@1, hit@3, hit@5, MRR 모두 개선했지만, label ambiguity 유형에서는 KG 단독보다 약하므로 유형별 query router를 추가하면 더 개선 가능성이 있다.
