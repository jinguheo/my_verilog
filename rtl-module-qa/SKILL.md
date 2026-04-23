---
name: rtl-module-qa
description: answer questions about rtl modules, ports, parameters, versions, hierarchy, and connectivity using indexed structural and semantic data. use when chatgpt needs to explain what a verilog or systemverilog module does, show related versions, identify connections, or summarize evidence-backed module details.
---

# Overview
Answer evidence-backed questions about rtl modules and their relationships.

## Use this skill to
- explain what a module does in clear engineering language
- show ports, parameters, labels, and key always blocks
- identify parent modules, child instances, and signal bindings
- compare versions and surface high-confidence evidence

## Inputs
Accept free-form questions or structured lookup requests.

```json
{
  "question": "what does uart_rx do and how is it connected?",
  "module_name": "optional explicit target",
  "version": "optional commit or tag",
  "include_evidence": true
}
```

## Outputs
Return both markdown and machine-readable answer data.

```json
{
  "intent": "module_summary|connectivity|version|compare|similarity",
  "entities": ["uart_rx"],
  "answer": {
    "summary": "...",
    "version": {},
    "ports": [],
    "connectivity": {"parents": [], "children": [], "bindings": []},
    "labels": []
  },
  "evidence": [],
  "confidence": 0.0
}
```

## Retrieval policy
1. resolve explicit module names and versions first using relational facts
2. use graph traversal for hierarchy and connection questions
3. use semantic retrieval only to enrich summaries, not to replace structural facts
4. cite uncertainty whenever graph coverage or version coverage is incomplete

## Answer format
Present answers in this order when relevant:
1. one-line module purpose
2. version or repo context
3. ports or parameters that matter to the question
4. parent-child connectivity and notable signal bindings
5. labels and confidence

## Guardrails
- never invent connections not present in the graph or evidence
- distinguish fact, inference, and suggestion
- prefer concise module cards over long prose when multiple modules are requested

## Go implementation notes
Model this as a retrieval planner plus formatter.
- packages: `internal/qa`, `internal/retrieval`, `internal/formatter`, `internal/confidence`
- separate query planning from answer rendering
- keep graph queries explicit and testable

## Resources
- read `references/answer-contract.md` for the response schema
- read `references/retrieval-policy.md` for dispatch rules
- use `assets/go_scaffold.txt` for package layout
