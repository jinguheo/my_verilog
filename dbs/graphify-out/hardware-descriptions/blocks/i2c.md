# Hardware Description: i2c

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`i2c`** has the following hardware interfaces defined
- **Peripheral Pins for Chip IO**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`i2c`** has the following hardware interfaces defined

## Identity

- `ip_block`: `i2c`
- `bridge_edge_count`: 112
- Spec categories: document: 87, component: 41, testplan: 30, theory: 19, interface: 16
- Code categories: rtl: 64, dv: 47, sva: 44
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/i2c/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/i2c/data/i2c.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`i2c`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`tl`
…
```

### Peripheral Pins for Chip IO
_Source: `opentitan/hw/ip/i2c/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/i2c/data/i2c.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`i2c`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`tl`**
- Bus Host Interface
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/i2c/doc/interfaces.md`_

```
## Peripheral Pins for Chip IO

| Pin name   | Direction   | Description            |
|:-----------|:------------|:-----------------------|
| sda        | inout       | Serial input data bit  |
| scl        | inout       | Serial input clock bit |

## [Inter-Module Signals](https://opentitan.org/book/doc/contributing/hw/comportability/index.html#inter-signal-handling)

| Port Name     | Package::S
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/i2c/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

After reset, the initialization of the I2C HWIP primarily consists of four steps:
1. Timing parameter initialization
1. FIFO reset and configuration
1. Interrupt configuration
```

### Initialization
_Source: `opentitan/hw/ip/i2c/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

After reset, the initialization of the I2C HWIP primarily consists of four steps:
1. Timing parameter initialization
1. FIFO reset and configuration
1. Interrupt configuration
1. Enable I2C Controller or Target functionality
```

### Timing Parameter Tuning Algorithm
_Source: `opentitan/hw/ip/i2c/doc/programmers_guide.md`_

```
## Initialization

After reset, the initialization of the I2C HWIP primarily consists of four steps:
1. Timing parameter initialization
1. FIFO reset and configuration
1. Interrupt configuration
1. Enable I2C Controller or Target functionality

### Timing Parameter Tuning Algorithm

Of the four initialization steps, the timing parameter initialization is the most involved.  With so many timing par
…
```

### Summary
_Source: `opentitan/hw/ip/i2c/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/i2c/data/i2c.hjson -->
## Summary

| Name                                                          | Offset   |   Length | Description                                                                                               |
|:--------------------------------------------------------------|:---------|---------:|:-----------------------
…
```

### INTR STATE
_Source: `opentitan/hw/ip/i2c/doc/registers.md`_

```
| i2c.[`TARGET_TIMEOUT_CTRL`](#target_timeout_ctrl)             | 0x64     |        4 | I2C target internal stretching timeout control.                                                           |
| i2c.[`TARGET_NACK_COUNT`](#target_nack_count)                 | 0x68     |        4 | Number of times the I2C target has NACK'ed a new transaction since the last read of this register.        |
| i2c.[`
…
```

## Spec Anchors

- `component:i2c` (L1) — `__graphify_spec_only__/components.md`
- `i2c.hjson` (L1) — `opentitan/hw/ip/i2c/data/i2c.hjson`
- `human name` (L7) — `opentitan/hw/ip/i2c/data/i2c.hjson`
- `one line desc` (L8) — `opentitan/hw/ip/i2c/data/i2c.hjson`
- `one paragraph desc` (L9) — `opentitan/hw/ip/i2c/data/i2c.hjson`
- `cip id` (L16) — `opentitan/hw/ip/i2c/data/i2c.hjson`
- `design spec` (L17) — `opentitan/hw/ip/i2c/data/i2c.hjson`
- `dv doc` (L18) — `opentitan/hw/ip/i2c/data/i2c.hjson`
- `hw checklist` (L19) — `opentitan/hw/ip/i2c/data/i2c.hjson`
- `sw checklist` (L20) — `opentitan/hw/ip/i2c/data/i2c.hjson`
- `revisions` (L21) — `opentitan/hw/ip/i2c/data/i2c.hjson`
- `version` (L23) — `opentitan/hw/ip/i2c/data/i2c.hjson`
- `i2c_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/i2c/data/i2c_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/i2c/data/i2c_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/i2c/data/i2c_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/i2c/data/i2c_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/i2c/data/i2c_sec_cm_testplan.hjson`
- `i2c_testplan.hjson` (L1) — `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `testpoints` (L11) — `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `desc` (L17) — `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `Stimulus` (L21) — `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `Checking` (L30) — `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `stage` (L35) — `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `tests` (L36) — `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `covergroups` (L955) — `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/i2c/doc/checklist.md`
- `I2C Checklist` (L1) — `opentitan/hw/ip/i2c/doc/checklist.md`
- `Design Checklist` (L8) — `opentitan/hw/ip/i2c/doc/checklist.md`
- `D1` (L10) — `opentitan/hw/ip/i2c/doc/checklist.md`
- `D2` (L34) — `opentitan/hw/ip/i2c/doc/checklist.md`
- `D2S` (L76) — `opentitan/hw/ip/i2c/doc/checklist.md`
- `D3` (L96) — `opentitan/hw/ip/i2c/doc/checklist.md`
- `Verification Checklist` (L122) — `opentitan/hw/ip/i2c/doc/checklist.md`
- `V1` (L124) — `opentitan/hw/ip/i2c/doc/checklist.md`

## Code Evidence

**RTL** (29)
  - `i2c_pkg`:L9 — `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv`
  - `i2c.sv`:L1 — `opentitan\hw\ip\i2c\rtl\i2c.sv`
  - `i2c`:L9 — `opentitan\hw\ip\i2c\rtl\i2c.sv`
  - `i2c_reg_pkg`:L32 — `opentitan\hw\ip\i2c\rtl\i2c_reg_top.sv`
  - `i2c_reg_top`:L70 — `opentitan\hw\ip\i2c\rtl\i2c.sv`
  - `i2c_core`:L112 — `opentitan\hw\ip\i2c\rtl\i2c.sv`
  - `i2c_bus_monitor.sv`:L1 — `opentitan\hw\ip\i2c\rtl\i2c_bus_monitor.sv`
  - `i2c_bus_monitor`:L8 — `opentitan\hw\ip\i2c\rtl\i2c_bus_monitor.sv`
  - `i2c_controller_fsm.sv`:L1 — `opentitan\hw\ip\i2c\rtl\i2c_controller_fsm.sv`
  - `i2c_controller_fsm`:L9 — `opentitan\hw\ip\i2c\rtl\i2c_controller_fsm.sv`
  - `i2c_core.sv`:L1 — `opentitan\hw\ip\i2c\rtl\i2c_core.sv`
  - `i2c_core`:L9 — `opentitan\hw\ip\i2c\rtl\i2c_core.sv`
  - `i2c_fifos`:L376 — `opentitan\hw\ip\i2c\rtl\i2c_core.sv`
  - `i2c_bus_monitor`:L502 — `opentitan\hw\ip\i2c\rtl\i2c_core.sv`
  - `i2c_controller_fsm`:L527 — `opentitan\hw\ip\i2c\rtl\i2c_core.sv`
  - `i2c_target_fsm`:L583 — `opentitan\hw\ip\i2c\rtl\i2c_core.sv`
  - `i2c_fifos.sv`:L1 — `opentitan\hw\ip\i2c\rtl\i2c_fifos.sv`
  - `i2c_fifos`:L7 — `opentitan\hw\ip\i2c\rtl\i2c_fifos.sv`
  - `i2c_fifo_sync_sram_adapter`:L89 — `opentitan\hw\ip\i2c\rtl\i2c_fifos.sv`
  - `i2c_fifo_sync_sram_adapter.sv`:L1 — `opentitan\hw\ip\i2c\rtl\i2c_fifo_sync_sram_adapter.sv`
**DV** (11)
  - `i2c_port_conv.sv`:L1 — `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv`
  - `i2c_port_conv`:L6 — `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv`
  - `tb.sv`:L1 — `opentitan\hw\ip\i2c\dv\tb\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\i2c\dv\tb\tb.sv`
  - `i2c_env_pkg`:L10 — `opentitan\hw\ip\i2c\dv\tests\i2c_test_pkg.sv`
  - `i2c_test_pkg`:L10 — `opentitan\hw\ip\i2c\dv\tb\tb.sv`
  - `i2c_if`:L50 — `opentitan\hw\ip\i2c\dv\tb\tb.sv`
  - `i2c_dv_if`:L58 — `opentitan\hw\ip\i2c\dv\tb\tb.sv`
  - `i2c_port_conv`:L68 — `opentitan\hw\ip\i2c\dv\tb\tb.sv`
  - `i2c_base_test.sv`:L1 — `opentitan\hw\ip\i2c\dv\tests\i2c_base_test.sv`
  - `i2c_test_pkg.sv`:L1 — `opentitan\hw\ip\i2c\dv\tests\i2c_test_pkg.sv`
**SVA** (4)
  - `i2c_bind.sv`:L1 — `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv`
  - `i2c_bind`:L5 — `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv`
  - `i2c_protocol_cov.sv`:L1 — `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv`
  - `i2c_protocol_cov`:L6 — `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv`

## Neighbor Components

- `rv_plic` (6 refs; instantiates×6)
- `lowrisc_ibex` (4 refs; instantiates×2, imports_from×2)
- `pwrmgr` (3 refs; instantiates×3)
- `pulp_riscv_dbg` (2 refs; instantiates×2)
- `flash_ctrl` (1 refs; instantiates×1)
- `i2c_agent` (1 refs; imports_from×1)
- `rstmgr` (1 refs; imports_from×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:i2c` | `i2c_fifo_sync_sram_adapter.sv` | `opentitan\hw\ip\i2c\rtl\i2c_fifo_sync_sram_adapter.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_fifo_sync_sram_adapter` | `opentitan\hw\ip\i2c\rtl\i2c_fifo_sync_sram_adapter.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_protocol_cov.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_protocol_cov` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_base_test.sv` | `opentitan\hw\ip\i2c\dv\tests\i2c_base_test.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_controller_fsm.sv` | `opentitan\hw\ip\i2c\rtl\i2c_controller_fsm.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_controller_fsm` | `opentitan\hw\ip\i2c\rtl\i2c_controller_fsm.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_env_pkg` | `opentitan\hw\ip\i2c\dv\tests\i2c_test_pkg.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_test_pkg.sv` | `opentitan\hw\ip\i2c\dv\tests\i2c_test_pkg.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_port_conv.sv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_port_conv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_bus_monitor.sv` | `opentitan\hw\ip\i2c\rtl\i2c_bus_monitor.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_bus_monitor` | `opentitan\hw\ip\i2c\rtl\i2c_bus_monitor.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_pkg` | `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_target_fsm.sv` | `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_target_fsm` | `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_bind.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_bind` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_reg_pkg` | `opentitan\hw\ip\i2c\rtl\i2c_reg_top.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_reg_pkg.sv` | `opentitan\hw\ip\i2c\rtl\i2c_reg_pkg.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_reg_top.sv` | `opentitan\hw\ip\i2c\rtl\i2c_reg_top.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_reg_top` | `opentitan\hw\ip\i2c\rtl\i2c_reg_top.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_fifos.sv` | `opentitan\hw\ip\i2c\rtl\i2c_fifos.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_fifos` | `opentitan\hw\ip\i2c\rtl\i2c_fifos.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_fifo_sync_sram_adapter` | `opentitan\hw\ip\i2c\rtl\i2c_fifos.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_core.sv` | `opentitan\hw\ip\i2c\rtl\i2c_core.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_core` | `opentitan\hw\ip\i2c\rtl\i2c_core.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_fifos` | `opentitan\hw\ip\i2c\rtl\i2c_core.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_bus_monitor` | `opentitan\hw\ip\i2c\rtl\i2c_core.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_controller_fsm` | `opentitan\hw\ip\i2c\rtl\i2c_core.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_target_fsm` | `opentitan\hw\ip\i2c\rtl\i2c_core.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_pkg.sv` | `opentitan\hw\ip\i2c\rtl\i2c_pkg.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_test_pkg` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_if` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_dv_if` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_port_conv` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c.sv` | `opentitan\hw\ip\i2c\rtl\i2c.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c` | `opentitan\hw\ip\i2c\rtl\i2c.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_reg_top` | `opentitan\hw\ip\i2c\rtl\i2c.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `i2c_pkg` | `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `i2c_bind.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `i2c_bind` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `i2c_protocol_cov.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `i2c_protocol_cov` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `i2c_port_conv.sv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `i2c_port_conv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `tb.sv` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `i2c_pkg` | `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `i2c_bind.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `i2c_bind` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `i2c_protocol_cov.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `i2c_protocol_cov` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `i2c_port_conv.sv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `i2c_port_conv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `i2c_testplan.hjson` | `i2c_pkg` | `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv` |
| `spec_path_matches_code_path` | `i2c_testplan.hjson` | `i2c_bind.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `i2c_testplan.hjson` | `i2c_bind` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `i2c_testplan.hjson` | `i2c_protocol_cov.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |

## Retrieval Guidance

- For code-only queries mentioning `i2c`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `i2c`.
