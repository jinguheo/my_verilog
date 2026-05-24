# Hardware Description: rstmgr

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Programmer's Guide**: - [Device Interface Functions](../../../../../sw/device/lib/dif/dif_rstmgr.h)
- **Device Interface Functions DIFs**: - [Device Interface Functions](../../../../../sw/device/lib/dif/dif_rstmgr.h)
- **RSTMGR Checklist**: This checklist is for [Hardware Stage](../../../../../doc/project_governance/development_stages.md) transitions for the [RSTMGR peripheral.](../README.md)

## Identity

- `ip_block`: `rstmgr`
- `bridge_edge_count`: 680
- Spec categories: document: 522, testplan: 260, theory: 81, interface: 67, component: 41
- Code categories: rtl: 497, dv: 213, sva: 90, other_code: 9
- Bridge relations: spec_path_matches_code_path: 640, spec_component_matches_code: 40

## Spec Excerpts

### Programmer's Guide
_Source: `opentitan/hw/ip_templates/rstmgr/doc/programmers_guide.md`_

```
# Programmer's Guide

## Device Interface Functions (DIFs)

- [Device Interface Functions](../../../../../sw/device/lib/dif/dif_rstmgr.h)
```

### Device Interface Functions DIFs
_Source: `opentitan/hw/ip_templates/rstmgr/doc/programmers_guide.md`_

```
# Programmer's Guide

## Device Interface Functions (DIFs)

- [Device Interface Functions](../../../../../sw/device/lib/dif/dif_rstmgr.h)
```

### RSTMGR Checklist
_Source: `opentitan/hw/ip_templates/rstmgr/doc/checklist.md`_

```
# RSTMGR Checklist

This checklist is for [Hardware Stage](../../../../../doc/project_governance/development_stages.md) transitions for the [RSTMGR peripheral.](../README.md)
All checklist items refer to the content in the [Checklist.](../../../../../doc/project_governance/checklist/README.md)

## Design Checklist

### D1
```

### D2S
_Source: `opentitan/hw/ip_templates/rstmgr/doc/checklist.md`_

```
[CDC_SYNCMACRO]:         ../../../../../doc/project_governance/checklist/README.md#cdc_syncmacro
[LINT_PASS]:             ../../../../../doc/project_governance/checklist/README.md#lint_pass
[CDC_SETUP]:             ../../../../../doc/project_governance/checklist/README.md#cdc_setup
[RDC_SETUP]:             ../../../../../doc/project_governance/checklist/README.md#rdc_setup
[AREA_CHECK]:
…
```

### Verification Checklist
_Source: `opentitan/hw/ip_templates/rstmgr/doc/checklist.md`_

```
[LINT_COMPLETE]:        ../../../../../doc/project_governance/checklist/README.md#lint_complete
[CDC_COMPLETE]:         ../../../../../doc/project_governance/checklist/README.md#cdc_complete
[RDC_COMPLETE]:         ../../../../../doc/project_governance/checklist/README.md#rdc_complete
[REVIEW_RTL]:           ../../../../../doc/project_governance/checklist/README.md#review_rtl
[REVIEW_DELETED_FF]:
…
```

### resets
_Source: `opentitan/hw/ip_templates/rstmgr/data/rstmgr.cfg.example.hjson`_

```
// Otherwise, selects the domain to which it is related
  // 0 is defaulted for always on.
  // TBD: This should eventually be changed to a name->index project wide lookup
  //
  // clk:  related clock domain for synchronous release
  // If type is "por", there is not related clock, since it is
  // likely external or generated from a voltage comparator
  //
  resets: [
    { name: "rst_ni",
…
```

### template param list
_Source: `opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  template_param_list: [
    {
      name: "topname"
      desc: "Name of top-level design, e.g., 'darjeeling' or 'earlgrey'"
      type: "string"
      default: ""
    }
    {
```

### desc
_Source: `opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  template_param_list: [
    {
      name: "topname"
      desc: "Name of top-level design, e.g., 'darjeeling' or 'earlgrey'"
      type: "string"
      default: ""
    }
    {
      name: "uniquified_modules"
      desc: "A dic
…
```

## Spec Anchors

- `component:rstmgr` (L1) — `__graphify_spec_only__/components.md`
- `rstmgr.cfg.example.hjson` (L1) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr.cfg.example.hjson`
- `resets` (L32) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr.cfg.example.hjson`
- `rstmgr.tpldesc.hjson` (L1) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson`
- `template param list` (L5) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson`
- `desc` (L8) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson`
- `peripheral` (L33) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson`
- `width` (L36) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson`
- `int` (L41) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson`
- `debug` (L42) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson`
- `gen` (L74) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson`
- `rst type` (L75) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson`
- `path` (L76) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson`
- `lpg path` (L77) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson`
- `rstmgr_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr_sec_cm_testplan.hjson`
- `stage` (L31) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr_sec_cm_testplan.hjson`
- `tests` (L32) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr_sec_cm_testplan.hjson`
- `rstmgr_testplan.hjson` (L1) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr_testplan.hjson`
- `testpoints` (L14) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr_testplan.hjson`
- `desc` (L17) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr_testplan.hjson`
- `stage` (L37) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr_testplan.hjson`
- `tests` (L38) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr_testplan.hjson`
- `covergroups` (L192) — `opentitan/hw/ip_templates/rstmgr/data/rstmgr_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip_templates/rstmgr/doc/checklist.md`
- `RSTMGR Checklist` (L1) — `opentitan/hw/ip_templates/rstmgr/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip_templates/rstmgr/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip_templates/rstmgr/doc/checklist.md`
- `D2` (L32) — `opentitan/hw/ip_templates/rstmgr/doc/checklist.md`
- `D2S` (L74) — `opentitan/hw/ip_templates/rstmgr/doc/checklist.md`
- `D3` (L94) — `opentitan/hw/ip_templates/rstmgr/doc/checklist.md`
- `Verification Checklist` (L120) — `opentitan/hw/ip_templates/rstmgr/doc/checklist.md`
- `V1` (L122) — `opentitan/hw/ip_templates/rstmgr/doc/checklist.md`

## Code Evidence

**RTL** (22)
  - `prim_sync_reqack`:L274 — `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_cnsty_chk.sv`
  - `prim_mubi4_sender`:L125 — `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_leaf_rst.sv`
  - `prim_mubi4_sync`:L32 — `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_leaf_rst.sv`
  - `prim_clock_buf`:L148 — `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr.sv`
  - `rstmgr_cnsty_chk.sv`:L1 — `opentitan\hw\ip_templates\rstmgr\rtl\rstmgr_cnsty_chk.sv`
  - `rstmgr_cnsty_chk`:L14 — `opentitan\hw\ip_templates\rstmgr\rtl\rstmgr_cnsty_chk.sv`
  - `rstmgr_reg_pkg`:L24 — `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_reg_top.sv`
  - `rstmgr_crash_info.sv`:L1 — `opentitan\hw\ip_templates\rstmgr\rtl\rstmgr_crash_info.sv`
  - `rstmgr_crash_info`:L8 — `opentitan\hw\ip_templates\rstmgr\rtl\rstmgr_crash_info.sv`
  - `rstmgr_ctrl.sv`:L1 — `opentitan\hw\ip_templates\rstmgr\rtl\rstmgr_ctrl.sv`
  - `rstmgr_ctrl`:L10 — `opentitan\hw\ip_templates\rstmgr\rtl\rstmgr_ctrl.sv`
  - `rstmgr_leaf_rst.sv`:L1 — `opentitan\hw\ip_templates\rstmgr\rtl\rstmgr_leaf_rst.sv`
  - `rstmgr_leaf_rst`:L10 — `opentitan\hw\ip_templates\rstmgr\rtl\rstmgr_leaf_rst.sv`
  - `rstmgr_por.sv`:L1 — `opentitan\hw\ip_templates\rstmgr\rtl\rstmgr_por.sv`
  - `rstmgr_por`:L8 — `opentitan\hw\ip_templates\rstmgr\rtl\rstmgr_por.sv`
  - `rstmgr.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\rtl\rstmgr.sv`
  - `rstmgr`:L11 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\rtl\rstmgr.sv`
  - `rstmgr_reg_top`:L172 — `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr.sv`
  - `rstmgr_cnsty_chk.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\rtl\rstmgr_cnsty_chk.sv`
  - `rstmgr_cnsty_chk`:L14 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\rtl\rstmgr_cnsty_chk.sv`
**DV** (20)
  - `cip_base_pkg`:L8 — `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\tests\rstmgr_test_pkg.sv`
  - `prim_rst_sync`:L451 — `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv`
  - `rstmgr_cov_bind.sv`:L1 — `opentitan\hw\ip_templates\rstmgr\dv\cov\rstmgr_cov_bind.sv`
  - `rstmgr_cov_bind`:L7 — `opentitan\hw\ip_templates\rstmgr\dv\cov\rstmgr_cov_bind.sv`
  - `tb.sv`:L1 — `opentitan\hw\ip_templates\rstmgr\dv\rstmgr_cnsty_chk\tb.sv`
  - `tb`:L413 — `opentitan\hw\ip_templates\rstmgr\dv\rstmgr_cnsty_chk\tb.sv`
  - `rstmgr_cnsty_chk_if`:L436 — `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv`
  - `rstmgr_cnsty_chk`:L458 — `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv`
  - `rstmgr_base_test.sv`:L1 — `opentitan\hw\ip_templates\rstmgr\dv\tests\rstmgr_base_test.sv`
  - `rstmgr_test_pkg.sv`:L1 — `opentitan\hw\ip_templates\rstmgr\dv\tests\rstmgr_test_pkg.sv`
  - `rstmgr_env_pkg`:L9 — `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\tests\rstmgr_test_pkg.sv`
  - `tb.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\tb.sv`
  - `rstmgr_test_pkg`:L10 — `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\tb.sv`
  - `rstmgr_cov_bind.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\cov\rstmgr_cov_bind.sv`
  - `rstmgr_cov_bind`:L7 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\cov\rstmgr_cov_bind.sv`
  - `tb.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv`
  - `tb`:L413 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv`
  - `rstmgr_base_test.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\tests\rstmgr_base_test.sv`
  - `rstmgr_test_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\tests\rstmgr_test_pkg.sv`
**SVA** (8)
  - `rstmgr_attrs_sva_if.sv`:L1 — `opentitan\hw\ip_templates\rstmgr\dv\sva\rstmgr_attrs_sva_if.sv`
  - `rstmgr_sw_rst_sva_if.sv`:L1 — `opentitan\hw\ip_templates\rstmgr\dv\sva\rstmgr_sw_rst_sva_if.sv`
  - `rstmgr_attrs_sva_if.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\sva\rstmgr_attrs_sva_if.sv`
  - `rstmgr_bind.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\sva\rstmgr_bind.sv`
  - `rstmgr_bind`:L5 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\sva\rstmgr_bind.sv`
  - `rstmgr_cascading_sva_if.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\sva\rstmgr_cascading_sva_if.sv`
  - `rstmgr_rst_en_track_sva_if.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\sva\rstmgr_rst_en_track_sva_if.sv`
  - `rstmgr_sw_rst_sva_if.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\sva\rstmgr_sw_rst_sva_if.sv`

## Neighbor Components

- `clkmgr` (41 refs; instantiates×37, imports_from×4)
- `pulp_riscv_dbg` (24 refs; instantiates×24)
- `ast` (20 refs; instantiates×20)
- `rv_plic` (18 refs; instantiates×18)
- `flash_ctrl` (14 refs; instantiates×11, imports_from×3)
- `lowrisc_ibex` (11 refs; instantiates×8, imports_from×3)
- `prim` (10 refs; instantiates×10)
- `rv_core_ibex` (7 refs; imports_from×7)
- `pwrmgr` (7 refs; imports_from×4, instantiates×3)
- `spi_device` (6 refs; instantiates×5, imports_from×1)
- `pinmux` (6 refs; instantiates×6)
- `rstmgr.c` (4 refs; calls×4)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_rst_en_track_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\sva\rstmgr_rst_en_track_sva_if.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_cascading_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\sva\rstmgr_cascading_sva_if.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_rst_en_track_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\sva\rstmgr_rst_en_track_sva_if.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_sw_rst_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\sva\rstmgr_sw_rst_sva_if.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_attrs_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\sva\rstmgr_attrs_sva_if.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_rst_en_track_sva_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rstmgr\dv\sva\rstmgr_rst_en_track_sva_if.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_base_test.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\tests\rstmgr_base_test.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_env_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\tests\rstmgr_test_pkg.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_cascading_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\sva\rstmgr_cascading_sva_if.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_test_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\tests\rstmgr_test_pkg.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_cnsty_chk_if` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_cnsty_chk` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_cascading_sva_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rstmgr\dv\sva\rstmgr_cascading_sva_if.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_cov_bind.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\cov\rstmgr_cov_bind.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_cov_bind` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\cov\rstmgr_cov_bind.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_sw_rst_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\sva\rstmgr_sw_rst_sva_if.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_crash_info.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_crash_info.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_crash_info` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_crash_info.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_attrs_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\sva\rstmgr_attrs_sva_if.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_cnsty_chk.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_cnsty_chk.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_cnsty_chk` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_cnsty_chk.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_base_test.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\tests\rstmgr_base_test.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_sw_rst_sva_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rstmgr\dv\sva\rstmgr_sw_rst_sva_if.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_leaf_rst.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_leaf_rst.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_leaf_rst` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_leaf_rst.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_reg_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_reg_top.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_test_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\tests\rstmgr_test_pkg.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_attrs_sva_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rstmgr\dv\sva\rstmgr_attrs_sva_if.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_bind.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\sva\rstmgr_bind.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_bind` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\sva\rstmgr_bind.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_reg_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_reg_pkg.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_reg_top.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_reg_top.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_reg_top.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_base_test.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rstmgr\dv\tests\rstmgr_base_test.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_cov_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\cov\rstmgr_cov_bind.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_cov_bind` | `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\dv\cov\rstmgr_cov_bind.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_test_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rstmgr\dv\tests\rstmgr_test_pkg.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_crash_info.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\rtl\rstmgr_crash_info.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_crash_info` | `opentitan\hw\top_darjeeling\ip_autogen\rstmgr\rtl\rstmgr_crash_info.sv` |
| `spec_component_matches_code` | `component:rstmgr` | `rstmgr_ctrl.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_ctrl.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `prim_sync_reqack` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_cnsty_chk.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `prim_mubi4_sender` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_leaf_rst.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `prim_mubi4_sync` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_leaf_rst.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `cip_base_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\tests\rstmgr_test_pkg.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `prim_clock_buf` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `prim_rst_sync` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `rstmgr_cov_bind.sv` | `opentitan\hw\ip_templates\rstmgr\dv\cov\rstmgr_cov_bind.sv` |
| `spec_path_matches_code_path` | `rstmgr.cfg.example.hjson` | `rstmgr_cov_bind` | `opentitan\hw\ip_templates\rstmgr\dv\cov\rstmgr_cov_bind.sv` |
| `spec_path_matches_code_path` | `rstmgr.tpldesc.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `rstmgr.tpldesc.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `rstmgr.tpldesc.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `rstmgr.tpldesc.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |

## Retrieval Guidance

- For code-only queries mentioning `rstmgr`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `rstmgr`.
