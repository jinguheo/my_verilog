# Hardware Description: prim_flash

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `prim_flash`
- `approved_label`: `pending:prim_flash`
- `doc_anchor`: `prim_flash`
- `module_name_prefix`: `prim_flash`
- `bridge_edge_count`: 6

## Inferred Hardware Role

`prim_flash` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 7
- Code categories: rtl: 6
- Bridge relations: spec_component_matches_code: 6

## Spec Anchors

- `component:prim_flash` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `prim_flash` (L355) - `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv`
- `prim_flash.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim_generic\rtl\prim_flash.sv`
- `prim_flash` (L8) - `ibex\vendor\lowrisc_ip\ip\prim_generic\rtl\prim_flash.sv`
- `prim_flash.sv` (L1) - `opentitan\hw\ip\prim_generic\rtl\prim_flash.sv`
- `prim_flash` (L8) - `opentitan\hw\ip\prim_generic\rtl\prim_flash.sv`
- `flash_ctrl_prim_reg_top` (L118) - `opentitan\hw\ip\prim_generic\rtl\prim_flash.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:prim_flash` | `prim_flash` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv` |
| `spec_component_matches_code` | `component:prim_flash` | `prim_flash.sv` | `ibex\vendor\lowrisc_ip\ip\prim_generic\rtl\prim_flash.sv` |
| `spec_component_matches_code` | `component:prim_flash` | `prim_flash` | `ibex\vendor\lowrisc_ip\ip\prim_generic\rtl\prim_flash.sv` |
| `spec_component_matches_code` | `component:prim_flash` | `prim_flash.sv` | `opentitan\hw\ip\prim_generic\rtl\prim_flash.sv` |
| `spec_component_matches_code` | `component:prim_flash` | `prim_flash` | `opentitan\hw\ip\prim_generic\rtl\prim_flash.sv` |
| `spec_component_matches_code` | `component:prim_flash` | `flash_ctrl_prim_reg_top` | `opentitan\hw\ip\prim_generic\rtl\prim_flash.sv` |

## Retrieval Guidance

- When a code-only query mentions `prim_flash`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
