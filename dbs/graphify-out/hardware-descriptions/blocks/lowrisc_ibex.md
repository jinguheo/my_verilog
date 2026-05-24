# Hardware Description: lowrisc_ibex

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Standards Compliance**: Ibex is a standards-compliant 32 bit RISC-V processor.
- **Licensing**: Ibex is released under the Apache license, version 2.0.
- **Synthesis Targets**: ASIC Synthesis

## Identity

- `ip_block`: `lowrisc_ibex`
- `bridge_edge_count`: 343
- Spec categories: document: 518, testplan: 28, interface: 7
- Code categories: other_code: 1092, dv: 714, rtl: 310, package: 9
- Bridge relations: spec_path_matches_code_path: 343

## Spec Excerpts

### Standards Compliance
_Source: `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/compliance.rst`_

```
Standards Compliance
====================

Ibex is a standards-compliant 32 bit RISC-V processor.
It follows these specifications:

* `RISC-V Instruction Set Manual, Volume I: User-Level ISA, document version 20190608-Base-Ratified (June 8, 2019) <https://github.com/riscv/riscv-isa-manual/releases/download/Ratified-IMFDQC-and-Priv-v1.11/riscv-spec-20190608.pdf>`_
* `RISC-V Instruction Set Manual,
…
```

### Licensing
_Source: `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/licensing.rst`_

```
Licensing
=========

Ibex is released under the Apache license, version 2.0.

Ibex can be used, modified, and distributed for any purpose (including commercial) and without any royalties.
There are some requirements on including copyright notices and the original license.
```

### Synthesis Targets
_Source: `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/targets.rst`_

```
Synthesis Targets
=================

ASIC Synthesis
--------------

ASIC synthesis is supported for Ibex.
The whole design is completely synchronous and uses positive-edge triggered flip-flops, except for the register file, which can be implemented either with latches or with flip-flops.
```

### ASIC Synthesis
_Source: `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/targets.rst`_

```
Synthesis Targets
=================

ASIC Synthesis
--------------

ASIC synthesis is supported for Ibex.
The whole design is completely synchronous and uses positive-edge triggered flip-flops, except for the register file, which can be implemented either with latches or with flip-flops.
See :ref:`register-file` for more details.

FPGA Synthesis
```

### FPGA Synthesis
_Source: `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/targets.rst`_

```
ASIC Synthesis
--------------

ASIC synthesis is supported for Ibex.
The whole design is completely synchronous and uses positive-edge triggered flip-flops, except for the register file, which can be implemented either with latches or with flip-flops.
See :ref:`register-file` for more details.

FPGA Synthesis
--------------

FPGA Synthesis is supported for Ibex.
The FPGA-optimized register file im
…
```

### Verification Overview
_Source: `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/verification_overview.rst`_

```
Verification Overview
=====================

Ibex is verified using a :ref:`UVM based testbench<verification>` that employs a :ref:`co-simulation methodology<cosim>` to cross-check Ibex execution against an ISS reference model (`Spike <https://github.com/lowRISC/riscv-isa-sim>`_).
The testbench runs binaries built from source produced by the `RISC-DV <https://github.com/chipsalliance/riscv-dv>`_ r
…
```

### Verification Status
_Source: `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/verification_overview.rst`_

```
Verification Overview
=====================

Ibex is verified using a :ref:`UVM based testbench<verification>` that employs a :ref:`co-simulation methodology<cosim>` to cross-check Ibex execution against an ISS reference model (`Spike <https://github.com/lowRISC/riscv-isa-sim>`_).
The testbench runs binaries built from source produced by the `RISC-DV <https://github.com/chipsalliance/riscv-dv>`_ r
…
```

### Examples
_Source: `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/examples.rst`_

```
.. _examples:

Examples
========

There are two examples that demonstrate Ibex usage.

The first is 'Simple System' and is part of the Ibex repository.
It demonstrates a minimal system connecting Ibex to some memory with a timer peripheral and is targeted at simulation.
```

## Spec Anchors

- `compliance.rst` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/compliance.rst`
- `Standards Compliance` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/compliance.rst`
- `index.rst` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/index.rst`
- `Introduction to Ibex` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/index.rst`
- `licensing.rst` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/licensing.rst`
- `Licensing` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/licensing.rst`
- `targets.rst` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/targets.rst`
- `Synthesis Targets` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/targets.rst`
- `ASIC Synthesis` (L4) — `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/targets.rst`
- `FPGA Synthesis` (L11) — `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/targets.rst`
- `verification_overview.rst` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/verification_overview.rst`
- `Verification Overview` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/verification_overview.rst`
- `Verification Status` (L9) — `opentitan/hw/vendor/lowrisc_ibex/doc/01_overview/verification_overview.rst`
- `configuration.rst` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/configuration.rst`
- `Ibex Configurations` (L3) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/configuration.rst`
- `Configuration Tool` (L11) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/configuration.rst`
- `Supported Configurations` (L35) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/configuration.rst`
- `examples.rst` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/examples.rst`
- `Examples` (L3) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/examples.rst`
- `Simple System` (L14) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/examples.rst`
- `getting_started.rst` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/getting_started.rst`
- `Getting Started with Ibex` (L3) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/getting_started.rst`
- `index.rst` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/index.rst`
- `Ibex User Guide` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/index.rst`
- `integration.rst` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `Core Integration` (L3) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `Register File` (L10) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `Identification CSRs` (L17) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `Primitives` (L33) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `RTL File List` (L65) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `Instantiation Template` (L86) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `Parameters` (L183) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `Interfaces` (L271) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/integration.rst`
- `system_requirements.rst` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/system_requirements.rst`
- `System and Tool Requirements` (L1) — `opentitan/hw/vendor/lowrisc_ibex/doc/02_user/system_requirements.rst`

## Code Evidence

**DV** (50)
  - `Cosim()`:L44 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim.h`
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
  - `SpikeCosim()`:L36 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
  - `addr_to_mem()`:L82 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
  - `mmio_load()`:L84 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`
  - `mmio_store()`:L113 — `opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc`

## Neighbor Components

- `google_riscv-dv` (482 refs; contains×479, imports_from×3)
- `ibex` (402 refs; contains×310, imports_from×52, instantiates×39)
- `otbn` (221 refs; calls×207, instantiates×11, imports_from×3)
- `riscv-tests` (79 refs; calls×79)
- `prim` (54 refs; instantiates×34, calls×14, imports_from×6)
- `gpio.rs` (27 refs; calls×27)
- `otp_ctrl_descrambling_test.c` (24 refs; calls×24)
- `aes` (22 refs; instantiates×19, imports_from×2, calls×1)
- `clkmgr` (21 refs; instantiates×18, imports_from×3)
- `otp_ctrl` (20 refs; instantiates×15, imports_from×4, calls×1)
- `rom_ctrl` (17 refs; calls×12, instantiates×3, imports_from×2)
- `gpio` (17 refs; calls×11, instantiates×3, imports_from×3)

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

## Retrieval Guidance

- For code-only queries mentioning `lowrisc_ibex`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `lowrisc_ibex`.
