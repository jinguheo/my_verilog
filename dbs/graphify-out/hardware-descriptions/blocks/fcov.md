# Hardware Description: fcov

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `fcov`
- `approved_label`: `pending:fcov`
- `doc_anchor`: `fcov`
- `module_name_prefix`: `fcov`
- `bridge_edge_count`: 14

## Inferred Hardware Role

`fcov` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 15
- Code categories: dv: 14
- Bridge relations: spec_component_matches_code: 14

## Spec Anchors

- `component:fcov` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `core_ibex_pmp_fcov_if.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\fcov\core_ibex_pmp_fcov_if.sv`
- `ibex_icache_fcov_bind.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_bind.sv`
- `ibex_icache_fcov_bind` (L7) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_bind.sv`
- `core_ibex_fcov_bind.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_bind.sv`
- `core_ibex_fcov_bind` (L5) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_bind.sv`
- `ibex_icache_fcov_if.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_if.sv`
- `core_ibex_fcov_if.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_if.sv`
- `core_ibex_pmp_fcov_if.sv` (L1) - `ibex\dv\uvm\core_ibex\fcov\core_ibex_pmp_fcov_if.sv`
- `ibex_icache_fcov_bind.sv` (L1) - `ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_bind.sv`
- `ibex_icache_fcov_bind` (L7) - `ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_bind.sv`
- `core_ibex_fcov_bind.sv` (L1) - `ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_bind.sv`
- `core_ibex_fcov_bind` (L5) - `ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_bind.sv`
- `ibex_icache_fcov_if.sv` (L1) - `ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_if.sv`
- `core_ibex_fcov_if.sv` (L1) - `ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_if.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:fcov` | `core_ibex_pmp_fcov_if.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\fcov\core_ibex_pmp_fcov_if.sv` |
| `spec_component_matches_code` | `component:fcov` | `ibex_icache_fcov_bind.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_bind.sv` |
| `spec_component_matches_code` | `component:fcov` | `ibex_icache_fcov_bind` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_bind.sv` |
| `spec_component_matches_code` | `component:fcov` | `core_ibex_fcov_bind.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_bind.sv` |
| `spec_component_matches_code` | `component:fcov` | `core_ibex_fcov_bind` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_bind.sv` |
| `spec_component_matches_code` | `component:fcov` | `ibex_icache_fcov_if.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_if.sv` |
| `spec_component_matches_code` | `component:fcov` | `core_ibex_fcov_if.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_if.sv` |
| `spec_component_matches_code` | `component:fcov` | `core_ibex_pmp_fcov_if.sv` | `ibex\dv\uvm\core_ibex\fcov\core_ibex_pmp_fcov_if.sv` |
| `spec_component_matches_code` | `component:fcov` | `ibex_icache_fcov_bind.sv` | `ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_bind.sv` |
| `spec_component_matches_code` | `component:fcov` | `ibex_icache_fcov_bind` | `ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_bind.sv` |
| `spec_component_matches_code` | `component:fcov` | `core_ibex_fcov_bind.sv` | `ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_bind.sv` |
| `spec_component_matches_code` | `component:fcov` | `core_ibex_fcov_bind` | `ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_bind.sv` |
| `spec_component_matches_code` | `component:fcov` | `ibex_icache_fcov_if.sv` | `ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_if.sv` |
| `spec_component_matches_code` | `component:fcov` | `core_ibex_fcov_if.sv` | `ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_if.sv` |

## Retrieval Guidance

- When a code-only query mentions `fcov`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
