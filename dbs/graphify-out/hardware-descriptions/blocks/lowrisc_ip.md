# Hardware Description: lowrisc_ip

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **DVSim design doc**: An industry-grade EDA tool flow manager / build and run system that strives to achieve a bug-free Silicon must support several [usecases](#goals).
- **Context**: An industry-grade EDA tool flow manager / build and run system that strives to achieve a bug-free Silicon must support several [usecases](#goals).
- **Goals**: Hardware companies often invest in engineering resources to build and maintain custom tooling to manage EDA tool flows.

## Identity

- `ip_block`: `lowrisc_ip`
- `bridge_edge_count`: 48
- Spec categories: document: 54, testplan: 27
- Code categories: dv: 114, other_code: 46, rtl: 12
- Bridge relations: spec_path_matches_code_path: 48

## Spec Excerpts

### DVSim design doc
_Source: `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`_

```
# DVSim design doc

An industry-grade EDA tool flow manager / build and run system that strives to achieve a bug-free Silicon must support several [usecases](#goals).
The terminology used in this document is covered in the [glossary](./glossary.md).

# Context

Hardware companies often invest in engineering resources to build and maintain custom tooling to manage EDA tool flows.
```

### Context
_Source: `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`_

```
# DVSim design doc

An industry-grade EDA tool flow manager / build and run system that strives to achieve a bug-free Silicon must support several [usecases](#goals).
The terminology used in this document is covered in the [glossary](./glossary.md).

# Context

Hardware companies often invest in engineering resources to build and maintain custom tooling to manage EDA tool flows.
It enables them to
…
```

### Goals
_Source: `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`_

```
Hardware companies often invest in engineering resources to build and maintain custom tooling to manage EDA tool flows.
It enables them to deploy and scale EDA workloads efficiently across their projects onto their compute infrastructure, monitor their execution, assess success and generate and publish queryable report to track the overall health and progress of their projects.
These are often pro
…
```

### DVSIM Testplanner tool
_Source: `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`_

```
# DVSIM Testplanner tool

`testplanner` is a Python based tool for parsing testplans written in Hjson format into a data structure that can be used for:
* Expanding the testplan inline within the DV document as a table;
* Annotating the simulation results with testplan entries for a document driven DV execution;

Please see [DV methodology](../../../doc/contributing/dv/methodology/README.md#testpl
…
```

### Hjson testplan
_Source: `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`_

```
`testplanner` is a Python based tool for parsing testplans written in Hjson format into a data structure that can be used for:
* Expanding the testplan inline within the DV document as a table;
* Annotating the simulation results with testplan entries for a document driven DV execution;

Please see [DV methodology](../../../doc/contributing/dv/methodology/README.md#testplan) for more details on th
…
```

### Testpoints
_Source: `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`_

```
Please see [DV methodology](../../../doc/contributing/dv/methodology/README.md#testplan) for more details on the rationale and motivation for writing and maintaining testplans in a machine-parseable format (`Hjson`).
This document will focus on the anatomy of an Hjson testplan, the list of features supported and some of the ways of using the tool.

## Hjson testplan

A testplan consists of a list
…
```

### Glossary of Terms
_Source: `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`_

```
# Glossary of Terms

## Build

"Build" refers to the invocation of the EDA tool to compile and elaborate the provided top levels which results in the generation of an executable / database and all of its pre-requisites.
In OpenTitan, the build stage broadly performs the following steps:
- Create the build directory.
- Execute an pre-build utility scripts, if provided.
```

### Build
_Source: `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`_

```
# Glossary of Terms

## Build

"Build" refers to the invocation of the EDA tool to compile and elaborate the provided top levels which results in the generation of an executable / database and all of its pre-requisites.
In OpenTitan, the build stage broadly performs the following steps:
- Create the build directory.
- Execute an pre-build utility scripts, if provided.
- Invoke FuseSoC (or equivale
…
```

## Spec Anchors

- `design_doc.md` (L1) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `DVSim design doc` (L1) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `Context` (L6) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `Goals` (L16) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `Non-goals` (L107) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `Architecture` (L111) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `EDA tool flow steps` (L115) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `Flow-specific Makefile` (L127) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `DUT configuration` (L138) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `Parser stage` (L144) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `Mode object creation stage` (L150) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `glossary.md` (L1) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `Glossary of Terms` (L1) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `Build` (L3) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `Build configuration` (L13) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `Build modes` (L15) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `Compute infrastructure` (L23) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `Design level` (L30) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `DUT` (L55) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `DUT configuration file` (L60) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `EDA tool flow` (L66) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `Filelist` (L84) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `testplanner.md` (L1) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `DVSIM Testplanner tool` (L1) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Hjson testplan` (L10) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Testpoints` (L14) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Covergroups` (L111) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Import shared testplans` (L141) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Example sources` (L206) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Limitations` (L216) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Usage examples` (L222) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Standalone tool invocations` (L224) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `APIs for external tools` (L275) — `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`

## Code Evidence

**DV** (50)
  - `clk_if.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_if.sv`
  - `clk_rst_if.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_rst_if.sv`
  - `common_ifs_pkg.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\common_ifs_pkg.sv`
  - `entropy_subsys_fifo_exception_if.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_if.sv`
  - `entropy_subsys_fifo_exception_pkg.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_pkg.sv`
  - `pins_if.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\pins_if.sv`
  - `rst_shadowed_if.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\rst_shadowed_if.sv`
  - `csr_seq_lib.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\csr_utils\csr_seq_lib.sv`
  - `csr_utils_pkg.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\csr_utils\csr_utils_pkg.sv`
  - `csr_excl_item.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\csr_excl_item.sv`
  - `dv_base_lockable_field_cov.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_lockable_field_cov.sv`
  - `dv_base_mem.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_mem.sv`
  - `dv_base_mubi_cov.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_mubi_cov.sv`
  - `dv_base_reg.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_reg.sv`
  - `dv_base_reg_block.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_reg_block.sv`
  - `dv_base_reg_field.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_reg_field.sv`
  - `dv_base_reg_map.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_reg_map.sv`
  - `dv_base_reg_pkg.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_reg_pkg.sv`
  - `dv_base_shadowed_field_cov.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_shadowed_field_cov.sv`
  - `dv_base_agent.sv`:L1 — `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_agent.sv`

## Neighbor Components

- `verilator_sim_ctrl.cc` (26 refs; contains×26)
- `lowrisc_ibex` (8 refs; imports_from×8)
- `ibex` (2 refs; imports_from×2)
- `verilator_sim_ctrl.h` (2 refs; contains×2)
- `rv_core_ibex` (1 refs; imports_from×1)
- `jtag_rv_debugger_pkg.sv` (1 refs; imports_from×1)
- `lc_ctrl` (1 refs; imports_from×1)
- `sim_ctrl_extension.h` (1 refs; contains×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `design_doc.md` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `clk_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_if.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `clk_rst_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_rst_if.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `common_ifs_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\common_ifs_pkg.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `entropy_subsys_fifo_exception_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_if.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `entropy_subsys_fifo_exception_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_pkg.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `pins_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\pins_if.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `rst_shadowed_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\rst_shadowed_if.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `csr_seq_lib.sv` | `ibex\vendor\lowrisc_ip\dv\sv\csr_utils\csr_seq_lib.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `clk_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_if.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `clk_rst_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_rst_if.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `common_ifs_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\common_ifs_pkg.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `entropy_subsys_fifo_exception_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_if.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `entropy_subsys_fifo_exception_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_pkg.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `pins_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\pins_if.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `rst_shadowed_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\rst_shadowed_if.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `csr_seq_lib.sv` | `ibex\vendor\lowrisc_ip\dv\sv\csr_utils\csr_seq_lib.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `clk_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_if.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `clk_rst_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_rst_if.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `common_ifs_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\common_ifs_pkg.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `entropy_subsys_fifo_exception_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_if.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `entropy_subsys_fifo_exception_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_pkg.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `pins_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\pins_if.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `rst_shadowed_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\rst_shadowed_if.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `csr_seq_lib.sv` | `ibex\vendor\lowrisc_ip\dv\sv\csr_utils\csr_seq_lib.sv` |

## Retrieval Guidance

- For code-only queries mentioning `lowrisc_ip`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `lowrisc_ip`.
