# Hardware Description: cosim

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `cosim`
- `bridge_edge_count`: 40
- Spec categories: component: 41
- Code categories: dv: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:cosim` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**DV** (40)
  - `SpikeCosim()`:L36 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
  - `spike_cosim.cc`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
  - `spike_cosim.h`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.h`
  - `riscv_cosim_step()`:L13 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `riscv_cosim_set_mip()`:L24 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `riscv_cosim_set_nmi()`:L31 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `riscv_cosim_set_nmi_int()`:L37 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `riscv_cosim_set_debug_req()`:L42 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `riscv_cosim_set_mcycle()`:L48 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `riscv_cosim_set_csr()`:L55 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `riscv_cosim_set_ic_scr_key_valid()`:L62 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `riscv_cosim_notify_dside_access()`:L68 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `riscv_cosim_set_iside_error()`:L89 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `riscv_cosim_get_num_errors()`:L95 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `riscv_cosim_get_error()`:L101 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `riscv_cosim_clear_errors()`:L111 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `riscv_cosim_write_mem_byte()`:L117 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `riscv_cosim_get_insn_cnt()`:L124 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `cosim_dpi.cc`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
  - `cosim_dpi.h`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.h`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:cosim` | `SpikeCosim()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `spike_cosim.cc` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `spike_cosim.h` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.h` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_step()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_set_mip()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_set_nmi()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_set_nmi_int()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_set_debug_req()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_set_mcycle()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_set_csr()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_set_ic_scr_key_valid()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_notify_dside_access()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_set_iside_error()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_get_num_errors()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_get_error()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_clear_errors()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_write_mem_byte()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `riscv_cosim_get_insn_cnt()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `cosim_dpi.cc` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `cosim_dpi.h` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.h` |
| `spec_component_matches_code` | `component:cosim` | `Cosim()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim.h` |
| `spec_component_matches_code` | `component:cosim` | `cosim.h` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim.h` |
| `spec_component_matches_code` | `component:cosim` | `spike_cosim.cc` | `ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `spike_cosim.h` | `ibex\dv\cosim\spike_cosim.h` |
| `spec_component_matches_code` | `component:cosim` | `cosim_dpi.cc` | `ibex\dv\cosim\cosim_dpi.cc` |
| `spec_component_matches_code` | `component:cosim` | `cosim_dpi.h` | `ibex\dv\cosim\cosim_dpi.h` |
| `spec_component_matches_code` | `component:cosim` | `cosim.h` | `ibex\dv\cosim\cosim.h` |
| `spec_component_matches_code` | `component:cosim` | `addr_to_mem()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `mmio_load()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `mmio_store()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `proc_reset()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `get_symbol()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `add_memory()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `backdoor_write_mem()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `backdoor_read_mem()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `step()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `check_retired_instr()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `check_sync_trap()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `check_gpr_write()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |
| `spec_component_matches_code` | `component:cosim` | `check_suppress_reg_write()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` |

## Retrieval Guidance

- For code-only queries mentioning `cosim`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `cosim`.
