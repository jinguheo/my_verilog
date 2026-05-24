# Hardware Description: spi_host

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`spi_host`** has the following hardware interfaces defined
- **Peripheral Pins for Chip IO**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`spi_host`** has the following hardware interfaces defined

## Identity

- `ip_block`: `spi_host`
- `bridge_edge_count`: 112
- Spec categories: document: 89, component: 41, testplan: 30, theory: 19, interface: 15
- Code categories: dv: 84, rtl: 71, sva: 10
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/spi_host/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/spi_host/data/spi_host.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`spi_host`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces
…
```

### Peripheral Pins for Chip IO
_Source: `opentitan/hw/ip/spi_host/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/spi_host/data/spi_host.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`spi_host`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`tl`**
- Bus
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/spi_host/doc/interfaces.md`_

```
## Peripheral Pins for Chip IO

| Pin name   | Direction   | Description                                                                    |
|:-----------|:------------|:-------------------------------------------------------------------------------|
| sck        | output      | SPI Clock                                                                      |
| csb        | output      | Chip Sele
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/spi_host/doc/programmers_guide.md`_

```
# Programmer's Guide

The operation of the SPI_HOST IP proceeds in seven general steps.

To initialize the IP:
1. Program the [`CONFIGOPTS`](registers.md#configopts) multi-register with the appropriate timing and polarity settings for each `csb` line.
2. Set the desired interrupt parameters
3. Enable the IP
```

### Initializing the IP
_Source: `opentitan/hw/ip/spi_host/doc/programmers_guide.md`_

```
7. For transactions which expect to receive a reply, the data can then be read back from the [`RXDATA`](registers.md#rxdata) window.

These latter four steps are then repeated for each command.
Each step is covered in detail in the following sections.

For concreteness, this Programmer's Guide uses examples from one of our primary target devices, the [W25Q01JV flash from Winbond](https://www.winbo
…
```

### Per-target Configuration
_Source: `opentitan/hw/ip/spi_host/doc/programmers_guide.md`_

```
These latter four steps are then repeated for each command.
Each step is covered in detail in the following sections.

For concreteness, this Programmer's Guide uses examples from one of our primary target devices, the [W25Q01JV flash from Winbond](https://www.winbond.com/resource-files/W25Q01JV%20SPI%20RevB%2011132019.pdf).
The SPI_HOST IP is however suitable for interacting with any number of SP
…
```

### Summary
_Source: `opentitan/hw/ip/spi_host/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/spi_host/data/spi_host.hjson -->
## Summary

| Name                                     | Offset   |   Length | Description                                              |
|:-----------------------------------------|:---------|---------:|:---------------------------------------------------------|
| spi_host.[`INTR_STATE`](#intr_state)     |
…
```

### INTR STATE
_Source: `opentitan/hw/ip/spi_host/doc/registers.md`_

```
| spi_host.[`CSID`](#csid)                 | 0x1c     |        4 | Chip-Select ID                                           |
| spi_host.[`COMMAND`](#command)           | 0x20     |        4 | Command Register                                         |
| spi_host.[`RXDATA`](#rxdata)             | 0x24     |        4 | SPI Receive Data.                                        |
| spi_host.[`TXDATA`](
…
```

## Spec Anchors

- `component:spi_host` (L1) — `__graphify_spec_only__/components.md`
- `spi_host.hjson` (L1) — `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `human name` (L6) — `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `one line desc` (L7) — `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `one paragraph desc` (L8) — `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `cip id` (L16) — `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `design spec` (L17) — `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `dv doc` (L18) — `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `hw checklist` (L19) — `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `sw checklist` (L20) — `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `revisions` (L21) — `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `version` (L23) — `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `spi_host_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/spi_host/data/spi_host_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/spi_host/data/spi_host_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/spi_host/data/spi_host_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/spi_host/data/spi_host_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/spi_host/data/spi_host_sec_cm_testplan.hjson`
- `spi_host_testplan.hjson` (L1) — `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `testpoints` (L13) — `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `desc` (L16) — `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `Stimulus` (L20) — `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `Checking` (L24) — `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `stage` (L27) — `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `tests` (L28) — `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `covergroups` (L291) — `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/spi_host/doc/checklist.md`
- `SPI HOST Checklist` (L1) — `opentitan/hw/ip/spi_host/doc/checklist.md`
- `Design Checklist` (L11) — `opentitan/hw/ip/spi_host/doc/checklist.md`
- `D1` (L13) — `opentitan/hw/ip/spi_host/doc/checklist.md`
- `D2` (L37) — `opentitan/hw/ip/spi_host/doc/checklist.md`
- `D2S` (L79) — `opentitan/hw/ip/spi_host/doc/checklist.md`
- `D3` (L99) — `opentitan/hw/ip/spi_host/doc/checklist.md`
- `Verification Checklist` (L125) — `opentitan/hw/ip/spi_host/doc/checklist.md`
- `V1` (L127) — `opentitan/hw/ip/spi_host/doc/checklist.md`

## Code Evidence

**RTL** (31)
  - `tlul_adapter_reg_racl`:L52 — `opentitan\hw\ip\spi_host\rtl\spi_host_window.sv`
  - `spi_host_reg_pkg`:L37 — `opentitan\hw\ip\spi_host\rtl\spi_host_reg_top.sv`
  - `spi_host.sv`:L1 — `opentitan\hw\ip\spi_host\rtl\spi_host.sv`
  - `spi_host`:L11 — `opentitan\hw\ip\spi_host\rtl\spi_host.sv`
  - `spi_host_cmd_pkg`:L40 — `opentitan\hw\ip\spi_host\rtl\spi_host_shift_register.sv`
  - `spi_host_reg_top`:L89 — `opentitan\hw\ip\spi_host\rtl\spi_host.sv`
  - `spi_host_command_queue`:L305 — `opentitan\hw\ip\spi_host\rtl\spi_host.sv`
  - `spi_host_window`:L333 — `opentitan\hw\ip\spi_host\rtl\spi_host.sv`
  - `spi_host_data_fifos`:L431 — `opentitan\hw\ip\spi_host\rtl\spi_host.sv`
  - `spi_host_core`:L480 — `opentitan\hw\ip\spi_host\rtl\spi_host.sv`
  - `spi_host_byte_merge.sv`:L1 — `opentitan\hw\ip\spi_host\rtl\spi_host_byte_merge.sv`
  - `spi_host_byte_merge`:L8 — `opentitan\hw\ip\spi_host\rtl\spi_host_byte_merge.sv`
  - `spi_host_byte_select.sv`:L1 — `opentitan\hw\ip\spi_host\rtl\spi_host_byte_select.sv`
  - `spi_host_byte_select`:L7 — `opentitan\hw\ip\spi_host\rtl\spi_host_byte_select.sv`
  - `spi_host_cmd_pkg.sv`:L1 — `opentitan\hw\ip\spi_host\rtl\spi_host_cmd_pkg.sv`
  - `spi_host_command_queue.sv`:L1 — `opentitan\hw\ip\spi_host\rtl\spi_host_command_queue.sv`
  - `spi_host_command_queue`:L8 — `opentitan\hw\ip\spi_host\rtl\spi_host_command_queue.sv`
  - `spi_host_core.sv`:L1 — `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv`
  - `spi_host_core`:L8 — `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv`
  - `spi_host_byte_merge`:L67 — `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv`
**DV** (13)
  - `spi_if`:L46 — `opentitan\hw\ip\spi_host\dv\tb.sv`
  - `spi_device_pkg`:L15 — `opentitan\hw\ip\spi_host\dv\tb.sv`
  - `spi_host_fsm_if.sv`:L1 — `opentitan\hw\ip\spi_host\dv\spi_host_fsm_if.sv`
  - `tb.sv`:L1 — `opentitan\hw\ip\spi_host\dv\tb.sv`
  - `tb`:L6 — `opentitan\hw\ip\spi_host\dv\tb.sv`
  - `spi_host_env_pkg`:L10 — `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv`
  - `spi_host_test_pkg`:L11 — `opentitan\hw\ip\spi_host\dv\tb.sv`
  - `spi_host_cov_bind.sv`:L1 — `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_bind.sv`
  - `spi_host_cov_bind`:L6 — `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_bind.sv`
  - `spi_host_cov_if.sv`:L1 — `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_if.sv`
  - `spi_host_pkg`:L13 — `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_if.sv`
  - `spi_host_base_test.sv`:L1 — `opentitan\hw\ip\spi_host\dv\tests\spi_host_base_test.sv`
  - `spi_host_test_pkg.sv`:L1 — `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv`
**SVA** (6)
  - `spi_host_bind.sv`:L1 — `opentitan\hw\ip\spi_host\dv\sva\spi_host_bind.sv`
  - `spi_host_bind`:L5 — `opentitan\hw\ip\spi_host\dv\sva\spi_host_bind.sv`
  - `spi_host_data_stable_sva.sv`:L1 — `opentitan\hw\ip\spi_host\dv\sva\spi_host_data_stable_sva.sv`
  - `spi_host_data_stable_sva`:L7 — `opentitan\hw\ip\spi_host\dv\sva\spi_host_data_stable_sva.sv`
  - `whole_cycle_data_stable_signal_checker`:L43 — `opentitan\hw\ip\spi_host\dv\sva\spi_host_data_stable_sva.sv`
  - `whole_cycle_data_stable_signal_checker`:L69 — `opentitan\hw\ip\spi_host\dv\sva\spi_host_data_stable_sva.sv`

## Neighbor Components

- `spi_device` (22 refs; imports_from×21, instantiates×1)
- `rv_plic` (6 refs; instantiates×6)
- `lowrisc_ibex` (4 refs; imports_from×3, instantiates×1)
- `pwrmgr` (4 refs; instantiates×3, imports_from×1)
- `pulp_riscv_dbg` (2 refs; instantiates×2)
- `ast` (2 refs; instantiates×2)
- `ac_range_check` (1 refs; instantiates×1)
- `rstmgr` (1 refs; imports_from×1)
- `rv_core_ibex` (1 refs; instantiates×1)
- `mbx` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:spi_host` | `spi_host` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_data_stable_sva.sv` | `opentitan\hw\ip\spi_host\dv\sva\spi_host_data_stable_sva.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_data_stable_sva` | `opentitan\hw\ip\spi_host\dv\sva\spi_host_data_stable_sva.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_base_test.sv` | `opentitan\hw\ip\spi_host\dv\tests\spi_host_base_test.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_cmd_pkg` | `opentitan\hw\ip\spi_host\rtl\spi_host_shift_register.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_shift_register.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_shift_register.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_shift_register` | `opentitan\hw\ip\spi_host\rtl\spi_host_shift_register.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_env_pkg` | `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_test_pkg.sv` | `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_command_queue.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_command_queue.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_command_queue` | `opentitan\hw\ip\spi_host\rtl\spi_host_command_queue.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_cov_bind.sv` | `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_bind.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_cov_bind` | `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_bind.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_byte_select.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_byte_select.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_byte_select` | `opentitan\hw\ip\spi_host\rtl\spi_host_byte_select.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_byte_merge.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_byte_merge.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_byte_merge` | `opentitan\hw\ip\spi_host\rtl\spi_host_byte_merge.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_data_fifos.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_data_fifos.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_data_fifos` | `opentitan\hw\ip\spi_host\rtl\spi_host_data_fifos.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_cov_if.sv` | `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_if.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_pkg` | `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_if.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_reg_pkg` | `opentitan\hw\ip\spi_host\rtl\spi_host_reg_top.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_bind.sv` | `opentitan\hw\ip\spi_host\dv\sva\spi_host_bind.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_bind` | `opentitan\hw\ip\spi_host\dv\sva\spi_host_bind.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_cmd_pkg.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_cmd_pkg.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_reg_pkg.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_reg_pkg.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_reg_top.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_reg_top.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_reg_top` | `opentitan\hw\ip\spi_host\rtl\spi_host_reg_top.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_window.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_window.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_window` | `opentitan\hw\ip\spi_host\rtl\spi_host_window.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_fsm_if.sv` | `opentitan\hw\ip\spi_host\dv\spi_host_fsm_if.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_core.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_core` | `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_byte_merge` | `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_byte_select` | `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_shift_register` | `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_fsm` | `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_fsm.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_fsm.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_fsm` | `opentitan\hw\ip\spi_host\rtl\spi_host_fsm.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `tlul_adapter_reg_racl` | `opentitan\hw\ip\spi_host\rtl\spi_host_window.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `spi_if` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `spi_device_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `spi_host_fsm_if.sv` | `opentitan\hw\ip\spi_host\dv\spi_host_fsm_if.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `tb.sv` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `tb` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `spi_host_env_pkg` | `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `spi_host_test_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `tlul_adapter_reg_racl` | `opentitan\hw\ip\spi_host\rtl\spi_host_window.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `spi_if` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `spi_device_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `spi_host_fsm_if.sv` | `opentitan\hw\ip\spi_host\dv\spi_host_fsm_if.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `spi_host_env_pkg` | `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `spi_host_test_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_testplan.hjson` | `tlul_adapter_reg_racl` | `opentitan\hw\ip\spi_host\rtl\spi_host_window.sv` |
| `spec_path_matches_code_path` | `spi_host_testplan.hjson` | `spi_if` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_testplan.hjson` | `spi_device_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_testplan.hjson` | `spi_host_fsm_if.sv` | `opentitan\hw\ip\spi_host\dv\spi_host_fsm_if.sv` |

## Retrieval Guidance

- For code-only queries mentioning `spi_host`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `spi_host`.
