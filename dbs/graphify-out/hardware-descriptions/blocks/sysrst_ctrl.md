# Hardware Description: sysrst_ctrl

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`sysrst_ctrl`** has the following hardware interfaces defined
- **Peripheral Pins for Chip IO**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`sysrst_ctrl`** has the following hardware interfaces defined

## Identity

- `ip_block`: `sysrst_ctrl`
- `bridge_edge_count`: 104
- Spec categories: document: 71, component: 41, testplan: 28, theory: 19, interface: 15
- Code categories: dv: 80, rtl: 63, other_code: 51, sva: 4
- Bridge relations: spec_path_matches_code_path: 64, spec_component_matches_code: 40

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/sysrst_ctrl/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`sysrst_ctrl`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_aon_i`**
- Bus
…
```

### Peripheral Pins for Chip IO
_Source: `opentitan/hw/ip/sysrst_ctrl/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`sysrst_ctrl`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_aon_i`**
- Bus Device Interfaces (TL-U
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/sysrst_ctrl/doc/interfaces.md`_

```
| key0_out    | output      | Passthrough from key0_in, can be configured to invert                |
| key1_out    | output      | Passthrough from key1_in, can be configured to invert                |
| key2_out    | output      | Passthrough from key2_in, can be configured to invert                |
| pwrb_out    | output      | Passthrough from pwrb_in, can be configured to invert
…
```

### Summary
_Source: `opentitan/hw/ip/sysrst_ctrl/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson -->
## Summary

| Name                                                              | Offset   |   Length | Description                                                                    |
|:------------------------------------------------------------------|:---------|---------:|:--------------------------
…
```

### INTR STATE
_Source: `opentitan/hw/ip/sysrst_ctrl/doc/registers.md`_

```
| sysrst_ctrl.[`COM_DET_CTL_3`](#com_det_ctl)                       | 0x90     |        4 | To define the duration that the combo should be pressed                        |
| sysrst_ctrl.[`COM_OUT_CTL_0`](#com_out_ctl)                       | 0x94     |        4 | To define the actions once the combo is detected                               |
| sysrst_ctrl.[`COM_OUT_CTL_1`](#com_out_ctl)
…
```

### Fields
_Source: `opentitan/hw/ip/sysrst_ctrl/doc/registers.md`_

```
| sysrst_ctrl.[`KEY_INTR_STATUS`](#key_intr_status)                 | 0xa8     |        4 | key interrupt source                                                           |

## INTR_STATE
Interrupt State Register
- Offset: `0x0`
- Reset default: `0x0`
- Reset mask: `0x1`

### Fields

```wavejson
{"reg": [{"name": "event_detected", "bits": 1, "attr": ["ro"], "rotate": -90}, {"bits": 31}], "config":
…
```

### Theory of Operation
_Source: `opentitan/hw/ip/sysrst_ctrl/doc/theory_of_operation.md`_

```
# Theory of Operation

![`sysrst_ctrl` Block Diagram](./sysrst_ctrl_blockdiagram.svg)

The block diagram above shows a conceptual view of the `sysrst_ctrl` block, which consists of 3 main modules:
The first is the configuration and status registers, the second is the keyboard combo debounce and detection logic, and the third is the pinout override logic.
The debounce logic does not implement a low
…
```

### Combo detection
_Source: `opentitan/hw/ip/sysrst_ctrl/doc/theory_of_operation.md`_

```
This allows the security chip to take over the inputs for its own use without disturbing the main user.

The `sysrst_ctrl` also controls two active-low open-drain I/Os named `flash_wp_l_i` / `flash_wp_l_o` and `ec_rst_l_i` / `ec_rst_l_o`.
The `ec_rst_l_i` / `ec_rst_l_o` signals are connected to the same bidirectional pin of the OpenTitan chip, and are used to either reset the embedded controller (
…
```

## Spec Anchors

- `component:sysrst_ctrl` (L1) — `__graphify_spec_only__/components.md`
- `sysrst_ctrl.hjson` (L1) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `human name` (L6) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `one line desc` (L7) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `one paragraph desc` (L8) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `cip id` (L14) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `design spec` (L15) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `dv doc` (L16) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `hw checklist` (L17) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `sw checklist` (L18) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `version` (L19) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `life stage` (L20) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `sysrst_ctrl_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_sec_cm_testplan.hjson`
- `sysrst_ctrl_testplan.hjson` (L1) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_testplan.hjson`
- `testpoints` (L12) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_testplan.hjson`
- `desc` (L15) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_testplan.hjson`
- `stage` (L21) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_testplan.hjson`
- `tests` (L22) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_testplan.hjson`
- `covergroups` (L235) — `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `SYSRST CTRL Checklist` (L1) — `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `D2` (L32) — `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `D2S` (L74) — `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `D3` (L94) — `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `Verification Checklist` (L120) — `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `V1` (L122) — `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `V2` (L172) — `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `V2S` (L219) — `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`

## Code Evidence

**RTL** (31)
  - `sysrst_ctrl_pkg`:L8 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv`
  - `sysrst_ctrl.sv`:L1 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
  - `sysrst_ctrl`:L9 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
  - `sysrst_ctrl_reg_pkg`:L9 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv`
  - `sysrst_ctrl_autoblock`:L154 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
  - `sysrst_ctrl_ulp`:L182 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
  - `sysrst_ctrl_keyintr`:L206 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
  - `sysrst_ctrl_combo`:L233 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
  - `sysrst_ctrl_pin`:L266 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
  - `sysrst_ctrl_intr`:L330 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
  - `sysrst_ctrl_autoblock.sv`:L1 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_autoblock.sv`
  - `sysrst_ctrl_autoblock`:L7 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_autoblock.sv`
  - `sysrst_ctrl_detect`:L28 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv`
  - `sysrst_ctrl_combo.sv`:L1 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_combo.sv`
  - `sysrst_ctrl_combo`:L7 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_combo.sv`
  - `sysrst_ctrl_comboact.sv`:L1 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_comboact.sv`
  - `sysrst_ctrl_comboact`:L7 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_comboact.sv`
  - `sysrst_ctrl_detect.sv`:L1 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_detect.sv`
  - `sysrst_ctrl_detect`:L24 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_detect.sv`
  - `sysrst_ctrl_intr.sv`:L1 — `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_intr.sv`
**DV** (10)
  - `tb.sv`:L1 — `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv`
  - `sysrst_ctrl_env_pkg`:L9 — `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv`
  - `sysrst_ctrl_test_pkg`:L10 — `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv`
  - `sysrst_ctrl_if`:L36 — `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv`
  - `sysrst_ctrl_cov_bind.sv`:L1 — `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv`
  - `sysrst_ctrl_cov_bind`:L6 — `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv`
  - `sysrst_ctrl_cov_if.sv`:L1 — `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_if.sv`
  - `sysrst_ctrl_base_test.sv`:L1 — `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_base_test.sv`
  - `sysrst_ctrl_test_pkg.sv`:L1 — `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv`
**SVA** (2)
  - `sysrst_ctrl_bind.sv`:L1 — `opentitan\hw\ip\sysrst_ctrl\dv\sva\sysrst_ctrl_bind.sv`
  - `sysrst_ctrl_bind`:L5 — `opentitan\hw\ip\sysrst_ctrl\dv\sva\sysrst_ctrl_bind.sv`
**OTHER_CODE** (7)
  - `mod.rs`:L1 — `opentitan\sw\host\tests\chip\sysrst_ctrl\mod.rs`
  - `sysrst_ctrl.rs`:L1 — `opentitan\sw\host\tests\chip\sysrst_ctrl\sysrst_ctrl.rs`
  - `Config`:L9 — `opentitan\sw\host\tests\chip\sysrst_ctrl\sysrst_ctrl.rs`
  - `setup_pins()`:L22 — `opentitan\sw\host\tests\chip\sysrst_ctrl\sysrst_ctrl.rs`
  - `set_pins()`:L47 — `opentitan\sw\host\tests\chip\sysrst_ctrl\sysrst_ctrl.rs`
  - `read_pins()`:L60 — `opentitan\sw\host\tests\chip\sysrst_ctrl\sysrst_ctrl.rs`
  - `sysrst_ctrl_ec_rst_l.rs`:L1 — `opentitan\sw\host\tests\chip\sysrst_ctrl\sysrst_ctrl_ec_rst_l.rs`

## Neighbor Components

- `uart` (16 refs; calls×16)
- `lowrisc_ibex` (7 refs; calls×4, imports_from×2, instantiates×1)
- `rv_plic` (6 refs; instantiates×6)
- `uart.rs` (5 refs; calls×5)
- `gpio.rs` (5 refs; calls×5)
- `riscv-tests` (3 refs; calls×3)
- `pwrmgr` (3 refs; instantiates×3)
- `pulp_riscv_dbg` (2 refs; instantiates×2)
- `rstmgr` (2 refs; instantiates×1, imports_from×1)
- `spi.rs` (2 refs; calls×2)
- `gpio_monitor.rs` (2 refs; calls×2)
- `pinmux` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_base_test.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_env_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_test_pkg.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_cov_bind.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_cov_bind` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_cov_if.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_if.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_autoblock.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_autoblock.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_autoblock` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_autoblock.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_comboact.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_comboact.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_comboact` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_comboact.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_bind.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\sva\sysrst_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_bind` | `opentitan\hw\ip\sysrst_ctrl\dv\sva\sysrst_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_keyintr.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_keyintr.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_keyintr` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_keyintr.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_reg_pkg.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_reg_top.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_reg_top` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_detect.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_detect.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_detect` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_detect.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_combo.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_combo.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_combo` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_combo.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_intr.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_intr.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_intr` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_intr.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_pkg` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_reg_pkg` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_detect` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_pin.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_pin.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_pin` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_pin.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_pkg.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_ulp.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_ulp` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_autoblock` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_ulp` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_keyintr` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_combo` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_pin` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_intr` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `tb.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `tb` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `sysrst_ctrl_env_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `sysrst_ctrl_test_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `sysrst_ctrl_if` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `sysrst_ctrl_cov_bind.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `sysrst_ctrl_cov_bind` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `sysrst_ctrl_cov_if.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_if.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `sysrst_ctrl_env_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `sysrst_ctrl_test_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `sysrst_ctrl_if` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `sysrst_ctrl_cov_bind.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `sysrst_ctrl_cov_bind` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `sysrst_ctrl_cov_if.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_if.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_testplan.hjson` | `tb` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_testplan.hjson` | `sysrst_ctrl_env_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_testplan.hjson` | `sysrst_ctrl_test_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |

## Retrieval Guidance

- For code-only queries mentioning `sysrst_ctrl`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `sysrst_ctrl`.
