# Hardware Description: cosim

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `cosim`
- `approved_label`: `pending:cosim`
- `doc_anchor`: `cosim`
- `module_name_prefix`: `cosim`
- `bridge_edge_count`: 40

## Inferred Hardware Role

`cosim` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 41
- Code categories: dv: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:cosim` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `SpikeCosim()` (L36) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `spike_cosim.cc` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `spike_cosim.h` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.h`
- `riscv_cosim_step()` (L13) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `riscv_cosim_set_mip()` (L24) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `riscv_cosim_set_nmi()` (L31) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `riscv_cosim_set_nmi_int()` (L37) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `riscv_cosim_set_debug_req()` (L42) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `riscv_cosim_set_mcycle()` (L48) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `riscv_cosim_set_csr()` (L55) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `riscv_cosim_set_ic_scr_key_valid()` (L62) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `riscv_cosim_notify_dside_access()` (L68) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `riscv_cosim_set_iside_error()` (L89) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `riscv_cosim_get_num_errors()` (L95) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `riscv_cosim_get_error()` (L101) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `riscv_cosim_clear_errors()` (L111) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `riscv_cosim_write_mem_byte()` (L117) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `riscv_cosim_get_insn_cnt()` (L124) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `cosim_dpi.cc` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc`
- `cosim_dpi.h` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.h`
- `Cosim()` (L44) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim.h`
- `cosim.h` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim.h`
- `spike_cosim.cc` (L1) - `ibex\dv\cosim\spike_cosim.cc`
- `spike_cosim.h` (L1) - `ibex\dv\cosim\spike_cosim.h`
- `cosim_dpi.cc` (L1) - `ibex\dv\cosim\cosim_dpi.cc`
- `cosim_dpi.h` (L1) - `ibex\dv\cosim\cosim_dpi.h`
- `cosim.h` (L1) - `ibex\dv\cosim\cosim.h`
- `addr_to_mem()` (L82) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `mmio_load()` (L84) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `mmio_store()` (L113) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `proc_reset()` (L122) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `get_symbol()` (L124) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `add_memory()` (L126) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `backdoor_write_mem()` (L132) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `backdoor_read_mem()` (L137) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `step()` (L172) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `check_retired_instr()` (L321) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `check_sync_trap()` (L389) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `check_gpr_write()` (L435) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `check_suppress_reg_write()` (L475) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`

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

- When a code-only query mentions `cosim`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
