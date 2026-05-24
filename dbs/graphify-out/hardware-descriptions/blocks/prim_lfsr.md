# Hardware Description: prim_lfsr

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `prim_lfsr`
- `bridge_edge_count`: 9
- Spec categories: component: 10
- Code categories: rtl: 5, dv: 4
- Bridge relations: spec_component_matches_code: 9

## Spec Anchors

- `component:prim_lfsr` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**RTL** (5)
  - `prim_lfsr`:L76 — `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_dummy_instr.sv`
  - `prim_lfsr.sv`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_lfsr.sv`
  - `prim_lfsr`:L29 — `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_lfsr.sv`
  - `prim_lfsr.sv`:L1 — `opentitan\hw\ip\prim\rtl\prim_lfsr.sv`
  - `prim_lfsr`:L29 — `opentitan\hw\ip\prim\rtl\prim_lfsr.sv`
**DV** (4)
  - `prim_lfsr_tb.sv`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_lfsr\prim_lfsr_tb.sv`
  - `prim_lfsr_tb`:L8 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_lfsr\prim_lfsr_tb.sv`
  - `prim_lfsr_tb.sv`:L1 — `opentitan\hw\ip\prim\dv\prim_lfsr\prim_lfsr_tb.sv`
  - `prim_lfsr_tb`:L8 — `opentitan\hw\ip\prim\dv\prim_lfsr\prim_lfsr_tb.sv`

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

- For code-only queries mentioning `prim_lfsr`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `prim_lfsr`.
