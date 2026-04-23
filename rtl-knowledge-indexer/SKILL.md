---
name: rtl-knowledge-indexer
description: index normalized rtl intermediate representations into relational, graph, and vector stores for module lookup, connectivity analysis, version tracking, and semantic retrieval. use when chatgpt needs to load or update postgres, neo4j, or pgvector style stores from parsed rtl artifacts.
---

# Overview
Load normalized rtl IR into queryable knowledge stores.

## Use this skill to
- persist modules, ports, parameters, instances, and versions into a relational schema
- build connectivity and hierarchy graphs
- generate vector-search records for summaries and semantic retrieval
- maintain idempotent upserts and version lineage

## Inputs
Expect parsed IR plus indexing targets.

```json
{
  "ir_path": "artifacts/project/ir.json",
  "targets": ["postgres", "neo4j", "pgvector"],
  "mode": "upsert",
  "version_key": "repo+commit"
}
```

## Outputs
Return markdown plus an index report.

```json
{
  "entities_written": {
    "modules": 0,
    "ports": 0,
    "instances": 0,
    "embeddings": 0
  },
  "stores": {
    "postgres": "ok",
    "neo4j": "ok",
    "pgvector": "ok"
  },
  "warnings": []
}
```

## Workflow
1. Validate required ids and version metadata in the IR.
2. Upsert relational entities first.
3. Materialize graph nodes and edges next.
4. Generate or refresh semantic text chunks for vector indexing.
5. Record lineage and summary counts.
6. Return a concise report with warnings and partial failures.

## Indexing rules
- never generate new canonical ids during indexing
- separate raw facts from inferred labels
- version rows by repo plus commit or immutable snapshot id
- preserve partial index success with per-store status

## Go implementation notes
Build this as a thin orchestrator over store adapters.
- packages: `internal/indexer`, `internal/store/postgres`, `internal/store/neo4j`, `internal/store/vector`
- define a common `Writer` interface and per-store transaction report
- prefer idempotent batch upserts and explicit retry boundaries

## Resources
- read `references/postgres-schema.md` for relational entities
- read `references/graph-schema.md` for nodes and edges
- read `references/vector-records.md` for embedding payloads
- use `assets/go_scaffold.txt` for suggested packages
