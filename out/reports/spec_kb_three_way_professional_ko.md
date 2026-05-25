# Spec KB 3-Way Comparative Evaluation Report

작성일: 2026-05-25  
기준 시점: 2026-05-25 16:55 KST  
대상 워크스페이스: `D:\MyWork\verilog`

## 1. Executive Summary

본 보고서는 동일한 spec 문서 집합을 세 가지 방식으로 처리한 결과를 비교 평가한다.

1. `OpenKB <- raw docs`
2. `Graphify raw`
3. `OpenKB <- Graphify wiki`

핵심 결론은 다음과 같다.

- 구조형 지식 그래프의 품질은 `Graphify raw`가 가장 우수하다.
- 사람 중심 탐색성과 요약형 KB 사용성은 `OpenKB <- Graphify wiki`가 가장 우수하다.
- 가장 깊은 증거 회수와 원문 coverage는 `OpenKB <- raw docs`가 가장 우수하다.

즉, 단일 방식으로 모든 목적을 만족시키기보다 다음과 같은 계층형 운영이 가장 타당하다.

- backbone: `Graphify raw`
- browsing layer: `OpenKB <- Graphify wiki`
- deep evidence fallback: `OpenKB <- raw docs`

## 2. Evaluation Scope

### 2.1 Common Source Corpus

세 방식은 모두 동일한 원본 문서 집합을 기준으로 한다.

- source: `D:\MyWork\verilog\out\spec_documents_20260514_204108`
- total files: `985`
- 주요 구성:
  - Markdown (`.md`): `545`
  - HJSON (`.hjson`): `367`
  - reStructuredText (`.rst`): `70`

문서군은 OpenTitan 및 Ibex 관련 spec, interfaces, registers, theory_of_operation, programmers_guide, testplan 계열을 포함한다.

### 2.2 Compared Pipelines

#### A. OpenKB <- raw docs

- path: `D:\MyWork\verilog\dbs\graphify-out\openkb-full-ollama\kb`
- 의미: 원본 spec 문서를 OpenKB가 직접 ingest

#### B. Graphify raw

- path: `D:\MyWork\verilog\dbs\graphify-out\spec-only-graphify`
- 의미: 원본 spec 문서를 Graphify가 직접 구조화

#### C. OpenKB <- Graphify wiki

- path: `D:\MyWork\verilog\dbs\graphify-out\kb-variants\spec-graphify-wiki\kb`
- 의미: Graphify가 먼저 compact wiki/anchor를 만들고, 그 결과를 OpenKB가 재구성

## 3. Measured Status Snapshot

### 3.1 OpenKB <- raw docs

기준 시점 실측:

- input target: `985`
- hashes: `747`
- sources: `748`
- summaries: `747`
- concepts: `477`

해석:

- 현재도 ingest 진행 중이다.
- 전체 coverage 측면에서는 가장 넓은 결과를 생성 중이다.
- concept generation warning이 간헐적으로 존재하지만, 문서 추가 자체는 지속적으로 성공하고 있다.

### 3.2 Graphify raw

기준 시점 실측:

- nodes: `8196`
- edges: `30054`
- communities: `33`
- extraction: `100% EXTRACTED`
- inferred edges: `0`
- token cost: `0`

해석:

- 완전 결정론적 구조 추출이다.
- graph community와 component hub 해석에 매우 유리하다.
- 자연어 summary 계층은 제공하지 않지만, 구조 보존력과 재현성이 높다.

### 3.3 OpenKB <- Graphify wiki

기준 시점 실측:

- raw top-level pages: `104`
- hashes: `107`
- sources: `104`
- summaries: `104`
- concepts: `52`

해석:

- compact input 기반이라 ingest 안정성이 높다.
- Graphify anchor를 유지한 채 OpenKB summary/concept 레이어가 추가된다.
- 원문 depth는 raw ingest보다 얕지만, 탐색성과 요약성은 더 좋다.

## 4. Architectural Comparison

### 4.1 OpenKB <- raw docs

장점:

- 가장 높은 원문 coverage
- 가장 강한 section-level evidence 보존
- registers, interfaces, theory_of_operation, testplan의 상세 정보 회수에 유리

한계:

- 처리 시간이 가장 길다
- knowledge base 규모가 커져 retrieval noise 가능성이 있다
- 구조 일관성은 Graphify 계열보다 떨어질 수 있다

### 4.2 Graphify raw

장점:

- 구조 명확성이 가장 높다
- component/topic/community 단위 해석에 강하다
- deterministic pipeline이라 재현성이 높다
- token cost 없이 반복 가능하다

한계:

- 자연어 summary 레이어가 없다
- 증거를 사람이 읽기 좋은 서술형으로 재구성해주지 않는다
- 직접 질의 응답형 사용성은 별도 레이어가 필요하다

### 4.3 OpenKB <- Graphify wiki

장점:

- Graphify 구조 anchor를 유지한다
- summary, related concepts, related documents가 생긴다
- compact input이라 처리 안정성과 비용 측면에서 유리하다

한계:

- Graphify에서 이미 압축된 정보 이상의 원문 증거는 복원하지 못한다
- 일부 concept가 일반론적이거나 중복되는 경향이 있다
- deep evidence retrieval에서는 raw ingest보다 불리하다

## 5. Comparative Evaluation

| Category | OpenKB raw | Graphify raw | OpenKB <- Graphify wiki |
|---|---|---|---|
| Source coverage | Highest | High | Medium |
| Structural clarity | Medium | Highest | High |
| Natural-language summary | High | Low | High |
| Concept browsing | Highest | Low | Medium to High |
| Traceability | High | Highest | High |
| Processing cost | Highest | Lowest | Low |
| Processing speed | Slowest | Fastest | Fast |
| Retrieval noise risk | Medium to High | Low | Low to Medium |
| Deep evidence fallback | Highest | Medium | Medium |
| Community / topology analysis | Medium | Highest | High |

## 6. Expert Interpretation

### 6.1 If the goal is a spec backbone graph

`Graphify raw`가 최선이다.

이 방식은 spec corpus를 구조적으로 분해하고, component 및 community 수준에서 해석 가능하게 만든다. LLM 재작성 없이 deterministic하게 반복 가능하므로, spec knowledge graph의 기준면으로 두기에 가장 적합하다.

### 6.2 If the goal is analyst-friendly browsing

`OpenKB <- Graphify wiki`가 최선이다.

이 방식은 Graphify의 anchor를 유지하면서 OpenKB가 문서를 다시 요약하고 concept 연결을 만들어주기 때문에, 사람이 빠르게 spec landscape를 탐색하기에 가장 효율적이다.

### 6.3 If the goal is maximum evidence recall

`OpenKB <- raw docs`가 최선이다.

원문 문서를 직접 ingest하기 때문에 register, interface, testplan, operational detail 같은 상세 근거를 가장 풍부하게 남긴다. 단, 대가로 처리 시간과 노이즈 리스크가 커진다.

## 7. Recommended Operating Model

단일 저장소로 통합하기보다 역할 기반 계층 구조를 권장한다.

### Layer 1. Backbone

- `Graphify raw`
- 역할: 구조 기준면, component map, community map, deterministic graph

### Layer 2. Browsing / analyst support

- `OpenKB <- Graphify wiki`
- 역할: 빠른 summary browsing, concept navigation, low-cost exploratory retrieval

### Layer 3. Evidence fallback

- `OpenKB <- raw docs`
- 역할: 상세 spec evidence, section-level fallback, 깊은 문서 근거 회수

## 8. Final Conclusion

세 방식은 경쟁 관계라기보다 역할이 분리된 상호보완 관계에 가깝다.

최종 권고는 다음과 같다.

1. 구조형 spec KG의 기준 저장소는 `Graphify raw`
2. 실무 탐색용 KB는 `OpenKB <- Graphify wiki`
3. 깊은 근거 회수는 `OpenKB <- raw docs`

한 줄로 요약하면:

`Graphify raw가 가장 좋은 구조형 KG이고, OpenKB <- Graphify wiki가 가장 좋은 탐색형 KB이며, OpenKB raw가 가장 좋은 증거 백업층이다.`
