---
name: rtl-semantic-labeler
description: propose and maintain semantic labels, summaries, protocol tags, and design-intent metadata for rtl modules and blocks. use when chatgpt needs to classify modules such as fifo, arbiter, apb, or cdc, generate human-readable summaries, and prepare review-ready semantic enrichment records for the rtl knowledge base.
---

# Overview
Generate and maintain semantic metadata that structural parsers cannot provide alone.

## Use this skill to
- assign role, protocol, function, quality, and style labels
- summarize modules and important blocks in engineering language
- emit review-ready evidence and confidence
- grow the internal label taxonomy over time without breaking compatibility

## Inputs
Accept IR entities plus optional taxonomy hints.

```json
{
  "ir_path": "artifacts/project/ir.json",
  "taxonomy_version": "v1",
  "label_groups": ["role", "protocol", "function", "quality", "style"],
  "review_mode": true
}
```

## Outputs
Return markdown plus enrichment records.

```json
{
  "module_enrichments": [
    {
      "module_id": "...",
      "labels": [{"key": "fifo", "confidence": 0.93, "source": "rule"}],
      "summary_short": "...",
      "summary_long": "...",
      "evidence": []
    }
  ],
  "review_queue": [],
  "taxonomy_updates": []
}
```

## Workflow
1. run deterministic rules first for strong pattern matches
2. generate summary and label proposals next
3. attach evidence spans and provenance for each proposal
4. create a review queue for low-confidence or new labels
5. emit taxonomy update suggestions only when clearly justified

## Labeling rules
- keep taxonomy small and stable
- distinguish protocol tags from functional role tags
- do not mark a module as verified or reusable without evidence
- use low confidence rather than over-claiming

## Go implementation notes
Build a rule engine plus proposal pipeline.
- packages: `internal/taxonomy`, `internal/rules`, `internal/summary`, `internal/review`
- rules should be deterministic and unit-tested
- keep llm-proposed labels separate from approved labels in storage

## Resources
- read `references/taxonomy.md` for seed labels
- read `references/rule-examples.md` for deterministic patterns
- use `assets/go_scaffold.txt` for package layout
