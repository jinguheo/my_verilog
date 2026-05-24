# Hardware Description: soc_dbg_ctrl

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`soc_dbg_ctrl`** has the following hardware interfaces defined
- **Inter-Module Signals**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`soc_dbg_ctrl`** has the following hardware interfaces defined

## Identity

- `ip_block`: `soc_dbg_ctrl`
- `bridge_edge_count`: 95
- Spec categories: document: 81, testplan: 28, component: 24, interface: 14, theory: 10
- Code categories: dv: 66, rtl: 29, sva: 22
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 23

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/soc_dbg_ctrl/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`soc_dbg_ctrl`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/soc_dbg_ctrl/doc/interfaces.md`_

```
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`soc_dbg_ctrl`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`core_tl`**, **`jtag_tl`**
- Bus Host Interfaces (TL-UL): *none*
- Peripheral Pins for Chip IO:
…
```

### Security Alerts
_Source: `opentitan/hw/ip/soc_dbg_ctrl/doc/interfaces.md`_

```
| lc_raw_test_rma    | lc_ctrl_pkg::lc_tx               | uni     | rcv   |       1 | Test enable qualifier coming from life cycle controller. This signals enables RAW, TEST and RMA mode accesses.                                             |
| lc_cpu_en          | lc_ctrl_pkg::lc_tx               | uni     | rcv   |       1 | CPU enable qualifier coming from life cycle controller. Indication from
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/soc_dbg_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

TODO (#26949)
```

### Summary of the core interface's registers
_Source: `opentitan/hw/ip/soc_dbg_ctrl/doc/registers.md`_

```
# Registers

The RoT shall define three registers and drive the debug policy bus from that.
These registers are updated by the RoT FW and are distributed by the debug policy bus to all consumers, e.g., HW TAPs in the system.
Depending on the configured debug category, a consumer might accept the debug command or not (if it is not part of the selected debug category).

<!-- BEGIN CMDGEN util/regtoo
…
```

### ALERT TEST
_Source: `opentitan/hw/ip/soc_dbg_ctrl/doc/registers.md`_

```
| soc_dbg_ctrl.[`ALERT_TEST`](#alert_test)                                               | 0x0      |        4 | Alert Test Register                                                                                         |
| soc_dbg_ctrl.[`DEBUG_POLICY_VALID_SHADOWED`](#debug_policy_valid_shadowed)             | 0x4      |        4 | Debug Policy Valid.
…
```

### Fields
_Source: `opentitan/hw/ip/soc_dbg_ctrl/doc/registers.md`_

```
| soc_dbg_ctrl.[`STATUS`](#status)                                                       | 0x18     |        4 | Debug Status Register                                                                                       |

## ALERT_TEST
Alert Test Register
- Offset: `0x0`
- Reset default: `0x0`
- Reset mask: `0x3`

### Fields

```wavejson
{"reg": [{"name": "fatal_fault", "bits": 1, "attr": ["wo"]
…
```

### Theory of Operation
_Source: `opentitan/hw/ip/soc_dbg_ctrl/doc/theory_of_operation.md`_

```
# Theory of Operation

TODO (#26949)
```

## Spec Anchors

- `component:soc_dbg_ctrl` (L1) — `__graphify_spec_only__/components.md`
- `soc_dbg_ctrl.hjson` (L1) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl.hjson`
- `human name` (L7) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl.hjson`
- `one line desc` (L8) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl.hjson`
- `one paragraph desc` (L9) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl.hjson`
- `cip id` (L15) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl.hjson`
- `design spec` (L16) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl.hjson`
- `dv doc` (L17) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl.hjson`
- `hw checklist` (L18) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl.hjson`
- `sw checklist` (L19) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl.hjson`
- `revisions` (L20) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl.hjson`
- `version` (L22) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl.hjson`
- `soc_dbg_ctrl_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl_sec_cm_testplan.hjson`
- `soc_dbg_ctrl_testplan.hjson` (L1) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl_testplan.hjson`
- `import testplans` (L7) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl_testplan.hjson`
- `testpoints` (L10) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl_testplan.hjson`
- `desc` (L13) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl_testplan.hjson`
- `stage` (L22) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl_testplan.hjson`
- `tests` (L23) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl_testplan.hjson`
- `covergroups` (L33) — `opentitan/hw/ip/soc_dbg_ctrl/data/soc_dbg_ctrl_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/soc_dbg_ctrl/doc/checklist.md`
- `Design Checklist` (L13) — `opentitan/hw/ip/soc_dbg_ctrl/doc/checklist.md`
- `D1` (L15) — `opentitan/hw/ip/soc_dbg_ctrl/doc/checklist.md`
- `D2` (L41) — `opentitan/hw/ip/soc_dbg_ctrl/doc/checklist.md`
- `D2S` (L83) — `opentitan/hw/ip/soc_dbg_ctrl/doc/checklist.md`
- `D3` (L103) — `opentitan/hw/ip/soc_dbg_ctrl/doc/checklist.md`
- `Verification Checklist` (L129) — `opentitan/hw/ip/soc_dbg_ctrl/doc/checklist.md`
- `V1` (L131) — `opentitan/hw/ip/soc_dbg_ctrl/doc/checklist.md`
- `V2` (L181) — `opentitan/hw/ip/soc_dbg_ctrl/doc/checklist.md`
- `V2S` (L227) — `opentitan/hw/ip/soc_dbg_ctrl/doc/checklist.md`
- `V3` (L243) — `opentitan/hw/ip/soc_dbg_ctrl/doc/checklist.md`

## Code Evidence

**RTL** (15)
  - `soc_dbg_ctrl.sv`:L1 — `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl.sv`
  - `soc_dbg_ctrl`:L7 — `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl.sv`
  - `soc_dbg_ctrl_pkg`:L10 — `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl.sv`
  - `soc_dbg_ctrl_reg_pkg`:L22 — `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_jtag_reg_top.sv`
  - `soc_dbg_ctrl_core_reg_top`:L93 — `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl.sv`
  - `soc_dbg_ctrl_jtag_reg_top`:L106 — `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl.sv`
  - `soc_dbg_ctrl_core_reg_top.sv`:L1 — `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_core_reg_top.sv`
  - `soc_dbg_ctrl_core_reg_top`:L9 — `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_core_reg_top.sv`
  - `soc_dbg_ctrl_decode.sv`:L1 — `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_decode.sv`
  - `soc_dbg_ctrl_decode`:L5 — `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_decode.sv`
  - `soc_dbg_ctrl_jtag_reg_top.sv`:L1 — `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_jtag_reg_top.sv`
  - `soc_dbg_ctrl_jtag_reg_top`:L9 — `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_jtag_reg_top.sv`
  - `soc_dbg_ctrl_pkg.sv`:L1 — `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_pkg.sv`
  - `soc_dbg_ctrl_reg_pkg.sv`:L1 — `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_reg_pkg.sv`
  - `soc_dbg_ctrl`:L2627 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
**DV** (6)
  - `tb.sv`:L1 — `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv`
  - `soc_dbg_ctrl_env_pkg`:L9 — `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_test_pkg.sv`
  - `soc_dbg_ctrl_test_pkg`:L10 — `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv`
  - `soc_dbg_ctrl_base_test.sv`:L1 — `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_base_test.sv`
  - `soc_dbg_ctrl_test_pkg.sv`:L1 — `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_test_pkg.sv`
**SVA** (2)
  - `soc_dbg_ctrl_bind.sv`:L1 — `opentitan\hw\ip\soc_dbg_ctrl\dv\sva\soc_dbg_ctrl_bind.sv`
  - `soc_dbg_ctrl_bind`:L5 — `opentitan\hw\ip\soc_dbg_ctrl\dv\sva\soc_dbg_ctrl_bind.sv`

## Neighbor Components

- `rv_plic` (12 refs; instantiates×12)
- `flash_ctrl` (3 refs; instantiates×3)
- `lowrisc_ibex` (2 refs; instantiates×1, imports_from×1)
- `pwrmgr` (2 refs; imports_from×1, instantiates×1)
- `rv_core_ibex` (1 refs; imports_from×1)
- `pulp_riscv_dbg` (1 refs; instantiates×1)
- `ac_range_check` (1 refs; instantiates×1)
- `rstmgr` (1 refs; imports_from×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_base_test.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_env_pkg` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_test_pkg.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_reg_pkg` | `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_jtag_reg_top.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_core_reg_top.sv` | `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_core_reg_top.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_core_reg_top` | `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_core_reg_top.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_jtag_reg_top.sv` | `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_jtag_reg_top.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_jtag_reg_top` | `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_jtag_reg_top.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_bind.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\sva\soc_dbg_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_bind` | `opentitan\hw\ip\soc_dbg_ctrl\dv\sva\soc_dbg_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_reg_pkg.sv` | `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_decode.sv` | `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_decode.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_decode` | `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_decode.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_pkg.sv` | `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl.sv` | `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl` | `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_pkg` | `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_core_reg_top` | `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_jtag_reg_top` | `opentitan\hw\ip\soc_dbg_ctrl\rtl\soc_dbg_ctrl.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `soc_dbg_ctrl_test_pkg` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `tb.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:soc_dbg_ctrl` | `tb` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl.hjson` | `tb.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl.hjson` | `tb` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl.hjson` | `soc_dbg_ctrl_env_pkg` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl.hjson` | `soc_dbg_ctrl_test_pkg` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl.hjson` | `soc_dbg_ctrl_bind.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\sva\soc_dbg_ctrl_bind.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl.hjson` | `soc_dbg_ctrl_bind` | `opentitan\hw\ip\soc_dbg_ctrl\dv\sva\soc_dbg_ctrl_bind.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl.hjson` | `soc_dbg_ctrl_base_test.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_base_test.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl.hjson` | `soc_dbg_ctrl_test_pkg.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_sec_cm_testplan.hjson` | `soc_dbg_ctrl_env_pkg` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_sec_cm_testplan.hjson` | `soc_dbg_ctrl_test_pkg` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_sec_cm_testplan.hjson` | `soc_dbg_ctrl_bind.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\sva\soc_dbg_ctrl_bind.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_sec_cm_testplan.hjson` | `soc_dbg_ctrl_bind` | `opentitan\hw\ip\soc_dbg_ctrl\dv\sva\soc_dbg_ctrl_bind.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_sec_cm_testplan.hjson` | `soc_dbg_ctrl_base_test.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_base_test.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_sec_cm_testplan.hjson` | `soc_dbg_ctrl_test_pkg.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_testplan.hjson` | `tb` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_testplan.hjson` | `soc_dbg_ctrl_env_pkg` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_testplan.hjson` | `soc_dbg_ctrl_test_pkg` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_testplan.hjson` | `soc_dbg_ctrl_bind.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\sva\soc_dbg_ctrl_bind.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_testplan.hjson` | `soc_dbg_ctrl_bind` | `opentitan\hw\ip\soc_dbg_ctrl\dv\sva\soc_dbg_ctrl_bind.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_testplan.hjson` | `soc_dbg_ctrl_base_test.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_base_test.sv` |
| `spec_path_matches_code_path` | `soc_dbg_ctrl_testplan.hjson` | `soc_dbg_ctrl_test_pkg.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `soc_dbg_ctrl_env_pkg` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `soc_dbg_ctrl_test_pkg` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `soc_dbg_ctrl_bind.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\sva\soc_dbg_ctrl_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `soc_dbg_ctrl_bind` | `opentitan\hw\ip\soc_dbg_ctrl\dv\sva\soc_dbg_ctrl_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `soc_dbg_ctrl_base_test.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_base_test.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `soc_dbg_ctrl_test_pkg.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `soc_dbg_ctrl_env_pkg` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tests\soc_dbg_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `soc_dbg_ctrl_test_pkg` | `opentitan\hw\ip\soc_dbg_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `soc_dbg_ctrl_bind.sv` | `opentitan\hw\ip\soc_dbg_ctrl\dv\sva\soc_dbg_ctrl_bind.sv` |

## Retrieval Guidance

- For code-only queries mentioning `soc_dbg_ctrl`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `soc_dbg_ctrl`.
