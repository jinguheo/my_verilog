# Hardware Description: rom_ctrl

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`rom_ctrl`** has the following hardware interfaces defined
- **Inter-Module Signals**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`rom_ctrl`** has the following hardware interfaces defined

## Identity

- `ip_block`: `rom_ctrl`
- `bridge_edge_count`: 112
- Spec categories: document: 77, component: 41, testplan: 28, interface: 16, theory: 16
- Code categories: dv: 79, rtl: 74, other_code: 60, sva: 4
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/rom_ctrl/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/rom_ctrl/data/rom_ctrl.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`rom_ctrl`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/rom_ctrl/doc/interfaces.md`_

```
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`rom_ctrl`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`regs_tl`**, **`rom_tl`**
- Bus Host Interfaces (TL-UL): *none*
- Peripheral Pins for Chip IO: *none
…
```

### Security Alerts
_Source: `opentitan/hw/ip/rom_ctrl/doc/interfaces.md`_

```
|:------------|:--------------------------|:--------|:------|--------:|:--------------|
| rom_cfg     | prim_rom_pkg::rom_cfg     | uni     | rcv   |       1 |               |
| pwrmgr_data | rom_ctrl_pkg::pwrmgr_data | uni     | req   |       1 |               |
| keymgr_data | rom_ctrl_pkg::keymgr_data | uni     | req   |       1 |               |
| kmac_data   | kmac_pkg::app             | req_
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/rom_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

Software will mostly interact with the ROM controller by fetching code or loading data from ROM.
For this, the block looks like a block of memory, accessible through a TL-UL window.
However, there are a few registers that are accessible.
Other than the standard [`ALERT_TEST`](registers.md#alert_test) register, all are read-only.

The [`FATAL_ALERT_CAUSE`](registers.md#fatal_a
…
```

### Device Interface Functions DIFs
_Source: `opentitan/hw/ip/rom_ctrl/doc/programmers_guide.md`_

```
The [`FATAL_ALERT_CAUSE`](registers.md#fatal_alert_cause) register might change value during operations (if an alert is signalled), but the other registers will all have fixed values by the time any software runs.

To get the computed ROM digest, software can read [`DIGEST_0`](registers.md#digest) through [`DIGEST_7`](registers.md#digest).
The ROM also contains an expected ROM digest.
Unlike the r
…
```

### Summary
_Source: `opentitan/hw/ip/rom_ctrl/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/rom_ctrl/data/rom_ctrl.hjson -->
## Summary

| Name                                               | Offset   |   Length | Description                                         |
|:---------------------------------------------------|:---------|---------:|:----------------------------------------------------|
| rom_ctrl.[`ALERT_TEST`](#alert_te
…
```

### ALERT TEST
_Source: `opentitan/hw/ip/rom_ctrl/doc/registers.md`_

```
| rom_ctrl.[`EXP_DIGEST_1`](#exp_digest)             | 0x2c     |        4 | The expected digest, stored in the top words of ROM |
| rom_ctrl.[`EXP_DIGEST_2`](#exp_digest)             | 0x30     |        4 | The expected digest, stored in the top words of ROM |
| rom_ctrl.[`EXP_DIGEST_3`](#exp_digest)             | 0x34     |        4 | The expected digest, stored in the top words of ROM |
| rom_c
…
```

### Fields
_Source: `opentitan/hw/ip/rom_ctrl/doc/registers.md`_

```
| rom_ctrl.[`EXP_DIGEST_7`](#exp_digest)             | 0x44     |        4 | The expected digest, stored in the top words of ROM |

## ALERT_TEST
Alert Test Register
- Offset: `0x0`
- Reset default: `0x0`
- Reset mask: `0x1`

### Fields

```wavejson
{"reg": [{"name": "fatal", "bits": 1, "attr": ["wo"], "rotate": -90}, {"bits": 31}], "config": {"lanes": 1, "fontsize": 10, "vspace": 80}}
```

|  Bit
…
```

## Spec Anchors

- `component:rom_ctrl` (L1) — `__graphify_spec_only__/components.md`
- `rom_ctrl.hjson` (L1) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `human name` (L6) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `one line desc` (L7) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `one paragraph desc` (L8) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `cip id` (L15) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `design spec` (L16) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `dv doc` (L17) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `hw checklist` (L18) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `sw checklist` (L19) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `revisions` (L20) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `version` (L22) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `rom_ctrl_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_sec_cm_testplan.hjson`
- `stage` (L33) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_sec_cm_testplan.hjson`
- `tests` (L34) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_sec_cm_testplan.hjson`
- `rom_ctrl_testplan.hjson` (L1) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_testplan.hjson`
- `testpoints` (L15) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_testplan.hjson`
- `desc` (L18) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_testplan.hjson`
- `stage` (L37) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_testplan.hjson`
- `tests` (L38) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_testplan.hjson`
- `covergroups` (L81) — `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `Rom Controller Checklist` (L1) — `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `D2` (L32) — `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `D2S` (L74) — `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `D3` (L94) — `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `Verification Checklist` (L120) — `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `V1` (L122) — `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `V2` (L172) — `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `V2S` (L218) — `opentitan/hw/ip/rom_ctrl/doc/checklist.md`

## Code Evidence

**RTL** (28)
  - `prim_prince`:L108 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv`
  - `prim_rom_pkg`:L25 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv`
  - `rom_ctrl_reg_pkg`:L20 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_rom_reg_top.sv`
  - `rom_ctrl.sv`:L1 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv`
  - `rom_ctrl`:L7 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv`
  - `rom_ctrl_pkg`:L50 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv`
  - `rom_ctrl_mux`:L235 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv`
  - `rom_ctrl_regs_reg_top`:L332 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv`
  - `rom_ctrl_compare.sv`:L1 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_compare.sv`
  - `rom_ctrl_compare`:L14 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_compare.sv`
  - `rom_ctrl_counter.sv`:L1 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_counter.sv`
  - `rom_ctrl_counter`:L33 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_counter.sv`
  - `rom_ctrl_fsm.sv`:L1 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv`
  - `rom_ctrl_fsm`:L47 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv`
  - `rom_ctrl_counter`:L113 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv`
  - `rom_ctrl_compare`:L131 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv`
  - `rom_ctrl_mux.sv`:L1 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_mux.sv`
  - `rom_ctrl_mux`:L9 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_mux.sv`
  - `rom_ctrl_pkg.sv`:L1 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_pkg.sv`
  - `rom_ctrl_regs_reg_top.sv`:L1 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_regs_reg_top.sv`
**DV** (15)
  - `kmac_app_intf`:L30 — `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv`
  - `rom_ctrl_cov_bind.sv`:L1 — `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv`
  - `rom_ctrl_cov_bind`:L6 — `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv`
  - `rom_ctrl_cov_if.sv`:L1 — `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_if.sv`
  - `tb.sv`:L1 — `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv`
  - `tb`:L8 — `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv`
  - `rom_ctrl_compare_if.sv`:L1 — `opentitan\hw\ip\rom_ctrl\dv\tb\rom_ctrl_compare_if.sv`
  - `rom_ctrl_fsm_if.sv`:L1 — `opentitan\hw\ip\rom_ctrl\dv\tb\rom_ctrl_fsm_if.sv`
  - `rom_ctrl_if.sv`:L1 — `opentitan\hw\ip\rom_ctrl\dv\tb\rom_ctrl_if.sv`
  - `tb.sv`:L1 — `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv`
  - `rom_ctrl_env_pkg`:L9 — `opentitan\hw\ip\rom_ctrl\dv\tests\rom_ctrl_test_pkg.sv`
  - `rom_ctrl_test_pkg`:L10 — `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv`
  - `rom_ctrl_base_test.sv`:L1 — `opentitan\hw\ip\rom_ctrl\dv\tests\rom_ctrl_base_test.sv`
  - `rom_ctrl_test_pkg.sv`:L1 — `opentitan\hw\ip\rom_ctrl\dv\tests\rom_ctrl_test_pkg.sv`
**SVA** (2)
  - `rom_ctrl_bind.sv`:L1 — `opentitan\hw\ip\rom_ctrl\dv\sva\rom_ctrl_bind.sv`
  - `rom_ctrl_bind`:L5 — `opentitan\hw\ip\rom_ctrl\dv\sva\rom_ctrl_bind.sv`
**OTHER_CODE** (5)
  - `gen_vivado_mem_image.py`:L1 — `opentitan\hw\ip\rom_ctrl\util\gen_vivado_mem_image.py`
  - `UpdatememSimulator`:L30 — `opentitan\hw\ip\rom_ctrl\util\gen_vivado_mem_image.py`
  - `.__init__()`:L33 — `opentitan\hw\ip\rom_ctrl\util\gen_vivado_mem_image.py`
  - `.write_updatemem_hex_string()`:L40 — `opentitan\hw\ip\rom_ctrl\util\gen_vivado_mem_image.py`
  - `.render_init_lines()`:L63 — `opentitan\hw\ip\rom_ctrl\util\gen_vivado_mem_image.py`

## Neighbor Components

- `lowrisc_ibex` (17 refs; calls×12, instantiates×3, imports_from×2)
- `rv_plic` (7 refs; instantiates×7)
- `riscv-tests` (6 refs; calls×6)
- `rv_core_ibex` (5 refs; imports_from×4, instantiates×1)
- `prim` (4 refs; instantiates×2, imports_from×2)
- `otp_ctrl` (4 refs; imports_from×4)
- `flash_ctrl` (2 refs; instantiates×2)
- `prim_generic` (2 refs; imports_from×2)
- `prim_xilinx` (2 refs; imports_from×2)
- `rstmgr` (2 refs; instantiates×1, imports_from×1)
- `pwrmgr` (1 refs; instantiates×1)
- `keymgr` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_base_test.sv` | `opentitan\hw\ip\rom_ctrl\dv\tests\rom_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_env_pkg` | `opentitan\hw\ip\rom_ctrl\dv\tests\rom_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_test_pkg.sv` | `opentitan\hw\ip\rom_ctrl\dv\tests\rom_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_scrambled_rom.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_scrambled_rom` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_compare_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\tb\rom_ctrl_compare_if.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_regs_reg_top.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_regs_reg_top` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_cov_bind.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_cov_bind` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_reg_pkg` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_rom_reg_top.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_rom_reg_top.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_rom_reg_top.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_rom_reg_top` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_rom_reg_top.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_cov_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_if.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_fsm_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\tb\rom_ctrl_fsm_if.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_bind.sv` | `opentitan\hw\ip\rom_ctrl\dv\sva\rom_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_bind` | `opentitan\hw\ip\rom_ctrl\dv\sva\rom_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_compare.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_compare.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_compare` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_compare.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_counter.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_counter.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_counter` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_counter.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_reg_pkg.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\tb\rom_ctrl_if.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_pkg` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_fsm.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_fsm` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_counter` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_compare` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_mux.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_mux.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_mux` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_mux.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_pkg.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_mux` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_regs_reg_top` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_test_pkg` | `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `prim_prince` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `prim_rom_pkg` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `prim_subst_perm` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `prim_prince` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `prim_rom_pkg` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `kmac_app_intf` | `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `rom_ctrl_cov_bind.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `rom_ctrl_cov_bind` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `rom_ctrl_cov_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_if.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `tb.sv` | `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `tb` | `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `prim_prince` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `prim_rom_pkg` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `kmac_app_intf` | `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `rom_ctrl_cov_bind.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `rom_ctrl_cov_bind` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `rom_ctrl_cov_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_if.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_testplan.hjson` | `prim_prince` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_testplan.hjson` | `prim_rom_pkg` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_testplan.hjson` | `kmac_app_intf` | `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_testplan.hjson` | `rom_ctrl_cov_bind.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |

## Retrieval Guidance

- For code-only queries mentioning `rom_ctrl`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `rom_ctrl`.
