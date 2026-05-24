# Hardware Description: keymgr_dpe

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`keymgr_dpe`** has the following hardware interfaces defined
- **Inter-Module Signals**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`keymgr_dpe`** has the following hardware interfaces defined

## Identity

- `ip_block`: `keymgr_dpe`
- `bridge_edge_count`: 107
- Spec categories: document: 83, component: 36, testplan: 29, theory: 19, interface: 14
- Code categories: rtl: 101, dv: 36, sva: 4
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 35

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/keymgr_dpe/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/keymgr_dpe/data/keymgr_dpe.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`keymgr_dpe`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_edn_i`**
- Bus Dev
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/keymgr_dpe/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/keymgr_dpe/data/keymgr_dpe.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`keymgr_dpe`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_edn_i`**
- Bus Device Interfaces (TL-UL):
…
```

### Interrupts
_Source: `opentitan/hw/ip/keymgr_dpe/doc/interfaces.md`_

```
| otp_key         | otp_ctrl_pkg::otp_keymgr_key | uni     | rcv   |       1 |               |
| otp_device_id   | otp_ctrl_pkg::otp_device_id  | uni     | rcv   |       1 |               |
| lc_keymgr_en    | lc_ctrl_pkg::lc_tx           | uni     | rcv   |       1 |               |
| lc_keymgr_div   | lc_ctrl_pkg::lc_keymgr_div   | uni     | rcv   |       1 |               |
| rom_digest      |
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/keymgr_dpe/doc/programmers_guide.md`_

```
# Programmer's Guide

Before initiating any of the following key generation operations, it is recommended (but not mandatory) to check that keymgr_dpe is ready to handle them.
Except for the first advance call that initializes keymgr_dpe, this means keymgr_dpe is idle (as reported in `OP_STATUS`) and FSM is in `Available` state (reported in `WORKING_STATE`).

Similarly, at the end of the operation
…
```

### Initialize first advance call
_Source: `opentitan/hw/ip/keymgr_dpe/doc/programmers_guide.md`_

```
# Programmer's Guide

Before initiating any of the following key generation operations, it is recommended (but not mandatory) to check that keymgr_dpe is ready to handle them.
Except for the first advance call that initializes keymgr_dpe, this means keymgr_dpe is idle (as reported in `OP_STATUS`) and FSM is in `Available` state (reported in `WORKING_STATE`).

Similarly, at the end of the operation
…
```

### Advance
_Source: `opentitan/hw/ip/keymgr_dpe/doc/programmers_guide.md`_

```
Keymgr_DPE is initialized by configuring the following CSR:
*  Set `CONTROL_SHADOWED.OPERATION` to `Advance`.
*  Set `CONTROL_SHADOWED.SLOT_DST_SEL` to the destination slot to which UDS should be latched.
*  Set `START` to initiate the operation.

At the end of the successful first advance call, the UDS is latched into the specified destination slot.

## Advance

This section specifically addresse
…
```

### Summary
_Source: `opentitan/hw/ip/keymgr_dpe/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/keymgr_dpe/data/keymgr_dpe.hjson -->
## Summary

| Name                                                               | Offset   |   Length | Description                                                                |
|:-------------------------------------------------------------------|:---------|---------:|:------------------------------
…
```

### INTR STATE
_Source: `opentitan/hw/ip/keymgr_dpe/doc/registers.md`_

```
| keymgr_dpe.[`SW_SHARE1_OUTPUT_7`](#sw_share1_output)               | 0xbc     |        4 | Key manager software output.                                               |
| keymgr_dpe.[`WORKING_STATE`](#working_state)                       | 0xc0     |        4 | Key manager working state.                                                 |
| keymgr_dpe.[`OP_STATUS`](#op_status)
…
```

## Spec Anchors

- `component:keymgr_dpe` (L1) — `__graphify_spec_only__/components.md`
- `keymgr_dpe.hjson` (L1) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `human name` (L6) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `one line desc` (L7) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `one paragraph desc` (L8) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `cip id` (L13) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `design spec` (L14) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `dv doc` (L15) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `hw checklist` (L16) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `sw checklist` (L17) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `revisions` (L18) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `version` (L20) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `keymgr_dpe_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_sec_cm_testplan.hjson`
- `keymgr_dpe_testplan.hjson` (L1) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `testpoints` (L14) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `desc` (L17) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `Stimulus` (L21) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `Checks` (L30) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `stage` (L38) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `tests` (L39) — `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `KEYMGR Checklist` (L1) — `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `D2` (L34) — `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `D2S` (L76) — `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `D3` (L96) — `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `Verification Checklist` (L122) — `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `V1` (L124) — `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `V2` (L174) — `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`

## Code Evidence

**RTL** (24)
  - `prim_sec_anchor_const`:L105 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
  - `keymgr_reseed_ctrl`:L179 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
  - `keymgr_cfg_en`:L343 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
  - `keymgr_input_checks`:L508 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
  - `keymgr_kmac_if`:L582 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
  - `keymgr_sideload_key_ctrl`:L614 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
  - `keymgr_dpe.sv`:L1 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
  - `keymgr_dpe`:L10 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
  - `keymgr_dpe_pkg`:L11 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_op_state_ctrl.sv`
  - `keymgr_dpe_reg_pkg`:L26 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_reg_top.sv`
  - `keymgr_dpe_reg_top`:L129 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
  - `keymgr_dpe_ctrl`:L279 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
  - `keymgr_dpe_ctrl.sv`:L1 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv`
  - `keymgr_dpe_ctrl`:L10 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv`
  - `keymgr_dpe_op_state_ctrl`:L610 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv`
  - `keymgr_data_en_state`:L632 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv`
  - `keymgr_err`:L694 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv`
  - `keymgr_dpe_op_state_ctrl.sv`:L1 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_op_state_ctrl.sv`
  - `keymgr_dpe_op_state_ctrl`:L10 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_op_state_ctrl.sv`
  - `keymgr_dpe_pkg.sv`:L1 — `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_pkg.sv`
**DV** (9)
  - `tb.sv`:L1 — `opentitan\hw\ip\keymgr_dpe\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\keymgr_dpe\dv\tb.sv`
  - `keymgr_dpe_env_pkg`:L9 — `opentitan\hw\ip\keymgr_dpe\dv\tests\keymgr_dpe_test_pkg.sv`
  - `keymgr_dpe_test_pkg`:L10 — `opentitan\hw\ip\keymgr_dpe\dv\tb.sv`
  - `keymgr_dpe_if`:L26 — `opentitan\hw\ip\keymgr_dpe\dv\tb.sv`
  - `keymgr_dpe_cov_bind.sv`:L1 — `opentitan\hw\ip\keymgr_dpe\dv\cov\keymgr_dpe_cov_bind.sv`
  - `keymgr_dpe_cov_bind`:L6 — `opentitan\hw\ip\keymgr_dpe\dv\cov\keymgr_dpe_cov_bind.sv`
  - `keymgr_dpe_base_test.sv`:L1 — `opentitan\hw\ip\keymgr_dpe\dv\tests\keymgr_dpe_base_test.sv`
  - `keymgr_dpe_test_pkg.sv`:L1 — `opentitan\hw\ip\keymgr_dpe\dv\tests\keymgr_dpe_test_pkg.sv`
**SVA** (2)
  - `keymgr_dpe_bind.sv`:L1 — `opentitan\hw\ip\keymgr_dpe\dv\sva\keymgr_dpe_bind.sv`
  - `keymgr_dpe_bind`:L5 — `opentitan\hw\ip\keymgr_dpe\dv\sva\keymgr_dpe_bind.sv`

## Neighbor Components

- `rv_plic` (6 refs; instantiates×6)
- `keymgr` (6 refs; instantiates×6)
- `pwrmgr` (4 refs; instantiates×3, imports_from×1)
- `lowrisc_ibex` (3 refs; instantiates×2, imports_from×1)
- `flash_ctrl` (3 refs; instantiates×3)
- `otbn` (3 refs; imports_from×3)
- `rv_core_ibex` (2 refs; imports_from×1, instantiates×1)
- `sensor_ctrl` (1 refs; instantiates×1)
- `pulp_riscv_dbg` (1 refs; instantiates×1)
- `rstmgr` (1 refs; imports_from×1)
- `rom_ctrl` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_base_test.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tests\keymgr_dpe_base_test.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_env_pkg` | `opentitan\hw\ip\keymgr_dpe\dv\tests\keymgr_dpe_test_pkg.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_test_pkg.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tests\keymgr_dpe_test_pkg.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_pkg` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_op_state_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_op_state_ctrl.sv` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_op_state_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_op_state_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_op_state_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_cov_bind.sv` | `opentitan\hw\ip\keymgr_dpe\dv\cov\keymgr_dpe_cov_bind.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_cov_bind` | `opentitan\hw\ip\keymgr_dpe\dv\cov\keymgr_dpe_cov_bind.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_bind.sv` | `opentitan\hw\ip\keymgr_dpe\dv\sva\keymgr_dpe_bind.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_bind` | `opentitan\hw\ip\keymgr_dpe\dv\sva\keymgr_dpe_bind.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_reg_pkg` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_reg_top.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_reg_pkg.sv` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_reg_pkg.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_reg_top.sv` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_reg_top.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_reg_top` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_reg_top.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_ctrl.sv` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_op_state_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_pkg.sv` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_pkg.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe.sv` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_reg_top` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_test_pkg` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_if` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_data_en_state` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_err` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `prim_sec_anchor_const` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_reseed_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_cfg_en` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_input_checks` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_kmac_if` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_sideload_key_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `tb.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `tb` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `prim_sec_anchor_const` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `keymgr_reseed_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `keymgr_cfg_en` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `keymgr_input_checks` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `keymgr_kmac_if` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `keymgr_sideload_key_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `tb.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `tb` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `prim_sec_anchor_const` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `keymgr_reseed_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `keymgr_cfg_en` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `keymgr_input_checks` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `keymgr_kmac_if` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `keymgr_sideload_key_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `prim_sec_anchor_const` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `keymgr_reseed_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `keymgr_cfg_en` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `keymgr_input_checks` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `keymgr_kmac_if` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `keymgr_sideload_key_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `tb` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_sec_anchor_const` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |

## Retrieval Guidance

- For code-only queries mentioning `keymgr_dpe`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `keymgr_dpe`.
