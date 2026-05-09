# Retrieval Methods Comparison

Questions: 175, modules indexed: 732

## Performance

| Method | Hit@1 | Hit@3 | MRR | Weighted Hit@1 | Avg query ms |
|---|---:|---:|---:|---:|---:|
| Baseline | 0.8514 | 0.8629 | 0.8686 | 0.8393 | 28.171 |
| KG | 0.8514 | 0.8629 | 0.8562 | 0.8423 | 34.284 |
| Manticore Parser/LSP | 0.8629 | 0.8914 | 0.8857 | 0.8401 | 37.386 |
| Manticore Hybrid | 0.8686 | 0.8914 | 0.8781 | 0.8479 | 46.418 |

## Method Features

| Method | Input signals | Ranking | Strength | Tradeoff |
|---|---|---|---|---|
| Baseline | Module name, file path, ports, instances | Parser/LSP lexical overlap with exact anchors | Fast simple lookup, transparent evidence | Weak on semantic paraphrase and function similarity |
| KG | Baseline fields plus labels, summaries, graph context | KG-aware scorer with semantic expansion | Uses ontology and reverse graph relationships | Can add noise when labels are broad or sparse |
| Manticore Parser/LSP | Parser/LSP fields only | Manticore-style BM25F full-text field weighting | Best text ranking without KG dependency | Still blind to ontology-only relationships |
| Manticore Hybrid | Parser/LSP fields plus KG labels, summaries, parents | BM25F with KG field boosts | Best overall Hit@1 in this run | Slowest local proxy query latency |
