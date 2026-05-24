# Hardware Description: otp_ctrl

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Programmer's Guide**: During provisioning and manufacturing, SW interacts with the OTP controller mostly through the Direct Access Interface (DAI), which is described below.
- **General Guidance**: During provisioning and manufacturing, SW interacts with the OTP controller mostly through the Direct Access Interface (DAI), which is described below.
- **Initialization**: During provisioning and manufacturing, SW interacts with the OTP controller mostly through the Direct Access Interface (DAI), which is described below.

## Identity

- `ip_block`: `otp_ctrl`
- `bridge_edge_count`: 528
- Spec categories: document: 472, testplan: 113, theory: 79, interface: 55, component: 41
- Code categories: rtl: 558, sva: 49, dv: 31, other_code: 18
- Bridge relations: spec_path_matches_code_path: 488, spec_component_matches_code: 40

## Spec Excerpts

### Programmer's Guide
_Source: `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

During provisioning and manufacturing, SW interacts with the OTP controller mostly through the Direct Access Interface (DAI), which is described below.
Afterwards during production, SW is expected to perform only read accesses via the exposed CSRs and CSR windows, since all write access to the partitions has been locked down.

The following sections provide some general guida
…
```

### General Guidance
_Source: `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

During provisioning and manufacturing, SW interacts with the OTP controller mostly through the Direct Access Interface (DAI), which is described below.
Afterwards during production, SW is expected to perform only read accesses via the exposed CSRs and CSR windows, since all write access to the partitions has been locked down.

The following sections provide some general guida
…
```

### Initialization
_Source: `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`_

```
During provisioning and manufacturing, SW interacts with the OTP controller mostly through the Direct Access Interface (DAI), which is described below.
Afterwards during production, SW is expected to perform only read accesses via the exposed CSRs and CSR windows, since all write access to the partitions has been locked down.

The following sections provide some general guidance, followed by an ex
…
```

### Theory of Operation
_Source: `opentitan/hw/ip_templates/otp_ctrl/doc/theory_of_operation.md`_

```
# Theory of Operation

Conceptually speaking, the OTP functionality is at a high level split into "front-end" and "back-end".
The "front-end" contains the logical partitions that feed the hardware and software consumer interfaces of the system.
The "back-end" represents the programming interface used by hardware and software components to stage the upcoming values.
The diagram below illustrates th
…
```

### Logical Partitions
_Source: `opentitan/hw/ip_templates/otp_ctrl/doc/theory_of_operation.md`_

```
Note that the front-end contains both buffered and unbuffered partitions.
Buffered partitions are sensed once per power cycle and their contents are stored in registers, whereas unbuffered partitions are read on-demand.
The former are typically partitions that contain data like hardware configuration bits, key material and the life cycle state that need to be always available to the hardware, wher
…
```

### Partition Listing and Description
_Source: `opentitan/hw/ip_templates/otp_ctrl/doc/theory_of_operation.md`_

```
- This controls whether a particular partition can be subject to zeroization in line with FIPS and [OCP L.O.C.K.](https://www.opencompute.org/documents/ocp-l-o-c-k-0-8-1-pdf-1) requirements.
  - A zeroized partition has all its fuses (including the digest field) blown. Currently, the OTP macro is configured to also zeroize the redundant ECC bits of each partition word.

Since the OTP is memory-lik
…
```

### OTP CTRL Checklist
_Source: `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`_

```
# OTP_CTRL Checklist

<!--
NOTE: This is a template checklist document that is required to be copied over to the 'doc'
directory for a new design that transitions from L0 (Specification) to L1 (Development)
stage, and updated as needed. Once done, please remove this comment before checking it in.
-->
This checklist is for [Hardware Stage](../../../../../doc/project_governance/development_stages.md
…
```

### D2S
_Source: `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`_

```
[CDC_SYNCMACRO]:         ../../../../../doc/project_governance/checklist/README.md#cdc_syncmacro
[LINT_PASS]:             ../../../../../doc/project_governance/checklist/README.md#lint_pass
[CDC_SETUP]:             ../../../../../doc/project_governance/checklist/README.md#cdc_setup
[RDC_SETUP]:             ../../../../../doc/project_governance/checklist/README.md#rdc_setup
[AREA_CHECK]:
…
```

## Spec Anchors

- `component:otp_ctrl` (L1) — `__graphify_spec_only__/components.md`
- `otp_ctrl.tpldesc.hjson` (L1) — `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl.tpldesc.hjson`
- `template param list` (L5) — `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl.tpldesc.hjson`
- `desc` (L8) — `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl.tpldesc.hjson`
- `otp_ctrl_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `OTP CTRL Checklist` (L1) — `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `Design Checklist` (L11) — `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `D1` (L13) — `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `D2` (L37) — `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `D2S` (L79) — `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `D3` (L99) — `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `Verification Checklist` (L125) — `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `V1` (L127) — `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `V2` (L177) — `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `V2S` (L223) — `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `programmers_guide.md` (L1) — `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Programmer's Guide` (L1) — `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `General Guidance` (L9) — `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Initialization` (L11) — `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Reset Considerations` (L28) — `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Programming Already Programmed Regions` (L34) — `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Potential Side-Effects on Flash via Life Cycle` (L39) — `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Direct Access Interface` (L45) — `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Readout Sequence` (L61) — `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Programming Sequence` (L78) — `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Digest Calculation Sequence` (L98) — `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `theory_of_operation.md` (L1) — `opentitan/hw/ip_templates/otp_ctrl/doc/theory_of_operation.md`
- `Theory of Operation` (L1) — `opentitan/hw/ip_templates/otp_ctrl/doc/theory_of_operation.md`
- `Logical Partitions` (L17) — `opentitan/hw/ip_templates/otp_ctrl/doc/theory_of_operation.md`
- `Partition Listing and Description` (L45) — `opentitan/hw/ip_templates/otp_ctrl/doc/theory_of_operation.md`

## Code Evidence

**RTL** (29)
  - `prim_secded_inv_72_64_enc`:L39 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv`
  - `prim_sec_anchor_flop`:L275 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv`
  - `prim_sum_tree`:L944 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_dai.sv`
  - `otp_ctrl_pkg`:L13 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv`
  - `prim_util_pkg`:L12 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv`
  - `otp_ctrl_pkg.sv`:L1 — `opentitan\hw\ip\otp_ctrl\rtl\otp_ctrl_pkg.sv`
  - `otp_ctrl_macro_pkg`:L15 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv`
  - `otp_macro_pkg`:L21 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl.sv`
  - `otp_ctrl_dai.sv`:L1 — `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_dai.sv`
  - `otp_ctrl_dai`:L10 — `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_dai.sv`
  - `otp_ctrl_reg_pkg`:L14 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv`
  - `otp_ctrl_part_pkg`:L77 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_scrmbl.sv`
  - `otp_ctrl_top_specific_pkg`:L76 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_scrmbl.sv`
  - `otp_ctrl_ecc_reg.sv`:L1 — `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv`
  - `otp_ctrl_ecc_reg`:L10 — `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv`
  - `otp_ctrl_lci.sv`:L1 — `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_lci.sv`
  - `otp_ctrl_lci`:L10 — `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_lci.sv`
  - `otp_ctrl_lfsr_timer.sv`:L1 — `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_lfsr_timer.sv`
  - `otp_ctrl_lfsr_timer`:L31 — `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_lfsr_timer.sv`
  - `prim_double_lfsr`:L94 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_lfsr_timer.sv`
**DV** (8)
  - `otp_ctrl_base_test.sv`:L1 — `opentitan\hw\ip_templates\otp_ctrl\dv\tests\otp_ctrl_base_test.sv`
  - `otp_ctrl_test_pkg.sv`:L1 — `opentitan\hw\ip_templates\otp_ctrl\dv\tests\otp_ctrl_test_pkg.sv`
  - `otp_ctrl_env_pkg`:L9 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\dv\tests\otp_ctrl_test_pkg.sv`
  - `mem_bkdr_util_pkg`:L12 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\dv\tb.sv`
  - `tb.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\dv\tb.sv`
  - `otp_ctrl_test_pkg`:L10 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\dv\tb.sv`
  - `otp_ctrl_if`:L70 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\dv\tb.sv`
**SVA** (2)
  - `otp_ctrl_bind.sv`:L1 — `opentitan\hw\ip_templates\otp_ctrl\dv\sva\otp_ctrl_bind.sv`
  - `otp_ctrl_bind`:L5 — `opentitan\hw\ip_templates\otp_ctrl\dv\sva\otp_ctrl_bind.sv`
**OTHER_CODE** (11)
  - `dt.py`:L1 — `opentitan\hw\ip_templates\otp_ctrl\util\dt.py`
  - `OtpCtrlExt`:L50 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\dt.py`
  - `.__init__()`:L59 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\dt.py`
  - `create_ext()`:L102 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\dt.py`
  - `.extend_dt_ip()`:L106 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\dt.py`
  - `.fill_dt_ip()`:L121 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\dt.py`
  - `.render_dt_ip()`:L143 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\dt.py`
  - `ipconfig.py`:L1 — `opentitan\hw\ip_templates\otp_ctrl\util\ipconfig.py`
  - `OtpCtrlIpConfig`:L13 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`
  - `.__init__()`:L14 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`
  - `.sw_readable_partitions()`:L23 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`

## Neighbor Components

- `rv_core_ibex` (26 refs; instantiates×15, imports_from×11)
- `flash_ctrl` (23 refs; instantiates×23)
- `lowrisc_ibex` (20 refs; instantiates×15, imports_from×4, calls×1)
- `rv_plic` (12 refs; instantiates×12)
- `prim` (8 refs; instantiates×8)
- `pwrmgr` (6 refs; instantiates×6)
- `pulp_riscv_dbg` (4 refs; instantiates×4)
- `rom_ctrl` (4 refs; imports_from×4)
- `otp_ctrl.rs` (4 refs; calls×4)
- `rstmgr` (3 refs; imports_from×3)
- `lc_ctrl` (3 refs; imports_from×3)
- `otbn` (3 refs; imports_from×3)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_top_specific_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_macro_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_reg_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_base_test.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\dv\tests\otp_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_top_specific_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_test_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\dv\tests\otp_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_core_reg_top.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_core_reg_top.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_core_reg_top` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_core_reg_top.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_base_test.sv` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\dv\tests\otp_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_env_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\dv\tests\otp_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_cov_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\dv\cov\otp_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_cov_bind` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\dv\cov\otp_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_test_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\dv\tests\otp_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_lfsr_timer.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_lfsr_timer.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_lfsr_timer` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_lfsr_timer.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_part_unbuf.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_part_unbuf.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_part_unbuf` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_part_unbuf.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_core_reg_top.sv` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_core_reg_top.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_core_reg_top` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_core_reg_top.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_cov_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\dv\cov\otp_ctrl_cov_if.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_macro_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_macro_pkg.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_cov_bind.sv` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\dv\cov\otp_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_cov_bind` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\dv\cov\otp_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_part_buf.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_part_buf.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_part_buf` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_part_buf.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_part_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_part_pkg.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_lfsr_timer.sv` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_lfsr_timer.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_lfsr_timer` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_lfsr_timer.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_part_unbuf.sv` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_part_unbuf.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_part_unbuf` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_part_unbuf.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\dv\sva\otp_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_bind` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\dv\sva\otp_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_ecc_reg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_ecc_reg` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_reg_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_cov_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\dv\cov\otp_ctrl_cov_if.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_macro_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_macro_pkg.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_ecc_reg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_part_buf.sv` |
| `spec_component_matches_code` | `component:otp_ctrl` | `otp_ctrl_scrmbl.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_scrmbl.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `prim_sum_tree` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_dai.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `otp_ctrl_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `prim_util_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `otp_ctrl_pkg.sv` | `opentitan\hw\ip\otp_ctrl\rtl\otp_ctrl_pkg.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `otp_ctrl_macro_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `otp_macro_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `otp_ctrl.tpldesc.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `prim_sum_tree` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_dai.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `otp_ctrl_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |

## Retrieval Guidance

- For code-only queries mentioning `otp_ctrl`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `otp_ctrl`.
