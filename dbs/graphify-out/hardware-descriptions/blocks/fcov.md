# Hardware Description: fcov

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `fcov`
- `bridge_edge_count`: 14
- Spec categories: component: 15
- Code categories: dv: 14
- Bridge relations: spec_component_matches_code: 14

## Spec Anchors

- `component:fcov` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**DV** (14)
  - `core_ibex_pmp_fcov_if.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\fcov\core_ibex_pmp_fcov_if.sv`
  - `ibex_icache_fcov_bind.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_bind.sv`
  - `ibex_icache_fcov_bind`:L7 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_bind.sv`
  - `core_ibex_fcov_bind.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_bind.sv`
  - `core_ibex_fcov_bind`:L5 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_bind.sv`
  - `ibex_icache_fcov_if.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_if.sv`
  - `core_ibex_fcov_if.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_if.sv`
  - `core_ibex_pmp_fcov_if.sv`:L1 — `ibex\dv\uvm\core_ibex\fcov\core_ibex_pmp_fcov_if.sv`
  - `ibex_icache_fcov_bind.sv`:L1 — `ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_bind.sv`
  - `ibex_icache_fcov_bind`:L7 — `ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_bind.sv`
  - `core_ibex_fcov_bind.sv`:L1 — `ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_bind.sv`
  - `core_ibex_fcov_bind`:L5 — `ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_bind.sv`
  - `ibex_icache_fcov_if.sv`:L1 — `ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_if.sv`
  - `core_ibex_fcov_if.sv`:L1 — `ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_if.sv`

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

- For code-only queries mentioning `fcov`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `fcov`.
