# Hardware Description: lc_ctrl

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Note that parameters prefixed with `RndCnst` are random netlist constants that need to be regenerated via topgen before the tapeout (typically by the silicon creator).
- **Parameters**: Note that parameters prefixed with `RndCnst` are random netlist constants that need to be regenerated via topgen before the tapeout (typically by the silicon creator).
- **Signals**: `AlertAsyncOn` | 2'b11 | 2'b11 |

## Identity

- `ip_block`: `lc_ctrl`
- `bridge_edge_count`: 192
- Spec categories: document: 181, component: 41, testplan: 34, interface: 21, theory: 19
- Code categories: dv: 136, rtl: 95, sva: 4
- Bridge relations: spec_path_matches_code_path: 152, spec_component_matches_code: 40

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/lc_ctrl/doc/interfaces.md`_

```
# Hardware Interfaces

### Parameters

Note that parameters prefixed with `RndCnst` are random netlist constants that need to be regenerated via topgen before the tapeout (typically by the silicon creator).

Parameter                        | Default (Max)  | Top Earlgrey   | Description
---------------------------------|----------------|----------------|---------------
```

### Parameters
_Source: `opentitan/hw/ip/lc_ctrl/doc/interfaces.md`_

```
# Hardware Interfaces

### Parameters

Note that parameters prefixed with `RndCnst` are random netlist constants that need to be regenerated via topgen before the tapeout (typically by the silicon creator).

Parameter                        | Default (Max)  | Top Earlgrey   | Description
---------------------------------|----------------|----------------|---------------
`AlertAsyncOn`
…
```

### Signals
_Source: `opentitan/hw/ip/lc_ctrl/doc/interfaces.md`_

```
`AlertAsyncOn`                   | 2'b11          | 2'b11          |
`IdcodeValue`                    | `32'h00000001` | `32'h00000001` | Idcode for the LC JTAG TAP.
`RndCnstLcKeymgrDivInvalid`      | (see RTL)      | (see RTL)      | Diversification value used for all invalid life cycle states.
`RndCnstLcKeymgrDivTestUnlocked` | (see RTL)      | (see RTL)      | Diversification value used for the
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/lc_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

The register layout and offsets shown in the [register table](registers.md) below are identical for both the CSR and JTAG TAP interfaces.
Hence the following programming sequences apply to both SW running on the device and SW running on the test appliance that accesses life cycle through the TAP.

## Regular Life Cycle Transitions

1. In order to perform a life cycle transiti
…
```

### Regular Life Cycle Transitions
_Source: `opentitan/hw/ip/lc_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

The register layout and offsets shown in the [register table](registers.md) below are identical for both the CSR and JTAG TAP interfaces.
Hence the following programming sequences apply to both SW running on the device and SW running on the test appliance that accesses life cycle through the TAP.

## Regular Life Cycle Transitions

1. In order to perform a life cycle transiti
…
```

### Volatile RAW -> TEST UNLOCKED0 Transition
_Source: `opentitan/hw/ip/lc_ctrl/doc/programmers_guide.md`_

```
9. Reset the device so that the new life cycle state becomes effective.

Note that all life cycle state transition increments the `LC_TRANSITION_CNT` and moves the life cycle state into the temporary POST_TRANSITION state - even if the transition was unsuccessful.
Hence, step 8. cannot be carried out in case device SW is used to implement the programming sequence above, since the processor is disa
…
```

### Summary of the regs interface's registers
_Source: `opentitan/hw/ip/lc_ctrl/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/lc_ctrl/data/lc_ctrl.hjson -->
## Summary of the **`regs`** interface's registers

| Name                                                                | Offset   |   Length | Description                                                                              |
|:--------------------------------------------------------------------|:--
…
```

### ALERT TEST
_Source: `opentitan/hw/ip/lc_ctrl/doc/registers.md`_

```
| lc_ctrl.[`MANUF_STATE_1`](#manuf_state)                             | 0x70     |        4 | This is a 256bit field used for keeping track of the manufacturing state.                |
| lc_ctrl.[`MANUF_STATE_2`](#manuf_state)                             | 0x74     |        4 | This is a 256bit field used for keeping track of the manufacturing state.                |
| lc_ctrl.[`MANUF_STATE_3`](#m
…
```

## Spec Anchors

- `component:lc_ctrl` (L1) — `__graphify_spec_only__/components.md`
- `lc_ctrl.hjson` (L1) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `human name` (L6) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `one line desc` (L7) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `one paragraph desc` (L8) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `cip id` (L13) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `design spec` (L14) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `dv doc` (L15) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `hw checklist` (L16) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `sw checklist` (L17) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `version` (L18) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `life stage` (L19) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `lc_ctrl_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `stage` (L32) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `tests` (L33) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `TRANSITION.CONFIG.REGWEN` (L38) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `MANUF.STATE.SPARSE` (L51) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `TRANSITION.CTR.SPARSE` (L61) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `MANUF.STATE.BKGN CHK` (L71) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `TRANSITION.CTR.BKGN CHK` (L81) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `STATE.CONFIG.SPARSE` (L91) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `lc_ctrl_state.hjson` (L1) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `secded` (L12) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `data width` (L13) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `ecc width` (L14) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `ecc matrix` (L15) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `min hw` (L28) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `max hw` (L29) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `min hd` (L30) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `token size` (L33) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `tokens` (L34) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `lc state` (L47) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `lc_ctrl_testplan.hjson` (L1) — `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_testplan.hjson`

## Code Evidence

**RTL** (29)
  - `lc_ctrl_state_pkg`:L10 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv`
  - `lc_ctrl_reg_pkg`:L22 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv`
  - `lc_ctrl.sv`:L1 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv`
  - `lc_ctrl`:L10 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv`
  - `lc_ctrl_regs_reg_top`:L153 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv`
  - `lc_ctrl_kmac_if`:L748 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv`
  - `lc_ctrl_fsm`:L770 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv`
  - `lc_ctrl_dmi_reg_top.sv`:L1 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_dmi_reg_top.sv`
  - `lc_ctrl_dmi_reg_top`:L9 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_dmi_reg_top.sv`
  - `lc_ctrl_fsm.sv`:L1 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv`
  - `lc_ctrl_fsm`:L9 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv`
  - `lc_ctrl_token_pkg`:L113 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv`
  - `lc_ctrl_state_decode`:L764 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv`
  - `lc_ctrl_state_transition`:L777 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv`
  - `lc_ctrl_signal_decode`:L794 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv`
  - `lc_ctrl_kmac_if.sv`:L1 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_kmac_if.sv`
  - `lc_ctrl_kmac_if`:L10 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_kmac_if.sv`
  - `lc_ctrl_pkg.sv`:L1 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_pkg.sv`
  - `lc_ctrl_regs_reg_top.sv`:L1 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv`
  - `lc_ctrl_regs_reg_top`:L9 — `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv`
**DV** (13)
  - `tb.sv`:L1 — `opentitan\hw\ip\lc_ctrl\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\lc_ctrl\dv\tb.sv`
  - `lc_ctrl_env_pkg`:L10 — `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv`
  - `lc_ctrl_test_pkg`:L13 — `opentitan\hw\ip\lc_ctrl\dv\tb.sv`
  - `jtag_riscv_agent_pkg`:L15 — `opentitan\hw\ip\lc_ctrl\dv\tb.sv`
  - `lc_ctrl_dv_utils_pkg`:L16 — `opentitan\hw\ip\lc_ctrl\dv\tb.sv`
  - `lc_ctrl_if`:L64 — `opentitan\hw\ip\lc_ctrl\dv\tb.sv`
  - `lc_ctrl_cov_bind.sv`:L1 — `opentitan\hw\ip\lc_ctrl\dv\cov\lc_ctrl_cov_bind.sv`
  - `lc_ctrl_cov_bind`:L6 — `opentitan\hw\ip\lc_ctrl\dv\cov\lc_ctrl_cov_bind.sv`
  - `lc_ctrl_fsm_cov_if.sv`:L1 — `opentitan\hw\ip\lc_ctrl\dv\cov\lc_ctrl_fsm_cov_if.sv`
  - `lc_tx_cov_array_if.sv`:L1 — `opentitan\hw\ip\lc_ctrl\dv\cov\lc_tx_cov_array_if.sv`
  - `lc_ctrl_base_test.sv`:L1 — `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_base_test.sv`
  - `lc_ctrl_test_pkg.sv`:L1 — `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv`
**SVA** (2)
  - `lc_ctrl_bind.sv`:L1 — `opentitan\hw\ip\lc_ctrl\dv\sva\lc_ctrl_bind.sv`
  - `lc_ctrl_bind`:L5 — `opentitan\hw\ip\lc_ctrl\dv\sva\lc_ctrl_bind.sv`

## Neighbor Components

- `pwrmgr` (11 refs; imports_from×8, instantiates×3)
- `rv_core_ibex` (8 refs; instantiates×7, imports_from×1)
- `rv_plic` (7 refs; instantiates×7)
- `lowrisc_ibex` (5 refs; instantiates×3, imports_from×2)
- `otp_ctrl` (3 refs; imports_from×3)
- `pulp_riscv_dbg` (2 refs; instantiates×2)
- `lowrisc_ip` (1 refs; imports_from×1)
- `rstmgr` (1 refs; imports_from×1)
- `rom_ctrl` (1 refs; instantiates×1)
- `prim` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_transition.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_transition` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_base_test.sv` | `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_env_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_fsm_cov_if.sv` | `opentitan\hw\ip\lc_ctrl\dv\cov\lc_ctrl_fsm_cov_if.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_test_pkg.sv` | `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_signal_decode.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_signal_decode.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_signal_decode` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_signal_decode.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_reg_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_regs_reg_top.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_regs_reg_top` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_decode.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_decode.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_decode` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_decode.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_cov_bind.sv` | `opentitan\hw\ip\lc_ctrl\dv\cov\lc_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_cov_bind` | `opentitan\hw\ip\lc_ctrl\dv\cov\lc_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_dmi_reg_top.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_dmi_reg_top.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_dmi_reg_top` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_dmi_reg_top.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_pkg.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_pkg.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_bind.sv` | `opentitan\hw\ip\lc_ctrl\dv\sva\lc_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_bind` | `opentitan\hw\ip\lc_ctrl\dv\sva\lc_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_kmac_if.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_kmac_if.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_kmac_if` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_kmac_if.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_reg_pkg.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_fsm.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_fsm` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_token_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_decode` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_transition` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_signal_decode` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_pkg.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_regs_reg_top` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_kmac_if` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_fsm` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_test_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_dv_utils_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_if` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `lc_ctrl_state_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `tb.sv` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `tb` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `lc_ctrl_reg_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `lc_ctrl_env_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `lc_ctrl_test_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `jtag_riscv_agent_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `lc_ctrl_dv_utils_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `lc_ctrl_state_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `lc_ctrl_reg_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `lc_ctrl_env_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `lc_ctrl_test_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `jtag_riscv_agent_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `lc_ctrl_dv_utils_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_state.hjson` | `lc_ctrl_state_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_state.hjson` | `tb.sv` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_state.hjson` | `tb` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_state.hjson` | `lc_ctrl_reg_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv` |

## Retrieval Guidance

- For code-only queries mentioning `lc_ctrl`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `lc_ctrl`.
