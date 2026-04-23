# Workflow map

## 1. Build a fresh public rtl knowledge base

Input:
- repo urls
- allowlist or denylist
- branch or tag constraints

Sequence:
1. `rtl-source-ingestor`
2. `rtl-structure-parser`
3. `rtl-semantic-labeler`
4. `rtl-knowledge-indexer`

Expected outputs:
- snapshot manifest
- normalized IR
- labels and summaries
- indexed relational, graph, and vector records

## 2. Explain an indexed module

Input:
- module name or question

Sequence:
1. `rtl-module-qa`
2. optional `rtl-semantic-labeler`

Expected outputs:
- module card
- version context
- hierarchy and binding summary
- confidence and evidence

## 3. Prepare a new rtl design

Input:
- natural-language spec or structured spec json

Sequence:
1. optional `rtl-module-qa` for references
2. optional `rtl-semantic-labeler` for better reference labels
3. `rtl-design-generator`

Expected outputs:
- structured spec
- architecture plan
- rtl skeleton or generated block
- next validation steps

## 4. Repair stale answers

Sequence:
1. `rtl-knowledge-indexer` if IR exists but index is stale
2. `rtl-structure-parser` if parser artifacts are stale or missing
3. `rtl-source-ingestor` if the raw repo snapshot is missing
