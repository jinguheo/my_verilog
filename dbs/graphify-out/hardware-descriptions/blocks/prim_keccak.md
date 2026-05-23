# Hardware Description: prim_keccak

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `prim_keccak`
- `approved_label`: `pending:prim_keccak`
- `doc_anchor`: `prim_keccak`
- `module_name_prefix`: `prim_keccak`
- `bridge_edge_count`: 5

## Inferred Hardware Role

`prim_keccak` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 6
- Code categories: rtl: 4, dv: 1
- Bridge relations: spec_component_matches_code: 5

## Spec Anchors

- `component:prim_keccak` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `prim_keccak.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_keccak.sv`
- `prim_keccak` (L10) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_keccak.sv`
- `prim_keccak` (L47) - `opentitan\hw\ip\prim\fpv\tb\prim_keccak_tb.sv`
- `prim_keccak.sv` (L1) - `opentitan\hw\ip\prim\rtl\prim_keccak.sv`
- `prim_keccak` (L10) - `opentitan\hw\ip\prim\rtl\prim_keccak.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:prim_keccak` | `prim_keccak.sv` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_keccak.sv` |
| `spec_component_matches_code` | `component:prim_keccak` | `prim_keccak` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_keccak.sv` |
| `spec_component_matches_code` | `component:prim_keccak` | `prim_keccak` | `opentitan\hw\ip\prim\fpv\tb\prim_keccak_tb.sv` |
| `spec_component_matches_code` | `component:prim_keccak` | `prim_keccak.sv` | `opentitan\hw\ip\prim\rtl\prim_keccak.sv` |
| `spec_component_matches_code` | `component:prim_keccak` | `prim_keccak` | `opentitan\hw\ip\prim\rtl\prim_keccak.sv` |

## Retrieval Guidance

- When a code-only query mentions `prim_keccak`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
