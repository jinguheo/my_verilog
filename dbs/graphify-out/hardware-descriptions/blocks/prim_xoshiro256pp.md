# Hardware Description: prim_xoshiro256pp

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `prim_xoshiro256pp`
- `approved_label`: `pending:prim_xoshiro256pp`
- `doc_anchor`: `prim_xoshiro256pp`
- `module_name_prefix`: `prim_xoshiro256pp`
- `bridge_edge_count`: 4

## Inferred Hardware Role

`prim_xoshiro256pp` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 5
- Code categories: rtl: 4
- Bridge relations: spec_component_matches_code: 4

## Spec Anchors

- `component:prim_xoshiro256pp` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `prim_xoshiro256pp.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_xoshiro256pp.sv`
- `prim_xoshiro256pp` (L17) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_xoshiro256pp.sv`
- `prim_xoshiro256pp.sv` (L1) - `opentitan\hw\ip\prim\rtl\prim_xoshiro256pp.sv`
- `prim_xoshiro256pp` (L17) - `opentitan\hw\ip\prim\rtl\prim_xoshiro256pp.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:prim_xoshiro256pp` | `prim_xoshiro256pp.sv` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_xoshiro256pp.sv` |
| `spec_component_matches_code` | `component:prim_xoshiro256pp` | `prim_xoshiro256pp` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_xoshiro256pp.sv` |
| `spec_component_matches_code` | `component:prim_xoshiro256pp` | `prim_xoshiro256pp.sv` | `opentitan\hw\ip\prim\rtl\prim_xoshiro256pp.sv` |
| `spec_component_matches_code` | `component:prim_xoshiro256pp` | `prim_xoshiro256pp` | `opentitan\hw\ip\prim\rtl\prim_xoshiro256pp.sv` |

## Retrieval Guidance

- When a code-only query mentions `prim_xoshiro256pp`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
