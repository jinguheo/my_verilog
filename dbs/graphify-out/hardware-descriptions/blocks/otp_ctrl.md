# Hardware Description: otp_ctrl

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `otp_ctrl`
- `approved_label`: `pending:otp_ctrl`
- `doc_anchor`: `otp_ctrl`
- `module_name_prefix`: `otp_ctrl`
- `bridge_edge_count`: 528

## Inferred Hardware Role

`otp_ctrl` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 472, testplan: 113, theory: 79, interface: 55, component: 41
- Code categories: rtl: 558, sva: 49, dv: 31, other_code: 18
- Bridge relations: spec_path_matches_code_path: 488, spec_component_matches_code: 40

## Spec Anchors

- `component:otp_ctrl` (L1) - `__graphify_spec_only__/components.md`
- `otp_ctrl.tpldesc.hjson` (L1) - `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl.tpldesc.hjson`
- `template param list` (L5) - `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl.tpldesc.hjson`
- `desc` (L8) - `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl.tpldesc.hjson`
- `otp_ctrl_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `OTP CTRL Checklist` (L1) - `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `Design Checklist` (L11) - `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `D1` (L13) - `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `D2` (L37) - `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `D2S` (L79) - `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `D3` (L99) - `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `Verification Checklist` (L125) - `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `V1` (L127) - `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `V2` (L177) - `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `V2S` (L223) - `opentitan/hw/ip_templates/otp_ctrl/doc/checklist.md`
- `programmers_guide.md` (L1) - `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Programmer's Guide` (L1) - `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `General Guidance` (L9) - `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Initialization` (L11) - `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Reset Considerations` (L28) - `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Programming Already Programmed Regions` (L34) - `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Potential Side-Effects on Flash via Life Cycle` (L39) - `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Direct Access Interface` (L45) - `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Readout Sequence` (L61) - `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Programming Sequence` (L78) - `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `Digest Calculation Sequence` (L98) - `opentitan/hw/ip_templates/otp_ctrl/doc/programmers_guide.md`
- `theory_of_operation.md` (L1) - `opentitan/hw/ip_templates/otp_ctrl/doc/theory_of_operation.md`
- `Theory of Operation` (L1) - `opentitan/hw/ip_templates/otp_ctrl/doc/theory_of_operation.md`
- `Logical Partitions` (L17) - `opentitan/hw/ip_templates/otp_ctrl/doc/theory_of_operation.md`
- `Partition Listing and Description` (L45) - `opentitan/hw/ip_templates/otp_ctrl/doc/theory_of_operation.md`

## Code Evidence

- `prim_secded_inv_72_64_enc` (L39) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv`
- `prim_sec_anchor_flop` (L275) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv`
- `prim_sum_tree` (L944) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_dai.sv`
- `otp_ctrl_pkg` (L13) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv`
- `prim_util_pkg` (L12) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv`
- `otp_ctrl_pkg.sv` (L1) - `opentitan\hw\ip\otp_ctrl\rtl\otp_ctrl_pkg.sv`
- `otp_ctrl_macro_pkg` (L15) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv`
- `otp_macro_pkg` (L21) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl.sv`
- `otp_ctrl_bind.sv` (L1) - `opentitan\hw\ip_templates\otp_ctrl\dv\sva\otp_ctrl_bind.sv`
- `otp_ctrl_bind` (L5) - `opentitan\hw\ip_templates\otp_ctrl\dv\sva\otp_ctrl_bind.sv`
- `otp_ctrl_base_test.sv` (L1) - `opentitan\hw\ip_templates\otp_ctrl\dv\tests\otp_ctrl_base_test.sv`
- `otp_ctrl_test_pkg.sv` (L1) - `opentitan\hw\ip_templates\otp_ctrl\dv\tests\otp_ctrl_test_pkg.sv`
- `otp_ctrl_env_pkg` (L9) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\dv\tests\otp_ctrl_test_pkg.sv`
- `otp_ctrl_dai.sv` (L1) - `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_dai.sv`
- `otp_ctrl_dai` (L10) - `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_dai.sv`
- `otp_ctrl_reg_pkg` (L14) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv`
- `otp_ctrl_part_pkg` (L77) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_scrmbl.sv`
- `otp_ctrl_top_specific_pkg` (L76) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_scrmbl.sv`
- `otp_ctrl_ecc_reg.sv` (L1) - `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv`
- `otp_ctrl_ecc_reg` (L10) - `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv`
- `otp_ctrl_lci.sv` (L1) - `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_lci.sv`
- `otp_ctrl_lci` (L10) - `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_lci.sv`
- `otp_ctrl_lfsr_timer.sv` (L1) - `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_lfsr_timer.sv`
- `otp_ctrl_lfsr_timer` (L31) - `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_lfsr_timer.sv`
- `prim_double_lfsr` (L94) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_lfsr_timer.sv`
- `otp_ctrl_part_buf.sv` (L1) - `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_part_buf.sv`
- `otp_ctrl_part_buf` (L10) - `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_part_buf.sv`
- `prim_mubi8_sender` (L245) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_part_unbuf.sv`
- `otp_ctrl_ecc_reg` (L831) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_part_buf.sv`
- `otp_ctrl_part_unbuf.sv` (L1) - `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_part_unbuf.sv`
- `otp_ctrl_part_unbuf` (L10) - `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_part_unbuf.sv`
- `otp_ctrl_scrmbl.sv` (L1) - `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_scrmbl.sv`
- `otp_ctrl_scrmbl` (L74) - `opentitan\hw\ip_templates\otp_ctrl\rtl\otp_ctrl_scrmbl.sv`
- `prim_present` (L450) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_scrmbl.sv`
- `dt.py` (L1) - `opentitan\hw\ip_templates\otp_ctrl\util\dt.py`
- `OtpCtrlExt` (L50) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\dt.py`
- `.__init__()` (L59) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\dt.py`
- `create_ext()` (L102) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\dt.py`
- `.extend_dt_ip()` (L106) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\dt.py`
- `.fill_dt_ip()` (L121) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\dt.py`
- `.render_dt_ip()` (L143) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\dt.py`
- `ipconfig.py` (L1) - `opentitan\hw\ip_templates\otp_ctrl\util\ipconfig.py`
- `OtpCtrlIpConfig` (L13) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`
- `.__init__()` (L14) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`
- `.sw_readable_partitions()` (L23) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`

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
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `prim_util_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `otp_ctrl_pkg.sv` | `opentitan\hw\ip\otp_ctrl\rtl\otp_ctrl_pkg.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `otp_ctrl_macro_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `otp_macro_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_sec_cm_testplan.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_sum_tree` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_dai.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `otp_ctrl_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_util_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `otp_ctrl_pkg.sv` | `opentitan\hw\ip\otp_ctrl\rtl\otp_ctrl_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `otp_ctrl_macro_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `otp_macro_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl.sv` |

## Retrieval Guidance

- When a code-only query mentions `otp_ctrl`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
