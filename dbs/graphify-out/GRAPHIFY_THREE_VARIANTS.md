# Graphify Three KG Variants

This directory contains three Graphify-compatible KG variants.

| Variant | Nodes | Links/Edges | Graph JSON | Report |
|---|---:|---:|---|---|
| spec-only | 8196 | 30054 | spec-only-graphify\graph.json | spec-only-graphify\GRAPH_REPORT.md |
| code-only | 39694 | 95961 | code-only-graphify\graph.json | code-only-graphify\GRAPH_REPORT.md |
| spec-code | 47890 | 138613 | spec-code-graphify\graph.json | spec-code-graphify\GRAPH_REPORT.md |

## Variant Meaning

- `spec-only-graphify`: spec documents only, built deterministically from exported spec files.
- `code-only-graphify`: current code/rationale Graphify graph snapshot.
- `spec-code-graphify`: merged spec + code graph with inferred late-binding edges.

## Spec-Code Binding Edges

- `spec_component_matches_code`: spec component node matched to code node by component/path/label tokens.
- `spec_path_matches_code_path`: spec document path token matched to RTL/code source path token.

Large HTML visualization is skipped for these graphs because they exceed Graphify's HTML node limit.
Use `graph.json`, `GRAPH_REPORT.md`, or GraphML-capable tools for inspection.
