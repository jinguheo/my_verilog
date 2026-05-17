# Graphify vs OpenTology Code Graph Evaluation

This evaluation compares the local Graphify code graph JSON with the local OpenTology RDF/Turtle export generated from that graph. No LLM/API calls were used.

## Input Size and Load Cost

| Metric | Graphify JSON | OpenTology Turtle |
|---|---:|---:|
| File size | 57.70 MB | 30.69 MB |
| Nodes parsed | 39,694 | 39,694 |
| Edges parsed | 95,961 | 95,961 |
| Load time | 4.688 s | 4.863 s |
| Peak Python load memory | 173.2 MB | 50.7 MB |

## Query Performance

| Task | Cases | Graphify median | OpenTology median | Graphify speedup | Mean result Jaccard |
|---|---:|---:|---:|---:|---:|
| direct_relation | 60 | 0.0010 ms | 0.0009 ms | 0.95x | 1.000 |
| label_source_search | 10 | 69.3038 ms | 74.3827 ms | 1.05x | 1.000 |
| reverse_reachable_depth2 | 24 | 0.0766 ms | 0.0731 ms | 0.99x | 1.000 |
| community_lookup | 20 | 0.0615 ms | 0.0536 ms | 0.96x | 1.000 |

## Interpretation

- Graphify is the better default for fast retrieval and exploration because its JSON graph already carries the original extraction metadata, relation confidence, weights, communities, and HTML/graph-view tooling.
- OpenTology is better when you need a typed ontology layer, RDF interoperability, SPARQL-style governance queries, persistent project memory, decisions, issues, and agent workflow hooks.
- In this workspace, OpenTology is not adding new code facts beyond the Graphify-derived export; it mainly changes the representation and query model.
- For Verilog module lookup, instantiation navigation, and spec-code retrieval, Graphify/custom KG should remain the primary engine.
- For impact analysis, exact dependency/path queries, and future session/decision memory, OpenTology can be useful as an auxiliary layer once the local triplestore query path is stable.

## Caveats

- The OpenTology CLI SPARQL smoke query was slow and returned zero triples in the current local workspace state, so the detailed timing uses a direct parser over `current_graph.ttl`.
- The comparison is therefore a storage/query-model benchmark, not a full OpenTology MCP-agent workflow benchmark.
- Because OpenTology was generated from Graphify here, retrieval quality cannot exceed the underlying Graphify extraction unless additional OpenTology memory/decision data is added later.
