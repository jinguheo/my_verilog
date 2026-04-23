# Workflow Map

## Quick Demo Workflow

```mermaid
flowchart LR
  A["dbs/opentitan + dbs/ibex"] --> B["build_review_demo_100.py"]
  B --> C["ontology_seed_100.jsonl"]
  B --> D["review_candidates_100.jsonl"]
  B --> E["ontology_graph_100.json"]
  B --> F["search_comparison_100.json"]
  C --> G["review_console_data.json"]
  D --> G
  E --> G
  F --> G
  G --> H["Review Console"]
```

실행:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step demo
```

## Full Knowledge DB Workflow

```mermaid
flowchart TD
  A["Public RTL DB"] --> B["generate_ontology_seed.py"]
  A --> C["extract_opentitan_labels.py"]
  A --> D["extract_ibex_labels.py"]
  B --> E["merged_ontology_seed.jsonl"]
  C --> F["merged_labels.jsonl"]
  D --> F
  E --> G["embedding_rows.json"]
  E --> H["Neo4j Module nodes"]
  F --> H
  I["postgres_schema.sql"] --> J["Postgres"]
  K["postgres_ontology_extension.sql"] --> J
```

실행:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step full
```

## Search Behavior

```mermaid
flowchart LR
  Q["User query"] --> A["Parser/LSP"]
  Q --> B["Ontology DB"]
  A --> A1["symbol match"]
  A --> A2["file/port string match"]
  B --> B1["module + label"]
  B --> B2["port + instance"]
  B --> B3["evidence + graph"]
  B --> B4["review state"]
```

Parser/LSP는 빠른 코드 탐색에 좋습니다. Ontology DB는 역할, protocol, evidence, graph 관계를 함께 보므로 review와 generation guardrail에 더 적합합니다.
