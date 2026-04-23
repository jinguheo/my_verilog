---
name: rtl-design-generator
description: turn natural-language rtl requests into structured specs, retrieve relevant reference modules, plan microarchitecture, and generate reviewable rtl skeletons with validation hooks. use when chatgpt needs to help design a new verilog or systemverilog module or extend an existing one toward implementation.
---

# Overview
Guide rtl generation as a retrieval-grounded design workflow rather than direct free-form code generation.

## Use this skill to
- parse natural-language design requests into structured specs
- retrieve similar modules, interfaces, and style references
- propose microarchitecture and implementation plan
- generate reviewable rtl skeletons and validation checklists

## Inputs
Accept natural language or structured spec input.

```json
{
  "request": "design a single-clock fifo with depth 16 and width 32",
  "constraints": {
    "language": "systemverilog",
    "style": ["always_ff", "always_comb", "logic"],
    "reset": "active_low"
  }
}
```

## Outputs
Return markdown plus machine-readable design artifacts.

```json
{
  "structured_spec": {},
  "references": [],
  "architecture_plan": {},
  "rtl_skeleton": "module ... endmodule",
  "validation_checklist": [],
  "confidence": 0.0
}
```

## Workflow
1. convert the user request into a structured spec
2. retrieve similar modules and reusable patterns from the knowledge base
3. plan interfaces, subblocks, state, and hazards before code generation
4. generate a reviewable rtl skeleton first
5. include validation tasks such as parse, lint, elaboration, and smoke tests
6. state assumptions and unresolved design choices explicitly

## Guardrails
- do not skip retrieval when a similar module exists
- prefer skeleton plus rationale over overconfident full implementations
- separate facts from suggested design choices
- include test and assertion hooks whenever practical

## Go implementation notes
Implement this as staged orchestration.
- packages: `internal/spec`, `internal/reference`, `internal/plan`, `internal/generate`, `internal/validate`
- each stage should have a stable json contract for downstream automation
- keep generated code reviewable and style-constrained

## Resources
- read `references/spec-schema.md` for structured design requests
- read `references/generation-workflow.md` for stage contracts
- use `assets/go_scaffold.txt` for package layout
