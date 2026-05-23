# Hardware Description: sysrst_ctrl

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `sysrst_ctrl`
- `approved_label`: `pending:sysrst_ctrl`
- `doc_anchor`: `sysrst_ctrl`
- `module_name_prefix`: `sysrst_ctrl`
- `bridge_edge_count`: 104

## Inferred Hardware Role

`sysrst_ctrl` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 71, component: 41, testplan: 28, theory: 19, interface: 15
- Code categories: dv: 80, rtl: 63, other_code: 51, sva: 4
- Bridge relations: spec_path_matches_code_path: 64, spec_component_matches_code: 40

## Spec Anchors

- `component:sysrst_ctrl` (L1) - `__graphify_spec_only__/components.md`
- `sysrst_ctrl.hjson` (L1) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `human name` (L6) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `one line desc` (L7) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `cip id` (L14) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `design spec` (L15) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `dv doc` (L16) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `hw checklist` (L17) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `sw checklist` (L18) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `version` (L19) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `life stage` (L20) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson`
- `sysrst_ctrl_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_sec_cm_testplan.hjson`
- `sysrst_ctrl_testplan.hjson` (L1) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_testplan.hjson`
- `testpoints` (L12) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_testplan.hjson`
- `desc` (L15) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_testplan.hjson`
- `stage` (L21) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_testplan.hjson`
- `tests` (L22) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_testplan.hjson`
- `covergroups` (L235) - `opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `SYSRST CTRL Checklist` (L1) - `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `D2` (L32) - `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `D2S` (L74) - `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `D3` (L94) - `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `Verification Checklist` (L120) - `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `V1` (L122) - `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `V2` (L172) - `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`
- `V2S` (L219) - `opentitan/hw/ip/sysrst_ctrl/doc/checklist.md`

## Code Evidence

- `tb.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv`
- `sysrst_ctrl_env_pkg` (L9) - `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv`
- `sysrst_ctrl_test_pkg` (L10) - `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv`
- `sysrst_ctrl_if` (L36) - `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv`
- `sysrst_ctrl_cov_bind.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv`
- `sysrst_ctrl_cov_bind` (L6) - `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv`
- `sysrst_ctrl_cov_if.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_if.sv`
- `sysrst_ctrl_pkg` (L8) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv`
- `sysrst_ctrl_bind.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\dv\sva\sysrst_ctrl_bind.sv`
- `sysrst_ctrl_bind` (L5) - `opentitan\hw\ip\sysrst_ctrl\dv\sva\sysrst_ctrl_bind.sv`
- `sysrst_ctrl_base_test.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_base_test.sv`
- `sysrst_ctrl_test_pkg.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv`
- `sysrst_ctrl.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
- `sysrst_ctrl` (L9) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
- `sysrst_ctrl_reg_pkg` (L9) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv`
- `sysrst_ctrl_autoblock` (L154) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
- `sysrst_ctrl_ulp` (L182) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
- `sysrst_ctrl_keyintr` (L206) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
- `sysrst_ctrl_combo` (L233) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
- `sysrst_ctrl_pin` (L266) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
- `sysrst_ctrl_intr` (L330) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv`
- `sysrst_ctrl_autoblock.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_autoblock.sv`
- `sysrst_ctrl_autoblock` (L7) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_autoblock.sv`
- `sysrst_ctrl_detect` (L28) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv`
- `sysrst_ctrl_combo.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_combo.sv`
- `sysrst_ctrl_combo` (L7) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_combo.sv`
- `sysrst_ctrl_comboact.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_comboact.sv`
- `sysrst_ctrl_comboact` (L7) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_comboact.sv`
- `sysrst_ctrl_detect.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_detect.sv`
- `sysrst_ctrl_detect` (L24) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_detect.sv`
- `sysrst_ctrl_intr.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_intr.sv`
- `sysrst_ctrl_intr` (L7) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_intr.sv`
- `sysrst_ctrl_keyintr.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_keyintr.sv`
- `sysrst_ctrl_keyintr` (L7) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_keyintr.sv`
- `sysrst_ctrl_pin.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_pin.sv`
- `sysrst_ctrl_pin` (L8) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_pin.sv`
- `sysrst_ctrl_pkg.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_pkg.sv`
- `sysrst_ctrl_reg_pkg.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_reg_pkg.sv`
- `sysrst_ctrl_reg_top.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_reg_top.sv`
- `sysrst_ctrl_reg_top` (L9) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_reg_top.sv`
- `sysrst_ctrl_ulp.sv` (L1) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv`
- `sysrst_ctrl_ulp` (L7) - `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv`
- `mod.rs` (L1) - `opentitan\sw\host\tests\chip\sysrst_ctrl\mod.rs`
- `sysrst_ctrl.rs` (L1) - `opentitan\sw\host\tests\chip\sysrst_ctrl\sysrst_ctrl.rs`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_base_test.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_env_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_test_pkg.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_cov_bind.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_cov_bind` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_cov_if.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_if.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_autoblock.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_autoblock.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_autoblock` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_autoblock.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_comboact.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_comboact.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_comboact` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_comboact.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_bind.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\sva\sysrst_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_bind` | `opentitan\hw\ip\sysrst_ctrl\dv\sva\sysrst_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_keyintr.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_keyintr.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_keyintr` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_keyintr.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_reg_pkg.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_reg_top.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_reg_top` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_detect.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_detect.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_detect` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_detect.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_combo.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_combo.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_combo` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_combo.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_intr.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_intr.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_intr` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_intr.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_pkg` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_reg_pkg` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_detect` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_pin.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_pin.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_pin` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_pin.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_pkg.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_ulp.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_ulp` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl_ulp.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl.sv` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_autoblock` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_ulp` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_keyintr` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_combo` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_pin` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_component_matches_code` | `component:sysrst_ctrl` | `sysrst_ctrl_intr` | `opentitan\hw\ip\sysrst_ctrl\rtl\sysrst_ctrl.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `tb.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `tb` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `sysrst_ctrl_env_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `sysrst_ctrl_test_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `sysrst_ctrl_if` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `sysrst_ctrl_cov_bind.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `sysrst_ctrl_cov_bind` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl.hjson` | `sysrst_ctrl_cov_if.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_if.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `sysrst_ctrl_env_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `sysrst_ctrl_test_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `sysrst_ctrl_if` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `sysrst_ctrl_cov_bind.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `sysrst_ctrl_cov_bind` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_sec_cm_testplan.hjson` | `sysrst_ctrl_cov_if.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_if.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_testplan.hjson` | `tb` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_testplan.hjson` | `sysrst_ctrl_env_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_testplan.hjson` | `sysrst_ctrl_test_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_testplan.hjson` | `sysrst_ctrl_if` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_testplan.hjson` | `sysrst_ctrl_cov_bind.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_testplan.hjson` | `sysrst_ctrl_cov_bind` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `sysrst_ctrl_testplan.hjson` | `sysrst_ctrl_cov_if.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sysrst_ctrl_env_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sysrst_ctrl_test_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sysrst_ctrl_if` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sysrst_ctrl_cov_bind.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sysrst_ctrl_cov_bind` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sysrst_ctrl_cov_if.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_if.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sysrst_ctrl_env_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tests\sysrst_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sysrst_ctrl_test_pkg` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sysrst_ctrl_if` | `opentitan\hw\ip\sysrst_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sysrst_ctrl_cov_bind.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sysrst_ctrl_cov_bind` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sysrst_ctrl_cov_if.sv` | `opentitan\hw\ip\sysrst_ctrl\dv\cov\sysrst_ctrl_cov_if.sv` |

## Retrieval Guidance

- When a code-only query mentions `sysrst_ctrl`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
