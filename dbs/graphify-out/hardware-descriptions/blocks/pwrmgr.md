# Hardware Description: pwrmgr

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `pwrmgr`
- `approved_label`: `pending:pwrmgr`
- `doc_anchor`: `pwrmgr`
- `module_name_prefix`: `pwrmgr`
- `bridge_edge_count`: 568

## Inferred Hardware Role

`pwrmgr` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 466, testplan: 176, theory: 108, interface: 70, component: 41
- Code categories: rtl: 389, sva: 167, dv: 131, other_code: 17
- Bridge relations: spec_path_matches_code_path: 528, spec_component_matches_code: 40

## Spec Anchors

- `component:pwrmgr` (L1) - `__graphify_spec_only__/components.md`
- `pwrmgr.tpldesc.hjson` (L1) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson`
- `template param list` (L5) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson`
- `desc` (L8) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson`
- `width` (L31) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson`
- `peripheral` (L43) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson`
- `int` (L51) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson`
- `debug` (L52) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson`
- `pwrmgr_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_sec_cm_testplan.hjson`
- `stage` (L32) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_sec_cm_testplan.hjson`
- `tests` (L33) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_sec_cm_testplan.hjson`
- `pwrmgr_testplan.hjson` (L1) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_testplan.hjson`
- `testpoints` (L13) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_testplan.hjson`
- `desc` (L16) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_testplan.hjson`
- `stage` (L41) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_testplan.hjson`
- `tests` (L42) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_testplan.hjson`
- `covergroups` (L280) - `opentitan/hw/ip_templates/pwrmgr/data/pwrmgr_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `PWRMGR Checklist` (L1) - `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `D2` (L32) - `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `D2S` (L74) - `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `D3` (L94) - `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `Verification Checklist` (L120) - `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `V1` (L122) - `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `V2` (L172) - `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `V2S` (L218) - `opentitan/hw/ip_templates/pwrmgr/doc/checklist.md`
- `programmers_guide.md` (L1) - `opentitan/hw/ip_templates/pwrmgr/doc/programmers_guide.md`
- `Programmer's Guide` (L1) - `opentitan/hw/ip_templates/pwrmgr/doc/programmers_guide.md`
- `Programmer Sequence for Entering Low Power` (L8) - `opentitan/hw/ip_templates/pwrmgr/doc/programmers_guide.md`
- `Possible Exits` (L25) - `opentitan/hw/ip_templates/pwrmgr/doc/programmers_guide.md`

## Code Evidence

- `prim_pulse_sync` (L108) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_cdc.sv`
- `lc_ctrl_pkg` (L76) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_fsm.sv`
- `pins_if` (L39) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tb.sv`
- `tl_if` (L44) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tb.sv`
- `prim_intr_hw` (L705) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
- `alert_esc_if` (L40) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tb.sv`
- `pwrmgr_sec_cm_checker_assert.sv` (L1) - `opentitan\hw\ip_templates\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv`
- `pwrmgr_sec_cm_checker_assert` (L7) - `opentitan\hw\ip_templates\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv`
- `pwrmgr_reg_pkg` (L10) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_wake_info.sv`
- `pwrmgr_unit_only_bind.sv` (L1) - `opentitan\hw\ip_templates\pwrmgr\dv\sva\pwrmgr_unit_only_bind.sv`
- `pwrmgr_unit_only_bind` (L6) - `opentitan\hw\ip_templates\pwrmgr\dv\sva\pwrmgr_unit_only_bind.sv`
- `pwrmgr_base_test.sv` (L1) - `opentitan\hw\ip_templates\pwrmgr\dv\tests\pwrmgr_base_test.sv`
- `pwrmgr_test_pkg.sv` (L1) - `opentitan\hw\ip_templates\pwrmgr\dv\tests\pwrmgr_test_pkg.sv`
- `pwrmgr_env_pkg` (L9) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tests\pwrmgr_test_pkg.sv`
- `pwrmgr_cdc_pulse.sv` (L1) - `opentitan\hw\ip_templates\pwrmgr\rtl\pwrmgr_cdc_pulse.sv`
- `pwrmgr_cdc_pulse` (L11) - `opentitan\hw\ip_templates\pwrmgr\rtl\pwrmgr_cdc_pulse.sv`
- `pwrmgr_wake_info.sv` (L1) - `opentitan\hw\ip_templates\pwrmgr\rtl\pwrmgr_wake_info.sv`
- `pwrmgr_wake_info` (L10) - `opentitan\hw\ip_templates\pwrmgr\rtl\pwrmgr_wake_info.sv`
- `pwrmgr_pkg` (L10) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_wake_info.sv`
- `reg_pwrmgr.py` (L1) - `opentitan\hw\ip_templates\pwrmgr\util\reg_pwrmgr.py`
- `main()` (L14) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\util\reg_pwrmgr.py`
- `tb.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\tb.sv`
- `tb` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\tb.sv`
- `pwrmgr_test_pkg` (L10) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tb.sv`
- `pwrmgr_cov_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\cov\pwrmgr_cov_bind.sv`
- `pwrmgr_cov_bind` (L7) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\cov\pwrmgr_cov_bind.sv`
- `pwrmgr_ast_sva_if.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_ast_sva_if.sv`
- `pwrmgr_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_bind.sv`
- `pwrmgr_bind` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_bind.sv`
- `pwrmgr_clock_enables_sva_if.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_clock_enables_sva_if.sv`
- `pwrmgr_rstreqs_sva_if.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_rstreqs_sva_if.sv`
- `pwrmgr_sec_cm_checker_assert.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv`
- `pwrmgr_sec_cm_checker_assert` (L7) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv`
- `pwrmgr_unit_only_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_unit_only_bind.sv`
- `pwrmgr_unit_only_bind` (L6) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\sva\pwrmgr_unit_only_bind.sv`
- `pwrmgr_base_test.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\tests\pwrmgr_base_test.sv`
- `pwrmgr_test_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\dv\tests\pwrmgr_test_pkg.sv`
- `pwrmgr.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
- `pwrmgr` (L10) - `opentitan\hw\top_darjeeling\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
- `prim_clock_timeout` (L194) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
- `pwrmgr_reg_top` (L328) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
- `pwrmgr_cdc` (L415) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
- `pwrmgr_slow_fsm` (L553) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
- `pwrmgr_fsm` (L606) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv`
- `pwrmgr_wake_info` (L686) - `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv`

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
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `prim_pulse_sync` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_cdc.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `lc_ctrl_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr_fsm.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `pins_if` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `tl_if` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `prim_intr_hw` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\rtl\pwrmgr.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `alert_esc_if` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `pwrmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `pwrmgr_sec_cm_testplan.hjson` | `pwrmgr_sec_cm_checker_assert` | `opentitan\hw\ip_templates\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `pwrmgr_testplan.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr_testplan.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr_testplan.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr_testplan.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr_testplan.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr_testplan.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr_testplan.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `pwrmgr_testplan.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |

## Retrieval Guidance

- When a code-only query mentions `pwrmgr`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
