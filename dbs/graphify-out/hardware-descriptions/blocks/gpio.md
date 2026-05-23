# Hardware Description: gpio

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `gpio`
- `approved_label`: `pending:gpio`
- `doc_anchor`: `gpio`
- `module_name_prefix`: `gpio`
- `bridge_edge_count`: 520

## Inferred Hardware Role

`gpio` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 426, testplan: 150, theory: 73, interface: 72, component: 41
- Code categories: rtl: 289, dv: 181, sva: 96, other_code: 36
- Bridge relations: spec_path_matches_code_path: 480, spec_component_matches_code: 40

## Spec Anchors

- `component:gpio` (L1) - `__graphify_spec_only__/components.md`
- `gpio.tpldesc.hjson` (L1) - `opentitan/hw/ip_templates/gpio/data/gpio.tpldesc.hjson`
- `template param list` (L5) - `opentitan/hw/ip_templates/gpio/data/gpio.tpldesc.hjson`
- `desc` (L8) - `opentitan/hw/ip_templates/gpio/data/gpio.tpldesc.hjson`
- `dtgen` (L29) - `opentitan/hw/ip_templates/gpio/data/gpio.tpldesc.hjson`
- `gpio_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip_templates/gpio/data/gpio_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip_templates/gpio/data/gpio_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip_templates/gpio/data/gpio_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip_templates/gpio/data/gpio_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip_templates/gpio/data/gpio_sec_cm_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `GPIO Checklist` (L1) - `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `D2` (L36) - `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `D2S` (L78) - `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `D3` (L98) - `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `Verification Checklist` (L124) - `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `V1` (L126) - `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `V2` (L178) - `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `V2S` (L229) - `opentitan/hw/ip_templates/gpio/doc/checklist.md`
- `gpio.hjson` (L1) - `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `human name` (L6) - `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `one line desc` (L7) - `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `cip id` (L15) - `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `design spec` (L16) - `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `dv doc` (L17) - `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `hw checklist` (L18) - `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `sw checklist` (L19) - `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `revisions` (L20) - `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `version` (L22) - `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio.hjson`
- `gpio_sec_cm_testplan.hjson` (L1) - `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/top_darjeeling/ip_autogen/gpio/data/gpio_sec_cm_testplan.hjson`

## Code Evidence

- `tl_agent_pkg` (L10) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv`
- `gpio_straps_if.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv`
- `gpio_pkg` (L10) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv`
- `gpio_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv`
- `gpio_bind` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv`
- `tb.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tb\tb.sv`
- `tb` (L6) - `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tb\tb.sv`
- `gpio_env_pkg` (L9) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv`
- `gpio_test_pkg` (L12) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv`
- `gpio_reg_pkg` (L32) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_reg_top.sv`
- `gpio_straps_if` (L36) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv`
- `gpio_base_test.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tests\gpio_base_test.sv`
- `gpio_test_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv`
- `gpio.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio.sv`
- `gpio` (L9) - `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio.sv`
- `gpio_reg_top` (L220) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv`
- `gpio_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_pkg.sv`
- `gpio_reg_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_reg_pkg.sv`
- `gpio_reg_top.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_reg_top.sv`
- `gpio_reg_top` (L9) - `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_reg_top.sv`
- `gpio_straps_if.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv`
- `gpio_bind.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\sva\gpio_bind.sv`
- `gpio_bind` (L5) - `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\sva\gpio_bind.sv`
- `tb.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\tb\tb.sv`
- `tb` (L6) - `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\tb\tb.sv`
- `gpio_base_test.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\tests\gpio_base_test.sv`
- `gpio_test_pkg.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv`
- `gpio.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio.sv`
- `gpio` (L9) - `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio.sv`
- `gpio_pkg.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_pkg.sv`
- `gpio_reg_pkg.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_reg_pkg.sv`
- `gpio_reg_top.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_reg_top.sv`
- `gpio_reg_top` (L9) - `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_reg_top.sv`
- `gpio_straps_if.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv`
- `gpio_bind.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\sva\gpio_bind.sv`
- `gpio_bind` (L5) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\sva\gpio_bind.sv`
- `tb.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv`
- `tb` (L6) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv`
- `gpio_base_test.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_base_test.sv`
- `gpio_test_pkg.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv`
- `gpio.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv`
- `gpio` (L9) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv`
- `gpio_pkg.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_pkg.sv`
- `gpio_reg_pkg.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_reg_pkg.sv`
- `gpio_reg_top.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_reg_top.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:gpio` | `gpio_straps_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_base_test.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_base_test.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_straps_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_env_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_test_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_straps_if.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_base_test.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tests\gpio_base_test.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_reg_top.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_test_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_bind.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_bind` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_reg_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_top.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_reg_top.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_reg_top.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_base_test.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\tests\gpio_base_test.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_test_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_bind` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_reg_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_top.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_reg_top.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_top` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_reg_top.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_test_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_straps_if` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_bind.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_bind` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_reg_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_top.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_reg_top.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_reg_top` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_reg_top.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio_pkg.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio.sv` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_component_matches_code` | `component:gpio` | `gpio` | `opentitan\hw\top_earlgrey\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `tl_agent_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `gpio_straps_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `gpio_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `gpio_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `gpio_bind` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `gpio_env_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio.tpldesc.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `tl_agent_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `gpio_straps_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `gpio_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `gpio_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `gpio_bind` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `gpio_env_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `gpio_sec_cm_testplan.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tl_agent_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `gpio_straps_if.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `gpio_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\rtl\gpio.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `gpio_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `gpio_bind` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\sva\gpio_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\gpio\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `gpio_env_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\tests\gpio_test_pkg.sv` |

## Retrieval Guidance

- When a code-only query mentions `gpio`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
