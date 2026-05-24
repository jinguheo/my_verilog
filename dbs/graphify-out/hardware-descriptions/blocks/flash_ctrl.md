# Hardware Description: flash_ctrl

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Programmer's Guide**: To issue a flash read, the programmer must
- **Issuing a Controller Read**: To issue a flash read, the programmer must
- **Issuing a Controller Program**: The above fields can be set in the [`CONTROL`](registers.md#control) and [`ADDR`](registers.md#addr) registers.

## Identity

- `ip_block`: `flash_ctrl`
- `bridge_edge_count`: 408
- Spec categories: document: 341, testplan: 124, theory: 77, interface: 46, component: 41
- Code categories: rtl: 472, dv: 62, sva: 56, other_code: 2
- Bridge relations: spec_path_matches_code_path: 368, spec_component_matches_code: 40

## Spec Excerpts

### Programmer's Guide
_Source: `opentitan/hw/ip_templates/flash_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

## Issuing a Controller Read

To issue a flash read, the programmer must
*  Specify the address of the first flash word to read
*  Specify the number of total flash words to read, beginning at the supplied address
*  Specify the operation to be 'READ' type
```

### Issuing a Controller Read
_Source: `opentitan/hw/ip_templates/flash_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

## Issuing a Controller Read

To issue a flash read, the programmer must
*  Specify the address of the first flash word to read
*  Specify the number of total flash words to read, beginning at the supplied address
*  Specify the operation to be 'READ' type
*  Set the 'START' bit for the operation to begin
```

### Issuing a Controller Program
_Source: `opentitan/hw/ip_templates/flash_ctrl/doc/programmers_guide.md`_

```
The above fields can be set in the [`CONTROL`](registers.md#control) and [`ADDR`](registers.md#addr) registers.
See [library code](https://github.com/lowRISC/opentitan/blob/master/sw/device/lib/dif/dif_flash_ctrl.c) for implementation.

It is acceptable for total number of flash words to be significantly greater than the depth of the read FIFO.
In this situation, the read FIFO will fill up (or hit
…
```

### Theory of Operation
_Source: `opentitan/hw/ip_templates/flash_ctrl/doc/theory_of_operation.md`_

```
# Theory of Operation

## Block Diagram

![Flash Block Diagram](../doc/flash_block_diagram.svg)

### Flash Protocol Controller
```

### Block Diagram
_Source: `opentitan/hw/ip_templates/flash_ctrl/doc/theory_of_operation.md`_

```
# Theory of Operation

## Block Diagram

![Flash Block Diagram](../doc/flash_block_diagram.svg)

### Flash Protocol Controller

The Flash Protocol Controller sits between the host software interface, other hardware components and the flash physical controller.
Its primary functions are two fold
```

### Flash Protocol Controller
_Source: `opentitan/hw/ip_templates/flash_ctrl/doc/theory_of_operation.md`_

```
# Theory of Operation

## Block Diagram

![Flash Block Diagram](../doc/flash_block_diagram.svg)

### Flash Protocol Controller

The Flash Protocol Controller sits between the host software interface, other hardware components and the flash physical controller.
Its primary functions are two fold
*  Translate software program, erase and read requests into a high level protocol for the actual flash p
…
```

### FLASH CTRL Checklist
_Source: `opentitan/hw/ip_templates/flash_ctrl/doc/checklist.md`_

```
# FLASH_CTRL Checklist

This checklist is for [Hardware Stage](../../../../../doc/project_governance/development_stages.md) transitions for the [FLASH_CTRL peripheral.](../README.md)
All checklist items refer to the content in the [Checklist.](../../../../../doc/project_governance/checklist/README.md)

## Design Checklist

### D1
```

### D2S
_Source: `opentitan/hw/ip_templates/flash_ctrl/doc/checklist.md`_

```
[CDC_SYNCMACRO]:         ../../../../../doc/project_governance/checklist/README.md#cdc_syncmacro
[LINT_PASS]:             ../../../../../doc/project_governance/checklist/README.md#lint_pass
[CDC_SETUP]:             ../../../../../doc/project_governance/checklist/README.md#cdc_setup
[RDC_SETUP]:             ../../../../../doc/project_governance/checklist/README.md#rdc_setup
[AREA_CHECK]:
…
```

## Spec Anchors

- `component:flash_ctrl` (L1) — `__graphify_spec_only__/components.md`
- `flash_ctrl.tpldesc.hjson` (L1) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl.tpldesc.hjson`
- `template param list` (L5) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl.tpldesc.hjson`
- `desc` (L8) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl.tpldesc.hjson`
- `flash_ctrl_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`
- `stage` (L32) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`
- `tests` (L33) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`
- `flash_ctrl_testplan.hjson` (L1) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl_testplan.hjson`
- `testpoints` (L14) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl_testplan.hjson`
- `desc` (L17) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl_testplan.hjson`
- `stage` (L24) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl_testplan.hjson`
- `tests` (L25) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl_testplan.hjson`
- `covergroups` (L415) — `opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip_templates/flash_ctrl/doc/checklist.md`
- `FLASH CTRL Checklist` (L1) — `opentitan/hw/ip_templates/flash_ctrl/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip_templates/flash_ctrl/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip_templates/flash_ctrl/doc/checklist.md`
- `D2` (L33) — `opentitan/hw/ip_templates/flash_ctrl/doc/checklist.md`
- `D2S` (L75) — `opentitan/hw/ip_templates/flash_ctrl/doc/checklist.md`
- `D3` (L95) — `opentitan/hw/ip_templates/flash_ctrl/doc/checklist.md`
- `Verification Checklist` (L121) — `opentitan/hw/ip_templates/flash_ctrl/doc/checklist.md`
- `V1` (L123) — `opentitan/hw/ip_templates/flash_ctrl/doc/checklist.md`
- `V2` (L173) — `opentitan/hw/ip_templates/flash_ctrl/doc/checklist.md`
- `V2S` (L219) — `opentitan/hw/ip_templates/flash_ctrl/doc/checklist.md`
- `programmers_guide.md` (L1) — `opentitan/hw/ip_templates/flash_ctrl/doc/programmers_guide.md`
- `Programmer's Guide` (L1) — `opentitan/hw/ip_templates/flash_ctrl/doc/programmers_guide.md`
- `Issuing a Controller Read` (L3) — `opentitan/hw/ip_templates/flash_ctrl/doc/programmers_guide.md`
- `Issuing a Controller Program` (L19) — `opentitan/hw/ip_templates/flash_ctrl/doc/programmers_guide.md`
- `Debugging a Read Error` (L27) — `opentitan/hw/ip_templates/flash_ctrl/doc/programmers_guide.md`
- `Error Encountered by Software Direct Read` (L31) — `opentitan/hw/ip_templates/flash_ctrl/doc/programmers_guide.md`
- `Error Encountered by Software Initiated Controller Operations` (L39) — `opentitan/hw/ip_templates/flash_ctrl/doc/programmers_guide.md`
- `Hardware Initiated Reads` (L44) — `opentitan/hw/ip_templates/flash_ctrl/doc/programmers_guide.md`

## Code Evidence

**RTL** (35)
  - `prim_arbiter_tree`:L163 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv`
  - `prim_count`:L240 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv`
  - `prim_secded_hamming_72_64_enc`:L775 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv`
  - `prim_secded_hamming_76_68_enc`:L334 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv`
  - `prim_secded_hamming_76_68_dec`:L435 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv`
  - `flash_ctrl_top_specific_pkg`:L14 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv`
  - `flash_phy_pkg`:L12 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_scramble.sv`
  - `tlul_rsp_intg_chk`:L1500 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl.sv`
  - `prim_subreg_shadow`:L10297 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_core_reg_top.sv`
  - `tlul_data_integ_enc`:L734 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv`
  - `flash_ctrl_pkg.sv`:L1 — `opentitan\hw\ip\flash_ctrl\rtl\flash_ctrl_pkg.sv`
  - `tlul_adapter_sram`:L527 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl.sv`
  - `tlul_data_integ_dec`:L118 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv`
  - `flash_ctrl_arb.sv`:L1 — `opentitan\hw\ip_templates\flash_ctrl\rtl\flash_ctrl_arb.sv`
  - `flash_ctrl_arb`:L15 — `opentitan\hw\ip_templates\flash_ctrl\rtl\flash_ctrl_arb.sv`
  - `flash_ctrl_erase.sv`:L1 — `opentitan\hw\ip_templates\flash_ctrl\rtl\flash_ctrl_erase.sv`
  - `flash_ctrl_erase`:L8 — `opentitan\hw\ip_templates\flash_ctrl\rtl\flash_ctrl_erase.sv`
  - `flash_ctrl_info_cfg.sv`:L1 — `opentitan\hw\ip_templates\flash_ctrl\rtl\flash_ctrl_info_cfg.sv`
  - `flash_ctrl_info_cfg`:L10 — `opentitan\hw\ip_templates\flash_ctrl\rtl\flash_ctrl_info_cfg.sv`
  - `flash_ctrl_lcmgr.sv`:L1 — `opentitan\hw\ip_templates\flash_ctrl\rtl\flash_ctrl_lcmgr.sv`
**DV** (13)
  - `rst_shadowed_if`:L50 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv`
  - `flash_ctrl_cov_bind.sv`:L1 — `opentitan\hw\ip_templates\flash_ctrl\dv\cov\flash_ctrl_cov_bind.sv`
  - `flash_ctrl_cov_bind`:L12 — `opentitan\hw\ip_templates\flash_ctrl\dv\cov\flash_ctrl_cov_bind.sv`
  - `flash_ctrl_phy_cov_if.sv`:L1 — `opentitan\hw\ip_templates\flash_ctrl\dv\cov\flash_ctrl_phy_cov_if.sv`
  - `tb.sv`:L1 — `opentitan\hw\ip_templates\flash_ctrl\dv\tb\tb.sv`
  - `flash_ctrl_env_pkg`:L9 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tests\flash_ctrl_test_pkg.sv`
  - `flash_ctrl_test_pkg`:L12 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv`
  - `flash_ctrl_bkdr_util_pkg`:L13 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip_templates\flash_ctrl\dv\tb\tb.sv`
  - `flash_ctrl_if`:L67 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv`
  - `flash_phy_prim_if`:L71 — `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv`
  - `flash_ctrl_base_test.sv`:L1 — `opentitan\hw\ip_templates\flash_ctrl\dv\tests\flash_ctrl_base_test.sv`
  - `flash_ctrl_test_pkg.sv`:L1 — `opentitan\hw\ip_templates\flash_ctrl\dv\tests\flash_ctrl_test_pkg.sv`
**SVA** (2)
  - `flash_ctrl_bind.sv`:L1 — `opentitan\hw\ip_templates\flash_ctrl\dv\sva\flash_ctrl_bind.sv`
  - `flash_ctrl_bind`:L5 — `opentitan\hw\ip_templates\flash_ctrl\dv\sva\flash_ctrl_bind.sv`

## Neighbor Components

- `rv_core_ibex` (38 refs; imports_from×24, instantiates×14)
- `otp_ctrl` (23 refs; instantiates×23)
- `rv_plic` (22 refs; instantiates×22)
- `pwrmgr` (18 refs; imports_from×10, instantiates×8)
- `prim` (14 refs; instantiates×14)
- `rstmgr` (14 refs; instantiates×11, imports_from×3)
- `lowrisc_ibex` (13 refs; instantiates×10, imports_from×3)
- `clkmgr` (10 refs; instantiates×10)
- `alert_handler` (10 refs; instantiates×10)
- `kmac` (8 refs; instantiates×8)
- `pulp_riscv_dbg` (8 refs; instantiates×8)
- `tlul` (5 refs; instantiates×5)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_top_specific_pkg.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_top_specific_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_top_specific_pkg.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_base_test.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tests\flash_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_env_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tests\flash_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_phy_cov_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\cov\flash_ctrl_phy_cov_if.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_test_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tests\flash_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_core_reg_top.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_core_reg_top.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_core_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_core_reg_top.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_prim_reg_top.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_prim_reg_top.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_prim_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_prim_reg_top.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_cov_bind.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\cov\flash_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_cov_bind` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\cov\flash_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_region_cfg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_region_cfg.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_region_cfg` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_region_cfg.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_top_specific_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\flash_ctrl\rtl\flash_ctrl_top_specific_pkg.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_info_cfg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_info_cfg.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_info_cfg` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_info_cfg.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_bind.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\sva\flash_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_bind` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\sva\flash_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_reg_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_base_test.sv` | `opentitan\hw\top_earlgrey\ip_autogen\flash_ctrl\dv\tests\flash_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_phy_cov_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\flash_ctrl\dv\cov\flash_ctrl_phy_cov_if.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_test_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\flash_ctrl\dv\tests\flash_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_erase.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_erase.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_erase` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_erase.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_lcmgr.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_lcmgr.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_lcmgr` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_lcmgr.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_core_reg_top.sv` | `opentitan\hw\top_earlgrey\ip_autogen\flash_ctrl\rtl\flash_ctrl_core_reg_top.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_core_reg_top` | `opentitan\hw\top_earlgrey\ip_autogen\flash_ctrl\rtl\flash_ctrl_core_reg_top.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_prim_reg_top.sv` | `opentitan\hw\top_earlgrey\ip_autogen\flash_ctrl\rtl\flash_ctrl_prim_reg_top.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_prim_reg_top` | `opentitan\hw\top_earlgrey\ip_autogen\flash_ctrl\rtl\flash_ctrl_prim_reg_top.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_prog.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_prog.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_prog` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_prog.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_cov_bind.sv` | `opentitan\hw\top_earlgrey\ip_autogen\flash_ctrl\dv\cov\flash_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_cov_bind` | `opentitan\hw\top_earlgrey\ip_autogen\flash_ctrl\dv\cov\flash_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_arb.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_arb.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_arb` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_arb.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_region_cfg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\flash_ctrl\rtl\flash_ctrl_region_cfg.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_region_cfg` | `opentitan\hw\top_earlgrey\ip_autogen\flash_ctrl\rtl\flash_ctrl_region_cfg.sv` |
| `spec_component_matches_code` | `component:flash_ctrl` | `flash_ctrl_rd.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_rd.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `prim_arbiter_tree` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `prim_count` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `prim_secded_hamming_72_64_enc` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `prim_secded_hamming_76_68_enc` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `prim_secded_hamming_76_68_dec` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `flash_ctrl_top_specific_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `flash_phy_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_scramble.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `rst_shadowed_if` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `flash_ctrl.tpldesc.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `flash_ctrl_sec_cm_testplan.hjson` | `prim_arbiter_tree` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv` |
| `spec_path_matches_code_path` | `flash_ctrl_sec_cm_testplan.hjson` | `prim_count` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv` |
| `spec_path_matches_code_path` | `flash_ctrl_sec_cm_testplan.hjson` | `prim_secded_hamming_72_64_enc` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv` |
| `spec_path_matches_code_path` | `flash_ctrl_sec_cm_testplan.hjson` | `prim_secded_hamming_76_68_enc` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv` |

## Retrieval Guidance

- For code-only queries mentioning `flash_ctrl`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `flash_ctrl`.
