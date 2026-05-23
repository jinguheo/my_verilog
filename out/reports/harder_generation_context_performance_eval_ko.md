# Harder Verilog Generation Context 성능 평가

- 작성일: 2026-05-10
- 평가 세트: `out/generation_context_eval/harder_generation_context_questions.jsonl`
- Prompt-only 세트: `out/generation_context_eval/harder_generation_context_prompts_only.jsonl`
- 문제 수: 77
- 난이도 구성: L4 26개, L5 51개
- 평가 대상: Parser/LSP baseline, KG, Manticore Parser/LSP, Manticore Hybrid

## 1. 평가 목적

기존 hard generation-context 문제는 정답 모듈명이 질문에 직접 포함되는 경우가 많아 lexical retrieval에 유리했다. 새 평가 세트는 정답 모듈명을 숨긴 blind-anchor 방식으로 구성했다.

새 문제는 다음 조건을 만족한다.

| 항목 | 내용 |
|---|---|
| 정답명 노출 | 제거 |
| 입력 단서 | role, coarse location, ports, child dependencies, semantic labels |
| 채점 목표 | generation brief의 primary owner RTL module 찾기 |
| 방해 요소 | primitive/package/reg_top/child dependency/neighbor module과 혼동 유도 |
| 난이도 | L4/L5만 유지 |

## 2. 전체 결과

| Method | hit@1 | hit@3 | hit@5 | MRR | Weighted hit@1 | Avg query ms |
|---|---:|---:|---:|---:|---:|---:|
| KG | 0.7662 | 0.9481 | 0.9740 | 0.8478 | 0.7610 | 368.347 |
| Parser/LSP baseline | 0.7532 | 0.9481 | 0.9740 | 0.8457 | 0.7497 | 483.503 |
| Manticore Parser/LSP | 0.3117 | 0.4286 | 0.4935 | 0.3721 | 0.3119 | 220.175 |
| Manticore Hybrid | 0.2208 | 0.3766 | 0.4935 | 0.3152 | 0.2176 | 223.407 |

결론적으로 KG가 가장 높은 hit@1, MRR, weighted hit@1을 기록했다. Parser/LSP baseline은 KG와 거의 같은 Top-3/Top-5 recall을 보였지만, 1순위 정확도에서는 KG가 1.3%p 앞섰다. Manticore 계열은 속도는 빠르지만 blind-anchor 조건에서 정확도가 크게 낮아졌다.

## 3. 기존 세트 대비 난이도 상승

| Method | 기존 hit@1 | 새 hit@1 | 변화 |
|---|---:|---:|---:|
| Parser/LSP baseline | 0.9481 | 0.7532 | -0.1949 |
| KG | 0.9481 | 0.7662 | -0.1819 |
| Manticore Parser/LSP | 0.8312 | 0.3117 | -0.5195 |

| Method | 기존 hit@3 | 새 hit@3 | 변화 |
|---|---:|---:|---:|
| Parser/LSP baseline | 1.0000 | 0.9481 | -0.0519 |
| KG | 0.9870 | 0.9481 | -0.0389 |
| Manticore Parser/LSP | 0.8961 | 0.4286 | -0.4675 |

| Method | 기존 MRR | 새 MRR | 변화 |
|---|---:|---:|---:|
| Parser/LSP baseline | 0.9675 | 0.8457 | -0.1218 |
| KG | 0.9658 | 0.8478 | -0.1180 |
| Manticore Parser/LSP | 0.8645 | 0.3721 | -0.4924 |

정답명 제거만으로 Parser/LSP와 KG의 hit@1이 약 18-19%p 하락했다. Manticore Parser/LSP는 약 52%p 하락해, BM25F-style full-text ranking이 정답명/직접 토큰 단서에 매우 크게 의존하고 있었음을 보여준다.

## 4. 난이도별 결과

### L4

| Method | Count | hit@1 | hit@3 | MRR |
|---|---:|---:|---:|---:|
| KG | 26 | 0.8462 | 0.9615 | 0.8987 |
| Parser/LSP baseline | 26 | 0.8077 | 0.9615 | 0.8859 |
| Manticore Parser/LSP | 26 | 0.3077 | 0.3846 | 0.3506 |
| Manticore Hybrid | 26 | 0.2692 | 0.3846 | 0.3314 |

L4에서는 KG의 구조/라벨 보강 효과가 가장 명확하다. Parser/LSP도 Top-3 recall은 동일하지만, KG가 1순위 anchor 선택에서 더 안정적이다.

### L5

| Method | Count | hit@1 | hit@3 | MRR |
|---|---:|---:|---:|---:|
| Parser/LSP baseline | 51 | 0.7255 | 0.9412 | 0.8252 |
| KG | 51 | 0.7255 | 0.9412 | 0.8219 |
| Manticore Parser/LSP | 51 | 0.3137 | 0.4510 | 0.3830 |
| Manticore Hybrid | 51 | 0.1961 | 0.3725 | 0.3069 |

L5에서는 Parser/LSP와 KG의 hit@1/hit@3가 동일하다. 다만 Parser/LSP의 MRR이 근소하게 높아, 일부 L5 사례에서는 KG 확장 신호가 child/neighbor module을 같이 끌어올려 순위를 미세하게 흔든 것으로 해석된다.

## 5. 주요 해석

### 5.1 KG가 현재 최선의 1순위 anchor selector

KG는 전체 hit@1 0.7662로 최고 성능이다. 차이는 크지 않지만, 정답명이 없는 상황에서도 labels, summaries, reverse parent context 같은 보강 신호가 owner module 판별에 기여했다.

### 5.2 Parser/LSP는 recall safety net으로 강함

Parser/LSP는 hit@5 0.9740으로 KG와 동일하다. 즉 1순위는 가끔 흔들려도 정답을 Top-5 후보군에 넣는 능력은 매우 좋다. 생성 파이프라인에서는 Parser/LSP Top-5를 후보 풀로 유지하고, KG/reranker로 owner module을 고르는 구성이 적합하다.

### 5.3 Manticore-style full-text ranking은 blind-anchor에 취약

Manticore Parser/LSP는 hit@1 0.3117, hit@5 0.4935로 급락했다. 정답명이 제거되면 ports/instances/labels가 비슷한 sibling, child, package, helper module이 높은 BM25 점수를 받기 쉽다.

Manticore Hybrid가 Parser/LSP-only보다 더 낮은 이유는 KG fields를 추가하면서 generic label 또는 broad context가 noise로 작동했기 때문으로 보인다. 이 방식은 anchor retrieval보다 broad full-text exploration에 더 적합하다.

## 6. 운영 권장안

| 목적 | 권장 방식 |
|---|---|
| 단일 1순위 anchor 선택 | KG |
| 후보군 recall 보장 | Parser/LSP Top-5 |
| 빠른 broad search | Manticore Parser/LSP |
| 최종 generation context assembly | KG 1순위 + Parser/LSP Top-5 교차검증 |

권장 파이프라인:

1. Parser/LSP로 Top-5 후보군을 만든다.
2. KG로 owner module을 rerank한다.
3. Top-1이 child/helper/reg_top/pkg이면 parent owner를 재탐색한다.
4. generation prompt에는 owner module, critical ports, selected child dependencies, negative-neighbor 목록을 함께 주입한다.

## 7. 현재 한계

| 항목 | 상태 |
|---|---|
| Graphify blind-anchor 재평가 | 아직 미측정 |
| OpenKB | indexed docs 0, LLM_API_KEY 미설정으로 제외 |
| 실제 generated RTL pass rate | 이번 평가는 context anchor retrieval이며 최종 RTL 생성 품질 평가는 아님 |

Graphify는 기존 쉬운 hard-context 세트에서는 hit@1 0.9740으로 최고였지만, 새 blind-anchor 세트에서는 아직 동일 조건으로 재측정하지 않았다. 기존 Graphify comparison runner가 고정된 질문 세트를 대상으로 작성되어 있어 별도 adapter가 필요하다.

## 8. 결론

새 문제 세트는 기존보다 훨씬 어렵다. 정답 모듈명을 숨기자 Parser/LSP와 KG의 hit@1은 약 0.95에서 약 0.76으로 내려갔고, Manticore Parser/LSP는 약 0.83에서 약 0.31까지 하락했다.

현재 blind-anchor 기준 최선은 KG이며, Parser/LSP는 recall 보강 채널로 매우 유용하다. Manticore는 속도와 broad search에는 장점이 있지만, primary generation anchor를 고르는 평가에서는 reranking 없이 단독 사용하기 어렵다.
