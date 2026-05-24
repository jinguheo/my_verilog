# Hardware Description: rv_timer

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`rv_timer`** has the following hardware interfaces defined
- **Inter-Module Signals**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`rv_timer`** has the following hardware interfaces defined

## Identity

- `ip_block`: `rv_timer`
- `bridge_edge_count`: 98
- Spec categories: document: 87, component: 27, testplan: 27, interface: 15, theory: 14
- Code categories: dv: 70, sva: 30, rtl: 19, other_code: 4
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 26

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/rv_timer/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/rv_timer/data/rv_timer.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`rv_timer`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/rv_timer/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/rv_timer/data/rv_timer.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`rv_timer`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`tl`**
- Bus
…
```

### Interrupts
_Source: `opentitan/hw/ip/rv_timer/doc/interfaces.md`_

```
## [Inter-Module Signals](https://opentitan.org/book/doc/contributing/hw/comportability/index.html#inter-signal-handling)

| Port Name     | Package::Struct               | Type    | Act   |   Width | Description                                                                                                                          |
|:--------------|:------------------------------|:--------|:----
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/rv_timer/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

Software is expected to configure `prescaler` and `step` before activating the
timer. These two fields need to be stable to correctly increment the timer
value. If software wants to change these fields, it should de-activate the
timer and then proceed.
```

### Initialization
_Source: `opentitan/hw/ip/rv_timer/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

Software is expected to configure `prescaler` and `step` before activating the
timer. These two fields need to be stable to correctly increment the timer
value. If software wants to change these fields, it should de-activate the
timer and then proceed.

## Register Access
```

### Register Access
_Source: `opentitan/hw/ip/rv_timer/doc/programmers_guide.md`_

```
## Initialization

Software is expected to configure `prescaler` and `step` before activating the
timer. These two fields need to be stable to correctly increment the timer
value. If software wants to change these fields, it should de-activate the
timer and then proceed.

## Register Access

The timer IP has 64-bit timer value registers and 64-bit compare registers. The
register interface, however
…
```

### Summary
_Source: `opentitan/hw/ip/rv_timer/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/rv_timer/data/rv_timer.hjson -->
## Summary

| Name                                             | Offset   |   Length | Description              |
|:-------------------------------------------------|:---------|---------:|:-------------------------|
| rv_timer.[`ALERT_TEST`](#alert_test)             | 0x0      |        4 | Alert Test Registe
…
```

### ALERT TEST
_Source: `opentitan/hw/ip/rv_timer/doc/registers.md`_

```
| rv_timer.[`INTR_STATE0`](#intr_state0)           | 0x104    |        4 | Interrupt Status         |
| rv_timer.[`INTR_TEST0`](#intr_test0)             | 0x108    |        4 | Interrupt test register  |
| rv_timer.[`CFG0`](#cfg0)                         | 0x10c    |        4 | Configuration for Hart 0 |
| rv_timer.[`TIMER_V_LOWER0`](#timer_v_lower0)     | 0x110    |        4 | Timer value Lower
…
```

## Spec Anchors

- `component:rv_timer` (L1) — `__graphify_spec_only__/components.md`
- `rv_timer.hjson` (L1) — `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `human name` (L7) — `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `one line desc` (L8) — `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `one paragraph desc` (L9) — `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `cip id` (L14) — `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `design spec` (L15) — `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `dv doc` (L16) — `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `hw checklist` (L17) — `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `sw checklist` (L18) — `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `revisions` (L19) — `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `version` (L21) — `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `rv_timer_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/rv_timer/data/rv_timer_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/rv_timer/data/rv_timer_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/rv_timer/data/rv_timer_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/rv_timer/data/rv_timer_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/rv_timer/data/rv_timer_sec_cm_testplan.hjson`
- `rv_timer_testplan.hjson` (L1) — `opentitan/hw/ip/rv_timer/data/rv_timer_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/rv_timer/data/rv_timer_testplan.hjson`
- `testpoints` (L12) — `opentitan/hw/ip/rv_timer/data/rv_timer_testplan.hjson`
- `desc` (L15) — `opentitan/hw/ip/rv_timer/data/rv_timer_testplan.hjson`
- `stage` (L21) — `opentitan/hw/ip/rv_timer/data/rv_timer_testplan.hjson`
- `tests` (L22) — `opentitan/hw/ip/rv_timer/data/rv_timer_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `RV TIMER Checklist` (L1) — `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `Design Checklist` (L7) — `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `D1` (L9) — `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `D2` (L35) — `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `D2S` (L79) — `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `D3` (L99) — `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `Verification Checklist` (L127) — `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `V1` (L129) — `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `V2` (L179) — `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `V2S` (L227) — `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `interfaces.md` (L1) — `opentitan/hw/ip/rv_timer/doc/interfaces.md`

## Code Evidence

**RTL** (10)
  - `rv_timer.sv`:L1 — `opentitan\hw\ip\rv_timer\rtl\rv_timer.sv`
  - `rv_timer`:L9 — `opentitan\hw\ip\rv_timer\rtl\rv_timer.sv`
  - `rv_timer_reg_pkg`:L32 — `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_top.sv`
  - `rv_timer_reg_top`:L126 — `opentitan\hw\ip\rv_timer\rtl\rv_timer.sv`
  - `rv_timer_reg_pkg.sv`:L1 — `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_pkg.sv`
  - `rv_timer_reg_top.sv`:L1 — `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_top.sv`
  - `rv_timer_reg_top`:L9 — `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_top.sv`
  - `timer_core.sv`:L1 — `opentitan\hw\ip\rv_timer\rtl\timer_core.sv`
  - `timer_core`:L7 — `opentitan\hw\ip\rv_timer\rtl\timer_core.sv`
  - `rv_timer`:L750 — `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
**DV** (8)
  - `tb.sv`:L1 — `opentitan\hw\ip\rv_timer\dv\tb\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\rv_timer\dv\tb\tb.sv`
  - `rv_timer_env_pkg`:L9 — `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv`
  - `rv_timer_test_pkg`:L11 — `opentitan\hw\ip\rv_timer\dv\tb\tb.sv`
  - `rv_timer_base_test.sv`:L1 — `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_base_test.sv`
  - `rv_timer_test_pkg.sv`:L1 — `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv`
  - `rv_timer_bind_fpv.sv`:L1 — `opentitan\hw\ip\rv_timer\fpv\tb\rv_timer_bind_fpv.sv`
  - `rv_timer_bind_fpv`:L9 — `opentitan\hw\ip\rv_timer\fpv\tb\rv_timer_bind_fpv.sv`
**SVA** (6)
  - `rv_timer_bind.sv`:L1 — `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv`
  - `rv_timer_bind`:L5 — `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv`
  - `rv_timer_core_assert_fpv.sv`:L1 — `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_core_assert_fpv.sv`
  - `rv_timer_core_assert_fpv`:L8 — `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_core_assert_fpv.sv`
  - `rv_timer_interrupts_assert_fpv.sv`:L1 — `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_interrupts_assert_fpv.sv`
  - `rv_timer_interrupts_assert_fpv`:L8 — `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_interrupts_assert_fpv.sv`
**OTHER_CODE** (2)
  - `reg_timer.py`:L1 — `opentitan\hw\ip\rv_timer\util\reg_timer.py`
  - `main()`:L14 — `opentitan\hw\ip\rv_timer\util\reg_timer.py`

## Neighbor Components

- `rv_plic` (6 refs; instantiates×6)
- `lowrisc_ibex` (4 refs; instantiates×2, calls×1, imports_from×1)
- `pwrmgr` (2 refs; instantiates×2)
- `gpio` (1 refs; imports_from×1)
- `rstmgr` (1 refs; imports_from×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_interrupts_assert_fpv.sv` | `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_interrupts_assert_fpv.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_interrupts_assert_fpv` | `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_interrupts_assert_fpv.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_core_assert_fpv.sv` | `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_core_assert_fpv.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_core_assert_fpv` | `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_core_assert_fpv.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_base_test.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_base_test.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_env_pkg` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_test_pkg.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_bind_fpv.sv` | `opentitan\hw\ip\rv_timer\fpv\tb\rv_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_bind_fpv` | `opentitan\hw\ip\rv_timer\fpv\tb\rv_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_bind.sv` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_bind` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_reg_pkg` | `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_reg_pkg.sv` | `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_pkg.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_reg_top.sv` | `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_reg_top` | `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer.sv` | `opentitan\hw\ip\rv_timer\rtl\rv_timer.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer` | `opentitan\hw\ip\rv_timer\rtl\rv_timer.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_reg_top` | `opentitan\hw\ip\rv_timer\rtl\rv_timer.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_test_pkg` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `timer_core.sv` | `opentitan\hw\ip\rv_timer\rtl\timer_core.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `timer_core` | `opentitan\hw\ip\rv_timer\rtl\timer_core.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `tb.sv` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `tb` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `reg_timer.py` | `opentitan\hw\ip\rv_timer\util\reg_timer.py` |
| `spec_component_matches_code` | `component:rv_timer` | `main()` | `opentitan\hw\ip\rv_timer\util\reg_timer.py` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `rv_timer_bind.sv` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `rv_timer_bind` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `tb.sv` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `tb` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `rv_timer_env_pkg` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `rv_timer_test_pkg` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `rv_timer_base_test.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_base_test.sv` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `rv_timer_test_pkg.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `rv_timer_bind.sv` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `rv_timer_bind` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `rv_timer_env_pkg` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `rv_timer_test_pkg` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `rv_timer_base_test.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_base_test.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `rv_timer_test_pkg.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `rv_timer_bind.sv` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `rv_timer_bind` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `tb` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `rv_timer_env_pkg` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `rv_timer_test_pkg` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `rv_timer_base_test.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_base_test.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `rv_timer_test_pkg.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_timer_bind.sv` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_timer_bind` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_timer_env_pkg` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_timer_test_pkg` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_timer_base_test.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_base_test.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_timer_test_pkg.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rv_timer_bind.sv` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rv_timer_bind` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |

## Retrieval Guidance

- For code-only queries mentioning `rv_timer`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `rv_timer`.
