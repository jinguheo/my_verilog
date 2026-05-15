# Three KG Views

## 1. Spec-Only

Input: spec documents only.

- HTML: `spec_only_kg.html`
- No code dependency.

## 2. Spec-Code

Input: spec document anchors plus code module KG.

- HTML: `spec_code_kg.html`
- JSON: `spec_code_kg.json`
- Meaning: spec and code are separate nodes joined by late-binding edges.

Counts:

- Spec documents: 986
- Code modules: 1433
- Nodes: 2561
- Edges: 24435
- Edge types: {'CODE_IN_IP': 1256, 'EXACT_MODULE_LINK': 4036, 'IP_BLOCK_LINK': 13679, 'LABEL_TO_CODE_MODULE': 465, 'SPEC_ABOUT_IP': 676, 'SPEC_IN_PROJECT': 986, 'SPEC_MENTIONS_LABEL': 3337}

## 3. Code-Only

Input: custom RTL code KG only.

- HTML: `code_only_kg.html`
- No spec document nodes.
