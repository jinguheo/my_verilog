# Verilog RTL Ontology Workflow

이 문서는 `D:\MyWork\verilog` 작업자가 실제로 어떤 순서로 확인하고 실행해야 하는지 설명합니다.

## 현재 남겨둔 핵심 구조

```text
D:\MyWork\verilog
├─ dbs\                  # 공용 RTL 원본 저장소
│  ├─ opentitan\
│  ├─ ibex\
│  ├─ sv-tests\
│  └─ RTLLM\
├─ platform\             # 실제 파이프라인, 스키마, 서비스, UI
├─ out\                  # 생성 산출물
├─ docs\                 # 작업자용 문서
└─ workflow.ps1          # 루트 실행 진입점
```

## 가장 먼저 실행할 명령

PowerShell을 `D:\MyWork\verilog`에서 열고 다음을 실행합니다.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step status
```

확인할 항목:

- `OpenTitan DB`, `Ibex DB`가 `True`여야 합니다.
- review demo를 이미 만든 상태라면 `Review demo data`가 `True`입니다.
- 전체 DB/Neo4j 부트스트랩을 아직 안 했다면 `Merged ontology seed`, `Merged labels`는 `False`일 수 있습니다.

## 빠른 review 화면 실행

Postgres나 Neo4j 없이 100개 RTL 파일만 뽑아서 ontology/review/search 비교 화면을 띄웁니다.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step demo
```

브라우저 주소:

```text
http://localhost:8765/platform/ui/review-console/index.html
```

생성 위치:

```text
D:\MyWork\verilog\out\review_demo_100
```

이 모드는 작업자가 ontology 품질, label 후보, 검색 차이를 빠르게 검토하는 용도입니다.

## 전체 ontology 산출물 생성

OpenTitan + Ibex 전체를 읽어 seed, label, merge, embedding 입력 파일을 만듭니다.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step seed
```

생성되는 주요 파일:

```text
D:\MyWork\verilog\out\opentitan_ontology_seed.jsonl
D:\MyWork\verilog\out\ibex_ontology_seed.jsonl
D:\MyWork\verilog\out\merged_ontology_seed.jsonl
D:\MyWork\verilog\out\opentitan_labels.jsonl
D:\MyWork\verilog\out\ibex_labels.jsonl
D:\MyWork\verilog\out\merged_labels.jsonl
D:\MyWork\verilog\out\embedding_rows.json
```

## Docker DB까지 올리는 전체 실행

Docker Desktop이 켜져 있어야 합니다.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step full
```

실행 순서:

1. `platform\runtime\volumes` 폴더 생성
2. `platform\.env` 생성
3. Postgres, Neo4j, Adminer 시작
4. Postgres schema 적재
5. OpenTitan + Ibex ontology seed/labels 생성
6. Neo4j graph 적재

접속 주소:

```text
Adminer: http://localhost:8081
Neo4j Browser: http://localhost:7474
Review Console: http://localhost:8765/platform/ui/review-console/index.html
```

## API 실행

Go가 PATH에 잡혀 있어야 합니다.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step module-api
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step vector-api
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step generator
```

현재 서비스는 scaffold 성격입니다. 작업자는 API가 켜지는지 확인한 뒤, 실제 Postgres/Neo4j repository adapter와 연결하는 단계를 별도 작업으로 잡아야 합니다.

## 작업자가 봐야 하는 핵심 판단

Review 화면에서 먼저 봐야 할 것은 label이 많아 보이는지가 아니라, label의 근거가 소스 경로/모듈명/포트/인스턴스와 맞는지입니다.

확인 순서:

1. `Overview`에서 샘플 수, module 수, label 수가 비정상적으로 작지 않은지 확인합니다.
2. `Review Queue`에서 `needs_review` 항목을 먼저 봅니다.
3. protocol label을 먼저 봅니다. 예: `protocol:uart`, `protocol:spi`, `protocol:tlul`
4. role label을 봅니다. 예: `role:controller`, `role:fifo`, `role:memory`, `role:crypto`
5. `Search Contrast`에서 parser/LSP 단순 검색과 ontology 검색의 결과 차이를 확인합니다.
6. `Ontology Graph`에서 label node에 너무 많은 모듈이 붙어 있으면 label rule이 과하게 넓은 것입니다.
7. false positive가 많은 label은 taxonomy 또는 rule을 수정하고 demo를 다시 생성합니다.

## Parser/LSP 단순 query와 Knowledge DB 검색 차이

Parser/LSP 방식은 현재 소스에서 보이는 심볼, 포트명, 파일명, 참조 관계를 빠르게 찾는 데 좋습니다.

Ontology/Knowledge DB 방식은 다음 정보를 함께 씁니다.

- module 이름
- source path
- ports
- instances
- inferred labels
- evidence
- graph relationship
- review state

예를 들어 `crypto memory` 같은 질의는 단순 심볼 검색에서는 직접 문자열이 없으면 결과가 비어 있을 수 있습니다. Ontology DB는 `role:crypto`, `role:memory` 같은 라벨과 근거 관계를 통해 후보를 보여줍니다.

## 반복 작업 루프

```text
RTL 원본 확인
→ ontology seed 생성
→ label proposal 생성
→ review queue 확인
→ false positive rule 수정
→ demo/seed 재생성
→ approved label만 graph/search/generation에 승격
```

작업자는 이 루프에서 “라벨을 많이 붙이는 것”보다 “승인 가능한 라벨만 남기는 것”을 목표로 해야 합니다.
