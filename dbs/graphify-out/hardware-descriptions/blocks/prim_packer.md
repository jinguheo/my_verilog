# Hardware Description: prim_packer

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `prim_packer`
- `approved_label`: `pending:prim_packer`
- `doc_anchor`: `prim_packer`
- `module_name_prefix`: `prim_packer`
- `bridge_edge_count`: 5

## Inferred Hardware Role

`prim_packer` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 6
- Code categories: rtl: 4, dv: 1
- Bridge relations: spec_component_matches_code: 5

## Spec Anchors

- `component:prim_packer` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `prim_packer.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer.sv`
- `prim_packer` (L10) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer.sv`
- `prim_packer` (L49) - `opentitan\hw\ip\prim\fpv\tb\prim_packer_tb.sv`
- `prim_packer.sv` (L1) - `opentitan\hw\ip\prim\rtl\prim_packer.sv`
- `prim_packer` (L10) - `opentitan\hw\ip\prim\rtl\prim_packer.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:prim_packer` | `prim_packer.sv` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer.sv` |
| `spec_component_matches_code` | `component:prim_packer` | `prim_packer` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer.sv` |
| `spec_component_matches_code` | `component:prim_packer` | `prim_packer` | `opentitan\hw\ip\prim\fpv\tb\prim_packer_tb.sv` |
| `spec_component_matches_code` | `component:prim_packer` | `prim_packer.sv` | `opentitan\hw\ip\prim\rtl\prim_packer.sv` |
| `spec_component_matches_code` | `component:prim_packer` | `prim_packer` | `opentitan\hw\ip\prim\rtl\prim_packer.sv` |

## Retrieval Guidance

- When a code-only query mentions `prim_packer`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
