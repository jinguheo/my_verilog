# Operator Checklist

## 1. 시작 전 확인

```powershell
cd D:\MyWork\verilog
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step status
```

확인:

- `dbs\opentitan` 존재
- `dbs\ibex` 존재
- Python 실행 가능
- Docker 전체 실행을 할 경우 Docker Desktop 실행 중

## 2. 빠른 검토 모드

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step demo
```

화면에서 확인:

- `Overview`: module/label/edge 수
- `Review Queue`: confidence 낮은 label
- `Search Contrast`: ontology 검색이 단순 query보다 어떤 후보를 더 찾는지
- `Ontology Graph`: 과하게 큰 label cluster

## 3. 전체 seed 생성 모드

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step seed
```

성공 기준:

- `merged_ontology_seed.jsonl` 생성
- `merged_labels.jsonl` 생성
- `embedding_rows.json` 생성
- PowerShell 출력에 Python error가 없어야 함

## 4. DB 적재 모드

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step stack
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step schema
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step neo4j
```

성공 기준:

- `docker ps`에서 `verilog-postgres`, `verilog-neo4j`, `verilog-adminer` 확인
- Neo4j Browser에서 `Module`, `Label`, `IPBlock` node 확인

## 5. Review 판정 기준

Approve:

- label이 module name, path, port, instance, doc evidence 중 하나 이상과 맞음
- 같은 label이 여러 프로젝트에서 같은 의미로 쓰임
- 검색 결과 개선에 실제로 도움이 됨

Reject:

- 단순 문자열 우연 매칭
- 너무 넓은 label이라 거의 모든 모듈에 붙음
- protocol/role 의미가 불분명함
- generation에 쓰면 잘못된 RTL 구조를 유도할 가능성이 큼

More evidence:

- 이름만으로는 맞아 보이나 포트/instance 근거가 약함
- OpenTitan과 Ibex에서 같은 label 의미가 다르게 쓰이는 것 같음
- approved label로 승격하기 전에 사람이 한 번 더 봐야 함

## 6. 자주 보는 파일

```text
platform\ingest\build_review_demo_100.py
platform\ingest\generate_ontology_seed.py
platform\ingest\extract_opentitan_labels.py
platform\ingest\extract_ibex_labels.py
platform\ontology\taxonomy_v2.json
platform\ui\review-console\index.html
out\review_demo_100\review_console_data.json
```

## 7. 문제가 생겼을 때

Port 8765가 이미 사용 중이면:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step demo -Port 8766
```

전체 seed를 다시 만들고 싶으면:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step seed
```

Review demo를 다른 샘플 크기로 만들고 싶으면:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step demo -Limit 200
```

Go API 실행이 실패하면:

```powershell
go version
```

`go`가 없다는 메시지가 나오면 Go 설치 또는 PATH 설정이 먼저입니다.
