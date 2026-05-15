# Spec Document KG Summary

## Scope

This graph is built from extracted spec document anchors only. It is separate
from the code KG and is intended to connect to code through late-binding keys:
`ip_block`, `module_name`, `spec_section`, `doc_anchor`, and `approved_label`.

## Counts

- Documents: 986
- Nodes: 9157
- Edges: 19915

## Node Types

- approved_label: 49
- document: 986
- ip_block: 87
- ip_mention: 88
- module_mention: 168
- project: 3
- spec_section: 7776

## Edge Types

- ABOUT_IP: 986
- HAS_SECTION: 7776
- IN_PROJECT: 986
- MENTIONED_IN_IP_DOC: 824
- MENTIONS_IP_NAME: 2786
- MENTIONS_LABEL: 3337
- MENTIONS_MODULE: 3133
- PART_OF_PROJECT: 87

## Top IP Blocks

- opentitan/unknown: 309
- ibex/ibex: 40
- opentitan/pinmux: 38
- opentitan/rstmgr: 33
- opentitan/rv_core_ibex: 30
- opentitan/clkmgr: 27
- opentitan/gpio: 27
- opentitan/pwrmgr: 27
- opentitan/otp_ctrl: 26
- opentitan/rv_plic: 24
- opentitan/lc_ctrl: 19
- opentitan/flash_ctrl: 18
- opentitan/alert_handler: 14
- opentitan/otbn: 13
- opentitan/prim: 12

## Outputs

- `spec_doc_kg.json`: full graph for programmatic use
- `spec_doc_kg.ttl`: RDF/Turtle export for OpenTology/SPARQL-style workflows
- `spec_doc_kg.html`: local interactive overview
