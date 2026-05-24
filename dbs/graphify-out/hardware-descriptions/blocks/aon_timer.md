# Hardware Description: aon_timer

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`aon_timer`** has the following hardware interfaces defined
- **Inter-Module Signals**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`aon_timer`** has the following hardware interfaces defined

## Identity

- `ip_block`: `aon_timer`
- `bridge_edge_count`: 93
- Spec categories: document: 90, testplan: 28, component: 22, interface: 15, theory: 12
- Code categories: dv: 66, sva: 22, rtl: 21, other_code: 2
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 21

## Spec Excerpts

### Interfaces
_Source: `opentitan/hw/ip/aon_timer/doc/interfaces.md`_

```
# Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/aon_timer/data/aon_timer.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`aon_timer`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_aon_i`**
- Bus Device Interfac
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/aon_timer/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/aon_timer/data/aon_timer.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`aon_timer`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_aon_i`**
- Bus Device Interfaces (TL-UL): **
…
```

### Interrupts
_Source: `opentitan/hw/ip/aon_timer/doc/interfaces.md`_

```
| wkup_req            | logic                         | uni     | req   |       1 |                                                                                                                                      |
| aon_timer_rst_req   | logic                         | uni     | req   |       1 |
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/aon_timer/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

1. Set the timer values [`WKUP_COUNT_LO`](registers.md#wkup_count_lo), [`WKUP_COUNT_HI`](registers.md#wkup_count_hi) and [`WDOG_COUNT`](registers.md#wdog_count) to zero.
2. Program the desired wakeup pre-scaler value in [`WKUP_CTRL`](registers.md#wkup_ctrl).
3. Program the desired thresholds in [`WKUP_THOLD_LO`](registers.md#wkup_thold_lo), [`WKUP_THOLD_HI`
…
```

### Initialization
_Source: `opentitan/hw/ip/aon_timer/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

1. Set the timer values [`WKUP_COUNT_LO`](registers.md#wkup_count_lo), [`WKUP_COUNT_HI`](registers.md#wkup_count_hi) and [`WDOG_COUNT`](registers.md#wdog_count) to zero.
2. Program the desired wakeup pre-scaler value in [`WKUP_CTRL`](registers.md#wkup_ctrl).
3. Program the desired thresholds in [`WKUP_THOLD_LO`](registers.md#wkup_thold_lo), [`WKUP_THOLD_HI`
…
```

### Watchdog pet
_Source: `opentitan/hw/ip/aon_timer/doc/programmers_guide.md`_

```
## Initialization

1. Set the timer values [`WKUP_COUNT_LO`](registers.md#wkup_count_lo), [`WKUP_COUNT_HI`](registers.md#wkup_count_hi) and [`WDOG_COUNT`](registers.md#wdog_count) to zero.
2. Program the desired wakeup pre-scaler value in [`WKUP_CTRL`](registers.md#wkup_ctrl).
3. Program the desired thresholds in [`WKUP_THOLD_LO`](registers.md#wkup_thold_lo), [`WKUP_THOLD_HI`](registers.md#wkup_th
…
```

### Summary
_Source: `opentitan/hw/ip/aon_timer/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/aon_timer/data/aon_timer.hjson -->
## Summary

| Name                                            | Offset   |   Length | Description                                    |
|:------------------------------------------------|:---------|---------:|:-----------------------------------------------|
| aon_timer.[`ALERT_TEST`](#alert_test)
…
```

### ALERT TEST
_Source: `opentitan/hw/ip/aon_timer/doc/registers.md`_

```
| aon_timer.[`WDOG_CTRL`](#wdog_ctrl)             | 0x1c     |        4 | Watchdog Timer Control register                |
| aon_timer.[`WDOG_BARK_THOLD`](#wdog_bark_thold) | 0x20     |        4 | Watchdog Timer Bark Threshold Register         |
| aon_timer.[`WDOG_BITE_THOLD`](#wdog_bite_thold) | 0x24     |        4 | Watchdog Timer Bite Threshold Register         |
| aon_timer.[`WDOG_COUNT`](#wdo
…
```

## Spec Anchors

- `component:aon_timer` (L1) — `__graphify_spec_only__/components.md`
- `aon_timer.hjson` (L1) — `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `human name` (L7) — `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `one line desc` (L8) — `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `one paragraph desc` (L9) — `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `cip id` (L17) — `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `design spec` (L18) — `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `dv doc` (L19) — `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `hw checklist` (L20) — `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `sw checklist` (L21) — `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `version` (L22) — `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `life stage` (L23) — `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `aon_timer_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/aon_timer/data/aon_timer_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/aon_timer/data/aon_timer_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/aon_timer/data/aon_timer_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/aon_timer/data/aon_timer_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/aon_timer/data/aon_timer_sec_cm_testplan.hjson`
- `aon_timer_testplan.hjson` (L1) — `opentitan/hw/ip/aon_timer/data/aon_timer_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/aon_timer/data/aon_timer_testplan.hjson`
- `testpoints` (L13) — `opentitan/hw/ip/aon_timer/data/aon_timer_testplan.hjson`
- `desc` (L16) — `opentitan/hw/ip/aon_timer/data/aon_timer_testplan.hjson`
- `stage` (L31) — `opentitan/hw/ip/aon_timer/data/aon_timer_testplan.hjson`
- `tests` (L32) — `opentitan/hw/ip/aon_timer/data/aon_timer_testplan.hjson`
- `covergroups` (L135) — `opentitan/hw/ip/aon_timer/data/aon_timer_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `AON Timer Checklist` (L1) — `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `D2` (L32) — `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `D2S` (L74) — `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `D3` (L94) — `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `Verification Checklist` (L120) — `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `V1` (L122) — `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `V2` (L172) — `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `V2S` (L218) — `opentitan/hw/ip/aon_timer/doc/checklist.md`

## Code Evidence

**RTL** (11)
  - `aon_timer.sv`:L1 — `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv`
  - `aon_timer`:L10 — `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv`
  - `aon_timer_reg_pkg`:L34 — `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_top.sv`
  - `aon_timer_reg_top`:L101 — `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv`
  - `aon_timer_core`:L164 — `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv`
  - `aon_timer_core.sv`:L1 — `opentitan\hw\ip\aon_timer\rtl\aon_timer_core.sv`
  - `aon_timer_core`:L7 — `opentitan\hw\ip\aon_timer\rtl\aon_timer_core.sv`
  - `aon_timer_reg_pkg.sv`:L1 — `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_pkg.sv`
  - `aon_timer_reg_top.sv`:L1 — `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_top.sv`
  - `aon_timer_reg_top`:L9 — `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_top.sv`
  - `aon_timer`:L1049 — `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
**DV** (6)
  - `tb.sv`:L1 — `opentitan\hw\ip\aon_timer\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\aon_timer\dv\tb.sv`
  - `aon_timer_env_pkg`:L10 — `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv`
  - `aon_timer_test_pkg`:L10 — `opentitan\hw\ip\aon_timer\dv\tb.sv`
  - `aon_timer_base_test.sv`:L1 — `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv`
  - `aon_timer_test_pkg.sv`:L1 — `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv`
**SVA** (2)
  - `aon_timer_bind.sv`:L1 — `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv`
  - `aon_timer_bind`:L5 — `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv`
**OTHER_CODE** (2)
  - `aon_timer.rs`:L1 — `opentitan\sw\host\ot_hal\src\dif\aon_timer.rs`
  - `AonTimerReg`:L7 — `opentitan\sw\host\ot_hal\src\dif\aon_timer.rs`

## Neighbor Components

- `rv_plic` (6 refs; instantiates×6)
- `lowrisc_ibex` (5 refs; instantiates×3, imports_from×2)
- `pwrmgr` (3 refs; instantiates×3)
- `pulp_riscv_dbg` (1 refs; instantiates×1)
- `rv_core_ibex` (1 refs; instantiates×1)
- `rstmgr` (1 refs; imports_from×1)
- `pinmux` (1 refs; instantiates×1)
- `clkmgr` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_base_test.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_test_pkg.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_bind.sv` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_bind` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_reg_pkg` | `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_top.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_reg_pkg.sv` | `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_pkg.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_reg_top.sv` | `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_top.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_reg_top` | `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_top.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_core.sv` | `opentitan\hw\ip\aon_timer\rtl\aon_timer_core.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_core` | `opentitan\hw\ip\aon_timer\rtl\aon_timer_core.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer.sv` | `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer` | `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_reg_top` | `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_core` | `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_test_pkg` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer.rs` | `opentitan\sw\host\ot_hal\src\dif\aon_timer.rs` |
| `spec_component_matches_code` | `component:aon_timer` | `AonTimerReg` | `opentitan\sw\host\ot_hal\src\dif\aon_timer.rs` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `aon_timer_test_pkg` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `aon_timer_bind.sv` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `aon_timer_bind` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `aon_timer_base_test.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `aon_timer_test_pkg.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `aon_timer_test_pkg` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `aon_timer_bind.sv` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `aon_timer_bind` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `aon_timer_base_test.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `aon_timer_test_pkg.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `aon_timer_test_pkg` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `aon_timer_bind.sv` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `aon_timer_bind` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `aon_timer_base_test.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `aon_timer_test_pkg.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aon_timer_test_pkg` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aon_timer_bind.sv` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aon_timer_bind` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aon_timer_base_test.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aon_timer_test_pkg.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aon_timer_test_pkg` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aon_timer_bind.sv` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aon_timer_bind` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aon_timer_base_test.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv` |

## Retrieval Guidance

- For code-only queries mentioning `aon_timer`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `aon_timer`.
