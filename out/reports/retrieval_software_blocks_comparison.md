# Retrieval Software Blocks Comparison

Methods 1, 2, and 3 now share the same tree-sitter-verilog frontend through `platform/ingest/generate_ontology_seed.py --frontend auto`. Regex extraction is only a fallback when the tree-sitter package is not available.

KG snapshot: 1433 modules, 16766 ports, 2103 instance edges, 18251 nodes, 22630 edges.

## Block-Level Differences

| Method | Frontend | Main software blocks | Processing focus | Strength | Tradeoff |
|---|---|---|---|---|---|
| 1. Parser + LSP Baseline | tree-sitter-verilog seed extractor, with regex fallback only when the Python tree-sitter package is unavailable | platform/ingest/generate_ontology_seed.py<br>tree_sitter.Parser + tree_sitter_verilog.language()<br>find_modules_tree_sitter(): module_declaration nodes<br>module_instantiation AST nodes for child module links<br>PORT_RE inside each AST module body for input/output/inout ports<br>platform/eval/retrieval_common.py baseline scorer | Walk RTL files under dbs/opentitan and dbs/ibex.<br>Parse each Verilog/SystemVerilog file with tree-sitter-verilog.<br>Extract module name, file path, ports, instances, and instance names into JSONL seed rows.<br>Rank benchmark queries by parser/LSP-style lexical overlap over module name, path, ports, and instances. | Fast structural lookup from AST-derived RTL facts. | No KG-only semantic expansion or graph traversal. |
| 2. Parser + LSP + Manticore | Same tree-sitter-verilog seed as method 1 | platform/eval/run_manticore_retrieval_analysis.py<br>BM25FIndex local Manticore-style ranker<br>manticore_documents.jsonl loader-ready full-text documents<br>manticore_schema.sql for later real Manticore Search loading<br>tools/manticoresearch local source checkout reference | Reuse tree-sitter module facts from merged_ontology_seed.jsonl.<br>Convert parser/LSP fields into weighted full-text documents.<br>Rank queries with BM25F-style field weighting over module, path, ports, instances, and instance names.<br>Emit documents and SQL schema so the same representation can be loaded into Manticore Search later. | Full-text ranking over parser/LSP fields without requiring KG context. | The current benchmark uses a local Manticore-style ranker, not a live searchd server. |
| 3. Knowledge Graph (Neo4j-style KG snapshot) | Same tree-sitter-verilog seed as method 1, plus labels and graph context | platform/eval/build_full_kg_snapshot.py<br>out/merged_ontology_seed.jsonl<br>out/merged_labels.jsonl<br>out/kg_full/kg_full_nodes_edges.json<br>platform/eval/retrieval_common.py KG scorer | Start from tree-sitter-extracted modules, ports, and instance edges.<br>Attach labels, summaries, IP block context, reverse parent hints, and inferred graph relationships.<br>Build a node/edge snapshot that can be mapped to a Neo4j-style graph model.<br>Rank queries with KG-aware expansion and graph-context signals. | Best Hit@1 in the current tree-sitter run because labels and graph context help disambiguation. | Quality depends on label coverage and graph extraction completeness. |
| 4. Graphify | Graphify AST and knowledge-graph extraction; independent graph builder with tree-sitter-style code structure extraction | graphify update .<br>graphify-out/graph.json<br>graphify-out/GRAPH_REPORT.md<br>graphify-out/graph_top_communities.html<br>graphify-out/wiki/index.md when present | Scan the whole workspace, including code, docs, scripts, generated reports, and Verilog assets.<br>Extract entities and EXTRACTED plus INFERRED relationships into a large knowledge graph.<br>Cluster communities and identify god nodes, bridges, and cross-module structure.<br>Generate HTML/JSON/Markdown audit artifacts for architecture browsing rather than benchmark-only retrieval. | Broad workspace-level architecture and community discovery. | Large graphs can exceed HTML visualization limits; use reports and JSON when the graph is too large. |

## Current Retrieval Metrics

| Mode | hit@1 | hit@3 | MRR | weighted hit@1 |
|---|---:|---:|---:|---:|
| `baseline` | 0.8629 | 0.8743 | 0.8824 | 0.8601 |
| `kg` | 0.8686 | 0.8800 | 0.8733 | 0.8683 |
| `manticore_parser_lsp` | 0.8629 | 0.8971 | 0.8935 | 0.8423 |
| `manticore_hybrid` | 0.8629 | 0.8971 | 0.8781 | 0.8423 |

## Short Answer

- Yes, methods 1, 2, and 3 can use tree-sitter, and the workflow has been updated so they do when `.venv-graphify` is available.
- Method 1 uses the AST facts directly with a lexical/parser-LSP scorer.
- Method 2 keeps the same AST facts but changes ranking to Manticore-style BM25F full-text retrieval.
- Method 3 keeps the same AST facts and adds labels, summaries, reverse parents, and graph relationships.
- Method 4 is broader: Graphify builds a workspace knowledge graph and community view, not just the retrieval benchmark index.
