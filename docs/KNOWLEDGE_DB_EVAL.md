# Knowledge DB Evaluation

이 문서는 현재 구성된 RTL knowledge DB를 기준으로 질문 세트와 retrieval 평가를 만드는 방법을 설명합니다.

## 목적

두 조건을 비교합니다.

1. `kg`
   - inferred labels
   - summary
   - reverse graph hint
   - semantic query expansion

2. `baseline`
   - module name
   - file path
   - ports
   - instances
   - parser/LSP 수준의 file-local signal

즉 `baseline`은 tree-sitter AST + LSP 기반 질의의 근사치이고, `kg`는 ontology/knowledge graph를 활용하는 조건입니다.

## 생성되는 문항

자동으로 아래 세트를 만듭니다.

- easy 50
- medium 50
- hard 50

총 150문항입니다.

질문 유형 예시:

- exact module lookup
- unique port lookup
- label + port combined lookup
- parent-child retrieval
- path + interface clue
- reverse graph query
- multi-hop wrapper query
- semantic bridge query

## 실행

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step benchmark
```

## 산출물

```text
out\eval_benchmark\benchmark_easy.jsonl
out\eval_benchmark\benchmark_medium.jsonl
out\eval_benchmark\benchmark_hard.jsonl
out\eval_benchmark\benchmark_all.jsonl
out\eval_benchmark\benchmark_summary.json

out\eval_results\retrieval_report.json
out\eval_results\retrieval_report.md
out\eval_results\detailed_runs.json
out\eval_results\predictions_for_verilogeval.json
out\eval_results\verilogeval_adapter.json
```

## VerilogEval

현재 이 workspace에서는 `verilogeval` 패키지나 공식 runner를 직접 찾지 못했습니다. 그래서 두 가지를 제공합니다.

1. 공식 runner가 생겼을 때 바로 연결할 수 있는 adapter 파일
2. 지금 바로 비교 가능한 `proxy VerilogEval score`

주의:

- `proxy VerilogEval score`는 공식 VerilogEval 점수가 아닙니다.
- 로컬 retrieval quality를 100점 스케일로 정규화한 readiness score입니다.

## 해석

보통 아래처럼 해석하면 됩니다.

- easy: exact lookup이 잘 되는지
- medium: label + interface 조합 질의가 잘 되는지
- hard: reverse graph, semantic paraphrase, wrapper reasoning이 되는지

실무적으로 중요한 건 `hard` 구간에서 `kg`가 `baseline`보다 얼마나 더 잘 맞는지입니다.
