# Hardware Description: rv_plic

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `rv_plic`
- `approved_label`: `pending:rv_plic`
- `doc_anchor`: `rv_plic`
- `module_name_prefix`: `rv_plic`
- `bridge_edge_count`: 456

## Inferred Hardware Role

`rv_plic` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 438, testplan: 141, theory: 100, component: 41, interface: 4
- Code categories: rtl: 422, sva: 60, dv: 28
- Bridge relations: spec_path_matches_code_path: 416, spec_component_matches_code: 40

## Spec Anchors

- `component:rv_plic` (L1) - `__graphify_spec_only__/components.md`
- `rv_plic.tpldesc.hjson` (L1) - `opentitan/hw/ip_templates/rv_plic/data/rv_plic.tpldesc.hjson`
- `template param list` (L5) - `opentitan/hw/ip_templates/rv_plic/data/rv_plic.tpldesc.hjson`
- `desc` (L8) - `opentitan/hw/ip_templates/rv_plic/data/rv_plic.tpldesc.hjson`
- `dtgen` (L23) - `opentitan/hw/ip_templates/rv_plic/data/rv_plic.tpldesc.hjson`
- `rv_plic_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip_templates/rv_plic/data/rv_plic_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip_templates/rv_plic/data/rv_plic_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip_templates/rv_plic/data/rv_plic_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip_templates/rv_plic/data/rv_plic_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip_templates/rv_plic/data/rv_plic_sec_cm_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `RV PLIC Checklist` (L1) - `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `D2` (L34) - `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `D2S` (L72) - `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `D3` (L92) - `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `Verification Checklist` (L118) - `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `V1` (L120) - `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `V2` (L170) - `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `V2S` (L216) - `opentitan/hw/ip_templates/rv_plic/doc/checklist.md`
- `README.md` (L1) - `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `RV PLIC DV document` (L1) - `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `Goals` (L3) - `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `Current status` (L12) - `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `Design features` (L17) - `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `Testbench architecture` (L21) - `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `Block diagram` (L25) - `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `TLUL assertions` (L28) - `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `RV PLIC assertions` (L35) - `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `Symbolic variables` (L39) - `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `Testplan` (L47) - `opentitan/hw/ip_templates/rv_plic/doc/dv/README.md`
- `programmers_guide.md` (L1) - `opentitan/hw/ip_templates/rv_plic/doc/programmers_guide.md`
- `Programmer's Guide` (L1) - `opentitan/hw/ip_templates/rv_plic/doc/programmers_guide.md`
- `Initialization` (L3) - `opentitan/hw/ip_templates/rv_plic/doc/programmers_guide.md`

## Code Evidence

- `prim_subreg` (L671) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
- `tlul_cmd_intg_chk` (L48) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
- `prim_reg_we_check` (L56) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
- `tlul_rsp_intg_gen` (L81) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
- `tlul_adapter_reg` (L92) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
- `prim_subreg_ext` (L8023) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
- `prim_max_tree` (L42) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_target.sv`
- `rv_plic_bind_fpv.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv`
- `rv_plic_bind_fpv` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv`
- `rv_plic_reg_pkg` (L22) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
- `rv_plic_tb.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv`
- `rv_plic_tb` (L7) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv`
- `rv_plic_assert_fpv.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv`
- `rv_plic_assert_fpv` (L8) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv`
- `rv_plic.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic.sv`
- `rv_plic` (L19) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic.sv`
- `rv_plic_gateway` (L241) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic.sv`
- `rv_plic_gateway.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_gateway.sv`
- `rv_plic_gateway` (L7) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_gateway.sv`
- `rv_plic_reg_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_reg_pkg.sv`
- `rv_plic_reg_top.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
- `rv_plic_reg_top` (L9) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
- `rv_plic_target.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_target.sv`
- `rv_plic_target` (L17) - `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\rtl\rv_plic_target.sv`
- `rv_plic_bind_fpv.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv`
- `rv_plic_bind_fpv` (L5) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv`
- `rv_plic_tb.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv`
- `rv_plic_tb` (L7) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv`
- `rv_plic_assert_fpv.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv`
- `rv_plic_assert_fpv` (L8) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv`
- `rv_plic.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic.sv`
- `rv_plic` (L19) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic.sv`
- `rv_plic_gateway.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic_gateway.sv`
- `rv_plic_gateway` (L7) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic_gateway.sv`
- `rv_plic_reg_pkg.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic_reg_pkg.sv`
- `rv_plic_reg_top.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
- `rv_plic_reg_top` (L9) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv`
- `rv_plic_target.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic_target.sv`
- `rv_plic_target` (L17) - `opentitan\hw\top_earlgrey\ip_autogen\rv_plic\rtl\rv_plic_target.sv`
- `rv_plic_bind_fpv.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv`
- `rv_plic_bind_fpv` (L5) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv`
- `rv_plic_tb.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv`
- `rv_plic_tb` (L7) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\tb\rv_plic_tb.sv`
- `rv_plic_assert_fpv.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv`
- `rv_plic_assert_fpv` (L8) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv`

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
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `prim_subreg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `tlul_cmd_intg_chk` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `prim_reg_we_check` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `tlul_rsp_intg_gen` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `tlul_adapter_reg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `prim_subreg_ext` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `prim_max_tree` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_target.sv` |
| `spec_path_matches_code_path` | `rv_plic_sec_cm_testplan.hjson` | `rv_plic_bind_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_plic\fpv\tb\rv_plic_bind_fpv.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |

## Retrieval Guidance

- When a code-only query mentions `rv_plic`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
