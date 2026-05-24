# Hardware Description: prim_flash

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `prim_flash`
- `bridge_edge_count`: 6
- Spec categories: component: 7
- Code categories: rtl: 6
- Bridge relations: spec_component_matches_code: 6

## Spec Anchors

- `component:prim_flash` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**RTL** (6)
  - `prim_flash`:L355 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv`
  - `prim_flash.sv`:L1 — `ibex\vendor\lowrisc_ip\ip\prim_generic\rtl\prim_flash.sv`
  - `prim_flash`:L8 — `ibex\vendor\lowrisc_ip\ip\prim_generic\rtl\prim_flash.sv`
  - `prim_flash.sv`:L1 — `opentitan\hw\ip\prim_generic\rtl\prim_flash.sv`
  - `prim_flash`:L8 — `opentitan\hw\ip\prim_generic\rtl\prim_flash.sv`
  - `flash_ctrl_prim_reg_top`:L118 — `opentitan\hw\ip\prim_generic\rtl\prim_flash.sv`

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

- For code-only queries mentioning `prim_flash`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `prim_flash`.
