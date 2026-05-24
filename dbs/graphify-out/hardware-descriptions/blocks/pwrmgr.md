# Hardware Description: pwrmgr

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Programmer's Guide**: The process in which the power manager is used is highly dependent on the system's topology.
- **Programmer Sequence for Entering Low Power**: The process in which the power manager is used is highly dependent on the system's topology.
- **Possible Exits**: 5. Configure low power mode configuration in [`CONTROL`](registers.md#control).

## Identity

- `ip_block`: `pwrmgr`
- `bridge_edge_count`: 568
- Spec categories: document: 466, testplan: 176, theory: 108, interface: 70, component: 41
- Code categories: rtl: 389, sva: 167, dv: 131, other_code: 17
- Bridge relations: spec_path_matches_code_path: 528, spec_component_matches_code: 40

## Spec Excerpts

### Programmer's Guide
_Source: `opentitan/hw/ip_templates/pwrmgr/doc/programmers_guide.md`_

```
# Programmer's Guide

The process in which the power manager is used is highly dependent on the system's topology.
The following proposes one method for how this can be done.

Assume first the system has the power states described [above](theory_of_operation.md#supported-low-power-modes).

## Programmer Sequence for Entering Low Power
```

### Programmer Sequence for Entering Low Power
_Source: `opentitan/hw/ip_templates/pwrmgr/doc/programmers_guide.md`_

```
# Programmer's Guide

The process in which the power manager is used is highly dependent on the system's topology.
The following proposes one method for how this can be done.

Assume first the system has the power states described [above](theory_of_operation.md#supported-low-power-modes).

## Programmer Sequence for Entering Low Power

1. Disable interrupt handling.
2. Mask all interrupt sources t
…
```

### Possible Exits
_Source: `opentitan/hw/ip_templates/pwrmgr/doc/programmers_guide.md`_

```
5. Configure low power mode configuration in [`CONTROL`](registers.md#control).
   - [`LOW_POWER_HINT`](registers.md#control--low_power_hint) must be set to trigger low power entry when the CPU sleeps.
7. Set and poll [`CFG_CDC_SYNC`](registers.md#cfg_cdc_sync) to ensure above settings propagate across clock domains.
8. Execute wait-for-interrupt instruction on the processing host.

Note that ente
…
```

### Theory of Operation
_Source: `opentitan/hw/ip_templates/pwrmgr/doc/theory_of_operation.md`_

```
# Theory of Operation

The power manager performs the following functions:
- Turn on/off power domain(s).
- Control root resets with the reset manager.
- Control root clock enables with AST and clock manager.
- Sequence various power up activities such as OTP sensing, life cycle initiation and releasing software to execute.
```

### Block Diagram
_Source: `opentitan/hw/ip_templates/pwrmgr/doc/theory_of_operation.md`_

```
The power manager performs the following functions:
- Turn on/off power domain(s).
- Control root resets with the reset manager.
- Control root clock enables with AST and clock manager.
- Sequence various power up activities such as OTP sensing, life cycle initiation and releasing software to execute.


## Block Diagram

See the below high level block diagram that illustrates the connections betwe
…
```

### Overall Sequencing
_Source: `opentitan/hw/ip_templates/pwrmgr/doc/theory_of_operation.md`_

```
## Block Diagram

See the below high level block diagram that illustrates the connections between the power manager and various system components.
Blocks outlined with a solid magenta line are always on; while blocks outlined with a dashed magenta line are a mix of components that are and those that are not.

![Power Manager Connectivity Diagram](../doc/pwrmgr_connectivity.svg)

## Overall Sequenc
…
```

### PWRMGR Checklist
_Source: `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`_

```
# PWRMGR Checklist

This checklist is for [Hardware Stage](../../../../../doc/project_governance/development_stages.md) transitions for the [PWRMGR peripheral.](../README.md)
All checklist items refer to the content in the [Checklist.](../../../../../doc/project_governance/checklist/README.md)

## Design Checklist

### D1
```

### D2S
_Source: `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`_

```
[CDC_SYNCMACRO]:         ../../../../../doc/project_governance/checklist/README.md#cdc_syncmacro
[LINT_PASS]:             ../../../../../doc/project_governance/checklist/README.md#lint_pass
[CDC_SETUP]:             ../../../../../doc/project_governance/checklist/README.md#cdc_setup
[RDC_SETUP]:             ../../../../../doc/project_governance/checklist/README.md#rdc_setup
[AREA_CHECK]:
…
```

## Spec Anchors

- `component:pwrmgr` (L1) — `__graphify_spec_only__/components.md`
- `pwrmgr.tpldesc.hjson` (L1) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson`
- `template param list` (L5) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson`
- `desc` (L8) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson`
- `width` (L31) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson`
- `peripheral` (L43) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson`
- `int` (L51) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson`
- `debug` (L52) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson`
- `pwrmgr_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_sec_cm_testplan.hjson`
- `stage` (L32) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_sec_cm_testplan.hjson`
- `tests` (L33) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_sec_cm_testplan.hjson`
- `pwrmgr_testplan.hjson` (L1) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_testplan.hjson`
- `testpoints` (L13) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_testplan.hjson`
- `desc` (L16) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_testplan.hjson`
- `stage` (L41) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_testplan.hjson`
- `tests` (L42) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_testplan.hjson`
- `covergroups` (L280) — `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `PWRMGR Checklist` (L1) — `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `D2` (L32) — `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `D2S` (L74) — `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `D3` (L94) — `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `Verification Checklist` (L120) — `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `V1` (L122) — `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `V2` (L172) — `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `V2S` (L218) — `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `programmers_guide.md` (L1) — `opentitan/hw/ip_templates/pwrmgr/doc/programmers_guide.md`
- `Programmer's Guide` (L1) — `opentitan/hw/ip_templates/pwrmgr/doc/programmers_guide.md`
- `Programmer Sequence for Entering Low Power` (L8) — `opentitan/hw/ip_templates/pwrmgr/doc/programmers_guide.md`
- `Possible Exits` (L25) — `opentitan/hw/ip_templates/pwrmgr/doc/programmers_guide.md`

## Code Evidence

**RTL** (22)
  - `prim_pulse_sync`:L108 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_cdc.sv`
  - `lc_ctrl_pkg`:L76 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_fsm.sv`
  - `prim_intr_hw`:L705 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
  - `pwrmgr_reg_pkg`:L10 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_wake_info.sv`
  - `pwrmgr_cdc_pulse.sv`:L1 — `opentitan\hw\ip_templates\pwrmgr\rtl\pwrmgr_cdc_pulse.sv`
  - `pwrmgr_cdc_pulse`:L11 — `opentitan\hw\ip_templates\pwrmgr\rtl\pwrmgr_cdc_pulse.sv`
  - `pwrmgr_wake_info.sv`:L1 — `opentitan\hw\ip_templates\pwrmgr\rtl\pwrmgr_wake_info.sv`
  - `pwrmgr_wake_info`:L10 — `opentitan\hw\ip_templates\pwrmgr\rtl\pwrmgr_wake_info.sv`
  - `pwrmgr_pkg`:L10 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_wake_info.sv`
  - `pwrmgr.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
  - `pwrmgr`:L10 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
  - `prim_clock_timeout`:L194 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
  - `pwrmgr_reg_top`:L328 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
  - `pwrmgr_cdc`:L415 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
  - `pwrmgr_slow_fsm`:L553 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
  - `pwrmgr_fsm`:L606 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
  - `pwrmgr_wake_info`:L686 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
  - `pwrmgr_cdc.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\rtl\pwrmgr_cdc.sv`
  - `pwrmgr_cdc`:L10 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\rtl\pwrmgr_cdc.sv`
  - `pwrmgr_cdc_pulse.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\rtl\pwrmgr_cdc_pulse.sv`
**DV** (13)
  - `pins_if`:L39 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tb.sv`
  - `tl_if`:L44 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tb.sv`
  - `alert_esc_if`:L40 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tb.sv`
  - `pwrmgr_base_test.sv`:L1 — `opentitan\hw\ip_templates\pwrmgr\dv\tests\pwrmgr_base_test.sv`
  - `pwrmgr_test_pkg.sv`:L1 — `opentitan\hw\ip_templates\pwrmgr\dv\tests\pwrmgr_test_pkg.sv`
  - `pwrmgr_env_pkg`:L9 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tests\pwrmgr_test_pkg.sv`
  - `tb.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\tb.sv`
  - `pwrmgr_test_pkg`:L10 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tb.sv`
  - `pwrmgr_cov_bind.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\cov\pwrmgr_cov_bind.sv`
  - `pwrmgr_cov_bind`:L7 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\cov\pwrmgr_cov_bind.sv`
  - `pwrmgr_base_test.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\tests\pwrmgr_base_test.sv`
  - `pwrmgr_test_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\tests\pwrmgr_test_pkg.sv`
**SVA** (13)
  - `pwrmgr_sec_cm_checker_assert.sv`:L1 — `opentitan\hw\ip_templates\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv`
  - `pwrmgr_sec_cm_checker_assert`:L7 — `opentitan\hw\ip_templates\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv`
  - `pwrmgr_unit_only_bind.sv`:L1 — `opentitan\hw\ip_templates\pwrmgr\dv\sva\pwrmgr_unit_only_bind.sv`
  - `pwrmgr_unit_only_bind`:L6 — `opentitan\hw\ip_templates\pwrmgr\dv\sva\pwrmgr_unit_only_bind.sv`
  - `pwrmgr_ast_sva_if.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_ast_sva_if.sv`
  - `pwrmgr_bind.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_bind.sv`
  - `pwrmgr_bind`:L5 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_bind.sv`
  - `pwrmgr_clock_enables_sva_if.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_clock_enables_sva_if.sv`
  - `pwrmgr_rstreqs_sva_if.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_rstreqs_sva_if.sv`
  - `pwrmgr_sec_cm_checker_assert.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv`
  - `pwrmgr_sec_cm_checker_assert`:L7 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv`
  - `pwrmgr_unit_only_bind.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_unit_only_bind.sv`
  - `pwrmgr_unit_only_bind`:L6 — `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_unit_only_bind.sv`
**OTHER_CODE** (2)
  - `reg_pwrmgr.py`:L1 — `opentitan\hw\ip_templates\pwrmgr\util\reg_pwrmgr.py`
  - `main()`:L14 — `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\util\reg_pwrmgr.py`

## Neighbor Components

- `flash_ctrl` (18 refs; imports_from×10, instantiates×8)
- `rv_plic` (18 refs; instantiates×18)
- `clkmgr` (17 refs; imports_from×11, instantiates×6)
- `pulp_riscv_dbg` (16 refs; instantiates×16)
- `lowrisc_ibex` (15 refs; instantiates×11, imports_from×3, calls×1)
- `prim` (14 refs; imports_from×8, instantiates×6)
- `rv_core_ibex` (12 refs; instantiates×9, imports_from×3)
- `lc_ctrl` (11 refs; imports_from×8, instantiates×3)
- `gpio` (9 refs; instantiates×9)
- `alert_handler` (8 refs; instantiates×8)
- `rstmgr` (7 refs; imports_from×4, instantiates×3)
- `otp_ctrl` (6 refs; instantiates×6)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_sec_cm_checker_assert.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_sec_cm_checker_assert` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_clock_enables_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_clock_enables_sva_if.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_sec_cm_checker_assert.sv` | `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_sec_cm_checker_assert` | `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_clock_enables_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_clock_enables_sva_if.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_rstreqs_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_rstreqs_sva_if.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_unit_only_bind.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_unit_only_bind.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_unit_only_bind` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_unit_only_bind.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_sec_cm_checker_assert.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_sec_cm_checker_assert` | `opentitan\hw\top_earlgrey\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_clock_enables_sva_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwrmgr\dv\sva\pwrmgr_clock_enables_sva_if.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_base_test.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tests\pwrmgr_base_test.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_env_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tests\pwrmgr_test_pkg.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_ast_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_ast_sva_if.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_test_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tests\pwrmgr_test_pkg.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_rstreqs_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_rstreqs_sva_if.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_unit_only_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_unit_only_bind.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_unit_only_bind` | `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_unit_only_bind.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_cov_bind.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\cov\pwrmgr_cov_bind.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_cov_bind` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\cov\pwrmgr_cov_bind.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_reg_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_wake_info.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_wake_info.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_rstreqs_sva_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwrmgr\dv\sva\pwrmgr_rstreqs_sva_if.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_unit_only_bind.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwrmgr\dv\sva\pwrmgr_unit_only_bind.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_unit_only_bind` | `opentitan\hw\top_earlgrey\ip_autogen\pwrmgr\dv\sva\pwrmgr_unit_only_bind.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_cdc_pulse.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_cdc_pulse.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_cdc_pulse` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_cdc_pulse.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_wake_info.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_wake_info.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_wake_info` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_wake_info.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_base_test.sv` | `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\tests\pwrmgr_base_test.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_slow_fsm.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_slow_fsm.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_slow_fsm` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_slow_fsm.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_ast_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_ast_sva_if.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_test_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\tests\pwrmgr_test_pkg.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_bind.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_bind.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_bind` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_bind.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_reg_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_reg_pkg.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_reg_top.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_reg_top.sv` |
| `spec_component_matches_code` | `component:pwrmgr` | `pwrmgr_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_reg_top.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `prim_pulse_sync` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_cdc.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `lc_ctrl_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_fsm.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `pins_if` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `tl_if` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `prim_intr_hw` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `alert_esc_if` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `pwrmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `pwrmgr.tpldesc.hjson` | `pwrmgr_sec_cm_checker_assert` | `opentitan\hw\ip_templates\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |

## Retrieval Guidance

- For code-only queries mentioning `pwrmgr`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `pwrmgr`.
