# Hardware Description: racl_ctrl

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `racl_ctrl`
- `approved_label`: `pending:racl_ctrl`
- `doc_anchor`: `racl_ctrl`
- `module_name_prefix`: `racl_ctrl`
- `bridge_edge_count`: 206

## Inferred Hardware Role

`racl_ctrl` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 222, interface: 29, component: 23, theory: 22, testplan: 14
- Code categories: dv: 118, rtl: 81, sva: 28
- Bridge relations: spec_path_matches_code_path: 184, spec_component_matches_code: 22

## Spec Anchors

- `component:racl_ctrl` (L1) - `__graphify_spec_only__/components.md`
- `racl_ctrl_testplan.hjson` (L1) - `opentitan/hw/ip/racl_ctrl/data/racl_ctrl_testplan.hjson`
- `import testplans` (L10) - `opentitan/hw/ip/racl_ctrl/data/racl_ctrl_testplan.hjson`
- `testpoints` (L28) - `opentitan/hw/ip/racl_ctrl/data/racl_ctrl_testplan.hjson`
- `desc` (L31) - `opentitan/hw/ip/racl_ctrl/data/racl_ctrl_testplan.hjson`
- `stage` (L38) - `opentitan/hw/ip/racl_ctrl/data/racl_ctrl_testplan.hjson`
- `tests` (L39) - `opentitan/hw/ip/racl_ctrl/data/racl_ctrl_testplan.hjson`
- `racl_ctrl.tpldesc.hjson` (L1) - `opentitan/hw/ip_templates/racl_ctrl/data/racl_ctrl.tpldesc.hjson`
- `template param list` (L5) - `opentitan/hw/ip_templates/racl_ctrl/data/racl_ctrl.tpldesc.hjson`
- `desc` (L8) - `opentitan/hw/ip_templates/racl_ctrl/data/racl_ctrl.tpldesc.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `Design Checklist` (L13) - `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `D1` (L15) - `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `D2` (L41) - `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `D2S` (L83) - `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `D3` (L103) - `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `Verification Checklist` (L129) - `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `V1` (L131) - `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `V2` (L181) - `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `V2S` (L227) - `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `V3` (L243) - `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `programmers_guide.md` (L1) - `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `Programmer's Guide` (L1) - `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `RACL Policies` (L5) - `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `Interrupts` (L11) - `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `Error Logs` (L16) - `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `Programming Sequence` (L29) - `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `Initializing the IP` (L31) - `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `Checking for and handling RACL errors` (L40) - `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `racl_ctrl.hjson` (L1) - `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/data/racl_ctrl.hjson`
- `human name` (L9) - `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/data/racl_ctrl.hjson`
- `one line desc` (L10) - `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/data/racl_ctrl.hjson`
- `one paragraph desc` (L11) - `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/data/racl_ctrl.hjson`
- `cip id` (L15) - `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/data/racl_ctrl.hjson`
- `design spec` (L16) - `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/data/racl_ctrl.hjson`

## Code Evidence

- `racl_ctrl_base_test.sv` (L1) - `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_base_test.sv`
- `racl_ctrl_test_pkg.sv` (L1) - `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_test_pkg.sv`
- `racl_ctrl_base_env_pkg` (L65) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv`
- `racl_ctrl_env_cfg.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv`
- `racl_ctrl_env_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv`
- `racl_ctrl_ral_pkg` (L11) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv`
- `tb.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv`
- `tb` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv`
- `racl_ctrl_test_pkg` (L13) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv`
- `racl_error_log_if` (L30) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv`
- `racl_ctrl_env_pkg` (L66) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv`
- `racl_ctrl_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\sva\racl_ctrl_bind.sv`
- `racl_ctrl_bind` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\sva\racl_ctrl_bind.sv`
- `racl_ctrl.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv`
- `racl_ctrl` (L7) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv`
- `racl_ctrl_reg_pkg` (L33) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_top.sv`
- `racl_ctrl_reg_top` (L47) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv`
- `prim_racl_error_arb` (L147) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv`
- `racl_ctrl_reg_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_pkg.sv`
- `racl_ctrl_reg_top.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_top.sv`
- `racl_ctrl_reg_top` (L9) - `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_top.sv`
- `racl_ctrl` (L2657) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `clkmgr_aon_cg_en_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv`
- `clkmgr_cg_en_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv`
- `clkmgr_div_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv`
- `clkmgr_extclk_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv`
- `clkmgr_gated_clock_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv`
- `clkmgr_lost_calib_ctrl_en_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv`
- `clkmgr_lost_calib_regwen_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv`
- `clkmgr_sec_cm_checker_assert.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv`
- `prim_flop_en` (L269) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `prim_ram_1p_adv` (L1487) - `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
- `tlul_cmd_intg_gen` (L46) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv`
- `dma` (L2221) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `keymgr_dpe` (L1905) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `tlul_jtag_dtm` (L1340) - `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
- `mbx` (L2257) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `prim_onehot_enc` (L128) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\sva\racl_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_bind` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\sva\racl_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_reg_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_reg_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_reg_top.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_reg_top` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_env_cfg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_env_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_ral_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_reg_top` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_base_test.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_base_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_test_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_test_pkg.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `prim_racl_error_arb` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_error_log_if` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `racl_ctrl_base_test.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_base_test.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `racl_ctrl_test_pkg.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `racl_ctrl_base_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `racl_ctrl_env_cfg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `racl_ctrl_env_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `racl_ctrl_ral_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `racl_ctrl_base_test.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_base_test.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `racl_ctrl_test_pkg.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `racl_ctrl_base_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `racl_ctrl_env_cfg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `racl_ctrl_env_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `racl_ctrl_ral_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `racl_ctrl_base_test.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_base_test.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `racl_ctrl_test_pkg.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `racl_ctrl_base_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `racl_ctrl_env_cfg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `racl_ctrl_env_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `racl_ctrl_ral_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `racl_ctrl_base_test.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_base_test.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `racl_ctrl_test_pkg.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `racl_ctrl_base_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `racl_ctrl_env_cfg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `racl_ctrl_env_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `racl_ctrl_ral_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |

## Retrieval Guidance

- When a code-only query mentions `racl_ctrl`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
