# Hardware Description: tlul

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **TLUL XBAR DV document**: * **DV**
- **Goals**: * **DV**
- **Current status**: * **DV**

## Identity

- `ip_block`: `tlul`
- `bridge_edge_count`: 80
- Spec categories: document: 70, component: 41, testplan: 14, theory: 1
- Code categories: rtl: 142, sva: 6, package: 2
- Bridge relations: spec_component_matches_code: 40, spec_path_matches_code_path: 40

## Spec Excerpts

### TLUL XBAR DV document
_Source: `opentitan/hw/ip/tlul/doc/dv/README.md`_

```
# TLUL XBAR DV document


## Goals
* **DV**
  * Verify all TLUL XBAR IP features by running dynamic simulations with a SV/UVM based testbench
  * Develop and run all tests based on the [testplan](#testplan) below towards closing code and functional coverage on the IP and all of its sub-modules
* **FPV**
```

### Goals
_Source: `opentitan/hw/ip/tlul/doc/dv/README.md`_

```
# TLUL XBAR DV document


## Goals
* **DV**
  * Verify all TLUL XBAR IP features by running dynamic simulations with a SV/UVM based testbench
  * Develop and run all tests based on the [testplan](#testplan) below towards closing code and functional coverage on the IP and all of its sub-modules
* **FPV**
  * Verify TileLink device protocol compliance with an SVA based testbench

## Current status
```

### Current status
_Source: `opentitan/hw/ip/tlul/doc/dv/README.md`_

```
## Goals
* **DV**
  * Verify all TLUL XBAR IP features by running dynamic simulations with a SV/UVM based testbench
  * Develop and run all tests based on the [testplan](#testplan) below towards closing code and functional coverage on the IP and all of its sub-modules
* **FPV**
  * Verify TileLink device protocol compliance with an SVA based testbench

## Current status
* [Design & verification st
…
```

### TL-UL Protocol Checker
_Source: `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`_

```
# TL-UL Protocol Checker

# TileLink-UL Protocol Checker


## **Overview**

This document details the protocol checker
```

### TileLink-UL Protocol Checker
_Source: `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`_

```
# TL-UL Protocol Checker

# TileLink-UL Protocol Checker


## **Overview**

This document details the protocol checker
[tlul_assert.sv](https://github.com/lowRISC/opentitan/blob/master/hw/ip/tlul/rtl/tlul_assert.sv)
for TL-UL (TileLink Uncached Lightweight), based on
```

### Overview
_Source: `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`_

```
# TL-UL Protocol Checker

# TileLink-UL Protocol Checker


## **Overview**

This document details the protocol checker
[tlul_assert.sv](https://github.com/lowRISC/opentitan/blob/master/hw/ip/tlul/rtl/tlul_assert.sv)
for TL-UL (TileLink Uncached Lightweight), based on
[TileLink specification version 1.7.1](https://sifive.cdn.prismic.io/sifive%2F57f93ecf-2c42-46f7-9818-bcdd7d39400a_tilelink-spec-1.7
…
```

### Bus Specification
_Source: `opentitan/hw/ip/tlul/README.md`_

```
# Bus Specification

# Overview

This document specifies the bus functionality within a Comportable top level
system. This includes the bus protocol and all hardware IP that supports
creating the network on chip within that framework.
```

### Overview
_Source: `opentitan/hw/ip/tlul/README.md`_

```
# Bus Specification

# Overview

This document specifies the bus functionality within a Comportable top level
system. This includes the bus protocol and all hardware IP that supports
creating the network on chip within that framework.

## Features
```

## Spec Anchors

- `component:tlul` (L1) — `__graphify_spec_only__/components.md`
- `tlul.prj.hjson` (L1) — `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `design spec` (L7) — `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `dv doc` (L8) — `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `hw checklist` (L9) — `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `revisions` (L10) — `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `version` (L12) — `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `life stage` (L13) — `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `design stage` (L14) — `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `verification stage` (L15) — `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `commit id` (L16) — `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `notes` (L17) — `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `tlul_testplan.hjson` (L1) — `opentitan/hw/ip/tlul/data/tlul_testplan.hjson`
- `testpoints` (L8) — `opentitan/hw/ip/tlul/data/tlul_testplan.hjson`
- `desc` (L11) — `opentitan/hw/ip/tlul/data/tlul_testplan.hjson`
- `stage` (L12) — `opentitan/hw/ip/tlul/data/tlul_testplan.hjson`
- `si stage` (L13) — `opentitan/hw/ip/tlul/data/tlul_testplan.hjson`
- `tests` (L14) — `opentitan/hw/ip/tlul/data/tlul_testplan.hjson`
- `README.md` (L1) — `opentitan/hw/ip/tlul/doc/dv/README.md`
- `TLUL XBAR DV document` (L1) — `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Goals` (L4) — `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Current status` (L11) — `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Design features` (L16) — `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Testbench architecture` (L29) — `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Block diagram` (L32) — `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Top level testbench` (L35) — `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Common DV utility components` (L41) — `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Global types & methods` (L46) — `opentitan/hw/ip/tlul/doc/dv/README.md`
- `TL agent` (L56) — `opentitan/hw/ip/tlul/doc/dv/README.md`
- `TlulProtocolChecker.md` (L1) — `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`
- `TL-UL Protocol Checker` (L1) — `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`
- `TileLink-UL Protocol Checker` (L3) — `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`
- `Overview` (L6) — `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`
- `Request Channel Channel A` (L42) — `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`
- `Response Channel Channel D` (L136) — `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`

## Code Evidence

**RTL** (44)
  - `prim_secded_inv_39_32_enc`:L17 — `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv`
  - `prim_secded_inv_39_32_dec`:L18 — `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv`
  - `prim_secded_inv_64_57_enc`:L24 — `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv`
  - `prim_secded_inv_64_57_dec`:L25 — `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_chk.sv`
  - `tlul_err`:L167 — `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv`
  - `prim_fifo_async`:L28 — `opentitan\hw\ip\tlul\rtl\tlul_fifo_async.sv`
  - `tb.sv`:L1 — `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv`
  - `xbar_base_test.sv`:L1 — `opentitan\hw\ip\tlul\generic_dv\tests\xbar_base_test.sv`
  - `xbar_error_test.sv`:L1 — `opentitan\hw\ip\tlul\generic_dv\tests\xbar_error_test.sv`
  - `sram2tlul.sv`:L1 — `opentitan\hw\ip\tlul\rtl\sram2tlul.sv`
  - `sram2tlul`:L12 — `opentitan\hw\ip\tlul\rtl\sram2tlul.sv`
  - `tlul_adapter_dmi.sv`:L1 — `opentitan\hw\ip\tlul\rtl\tlul_adapter_dmi.sv`
  - `tlul_adapter_dmi`:L11 — `opentitan\hw\ip\tlul\rtl\tlul_adapter_dmi.sv`
  - `tlul_adapter_host.sv`:L1 — `opentitan\hw\ip\tlul\rtl\tlul_adapter_host.sv`
  - `tlul_adapter_host`:L24 — `opentitan\hw\ip\tlul\rtl\tlul_adapter_host.sv`
  - `tlul_adapter_racl.sv`:L1 — `opentitan\hw\ip\tlul\rtl\tlul_adapter_racl.sv`
  - `tlul_adapter_racl`:L14 — `opentitan\hw\ip\tlul\rtl\tlul_adapter_racl.sv`
  - `tlul_adapter_reg.sv`:L1 — `opentitan\hw\ip\tlul\rtl\tlul_adapter_reg.sv`
  - `tlul_adapter_reg`:L95 — `opentitan\hw\ip\tlul\rtl\tlul_adapter_reg.sv`
**SVA** (4)
  - `tlul_assert.sv`:L1 — `opentitan\hw\ip\tlul\rtl\tlul_assert.sv`
  - `tlul_assert`:L10 — `opentitan\hw\ip\tlul\rtl\tlul_assert.sv`
  - `tlul_assert_multiple.sv`:L1 — `opentitan\hw\ip\tlul\rtl\tlul_assert_multiple.sv`
  - `tlul_assert_multiple`:L7 — `opentitan\hw\ip\tlul\rtl\tlul_assert_multiple.sv`
**PACKAGE** (2)
  - `xbar_test_pkg.sv`:L1 — `opentitan\hw\ip\tlul\generic_dv\tests\xbar_test_pkg.sv`
  - `xbar_env_pkg`:L11 — `opentitan\hw\ip\tlul\generic_dv\tests\xbar_test_pkg.sv`

## Neighbor Components

- `rv_core_ibex` (15 refs; imports_from×9, instantiates×6)
- `prim` (8 refs; instantiates×8)
- `lowrisc_ibex` (7 refs; instantiates×4, imports_from×3)
- `rv_plic` (6 refs; instantiates×6)
- `pulp_riscv_dbg` (5 refs; instantiates×5)
- `otbn` (5 refs; instantiates×5)
- `flash_ctrl` (5 refs; instantiates×5)
- `soc_proxy` (2 refs; instantiates×2)
- `spi_device` (2 refs; instantiates×2)
- `aes` (1 refs; instantiates×1)
- `pwrmgr` (1 refs; imports_from×1)
- `gpio` (1 refs; imports_from×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_sram_racl.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram_racl.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram_racl.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_racl` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram_racl.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_reg_racl.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_reg_racl.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_reg_racl` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_reg_racl.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_request_loopback.sv` | `opentitan\hw\ip\tlul\rtl\tlul_request_loopback.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_request_loopback` | `opentitan\hw\ip\tlul\rtl\tlul_request_loopback.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_assert_multiple.sv` | `opentitan\hw\ip\tlul\rtl\tlul_assert_multiple.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_assert_multiple` | `opentitan\hw\ip\tlul\rtl\tlul_assert_multiple.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_data_integ_dec.sv` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_data_integ_dec` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_data_integ_enc.sv` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_data_integ_enc` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_err` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_host.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_host.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_host` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_host.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_racl.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_racl.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_racl` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_racl.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_shim.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_shim.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_sram.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_sram` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_sram_byte` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_cmd_intg_chk.sv` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_chk.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_cmd_intg_chk` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_chk.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_cmd_intg_gen.sv` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_cmd_intg_gen` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_rsp_intg_chk.sv` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_chk.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_rsp_intg_chk` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_chk.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_rsp_intg_gen.sv` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_gen.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_rsp_intg_gen` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_gen.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_dmi.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_dmi.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_dmi` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_dmi.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_reg.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_reg.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_reg` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_reg.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_vh.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_vh.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_vh` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_vh.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_fifo_async.sv` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_async.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_fifo_async` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_async.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_fifo_sync.sv` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_sync.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_fifo_sync` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_sync.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `prim_secded_inv_39_32_enc` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `prim_secded_inv_39_32_dec` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `prim_secded_inv_64_57_enc` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `prim_secded_inv_64_57_dec` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_chk.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `tlul_err` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `prim_fifo_async` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_async.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `tb.sv` | `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `tb` | `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `prim_secded_inv_39_32_enc` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `prim_secded_inv_39_32_dec` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `prim_secded_inv_64_57_enc` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `prim_secded_inv_64_57_dec` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_chk.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `tlul_err` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `prim_fifo_async` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_async.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `tb` | `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_secded_inv_39_32_enc` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_secded_inv_39_32_dec` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_secded_inv_64_57_enc` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_secded_inv_64_57_dec` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_chk.sv` |

## Retrieval Guidance

- For code-only queries mentioning `tlul`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `tlul`.
