# Graphify Tree-Sitter Spec/Code Variant Evaluation Summary

## Scope

- Date: 2026-05-20
- Question set: `out/spec_code_retrieval_benchmark/questions_all.jsonl`
- Questions: 150
- Variants:
  - `spec-only`: `dbs/graphify-out/spec-only-graphify/graph.json`
  - `code-only`: `dbs/graphify-out/code-only-graphify/graph.json`
  - `spec-code`: `dbs/graphify-out/spec-code-graphify/graph.json`
- No `graphify update` was run. This evaluation used the stored graph JSON files.

## Tree-Sitter Check

- `tree_sitter` import: OK
- `tree_sitter_verilog` import: OK
- Current ontology seed frontend count: `tree-sitter = 1433 / 1433`
- Code graph snapshot:
  - `code-only`: 39,694 nodes, 95,961 links
  - `spec-code`: 47,890 nodes, 138,613 links

This means the current Graphify code-side extraction path is configured for tree-sitter Verilog/SystemVerilog parsing rather than regex-only extraction. The stored graph JSON does not repeat the parser frontend on every node, so the verification is based on the active Graphify environment, the ontology seed metadata, and the saved code graph snapshot.

## Overall Results

| Variant | Spec hit@5 | Code hit@5 | Joint hit@5 | Joint hit@10 | Joint MRR |
|---|---:|---:|---:|---:|---:|
| spec-only | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| code-only | 0.0000 | 0.1267 | 0.0000 | 0.0000 | 0.0000 |
| spec-code | 0.8933 | 0.3000 | 0.2533 | 0.3867 | 0.1132 |

## Interpretation

- `spec-only` is excellent for finding the correct spec evidence, but it cannot answer questions that also require the matching RTL/code node.
- `code-only` can find some code evidence, but it has no spec-side evidence, so joint spec-code traceability is zero.
- `spec-code` is the only variant that can retrieve both sides together. It improves code hit@5 from `0.1267` to `0.3000` and produces non-zero joint retrieval.
- The biggest practical value of tree-sitter in this setup is that the code graph has more reliable Verilog/SystemVerilog structural nodes and relations, which makes the spec-code bridge more useful than a raw text or regex-only code graph.

## Saved Artifacts

- `spec_code_graphify_variant_report.md`
- `spec_code_graphify_variant_report.json`
- `spec_code_graphify_variant_predictions.json`
