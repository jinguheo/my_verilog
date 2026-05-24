# Hardware Description: alert_handler

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Programmer's Guide**: False alerts during power-up and reset are not possible since the alerts are disabled by default, and need to be configured and locked in by the firmware.
- **Power-up and Reset Considerations**: False alerts during power-up and reset are not possible since the alerts are disabled by default, and need to be configured and locked in by the firmware.
- **Initialization**: The low-power state management of alert channels is handled entirely by hardware and hence this is transparent to software.

## Identity

- `ip_block`: `alert_handler`
- `bridge_edge_count`: 332
- Spec categories: document: 289, testplan: 113, theory: 52, component: 41, interface: 3
- Code categories: rtl: 224, dv: 111, sva: 88
- Bridge relations: spec_path_matches_code_path: 292, spec_component_matches_code: 40

## Spec Excerpts

### Programmer's Guide
_Source: `opentitan/hw/ip_templates/alert_handler/doc/programmers_guide.md`_

```
# Programmer's Guide


## Power-up and Reset Considerations

False alerts during power-up and reset are not possible since the alerts are disabled by default, and need to be configured and locked in by the firmware.
The ping timer won't start until initial configuration is over and the registers are locked in.
```

### Power-up and Reset Considerations
_Source: `opentitan/hw/ip_templates/alert_handler/doc/programmers_guide.md`_

```
# Programmer's Guide


## Power-up and Reset Considerations

False alerts during power-up and reset are not possible since the alerts are disabled by default, and need to be configured and locked in by the firmware.
The ping timer won't start until initial configuration is over and the registers are locked in.

The low-power state management of alert channels is handled entirely by hardware and he
…
```

### Initialization
_Source: `opentitan/hw/ip_templates/alert_handler/doc/programmers_guide.md`_

```
The low-power state management of alert channels is handled entirely by hardware and hence this is transparent to software.
Note however that the LPGs inherit the security properties of the associated clock groups and resets.
This means that the low-power state of certain alerts can be controlled by SW by means of clock gating or block reset.
For example, certain crypto blocks are located in a tra
…
```

### Programmer's Guide
_Source: `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/programmers_guide.md`_

```
# Programmer's Guide


## Power-up and Reset Considerations

False alerts during power-up and reset are not possible since the alerts are disabled by default, and need to be configured and locked in by the firmware.
The ping timer won't start until initial configuration is over and the registers are locked in.
```

### Power-up and Reset Considerations
_Source: `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/programmers_guide.md`_

```
# Programmer's Guide


## Power-up and Reset Considerations

False alerts during power-up and reset are not possible since the alerts are disabled by default, and need to be configured and locked in by the firmware.
The ping timer won't start until initial configuration is over and the registers are locked in.

The low-power state management of alert channels is handled entirely by hardware and he
…
```

### Initialization
_Source: `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/programmers_guide.md`_

```
The low-power state management of alert channels is handled entirely by hardware and hence this is transparent to software.
Note however that the LPGs inherit the security properties of the associated clock groups and resets.
This means that the low-power state of certain alerts can be controlled by SW by means of clock gating or block reset.
For example, certain crypto blocks are located in a tra
…
```

### Alert Handler Checklist
_Source: `opentitan/hw/ip_templates/alert_handler/doc/checklist.md`_

```
# Alert Handler Checklist

This checklist is for [Hardware Stage](../../../../../doc/project_governance/development_stages.md) transitions for the [Alert Handler peripheral.](../README.md)
All checklist items refer to the content in the [Checklist.](../../../../../doc/project_governance/checklist/README.md)

## Design Checklist

### D1
```

### D2S
_Source: `opentitan/hw/ip_templates/alert_handler/doc/checklist.md`_

```
[CDC_SYNCMACRO]:         ../../../../../doc/project_governance/checklist/README.md#cdc_syncmacro
[LINT_PASS]:             ../../../../../doc/project_governance/checklist/README.md#lint_pass
[CDC_SETUP]:             ../../../../../doc/project_governance/checklist/README.md#cdc_setup
[RDC_SETUP]:             ../../../../../doc/project_governance/checklist/README.md#rdc_setup
[AREA_CHECK]:
…
```

## Spec Anchors

- `component:alert_handler` (L1) — `__graphify_spec_only__/components.md`
- `alert_handler.tpldesc.hjson` (L1) — `opentitan/hw/ip_templates/alert_handler/data/alert_handler.tpldesc.hjson`
- `template param list` (L5) — `opentitan/hw/ip_templates/alert_handler/data/alert_handler.tpldesc.hjson`
- `desc` (L8) — `opentitan/hw/ip_templates/alert_handler/data/alert_handler.tpldesc.hjson`
- `alert_handler_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip_templates/alert_handler/data/alert_handler_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip_templates/alert_handler/data/alert_handler_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip_templates/alert_handler/data/alert_handler_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip_templates/alert_handler/data/alert_handler_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip_templates/alert_handler/data/alert_handler_sec_cm_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip_templates/alert_handler/doc/checklist.md`
- `Alert Handler Checklist` (L1) — `opentitan/hw/ip_templates/alert_handler/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip_templates/alert_handler/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip_templates/alert_handler/doc/checklist.md`
- `D2` (L32) — `opentitan/hw/ip_templates/alert_handler/doc/checklist.md`
- `D2S` (L74) — `opentitan/hw/ip_templates/alert_handler/doc/checklist.md`
- `D3` (L94) — `opentitan/hw/ip_templates/alert_handler/doc/checklist.md`
- `Verification Checklist` (L120) — `opentitan/hw/ip_templates/alert_handler/doc/checklist.md`
- `V1` (L122) — `opentitan/hw/ip_templates/alert_handler/doc/checklist.md`
- `V2` (L172) — `opentitan/hw/ip_templates/alert_handler/doc/checklist.md`
- `V2S` (L218) — `opentitan/hw/ip_templates/alert_handler/doc/checklist.md`
- `programmers_guide.md` (L1) — `opentitan/hw/ip_templates/alert_handler/doc/programmers_guide.md`
- `Programmer's Guide` (L1) — `opentitan/hw/ip_templates/alert_handler/doc/programmers_guide.md`
- `Power-up and Reset Considerations` (L4) — `opentitan/hw/ip_templates/alert_handler/doc/programmers_guide.md`
- `Initialization` (L16) — `opentitan/hw/ip_templates/alert_handler/doc/programmers_guide.md`
- `Interrupt Handling` (L64) — `opentitan/hw/ip_templates/alert_handler/doc/programmers_guide.md`
- `Device Interface Functions DIFs` (L96) — `opentitan/hw/ip_templates/alert_handler/doc/programmers_guide.md`
- `Register Table` (L100) — `opentitan/hw/ip_templates/alert_handler/doc/programmers_guide.md`
- `Additional Notes` (L105) — `opentitan/hw/ip_templates/alert_handler/doc/programmers_guide.md`
- `Timing Constraints` (L107) — `opentitan/hw/ip_templates/alert_handler/doc/programmers_guide.md`
- `Fast-track Alerts` (L113) — `opentitan/hw/ip_templates/alert_handler/doc/programmers_guide.md`
- `alert_handler.hjson` (L1) — `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler.hjson`
- `cip id` (L10) — `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler.hjson`
- `design spec` (L11) — `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler.hjson`
- `dv doc` (L12) — `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler.hjson`
- `hw checklist` (L13) — `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler.hjson`

## Code Evidence

**RTL** (26)
  - `prim_alert_pkg`:L11 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `prim_esc_pkg`:L12 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `alert_handler_pkg`:L7 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv`
  - `alert_handler_ping_timer`:L124 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `alert_handler.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `alert_handler`:L9 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `alert_handler_reg_wrap`:L74 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `alert_handler_lpg_ctrl`:L173 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `alert_handler_class`:L214 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `alert_handler_accu`:L234 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `alert_handler_esc_timer`:L249 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `alert_handler_accu.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_accu.sv`
  - `alert_handler_accu`:L15 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_accu.sv`
  - `alert_handler_class.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_class.sv`
  - `alert_handler_class`:L10 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_class.sv`
  - `alert_handler_esc_timer.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_esc_timer.sv`
  - `alert_handler_esc_timer`:L21 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_esc_timer.sv`
  - `alert_handler_lpg_ctrl.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_lpg_ctrl.sv`
  - `alert_handler_lpg_ctrl`:L14 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_lpg_ctrl.sv`
  - `alert_handler_ping_timer.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_ping_timer.sv`
**DV** (18)
  - `alert_handler_cov_bind.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv`
  - `alert_handler_cov_bind`:L7 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv`
  - `tb.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tb\tb.sv`
  - `tb`:L5 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tb\tb.sv`
  - `alert_handler_env_pkg`:L9 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\tests\alert_handler_test_pkg.sv`
  - `alert_handler_test_pkg`:L10 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\tb\tb.sv`
  - `alert_handler_if`:L28 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\tb\tb.sv`
  - `alert_esc_probe_if`:L31 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\tb\tb.sv`
  - `alert_handler_base_test.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tests\alert_handler_base_test.sv`
  - `alert_handler_test_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tests\alert_handler_test_pkg.sv`
  - `alert_handler_esc_timer_bind_fpv.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_bind_fpv.sv`
  - `alert_handler_esc_timer_bind_fpv`:L6 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_bind_fpv.sv`
  - `alert_handler_esc_timer_tb.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_tb.sv`
  - `alert_handler_esc_timer_tb`:L8 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_tb.sv`
  - `alert_handler_ping_timer_bind_fpv.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_bind_fpv.sv`
  - `alert_handler_ping_timer_bind_fpv`:L6 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_bind_fpv.sv`
  - `alert_handler_ping_timer_tb.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_tb.sv`
  - `alert_handler_ping_timer_tb`:L8 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_tb.sv`
**SVA** (6)
  - `alert_handler_bind.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv`
  - `alert_handler_bind`:L5 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv`
  - `alert_handler_esc_timer_assert_fpv.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_esc_timer_assert_fpv.sv`
  - `alert_handler_esc_timer_assert_fpv`:L10 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_esc_timer_assert_fpv.sv`
  - `alert_handler_ping_timer_assert_fpv.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv`
  - `alert_handler_ping_timer_assert_fpv`:L10 — `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv`

## Neighbor Components

- `prim` (20 refs; imports_from×20)
- `rv_plic` (12 refs; instantiates×12)
- `flash_ctrl` (10 refs; instantiates×10)
- `lowrisc_ibex` (8 refs; instantiates×6, imports_from×2)
- `pwrmgr` (8 refs; instantiates×8)
- `rv_core_ibex` (4 refs; imports_from×2, instantiates×2)
- `alert_esc_agent` (2 refs; imports_from×2)
- `rstmgr` (2 refs; imports_from×2)
- `otp_ctrl` (2 refs; instantiates×2)
- `otbn` (1 refs; imports_from×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_ping_timer_assert_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_ping_timer_assert_fpv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_esc_timer_assert_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_esc_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_esc_timer_assert_fpv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_esc_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_ping_timer_assert_fpv.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_ping_timer_assert_fpv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_ping_timer_bind_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_ping_timer_bind_fpv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_esc_timer_assert_fpv.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\vip\alert_handler_esc_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_esc_timer_assert_fpv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\vip\alert_handler_esc_timer_assert_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_esc_timer_bind_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_esc_timer_bind_fpv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_ping_timer_bind_fpv.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_ping_timer_bind_fpv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_esc_timer_bind_fpv.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_esc_timer_bind_fpv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_ping_timer_tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_tb.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_ping_timer_tb` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_tb.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_esc_timer_tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_tb.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_esc_timer_tb` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_tb.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_base_test.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tests\alert_handler_base_test.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_ping_timer_tb.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_tb.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_ping_timer_tb` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_ping_timer_tb.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_test_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tests\alert_handler_test_pkg.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_esc_timer_tb.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_tb.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_esc_timer_tb` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\fpv\tb\alert_handler_esc_timer_tb.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_base_test.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\tests\alert_handler_base_test.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_cov_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_cov_bind` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_env_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\tests\alert_handler_test_pkg.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_test_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\tests\alert_handler_test_pkg.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_ping_timer.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_ping_timer.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_ping_timer` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_ping_timer.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_esc_timer.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_esc_timer.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_esc_timer` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_esc_timer.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_cov_bind.sv` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_cov_bind` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_lpg_ctrl.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_lpg_ctrl.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_lpg_ctrl` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_lpg_ctrl.sv` |
| `spec_component_matches_code` | `component:alert_handler` | `alert_handler_reg_wrap.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `alert_handler_cov_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `alert_handler_cov_bind` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `alert_handler_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `alert_handler_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `alert_handler_bind` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv` |
| `spec_path_matches_code_path` | `alert_handler.tpldesc.hjson` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `alert_handler_sec_cm_testplan.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `alert_handler_sec_cm_testplan.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `alert_handler_sec_cm_testplan.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `alert_handler_sec_cm_testplan.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |

## Retrieval Guidance

- For code-only queries mentioning `alert_handler`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `alert_handler`.
