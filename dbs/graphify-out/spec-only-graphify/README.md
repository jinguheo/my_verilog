# Spec-only Graphify KB

- Source: `D:\MyWork\verilog\out\spec_documents_20260514_204108`
- Graph: `D:\MyWork\verilog\dbs\graphify-out\spec-only-graphify\graph.json`
- Report: `D:\MyWork\verilog\dbs\graphify-out\spec-only-graphify\GRAPH_REPORT.md`
- Nodes: 8196
- Edges: 30054
- Communities: 33

This KB is deterministic and spec-only. It does not include RTL/code nodes
and it did not run OpenKB or an LLM ingestion step.

Query example:

```powershell
& D:\MyWork\verilog\.venv-graphify\Scripts\graphify.exe query "ibex registers" --graph D:\MyWork\verilog\dbs\graphify-out\spec-only-graphify\graph.json
```
