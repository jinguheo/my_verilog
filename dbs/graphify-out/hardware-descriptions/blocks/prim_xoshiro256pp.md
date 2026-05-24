# Hardware Description: prim_xoshiro256pp

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `prim_xoshiro256pp`
- `bridge_edge_count`: 4
- Spec categories: component: 5
- Code categories: rtl: 4
- Bridge relations: spec_component_matches_code: 4

## Spec Anchors

- `component:prim_xoshiro256pp` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**RTL** (4)
  - `prim_xoshiro256pp.sv`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_xoshiro256pp.sv`
  - `prim_xoshiro256pp`:L17 — `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_xoshiro256pp.sv`
  - `prim_xoshiro256pp.sv`:L1 — `opentitan\hw\ip\prim\rtl\prim_xoshiro256pp.sv`
  - `prim_xoshiro256pp`:L17 — `opentitan\hw\ip\prim\rtl\prim_xoshiro256pp.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:prim_xoshiro256pp` | `prim_xoshiro256pp.sv` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_xoshiro256pp.sv` |
| `spec_component_matches_code` | `component:prim_xoshiro256pp` | `prim_xoshiro256pp` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_xoshiro256pp.sv` |
| `spec_component_matches_code` | `component:prim_xoshiro256pp` | `prim_xoshiro256pp.sv` | `opentitan\hw\ip\prim\rtl\prim_xoshiro256pp.sv` |
| `spec_component_matches_code` | `component:prim_xoshiro256pp` | `prim_xoshiro256pp` | `opentitan\hw\ip\prim\rtl\prim_xoshiro256pp.sv` |

## Retrieval Guidance

- For code-only queries mentioning `prim_xoshiro256pp`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `prim_xoshiro256pp`.
