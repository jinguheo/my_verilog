# Dispatch policy

## Intent map

### ingest
Trigger words:
- collect repos
- download public rtl
- snapshot
- manifest
- compile context

Route to:
- `rtl-source-ingestor`

### parse
Trigger words:
- tree-sitter
- ast
- cst
- lsp
- verible
- surelog
- slang
- elaborate
- normalize ir

Route to:
- `rtl-structure-parser`

### index
Trigger words:
- postgres
- neo4j
- graph db
- pgvector
- index data
- build graph
- version graph

Route to:
- `rtl-knowledge-indexer`

### qa
Trigger words:
- what does this module do
- explain this module
- show ports
- version
- who instantiates
- how is it connected

Route to:
- `rtl-module-qa`

### label
Trigger words:
- label taxonomy
- protocol tags
- semantic summary
- role classification
- function labels
- review queue

Route to:
- `rtl-semantic-labeler`

### generate
Trigger words:
- create rtl
- design a module
- rtl skeleton
- architecture plan
- generate verilog

Route to:
- `rtl-design-generator`

## Fallbacks
- if the question requires facts not present in the index, suggest `ingest -> parse -> index`
- if the answer is structurally complete but semantically weak, add `rtl-semantic-labeler`
- if generation lacks good references, run `rtl-module-qa` over related modules before `rtl-design-generator`

## Output contract
Always produce a minimal workflow trace:
```json
{
  "intent": "qa",
  "skills": ["rtl-module-qa"],
  "why": ["module explanation with connectivity evidence"],
  "blocked_by": []
}
```
