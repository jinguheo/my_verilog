# Spec-only Graphify KB

- Source: `D:\MyWork\verilog\out\ibex_graphify_openkb\kb\wiki`
- Graph: `D:\MyWork\verilog\dbs\graphify-out\ibex-graphify-openkb-graphify\graph.json`
- Report: `D:\MyWork\verilog\dbs\graphify-out\ibex-graphify-openkb-graphify\GRAPH_REPORT.md`
- Nodes: 191
- Edges: 524
- Communities: 10

This KB is deterministic and spec-only. It does not include RTL/code nodes
and it did not run OpenKB or an LLM ingestion step.

Query example:

```powershell
& D:\MyWork\verilog\.venv-graphify\Scripts\graphify.exe query "ibex registers" --graph D:\MyWork\verilog\dbs\graphify-out\ibex-graphify-openkb-graphify\graph.json
```
