# Hardware Description: adc_ctrl

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`adc_ctrl`** has the following hardware interfaces defined
- **Inter-Module Signals**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`adc_ctrl`** has the following hardware interfaces defined

## Identity

- `ip_block`: `adc_ctrl`
- `bridge_edge_count`: 104
- Spec categories: document: 84, component: 33, testplan: 30, interface: 16, theory: 16
- Code categories: dv: 81, rtl: 46, sva: 8
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 32

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/adc_ctrl/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/adc_ctrl/data/adc_ctrl.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`adc_ctrl`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_aon_i`**
- Bus Device In
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/adc_ctrl/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/adc_ctrl/data/adc_ctrl.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`adc_ctrl`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_aon_i`**
- Bus Device Interfaces (TL-UL): **`tl
…
```

### Interrupts
_Source: `opentitan/hw/ip/adc_ctrl/doc/interfaces.md`_

```
## [Inter-Module Signals](https://opentitan.org/book/doc/contributing/hw/comportability/index.html#inter-signal-handling)

| Port Name   | Package::Struct   | Type    | Act   |   Width | Description   |
|:------------|:------------------|:--------|:------|--------:|:--------------|
| adc         | ast_pkg::adc_ast  | req_rsp | req   |       1 |               |
| wkup_req    | logic             | u
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/adc_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

The controller should be initialized with the properties of the ADC and scan times.
* The ADC power up delay must be set in [`adc_pd_ctl.pwrup_time`](registers.md#adc_pd_ctl).
* The time to delay between samples in a slow scan should be set in [`adc_pd_ctl.wakeup_time`](registers.md#adc_pd_ctl).
* The number of samples to cause transition from slow to fast
…
```

### Initialization
_Source: `opentitan/hw/ip/adc_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

The controller should be initialized with the properties of the ADC and scan times.
* The ADC power up delay must be set in [`adc_pd_ctl.pwrup_time`](registers.md#adc_pd_ctl).
* The time to delay between samples in a slow scan should be set in [`adc_pd_ctl.wakeup_time`](registers.md#adc_pd_ctl).
* The number of samples to cause transition from slow to fast
…
```

### Running in normal mode
_Source: `opentitan/hw/ip/adc_ctrl/doc/programmers_guide.md`_

```
* The number of samples to cause transition from slow to fast scan should be set in [`adc_lp_sample_ctl`](registers.md#adc_lp_sample_ctl).
* The number of samples for debounce should be set in [`adc_sample_ctl`](registers.md#adc_sample_ctl).
* The filter registers [`adc_chnX_filter_ctlN`](registers.md#adc_chn0_filter_ctl) should be programmed.
* The interrupt [`adc_intr_ctl`](registers.md#adc_intr
…
```

### Summary
_Source: `opentitan/hw/ip/adc_ctrl/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/adc_ctrl/data/adc_ctrl.hjson -->
## Summary

| Name                                                     | Offset   |   Length | Description                               |
|:---------------------------------------------------------|:---------|---------:|:------------------------------------------|
| adc_ctrl.[`INTR_STATE`](#intr_state)
…
```

### INTR STATE
_Source: `opentitan/hw/ip/adc_ctrl/doc/registers.md`_

```
| adc_ctrl.[`adc_chn_val_0`](#adc_chn_val)                 | 0x64     |        4 | ADC value sampled on channel              |
| adc_ctrl.[`adc_chn_val_1`](#adc_chn_val)                 | 0x68     |        4 | ADC value sampled on channel              |
| adc_ctrl.[`adc_wakeup_ctl`](#adc_wakeup_ctl)             | 0x6c     |        4 | Enable filter matches as wakeups          |
| adc_ctrl.[`filter
…
```

## Spec Anchors

- `component:adc_ctrl` (L1) — `__graphify_spec_only__/components.md`
- `adc_ctrl.hjson` (L1) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `human name` (L5) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `one line desc` (L6) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `one paragraph desc` (L7) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `cip id` (L15) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `design spec` (L16) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `dv doc` (L17) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `hw checklist` (L18) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `sw checklist` (L19) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `version` (L20) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `life stage` (L21) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `adc_ctrl_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_sec_cm_testplan.hjson`
- `adc_ctrl_testplan.hjson` (L1) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `testpoints` (L12) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `desc` (L15) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `stage` (L31) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `tests` (L32) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `Stimulus` (L232) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `Checking` (L235) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `covergroups` (L244) — `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `ADC CTRL Checklist` (L1) — `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `Design Checklist` (L11) — `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `D1` (L13) — `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `D2` (L37) — `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `D2S` (L79) — `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `D3` (L99) — `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `Verification Checklist` (L125) — `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `V1` (L127) — `opentitan/hw/ip/adc_ctrl/doc/checklist.md`

## Code Evidence

**RTL** (19)
  - `adc_ctrl_pkg`:L11 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv`
  - `adc_ctrl.sv`:L1 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv`
  - `adc_ctrl`:L9 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv`
  - `adc_ctrl_reg_pkg`:L24 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_top.sv`
  - `adc_ctrl_reg_top`:L71 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv`
  - `adc_ctrl_core`:L85 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv`
  - `adc_ctrl_core.sv`:L1 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv`
  - `adc_ctrl_core`:L9 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv`
  - `adc_ctrl_fsm`:L153 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv`
  - `adc_ctrl_intr`:L193 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv`
  - `adc_ctrl_fsm.sv`:L1 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv`
  - `adc_ctrl_fsm`:L9 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv`
  - `adc_ctrl_intr.sv`:L1 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_intr.sv`
  - `adc_ctrl_intr`:L7 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_intr.sv`
  - `adc_ctrl_pkg.sv`:L1 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_pkg.sv`
  - `adc_ctrl_reg_pkg.sv`:L1 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_pkg.sv`
  - `adc_ctrl_reg_top.sv`:L1 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_top.sv`
  - `adc_ctrl_reg_top`:L9 — `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_top.sv`
  - `adc_ctrl`:L2047 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
**DV** (9)
  - `tb.sv`:L1 — `opentitan\hw\ip\adc_ctrl\dv\tb.sv`
  - `adc_ctrl_env_pkg`:L9 — `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv`
  - `adc_ctrl_test_pkg`:L34 — `opentitan\hw\ip\adc_ctrl\dv\tb.sv`
  - `tb`:L28 — `opentitan\hw\ip\adc_ctrl\dv\tb.sv`
  - `adc_ctrl_core_cov_if.sv`:L1 — `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_core_cov_if.sv`
  - `adc_ctrl_cov_bind.sv`:L1 — `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv`
  - `adc_ctrl_cov_bind`:L6 — `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv`
  - `adc_ctrl_base_test.sv`:L1 — `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_base_test.sv`
  - `adc_ctrl_test_pkg.sv`:L1 — `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv`
**SVA** (4)
  - `adc_ctrl_bind.sv`:L1 — `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_bind.sv`
  - `adc_ctrl_bind`:L5 — `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_bind.sv`
  - `adc_ctrl_fsm_sva_if.sv`:L1 — `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_fsm_sva_if.sv`
  - `adc_ctrl_sva_if.sv`:L1 — `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_sva_if.sv`

## Neighbor Components

- `rv_plic` (6 refs; instantiates×6)
- `pwrmgr` (4 refs; instantiates×4)
- `lowrisc_ibex` (2 refs; instantiates×1, imports_from×1)
- `rstmgr` (2 refs; instantiates×1, imports_from×1)
- `pinmux` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_core_cov_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_core_cov_if.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_base_test.sv` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_env_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_fsm_sva_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_fsm_sva_if.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_test_pkg.sv` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_cov_bind.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_cov_bind` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_sva_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_sva_if.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_bind.sv` | `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_bind` | `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_reg_pkg` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_reg_pkg.sv` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_reg_top.sv` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_reg_top` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_core.sv` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_core` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_fsm` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_intr` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_intr.sv` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_intr.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_intr` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_intr.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_pkg` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_fsm.sv` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_fsm` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_pkg.sv` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl.sv` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_reg_top` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_core` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_test_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `tb.sv` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `tb` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `tb.sv` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `adc_ctrl_env_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `adc_ctrl_test_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `tb` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `adc_ctrl_core_cov_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_core_cov_if.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `adc_ctrl_pkg` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `adc_ctrl_cov_bind.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `adc_ctrl_cov_bind` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `adc_ctrl_env_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `adc_ctrl_test_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `adc_ctrl_core_cov_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_core_cov_if.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `adc_ctrl_pkg` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `adc_ctrl_cov_bind.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `adc_ctrl_cov_bind` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `adc_ctrl_env_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `adc_ctrl_test_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `tb` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `adc_ctrl_core_cov_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_core_cov_if.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `adc_ctrl_pkg` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `adc_ctrl_cov_bind.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `adc_ctrl_cov_bind` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `adc_ctrl_env_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `adc_ctrl_test_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |

## Retrieval Guidance

- For code-only queries mentioning `adc_ctrl`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `adc_ctrl`.
