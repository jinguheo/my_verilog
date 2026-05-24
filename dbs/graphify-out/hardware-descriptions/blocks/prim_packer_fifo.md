# Hardware Description: prim_packer_fifo

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `prim_packer_fifo`
- `bridge_edge_count`: 5
- Spec categories: component: 6
- Code categories: rtl: 5
- Bridge relations: spec_component_matches_code: 5

## Spec Anchors

- `component:prim_packer_fifo` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**RTL** (5)
  - `prim_packer_fifo.sv`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer_fifo.sv`
  - `prim_packer_fifo`:L44 — `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer_fifo.sv`
  - `prim_packer_fifo`:L233 — `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv`
  - `prim_packer_fifo.sv`:L1 — `opentitan\hw\ip\prim\rtl\prim_packer_fifo.sv`
  - `prim_packer_fifo`:L44 — `opentitan\hw\ip\prim\rtl\prim_packer_fifo.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:prim_packer_fifo` | `prim_packer_fifo.sv` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer_fifo.sv` |
| `spec_component_matches_code` | `component:prim_packer_fifo` | `prim_packer_fifo` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer_fifo.sv` |
| `spec_component_matches_code` | `component:prim_packer_fifo` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_component_matches_code` | `component:prim_packer_fifo` | `prim_packer_fifo.sv` | `opentitan\hw\ip\prim\rtl\prim_packer_fifo.sv` |
| `spec_component_matches_code` | `component:prim_packer_fifo` | `prim_packer_fifo` | `opentitan\hw\ip\prim\rtl\prim_packer_fifo.sv` |

## Retrieval Guidance

- For code-only queries mentioning `prim_packer_fifo`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `prim_packer_fifo`.
