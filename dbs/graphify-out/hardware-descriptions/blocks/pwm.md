# Hardware Description: pwm

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `pwm`
- `approved_label`: `pending:pwm`
- `doc_anchor`: `pwm`
- `module_name_prefix`: `pwm`
- `bridge_edge_count`: 272

## Inferred Hardware Role

`pwm` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 188, testplan: 94, theory: 54, component: 33, interface: 24
- Code categories: dv: 106, rtl: 97, sva: 82, other_code: 9
- Bridge relations: spec_path_matches_code_path: 240, spec_component_matches_code: 32

## Spec Anchors

- `component:pwm` (L1) - `__graphify_spec_only__/components.md`
- `pwm.tpldesc.hjson` (L1) - `opentitan/hw/ip_templates/pwm/data/pwm.tpldesc.hjson`
- `template param list` (L5) - `opentitan/hw/ip_templates/pwm/data/pwm.tpldesc.hjson`
- `desc` (L8) - `opentitan/hw/ip_templates/pwm/data/pwm.tpldesc.hjson`
- `dtgen` (L29) - `opentitan/hw/ip_templates/pwm/data/pwm.tpldesc.hjson`
- `pwm_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip_templates/pwm/data/pwm_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip_templates/pwm/data/pwm_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip_templates/pwm/data/pwm_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip_templates/pwm/data/pwm_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip_templates/pwm/data/pwm_sec_cm_testplan.hjson`
- `pwm_testplan.hjson` (L1) - `opentitan/hw/ip_templates/pwm/data/pwm_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip_templates/pwm/data/pwm_testplan.hjson`
- `testpoints` (L11) - `opentitan/hw/ip_templates/pwm/data/pwm_testplan.hjson`
- `desc` (L14) - `opentitan/hw/ip_templates/pwm/data/pwm_testplan.hjson`
- `Stimulus` (L17) - `opentitan/hw/ip_templates/pwm/data/pwm_testplan.hjson`
- `Checking` (L22) - `opentitan/hw/ip_templates/pwm/data/pwm_testplan.hjson`
- `stage` (L26) - `opentitan/hw/ip_templates/pwm/data/pwm_testplan.hjson`
- `tests` (L27) - `opentitan/hw/ip_templates/pwm/data/pwm_testplan.hjson`
- `Checks` (L105) - `opentitan/hw/ip_templates/pwm/data/pwm_testplan.hjson`
- `covergroups` (L164) - `opentitan/hw/ip_templates/pwm/data/pwm_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip_templates/pwm/doc/checklist.md`
- `PWM Checklist` (L1) - `opentitan/hw/ip_templates/pwm/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip_templates/pwm/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip_templates/pwm/doc/checklist.md`
- `D2` (L32) - `opentitan/hw/ip_templates/pwm/doc/checklist.md`
- `D2S` (L74) - `opentitan/hw/ip_templates/pwm/doc/checklist.md`
- `D3` (L94) - `opentitan/hw/ip_templates/pwm/doc/checklist.md`
- `Verification Checklist` (L120) - `opentitan/hw/ip_templates/pwm/doc/checklist.md`
- `V1` (L122) - `opentitan/hw/ip_templates/pwm/doc/checklist.md`
- `V2` (L172) - `opentitan/hw/ip_templates/pwm/doc/checklist.md`
- `V2S` (L218) - `opentitan/hw/ip_templates/pwm/doc/checklist.md`
- `programmers_guide.md` (L1) - `opentitan/hw/ip_templates/pwm/doc/programmers_guide.md`
- `Programmer's Guide` (L1) - `opentitan/hw/ip_templates/pwm/doc/programmers_guide.md`
- `Device Interface Functions DIFs` (L37) - `opentitan/hw/ip_templates/pwm/doc/programmers_guide.md`
- `theory_of_operation.md` (L1) - `opentitan/hw/ip_templates/pwm/doc/theory_of_operation.md`

## Code Evidence

- `tb.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv`
- `pwm_env_pkg` (L9) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tests\pwm_test_pkg.sv`
- `pwm_test_pkg` (L10) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv`
- `pwm_monitor_pkg` (L11) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv`
- `tb` (L5) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv`
- `pwm_if` (L58) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv`
- `pwm_bind.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\sva\pwm_bind.sv`
- `pwm_bind` (L5) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\sva\pwm_bind.sv`
- `pwm_base_test.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tests\pwm_base_test.sv`
- `pwm_test_pkg.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tests\pwm_test_pkg.sv`
- `pwm.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm.sv`
- `pwm` (L7) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm.sv`
- `pwm_reg_pkg` (L33) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_reg_top.sv`
- `pwm_reg_top` (L42) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm.sv`
- `pwm_core` (L84) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm.sv`
- `pwm_chan.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_chan.sv`
- `pwm_chan` (L5) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_chan.sv`
- `pwm_core.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_core.sv`
- `pwm_core` (L7) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_core.sv`
- `pwm_reg_pkg.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_reg_pkg.sv`
- `pwm_reg_top.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_reg_top.sv`
- `pwm_reg_top` (L9) - `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_reg_top.sv`
- `pwm` (L2071) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
- `pwm.rs` (L1) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs`
- `PwmPeriod` (L9) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs`
- `Sample` (L18) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs`
- `Sample<PIN>` (L22) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs`
- `.pin()` (L23) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs`
- `Decoder` (L28) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs`
- `Decoder<PIN>` (L33) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs`
- `.decode_period()` (L34) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs`
- `.run()` (L53) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs`
- `clkmgr_aon_cg_en_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv`
- `clkmgr_cg_en_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv`
- `clkmgr_div_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv`
- `clkmgr_extclk_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv`
- `clkmgr_gated_clock_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv`
- `clkmgr_lost_calib_ctrl_en_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv`
- `clkmgr_lost_calib_regwen_sva_if.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv`
- `clkmgr_sec_cm_checker_assert.sv` (L1) - `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv`
- `prim_alert_sender` (L268) - `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
- `prim_alert_pkg` (L11) - `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
- `prim_esc_pkg` (L12) - `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
- `prim_secded_inv_72_64_enc` (L39) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv`
- `prim_sec_anchor_flop` (L275) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:pwm` | `pwm_base_test.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tests\pwm_base_test.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_env_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tests\pwm_test_pkg.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_test_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tests\pwm_test_pkg.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_bind.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\sva\pwm_bind.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_bind` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\sva\pwm_bind.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_reg_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_reg_top.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_reg_pkg.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_reg_top.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_reg_top.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_reg_top` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_reg_top.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_chan.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_chan.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_chan` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_chan.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_core.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_core.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_core` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm_core.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_reg_top` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_core` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\rtl\pwm.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_test_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_monitor_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm_if` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_component_matches_code` | `component:pwm` | `tb.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_component_matches_code` | `component:pwm` | `tb` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_component_matches_code` | `component:pwm` | `pwm.rs` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs` |
| `spec_component_matches_code` | `component:pwm` | `PwmPeriod` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs` |
| `spec_component_matches_code` | `component:pwm` | `Sample` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs` |
| `spec_component_matches_code` | `component:pwm` | `Sample<PIN>` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs` |
| `spec_component_matches_code` | `component:pwm` | `.pin()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs` |
| `spec_component_matches_code` | `component:pwm` | `Decoder` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs` |
| `spec_component_matches_code` | `component:pwm` | `Decoder<PIN>` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs` |
| `spec_component_matches_code` | `component:pwm` | `.decode_period()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs` |
| `spec_component_matches_code` | `component:pwm` | `.run()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\pwm.rs` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `tb.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `pwm_env_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tests\pwm_test_pkg.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `pwm_test_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `pwm_monitor_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `tb` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `pwm_if` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `pwm_bind.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\sva\pwm_bind.sv` |
| `spec_path_matches_code_path` | `pwm.tpldesc.hjson` | `pwm_bind` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\sva\pwm_bind.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `pwm_env_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tests\pwm_test_pkg.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `pwm_test_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `pwm_monitor_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `pwm_if` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `pwm_bind.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\sva\pwm_bind.sv` |
| `spec_path_matches_code_path` | `pwm_sec_cm_testplan.hjson` | `pwm_bind` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\sva\pwm_bind.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `tb.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `pwm_env_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tests\pwm_test_pkg.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `pwm_test_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `pwm_monitor_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `tb` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `pwm_if` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tb.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `pwm_bind.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\sva\pwm_bind.sv` |
| `spec_path_matches_code_path` | `pwm_testplan.hjson` | `pwm_bind` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\sva\pwm_bind.sv` |

## Retrieval Guidance

- When a code-only query mentions `pwm`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
