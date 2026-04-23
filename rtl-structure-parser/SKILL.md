---
name: rtl-structure-parser
description: parse verilog and systemverilog source snapshots into a normalized rtl intermediate representation using tree-sitter for fast syntax indexing and surelog, slang, or verible outputs for richer structure. use when chatgpt needs module, port, parameter, instance, always-block, and connectivity extraction for downstream indexing or question answering.
---

# Overview
Transform source snapshots into a parser-agnostic rtl intermediate representation.

## Use this skill to
- run syntax-first and semantic-aware parsing passes
- merge tree-sitter, surelog, slang, and verible outputs into one IR
- extract modules, interfaces, packages, ports, parameters, instances, and block summaries
- annotate parse gaps and confidence when elaboration is incomplete

## Inputs
Expect an ingest manifest plus optional parser configuration.

```json
{
  "manifest_path": "snapshots/project/manifest.json",
  "preferred_parsers": ["tree-sitter", "surelog", "slang", "verible"],
  "parse_mode": "best_effort",
  "top_context": "optional"
}
```

## Outputs
Return markdown plus IR json.

Required IR sections:

```json
{
  "files": [],
  "modules": [],
  "interfaces": [],
  "packages": [],
  "instances": [],
  "signals": [],
  "diagnostics": [],
  "confidence": {"overall": 0.0}
}
```

## Workflow
1. Load the ingest manifest and choose the best parser set.
2. Use tree-sitter output for spans, definitions, and fast fallback structure.
3. Use surelog or slang results for richer semantic structure and elaboration when available.
4. Normalize all parser outputs into the canonical IR.
5. Preserve evidence spans and parser provenance per entity.
6. Emit unresolved references as diagnostics, not silent omissions.

## Normalization rules
- assign stable ids using repo, file path, entity type, and local name
- store widths as expressions, not only folded integers
- keep both source-order children and graph-ready relationships
- attach parser provenance to every module and instance

## Go implementation notes
Use a pipeline package with parser adapters.
- packages: `internal/ir`, `internal/parsers`, `internal/normalize`, `internal/diagnostics`
- each parser adapter should emit a narrow adapter model before normalization
- keep `ParseResult` separate from final `IRDocument`

## Resources
- read `references/ir-schema.md` for the canonical IR
- read `references/normalization-rules.md` for merge rules
- use `assets/go_scaffold.txt` as the starter layout
