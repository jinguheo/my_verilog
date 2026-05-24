# Hardware Description: rv_plic

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **RV PLIC DV document**: * DV:
- **Goals**: * DV:
- **Current status**: * DV:

## Identity

- `ip_block`: `rv_plic`
- `bridge_edge_count`: 456
- Spec categories: document: 438, testplan: 141, theory: 100, component: 41, interface: 4
- Code categories: rtl: 422, sva: 60, dv: 28
- Bridge relations: spec_path_matches_code_path: 416, spec_component_matches_code: 40

## Spec Excerpts

### RV PLIC DV document
_Source: `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`_

```
# RV_PLIC DV document

## Goals
* DV:
  * RV_PLIC is decided to verify in FPV only

* FPV:
  * Verify all the RV_PLIC outputs by writing assumptions and assertions with a
```

### Goals
_Source: `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`_

```
# RV_PLIC DV document

## Goals
* DV:
  * RV_PLIC is decided to verify in FPV only

* FPV:
  * Verify all the RV_PLIC outputs by writing assumptions and assertions with a
    FPV based testbench
  * Verify TileLink device protocol compliance with a FPV based testbench
```

### Current status
_Source: `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`_

```
* DV:
  * RV_PLIC is decided to verify in FPV only

* FPV:
  * Verify all the RV_PLIC outputs by writing assumptions and assertions with a
    FPV based testbench
  * Verify TileLink device protocol compliance with a FPV based testbench

## Current status
* [Design & verification stage](../../../../README.md)
  * [HW development stages](../../../../../../doc/project_governance/development_stages.m
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip_templates/rv_plic/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

After reset, RV_PLIC doesn't generate any interrupts to any targets even if
interrupt sources are set, as all priorities and thresholds are 0 by default and
all ``IE`` values are 0. Software should configure the above three registers.
```

### Initialization
_Source: `opentitan/hw/ip_templates/rv_plic/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

After reset, RV_PLIC doesn't generate any interrupts to any targets even if
interrupt sources are set, as all priorities and thresholds are 0 by default and
all ``IE`` values are 0. Software should configure the above three registers.

[`PRIO0`](../data/rv_plic.hjson#prio_0) .. [`PRIO31`](../data/rv_plic.hjson#prio_1) registers are unique. So, only one of t
…
```

### Handling Interrupt Request Events
_Source: `opentitan/hw/ip_templates/rv_plic/doc/programmers_guide.md`_

```
void plic_enable(tid, iid) {
  // iid: 0-based ID
  int offset = ceil(N_SOURCE / 32) * tid + (iid >> 5);

  *(IE + offset) = *(IE + offset) | (1 << (iid % 32));
}
```

## Handling Interrupt Request Events

If software receives an interrupt request, it is recommended to follow the steps
shown below (assuming target 0 which uses [`CC0`](../data/rv_plic.hjson#cc0) for claim/complete).

1. Claim the i
…
```

### Theory of Operation
_Source: `opentitan/hw/ip_templates/rv_plic/doc/theory_of_operation.md`_

```
# Theory of Operation

## Block Diagram

![RV_PLIC Block Diagram](block_diagram.svg)

## Hardware Interfaces
```

### Block Diagram
_Source: `opentitan/hw/ip_templates/rv_plic/doc/theory_of_operation.md`_

```
# Theory of Operation

## Block Diagram

![RV_PLIC Block Diagram](block_diagram.svg)

## Hardware Interfaces

* [Interface Tables](../data/rv_plic.hjson#interfaces)
```

## Spec Anchors

- `component:rv_plic` (L1) — `__graphify_spec_only__/components.md`
- `rv_plic.tpldesc.hjson` (L1) — `opentitan/hw/ip_templates/rv_plic/data/rv_plic.tpldesc.hjson`
- `template param list` (L5) — `opentitan/hw/ip_templates/rv_plic/data/rv_plic.tpldesc.hjson`
- `desc` (L8) — `opentitan/hw/ip_templates/rv_plic/data/rv_plic.tpldesc.hjson`
- `dtgen` (L23) — `opentitan/hw/ip_templates/rv_plic/data/rv_plic.tpldesc.hjson`
- `rv_plic_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip_templates/rv_plic/data/rv_plic_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip_templates/rv_plic/data/rv_plic_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip_templates/rv_plic/data/rv_plic_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip_templates/rv_plic/data/rv_plic_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip_templates/rv_plic/data/rv_plic_sec_cm_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `RV PLIC Checklist` (L1) — `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `D2` (L34) — `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `D2S` (L72) — `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `D3` (L92) — `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `Verification Checklist` (L118) — `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `V1` (L120) — `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `V2` (L170) — `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `V2S` (L216) — `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `README.md` (L1) — `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `RV PLIC DV document` (L1) — `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `Goals` (L3) — `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `Current status` (L12) — `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `Design features` (L17) — `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `Testbench architecture` (L21) — `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `Block diagram` (L25) — `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `TLUL assertions` (L28) — `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `RV PLIC assertions` (L35) — `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `Symbolic variables` (L39) — `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `Testplan` (L47) — `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `programmers_guide.md` (L1) — `opentitan/hw/ip_templates/rv_plic/doc/programmers_guide.md`
- `Programmer's Guide` (L1) — `opentitan/hw/ip_templates/rv_plic/doc/programmers_guide.md`
- `Initialization` (L3) — `opentitan/hw/ip_templates/rv_plic/doc/programmers_guide.md`

## Code Evidence

**RTL** (32)
  - `prim_subreg`:L671 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
  - `tlul_cmd_intg_chk`:L48 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
  - `prim_reg_we_check`:L56 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
  - `tlul_rsp_intg_gen`:L81 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
  - `tlul_adapter_reg`:L92 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
  - `prim_subreg_ext`:L8023 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
  - `prim_max_tree`:L42 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_target.sv`
  - `rv_plic_reg_pkg`:L22 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
  - `rv_plic.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic.sv`
  - `rv_plic`:L19 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic.sv`
  - `rv_plic_gateway`:L241 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic.sv`
  - `rv_plic_gateway.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_gateway.sv`
  - `rv_plic_gateway`:L7 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_gateway.sv`
  - `rv_plic_reg_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_reg_pkg.sv`
  - `rv_plic_reg_top.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
  - `rv_plic_reg_top`:L9 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
  - `rv_plic_target.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_target.sv`
  - `rv_plic_target`:L17 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_target.sv`
  - `rv_plic.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic.sv`
  - `rv_plic`:L19 — `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic.sv`
**DV** (12)
  - `rv_plic_bind_fpv.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv`
  - `rv_plic_bind_fpv`:L5 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv`
  - `rv_plic_tb.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv`
  - `rv_plic_tb`:L7 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv`
  - `rv_plic_bind_fpv.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv`
  - `rv_plic_bind_fpv`:L5 — `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv`
  - `rv_plic_tb.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv`
  - `rv_plic_tb`:L7 — `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv`
  - `rv_plic_bind_fpv.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv`
  - `rv_plic_bind_fpv`:L5 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv`
  - `rv_plic_tb.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv`
  - `rv_plic_tb`:L7 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv`
**SVA** (6)
  - `rv_plic_assert_fpv.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv`
  - `rv_plic_assert_fpv`:L8 — `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv`
  - `rv_plic_assert_fpv.sv`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv`
  - `rv_plic_assert_fpv`:L8 — `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv`
  - `rv_plic_assert_fpv.sv`:L1 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv`
  - `rv_plic_assert_fpv`:L8 — `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv`

## Neighbor Components

- `flash_ctrl` (22 refs; instantiates×22)
- `ast` (18 refs; instantiates×18)
- `clkmgr` (18 refs; instantiates×18)
- `gpio` (18 refs; instantiates×18)
- `pinmux` (18 refs; instantiates×18)
- `pwrmgr` (18 refs; instantiates×18)
- `rstmgr` (18 refs; instantiates×18)
- `rv_core_ibex` (18 refs; instantiates×18)
- `mbx` (13 refs; instantiates×13)
- `rv_dm` (13 refs; instantiates×13)
- `soc_dbg_ctrl` (12 refs; instantiates×12)
- `alert_handler` (12 refs; instantiates×12)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_assert_fpv.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_assert_fpv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_bind_fpv.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_bind_fpv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_assert_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_assert_fpv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_reg_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_gateway.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_gateway.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_gateway` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_gateway.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_reg_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_pkg.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_reg_top.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_assert_fpv.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_assert_fpv` | `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_target.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_target.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_target` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_target.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_bind_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_bind_fpv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_tb.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_tb` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_bind_fpv.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_bind_fpv` | `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_gateway.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_gateway.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_gateway` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_gateway.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_reg_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_reg_pkg.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_reg_top.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_reg_top` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_target.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_target.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_target` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_target.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_tb` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_gateway` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_gateway.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic_gateway.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_gateway` | `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic_gateway.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic_reg_pkg.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_reg_top.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic_reg_top` | `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic.sv` |
| `spec_component_matches_code` | `component:rv_plic` | `rv_plic` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `prim_subreg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `tlul_cmd_intg_chk` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `prim_reg_we_check` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `tlul_rsp_intg_gen` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `tlul_adapter_reg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `prim_subreg_ext` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `prim_max_tree` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_target.sv` |
| `spec_path_matches_code_path` | `rv_plic.tpldesc.hjson` | `rv_plic_bind_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |

## Retrieval Guidance

- For code-only queries mentioning `rv_plic`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `rv_plic`.
