# Spec 문서 KG + 코드 KG 통합 평가 설계서

작성일: 2026-05-15

## 1. 목적

이 문서의 목적은 다음 세 가지를 현재 워크스페이스 기준으로 명확히 정리하는 것이다.

1. 코드 그래프는 어떤 방식이 가장 적합한가
2. spec 문서는 어떤 방식으로 KG/KB를 구축하는 것이 가장 적합한가
3. 코드 그래프와 spec 문서 그래프를 하나로 합칠지, 분리 운영할지, 또는 hybrid로 결합할지 어떻게 평가할 것인가

## 2. 현재 관찰 요약

### 2.1 코드 그래프 쪽 현재 증거

현재 워크스페이스에는 코드 retrieval 비교 결과가 이미 존재한다.

주요 근거:

- `out/reports/retrieval_methods_comparison.md`
- `docs/GRAPHIFY_KG_COMPARISON.md`
- `out/reports/hybrid_retrieval_performance_eval_ko.md`
- `out/reports/graphify_adversarial_retrieval_comparison_ko.md`

핵심 해석:

- RTL module retrieval 정확도에서는 현재 custom `KG`가 가장 안정적이다.
- `Parser+LSP`는 recall 보조 후보 생성기로 강하다.
- `Graphify`는 exact owner retrieval보다는 architecture navigation과 community-level exploration에 강하다.
- 실제 adversarial retrieval에서는 `KG` 단독보다 `Parser/LSP + KG + Graphify(module-card)` hybrid가 더 좋았다.

### 2.2 spec 문서 corpus 현재 상태

spec 문서 경로:

- `D:\MyWork\verilog\out\spec_documents_20260514_204108`

현재 corpus 실측:

| 항목 | 값 |
|---|---:|
| 전체 파일 수 | 985 |
| `doc` | 588 |
| `hjson_spec` | 367 |
| `readme` | 30 |
| `.md` | 545 |
| `.hjson` | 367 |
| `.rst` | 70 |
| Ibex 계열 | 52 |
| OpenTitan 계열 | 933 |

대표적으로 다음 블록 관련 문서가 여러 형태로 함께 존재한다.

- `clkmgr`
- `flash_ctrl`
- `pwrmgr`
- `rv_core_ibex`
- `pinmux`

이 문서들은 보통 다음 조합으로 존재한다.

- `theory_of_operation.md`
- `registers.md`
- `interfaces.md`
- `programmers_guide.md`
- `*.hjson`
- `*_testplan.hjson`

즉, 이 corpus는 단순 텍스트 문서 모음이 아니라, 자연어 문서와 구조화 spec 메타데이터가 함께 있는 혼합 corpus다.

## 3. 권장 구축 전략

### 3.1 코드 그래프

현재 기준 권장안:

- 메인 retrieval graph: `custom KG`
- 보조 navigation graph: `Graphify`
- 보조 candidate generator: `Parser+LSP`

이유:

- `custom KG`는 Verilog-specific labels, ports, reverse parent, instance edges를 직접 보유한다.
- `Graphify`는 broad code graph와 cross-module relation 탐색에 유리하지만, 현재는 exact RTL owner retrieval에는 얇다.
- `Parser+LSP`는 top-k recall 안정성이 높아 reranker/fusion 입력으로 적합하다.

### 3.2 spec 문서 그래프

현재 기준 권장안:

- 문서형 KB: `OpenKB` for `md/rst/readme`
- 구조형 spec KG: 별도 `HJSON parser KG` for `hjson_spec`

이유:

- `md/rst`는 section summary, concept linking, natural-language answer synthesis가 중요하므로 OpenKB 계열이 잘 맞는다.
- `hjson`은 register, field, interface, parameter, alert, interrupt, testplan item 같은 구조 정보가 풍부해서 단순 문서 임베딩보다 구조형 KG로 올리는 편이 훨씬 낫다.

### 3.3 통합 방식

현재 기준 권장안:

- 물리적 full merge보다 `분리 저장 + query-time hybrid`

권장 구조:

1. 코드 KG
2. Graphify code navigation graph
3. OpenKB 문서 KB
4. HJSON 구조형 spec KG
5. query router + late fusion

## 4. 왜 단일 merge를 바로 권장하지 않는가

단일 대형 graph는 보기에는 단순하지만, 현재 데이터 특성상 다음 문제가 크다.

1. 문서 노드와 파일 노드가 retrieval noise를 만들 수 있다.
2. 코드 retrieval의 목적 함수와 문서 retrieval의 목적 함수가 다르다.
3. `hjson`은 구조형 파싱이 중요한데, 단일 text-oriented merge로 처리하면 정보 손실이 생긴다.
4. `Graphify` 결과에서도 file/document-like node가 많아질수록 exact owner retrieval이 흔들리는 경향이 이미 관찰되었다.

따라서 추천 순서는 다음과 같다.

1. 먼저 분리 구축
2. 공통 anchor를 기준으로 연결
3. query-time fusion으로 성능 확인
4. 그 후에도 운영/성능 이득이 명확할 때만 physical merge 검토

## 5. 공통 anchor 설계

코드와 spec를 연결할 때는 free-form text 매칭보다 안정적인 anchor를 우선 사용한다.

우선순위 anchor:

| Anchor | 설명 |
|---|---|
| `ip/block name` | `clkmgr`, `flash_ctrl`, `pinmux`, `rv_core_ibex` 등 |
| `module name` | 실제 RTL module 이름 |
| `source path family` | `hw/ip_templates/<ip>/`, `hw/top_*/ip_autogen/<ip>/` 등 |
| `register name` | `registers.md`와 `*.hjson` 사이 정합 |
| `interface signal name` | `interfaces.md`와 RTL port 연결 |
| `testplan item` | `*_testplan.hjson`와 DV/coverage 문서 연결 |
| `approved label` | 현재 merged labels와 연결 |

추천 연결 edge 예시:

- `SPEC_DESCRIBES_MODULE`
- `SPEC_DESCRIBES_IP`
- `SPEC_DEFINES_REGISTER`
- `SPEC_DEFINES_INTERFACE`
- `SPEC_TESTPLANS_MODULE`
- `DOC_REFERS_TO_DOC`
- `DOC_SUPPORTS_LABEL`

## 6. 비교할 구축안

반드시 아래 네 가지를 같은 질문셋으로 비교한다.

### A. Code-only baseline

- 코드 KG만 사용
- spec 문서 미사용

의미:

- 현재 코드 retrieval upper baseline

### B. Spec-only baseline

- OpenKB + HJSON KG만 사용
- 코드 KG 미사용

의미:

- spec 문서만으로 code-relevant answer를 얼마나 찾는지 측정

### C. Single merged graph

- 코드 node와 spec node를 하나의 graph로 통합
- 하나의 retriever/ranker로 처리

의미:

- 운영 단순성 대 precision 손실 여부 확인

### D. Dual-graph hybrid

- 코드 KG와 spec KB/KG를 분리 저장
- query router가 질문 타입에 따라 비중을 조절
- late fusion 또는 weighted RRF 적용

의미:

- 현재 가장 유력한 실전형 구조

## 7. 평가 질문셋 설계

질문은 반드시 세 축으로 나눈다.

### 7.1 코드 중심 질문

목표:

- 올바른 RTL module anchor를 찾는 능력 평가

예시 유형:

- exact module lookup
- parent-child disambiguation
- sibling disambiguation
- wrapper/reference block retrieval
- generation anchor retrieval

주요 지표:

- hit@1
- hit@3
- hit@5
- MRR

### 7.2 spec 중심 질문

목표:

- 문서/섹션/구조 spec 자체를 찾는 능력 평가

예시 유형:

- 어떤 문서가 해당 block의 동작을 설명하는가
- 어떤 section이 register behavior를 정의하는가
- 어떤 HJSON이 해당 block의 testplan을 담는가
- 어떤 문서가 인터페이스 신호 의미를 설명하는가

gold 형태:

- 파일 path
- section heading
- register name
- hjson object key

주요 지표:

- doc hit@1
- section hit@3
- field-level exact match
- evidence coverage

### 7.3 혼합 질문

목표:

- spec와 code를 넘나드는 실제 설계 업무형 질문 평가

예시 유형:

- 이 spec 요구를 만족하는 RTL anchor module은 무엇인가
- 이 RTL block의 근거 spec section은 어디인가
- 이 register 정의가 구현된 RTL block은 무엇인가
- 이 testplan item이 검증하는 설계 블록은 무엇인가

gold 형태:

- `module + spec file`
- `module + section`
- `module + register group`

주요 지표:

- paired hit@1
- one-side correct / both-side correct
- path evidence score

## 8. query router 권장 규칙

dual-graph hybrid를 쓸 경우 질문을 최소 세 가지로 분류한다.

### 8.1 code-first

질문 신호:

- module
- wrapper
- parent
- child
- hierarchy
- ports
- instance
- replacement RTL

기본 비중:

- 코드 KG 0.60
- Parser/LSP 0.20
- Graphify 0.10
- spec KB/KG 0.10

### 8.2 spec-first

질문 신호:

- section
- programmer guide
- theory of operation
- register
- testplan
- interface description

기본 비중:

- OpenKB 0.45
- HJSON KG 0.35
- 코드 KG 0.15
- Graphify 0.05

### 8.3 cross-domain

질문 신호:

- "근거", "according to spec", "which RTL implements", "which document explains", "reference block and spec"

기본 비중:

- 코드 KG 0.35
- OpenKB 0.25
- HJSON KG 0.25
- Graphify 0.10
- Parser/LSP 0.05

## 9. 성능 판정 기준

최종 결론은 단순 hit@1 하나로 내리지 않는다.

우선순위:

1. 혼합 질문의 both-side correctness
2. 코드 중심 질문의 hit@1
3. spec 중심 질문의 section/field hit
4. latency
5. context token size
6. 운영 복잡도

운영 판단 기준:

- `single merged graph`가 hybrid보다 hit@1과 both-side correctness가 비슷하거나 더 좋아야 merge 검토
- `dual-graph hybrid`가 혼합 질문 정확도와 유지보수성을 동시에 만족하면 분리 운영 유지
- `spec-only`가 code anchor를 잘 못 찾으면 spec 시스템은 retrieval source이지 primary anchor engine은 아님

## 10. 현재 시점의 가설

현재 증거만으로 세우는 작업 가설은 다음과 같다.

### 가설 1

코드 anchor retrieval은 여전히 `custom KG`가 중심일 것이다.

### 가설 2

spec 문서 질의는 `OpenKB + HJSON parser KG` 조합이 단일 방식보다 좋을 것이다.

### 가설 3

코드와 spec를 하나의 graph로 완전 merge한 방식은 `dual-graph hybrid`보다 exact retrieval precision이 낮을 가능성이 높다.

### 가설 4

가장 실전적인 구조는 아래일 가능성이 높다.

- 코드: `KG + Parser/LSP + Graphify`
- 문서: `OpenKB + HJSON KG`
- 통합: `query-time late fusion`

## 11. 바로 실행할 다음 단계

### 단계 1. spec 질문셋 생성

최소 60문항 권장:

- spec-only 20
- cross-domain 20
- code-from-spec generation-anchor 20

### 단계 2. HJSON parser KG 스냅샷 생성

추출 대상:

- ip/block
- register
- field
- interrupt
- alert
- interface item
- testplan item

### 단계 3. OpenKB 실측 완료

필요 조건:

- `LLM_API_KEY`
- `openkb add raw`
- 동일 질문셋에 대한 `openkb query` scoring

### 단계 4. 4-way 비교 실행

비교군:

- code-only
- spec-only
- merged-single
- dual-hybrid

### 단계 5. 통합 결론 확정

최종 산출물:

- 성능표
- 실패 유형표
- latency 비교
- token budget 비교
- 운영 권장안

## 12. 최종 권고

현재 기준 권고는 다음과 같다.

1. 코드 그래프는 `custom KG`를 메인으로 유지한다.
2. spec 문서는 `OpenKB`와 `HJSON 구조형 KG`를 분리 구축한다.
3. 두 그래프는 지금 당장 하나로 완전 merge하지 않는다.
4. 먼저 `dual-graph hybrid`로 평가한 뒤, merge가 hybrid보다 낫다는 증거가 있을 때만 통합을 검토한다.

한 줄로 요약하면:

`코드는 KG 중심, spec은 OpenKB+HJSON 중심, 통합은 분리 저장 후 query-time hybrid가 현재 가장 유망하다.`
