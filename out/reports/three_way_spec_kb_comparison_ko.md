# 3-Way Spec KB Comparison
작성일: 2026-05-25

## 1. 비교 대상

동일한 spec 문서군(`D:\MyWork\verilog\out\spec_documents_20260514_204108`)을 서로 다른 방식으로 처리한 세 경로를 비교한다.

1. `OpenKB <- raw docs`
2. `Graphify raw` (`spec-only-graphify`)
3. `OpenKB <- Graphify wiki`

여기서 이름은 다음처럼 대응된다.

- `OpenKB raw`:
  [openkb-full-ollama/kb](D:/MyWork/verilog/dbs/graphify-out/openkb-full-ollama/kb)
- `Graphify raw`:
  [spec-only-graphify](D:/MyWork/verilog/dbs/graphify-out/spec-only-graphify)
- `Graphify wiki -> OpenKB`:
  [spec-graphify-wiki/kb](D:/MyWork/verilog/dbs/graphify-out/kb-variants/spec-graphify-wiki/kb)

## 2. 현재 실측 상태

### A. OpenKB <- raw docs

현재 진행 중인 상태다.

- 입력 문서 수: `985`
- 최근 확인 시점 기준 hashes: `707`
- 최근 확인 시점 기준 sources: `708`
- 최근 확인 시점 기준 summaries: `707`
- 최근 확인 시점 기준 concepts: `450`

관련 로그:

- [resume_raw_full.log](D:/MyWork/verilog/dbs/graphify-out/openkb-full-ollama/kb/resume_raw_full.log)

특징:

- 가장 넓은 coverage
- 가장 깊은 evidence
- 가장 느리고 무거움
- concept generation warning이 간헐적으로 존재

### B. Graphify raw (`spec-only-graphify`)

이 경로는 raw spec 문서를 Graphify가 직접 구조화한 결과다.

기준 파일:

- [GRAPH_REPORT.md](D:/MyWork/verilog/dbs/graphify-out/spec-only-graphify/GRAPH_REPORT.md)
- [graph.json](D:/MyWork/verilog/dbs/graphify-out/spec-only-graphify/graph.json)

실측:

- `8196 nodes`
- `30054 edges`
- `33 communities`
- `100% EXTRACTED`
- `0% INFERRED`
- `Token cost: 0`

특징:

- 결정론적 구조화
- Graph community, component hub, source path 유지
- LLM 요약 없음
- retrieval보다 구조 탐색과 anchor 보존에 강함

### C. OpenKB <- Graphify wiki

이 경로는 Graphify가 먼저 wiki/anchor를 만든 뒤, 그 compact wiki를 OpenKB가 다시 KB로 변환한 결과다.

기준 경로:

- [spec-graphify-wiki/kb](D:/MyWork/verilog/dbs/graphify-out/kb-variants/spec-graphify-wiki/kb)
- [graphify-openkb-bridge/README.md](D:/MyWork/verilog/dbs/graphify-out/graphify-openkb-bridge/README.md)

실측:

- raw top-level pages: `104`
- hashes: `107`
- sources: `104`
- summaries: `104`
- concepts: `52`

특징:

- compact curated input
- Graphify anchor 유지
- OpenKB summary / concept layer 추가
- raw OpenKB보다 훨씬 가볍고 안정적

## 3. 같은 문서 기준에서의 차이

세 방식은 모두 같은 원본 spec corpus에서 출발하지만, 중간 표현과 목표가 다르다.

### 3.1 OpenKB raw

원본 문서를 직접 요약하고 개념화한다.

장점:

- 가장 높은 coverage
- section-level evidence가 가장 많이 살아남음
- registers / interfaces / theory_of_operation / testplan 같은 구체 항목에 강함

단점:

- 처리 시간이 가장 오래 걸림
- KB가 커져서 retrieval noise 가능성이 있음
- concept 품질이 균질하지 않을 수 있음

### 3.2 Graphify raw

원본 문서를 graph 구조로 바로 바꾼다.

장점:

- 구조 명확성 최고
- community / hub / edge 관점이 강함
- traceability와 deterministic reproducibility가 좋음
- LLM 비용이 없음

단점:

- 자연어 summary 층이 없음
- 사람이 질문형 탐색을 하려면 별도 query layer가 더 필요함
- raw evidence는 그래프 구조로는 좋지만 서술형 응답에는 약함

### 3.3 OpenKB <- Graphify wiki

Graphify raw를 사람/LLM 친화적인 compact wiki로 압축한 뒤 OpenKB로 다시 가공한다.

장점:

- 구조 anchor와 자연어 summary의 균형이 좋음
- compact해서 처리 안정성이 높음
- related concepts / related documents 탐색이 쉬움

단점:

- Graphify에서 한 번 압축된 정보 이상으로는 복구가 안 됨
- 원문 깊이는 raw OpenKB보다 얕음
- 일부 summary/concept는 템플릿 느낌이 남음

## 4. 성능 관점 3-way 비교

| 항목 | OpenKB raw | Graphify raw | OpenKB <- Graphify wiki |
|---|---|---|---|
| 원문 coverage | 가장 좋음 | 좋음 | 중간 |
| 구조 명확성 | 중간 | 가장 좋음 | 좋음 |
| 자연어 요약 | 좋음 | 약함 | 좋음 |
| concept 탐색 | 가장 풍부 | 약함 | 중간~좋음 |
| traceability | 좋음 | 가장 좋음 | 좋음 |
| 처리 비용 | 가장 큼 | 가장 작음 | 작음 |
| 처리 속도 | 가장 느림 | 가장 빠름 | 빠름 |
| retrieval noise 위험 | 중간~높음 | 낮음 | 낮음~중간 |
| deep evidence fallback | 가장 좋음 | 중간 | 중간 |
| 구조 기반 탐색 | 중간 | 가장 좋음 | 좋음 |

## 5. 목적별 승자

### 5.1 구조 기반 spec KG

승자: `Graphify raw`

이유:

- component / topic / community 구조가 가장 또렷함
- deterministic graph라 재현성이 좋음
- LLM 재해석 없이 raw spec 구조를 안정적으로 유지함

### 5.2 사람 친화적 spec KB 탐색

승자: `OpenKB <- Graphify wiki`

이유:

- Graphify의 구조 anchor를 유지하면서
- summary / related concepts / related docs가 붙어 사용성이 좋아짐

### 5.3 가장 깊은 근거 회수

승자: `OpenKB raw`

이유:

- 원문 전체를 직접 다루므로
- testplan, register, interface, operation detail 같은 깊은 evidence에서 가장 유리함

## 6. 최종 권고

세 방식 중 하나만 고르기보다 계층적으로 같이 쓰는 것이 가장 좋다.

### 권장 구조

1. 기본 spec graph:
   `Graphify raw`
2. 빠른 탐색 KB:
   `OpenKB <- Graphify wiki`
3. 깊은 근거 fallback:
   `OpenKB raw`

즉, 역할 분담은 이렇게 보는 편이 가장 현실적이다.

- backbone: `Graphify raw`
- browsing layer: `OpenKB(Graphify wiki)`
- evidence fallback: `OpenKB(raw docs)`

## 7. 한 줄 결론

한 줄로 정리하면:

`같은 spec 문서 기준으로 보면, Graphify raw가 가장 좋은 구조형 KG이고, OpenKB(Graphify wiki)가 가장 좋은 탐색형 KB이며, OpenKB raw가 가장 좋은 깊은 증거 저장소다.`
