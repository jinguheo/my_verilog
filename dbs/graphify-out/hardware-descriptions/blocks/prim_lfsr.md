# Hardware Description: prim_lfsr

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `prim_lfsr`
- `approved_label`: `pending:prim_lfsr`
- `doc_anchor`: `prim_lfsr`
- `module_name_prefix`: `prim_lfsr`
- `bridge_edge_count`: 9

## Inferred Hardware Role

`prim_lfsr` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 10
- Code categories: rtl: 5, dv: 4
- Bridge relations: spec_component_matches_code: 9

## Spec Anchors

- `component:prim_lfsr` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `prim_lfsr_tb.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_lfsr\prim_lfsr_tb.sv`
- `prim_lfsr_tb` (L8) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_lfsr\prim_lfsr_tb.sv`
- `prim_lfsr` (L76) - `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_dummy_instr.sv`
- `prim_lfsr_tb.sv` (L1) - `opentitan\hw\ip\prim\dv\prim_lfsr\prim_lfsr_tb.sv`
- `prim_lfsr_tb` (L8) - `opentitan\hw\ip\prim\dv\prim_lfsr\prim_lfsr_tb.sv`
- `prim_lfsr.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_lfsr.sv`
- `prim_lfsr` (L29) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_lfsr.sv`
- `prim_lfsr.sv` (L1) - `opentitan\hw\ip\prim\rtl\prim_lfsr.sv`
- `prim_lfsr` (L29) - `opentitan\hw\ip\prim\rtl\prim_lfsr.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:prim_lfsr` | `prim_lfsr_tb.sv` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_lfsr\prim_lfsr_tb.sv` |
| `spec_component_matches_code` | `component:prim_lfsr` | `prim_lfsr_tb` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_lfsr\prim_lfsr_tb.sv` |
| `spec_component_matches_code` | `component:prim_lfsr` | `prim_lfsr` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_dummy_instr.sv` |
| `spec_component_matches_code` | `component:prim_lfsr` | `prim_lfsr_tb.sv` | `opentitan\hw\ip\prim\dv\prim_lfsr\prim_lfsr_tb.sv` |
| `spec_component_matches_code` | `component:prim_lfsr` | `prim_lfsr_tb` | `opentitan\hw\ip\prim\dv\prim_lfsr\prim_lfsr_tb.sv` |
| `spec_component_matches_code` | `component:prim_lfsr` | `prim_lfsr.sv` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_lfsr.sv` |
| `spec_component_matches_code` | `component:prim_lfsr` | `prim_lfsr` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_lfsr.sv` |
| `spec_component_matches_code` | `component:prim_lfsr` | `prim_lfsr.sv` | `opentitan\hw\ip\prim\rtl\prim_lfsr.sv` |
| `spec_component_matches_code` | `component:prim_lfsr` | `prim_lfsr` | `opentitan\hw\ip\prim\rtl\prim_lfsr.sv` |

## Retrieval Guidance

- When a code-only query mentions `prim_lfsr`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
