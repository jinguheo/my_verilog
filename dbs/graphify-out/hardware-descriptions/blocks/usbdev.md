# Hardware Description: usbdev

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`usbdev`** has the following hardware interfaces defined
- **Peripheral Pins for Chip IO**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`usbdev`** has the following hardware interfaces defined

## Identity

- `ip_block`: `usbdev`
- `bridge_edge_count`: 120
- Spec categories: document: 105, component: 41, testplan: 29, theory: 19, interface: 16
- Code categories: rtl: 76, dv: 75, sva: 24
- Bridge relations: spec_path_matches_code_path: 80, spec_component_matches_code: 40

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/usbdev/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/usbdev/data/usbdev.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`usbdev`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_aon_i`**
- Bus Device Interfac
…
```

### Peripheral Pins for Chip IO
_Source: `opentitan/hw/ip/usbdev/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/usbdev/data/usbdev.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`usbdev`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_aon_i`**
- Bus Device Interfaces (TL-UL): **`tl`**
-
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/usbdev/doc/interfaces.md`_

```
## Peripheral Pins for Chip IO

| Pin name   | Direction   | Description         |
|:-----------|:------------|:--------------------|
| sense      | input       | USB host VBUS sense |
| usb_dp     | inout       | USB data D+         |
| usb_dn     | inout       | USB data D-         |

## [Inter-Module Signals](https://opentitan.org/book/doc/contributing/hw/comportability/index.html#inter-signal-
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/usbdev/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

The basic hardware initialization is to (in any order) configure the physical interface for the implementation via the [`phy_config`](registers.md#phy_config) register, fill the Available Buffer FIFO, enable IN and OUT endpoints with ID 0 (this is the control endpoint that the host will use to configure the interface), enable reception of SETUP and OUT pack
…
```

### Initialization
_Source: `opentitan/hw/ip/usbdev/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

The basic hardware initialization is to (in any order) configure the physical interface for the implementation via the [`phy_config`](registers.md#phy_config) register, fill the Available Buffer FIFO, enable IN and OUT endpoints with ID 0 (this is the control endpoint that the host will use to configure the interface), enable reception of SETUP and OUT pack
…
```

### Buffers
_Source: `opentitan/hw/ip/usbdev/doc/programmers_guide.md`_

```
When a Set Address request is received, the device ID received must be stored in the [`usbctrl.device_address`](registers.md#usbctrl) register.
Note that device 0 is used for the entire control transaction setting the new device ID, so writing the new ID to the register should not be done until the ACK for the Status stage has been received (see [USB 2.0 specification](https://www.usb.org/document
…
```

### Summary
_Source: `opentitan/hw/ip/usbdev/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/usbdev/data/usbdev.hjson -->
## Summary

| Name                                         | Offset   |   Length | Description                                                                |
|:---------------------------------------------|:---------|---------:|:---------------------------------------------------------------------------|
| usb
…
```

### INTR STATE
_Source: `opentitan/hw/ip/usbdev/doc/registers.md`_

```
| usbdev.[`wake_events`](#wake_events)         | 0x94     |        4 | USB wake module events and debug                                           |
| usbdev.[`fifo_ctrl`](#fifo_ctrl)             | 0x98     |        4 | FIFO control register                                                      |
| usbdev.[`count_out`](#count_out)             | 0x9c     |        4 | Counter for OUT side USB events.
…
```

## Spec Anchors

- `component:usbdev` (L1) — `__graphify_spec_only__/components.md`
- `usbdev.hjson` (L1) — `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `human name` (L6) — `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `one line desc` (L7) — `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `one paragraph desc` (L8) — `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `cip id` (L16) — `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `design spec` (L17) — `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `dv doc` (L18) — `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `hw checklist` (L19) — `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `sw checklist` (L20) — `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `version` (L21) — `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `life stage` (L22) — `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `usbdev_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/usbdev/data/usbdev_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/usbdev/data/usbdev_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/usbdev/data/usbdev_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/usbdev/data/usbdev_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/usbdev/data/usbdev_sec_cm_testplan.hjson`
- `usbdev_testplan.hjson` (L1) — `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `import testplans` (L7) — `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `testpoints` (L13) — `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `desc` (L16) — `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `stage` (L43) — `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `tests` (L44) — `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `Background` (L1020) — `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `covergroups` (L1276) — `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/usbdev/doc/checklist.md`
- `USB Device Checklist` (L1) — `opentitan/hw/ip/usbdev/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/usbdev/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/usbdev/doc/checklist.md`
- `D2` (L32) — `opentitan/hw/ip/usbdev/doc/checklist.md`
- `D2S` (L74) — `opentitan/hw/ip/usbdev/doc/checklist.md`
- `D3` (L94) — `opentitan/hw/ip/usbdev/doc/checklist.md`
- `Verification Checklist` (L120) — `opentitan/hw/ip/usbdev/doc/checklist.md`
- `V1` (L122) — `opentitan/hw/ip/usbdev/doc/checklist.md`
- `V2` (L172) — `opentitan/hw/ip/usbdev/doc/checklist.md`

## Code Evidence

**RTL** (38)
  - `usbdev.sv`:L1 — `opentitan\hw\ip\usbdev\rtl\usbdev.sv`
  - `usbdev`:L9 — `opentitan\hw\ip\usbdev\rtl\usbdev.sv`
  - `usbdev_pkg`:L10 — `opentitan\hw\ip\usbdev\rtl\usbdev_aon_wake.sv`
  - `usbdev_reg_pkg`:L29 — `opentitan\hw\ip\usbdev\rtl\usbdev_reg_top.sv`
  - `usbdev_usbif`:L583 — `opentitan\hw\ip\usbdev\rtl\usbdev.sv`
  - `usbdev_reg_top`:L893 — `opentitan\hw\ip\usbdev\rtl\usbdev.sv`
  - `usbdev_iomux`:L1193 — `opentitan\hw\ip\usbdev\rtl\usbdev.sv`
  - `usbdev_counter`:L1333 — `opentitan\hw\ip\usbdev\rtl\usbdev.sv`
  - `usbdev_aon_wake.sv`:L1 — `opentitan\hw\ip\usbdev\rtl\usbdev_aon_wake.sv`
  - `usbdev_aon_wake`:L10 — `opentitan\hw\ip\usbdev\rtl\usbdev_aon_wake.sv`
  - `usbdev_counter.sv`:L1 — `opentitan\hw\ip\usbdev\rtl\usbdev_counter.sv`
  - `usbdev_counter`:L16 — `opentitan\hw\ip\usbdev\rtl\usbdev_counter.sv`
  - `usbdev_iomux.sv`:L1 — `opentitan\hw\ip\usbdev\rtl\usbdev_iomux.sv`
  - `usbdev_iomux`:L10 — `opentitan\hw\ip\usbdev\rtl\usbdev_iomux.sv`
  - `usbdev_linkstate.sv`:L1 — `opentitan\hw\ip\usbdev\rtl\usbdev_linkstate.sv`
  - `usbdev_linkstate`:L10 — `opentitan\hw\ip\usbdev\rtl\usbdev_linkstate.sv`
  - `usbdev_pkg.sv`:L1 — `opentitan\hw\ip\usbdev\rtl\usbdev_pkg.sv`
  - `usbdev_reg_pkg.sv`:L1 — `opentitan\hw\ip\usbdev\rtl\usbdev_reg_pkg.sv`
  - `usbdev_reg_top.sv`:L1 — `opentitan\hw\ip\usbdev\rtl\usbdev_reg_top.sv`
  - `usbdev_reg_top`:L9 — `opentitan\hw\ip\usbdev\rtl\usbdev_reg_top.sv`
**DV** (10)
  - `tb.sv`:L1 — `opentitan\hw\ip\usbdev\dv\tb\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\usbdev\dv\tb\tb.sv`
  - `usbdev_env_pkg`:L9 — `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv`
  - `usbdev_test_pkg`:L10 — `opentitan\hw\ip\usbdev\dv\tb\tb.sv`
  - `usb20_if`:L93 — `opentitan\hw\ip\usbdev\dv\tb\tb.sv`
  - `usb20_block_if`:L98 — `opentitan\hw\ip\usbdev\dv\tb\tb.sv`
  - `usb20_usbdpi`:L203 — `opentitan\hw\ip\usbdev\dv\tb\tb.sv`
  - `usbdev_osc_tuning_if`:L278 — `opentitan\hw\ip\usbdev\dv\tb\tb.sv`
  - `usbdev_base_test.sv`:L1 — `opentitan\hw\ip\usbdev\dv\tests\usbdev_base_test.sv`
  - `usbdev_test_pkg.sv`:L1 — `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv`
**SVA** (2)
  - `usbdev_bind.sv`:L1 — `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv`
  - `usbdev_bind`:L5 — `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv`

## Neighbor Components

- `rv_plic` (6 refs; instantiates×6)
- `lowrisc_ibex` (4 refs; instantiates×3, imports_from×1)
- `pulp_riscv_dbg` (4 refs; instantiates×4)
- `pinmux` (4 refs; instantiates×4)
- `pwrmgr` (3 refs; instantiates×3)
- `rstmgr` (1 refs; imports_from×1)
- `clkmgr` (1 refs; instantiates×1)
- `rv_core_ibex` (1 refs; instantiates×1)
- `otp_ctrl` (1 refs; imports_from×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:usbdev` | `usbdev` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_base_test.sv` | `opentitan\hw\ip\usbdev\dv\tests\usbdev_base_test.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_env_pkg` | `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_test_pkg.sv` | `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_linkstate.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_linkstate.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_linkstate` | `opentitan\hw\ip\usbdev\rtl\usbdev_linkstate.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_pkg` | `opentitan\hw\ip\usbdev\rtl\usbdev_aon_wake.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_aon_wake.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_aon_wake.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_aon_wake` | `opentitan\hw\ip\usbdev\rtl\usbdev_aon_wake.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_bind.sv` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_bind` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_reg_pkg` | `opentitan\hw\ip\usbdev\rtl\usbdev_reg_top.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_counter.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_counter.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_counter` | `opentitan\hw\ip\usbdev\rtl\usbdev_counter.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_reg_pkg.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_reg_pkg.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_reg_top.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_reg_top.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_reg_top` | `opentitan\hw\ip\usbdev\rtl\usbdev_reg_top.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_iomux.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_iomux.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_iomux` | `opentitan\hw\ip\usbdev\rtl\usbdev_iomux.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_usbif.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_usbif.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_usbif` | `opentitan\hw\ip\usbdev\rtl\usbdev_usbif.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_linkstate` | `opentitan\hw\ip\usbdev\rtl\usbdev_usbif.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_pkg.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_pkg.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev` | `opentitan\hw\ip\usbdev\rtl\usbdev.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_usbif` | `opentitan\hw\ip\usbdev\rtl\usbdev.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_reg_top` | `opentitan\hw\ip\usbdev\rtl\usbdev.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_iomux` | `opentitan\hw\ip\usbdev\rtl\usbdev.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_counter` | `opentitan\hw\ip\usbdev\rtl\usbdev.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_test_pkg` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_osc_tuning_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_nb_out_pe.sv` | `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_out_pe.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_nb_out_pe` | `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_out_pe.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_nb_in_pe.sv` | `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_in_pe.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_nb_in_pe` | `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_in_pe.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_consts_pkg.sv` | `opentitan\hw\ip\usbdev\rtl\usb_consts_pkg.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_tx_mux.sv` | `opentitan\hw\ip\usbdev\rtl\usb_fs_tx_mux.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_tx_mux` | `opentitan\hw\ip\usbdev\rtl\usb_fs_tx_mux.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_nb_pe` | `opentitan\hw\ip\usbdev\rtl\usbdev_usbif.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_nb_pe.sv` | `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_pe.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `usbdev_bind.sv` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `usbdev_bind` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `tb.sv` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `tb` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `usbdev_env_pkg` | `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `usbdev_test_pkg` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `usb20_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `usb20_block_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `usbdev_bind.sv` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `usbdev_bind` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `usbdev_env_pkg` | `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `usbdev_test_pkg` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `usb20_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `usb20_block_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_testplan.hjson` | `usbdev_bind.sv` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `usbdev_testplan.hjson` | `usbdev_bind` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `usbdev_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_testplan.hjson` | `tb` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |

## Retrieval Guidance

- For code-only queries mentioning `usbdev`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `usbdev`.
