# Hardware Description: spi_device

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`spi_device`** has the following hardware interfaces defined
- **Peripheral Pins for Chip IO**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`spi_device`** has the following hardware interfaces defined

## Identity

- `ip_block`: `spi_device`
- `bridge_edge_count`: 112
- Spec categories: document: 94, component: 41, testplan: 28, theory: 19, interface: 15
- Code categories: rtl: 148, other_code: 35, dv: 28, sva: 22
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/spi_device/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/spi_device/data/spi_device.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`spi_device`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`scan_clk_i`**
- Bus De
…
```

### Peripheral Pins for Chip IO
_Source: `opentitan/hw/ip/spi_device/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/spi_device/data/spi_device.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`spi_device`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`scan_clk_i`**
- Bus Device Interfaces (TL-UL)
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/spi_device/doc/interfaces.md`_

```
| Pin name   | Direction   | Description                                    |
|:-----------|:------------|:-----------------------------------------------|
| sck        | input       | SPI Clock                                      |
| csb        | input       | Chip Select#                                   |
| tpm_csb    | input       | TPM Chip Select#                               |
| sd[3:0]
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/spi_device/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

## Dual-port SRAM Layout

The figure below shows the SRAM layout.
The SRAM begins at `0x1000`, which in the figure is `0x000`.
```

### Initialization
_Source: `opentitan/hw/ip/spi_device/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

## Dual-port SRAM Layout

The figure below shows the SRAM layout.
The SRAM begins at `0x1000`, which in the figure is `0x000`.

![SPI Device Dual-port SRAM Layout](../doc/spid_sram_layout.svg)
```

### Dual-port SRAM Layout
_Source: `opentitan/hw/ip/spi_device/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

## Dual-port SRAM Layout

The figure below shows the SRAM layout.
The SRAM begins at `0x1000`, which in the figure is `0x000`.

![SPI Device Dual-port SRAM Layout](../doc/spid_sram_layout.svg)

In addition to the various buffers for Flash and Passthrough modes, the TPM Read and Write FIFOs are also assigned to the SRAM.
```

### Summary
_Source: `opentitan/hw/ip/spi_device/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/spi_device/data/spi_device.hjson -->
## Summary

| Name                                                     | Offset   |   Length | Description                                     |
|:---------------------------------------------------------|:---------|---------:|:------------------------------------------------|
| spi_device.[`INTR_STATE`]
…
```

### INTR STATE
_Source: `opentitan/hw/ip/spi_device/doc/registers.md`_

```
| spi_device.[`TPM_INT_STATUS`](#tpm_int_status)           | 0x824    |        4 | TPM_INT_STATUS                                  |
| spi_device.[`TPM_DID_VID`](#tpm_did_vid)                 | 0x828    |        4 | TPM_DID/ TPM_VID register                       |
| spi_device.[`TPM_RID`](#tpm_rid)                         | 0x82c    |        4 | TPM_RID                                         |
|
…
```

## Spec Anchors

- `component:spi_device` (L1) — `__graphify_spec_only__/components.md`
- `spi_device.hjson` (L1) — `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `human name` (L6) — `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `one line desc` (L7) — `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `one paragraph desc` (L8) — `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `cip id` (L14) — `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `design spec` (L15) — `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `dv doc` (L16) — `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `hw checklist` (L17) — `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `sw checklist` (L18) — `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `revisions` (L19) — `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `version` (L21) — `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `spi_device_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/spi_device/data/spi_device_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/spi_device/data/spi_device_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/spi_device/data/spi_device_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/spi_device/data/spi_device_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/spi_device/data/spi_device_sec_cm_testplan.hjson`
- `spi_device_testplan.hjson` (L1) — `opentitan/hw/ip/spi_device/data/spi_device_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/spi_device/data/spi_device_testplan.hjson`
- `testpoints` (L13) — `opentitan/hw/ip/spi_device/data/spi_device_testplan.hjson`
- `desc` (L16) — `opentitan/hw/ip/spi_device/data/spi_device_testplan.hjson`
- `stage` (L21) — `opentitan/hw/ip/spi_device/data/spi_device_testplan.hjson`
- `tests` (L22) — `opentitan/hw/ip/spi_device/data/spi_device_testplan.hjson`
- `covergroups` (L368) — `opentitan/hw/ip/spi_device/data/spi_device_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/spi_device/doc/checklist.md`
- `SPI DEVICE Checklist` (L1) — `opentitan/hw/ip/spi_device/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/spi_device/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/spi_device/doc/checklist.md`
- `D2` (L34) — `opentitan/hw/ip/spi_device/doc/checklist.md`
- `D2S` (L76) — `opentitan/hw/ip/spi_device/doc/checklist.md`
- `D3` (L96) — `opentitan/hw/ip/spi_device/doc/checklist.md`
- `Verification Checklist` (L122) — `opentitan/hw/ip/spi_device/doc/checklist.md`
- `V1` (L124) — `opentitan/hw/ip/spi_device/doc/checklist.md`
- `V2` (L174) — `opentitan/hw/ip/spi_device/doc/checklist.md`
- `V2S` (L220) — `opentitan/hw/ip/spi_device/doc/checklist.md`

## Code Evidence

**RTL** (42)
  - `prim_fifo_async_sram_adapter`:L486 — `opentitan\hw\ip\spi_device\rtl\spid_upload.sv`
  - `prim_ram_2p_pkg`:L15 — `opentitan\hw\ip\spi_device\rtl\spid_dpram.sv`
  - `prim_ram_2p_async_adv`:L552 — `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv`
  - `prim_slicer`:L922 — `opentitan\hw\ip\spi_device\rtl\spi_tpm.sv`
  - `prog_passthrough_host.sv`:L1 — `opentitan\hw\ip\spi_device\pre_dv\program\prog_passthrough_host.sv`
  - `spid_common`:L11 — `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv`
  - `prog_passthrough_sw.sv`:L1 — `opentitan\hw\ip\spi_device\pre_dv\program\prog_passthrough_sw.sv`
  - `spiflash.sv`:L1 — `opentitan\hw\ip\spi_device\pre_dv\program\spiflash.sv`
  - `spid_common.sv`:L1 — `opentitan\hw\ip\spi_device\pre_dv\tb\spid_common.sv`
  - `spid_jedec_tb.sv`:L1 — `opentitan\hw\ip\spi_device\pre_dv\tb\spid_jedec_tb.sv`
  - `spid_jedec_tb`:L7 — `opentitan\hw\ip\spi_device\pre_dv\tb\spid_jedec_tb.sv`
  - `spid_jedec`:L1337 — `opentitan\hw\ip\spi_device\rtl\spi_device.sv`
  - `spi_cmdparse`:L1172 — `opentitan\hw\ip\spi_device\rtl\spi_device.sv`
  - `spi_s2p`:L1137 — `opentitan\hw\ip\spi_device\rtl\spi_device.sv`
  - `spi_p2s`:L1152 — `opentitan\hw\ip\spi_device\rtl\spi_device.sv`
  - `spid_passthrough_tb.sv`:L1 — `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv`
  - `tb`:L7 — `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv`
  - `prog_passthrough_host`:L97 — `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv`
  - `prog_passthrough_sw`:L103 — `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv`
  - `spiflash`:L115 — `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv`
**DV** (6)
  - `tb.sv`:L1 — `opentitan\hw\ip\spi_device\dv\tb\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\spi_device\dv\tb\tb.sv`
  - `spi_device_env_pkg`:L10 — `opentitan\hw\ip\spi_device\dv\tests\spi_device_test_pkg.sv`
  - `spi_device_test_pkg`:L11 — `opentitan\hw\ip\spi_device\dv\tb\tb.sv`
  - `spi_device_base_test.sv`:L1 — `opentitan\hw\ip\spi_device\dv\tests\spi_device_base_test.sv`
  - `spi_device_test_pkg.sv`:L1 — `opentitan\hw\ip\spi_device\dv\tests\spi_device_test_pkg.sv`
**SVA** (2)
  - `spi_device_bind.sv`:L1 — `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv`
  - `spi_device_bind`:L5 — `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv`

## Neighbor Components

- `spi_host` (22 refs; imports_from×21, instantiates×1)
- `lowrisc_ibex` (16 refs; instantiates×12, calls×2, imports_from×2)
- `spiflash` (13 refs; calls×13)
- `prim` (12 refs; imports_from×8, instantiates×4)
- `gpio.rs` (11 refs; calls×11)
- `uart` (10 refs; calls×10)
- `pulp_riscv_dbg` (8 refs; instantiates×8)
- `i2c.rs` (7 refs; calls×7)
- `rstmgr` (6 refs; instantiates×5, imports_from×1)
- `rv_plic` (6 refs; instantiates×6)
- `pwrmgr` (5 refs; instantiates×5)
- `spi.rs` (5 refs; imports_from×4, calls×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:spi_device` | `spi_device` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_base_test.sv` | `opentitan\hw\ip\spi_device\dv\tests\spi_device_base_test.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_env_pkg` | `opentitan\hw\ip\spi_device\dv\tests\spi_device_test_pkg.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_test_pkg.sv` | `opentitan\hw\ip\spi_device\dv\tests\spi_device_test_pkg.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_bind.sv` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_bind` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_reg_pkg.sv` | `opentitan\hw\ip\spi_device\rtl\spi_device_reg_pkg.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_reg_top.sv` | `opentitan\hw\ip\spi_device\rtl\spi_device_reg_top.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_reg_top` | `opentitan\hw\ip\spi_device\rtl\spi_device_reg_top.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_pkg.sv` | `opentitan\hw\ip\spi_device\rtl\spi_device_pkg.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device.sv` | `opentitan\hw\ip\spi_device\rtl\spi_device.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device` | `opentitan\hw\ip\spi_device\rtl\spi_device.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_reg_top` | `opentitan\hw\ip\spi_device\rtl\spi_device.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_reg_pkg` | `opentitan\hw\ip\spi_device\rtl\spi_tpm.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_test_pkg` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `prog_passthrough_host.sv` | `opentitan\hw\ip\spi_device\pre_dv\program\prog_passthrough_host.sv` |
| `spec_component_matches_code` | `component:spi_device` | `prog_passthrough_sw.sv` | `opentitan\hw\ip\spi_device\pre_dv\program\prog_passthrough_sw.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_passthrough_tb.sv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `tb` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `prog_passthrough_host` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `prog_passthrough_sw` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spiflash` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_fifo2sram_adapter.sv` | `opentitan\hw\ip\spi_device\rtl\spid_fifo2sram_adapter.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_fifo2sram_adapter` | `opentitan\hw\ip\spi_device\rtl\spid_fifo2sram_adapter.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_readcmd_tb.sv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_readcmd_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `tb` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_readcmd_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `prim_ram_2p_async_adv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_common` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_status_tb.sv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_status_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_status_tb` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_status_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_upload_tb.sv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_upload_tb` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spiflash.sv` | `opentitan\hw\ip\spi_device\pre_dv\program\spiflash.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_jedec_tb.sv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_jedec_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_jedec_tb` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_jedec_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_common.sv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_common.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_tpm_tb.sv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spi_tpm_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_tpm_tb` | `opentitan\hw\ip\spi_device\pre_dv\tb\spi_tpm_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_readbuffer.sv` | `opentitan\hw\ip\spi_device\rtl\spid_readbuffer.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_readbuffer` | `opentitan\hw\ip\spi_device\rtl\spid_readbuffer.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `prim_fifo_async_sram_adapter` | `opentitan\hw\ip\spi_device\rtl\spid_upload.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `prim_ram_2p_pkg` | `opentitan\hw\ip\spi_device\rtl\spid_dpram.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `prim_ram_2p_async_adv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `prim_slicer` | `opentitan\hw\ip\spi_device\rtl\spi_tpm.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `spi_device_bind.sv` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `spi_device_bind` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `tb.sv` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `tb` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `prim_fifo_async_sram_adapter` | `opentitan\hw\ip\spi_device\rtl\spid_upload.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `prim_ram_2p_pkg` | `opentitan\hw\ip\spi_device\rtl\spid_dpram.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `prim_ram_2p_async_adv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `prim_slicer` | `opentitan\hw\ip\spi_device\rtl\spi_tpm.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `spi_device_bind.sv` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `spi_device_bind` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `spi_device_testplan.hjson` | `prim_fifo_async_sram_adapter` | `opentitan\hw\ip\spi_device\rtl\spid_upload.sv` |
| `spec_path_matches_code_path` | `spi_device_testplan.hjson` | `prim_ram_2p_pkg` | `opentitan\hw\ip\spi_device\rtl\spid_dpram.sv` |
| `spec_path_matches_code_path` | `spi_device_testplan.hjson` | `prim_ram_2p_async_adv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_path_matches_code_path` | `spi_device_testplan.hjson` | `prim_slicer` | `opentitan\hw\ip\spi_device\rtl\spi_tpm.sv` |

## Retrieval Guidance

- For code-only queries mentioning `spi_device`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `spi_device`.
