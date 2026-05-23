# Hardware Description: prim_ram_1p_scr

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `prim_ram_1p_scr`
- `approved_label`: `pending:prim_ram_1p_scr`
- `doc_anchor`: `prim_ram_1p_scr`
- `module_name_prefix`: `prim_ram_1p_scr`
- `bridge_edge_count`: 5

## Inferred Hardware Role

`prim_ram_1p_scr` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 6
- Code categories: rtl: 5
- Bridge relations: spec_component_matches_code: 5

## Spec Anchors

- `component:prim_ram_1p_scr` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `prim_ram_1p_scr.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ram_1p_scr.sv`
- `prim_ram_1p_scr` (L26) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ram_1p_scr.sv`
- `prim_ram_1p_scr.sv` (L1) - `opentitan\hw\ip\prim\rtl\prim_ram_1p_scr.sv`
- `prim_ram_1p_scr` (L26) - `opentitan\hw\ip\prim\rtl\prim_ram_1p_scr.sv`
- `prim_ram_1p_scr` (L679) - `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:prim_ram_1p_scr` | `prim_ram_1p_scr.sv` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ram_1p_scr.sv` |
| `spec_component_matches_code` | `component:prim_ram_1p_scr` | `prim_ram_1p_scr` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ram_1p_scr.sv` |
| `spec_component_matches_code` | `component:prim_ram_1p_scr` | `prim_ram_1p_scr.sv` | `opentitan\hw\ip\prim\rtl\prim_ram_1p_scr.sv` |
| `spec_component_matches_code` | `component:prim_ram_1p_scr` | `prim_ram_1p_scr` | `opentitan\hw\ip\prim\rtl\prim_ram_1p_scr.sv` |
| `spec_component_matches_code` | `component:prim_ram_1p_scr` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |

## Retrieval Guidance

- When a code-only query mentions `prim_ram_1p_scr`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
