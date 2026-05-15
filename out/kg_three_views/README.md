# Three KG Views

This folder is portable. Copy the whole `kg_three_views` folder to another PC
and open `OPEN_ME.html` or `index.html` in Chrome, Edge, or Firefox.

The HTML files are self-contained: graph data, JavaScript, and CSS are embedded
inside each file. No Python environment, local server, database, CDN, or
internet connection is required.

Some node details contain original paths such as `D:\MyWork\verilog\...`.
Those paths are metadata from the source machine only. They are not used for
loading the graph, so the files still open on another PC.

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
