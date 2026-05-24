# Hardware Description: pmp

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `pmp`
- `bridge_edge_count`: 35
- Spec categories: component: 36
- Code categories: other_code: 35
- Bridge relations: spec_component_matches_code: 35

## Spec Anchors

- `component:pmp` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**OTHER_CODE** (35)
  - `pmp.c`:L1 — `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c`
  - `pmp_ok()`:L65 — `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c`
  - `set_pmp()`:L132 — `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c`
  - `set_pmp_range()`:L143 — `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c`
  - `set_pmp_napot()`:L152 — `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c`
  - `pmp.c`:L1 — `opentitan\sw\device\lib\runtime\pmp.c`
  - `pmp_cfg_csr_read()`:L90 — `opentitan\sw\device\lib\runtime\pmp.c`
  - `pmp_cfg_csr_write()`:L116 — `opentitan\sw\device\lib\runtime\pmp.c`
  - `pmp_addr_csr_read()`:L139 — `opentitan\sw\device\lib\runtime\pmp.c`
  - `pmp_addr_csr_write()`:L161 — `opentitan\sw\device\lib\runtime\pmp.c`
  - `pmp_csr_cfg_field_read()`:L185 — `opentitan\sw\device\lib\runtime\pmp.c`
  - `pmp_csr_cfg_field_write()`:L213 — `opentitan\sw\device\lib\runtime\pmp.c`
  - `pmp_csr_address_write()`:L264 — `opentitan\sw\device\lib\runtime\pmp.c`
  - `pmp_cfg_permissions_set()`:L290 — `opentitan\sw\device\lib\runtime\pmp.c`
  - `pmp_cfg_mode_lock_set()`:L329 — `opentitan\sw\device\lib\runtime\pmp.c`
  - `pmp_address_aligned()`:L347 — `opentitan\sw\device\lib\runtime\pmp.c`
  - `pmp_napot_address_construct()`:L364 — `opentitan\sw\device\lib\runtime\pmp.c`
  - `pmp_region_configure_off()`:L391 — `opentitan\sw\device\lib\runtime\pmp.c`
  - `pmp_region_configure_na4()`:L417 — `opentitan\sw\device\lib\runtime\pmp.c`
  - `pmp_region_configure_napot()`:L456 — `opentitan\sw\device\lib\runtime\pmp.c`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:pmp` | `pmp.c` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_ok()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `set_pmp()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `set_pmp_range()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `set_pmp_napot()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp.c` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_cfg_csr_read()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_cfg_csr_write()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_addr_csr_read()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_addr_csr_write()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_csr_cfg_field_read()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_csr_cfg_field_write()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_csr_address_write()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_cfg_permissions_set()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_cfg_mode_lock_set()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_address_aligned()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_napot_address_construct()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_region_configure_off()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_region_configure_na4()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_region_configure_napot()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_region_configure_tor()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_region_is_configured()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp_region_lock_status_get()` | `opentitan\sw\device\lib\runtime\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `pmp.h` | `opentitan\sw\device\lib\runtime\pmp.h` |
| `spec_component_matches_code` | `component:pmp` | `handle_trap()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `init_pt()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `va2pa()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `test_one()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `test_all_sizes()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `test_range_once()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `test_range()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `test_ranges()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `exhaustive_test()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `detect_granule()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |
| `spec_component_matches_code` | `component:pmp` | `main()` | `ibex\vendor\riscv-tests\benchmarks\pmp\pmp.c` |

## Retrieval Guidance

- For code-only queries mentioning `pmp`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `pmp`.
