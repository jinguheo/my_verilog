# Hardware Description: pulp_riscv_dbg

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Overview**: This document specifies the processor debug system. The debug system implements run-control debug and bus access functionality according to the [RISC-V Debug Specification 0.13.2](https://github.com/riscv/riscv-debug-…
- **Description**: - Run-control debug functionality according to the [RISC-V Debug Specification version 0.13.2](https://github.com/riscv/riscv-debug-spec/raw/4e0bb0fc2d843473db2356623792c6b7603b94d4/riscv-debug-release.pdf), which…
- **Compatibility**: - Support for up to 2^20 harts through one Debug Module

## Identity

- `ip_block`: `pulp_riscv_dbg`
- `bridge_edge_count`: 16
- Spec categories: document: 26, theory: 1
- Code categories: rtl: 77, other_code: 64, sva: 6, dv: 4, package: 3
- Bridge relations: spec_path_matches_code_path: 16

## Spec Excerpts

### Overview
_Source: `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`_

```
# Overview

This document specifies the processor debug system. The debug system implements run-control debug and bus access functionality according to the [RISC-V Debug Specification 0.13.2](https://github.com/riscv/riscv-debug-spec/raw/4e0bb0fc2d843473db2356623792c6b7603b94d4/riscv-debug-release.pdf). It can be accessed over JTAG (IEEE Std 1149.1-2013).

## Features

- Run-control debug function
…
```

### Description
_Source: `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`_

```
- Run-control debug functionality according to the [RISC-V Debug Specification version 0.13.2](https://github.com/riscv/riscv-debug-spec/raw/4e0bb0fc2d843473db2356623792c6b7603b94d4/riscv-debug-release.pdf), which includes all standard debug features: breakpoints, stepping, access to the CPU's GPRs and arbitrary memory locations.
- Implementation following the Execution Based method as outlined in
…
```

### Compatibility
_Source: `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`_

```
- Support for up to 2^20 harts through one Debug Module
- Support for arbitrary memory location of DM
- Support for one debug scratch register if the DM is located at the zero page.

## Description

The debug system described in this document consists of two modules, which are implemented according to the RISC-V Debug Specification: The Debug Module (DM) implemented with a Program Buffer, and a JT
…
```

## Spec Anchors

- `debug-system.md` (L1) — `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Overview` (L1) — `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Features` (L5) — `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Description` (L15) — `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Compatibility` (L19) — `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Theory of Operations` (L34) — `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Block Diagram` (L39) — `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Debug Module Registers` (L43) — `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `dmcontrol 0x10` (L87) — `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `dmstatus 0x11` (L103) — `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`
- `Customization` (L126) — `opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md`

## Code Evidence

**RTL** (38)
  - `prim_clock_mux2`:L76 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv`
  - `prim_fifo_sync`:L590 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_csrs.sv`
  - `prim_flop_2sync`:L65 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv`
  - `dmi_jtag`:L70 — `opentitan\hw\vendor\pulp_riscv_dbg\tb\jtag_dmi\tb_jtag_dmi.sv`
  - `dm_top`:L235 — `opentitan\hw\vendor\pulp_riscv_dbg\tb\tb_top_verilator.sv`
  - `prim_clock_inv`:L190 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_jtag_tap.sv`
  - `debug_rom.sv`:L1 — `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\debug_rom.sv`
  - `debug_rom`:L17 — `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\debug_rom.sv`
  - `debug_rom_one_scratch.sv`:L1 — `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\debug_rom_one_scratch.sv`
  - `debug_rom_one_scratch`:L17 — `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\debug_rom_one_scratch.sv`
  - `dmi_bscane_tap.sv`:L1 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_bscane_tap.sv`
  - `dmi_jtag_tap`:L14 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_bscane_tap.sv`
  - `BSCANE2`:L47 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_bscane_tap.sv`
  - `dmi_cdc.sv`:L1 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv`
  - `dmi_cdc`:L19 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv`
  - `prim_fifo_async_simple`:L85 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv`
  - `dmi_intf.sv`:L1 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_intf.sv`
  - `dm`:L10 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_test.sv`
  - `dmi_jtag.sv`:L1 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_jtag.sv`
  - `dmi_jtag`:L19 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_jtag.sv`
**SVA** (3)
  - `dm_csrs_sva.sv`:L1 — `opentitan\hw\vendor\pulp_riscv_dbg\sva\dm_csrs_sva.sv`
  - `dm_csrs_sva`:L31 — `opentitan\hw\vendor\pulp_riscv_dbg\sva\dm_csrs_sva.sv`
  - `dm_sba_sva.sv`:L1 — `opentitan\hw\vendor\pulp_riscv_dbg\sva\dm_sba_sva.sv`
**PACKAGE** (1)
  - `dm_pkg.sv`:L1 — `opentitan\hw\vendor\pulp_riscv_dbg\src\dm_pkg.sv`
**OTHER_CODE** (8)
  - `_exit()`:L97 — `opentitan\hw\vendor\pulp_riscv_dbg\tb\prog\syscalls.c`
  - `openocd-to-junit.py`:L1 — `opentitan\hw\vendor\pulp_riscv_dbg\ci\openocd-to-junit.py`
  - `main()`:L6 — `opentitan\hw\vendor\pulp_riscv_dbg\ci\openocd-to-junit.py`
  - `debug_rom.h`:L1 — `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\debug_rom.h`
  - `debug_rom_one_scratch.h`:L1 — `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\debug_rom_one_scratch.h`
  - `encoding.h`:L1 — `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\encoding.h`
  - `gen_rom.py`:L1 — `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\gen_rom.py`
  - `read_bin()`:L93 — `opentitan\hw\vendor\pulp_riscv_dbg\debug_rom\gen_rom.py`

## Neighbor Components

- `rstmgr` (24 refs; instantiates×24)
- `prim` (20 refs; instantiates×20)
- `pwrmgr` (16 refs; instantiates×16)
- `ast` (16 refs; instantiates×16)
- `clkmgr` (14 refs; instantiates×14)
- `spi_device` (8 refs; instantiates×8)
- `flash_ctrl` (8 refs; instantiates×8)
- `riscv-tests` (7 refs; calls×6, contains×1)
- `prim_generic` (6 refs; instantiates×6)
- `tlul` (5 refs; instantiates×5)
- `lowrisc_ibex` (4 refs; calls×3, instantiates×1)
- `rv_dm` (4 refs; instantiates×4)

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

- For code-only queries mentioning `pulp_riscv_dbg`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `pulp_riscv_dbg`.
