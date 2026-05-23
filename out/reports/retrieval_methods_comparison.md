# Retrieval Methods Comparison

Total methods: 4
Questions: 175

## Performance

| Method | Hit@1 | Hit@3 | MRR | Weighted Hit@1 | Avg query ms |
|---|---:|---:|---:|---:|---:|
| Parser+LSP | 0.8629 | 0.8743 | 0.8824 | 0.8601 | n/a |
| KG | 0.8686 | 0.8800 | 0.8733 | 0.8683 | n/a |
| Graphify | 0.6914 | 0.8971 | 0.7950 | 0.6913 | n/a |
| Manticore | 0.8629 | 0.8971 | 0.8935 | 0.8423 | 46.801 |

## Method Features

| Method | Input signals | Ranking | Strength | Tradeoff |
|---|---|---|---|---|
| Parser+LSP | tree-sitter parser/LSP seed: module name, file path, ports, instances | Parser/LSP-style lexical overlap with exact anchors | Fast structural RTL lookup | No cross-module graph or full-text ranker |
| KG | parser/LSP seed plus labels, summaries, reverse parents | KG-aware scorer with semantic expansion | Best weighted structural retrieval in this run | Depends on KG label and graph quality |
| Graphify | Graphify AST graph and BFS query subgraph | Graph node match mapped back to RTL modules | General codebase navigation and relationship context | Less Verilog-specific than the custom KG |
| Manticore | parser/LSP fields indexed as Manticore-style full-text documents | BM25F-style field weighting with exact boosts | Best Hit@3/MRR among parser+LSP-only methods | Local proxy model; real searchd server not started |

## Reading

- `KG` has the best weighted hit@1 because Verilog-specific labels and reverse graph hints help harder questions.
- `Manticore` improves parser+LSP full-text ranking, especially hit@3 and MRR, without requiring KG fields.
- `Graphify` is useful for broad codebase navigation but is weaker for exact Verilog module retrieval in this benchmark.
