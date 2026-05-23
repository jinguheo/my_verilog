# Hardware Description: pulp_riscv_dbg

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `pulp_riscv_dbg`
- `approved_label`: `pending:pulp_riscv_dbg`
- `doc_anchor`: `pulp_riscv_dbg`
- `module_name_prefix`: `pulp_riscv_dbg`
- `bridge_edge_count`: 16

## Inferred Hardware Role

`pulp_riscv_dbg` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 26, theory: 1
- Code categories: rtl: 77, other_code: 64, sva: 6, dv: 4, package: 3
- Bridge relations: spec_path_matches_code_path: 16

## Spec Anchors

- `debug-system.md` (L1) - `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Overview` (L1) - `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Features` (L5) - `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Description` (L15) - `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Compatibility` (L19) - `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Theory of Operations` (L34) - `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Block Diagram` (L39) - `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Debug Module Registers` (L43) - `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `dmcontrol 0x10` (L87) - `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `dmstatus 0x11` (L103) - `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Customization` (L126) - `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`

## Code Evidence

- `prim_clock_mux2` (L76) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv`
- `prim_fifo_sync` (L590) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_csrs.sv`
- `prim_flop_2sync` (L65) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv`
- `_exit()` (L97) - `opentitan\hw\vendor\pulp_riscv_dbg\tb\prog\syscalls.c`
- `dmi_jtag` (L70) - `opentitan\hw\vendor\pulp_riscv_dbg\tb\jtag_dmi\tb_jtag_dmi.sv`
- `dm_top` (L235) - `opentitan\hw\vendor\pulp_riscv_dbg\tb\tb_top_verilator.sv`
- `prim_clock_inv` (L190) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_jtag_tap.sv`
- `openocd-to-junit.py` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\ci\openocd-to-junit.py`
- `main()` (L6) - `opentitan\hw\vendor\pulp_riscv_dbg\ci\openocd-to-junit.py`
- `debug_rom.h` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\debug_rom.h`
- `debug_rom.sv` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\debug_rom.sv`
- `debug_rom` (L17) - `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\debug_rom.sv`
- `debug_rom_one_scratch.h` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\debug_rom_one_scratch.h`
- `debug_rom_one_scratch.sv` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\debug_rom_one_scratch.sv`
- `debug_rom_one_scratch` (L17) - `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\debug_rom_one_scratch.sv`
- `encoding.h` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\encoding.h`
- `gen_rom.py` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\gen_rom.py`
- `read_bin()` (L93) - `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\gen_rom.py`
- `dmi_bscane_tap.sv` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_bscane_tap.sv`
- `dmi_jtag_tap` (L14) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_bscane_tap.sv`
- `BSCANE2` (L47) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_bscane_tap.sv`
- `dmi_cdc.sv` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv`
- `dmi_cdc` (L19) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv`
- `prim_fifo_async_simple` (L85) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv`
- `dmi_intf.sv` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_intf.sv`
- `dm` (L10) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_test.sv`
- `dmi_jtag.sv` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_jtag.sv`
- `dmi_jtag` (L19) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_jtag.sv`
- `dmi_jtag_tap` (L305) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_jtag.sv`
- `dmi_cdc` (L331) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_jtag.sv`
- `dmi_jtag_tap.sv` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_jtag_tap.sv`
- `dmi_jtag_tap` (L19) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_jtag_tap.sv`
- `dmi_test.sv` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_test.sv`
- `dm_csrs.sv` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_csrs.sv`
- `dm_csrs` (L18) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_csrs.sv`
- `dm_mem.sv` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_mem.sv`
- `dm_mem` (L19) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_mem.sv`
- `debug_rom` (L566) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_mem.sv`
- `debug_rom_one_scratch` (L577) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_mem.sv`
- `dm_pkg.sv` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_pkg.sv`
- `dm_sba.sv` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_sba.sv`
- `dm_sba` (L18) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_sba.sv`
- `dm_top.sv` (L1) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_top.sv`
- `dm_top` (L20) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_top.sv`
- `dm_csrs` (L118) - `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_top.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `debug-system.md` | `prim_clock_mux2` | `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `prim_fifo_sync` | `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_csrs.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `prim_flop_2sync` | `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `dmi_jtag` | `opentitan\hw\vendor\pulp_riscv_dbg\tb\jtag_dmi\tb_jtag_dmi.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `dm_top` | `opentitan\hw\vendor\pulp_riscv_dbg\tb\tb_top_verilator.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `prim_clock_inv` | `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_jtag_tap.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `debug_rom.sv` | `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\debug_rom.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `debug_rom` | `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\debug_rom.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `debug-system.md` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |

## Retrieval Guidance

- When a code-only query mentions `pulp_riscv_dbg`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
