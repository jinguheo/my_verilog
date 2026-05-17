# OpenTology-Friendly Relation Query Benchmark

This benchmark is intentionally shaped around what OpenTology should be good at: exact graph relation queries, reverse impact queries, transitive reachability, path checks, and community/typed graph lookups.

No LLM/API calls were used. The benchmark uses the local OpenTology Turtle export.

## Summary

- Source: `D:\MyWork\verilog\dbs\graphify-out\opentology-current\.opentology\data\current_graph.ttl`
- Nodes: 39,694
- Edges: 95,961
- Load time: 0.790 s
- Questions: 111

## Question Mix

| Category | Questions | Median eval time | Mean answer count |
|---|---:|---:|---:|
| direct_relation | 36 | 0.0013 ms | 166.5 |
| reverse_relation | 24 | 0.0008 ms | 149.9 |
| transitive_reachable | 15 | 0.1651 ms | 416.7 |
| impact_reverse_reachable | 12 | 0.2477 ms | 564.5 |
| path_query | 12 | 0.0100 ms | 2.2 |
| community_peers | 12 | 0.4000 ms | 25.0 |

## Example Questions

| ID | Category | Question | Answers |
|---|---|---|---:|
| direct_calls_001 | direct_relation | Which nodes does `.ok()` directly `calls`? | 1157 |
| direct_calls_002 | direct_relation | Which nodes does `.exit()` directly `calls`? | 874 |
| direct_calls_003 | direct_relation | Which nodes does `tohost_exit()` directly `calls`? | 746 |
| direct_calls_004 | direct_relation | Which nodes does `.append()` directly `calls`? | 618 |
| direct_calls_005 | direct_relation | Which nodes does `mmio_region_read32()` directly `calls`? | 477 |
| direct_calls_006 | direct_relation | Which nodes does `memcpy()` directly `calls`? | 459 |
| direct_instantiates_007 | direct_relation | Which nodes does `prim_flop_2sync` directly `instantiates`? | 109 |
| direct_instantiates_008 | direct_relation | Which nodes does `prim_flop` directly `instantiates`? | 86 |
| direct_instantiates_009 | direct_relation | Which nodes does `tlul_rsp_intg_gen` directly `instantiates`? | 77 |
| direct_instantiates_010 | direct_relation | Which nodes does `prim_subreg` directly `instantiates`? | 69 |
| direct_instantiates_011 | direct_relation | Which nodes does `tlul_adapter_reg` directly `instantiates`? | 69 |
| direct_instantiates_012 | direct_relation | Which nodes does `prim_reg_we_check` directly `instantiates`? | 67 |

## Interpretation

- These questions are better suited to OpenTology than broad semantic retrieval because they can be expressed as exact RDF/SPARQL patterns.
- Strong categories: direct relation lookup, reverse relation lookup, transitive reachability, impact-style reverse traversal, and explicit path existence.
- Weak categories remain natural-language design explanation, fuzzy spec-code matching, and Verilog generation context; those still need Graphify/custom KG plus retrieval scoring.
- In the current workspace, OpenTology facts are derived from Graphify, so this benchmark evaluates the query/ontology layer, not new extraction quality.
