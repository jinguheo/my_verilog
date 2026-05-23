# Hardware Description: keymgr

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `keymgr`
- `approved_label`: `pending:keymgr`
- `doc_anchor`: `keymgr`
- `module_name_prefix`: `keymgr`
- `bridge_edge_count`: 112

## Inferred Hardware Role

`keymgr` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 83, component: 41, testplan: 30, theory: 19, interface: 15
- Code categories: dv: 79, rtl: 62, sva: 13, other_code: 3
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Anchors

- `component:keymgr` (L1) - `__graphify_spec_only__/components.md`
- `keymgr.hjson` (L1) - `opentitan/hw/ip/keymgr/data/keymgr.hjson`
- `human name` (L6) - `opentitan/hw/ip/keymgr/data/keymgr.hjson`
- `one line desc` (L7) - `opentitan/hw/ip/keymgr/data/keymgr.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/ip/keymgr/data/keymgr.hjson`
- `cip id` (L18) - `opentitan/hw/ip/keymgr/data/keymgr.hjson`
- `design spec` (L19) - `opentitan/hw/ip/keymgr/data/keymgr.hjson`
- `dv doc` (L20) - `opentitan/hw/ip/keymgr/data/keymgr.hjson`
- `hw checklist` (L21) - `opentitan/hw/ip/keymgr/data/keymgr.hjson`
- `sw checklist` (L22) - `opentitan/hw/ip/keymgr/data/keymgr.hjson`
- `revisions` (L23) - `opentitan/hw/ip/keymgr/data/keymgr.hjson`
- `version` (L25) - `opentitan/hw/ip/keymgr/data/keymgr.hjson`
- `keymgr_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/keymgr/data/keymgr_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/keymgr/data/keymgr_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/keymgr/data/keymgr_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/keymgr/data/keymgr_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/keymgr/data/keymgr_sec_cm_testplan.hjson`
- `keymgr_testplan.hjson` (L1) - `opentitan/hw/ip/keymgr/data/keymgr_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/keymgr/data/keymgr_testplan.hjson`
- `testpoints` (L15) - `opentitan/hw/ip/keymgr/data/keymgr_testplan.hjson`
- `desc` (L18) - `opentitan/hw/ip/keymgr/data/keymgr_testplan.hjson`
- `Stimulus` (L22) - `opentitan/hw/ip/keymgr/data/keymgr_testplan.hjson`
- `Checks` (L30) - `opentitan/hw/ip/keymgr/data/keymgr_testplan.hjson`
- `stage` (L39) - `opentitan/hw/ip/keymgr/data/keymgr_testplan.hjson`
- `tests` (L40) - `opentitan/hw/ip/keymgr/data/keymgr_testplan.hjson`
- `covergroups` (L212) - `opentitan/hw/ip/keymgr/data/keymgr_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/keymgr/doc/checklist.md`
- `KEYMGR Checklist` (L1) - `opentitan/hw/ip/keymgr/doc/checklist.md`
- `Design Checklist` (L11) - `opentitan/hw/ip/keymgr/doc/checklist.md`
- `D1` (L13) - `opentitan/hw/ip/keymgr/doc/checklist.md`
- `D2` (L37) - `opentitan/hw/ip/keymgr/doc/checklist.md`
- `D2S` (L79) - `opentitan/hw/ip/keymgr/doc/checklist.md`
- `D3` (L99) - `opentitan/hw/ip/keymgr/doc/checklist.md`
- `Verification Checklist` (L125) - `opentitan/hw/ip/keymgr/doc/checklist.md`
- `V1` (L127) - `opentitan/hw/ip/keymgr/doc/checklist.md`

## Code Evidence

- `tb.sv` (L1) - `opentitan\hw\ip\keymgr\dv\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\keymgr\dv\tb.sv`
- `keymgr_env_pkg` (L9) - `opentitan\hw\ip\keymgr\dv\tests\keymgr_test_pkg.sv`
- `keymgr_test_pkg` (L10) - `opentitan\hw\ip\keymgr\dv\tb.sv`
- `keymgr_if` (L24) - `opentitan\hw\ip\keymgr\dv\tb.sv`
- `keymgr_cov_bind.sv` (L1) - `opentitan\hw\ip\keymgr\dv\cov\keymgr_cov_bind.sv`
- `keymgr_cov_bind` (L6) - `opentitan\hw\ip\keymgr\dv\cov\keymgr_cov_bind.sv`
- `keymgr_bind.sv` (L1) - `opentitan\hw\ip\keymgr\dv\sva\keymgr_bind.sv`
- `keymgr_bind` (L5) - `opentitan\hw\ip\keymgr\dv\sva\keymgr_bind.sv`
- `keymgr_base_test.sv` (L1) - `opentitan\hw\ip\keymgr\dv\tests\keymgr_base_test.sv`
- `keymgr_test_pkg.sv` (L1) - `opentitan\hw\ip\keymgr\dv\tests\keymgr_test_pkg.sv`
- `keymgr.sv` (L1) - `opentitan\hw\ip\keymgr\rtl\keymgr.sv`
- `keymgr` (L10) - `opentitan\hw\ip\keymgr\rtl\keymgr.sv`
- `keymgr_reg_pkg` (L26) - `opentitan\hw\ip\keymgr\rtl\keymgr_reg_top.sv`
- `keymgr_reg_top` (L148) - `opentitan\hw\ip\keymgr\rtl\keymgr.sv`
- `keymgr_ctrl` (L283) - `opentitan\hw\ip\keymgr\rtl\keymgr.sv`
- `keymgr_cfg_en.sv` (L1) - `opentitan\hw\ip\keymgr\rtl\keymgr_cfg_en.sv`
- `keymgr_cfg_en` (L10) - `opentitan\hw\ip\keymgr\rtl\keymgr_cfg_en.sv`
- `keymgr_ctrl.sv` (L1) - `opentitan\hw\ip\keymgr\rtl\keymgr_ctrl.sv`
- `keymgr_ctrl` (L10) - `opentitan\hw\ip\keymgr\rtl\keymgr_ctrl.sv`
- `keymgr_data_en_state.sv` (L1) - `opentitan\hw\ip\keymgr\rtl\keymgr_data_en_state.sv`
- `keymgr_data_en_state` (L10) - `opentitan\hw\ip\keymgr\rtl\keymgr_data_en_state.sv`
- `keymgr_err.sv` (L1) - `opentitan\hw\ip\keymgr\rtl\keymgr_err.sv`
- `keymgr_err` (L10) - `opentitan\hw\ip\keymgr\rtl\keymgr_err.sv`
- `keymgr_input_checks.sv` (L1) - `opentitan\hw\ip\keymgr\rtl\keymgr_input_checks.sv`
- `keymgr_input_checks` (L11) - `opentitan\hw\ip\keymgr\rtl\keymgr_input_checks.sv`
- `prim_msb_extend` (L42) - `opentitan\hw\ip\keymgr\rtl\keymgr_input_checks.sv`
- `keymgr_kmac_if.sv` (L1) - `opentitan\hw\ip\keymgr\rtl\keymgr_kmac_if.sv`
- `keymgr_kmac_if` (L10) - `opentitan\hw\ip\keymgr\rtl\keymgr_kmac_if.sv`
- `keymgr_op_state_ctrl.sv` (L1) - `opentitan\hw\ip\keymgr\rtl\keymgr_op_state_ctrl.sv`
- `keymgr_op_state_ctrl` (L10) - `opentitan\hw\ip\keymgr\rtl\keymgr_op_state_ctrl.sv`
- `keymgr_pkg.sv` (L1) - `opentitan\hw\ip\keymgr\rtl\keymgr_pkg.sv`
- `keymgr_reg_pkg.sv` (L1) - `opentitan\hw\ip\keymgr\rtl\keymgr_reg_pkg.sv`
- `keymgr_reg_top.sv` (L1) - `opentitan\hw\ip\keymgr\rtl\keymgr_reg_top.sv`
- `keymgr_reg_top` (L9) - `opentitan\hw\ip\keymgr\rtl\keymgr_reg_top.sv`
- `keymgr_reseed_ctrl.sv` (L1) - `opentitan\hw\ip\keymgr\rtl\keymgr_reseed_ctrl.sv`
- `keymgr_reseed_ctrl` (L10) - `opentitan\hw\ip\keymgr\rtl\keymgr_reseed_ctrl.sv`
- `keymgr_sideload_key.sv` (L1) - `opentitan\hw\ip\keymgr\rtl\keymgr_sideload_key.sv`
- `keymgr_sideload_key` (L9) - `opentitan\hw\ip\keymgr\rtl\keymgr_sideload_key.sv`
- `keymgr_sideload_key_ctrl.sv` (L1) - `opentitan\hw\ip\keymgr\rtl\keymgr_sideload_key_ctrl.sv`
- `keymgr_sideload_key_ctrl` (L9) - `opentitan\hw\ip\keymgr\rtl\keymgr_sideload_key_ctrl.sv`
- `keymgr_sideload_key` (L148) - `opentitan\hw\ip\keymgr\rtl\keymgr_sideload_key_ctrl.sv`
- `rom_e2e_keymgr_init_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\keymgr\rom_e2e_keymgr_init_test.c`
- `print_otp_sw_cfg_digests()` (L35) - `opentitan\sw\device\silicon_creator\rom\e2e\keymgr\rom_e2e_keymgr_init_test.c`
- `test_main()` (L47) - `opentitan\sw\device\silicon_creator\rom\e2e\keymgr\rom_e2e_keymgr_init_test.c`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:keymgr` | `keymgr_sideload_key_ctrl.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr_sideload_key_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_sideload_key_ctrl` | `opentitan\hw\ip\keymgr\rtl\keymgr_sideload_key_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_sideload_key` | `opentitan\hw\ip\keymgr\rtl\keymgr_sideload_key_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_base_test.sv` | `opentitan\hw\ip\keymgr\dv\tests\keymgr_base_test.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_env_pkg` | `opentitan\hw\ip\keymgr\dv\tests\keymgr_test_pkg.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_test_pkg.sv` | `opentitan\hw\ip\keymgr\dv\tests\keymgr_test_pkg.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_data_en_state.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr_data_en_state.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_data_en_state` | `opentitan\hw\ip\keymgr\rtl\keymgr_data_en_state.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_op_state_ctrl.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr_op_state_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_op_state_ctrl` | `opentitan\hw\ip\keymgr\rtl\keymgr_op_state_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_input_checks.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr_input_checks.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_input_checks` | `opentitan\hw\ip\keymgr\rtl\keymgr_input_checks.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_sideload_key.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr_sideload_key.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_sideload_key` | `opentitan\hw\ip\keymgr\rtl\keymgr_sideload_key.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_cov_bind.sv` | `opentitan\hw\ip\keymgr\dv\cov\keymgr_cov_bind.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_cov_bind` | `opentitan\hw\ip\keymgr\dv\cov\keymgr_cov_bind.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_reseed_ctrl.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr_reseed_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_reseed_ctrl` | `opentitan\hw\ip\keymgr\rtl\keymgr_reseed_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_bind.sv` | `opentitan\hw\ip\keymgr\dv\sva\keymgr_bind.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_bind` | `opentitan\hw\ip\keymgr\dv\sva\keymgr_bind.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_reg_pkg` | `opentitan\hw\ip\keymgr\rtl\keymgr_reg_top.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_kmac_if.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr_kmac_if.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_kmac_if` | `opentitan\hw\ip\keymgr\rtl\keymgr_kmac_if.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_reg_pkg.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr_reg_pkg.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_reg_top.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr_reg_top.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_reg_top` | `opentitan\hw\ip\keymgr\rtl\keymgr_reg_top.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_cfg_en.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr_cfg_en.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_cfg_en` | `opentitan\hw\ip\keymgr\rtl\keymgr_cfg_en.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_ctrl.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_ctrl` | `opentitan\hw\ip\keymgr\rtl\keymgr_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_err.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr_err.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_err` | `opentitan\hw\ip\keymgr\rtl\keymgr_err.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_pkg.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr_pkg.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr` | `opentitan\hw\ip\keymgr\rtl\keymgr.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_reg_top` | `opentitan\hw\ip\keymgr\rtl\keymgr.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_ctrl` | `opentitan\hw\ip\keymgr\rtl\keymgr.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_test_pkg` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_component_matches_code` | `component:keymgr` | `keymgr_if` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr.hjson` | `tb.sv` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr.hjson` | `tb` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr.hjson` | `keymgr_env_pkg` | `opentitan\hw\ip\keymgr\dv\tests\keymgr_test_pkg.sv` |
| `spec_path_matches_code_path` | `keymgr.hjson` | `keymgr_test_pkg` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr.hjson` | `keymgr_if` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr.hjson` | `keymgr_cov_bind.sv` | `opentitan\hw\ip\keymgr\dv\cov\keymgr_cov_bind.sv` |
| `spec_path_matches_code_path` | `keymgr.hjson` | `keymgr_cov_bind` | `opentitan\hw\ip\keymgr\dv\cov\keymgr_cov_bind.sv` |
| `spec_path_matches_code_path` | `keymgr.hjson` | `keymgr_bind.sv` | `opentitan\hw\ip\keymgr\dv\sva\keymgr_bind.sv` |
| `spec_path_matches_code_path` | `keymgr_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_sec_cm_testplan.hjson` | `keymgr_env_pkg` | `opentitan\hw\ip\keymgr\dv\tests\keymgr_test_pkg.sv` |
| `spec_path_matches_code_path` | `keymgr_sec_cm_testplan.hjson` | `keymgr_test_pkg` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_sec_cm_testplan.hjson` | `keymgr_if` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_sec_cm_testplan.hjson` | `keymgr_cov_bind.sv` | `opentitan\hw\ip\keymgr\dv\cov\keymgr_cov_bind.sv` |
| `spec_path_matches_code_path` | `keymgr_sec_cm_testplan.hjson` | `keymgr_cov_bind` | `opentitan\hw\ip\keymgr\dv\cov\keymgr_cov_bind.sv` |
| `spec_path_matches_code_path` | `keymgr_sec_cm_testplan.hjson` | `keymgr_bind.sv` | `opentitan\hw\ip\keymgr\dv\sva\keymgr_bind.sv` |
| `spec_path_matches_code_path` | `keymgr_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_testplan.hjson` | `tb` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_testplan.hjson` | `keymgr_env_pkg` | `opentitan\hw\ip\keymgr\dv\tests\keymgr_test_pkg.sv` |
| `spec_path_matches_code_path` | `keymgr_testplan.hjson` | `keymgr_test_pkg` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_testplan.hjson` | `keymgr_if` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_testplan.hjson` | `keymgr_cov_bind.sv` | `opentitan\hw\ip\keymgr\dv\cov\keymgr_cov_bind.sv` |
| `spec_path_matches_code_path` | `keymgr_testplan.hjson` | `keymgr_cov_bind` | `opentitan\hw\ip\keymgr\dv\cov\keymgr_cov_bind.sv` |
| `spec_path_matches_code_path` | `keymgr_testplan.hjson` | `keymgr_bind.sv` | `opentitan\hw\ip\keymgr\dv\sva\keymgr_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `keymgr_env_pkg` | `opentitan\hw\ip\keymgr\dv\tests\keymgr_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `keymgr_test_pkg` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `keymgr_if` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `keymgr_cov_bind.sv` | `opentitan\hw\ip\keymgr\dv\cov\keymgr_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `keymgr_cov_bind` | `opentitan\hw\ip\keymgr\dv\cov\keymgr_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `keymgr_bind.sv` | `opentitan\hw\ip\keymgr\dv\sva\keymgr_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `keymgr_env_pkg` | `opentitan\hw\ip\keymgr\dv\tests\keymgr_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `keymgr_test_pkg` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `keymgr_if` | `opentitan\hw\ip\keymgr\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `keymgr_cov_bind.sv` | `opentitan\hw\ip\keymgr\dv\cov\keymgr_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `keymgr_cov_bind` | `opentitan\hw\ip\keymgr\dv\cov\keymgr_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `keymgr_bind.sv` | `opentitan\hw\ip\keymgr\dv\sva\keymgr_bind.sv` |

## Retrieval Guidance

- When a code-only query mentions `keymgr`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
