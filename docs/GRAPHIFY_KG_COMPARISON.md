# Current RTL KG vs Graphify

## Scope

- Source files compared: 1534
- Graphify graph: 3748 nodes / 5412 edges
- Graphify output: `D:\MyWork\verilog\graphify-out\graph.json`
- Current KG: 21792 nodes / 39268 edges

## Retrieval Performance

| Benchmark | Method | Hit@1 | Hit@3 | MRR |
|---|---:|---:|---:|---:|
| General 150 | Current KG | 0.7933 | 0.8333 | 0.8169 |
| General 150 | Graphify | 0.3800 | 0.5667 | 0.4865 |
| Multi-axis 175 | Current KG | 0.8514 | 0.8629 | 0.8562 |
| Multi-axis 175 | Graphify | 0.6914 | 0.8971 | 0.7950 |

## Token Use

Average tokens are estimated as characters / 4.

| Benchmark | Method | Avg context tokens | Reduction vs raw gold source |
|---|---:|---:|---:|
| General 150 | Current KG cards | 465.6 | 20.4x |
| General 150 | Graphify query subgraph | 1157.0 | 8.21x |
| Multi-axis 175 | Current KG cards | 472.8 | 28.62x |
| Multi-axis 175 | Graphify query subgraph | 1302.1 | 10.39x |

## Reading

- Current KG is better for RTL module retrieval because it stores Verilog-specific labels, ports, project identity, and instance edges.
- Graphify now works as a general code graph for this workspace, but its Verilog AST output is still thinner than the custom KG: module/file/import/instantiation structure, not domain labels or ports.
- Graphify is most useful as a broad architecture/navigation layer and as a persistent graph skill; the current KG remains the stronger retrieval engine for VerilogEval-style module lookup.
