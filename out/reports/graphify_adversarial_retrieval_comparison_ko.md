# Graphify Adversarial Retrieval 성능 비교

- 작성일: 2026-05-10
- 평가 세트: `out/adversarial_retrieval_benchmark/questions_all.jsonl`
- Graphify 결과: `out/adversarial_graphify_eval/graphify_retrieval_report.json`
- Parser/LSP 및 KG 결과: `out/adversarial_retrieval_eval/multiaxis_report.json`
- Graphify adapter: `platform/eval/run_graphify_retrieval_eval.py`

## 1. 결론

Adversarial retrieval 기준으로 Graphify는 현재 Parser/LSP, KG보다 크게 낮다. 특히 shared-child parent retrieval과 sibling disambiguation에서 거의 정답을 찾지 못한다.

핵심 원인은 Graphify 자체가 일반 code graph/navigation에는 강하지만, 현재 평가 adapter의 Graphify ranking은 Verilog-specific retrieval에 필요한 ports, labels, owner/child role, parent disambiguation signal을 충분히 활용하지 못하기 때문이다.

추가 분석 결과, 사용자의 지적처럼 파일 정보 쏠림도 주요 원인이다. Graphify 전체 graph에서 파일성 노드는 약 12% 수준인데, adversarial retrieval의 Graphify Top-5 후보에서는 `.sv` 파일 노드 기반 후보가 77.6%까지 올라갔다. 즉 현재 Graphify ranking은 module owner보다 file/source path text에 과하게 끌린다.

## 2. 전체 성능 비교

| Method | Questions | hit@1 | hit@3 | hit@5 | MRR | Misses |
|---|---:|---:|---:|---:|---:|---:|
| KG | 117 | 0.3162 | 0.5897 | 0.7265 | 0.4557 | 32 |
| Parser/LSP baseline | 117 | 0.2821 | 0.5214 | 0.6923 | 0.4168 | 36 |
| Graphify + module-card rerank | 117 | 0.0427 | 0.1026 | 0.1538 | 0.0875 | 94 |
| Graphify | 117 | 0.0085 | 0.0342 | 0.0427 | 0.0253 | 110 |

Graphify는 117문제 중 hit@1이 1문제 수준이고, hit@5도 5문제 수준이다. 파일/path 점수 대신 module card의 ports, instances, labels로 재랭킹하면 hit@5가 0.0427에서 0.1538로 약 3.6배 개선된다. 그래도 KG는 117문제 중 Top-5에 85개를 포함해 격차가 크다.

## 3. 난이도별 결과

| Level | Method | Count | hit@1 | hit@3 | hit@5 | MRR |
|---|---|---:|---:|---:|---:|---:|
| L4 | KG | 59 | 0.3220 | 0.6271 | 0.7288 | 0.4616 |
| L4 | Parser/LSP | 59 | 0.3220 | 0.5593 | 0.6949 | 0.4517 |
| L4 | Graphify + module-card rerank | 59 | 0.0508 | 0.1186 | 0.1695 | 0.1013 |
| L4 | Graphify | 59 | 0.0169 | 0.0508 | 0.0678 | 0.0417 |
| L5 | KG | 58 | 0.3103 | 0.5517 | 0.7241 | 0.4497 |
| L5 | Parser/LSP | 58 | 0.2414 | 0.4828 | 0.6897 | 0.3813 |
| L5 | Graphify + module-card rerank | 58 | 0.0345 | 0.0862 | 0.1379 | 0.0735 |
| L5 | Graphify | 58 | 0.0000 | 0.0172 | 0.0172 | 0.0086 |

L5에서는 Graphify hit@1이 0이다. 정답명 없이 shared child, sibling, broad label만 주어지는 경우 Graphify의 현재 node text scoring이 primary owner module로 연결하지 못한다.

## 4. 유형별 결과

| Type | Method | Count | hit@1 | hit@3 | hit@5 | MRR |
|---|---|---:|---:|---:|---:|---:|
| shared child parent retrieval | KG | 50 | 0.4400 | 0.7200 | n/a | 0.5840 |
| shared child parent retrieval | Parser/LSP | 50 | 0.4000 | 0.6000 | n/a | 0.5137 |
| shared child parent retrieval | Graphify | 50 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| sibling disambiguation | KG | 45 | 0.2000 | 0.4667 | n/a | 0.3400 |
| sibling disambiguation | Parser/LSP | 45 | 0.1556 | 0.4444 | n/a | 0.3189 |
| sibling disambiguation | Graphify | 45 | 0.0000 | 0.0222 | 0.0222 | 0.0158 |
| label ambiguity | KG | 22 | 0.2727 | 0.5455 | n/a | 0.4008 |
| label ambiguity | Parser/LSP | 22 | 0.2727 | 0.5000 | n/a | 0.3970 |
| label ambiguity | Graphify | 22 | 0.0455 | 0.1364 | 0.1818 | 0.1023 |

Graphify가 상대적으로 가장 나은 유형은 label ambiguity지만, 여기서도 hit@1은 0.0455에 그친다. shared-child parent retrieval은 0이다.

## 5. 왜 Graphify가 낮게 나왔나

### 5.0 파일 노드 쏠림

Graphify 전체 graph와 실제 retrieval 후보의 분포가 다르다.

| 항목 | 값 |
|---|---:|
| 전체 graph nodes | 48,414 |
| 전체 file-like nodes | 5,797 |
| 전체 file-like 비율 | 0.1197 |
| adversarial Graphify Top-5 후보 수 | 585 |
| Top-5 `.sv/.v` file-node 후보 | 454 |
| Top-5 file-node 비율 | 0.7761 |

전체 graph에서는 파일 노드가 소수지만, scoring 결과에서는 파일 노드가 대부분을 차지한다. 따라서 현재 adapter는 Graphify graph를 "module retrieval graph"라기보다 "source/file text retrieval graph"처럼 사용하고 있다.

### 5.1 현재 Graphify graph가 Verilog retrieval feature를 충분히 담지 않음

Graphify 평가에 사용된 graph metadata:

| 항목 | 값 |
|---|---:|
| source files | 1534 |
| nodes | 3748 |
| edges | 5412 |
| communities | 581 |

이 그래프는 module/file/import/instantiation 중심의 일반 code graph에 가깝다. 반면 KG와 Parser/LSP retrieval은 ports, labels, instances, reverse parent context, approved labels를 scoring에 직접 사용한다.

### 5.2 Adversarial 문제는 owner disambiguation을 요구함

예를 들어 shared child 문제는 `prim_flop_2sync` 같은 재사용 child를 중심으로 질문하지만 정답은 그 child를 소유한 parent module이다. 현재 Graphify scoring은 질문 토큰과 node label/source path의 텍스트 매칭에 치우쳐, owner parent를 올리는 로직이 약하다.

### 5.3 Prompt에 정답명이 없으면 node-label matching이 약해짐

기존 generation context 세트에서는 정답 모듈명이 질문에 포함되어 Graphify가 매우 높은 hit@1을 냈다. 하지만 adversarial 세트는 정답명을 숨겼기 때문에, Graphify가 label/path text match 이점을 거의 잃었다.

## 6. 공정성 조정

Graphify 후보에서도 Parser/LSP·KG와 동일하게 다음 경로를 제외하도록 adapter를 보정했다.

- `\dv\`
- `\tb`
- `\formal\`
- `\pre_sca\`
- `\lint\`
- `\fpv\`
- `\doc\`

보정 후에도 성능은 거의 개선되지 않았다. 따라서 낮은 성능은 testbench 후보 노이즈만의 문제가 아니라 Verilog-specific owner retrieval signal 부족 문제로 보는 것이 타당하다.

## 7. 개선 방향

Graphify를 이 retrieval test에 맞추려면 다음 보강이 필요하다.

| 개선 | 기대 효과 |
|---|---|
| Verilog module node type filtering | file/testbench/package 노드 혼입 감소 |
| port/instance/label fields를 graph node attribute로 주입 | Parser/LSP 수준의 구조 단서 확보 |
| shared-child query에서 parent traversal boost | parent-from-child 문제 개선 |
| sibling family reranker | 같은 prefix 모듈 간 owner 선택 개선 |
| KG module card와 Graphify BFS context 결합 | Graphify navigation 장점 + KG retrieval 정확도 결합 |

빠른 실험으로 `Graphify + module-card rerank`를 추가했더니 hit@5가 0.0427에서 0.1538로 개선됐다. 이는 파일 정보 과다 문제가 실제 원인임을 보여준다. 하지만 sibling disambiguation은 여전히 hit@1 0.0000이라, 단순 재랭킹만으로는 부족하고 graph node에 Verilog module-level facts를 직접 넣어야 한다.

## 8. 최종 판단

Adversarial retrieval 기준 현재 순위는 다음과 같다.

1. KG
2. Parser/LSP baseline
3. Graphify

Graphify는 지금 상태로는 정확한 Verilog module retrieval engine이라기보다, 넓은 코드 그래프 탐색과 관계 맥락 제공에 더 적합하다. Adversarial retrieval의 primary owner module 선택에는 KG/Parser-LSP 기반 scorer가 훨씬 강하다.
