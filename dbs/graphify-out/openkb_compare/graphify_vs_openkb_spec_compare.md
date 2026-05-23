# Graphify Spec Graph vs OpenKB Prepared KB Comparison

Generated: 2026-05-17

## What Was Executed

OpenKB CLI `status` and `list` were executed against the prepared KB variants:

- `dbs/graphify-out/kb-variants/spec-only/kb`
- `dbs/graphify-out/kb-variants/spec-code/kb`

The LLM-backed `openkb add` and `openkb query` steps were not executed. The local OpenKB environment is prepared offline, but full OpenKB compilation requires the missing runtime dependencies and an LLM API key.

## Current Result

| Variant | Recursive raw files | OpenKB indexed documents | Wiki source pages | Summaries | Concepts | Reports |
|---|---:|---:|---:|---:|---:|---:|
| spec-only | 987 | 0 | 0 | 0 | 0 | 0 |
| spec-code | 995 | 0 | 0 | 0 | 0 | 0 |

OpenKB CLI output:

```text
spec-only:
Knowledge Base Status:
  sources   0
  summaries 0
  concepts  0
  reports   0
  raw       2
  Total indexed: 0 document(s)

spec-code:
Knowledge Base Status:
  sources   0
  summaries 0
  concepts  0
  reports   0
  raw       2
  Total indexed: 0 document(s)
```

The difference between recursive raw count and CLI raw count is because the OpenKB CLI counts direct files under `raw/`, while the prepared corpus stores most files under nested folders such as `raw/spec_documents/` and `raw/code_graph/`.

## Graphify Spec Graph

Graphify spec-only graph is already materialized as a graph:

| Item | Value |
|---|---:|
| Nodes | 8,196 |
| Edges | 30,054 |
| Communities | 33 |
| Extraction | 100% deterministic local extraction |
| LLM/API required | No |

Main node roles:

| Role | Count |
|---|---:|
| section | 6,748 |
| document | 985 |
| component | 437 |
| topic | 16 |
| category | 7 |
| project | 2 |
| corpus | 1 |

Main edge relations:

| Relation | Count |
|---|---:|
| references_component | 11,057 |
| documents_component | 9,423 |
| contains | 7,742 |
| mentions_topic | 1,832 |

## OpenKB Prepared KB

OpenKB is currently a prepared workspace, not a compiled wiki:

| Variant | Raw corpus contents |
|---|---|
| spec-only | Normalized spec documents only |
| spec-code | Normalized spec documents plus code graph summary/index files |

Spec document corpus:

| Item | Value |
|---|---:|
| Documents | 985 |
| OpenTitan docs | 933 |
| Ibex docs | 52 |
| Markdown | 545 |
| HJSON | 367 |
| RST | 70 |
| TXT | 3 |

## Key Difference

| Aspect | Graphify | OpenKB |
|---|---|---|
| Current state | Fully materialized graph | Prepared raw KB, not indexed |
| Output shape | `graph.json`, communities, HTML graph | `kb/raw`, `kb/wiki`, OpenKB skeleton |
| Spec structure | document, section, component, topic nodes | normalized Markdown documents |
| Relationship modeling | explicit graph edges | wiki links and summaries after `openkb add` |
| Current query readiness | graph traversal is ready | `openkb query` is not ready until indexed |
| Best use now | visual graph, structural retrieval, spec-code bridge | document QA after compile/index |

## Practical Conclusion

For the current repository state:

1. Graphify is the usable spec graph now.
2. OpenKB has the right input corpus prepared, but it has not compiled the documents into wiki/source/summary/concept pages yet.
3. To fairly compare Graphify vs OpenKB QA quality, the next step is to run `openkb add raw/` for `spec-only` and `spec-code` after installing OpenKB runtime dependencies and configuring an LLM API key.
4. Until then, OpenKB can be compared as a prepared document corpus, not as a completed KG/wiki retrieval engine.

