---
name: rtl-orchestrator
description: coordinate a multi-skill rtl knowledge and design workflow across source ingestion, structural parsing, indexing, module question answering, semantic labeling, and rtl generation. use when chatgpt needs to route a verilog or systemverilog task to the right rtl skill, combine outputs from multiple rtl skills, or decide the next step in an end-to-end workflow from public source collection through generated rtl skeletons.
---

# Overview
Route rtl work to the correct specialized skill and keep outputs consistent across the full pipeline.

## Core capabilities
### 1. Dispatch by task intent
Map the user request to one or more of these skills:
- `rtl-source-ingestor` for repo collection, snapshot manifests, compile contexts, and source normalization
- `rtl-structure-parser` for tree-sitter, surelog, slang, verible, and IR normalization work
- `rtl-knowledge-indexer` for postgres, graph, and vector indexing
- `rtl-module-qa` for module explanations, versions, hierarchy, and connectivity answers
- `rtl-semantic-labeler` for role, protocol, function, and quality labels plus summaries
- `rtl-design-generator` for spec parsing, reference retrieval, architecture planning, and rtl skeleton generation

### 2. Chain skills in the right order
Use these default sequences.

**Build or refresh the database**
1. run `rtl-source-ingestor`
2. run `rtl-structure-parser`
3. run `rtl-semantic-labeler` if labels or summaries are missing
4. run `rtl-knowledge-indexer`

**Answer a technical question**
1. run `rtl-module-qa`
2. run `rtl-semantic-labeler` only if the answer needs missing labels or a better summary
3. run `rtl-knowledge-indexer` only if stale indexing blocks the answer

**Prepare new rtl design work**
1. run `rtl-module-qa` or `rtl-semantic-labeler` to collect references
2. run `rtl-design-generator`
3. suggest validation or indexing follow-up when the generated output should be stored

### 3. Normalize outputs
When combining results from multiple skills, preserve these top-level fields when possible:
```json
{
  "task_type": "ingest|parse|index|qa|label|generate|multi_step",
  "status": "ok|partial|blocked",
  "summary": "...",
  "artifacts": [],
  "evidence": [],
  "confidence": 0.0,
  "next_steps": []
}
```

## Dispatch rules
### Use `rtl-source-ingestor` when
- the user wants to pull public verilog or systemverilog repos
- the repo, branch, tag, manifest, allowlist, or compile context is the main task
- raw snapshots or file inventories are missing

### Use `rtl-structure-parser` when
- the user asks for AST, CST, IR, elaboration, or parser setup
- module, port, parameter, instance, or binding extraction is required
- tree-sitter, surelog, slang, or verible output must be normalized

### Use `rtl-knowledge-indexer` when
- new IR should be loaded into postgres, graph, or vector stores
- graph connectivity or vector summaries are stale or missing
- schema, version, or index consistency is the task

### Use `rtl-module-qa` when
- the user asks what a module does
- the user wants ports, parameters, versions, hierarchy, signal bindings, or connectivity
- the user asks for evidence-backed explanations of indexed rtl

### Use `rtl-semantic-labeler` when
- role, protocol, function, or quality labels are missing
- the user wants better summaries, taxonomy growth, or review queues
- new internal db semantics must be added consistently

### Use `rtl-design-generator` when
- the user wants a new module, architecture plan, or rtl skeleton
- the user provides a natural-language spec or structured design constraints
- retrieval-augmented generation is needed from existing references

## Conflict resolution
- prefer structure-first answers over semantic guesses
- prefer indexed facts over generated summaries when they disagree
- surface uncertainty if indexing or elaboration coverage is incomplete
- do not call the generator when the user is only asking explanatory questions
- do not claim a module is connected unless that fact exists in graph or binding evidence

## Output pattern
For end-to-end tasks, return:
1. the chosen skill sequence
2. the reason for each handoff
3. the combined result or current blocking point
4. concrete next steps

## Go implementation notes
Treat this as a thin orchestration layer.
- packages: `internal/orchestrator`, `internal/intent`, `internal/contracts`, `internal/pipeline`
- keep skill dispatch declarative through intent-to-skill maps
- preserve structured contracts so downstream services stay testable
- keep orchestration stateless except for workflow trace ids

## Resources
- read `references/dispatch-policy.md` for intent routing and fallback rules
- read `references/workflow-map.md` for end-to-end sequences
- use `assets/go_scaffold.txt` for package layout
