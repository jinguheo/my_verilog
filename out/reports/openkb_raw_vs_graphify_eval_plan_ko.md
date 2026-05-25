# OpenKB Raw vs Graphify 입력 비교 실험안

작성일: 2026-05-25

## 1. 목적

OpenKB에 spec 문서를 넣는 두 가지 방식을 같은 질문셋으로 비교한다.

1. `raw 문서 -> OpenKB`
2. `Graphify 처리본 -> OpenKB`

이 비교의 목적은 다음을 확인하는 것이다.

- 원문 전체를 넣는 방식이 실제 질의 정확도에서 더 좋은가
- Graphify가 먼저 압축/정리한 입력을 넣는 방식이 더 안정적인가
- 최종적으로 spec 문서용 KB를 어떤 입력 방식으로 운영하는 것이 좋은가

## 2. 비교 대상

### A. Raw 문서 기반 OpenKB

입력 corpus:

- `D:\MyWork\verilog\out\spec_documents_20260514_204108`

준비된 KB:

- `D:\MyWork\verilog\dbs\graphify-out\kb-variants\spec-only\kb`

특징:

- 전체 spec 문서 coverage가 가장 넓다.
- `985`개 문서가 그대로 정규화되어 들어간다.
- 원문 세부 정보는 가장 잘 보존된다.
- ingestion 비용과 노이즈가 크다.

### B. Graphify 처리본 기반 OpenKB

입력 corpus:

- `D:\MyWork\verilog\dbs\graphify-out\graphify-openkb-bridge`
- `D:\MyWork\verilog\dbs\graphify-out\kb-variants\spec-graphify-wiki\kb`

핵심 산출물:

- `graphify_derived_spec_wiki.html`
- `spec-graphify-wiki/kb/raw`

특징:

- Graphify가 구조화한 component/topic/document-map 중심 입력이다.
- 총 Markdown 페이지는 `107`개다.
- token과 문서 수가 크게 줄어든다.
- 원문 세부 정보 일부가 희석될 수 있다.

## 3. 현재 상태

### 3.1 Raw 문서 기반

- prepared KB는 이미 존재한다.
- OpenKB 정식 평가용 skeleton도 별도로 존재한다.
- 일부 대량 ingest 실험은 `openkb-full-ollama`에서 수행되었고, 현재 최소 `150`개 문서까지 반영된 상태다.

관련 경로:

- `dbs/graphify-out/openkb-full-ollama/kb`
- `dbs/graphify-out/openkb-full-ollama/run.log`
- `dbs/graphify-out/openkb-full-ollama/continue.log`

### 3.2 Graphify 처리본 기반

- Graphify bridge 산출물은 이미 준비되어 있다.
- 3페이지 trial은 시도되었지만 rate limit 때문에 요약/개념 생성이 끝나지 않았다.

관련 경로:

- `dbs/graphify-out/graphify-openkb-bridge/README.md`
- `dbs/graphify-out/kb-variants/spec-graphify-wiki/kb`

## 4. 권장 실행 순서

### 4.1 먼저 Graphify 처리본 기반 OpenKB

이유:

- 입력 문서 수가 `107`개로 훨씬 작다.
- 파이프라인이 끝까지 도는지 먼저 확인하기 좋다.
- OpenKB가 구조화된 compact input에서 얼마나 안정적으로 동작하는지 빠르게 볼 수 있다.
- 실패해도 복구 비용이 낮다.

### 4.2 그 다음 Raw 문서 기반 OpenKB

이유:

- coverage 상한을 보는 실험이다.
- 원문 전체를 넣었을 때의 recall과 evidence richness를 확인할 수 있다.
- 대신 runtime과 token cost가 크고 concept generation failure가 더 많을 가능성이 높다.

## 5. 실험 질문셋

동일 질문셋으로 비교해야 한다.

### 5.1 spec-only 질의

예시:

- 어떤 문서가 `clkmgr` 동작을 가장 직접적으로 설명하는가
- `pinmux` register behavior를 설명하는 핵심 문서는 무엇인가
- `rv_core_ibex` 관련 interface 설명은 어디에 있는가

평가 기준:

- gold 문서 path hit@1
- gold section hit@3

### 5.2 cross-domain 질의

예시:

- `pwrmgr` spec 요구와 가장 직접적으로 연결되는 RTL anchor는 무엇인가
- `flash_ctrl`의 근거 spec 문서는 어디인가
- `rv_core_ibex`의 register/interface 문서와 RTL 모듈을 같이 찾아라

평가 기준:

- spec evidence correctness
- code anchor correctness
- both-side correctness

### 5.3 generation-anchor 질의

예시:

- `clkmgr`와 동등한 block을 만들려면 어떤 문서와 어떤 RTL을 먼저 봐야 하는가
- `pinmux` wrapper를 설계할 때 기준이 되는 spec section과 RTL anchor는 무엇인가

평가 기준:

- top-1 문서 선택
- top-1 RTL anchor 선택
- paired answer quality

## 6. 비교 지표

반드시 아래 항목을 같이 본다.

### 정확도

- doc hit@1
- doc hit@3
- section hit@3
- code anchor hit@1
- both-side correctness

### 효율

- 총 ingest 시간
- 평균 query 시간
- 질문당 입력 token 규모
- summary/concept 생성량

### 안정성

- ingestion 성공 문서 수
- 경고/실패 수
- 재개 가능성
- rate limit 민감도

## 7. 예상 결과 가설

### Graphify 처리본 기반 OpenKB의 장점

- 더 적은 문서 수
- 더 빠른 ingest
- 더 안정적인 curation
- 더 낮은 token cost

### Raw 문서 기반 OpenKB의 장점

- 더 높은 coverage
- 더 풍부한 evidence
- 세부 register/testplan/interface 정보 보존

### 예상되는 실제 결과

- `spec-only 질의`는 raw 입력이 더 강할 가능성이 있다.
- `cross-domain 질의`는 Graphify 처리본이 오히려 더 안정적일 수 있다.
- `generation-anchor` 계열은 Graphify 처리본이 더 compact한 anchor를 줄 가능성이 높다.

## 8. 최종 판정 기준

다음 조건이면 `Graphify -> OpenKB`를 운영 기본값으로 본다.

1. spec-only 정확도가 raw 대비 크게 떨어지지 않는다.
2. cross-domain both-side correctness가 raw와 비슷하거나 더 좋다.
3. ingest/runtime/token cost가 raw보다 의미 있게 낮다.

다음 조건이면 `raw -> OpenKB`를 주력으로 본다.

1. spec-only 정확도 차이가 크다.
2. register/interface/testplan 수준 evidence가 훨씬 풍부하다.
3. 운영 시간 증가를 감수할 가치가 있다.

다음 조건이면 두 방식을 같이 유지한다.

1. Graphify 처리본은 fast path
2. raw 문서 기반은 deep evidence fallback

## 9. 실전 권장 운영 구조

현재 기준으로 가장 현실적인 운영안은 다음과 같다.

1. 기본 질의:
   `Graphify 처리본 -> OpenKB`
2. 정밀 재검증:
   `raw 문서 -> OpenKB`
3. 코드 연결:
   `custom KG`와 query-time late fusion

즉 운영 모드는 다음과 같다.

- Fast spec KB: `spec-graphify-wiki`
- Full spec KB: `spec-only`
- Code anchor KG: `custom KG`

## 10. 실행 우선순위

### 우선순위 1

`spec-graphify-wiki` OpenKB ingest 완주

대상:

- `dbs/graphify-out/kb-variants/spec-graphify-wiki/kb`

### 우선순위 2

같은 질문셋으로 Graphify 입력 OpenKB 평가

### 우선순위 3

`spec-only` OpenKB ingest 완주

대상:

- `dbs/graphify-out/kb-variants/spec-only/kb`

### 우선순위 4

raw vs graphify OpenKB 정량 비교

## 11. 결론

현재는 아래 순서가 가장 합리적이다.

1. `Graphify 처리본 -> OpenKB`를 먼저 완주한다.
2. 그 다음 `raw 문서 -> OpenKB`를 완주한다.
3. 동일 질문셋으로 두 결과를 비교한다.
4. 최종적으로는 `fast path`와 `deep evidence path`를 분리 운영할 가능성이 가장 높다.

한 줄 요약:

`Graphify 입력 OpenKB를 먼저, raw 입력 OpenKB를 나중에 돌리고, 둘을 같은 질문셋으로 비교하는 것이 현재 가장 효율적인 실험 순서다.`
