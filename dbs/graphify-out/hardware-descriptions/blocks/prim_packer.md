# Hardware Description: prim_packer

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `prim_packer`
- `bridge_edge_count`: 5
- Spec categories: component: 6
- Code categories: rtl: 4, dv: 1
- Bridge relations: spec_component_matches_code: 5

## Spec Anchors

- `component:prim_packer` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**RTL** (4)
  - `prim_packer.sv`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer.sv`
  - `prim_packer`:L10 — `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer.sv`
  - `prim_packer.sv`:L1 — `opentitan\hw\ip\prim\rtl\prim_packer.sv`
  - `prim_packer`:L10 — `opentitan\hw\ip\prim\rtl\prim_packer.sv`
**DV** (1)
  - `prim_packer`:L49 — `opentitan\hw\ip\prim\fpv\tb\prim_packer_tb.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:prim_packer` | `prim_packer.sv` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer.sv` |
| `spec_component_matches_code` | `component:prim_packer` | `prim_packer` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer.sv` |
| `spec_component_matches_code` | `component:prim_packer` | `prim_packer` | `opentitan\hw\ip\prim\fpv\tb\prim_packer_tb.sv` |
| `spec_component_matches_code` | `component:prim_packer` | `prim_packer.sv` | `opentitan\hw\ip\prim\rtl\prim_packer.sv` |
| `spec_component_matches_code` | `component:prim_packer` | `prim_packer` | `opentitan\hw\ip\prim\rtl\prim_packer.sv` |

## Retrieval Guidance

- For code-only queries mentioning `prim_packer`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `prim_packer`.
