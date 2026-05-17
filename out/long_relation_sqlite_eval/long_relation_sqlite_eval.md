# Long Relation Query: OpenTology Graph vs SQLite

This benchmark focuses on long graph relationships: recursive forward traversal, reverse impact traversal, and mixed structural traversal. It compares an in-memory OpenTology-style adjacency index with SQLite recursive CTE queries over the same edges.

## Dataset

- Nodes: 39,694
- Edges: 95,961
- Turtle parse/load: 0.847 s
- SQLite in-memory build + indexes: 0.520 s
- Query cases: 92

## By Query Mode

| Mode | Cases | Memory median | SQLite median | SQLite / Memory | Mean results | Jaccard |
|---|---:|---:|---:|---:|---:|---:|
| forward | 48 | 0.0424 ms | 74.2260 ms | 2524.33x | 63.1 | 1.000 |
| mixed_forward | 12 | 0.0378 ms | 0.1894 ms | 2.74x | 65.8 | 1.000 |
| reverse | 32 | 0.0290 ms | 103.4990 ms | 1710.67x | 46.4 | 1.000 |

## By Depth

| Depth | Cases | Memory median | SQLite median | SQLite / Memory | Mean results |
|---:|---:|---:|---:|---:|---:|
| 2 | 24 | 0.0371 ms | 42.0559 ms | 1063.53x | 48.3 |
| 3 | 24 | 0.0323 ms | 53.1527 ms | 1488.56x | 57.0 |
| 4 | 24 | 0.0332 ms | 67.3204 ms | 2095.84x | 63.2 |
| 5 | 20 | 0.0426 ms | 106.3742 ms | 2700.44x | 63.1 |

## Interpretation

- For interactive single-session retrieval, the in-memory graph index is faster for long traversals because it avoids recursive SQL execution overhead.
- SQLite becomes attractive when you want persistence, repeatable SQL reports, joins with metadata tables, filtering/sorting/aggregation, or running many ad-hoc relation queries without custom Python code.
- For very long or heavily filtered queries, SQL can be operationally cleaner even when raw latency is slower.
- A practical hybrid is best: keep Graphify/OpenTology adjacency for fast online traversal, and export edges to SQLite/DuckDB for analytics, dashboards, batch reports, and long relation audits.
