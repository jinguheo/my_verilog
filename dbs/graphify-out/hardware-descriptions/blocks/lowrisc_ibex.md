# Hardware Description: lowrisc_ibex

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `lowrisc_ibex`
- `approved_label`: `pending:lowrisc_ibex`
- `doc_anchor`: `lowrisc_ibex`
- `module_name_prefix`: `lowrisc_ibex`
- `bridge_edge_count`: 343

## Inferred Hardware Role

`lowrisc_ibex` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 518, testplan: 28, interface: 7
- Code categories: other_code: 1092, dv: 714, rtl: 310, package: 9
- Bridge relations: spec_path_matches_code_path: 343

## Spec Anchors

- `compliance.rst` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/compliance.rst`
- `Standards Compliance` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/compliance.rst`
- `index.rst` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/index.rst`
- `Introduction to Ibex` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/index.rst`
- `licensing.rst` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/licensing.rst`
- `Licensing` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/licensing.rst`
- `targets.rst` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/targets.rst`
- `Synthesis Targets` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/targets.rst`
- `ASIC Synthesis` (L4) - `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/targets.rst`
- `FPGA Synthesis` (L11) - `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/targets.rst`
- `verification_overview.rst` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/verification_overview.rst`
- `Verification Overview` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/verification_overview.rst`
- `Verification Status` (L9) - `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/verification_overview.rst`
- `configuration.rst` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/configuration.rst`
- `Ibex Configurations` (L3) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/configuration.rst`
- `Configuration Tool` (L11) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/configuration.rst`
- `Supported Configurations` (L35) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/configuration.rst`
- `examples.rst` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/examples.rst`
- `Examples` (L3) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/examples.rst`
- `Simple System` (L14) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/examples.rst`
- `getting_started.rst` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/getting_started.rst`
- `Getting Started with Ibex` (L3) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/getting_started.rst`
- `index.rst` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/index.rst`
- `Ibex User Guide` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/index.rst`
- `integration.rst` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `Core Integration` (L3) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `Register File` (L10) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `Identification CSRs` (L17) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `Primitives` (L33) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `RTL File List` (L65) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `Instantiation Template` (L86) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `Parameters` (L183) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `Interfaces` (L271) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `system_requirements.rst` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/system_requirements.rst`
- `System and Tool Requirements` (L1) - `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/system_requirements.rst`

## Code Evidence

- `Cosim()` (L44) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim.h`
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
- `SpikeCosim()` (L36) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
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
- `on_csr_write()` (L500) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `leave_nmi_mode()` (L513) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `handle_cpuctrl_exception_entry()` (L533) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `change_cpuctrlsts_sync_exc_seen()` (L542) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `set_cpuctrlsts_double_fault_seen()` (L557) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `initial_proc_setup()` (L564) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `set_mip()` (L586) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `early_interrupt_handle()` (L613) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `misaligned_pmp_fixup()` (L648) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `set_nmi()` (L685) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `set_nmi_int()` (L702) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `set_debug_req()` (L719) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `set_mcycle()` (L724) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `set_csr()` (L750) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
- `set_ic_scr_key_valid()` (L760) - `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `vendor.md` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `vendor.md` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `vendor.md` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `vendor.md` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `vendor.md` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `vendor.md` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `vendor.md` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `vendor.md` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `create_top.md` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `create_top.md` | `top.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `create_top.md` | `top` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `top_desc.md` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `top_desc.md` | `top.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `top_desc.md` | `top` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `index.rst` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `index.rst` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `index.rst` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `index.rst` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `index.rst` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `index.rst` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `index.rst` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `index.rst` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `index.rst` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `index.rst` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |

## Retrieval Guidance

- When a code-only query mentions `lowrisc_ibex`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
