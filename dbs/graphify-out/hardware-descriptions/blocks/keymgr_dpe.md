# Hardware Description: keymgr_dpe

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `keymgr_dpe`
- `approved_label`: `pending:keymgr_dpe`
- `doc_anchor`: `keymgr_dpe`
- `module_name_prefix`: `keymgr_dpe`
- `bridge_edge_count`: 107

## Inferred Hardware Role

`keymgr_dpe` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 83, component: 36, testplan: 29, theory: 19, interface: 14
- Code categories: rtl: 101, dv: 36, sva: 4
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 35

## Spec Anchors

- `component:keymgr_dpe` (L1) - `__graphify_spec_only__/components.md`
- `keymgr_dpe.hjson` (L1) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `human name` (L6) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `one line desc` (L7) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `cip id` (L13) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `design spec` (L14) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `dv doc` (L15) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `hw checklist` (L16) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `sw checklist` (L17) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `revisions` (L18) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `version` (L20) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe.hjson`
- `keymgr_dpe_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_sec_cm_testplan.hjson`
- `keymgr_dpe_testplan.hjson` (L1) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `testpoints` (L14) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `desc` (L17) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `Stimulus` (L21) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `Checks` (L30) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `stage` (L38) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `tests` (L39) - `opentitan/hw/ip/keymgr_dpe/data/keymgr_dpe_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `KEYMGR Checklist` (L1) - `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `D2` (L34) - `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `D2S` (L76) - `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `D3` (L96) - `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `Verification Checklist` (L122) - `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `V1` (L124) - `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`
- `V2` (L174) - `opentitan/hw/ip/keymgr_dpe/doc/checklist.md`

## Code Evidence

- `prim_sec_anchor_const` (L105) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
- `keymgr_reseed_ctrl` (L179) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
- `keymgr_cfg_en` (L343) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
- `keymgr_input_checks` (L508) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
- `keymgr_kmac_if` (L582) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
- `keymgr_sideload_key_ctrl` (L614) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\keymgr_dpe\dv\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\keymgr_dpe\dv\tb.sv`
- `keymgr_dpe_env_pkg` (L9) - `opentitan\hw\ip\keymgr_dpe\dv\tests\keymgr_dpe_test_pkg.sv`
- `keymgr_dpe_test_pkg` (L10) - `opentitan\hw\ip\keymgr_dpe\dv\tb.sv`
- `keymgr_dpe_if` (L26) - `opentitan\hw\ip\keymgr_dpe\dv\tb.sv`
- `keymgr_dpe_cov_bind.sv` (L1) - `opentitan\hw\ip\keymgr_dpe\dv\cov\keymgr_dpe_cov_bind.sv`
- `keymgr_dpe_cov_bind` (L6) - `opentitan\hw\ip\keymgr_dpe\dv\cov\keymgr_dpe_cov_bind.sv`
- `keymgr_dpe_bind.sv` (L1) - `opentitan\hw\ip\keymgr_dpe\dv\sva\keymgr_dpe_bind.sv`
- `keymgr_dpe_bind` (L5) - `opentitan\hw\ip\keymgr_dpe\dv\sva\keymgr_dpe_bind.sv`
- `keymgr_dpe_base_test.sv` (L1) - `opentitan\hw\ip\keymgr_dpe\dv\tests\keymgr_dpe_base_test.sv`
- `keymgr_dpe_test_pkg.sv` (L1) - `opentitan\hw\ip\keymgr_dpe\dv\tests\keymgr_dpe_test_pkg.sv`
- `keymgr_dpe.sv` (L1) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
- `keymgr_dpe` (L10) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
- `keymgr_dpe_pkg` (L11) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_op_state_ctrl.sv`
- `keymgr_dpe_reg_pkg` (L26) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_reg_top.sv`
- `keymgr_dpe_reg_top` (L129) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
- `keymgr_dpe_ctrl` (L279) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv`
- `keymgr_dpe_ctrl.sv` (L1) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv`
- `keymgr_dpe_ctrl` (L10) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv`
- `keymgr_dpe_op_state_ctrl` (L610) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv`
- `keymgr_data_en_state` (L632) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv`
- `keymgr_err` (L694) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv`
- `keymgr_dpe_op_state_ctrl.sv` (L1) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_op_state_ctrl.sv`
- `keymgr_dpe_op_state_ctrl` (L10) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_op_state_ctrl.sv`
- `keymgr_dpe_pkg.sv` (L1) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_pkg.sv`
- `keymgr_dpe_reg_pkg.sv` (L1) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_reg_pkg.sv`
- `keymgr_dpe_reg_top.sv` (L1) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_reg_top.sv`
- `keymgr_dpe_reg_top` (L9) - `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_reg_top.sv`
- `keymgr_dpe` (L1905) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_base_test.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tests\keymgr_dpe_base_test.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_env_pkg` | `opentitan\hw\ip\keymgr_dpe\dv\tests\keymgr_dpe_test_pkg.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_test_pkg.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tests\keymgr_dpe_test_pkg.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_pkg` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_op_state_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_op_state_ctrl.sv` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_op_state_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_op_state_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_op_state_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_cov_bind.sv` | `opentitan\hw\ip\keymgr_dpe\dv\cov\keymgr_dpe_cov_bind.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_cov_bind` | `opentitan\hw\ip\keymgr_dpe\dv\cov\keymgr_dpe_cov_bind.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_bind.sv` | `opentitan\hw\ip\keymgr_dpe\dv\sva\keymgr_dpe_bind.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_bind` | `opentitan\hw\ip\keymgr_dpe\dv\sva\keymgr_dpe_bind.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_reg_pkg` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_reg_top.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_reg_pkg.sv` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_reg_pkg.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_reg_top.sv` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_reg_top.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_reg_top` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_reg_top.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_ctrl.sv` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_op_state_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_pkg.sv` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_pkg.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe.sv` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_reg_top` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_test_pkg` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_dpe_if` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_data_en_state` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_err` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe_ctrl.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `prim_sec_anchor_const` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_reseed_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_cfg_en` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_input_checks` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_kmac_if` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `keymgr_sideload_key_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `tb.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_component_matches_code` | `component:keymgr_dpe` | `tb` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `prim_sec_anchor_const` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `keymgr_reseed_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `keymgr_cfg_en` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `keymgr_input_checks` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `keymgr_kmac_if` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `keymgr_sideload_key_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `tb.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe.hjson` | `tb` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `prim_sec_anchor_const` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `keymgr_reseed_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `keymgr_cfg_en` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `keymgr_input_checks` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `keymgr_kmac_if` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `keymgr_sideload_key_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `prim_sec_anchor_const` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `keymgr_reseed_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `keymgr_cfg_en` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `keymgr_input_checks` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `keymgr_kmac_if` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `keymgr_sideload_key_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `keymgr_dpe_testplan.hjson` | `tb` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_sec_anchor_const` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `keymgr_reseed_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `keymgr_cfg_en` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `keymgr_input_checks` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `keymgr_kmac_if` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `keymgr_sideload_key_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_sec_anchor_const` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `keymgr_reseed_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `keymgr_cfg_en` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `keymgr_input_checks` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `keymgr_kmac_if` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `keymgr_sideload_key_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\keymgr_dpe\dv\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `prim_sec_anchor_const` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `keymgr_reseed_ctrl` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `keymgr_cfg_en` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `keymgr_input_checks` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `keymgr_kmac_if` | `opentitan\hw\ip\keymgr_dpe\rtl\keymgr_dpe.sv` |

## Retrieval Guidance

- When a code-only query mentions `keymgr_dpe`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
