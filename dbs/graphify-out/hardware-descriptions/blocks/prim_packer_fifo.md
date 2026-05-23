# Hardware Description: prim_packer_fifo

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `prim_packer_fifo`
- `approved_label`: `pending:prim_packer_fifo`
- `doc_anchor`: `prim_packer_fifo`
- `module_name_prefix`: `prim_packer_fifo`
- `bridge_edge_count`: 5

## Inferred Hardware Role

`prim_packer_fifo` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 6
- Code categories: rtl: 5
- Bridge relations: spec_component_matches_code: 5

## Spec Anchors

- `component:prim_packer_fifo` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `prim_packer_fifo.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer_fifo.sv`
- `prim_packer_fifo` (L44) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer_fifo.sv`
- `prim_packer_fifo` (L233) - `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv`
- `prim_packer_fifo.sv` (L1) - `opentitan\hw\ip\prim\rtl\prim_packer_fifo.sv`
- `prim_packer_fifo` (L44) - `opentitan\hw\ip\prim\rtl\prim_packer_fifo.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:prim_packer_fifo` | `prim_packer_fifo.sv` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer_fifo.sv` |
| `spec_component_matches_code` | `component:prim_packer_fifo` | `prim_packer_fifo` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer_fifo.sv` |
| `spec_component_matches_code` | `component:prim_packer_fifo` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_component_matches_code` | `component:prim_packer_fifo` | `prim_packer_fifo.sv` | `opentitan\hw\ip\prim\rtl\prim_packer_fifo.sv` |
| `spec_component_matches_code` | `component:prim_packer_fifo` | `prim_packer_fifo` | `opentitan\hw\ip\prim\rtl\prim_packer_fifo.sv` |

## Retrieval Guidance

- When a code-only query mentions `prim_packer_fifo`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
