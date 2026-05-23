# Hardware Description: clkmgr

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `clkmgr`
- `approved_label`: `pending:clkmgr`
- `doc_anchor`: `clkmgr`
- `module_name_prefix`: `clkmgr`
- `bridge_edge_count`: 563

## Inferred Hardware Role

`clkmgr` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 477, testplan: 148, theory: 89, interface: 67, component: 41
- Code categories: sva: 351, rtl: 321, dv: 29, other_code: 2
- Bridge relations: spec_path_matches_code_path: 523, spec_component_matches_code: 40

## Spec Anchors

- `component:clkmgr` (L1) - `__graphify_spec_only__/components.md`
- `clkmgr.tpldesc.hjson` (L1) - `opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson`
- `template param list` (L5) - `opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson`
- `desc` (L8) - `opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson`
- `aon` (L25) - `opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson`
- `freq` (L26) - `opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson`
- `ref` (L27) - `opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson`
- `main` (L36) - `opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson`
- `div` (L41) - `opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson`
- `src` (L42) - `opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson`
- `hint clks` (L51) - `opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson`
- `src name` (L54) - `opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip_templates/clkmgr/doc/checklist.md`
- `CLKMGR Checklist` (L1) - `opentitan/hw/ip_templates/clkmgr/doc/checklist.md`
- `Design Checklist` (L11) - `opentitan/hw/ip_templates/clkmgr/doc/checklist.md`
- `D1` (L13) - `opentitan/hw/ip_templates/clkmgr/doc/checklist.md`
- `D2` (L37) - `opentitan/hw/ip_templates/clkmgr/doc/checklist.md`
- `D2S` (L79) - `opentitan/hw/ip_templates/clkmgr/doc/checklist.md`
- `D3` (L99) - `opentitan/hw/ip_templates/clkmgr/doc/checklist.md`
- `Verification Checklist` (L125) - `opentitan/hw/ip_templates/clkmgr/doc/checklist.md`
- `V1` (L127) - `opentitan/hw/ip_templates/clkmgr/doc/checklist.md`
- `V2` (L177) - `opentitan/hw/ip_templates/clkmgr/doc/checklist.md`
- `V2S` (L223) - `opentitan/hw/ip_templates/clkmgr/doc/checklist.md`
- `programmers_guide.md` (L1) - `opentitan/hw/ip_templates/clkmgr/doc/programmers_guide.md`
- `Programmer's Guide` (L1) - `opentitan/hw/ip_templates/clkmgr/doc/programmers_guide.md`
- `Transactional Clock Hints` (L6) - `opentitan/hw/ip_templates/clkmgr/doc/programmers_guide.md`
- `Peripheral Clock Controls` (L12) - `opentitan/hw/ip_templates/clkmgr/doc/programmers_guide.md`
- `Device Interface Functions DIFs` (L15) - `opentitan/hw/ip_templates/clkmgr/doc/programmers_guide.md`
- `clkmgr.hjson` (L1) - `opentitan/hw/top_darjeeling/ip_autogen/clkmgr/data/clkmgr.hjson`
- `human name` (L9) - `opentitan/hw/top_darjeeling/ip_autogen/clkmgr/data/clkmgr.hjson`
- `one line desc` (L10) - `opentitan/hw/top_darjeeling/ip_autogen/clkmgr/data/clkmgr.hjson`
- `one paragraph desc` (L11) - `opentitan/hw/top_darjeeling/ip_autogen/clkmgr/data/clkmgr.hjson`
- `cip id` (L19) - `opentitan/hw/top_darjeeling/ip_autogen/clkmgr/data/clkmgr.hjson`
- `design spec` (L20) - `opentitan/hw/top_darjeeling/ip_autogen/clkmgr/data/clkmgr.hjson`
- `dv doc` (L21) - `opentitan/hw/top_darjeeling/ip_autogen/clkmgr/data/clkmgr.hjson`

## Code Evidence

- `prim_edge_detector` (L114) - `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\rtl\clkmgr_meas_chk.sv`
- `clkmgr_aon_cg_en_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv`
- `clkmgr_cg_en_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv`
- `clkmgr_div_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv`
- `clkmgr_extclk_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv`
- `clkmgr_gated_clock_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv`
- `clkmgr_lost_calib_ctrl_en_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv`
- `clkmgr_lost_calib_regwen_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv`
- `clkmgr_sec_cm_checker_assert.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv`
- `clkmgr_sec_cm_checker_assert` (L7) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv`
- `clkmgr_trans_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_trans_sva_if.sv`
- `clkmgr_base_test.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\tests\clkmgr_base_test.sv`
- `clkmgr_test_pkg.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\tests\clkmgr_test_pkg.sv`
- `clkmgr_env_pkg` (L9) - `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\tests\clkmgr_test_pkg.sv`
- `clkmgr_byp.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\rtl\clkmgr_byp.sv`
- `clkmgr_byp` (L7) - `opentitan\hw\ip_templates\clkmgr\rtl\clkmgr_byp.sv`
- `clkmgr_pkg` (L8) - `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\rtl\clkmgr_trans.sv`
- `clkmgr_clk_status.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\rtl\clkmgr_clk_status.sv`
- `clkmgr_clk_status` (L7) - `opentitan\hw\ip_templates\clkmgr\rtl\clkmgr_clk_status.sv`
- `clkmgr_meas_chk.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\rtl\clkmgr_meas_chk.sv`
- `clkmgr_meas_chk` (L7) - `opentitan\hw\ip_templates\clkmgr\rtl\clkmgr_meas_chk.sv`
- `prim_clock_meas` (L43) - `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\rtl\clkmgr_meas_chk.sv`
- `clkmgr_root_ctrl.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\rtl\clkmgr_root_ctrl.sv`
- `clkmgr_root_ctrl` (L7) - `opentitan\hw\ip_templates\clkmgr\rtl\clkmgr_root_ctrl.sv`
- `clkmgr_trans.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\rtl\clkmgr_trans.sv`
- `clkmgr_trans` (L7) - `opentitan\hw\ip_templates\clkmgr\rtl\clkmgr_trans.sv`
- `tb.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\tb.sv`
- `tb` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\tb.sv`
- `clkmgr_test_pkg` (L10) - `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\tb.sv`
- `clkmgr_if` (L83) - `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\tb.sv`
- `clkmgr_cov_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\cov\clkmgr_cov_bind.sv`
- `clkmgr_cov_bind` (L7) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\cov\clkmgr_cov_bind.sv`
- `clkmgr_aon_cg_en_sva_if.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv`
- `clkmgr_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_bind.sv`
- `clkmgr_bind` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_bind.sv`
- `clkmgr_cg_en_sva_if.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv`
- `clkmgr_div_sva_if.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_div_sva_if.sv`
- `clkmgr_extclk_sva_if.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv`
- `clkmgr_gated_clock_sva_if.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv`
- `clkmgr_lost_calib_ctrl_en_sva_if.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv`
- `clkmgr_lost_calib_regwen_sva_if.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv`
- `clkmgr_sec_cm_checker_assert.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv`
- `clkmgr_sec_cm_checker_assert` (L7) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv`
- `clkmgr_trans_sva_if.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_trans_sva_if.sv`
- `clkmgr_base_test.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\tests\clkmgr_base_test.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_sec_cm_checker_assert` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_sec_cm_checker_assert` | `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_sec_cm_checker_assert` | `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_trans_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_trans_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_base_test.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\tests\clkmgr_base_test.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_env_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\tests\clkmgr_test_pkg.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_div_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_test_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\tests\clkmgr_test_pkg.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_cov_bind.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\cov\clkmgr_cov_bind.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_cov_bind` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\cov\clkmgr_cov_bind.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_clk_status.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\rtl\clkmgr_clk_status.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_clk_status` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\rtl\clkmgr_clk_status.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_trans_sva_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\sva\clkmgr_trans_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_root_ctrl.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\rtl\clkmgr_root_ctrl.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_root_ctrl` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\rtl\clkmgr_root_ctrl.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_base_test.sv` | `opentitan\hw\top_darjeeling\ip_autogen\clkmgr\dv\tests\clkmgr_base_test.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_meas_chk.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\rtl\clkmgr_meas_chk.sv` |
| `spec_component_matches_code` | `component:clkmgr` | `clkmgr_meas_chk` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\rtl\clkmgr_meas_chk.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `clkmgr.tpldesc.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `clkmgr.tpldesc.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `clkmgr.tpldesc.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `clkmgr.tpldesc.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `clkmgr.tpldesc.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `clkmgr.tpldesc.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `clkmgr.tpldesc.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `clkmgr.tpldesc.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |

## Retrieval Guidance

- When a code-only query mentions `clkmgr`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
