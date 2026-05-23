# Spec-only Graphify KB

- Source: `D:\MyWork\verilog\out\ibex_mini_docs`
- Graph: `D:\MyWork\verilog\dbs\graphify-out\ibex-mini-A\graph.json`
- Report: `D:\MyWork\verilog\dbs\graphify-out\ibex-mini-A\GRAPH_REPORT.md`
- Nodes: 18
- Edges: 26
- Communities: 3

This KB is deterministic and spec-only. It does not include RTL/code nodes
and it did not run OpenKB or an LLM ingestion step.

Query example:

```powershell
& D:\MyWork\verilog\.venv-graphify\Scripts\graphify.exe query "ibex registers" --graph D:\MyWork\verilog\dbs\graphify-out\ibex-mini-A\graph.json
```
