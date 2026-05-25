# Graphify Wiki vs OpenKB(Graphify Wiki) vs OpenKB(Raw Docs)
작성일: 2026-05-25

## 1. 비교 대상

이번 비교는 spec 문서용 지식베이스를 만드는 세 가지 경로를 대상으로 한다.

1. `Graphify wiki`
2. `OpenKB <- Graphify wiki`
3. `OpenKB <- raw spec documents`

각 방식은 목적이 조금 다르다.

- `Graphify wiki`:
  Graphify가 spec graph에서 뽑은 구조화 anchor/wiki
- `OpenKB <- Graphify wiki`:
  Graphify wiki를 다시 OpenKB가 요약/개념화한 KB
- `OpenKB <- raw spec documents`:
  원본 spec 문서 전체를 OpenKB가 직접 읽어 만든 KB

## 2. 현재 실측 상태

### A. Graphify wiki

기준 경로:

- [graphify-openkb-bridge/README.md](D:/MyWork/verilog/dbs/graphify-out/graphify-openkb-bridge/README.md)
- [graphify_derived_spec_wiki.html](D:/MyWork/verilog/dbs/graphify-out/graphify-openkb-bridge/graphify_derived_spec_wiki.html)
- [spec-graphify-wiki raw](D:/MyWork/verilog/dbs/graphify-out/kb-variants/spec-graphify-wiki/kb/raw)

구성:

- 총 raw 페이지: `104`
- component: `60`
- topic: `16`
- document map: `30`
- index: `1`

참고:

- bridge README에는 `107` 페이지로 설명되어 있으나,
  현재 파일 시스템 기준 raw 최상위 입력은 `104`개 파일이다.
  별도 하위 디렉터리(`components`, `topics`, `documents`)까지 합치면 총 입력 집합은 `210`개로 보이지만,
  실제 OpenKB의 top-level ingest 기준으로는 `104`개가 핵심 입력으로 반영되었다.

### B. OpenKB <- Graphify wiki

기준 경로:

- [spec-graphify-wiki KB](D:/MyWork/verilog/dbs/graphify-out/kb-variants/spec-graphify-wiki/kb)
- [resume_graphify_wiki.log](D:/MyWork/verilog/dbs/graphify-out/kb-variants/spec-graphify-wiki/kb/resume_graphify_wiki.log)

현재 상태:

- hashes: `107`
- sources: `104`
- summaries: `104`
- concepts: `52`

진행 상태:

- 루프 종료됨
- 마지막 로그 기준 `210/210`까지 스캔 완료
- 이후 `12`회 연속 stalled round 후 종료

### C. OpenKB <- raw spec documents

기준 경로:

- [openkb-full-ollama KB](D:/MyWork/verilog/dbs/graphify-out/openkb-full-ollama/kb)
- [resume_raw_full.log](D:/MyWork/verilog/dbs/graphify-out/openkb-full-ollama/kb/resume_raw_full.log)

현재 상태:

- hashes: `674`
- sources: `675`
- summaries: `674`
- concepts: `427`

진행 상태:

- 전체 목표: `985`
- 현재도 계속 진행 중
- 최근 로그 기준 `0674_chip_rstmgr_testplan...`까지 완료, `0675_chip_rv_core_ibex_testplan...` 처리 중

## 3. 구조적 차이

### 3.1 Graphify wiki

장점:

- Graphify의 `node id`, `community`, `role`, `confidence` 같은 구조 메타가 직접 남는다.
- 원본 source/evidence를 덜 가공하므로 traceability가 좋다.
- 사람이 HTML/Markdown으로 바로 읽기 쉽다.
- 토큰 비용 없이 즉시 탐색 가능하다.

한계:

- 자연어 탐색용 요약층은 얇다.
- 문서 간 개념 통합은 제한적이다.
- anchor가 얇게 만들어진 항목은 정보량이 적다.

예:

- [raw/components/clkmgr.md](D:/MyWork/verilog/dbs/graphify-out/kb-variants/spec-graphify-wiki/kb/raw/components/clkmgr.md)

이 페이지는 `component_clkmgr`, `community 12`, `confidence 1.0` 같은 anchor 정보는 좋지만,
참조 문서/섹션이 비어 있어 실제 spec evidence는 얇다.

### 3.2 OpenKB <- Graphify wiki

장점:

- Graphify anchor를 바탕으로 `summary`, `related concepts`, `related documents`를 생성해준다.
- topic 중심 질의, 개념 탐색, summary browsing이 쉬워진다.
- compact input이라 raw 전체보다 훨씬 가볍고 안정적으로 ingest된다.

한계:

- 입력이 이미 Graphify에서 압축된 상태라 빠진 evidence를 다시 복구하지는 못한다.
- 일부 summary/concept는 일반론적이고 템플릿 느낌이 있다.
- concept 중 일부는 중복되거나 너무 넓다.

예:

- [wiki/summaries/clkmgr.md](D:/MyWork/verilog/dbs/graphify-out/kb-variants/spec-graphify-wiki/kb/wiki/summaries/clkmgr.md)
- [wiki/concepts/concept-entity-anchor.md](D:/MyWork/verilog/dbs/graphify-out/kb-variants/spec-graphify-wiki/kb/wiki/concepts/concept-entity-anchor.md)

`clkmgr` summary는 Graphify anchor를 잘 포장하지만,
원본에 없던 깊은 spec 근거를 크게 더해주지는 않는다.
반면 `concept-entity-anchor`처럼 KB 전반의 curation 개념을 묶어주는 문서는 탐색 보조로는 유용하다.

### 3.3 OpenKB <- raw spec documents

장점:

- coverage가 가장 넓다.
- register/interface/testplan/theory_of_operation 등 세부 evidence 보존력이 가장 높다.
- 실제 spec 질의, section-level 근거, deep evidence fallback에 가장 유리하다.

한계:

- 가장 느리다.
- concept generation 실패 경고가 간헐적으로 발생한다.
- 문서량이 많아서 retrieval noise가 커질 수 있다.
- 자연어 KB는 풍부하지만, 구조 일관성은 Graphify 입력보다 약할 수 있다.

실제 로그 예:

- `Concept generation failed: 'name'`
- 그래도 문서 자체는 `[OK]`로 계속 추가되고 있음

## 4. 성능 관점 비교

| 항목 | Graphify wiki | OpenKB <- Graphify wiki | OpenKB <- raw docs |
|---|---|---|---|
| 입력 규모 | 가장 작음 | 작음 | 가장 큼 |
| 구조 명확성 | 가장 좋음 | 좋음 | 보통 |
| traceability | 가장 좋음 | 좋음 | 좋음 |
| 자연어 summary | 약함 | 좋음 | 좋음 |
| concept 탐색 | 약함 | 중간~좋음 | 가장 풍부 |
| 원문 evidence 보존 | 중간 | 중간 | 가장 좋음 |
| section-level retrieval 잠재력 | 중간 | 중간 | 가장 좋음 |
| 처리 안정성 | 가장 높음 | 높음 | 중간 |
| 처리 시간 | 가장 짧음 | 짧음 | 가장 김 |
| retrieval noise 위험 | 낮음 | 낮음~중간 | 중간~높음 |

## 5. 현재 시점 결론

### 5.1 하나만 고르면

지금 시점에서 spec 저장소의 기본 본체로는 `Graphify wiki`가 가장 균형이 좋다.

이유:

- 구조가 가장 명확하다.
- evidence anchor 보존이 좋다.
- 토큰 비용 없이 바로 탐색할 수 있다.
- spec용 curated layer로 다루기 쉽다.

### 5.2 자연어 KB를 얹고 싶다면

`OpenKB <- Graphify wiki`가 가장 실용적이다.

이유:

- compact input 기반이라 ingest가 안정적이다.
- summary/concept 층이 생겨 browsing이 편하다.
- Graphify의 구조 anchor를 완전히 잃지 않는다.

즉 이 방식은 `Graphify wiki`의 대체재라기보다 보조 레이어에 가깝다.

### 5.3 최종 깊은 근거가 필요하다면

`OpenKB <- raw docs`가 최종 evidence fallback으로 가장 강하다.

이유:

- 문서 coverage가 가장 넓다.
- testplan, registers, interfaces, theory_of_operation 같은 실제 spec section을 더 많이 보존한다.
- cross-domain 질의나 deep evidence 질의에서 유리할 가능성이 높다.

하지만 비용과 시간이 가장 크고, KB 품질이 더 균질하다고 보긴 어렵다.

## 6. 권장 운영 구조

현재 가장 현실적인 권장안은 다음이다.

1. 기본 spec graph/wiki:
   `Graphify wiki`
2. 빠른 자연어 KB:
   `OpenKB <- Graphify wiki`
3. 깊은 evidence fallback:
   `OpenKB <- raw docs`

즉 계층 구조는 이렇게 보는 편이 좋다.

- fast structured layer: `Graphify wiki`
- fast natural-language layer: `OpenKB(Graphify wiki)`
- deep evidence layer: `OpenKB(raw docs)`

## 7. 한 줄 평가

한 줄로 정리하면:

`Graphify wiki는 가장 좋은 spec 구조 저장소이고, OpenKB(Graphify wiki)는 좋은 탐색 보조층이며, OpenKB(raw docs)는 가장 강한 증거 백업층이다.`
