# Adversarial Retrieval 성능 평가

- 작성일: 2026-05-10
- 목적: 기존 retrieval test를 더 어렵게 만들 수 있는지 검증
- 일반 hard retrieval 세트: `out/hard_retrieval_benchmark/questions_all.jsonl`
- Adversarial retrieval 세트: `out/adversarial_retrieval_benchmark/questions_all.jsonl`
- 평가 결과:
  - 일반 hard retrieval: `out/hard_retrieval_eval/multiaxis_report.json`
  - adversarial retrieval: `out/adversarial_retrieval_eval/multiaxis_report.json`

## 1. 결론

가능하다. 단, 단순히 정답 모듈명을 숨기는 정도로는 충분히 어렵지 않다. 실제로 이름을 숨긴 일반 hard retrieval 세트에서는 Parser/LSP와 KG가 여전히 hit@1 약 0.84를 기록했다. 반면 같은 child dependency, 같은 naming family, 같은 semantic label을 공유하는 후보들끼리 일부러 헷갈리게 만든 adversarial retrieval 세트에서는 hit@1이 0.28~0.32까지 떨어졌다.

즉 앞으로 retrieval 성능을 제대로 압박하려면 “name-hidden”보다 “ambiguous-neighborhood adversarial” 방식이 맞다.

## 2. 세트별 난이도 비교

| Benchmark | Tasks | 구성 | Parser/LSP hit@1 | KG hit@1 | 해석 |
|---|---:|---|---:|---:|---|
| 기존 multi-axis retrieval | 175 | L1-L5, 직접 이름 질의 포함 | 0.8629 | 0.8686 | 쉬움. 직접 lookup 영향 큼 |
| hard retrieval blind | 175 | 정답명 제거, profile 질의 | 0.8457 | 0.8400 | 아직 쉬움. 포트/인스턴스가 너무 고유 |
| adversarial retrieval | 117 | shared child, sibling, shared label 혼동 | 0.2821 | 0.3162 | 실제 스트레스 테스트로 적합 |

## 3. Adversarial Retrieval 전체 성능

| Method | hit@1 | hit@3 | hit@5 | MRR | Weighted hit@1 |
|---|---:|---:|---:|---:|---:|
| KG | 0.3162 | 0.5897 | 0.7265 | 0.4557 | 0.3157 |
| Parser/LSP baseline | 0.2821 | 0.5214 | 0.6923 | 0.4168 | 0.2780 |

KG가 모든 핵심 지표에서 Parser/LSP를 앞섰다. 특히 hit@3는 +0.0683, hit@5는 +0.0342 높다. 다만 절대 성능은 낮아서, 이 세트가 retrieval model/reranker 개선용으로 훨씬 유용하다.

## 4. 난이도별 결과

| Level | Method | Count | hit@1 | hit@3 | MRR |
|---|---|---:|---:|---:|---:|
| L4 | KG | 59 | 0.3220 | 0.6271 | 0.4616 |
| L4 | Parser/LSP | 59 | 0.3220 | 0.5593 | 0.4517 |
| L5 | KG | 58 | 0.3103 | 0.5517 | 0.4497 |
| L5 | Parser/LSP | 58 | 0.2414 | 0.4828 | 0.3813 |

L5에서 KG의 이점이 더 분명하다. Parser/LSP는 L5 hit@1이 0.2414까지 내려가고, KG는 0.3103을 유지한다.

## 5. 유형별 결과

| Type | Method | Count | hit@1 | hit@3 | MRR |
|---|---|---:|---:|---:|---:|
| shared child parent retrieval | KG | 50 | 0.4400 | 0.7200 | 0.5840 |
| shared child parent retrieval | Parser/LSP | 50 | 0.4000 | 0.6000 | 0.5137 |
| label ambiguity | KG | 22 | 0.2727 | 0.5455 | 0.4008 |
| label ambiguity | Parser/LSP | 22 | 0.2727 | 0.5000 | 0.3970 |
| sibling disambiguation | KG | 45 | 0.2000 | 0.4667 | 0.3400 |
| sibling disambiguation | Parser/LSP | 45 | 0.1556 | 0.4444 | 0.3189 |

가장 어려운 유형은 sibling disambiguation이다. 같은 prefix/naming family에 속한 모듈들은 포트와 라벨도 비슷해서 기존 overlap scorer가 잘 흔들린다.

## 6. 생성된 산출물

| 파일 | 용도 |
|---|---|
| `platform/eval/harden_retrieval_questions.py` | 기존 multi-axis 문제를 name-hidden profile retrieval로 변환 |
| `platform/eval/build_adversarial_retrieval_benchmark.py` | ambiguous neighborhood 기반 adversarial retrieval 생성 |
| `out/hard_retrieval_benchmark/questions_all.jsonl` | 일반 hard retrieval 채점용 문제 |
| `out/hard_retrieval_benchmark/prompts_only.jsonl` | 일반 hard retrieval prompt-only |
| `out/adversarial_retrieval_benchmark/questions_all.jsonl` | adversarial retrieval 채점용 문제 |
| `out/adversarial_retrieval_benchmark/prompts_only.jsonl` | adversarial retrieval prompt-only |
| `out/adversarial_retrieval_eval/multiaxis_report.json` | Parser/LSP vs KG 평가 결과 |

## 7. 권장 사용법

앞으로 retrieval 성능 평가에는 다음 순서를 추천한다.

1. 기본 multi-axis로 regression smoke test를 돌린다.
2. hard retrieval blind로 정답명 의존성을 확인한다.
3. adversarial retrieval로 실제 개선 여부를 판단한다.

최종 KPI는 adversarial retrieval 기준으로 잡는 것이 좋다.

| KPI | 현재 KG | 목표 |
|---|---:|---:|
| hit@1 | 0.3162 | >= 0.45 |
| hit@3 | 0.5897 | >= 0.70 |
| hit@5 | 0.7265 | >= 0.82 |
| sibling disambiguation hit@1 | 0.2000 | >= 0.35 |

## 8. 개선 방향

| 문제 | 개선 방향 |
|---|---|
| sibling disambiguation 취약 | filename stem, hierarchy depth, parent/child role classifier 추가 |
| shared child에서 parent 혼동 | child fanout-aware reranking 및 parent owner boost |
| broad label noise | generic label downweight, label provenance/grounding score 추가 |
| Top-1 불안정 | Parser/LSP Top-5 + KG reranker + owner-role reranker 조합 |

## 9. 최종 판단

Retrieval test는 충분히 어렵게 만들 수 있고, 새 adversarial retrieval 세트는 그 목적에 맞게 동작한다. 기존 세트에서는 0.86 수준이던 hit@1이 0.32 수준으로 내려갔기 때문에, 앞으로 retrieval 개선을 검증할 때는 이 adversarial 세트를 기준으로 삼는 것이 좋다.
