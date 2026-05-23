# Hardware Description: testplanner

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `testplanner`
- `approved_label`: `pending:testplanner`
- `doc_anchor`: `testplanner`
- `module_name_prefix`: `testplanner`
- `bridge_edge_count`: 3

## Inferred Hardware Role

`testplanner` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: testplan: 4
- Code categories: other_code: 3
- Bridge relations: spec_component_matches_code: 3

## Spec Anchors

- `component:testplanner` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `testplanner.py` (L1) - `ibex\vendor\lowrisc_ip\util\dvsim\testplanner.py`
- `testplanner.py` (L1) - `opentitan\util\dvsim\testplanner.py`
- `main()` (L14) - `opentitan\util\dvsim\testplanner.py`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:testplanner` | `testplanner.py` | `ibex\vendor\lowrisc_ip\util\dvsim\testplanner.py` |
| `spec_component_matches_code` | `component:testplanner` | `testplanner.py` | `opentitan\util\dvsim\testplanner.py` |
| `spec_component_matches_code` | `component:testplanner` | `main()` | `opentitan\util\dvsim\testplanner.py` |

## Retrieval Guidance

- When a code-only query mentions `testplanner`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
