# Verilog 생성 성능 비교 보고서

- 작성일: 2026-05-10
- 대상 저장소: `D:\MyWork\verilog`
- 원천 산출물:
  - `out/reports/four_method_generation_eval_full_detail.md`
  - `out/reports/openkb_generation_performance_comparison.md`
  - `out/generation_context_eval/four_method_generation_eval_summary.md`
  - `out/generation_eval_l1_l5/generation_eval_summary.md`
  - `graphify-out/GRAPH_REPORT.md`

## 1. Executive Summary

본 비교는 Verilog 생성 자체의 최종 품질을 직접 측정한 결과와, 생성 전에 필요한 RTL 근거 컨텍스트를 얼마나 정확히 찾아오는지를 측정한 결과를 분리해 해석한다. 현재 가장 신뢰할 수 있는 비교축은 77개 Hard Generation Context Readiness 벤치마크이며, 여기서는 Graphify가 hit@1 및 MRR 기준 최상위 성능을 보였다.

핵심 결론은 다음과 같다.

| 구분 | 결론 |
|---|---|
| 최상위 단일 후보 정확도 | Graphify: hit@1 0.9740, MRR 0.9740 |
| Top-5 안정성 | Parser + LSP 및 KG: hit@5 1.0000 |
| 난이도별 강점 | L3는 모든 방식이 100% hit@1, L4/L5에서 차이가 발생 |
| 취약 방식 | Parser + LSP + Manticore는 L4/L5에서 child dependency에 과도하게 끌리는 경향 |
| OpenKB 상태 | raw docs 3개, questions 80개 준비. indexed docs 0 및 LLM_API_KEY 미설정으로 정량 비교 제외 |
| 직접 생성 검증 | L1-L5 smoke 5문제와 canonical/oracle VerilogEval 150문제는 모두 PASS이나, 이는 생성 모델 간 품질 비교가 아니라 harness sanity check |

권장 운영안은 Graphify를 1차 anchor retrieval로 사용하고, Parser + LSP 또는 KG를 Top-5 보강/검증 채널로 병행하는 하이브리드 전략이다. 이 구성은 Graphify의 높은 1순위 정확도와 Parser/KG의 높은 recall 안정성을 동시에 활용한다.

## 2. 평가 범위와 해석 기준

### 2.1 직접 생성 검증

`run_generation_verification.py` 기반 smoke benchmark는 Verilog 후보가 tree-sitter syntax check, Icarus Verilog compile, VVP simulation을 통과하는지 검증한다.

| Benchmark | 문제 수 | PASS | Pass rate | 해석 |
|---|---:|---:|---:|---|
| L1-L5 smoke generation | 5 | 5 | 1.0000 | 기본 생성 검증 harness 정상 동작 확인 |
| VerilogEval canonical/oracle candidates | 150 | 150 | 1.0000 | simulator/testbench sanity check. 실제 생성 모델 비교 아님 |

주의할 점은 VerilogEval mode별 후보가 현재 `oracle_reference`로 구성되어 있다는 것이다. 따라서 이 150/150 PASS 결과는 생성 전략의 우열이 아니라 평가 인프라가 정상적으로 canonical RTL을 컴파일/시뮬레이션할 수 있음을 의미한다.

### 2.2 생성 컨텍스트 준비도

실질 비교는 Hard Generation Context Readiness benchmark로 수행되었다. 이 벤치마크는 난이도 높은 Verilog 생성 프롬프트에서 "생성에 가장 먼저 anchor로 삼아야 할 기존 RTL 모듈"을 검색 방식별로 얼마나 정확히 찾는지 측정한다.

사용 지표:

| 지표 | 의미 |
|---|---|
| hit@1 | 1순위 후보가 정답 모듈인지 여부 |
| hit@3 | 상위 3개 후보 안에 정답 모듈 포함 여부 |
| hit@5 | 상위 5개 후보 안에 정답 모듈 포함 여부 |
| MRR | 정답 순위의 역수 평균. 1순위 정답에 더 높은 가중치 부여 |

이 지표는 "최종 Verilog 코드의 기능 pass rate"가 아니라 "좋은 코드를 생성하기 위한 근거 RTL을 얼마나 정확히 공급하는가"를 측정한다.

## 3. 전체 성능 비교

| Rank | Method | Questions | hit@1 | hit@3 | hit@5 | MRR | 상태 |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Graphify | 77 | 0.9740 | 0.9740 | 0.9740 | 0.9740 | measured |
| 2 | Parser + LSP | 77 | 0.9481 | 1.0000 | 1.0000 | 0.9675 | measured |
| 3 | KG | 77 | 0.9481 | 0.9870 | 1.0000 | 0.9658 | measured |
| 4 | Parser + LSP + Manticore | 77 | 0.8312 | 0.8961 | 0.9481 | 0.8645 | measured |
| - | OpenKB | 80 | N/A | N/A | N/A | N/A | prepared, not measured |

Graphify는 77문제 중 75문제를 1순위로 맞추며 가장 높은 hit@1을 기록했다. Parser + LSP와 KG는 각각 73문제를 1순위로 맞췄고, Top-5 기준에서는 둘 다 100% 또는 이에 준하는 수준을 보였다. Manticore 결합 방식은 의미적으로 가까운 child module을 강하게 끌어올리는 경향 때문에 anchor module retrieval에서는 가장 낮은 성능을 보였다.

## 4. 난이도별 성능 분석

### 4.1 L3

| Method | hit@1 | hit@3 | hit@5 |
|---|---:|---:|---:|
| Parser + LSP | 26/26, 100.0% | 26/26, 100.0% | 26/26, 100.0% |
| Parser + LSP + Manticore | 26/26, 100.0% | 26/26, 100.0% | 26/26, 100.0% |
| KG | 26/26, 100.0% | 26/26, 100.0% | 26/26, 100.0% |
| Graphify | 26/26, 100.0% | 26/26, 100.0% | 26/26, 100.0% |

L3는 모든 방식이 완전한 성능을 보였다. 단일 모듈명, 명확한 interface signal, top-level role이 충분히 드러나는 경우에는 검색 방식 간 차이가 거의 없다.

### 4.2 L4

| Method | hit@1 | hit@3 | hit@5 |
|---|---:|---:|---:|
| Parser + LSP | 23/26, 88.5% | 26/26, 100.0% | 26/26, 100.0% |
| Parser + LSP + Manticore | 18/26, 69.2% | 21/26, 80.8% | 25/26, 96.2% |
| KG | 22/26, 84.6% | 25/26, 96.2% | 26/26, 100.0% |
| Graphify | 25/26, 96.2% | 25/26, 96.2% | 25/26, 96.2% |

L4에서 Graphify의 1순위 정확도가 가장 높다. 다만 Parser + LSP는 Top-3/Top-5에서 완전한 recall을 보여 후처리 reranker 또는 cross-checker로 적합하다. KG는 Parser + LSP 대비 hit@1은 약간 낮지만 Top-5 recall은 동일하게 100%다.

### 4.3 L5

| Method | hit@1 | hit@3 | hit@5 |
|---|---:|---:|---:|
| Parser + LSP | 24/25, 96.0% | 25/25, 100.0% | 25/25, 100.0% |
| Parser + LSP + Manticore | 20/25, 80.0% | 22/25, 88.0% | 22/25, 88.0% |
| KG | 25/25, 100.0% | 25/25, 100.0% | 25/25, 100.0% |
| Graphify | 24/25, 96.0% | 24/25, 96.0% | 24/25, 96.0% |

L5에서는 KG가 전 지표 100%로 가장 안정적이다. 복합 child-role decomposition, interface compatibility, hierarchy preservation이 함께 주어지는 고난이도 generation brief에서는 명시적 그래프 관계가 강점으로 작동한 것으로 해석된다.

## 5. 방식별 평가

### 5.1 Graphify

Graphify는 전체 hit@1 0.9740, MRR 0.9740으로 가장 높은 1순위 anchor 정확도를 보였다. `graphify-out/GRAPH_REPORT.md` 기준 현재 그래프는 48,414 nodes, 147,070 edges, 827 communities로 구성되어 있으며, EXTRACTED 44%, INFERRED 56%의 관계를 포함한다. 대형 Verilog corpus에서 구조적/추론 관계를 함께 활용하는 장점이 수치로 확인된다.

주요 강점:

| 항목 | 평가 |
|---|---|
| 1순위 anchor 선택 | 최상 |
| L4 난이도 대응 | 최상 |
| Top-level 및 hierarchy context | 강함 |
| 운영 적합성 | generation prompt의 첫 anchor 자동 선택에 적합 |

주요 리스크:

| 리스크 | 근거 |
|---|---|
| 일부 leaf/특수 AES 모듈에서 miss | `aes_dom_inverse_gf2p8`, `aes_dom_inverse_gf2p4`에서 비모듈/주석성 노드가 상위 후보로 등장 |
| Top-5 recall이 Parser/KG보다 낮음 | 전체 hit@5 0.9740으로 Parser + LSP/KG의 1.0000보다 낮음 |
| inferred edge 검증 필요 | 그래프 내 inferred edge 비중이 높아 domain-specific false positive 관리 필요 |

권장 용도는 "첫 번째 context anchor 선택"이다. 단, Graphify 단독 운영보다는 Parser + LSP 또는 KG로 Top-5 후보군을 교차 검증하는 것이 안전하다.

### 5.2 Parser + LSP

Parser + LSP는 전체 hit@1 0.9481, hit@5 1.0000, MRR 0.9675로 매우 안정적인 baseline이다. L4/L5에서 1순위 miss가 있더라도 Top-3 또는 Top-5 안에는 정답을 모두 포함했다.

주요 강점:

| 항목 | 평가 |
|---|---|
| Top-5 recall | 최상 |
| 구조적 신뢰성 | 높음 |
| 구현 단순성 | 높음 |
| 디버깅 가능성 | 높음 |

주요 리스크:

| 리스크 | 근거 |
|---|---|
| L4 hit@1 하락 | L4에서 88.5% |
| child module/neighbor module과 top module 경계가 흐려질 수 있음 | `flash_ctrl`, `kmac`, `uart` 계열에서 top1이 region/core/reg_top으로 이동 |

권장 용도는 "recall 보장형 후보 수집"이다. Graphify가 1순위를 제안하고 Parser + LSP가 Top-5 후보에 정답 anchor가 있는지 보강하는 조합이 유리하다.

### 5.3 KG

KG는 전체 hit@1 0.9481, hit@5 1.0000, MRR 0.9658로 Parser + LSP와 거의 동일한 수준이며, L5에서는 25/25 hit@1로 가장 강했다.

주요 강점:

| 항목 | 평가 |
|---|---|
| 고난이도 L5 | 최상 |
| 명시적 관계 기반 추론 | 강함 |
| hierarchy/child dependency 보존 | 강함 |
| Top-5 안정성 | 최상 |

주요 리스크:

| 리스크 | 근거 |
|---|---|
| L4 hit@1이 Graphify보다 낮음 | L4 84.6% |
| top-level module과 child dependency가 매우 근접한 경우 순위가 밀릴 수 있음 | `top_earlgrey`, `flash_ctrl`, `kmac`, `uart` 일부 사례 |

권장 용도는 L5급 generation planning, child-role decomposition, interface preservation 검증이다. 특히 생성 프롬프트가 "기존 모듈과 동등한 블록을 작성하라"처럼 계층 보존을 요구할 때 KG의 안정성이 좋다.

### 5.4 Parser + LSP + Manticore

Manticore 결합 방식은 전체 hit@1 0.8312, hit@5 0.9481로 네 방식 중 가장 낮다. L3에서는 완벽하지만 L4/L5에서 성능이 크게 낮아졌다.

주요 관찰:

| 항목 | 평가 |
|---|---|
| L3 | 100% |
| L4 | hit@1 69.2%, hit@5 96.2% |
| L5 | hit@1 80.0%, hit@5 88.0% |
| 실패 유형 | primary module 대신 child dependency를 1순위로 선택 |

대표 miss:

| Task | Gold | Top candidate 경향 |
|---|---|---|
| `genctx_021_pwrmgr` | `pwrmgr` | `prim_esc_receiver`, `prim_clock_timeout`, `prim_flop_2sync` |
| `genctx_023_clkmgr` | `clkmgr` | `prim_clock_div`, `prim_mubi4_sync` |
| `genctx_024_clkmgr` | `clkmgr` | `clkmgr_reg_top`, `prim_clock_div` |
| `genctx_054_clkmgr` | `clkmgr` | `clkmgr_clk_status`, `clkmgr_reg_top` |

이 결과는 Manticore 자체가 무가치하다는 뜻이 아니라, 현재 weighting이 "generation anchor retrieval" 목적에는 맞지 않다는 뜻이다. child dependency 탐색, call/dependency expansion, related module enrichment에는 유용할 수 있으나, anchor module을 1순위로 고르는 단계에는 감점 또는 reranking 규칙이 필요하다.

### 5.5 OpenKB

OpenKB는 평가 준비는 되어 있으나 공정 비교 대상은 아니다.

| 항목 | 상태 |
|---|---|
| raw documents | 3 |
| indexed documents | 0 |
| prepared questions | 80 |
| LLM_API_KEY | false |
| 평가 상태 | prepared, not measured |

OpenKB를 비교군에 포함하려면 raw docs를 compile/index하고, 동일한 77 또는 80개 질문에 대해 query output을 점수화해야 한다. 현재 상태에서 Graphify/Parser/KG와 나란히 수치를 비교하면 왜곡된 결론이 된다.

## 6. 실패 패턴과 원인 분석

### 6.1 Child module over-ranking

Manticore 결합 방식의 주된 실패는 primary RTL module 대신 child dependency를 상위에 배치하는 것이다. generation brief에는 "preserve child dependencies"가 포함되므로 검색기가 `prim_clock_div`, `prim_esc_receiver`, `clkmgr_reg_top` 같은 child/neighbor module을 강하게 매칭한다. 하지만 실제 생성 anchor는 이를 포함하는 상위 모듈이어야 한다.

개선 방향:

| 조치 | 기대 효과 |
|---|---|
| module role classifier 추가 | top/primary/child/helper 구분 |
| prompt 내 "equivalent to X", "replacement X" 신호 가중치 상향 | gold anchor 우선순위 회복 |
| child dependency hit는 보조 점수로 제한 | child over-ranking 완화 |
| 후보군에서 동일 hierarchy parent를 역추적 | child가 top1일 때 parent module로 rerank |

### 6.2 Graphify의 non-module node exposure

Graphify의 miss 중 일부는 모듈명이 아닌 설명/주석성 노드가 상위 후보로 노출된 사례다. 이는 Graphify가 코드 심볼뿐 아니라 문서/개념 노드도 함께 다루기 때문에 생기는 장점과 리스크의 양면이다.

개선 방향:

| 조치 | 기대 효과 |
|---|---|
| generation anchor retrieval 시 node type filter 적용 | 비모듈 후보 제거 |
| Verilog module node boost | RTL anchor 정확도 향상 |
| AES leaf module alias/relationship 보강 | leaf module recall 개선 |
| inferred edge confidence threshold 튜닝 | false positive 감소 |

### 6.3 Top-level vs reg_top/core 혼동

Parser + LSP 및 KG 일부 miss는 `kmac` vs `kmac_core`, `uart` vs `uart_reg_top`, `flash_ctrl` vs `flash_ctrl_region_cfg`처럼 wrapper/top module과 내부 구현 모듈이 모두 강한 lexical/structural signal을 갖는 경우에 발생했다.

개선 방향:

| 조치 | 기대 효과 |
|---|---|
| module hierarchy depth feature 추가 | wrapper/top module 우선순위 조정 |
| interface port overlap scoring | intended anchor 식별 강화 |
| filename/path role feature 반영 | `rtl/autogen`, `reg_top`, `core` 역할 구분 |
| prompt type별 reranking | wrapper generation과 core replacement를 분리 |

## 7. 운영 권장안

### 7.1 추천 기본 파이프라인

1. Graphify로 1차 anchor 후보를 선택한다.
2. Parser + LSP로 Top-5 후보군을 생성해 recall을 보강한다.
3. KG로 hierarchy/child dependency/interface 관계를 검증한다.
4. 후보가 child/helper/reg_top에 치우치면 parent/top module reranking을 수행한다.
5. 최종 생성 프롬프트에는 anchor RTL, interface, child dependency, known review risk를 함께 주입한다.

### 7.2 방식별 배치

| 사용 시나리오 | 1순위 추천 | 보조 |
|---|---|---|
| 일반 RTL replacement/generation | Graphify | Parser + LSP |
| 복잡한 L5 hierarchy 보존 | KG | Graphify |
| 빠른 구조 기반 후보 수집 | Parser + LSP | KG |
| child dependency 확장/주변 모듈 탐색 | Manticore | KG |
| 문서 기반 KB 질의 | OpenKB | Graphify, KG |

### 7.3 KPI

단기 목표:

| KPI | 현재 | 목표 |
|---|---:|---:|
| Graphify hit@1 | 0.9740 | >= 0.9800 |
| Parser + LSP hit@5 | 1.0000 | 유지 |
| KG L5 hit@1 | 1.0000 | 유지 |
| Manticore L5 hit@5 | 0.8800 | >= 0.9600 |
| OpenKB indexed docs | 0 | > 0 및 정량 평가 완료 |

중기 목표:

| KPI | 목표 |
|---|---:|
| Real generated RTL compile pass rate | 별도 생성 후보 기준으로 측정 |
| Real generated RTL simulation pass rate | VerilogEval 및 내부 L1-L5 세트에서 측정 |
| Context retrieval to functional-pass correlation | retrieval hit@k와 simulation pass 간 상관 분석 |
| Review risk reduction | interface mismatch, child dependency omission, reset/clock handling 오류율 감소 |

## 8. 결론

현재 데이터 기준으로 Verilog 생성 성능을 높이기 위한 핵심 병목은 "생성 모델" 자체보다 "정확한 RTL context anchor 선택"에 있다. Hard Generation Context Readiness 비교에서 Graphify는 가장 높은 단일 후보 정확도를 보였고, Parser + LSP 및 KG는 Top-5 recall과 L5 안정성에서 강점을 보였다.

따라서 최종 권고는 단일 방식 채택이 아니라 역할 분담형 하이브리드 구성이다.

| 역할 | 권장 방식 |
|---|---|
| Primary anchor | Graphify |
| Recall safety net | Parser + LSP |
| Hierarchy/interface 검증 | KG |
| Related child dependency 확장 | Manticore, 단 anchor reranking 이후 |
| 문서형 지식 비교 | OpenKB indexing 완료 후 재평가 |

향후 real model-generated RTL 후보를 각 retrieval 방식별로 생성하고 동일 simulator harness로 compile/simulation pass rate를 측정하면, 현재의 "context readiness" 평가를 "end-to-end Verilog generation performance" 평가로 확장할 수 있다.
