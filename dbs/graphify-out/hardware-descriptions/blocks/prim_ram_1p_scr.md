# Hardware Description: prim_ram_1p_scr

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `prim_ram_1p_scr`
- `bridge_edge_count`: 5
- Spec categories: component: 6
- Code categories: rtl: 5
- Bridge relations: spec_component_matches_code: 5

## Spec Anchors

- `component:prim_ram_1p_scr` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**RTL** (5)
  - `prim_ram_1p_scr.sv`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ram_1p_scr.sv`
  - `prim_ram_1p_scr`:L26 — `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ram_1p_scr.sv`
  - `prim_ram_1p_scr.sv`:L1 — `opentitan\hw\ip\prim\rtl\prim_ram_1p_scr.sv`
  - `prim_ram_1p_scr`:L26 — `opentitan\hw\ip\prim\rtl\prim_ram_1p_scr.sv`
  - `prim_ram_1p_scr`:L679 — `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:prim_ram_1p_scr` | `prim_ram_1p_scr.sv` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ram_1p_scr.sv` |
| `spec_component_matches_code` | `component:prim_ram_1p_scr` | `prim_ram_1p_scr` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ram_1p_scr.sv` |
| `spec_component_matches_code` | `component:prim_ram_1p_scr` | `prim_ram_1p_scr.sv` | `opentitan\hw\ip\prim\rtl\prim_ram_1p_scr.sv` |
| `spec_component_matches_code` | `component:prim_ram_1p_scr` | `prim_ram_1p_scr` | `opentitan\hw\ip\prim\rtl\prim_ram_1p_scr.sv` |
| `spec_component_matches_code` | `component:prim_ram_1p_scr` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |

## Retrieval Guidance

- For code-only queries mentioning `prim_ram_1p_scr`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `prim_ram_1p_scr`.
