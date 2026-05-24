# Hardware Description: gpio

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`gpio`** has the following hardware interfaces defined
- **Peripheral Pins for Chip IO**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`gpio`** has the following hardware interfaces defined
- **Inter-Module Signals**: - Bus Host Interfaces (TL-UL): *none*

## Identity

- `ip_block`: `gpio`
- `bridge_edge_count`: 520
- Spec categories: document: 426, testplan: 150, theory: 73, interface: 72, component: 41
- Code categories: rtl: 289, dv: 181, sva: 96, other_code: 36
- Bridge relations: spec_path_matches_code_path: 480, spec_component_matches_code: 40

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/top_darjeeling/ip_autogen/gpio/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`gpio`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device
…
```

### Peripheral Pins for Chip IO
_Source: `opentitan/hw/top_darjeeling/ip_autogen/gpio/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`gpio`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`
…
```

### Inter-Module Signals
_Source: `opentitan/hw/top_darjeeling/ip_autogen/gpio/doc/interfaces.md`_

```
- Bus Host Interfaces (TL-UL): *none*

## Peripheral Pins for Chip IO

| Pin name   | Direction   | Description            |
|:-----------|:------------|:-----------------------|
| gpio[31:0] | inout       | GPIO inout to/from PAD |

## [Inter-Module Signals](https://opentitan.org/book/doc/contributing/hw/comportability/index.html#inter-signal-handling)

| Port Name      | Package::Struct
…
```

### Programmer's Guide
_Source: `opentitan/hw/top_darjeeling/ip_autogen/gpio/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

Initialization of the GPIO module includes the setting up of the interrupt
configuration for each GPIO input, as well as the configuration of
the required noise filtering. These do not provide masked access since
they are not expected to be done frequently.
```

### Initialization
_Source: `opentitan/hw/top_darjeeling/ip_autogen/gpio/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

Initialization of the GPIO module includes the setting up of the interrupt
configuration for each GPIO input, as well as the configuration of
the required noise filtering. These do not provide masked access since
they are not expected to be done frequently.

```cpp
```

### Common Examples
_Source: `opentitan/hw/top_darjeeling/ip_autogen/gpio/doc/programmers_guide.md`_

```
*GPIO_INTR_ENABLE =          0b11011111;
*GPIO_INTR_CTRL_EN_RISING =  0b00010011;
*GPIO_INTR_CTRL_EN_FALLING = 0b00011100;
*GPIO_INTR_CTRL_EN_LVLLOW  = 0b11000000;
*GPIO_INTR_CTRL_EN_LVLHIGH = 0b00000000;
*GPIO_CTRL_EN_INPUT_FILTER = 0b00001111;
```

## Common Examples

This section below shows the interaction between the direct access
and mask access for data output and data enable.

```cpp
// as
…
```

### Summary
_Source: `opentitan/hw/top_darjeeling/ip_autogen/gpio/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson -->
## Summary

| Name                                                       | Offset   |   Length | Description                                                                       |
|:-----------------------------------------------------------|:---------|---------:|:----------------------------
…
```

### INTR STATE
_Source: `opentitan/hw/top_darjeeling/ip_autogen/gpio/doc/registers.md`_

```
| gpio.[`INP_PRD_CNT_VAL_1`](#inp_prd_cnt_val)               | 0x6c     |        4 | Output value of one input period counter.                                         |
| gpio.[`INP_PRD_CNT_VAL_2`](#inp_prd_cnt_val)               | 0x70     |        4 | Output value of one input period counter.                                         |
| gpio.[`INP_PRD_CNT_VAL_3`](#inp_prd_cnt_val)               |
…
```

## Spec Anchors

- `component:gpio` (L1) — `__graphify_spec_only__/components.md`
- `gpio.tpldesc.hjson` (L1) — `opentitan/hw/ip_templates/gpio/data/gpio.tpldesc.hjson`
- `template param list` (L5) — `opentitan/hw/ip_templates/gpio/data/gpio.tpldesc.hjson`
- `desc` (L8) — `opentitan/hw/ip_templates/gpio/data/gpio.tpldesc.hjson`
- `dtgen` (L29) — `opentitan/hw/ip_templates/gpio/data/gpio.tpldesc.hjson`
- `gpio_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip_templates/gpio/data/gpio_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip_templates/gpio/data/gpio_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip_templates/gpio/data/gpio_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip_templates/gpio/data/gpio_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip_templates/gpio/data/gpio_sec_cm_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `GPIO Checklist` (L1) — `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `D2` (L36) — `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `D2S` (L78) — `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `D3` (L98) — `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `Verification Checklist` (L124) — `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `V1` (L126) — `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `V2` (L178) — `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `V2S` (L229) — `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `gpio.hjson` (L1) — `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `human name` (L6) — `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `one line desc` (L7) — `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `one paragraph desc` (L8) — `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `cip id` (L15) — `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `design spec` (L16) — `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `dv doc` (L17) — `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `hw checklist` (L18) — `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `sw checklist` (L19) — `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `revisions` (L20) — `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `version` (L22) — `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `gpio_sec_cm_testplan.hjson` (L1) — `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio_sec_cm_testplan.hjson`

## Code Evidence

**RTL** (21)
  - `gpio_pkg`:L10 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv`
  - `gpio_reg_pkg`:L32 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_reg_top.sv`
  - `gpio.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio.sv`
  - `gpio`:L9 — `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio.sv`
  - `gpio_reg_top`:L220 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv`
  - `gpio_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_pkg.sv`
  - `gpio_reg_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_reg_pkg.sv`
  - `gpio_reg_top.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_reg_top.sv`
  - `gpio_reg_top`:L9 — `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_reg_top.sv`
  - `gpio.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio.sv`
  - `gpio`:L9 — `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio.sv`
  - `gpio_pkg.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_pkg.sv`
  - `gpio_reg_pkg.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_reg_pkg.sv`
  - `gpio_reg_top.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_reg_top.sv`
  - `gpio_reg_top`:L9 — `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_reg_top.sv`
  - `gpio.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv`
  - `gpio`:L9 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv`
  - `gpio_pkg.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_pkg.sv`
  - `gpio_reg_pkg.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_reg_pkg.sv`
  - `gpio_reg_top.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_reg_top.sv`
**DV** (19)
  - `tl_agent_pkg`:L10 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv`
  - `gpio_straps_if.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv`
  - `tb.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tb\tb.sv`
  - `tb`:L6 — `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tb\tb.sv`
  - `gpio_env_pkg`:L9 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv`
  - `gpio_test_pkg`:L12 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv`
  - `gpio_straps_if`:L36 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv`
  - `gpio_base_test.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tests\gpio_base_test.sv`
  - `gpio_test_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv`
  - `gpio_straps_if.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv`
  - `tb.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\tb\tb.sv`
  - `tb`:L6 — `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\tb\tb.sv`
  - `gpio_base_test.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\tests\gpio_base_test.sv`
  - `gpio_test_pkg.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv`
  - `gpio_straps_if.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv`
  - `tb.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv`
  - `tb`:L6 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv`
  - `gpio_base_test.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_base_test.sv`
  - `gpio_test_pkg.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv`
**SVA** (6)
  - `gpio_bind.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv`
  - `gpio_bind`:L5 — `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv`
  - `gpio_bind.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\sva\gpio_bind.sv`
  - `gpio_bind`:L5 — `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\sva\gpio_bind.sv`
  - `gpio_bind.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\sva\gpio_bind.sv`
  - `gpio_bind`:L5 — `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\sva\gpio_bind.sv`
**OTHER_CODE** (4)
  - `gpio_intr.rs`:L1 — `opentitan\sw\host\tests\chip\gpio\src\gpio_intr.rs`
  - `Opts`:L23 — `opentitan\sw\host\tests\chip\gpio\src\gpio_intr.rs`
  - `Config`:L32 — `opentitan\sw\host\tests\chip\gpio\src\gpio_intr.rs`
  - `gpio_write()`:L118 — `opentitan\sw\host\tests\chip\gpio\src\gpio_intr.rs`

## Neighbor Components

- `gpio.rs` (28 refs; calls×28)
- `rv_plic` (18 refs; instantiates×18)
- `lowrisc_ibex` (17 refs; calls×11, instantiates×3, imports_from×3)
- `pwrmgr` (9 refs; instantiates×9)
- `uart` (6 refs; calls×5, imports_from×1)
- `rstmgr` (3 refs; imports_from×3)
- `uart.rs` (3 refs; calls×3)
- `prim` (2 refs; calls×2)
- `riscv-tests` (2 refs; calls×2)
- `gpio_unittest.cc` (2 refs; calls×2)
- `hmac` (1 refs; imports_from×1)
- `rv_timer` (1 refs; imports_from×1)

## Verification Coverage (SVA)

**8 assert** · **4 cover**

| Kind | Property ID | Spec reference | File:line |
|------|-------------|----------------|-----------|
| `assert` | `sva.gpio.rst.outputs_clear` | "After reset all outputs shall be 0 and output-enables deasserted." | `gpio_assert.sv:40` |
| `assert` | `sva.gpio.rst.oe_clear` |  | `gpio_assert.sv:48` |
| `assert` | `sva.gpio.rst.intr_clear` |  | `gpio_assert.sv:56` |
| `assert` | `sva.gpio.oe.asserted_when_reg_set` |  | `gpio_assert.sv:75` |
| `assert` | `sva.gpio.oe.deasserted_when_reg_clear` |  | `gpio_assert.sv:84` |
| `assert` | `sva.gpio.out.matches_reg_when_oe` |  | `gpio_assert.sv:106` |
| `assert` | `sva.gpio.masked.lower_unchanged_bits_stable` | "MASKED_OUT_LOWER write only changes bits whose mask bit is set." | `gpio_assert.sv:129` |
| `assert` | `sva.gpio.intr.gated_by_enable` |  | `gpio_assert.sv:150` |
| `cover` | `sva.gpio.cover.any_output_driven` |  | `gpio_assert.sv:163` |
| `cover` | `sva.gpio.cover.all_outputs_driven` |  | `gpio_assert.sv:167` |
| `cover` | `sva.gpio.cover.any_interrupt_fired` |  | `gpio_assert.sv:171` |
| `cover` | `anon_ln176` |  | `gpio_assert.sv:176` |

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:gpio` | `gpio_straps_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_base_test.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_base_test.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_straps_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_env_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_test_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_straps_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_base_test.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tests\gpio_base_test.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_reg_top.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_test_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_bind.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_bind` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_reg_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_top.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_reg_top.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_reg_top.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_base_test.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\tests\gpio_base_test.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_test_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_bind` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_reg_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_top.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_reg_top.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_top` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_reg_top.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_test_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_straps_if` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_bind.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_bind` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_reg_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_top.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_reg_top.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_top` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_reg_top.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `tl_agent_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `gpio_straps_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `gpio_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `gpio_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `gpio_bind` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `gpio_env_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `tl_agent_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `gpio_straps_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `gpio_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `gpio_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv` |

## Retrieval Guidance

- For code-only queries mentioning `gpio`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `gpio`.
