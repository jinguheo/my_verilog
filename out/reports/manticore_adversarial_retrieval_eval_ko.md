# Manticore Adversarial Retrieval 성능 평가

## 평가 조건

- 벤치마크: `out/adversarial_retrieval_benchmark/questions_all.jsonl`
- 문항 수: 117
- 난이도: L4 59개, L5 58개
- Manticore 방식: 실제 서버 실행이 아니라, Manticore Search-style BM25F 랭킹을 로컬로 모델링
- 인덱스 대상: 1,012개 parser/LSP 추출 모듈
- 산출물: `out/adversarial_manticore_eval/`

## 종합 성능

| 방식 | hit@1 | hit@3 | hit@5 | MRR | 평균 query ms |
|---|---:|---:|---:|---:|---:|
| Parser/LSP baseline | 0.2821 | 0.5214 | 0.6923 | 0.4168 | 259.300 |
| KG | 0.3162 | 0.5897 | 0.7265 | 0.4557 | 283.133 |
| Manticore parser/LSP | 0.0513 | 0.1624 | 0.2906 | 0.1231 | 395.788 |
| Manticore hybrid | 0.0513 | 0.1624 | 0.2735 | 0.1197 | 442.067 |
| Graphify | 0.0085 | 0.0342 | 0.0427 | 0.0253 | n/a |
| Graphify + module-card rerank | 0.0427 | 0.1026 | 0.1538 | 0.0875 | n/a |

## 유형별 성능

| 방식 | label ambiguity hit@1 | shared child parent hit@1 | sibling disambiguation hit@1 |
|---|---:|---:|---:|
| Parser/LSP baseline | 0.2727 | 0.4000 | 0.1556 |
| KG | 0.2727 | 0.4400 | 0.2000 |
| Manticore parser/LSP | 0.0909 | 0.0200 | 0.0667 |
| Manticore hybrid | 0.0909 | 0.0200 | 0.0667 |
| Graphify | 0.0455 | 0.0000 | 0.0000 |
| Graphify + module-card rerank | 0.1364 | 0.0400 | 0.0000 |

## 해석

Manticore parser/LSP는 일반 키워드 검색에는 적합하지만, 이번 adversarial retrieval처럼 "공통 child를 가진 parent 찾기", "비슷한 sibling 중 정답 구분", "라벨만 비슷한 후보 제거"가 핵심인 문제에서는 약했다.

가장 큰 약점은 shared child parent 문제다. Manticore parser/LSP의 해당 유형 hit@1은 0.0200으로, KG 0.4400과 큰 차이가 난다. BM25F는 질문에 등장한 child/utility 토큰 자체를 강하게 끌어올리는 경향이 있어서, 실제 정답인 parent module보다 `prim_flop_2sync`, `prim_flop` 같은 공통 child 또는 유틸리티 모듈이 상위에 뜨는 사례가 많았다.

Manticore hybrid는 labels, summary, parents를 추가로 인덱싱했지만 성능이 거의 개선되지 않았다. 이는 단순히 KG 필드를 텍스트 필드로 추가하는 것만으로는 그래프 방향성, parent-child 의미, sibling 배제 조건을 충분히 반영하지 못한다는 뜻이다.

Graphify보다는 Manticore가 높지만, KG/Parser baseline에는 크게 못 미친다. Graphify는 파일 노드와 source path 정보가 과하게 상위 후보를 지배하는 문제가 있었고, Manticore는 반대로 토큰 빈도와 공통 RTL utility 토큰이 랭킹을 지배하는 문제가 관찰된다.

## 결론

현재 adversarial retrieval 기준 순위는 다음과 같다.

1. KG: 가장 안정적이며 parent-child 방향성과 라벨 정보를 가장 잘 활용한다.
2. Parser/LSP baseline: 구조 필드 overlap만으로도 강한 편이다.
3. Manticore parser/LSP: 검색 엔진형 BM25는 hard retrieval에서 구조적 질의를 잘 못 푼다.
4. Graphify + module-card rerank: 기존 Graphify보다 개선됐지만 아직 낮다.
5. Graphify 기본: 파일 정보 쏠림 때문에 현 조건에서는 부적합하다.

Manticore를 개선하려면 단순 BM25 인덱스보다, child anchor가 등장할 때 child module 자체를 감점하고 parent 후보를 강하게 승격하는 구조적 query rewrite가 필요하다. 또한 sibling disambiguation에는 shared tokens보다 negative constraints와 path/project/interface 차이를 별도 feature로 분리해야 한다.
