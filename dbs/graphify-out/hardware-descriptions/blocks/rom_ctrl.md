# Hardware Description: rom_ctrl

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `rom_ctrl`
- `approved_label`: `pending:rom_ctrl`
- `doc_anchor`: `rom_ctrl`
- `module_name_prefix`: `rom_ctrl`
- `bridge_edge_count`: 112

## Inferred Hardware Role

`rom_ctrl` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 77, component: 41, testplan: 28, interface: 16, theory: 16
- Code categories: dv: 79, rtl: 74, other_code: 60, sva: 4
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Anchors

- `component:rom_ctrl` (L1) - `__graphify_spec_only__/components.md`
- `rom_ctrl.hjson` (L1) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `human name` (L6) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `one line desc` (L7) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `cip id` (L15) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `design spec` (L16) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `dv doc` (L17) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `hw checklist` (L18) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `sw checklist` (L19) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `revisions` (L20) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `version` (L22) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson`
- `rom_ctrl_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_sec_cm_testplan.hjson`
- `stage` (L33) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_sec_cm_testplan.hjson`
- `tests` (L34) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_sec_cm_testplan.hjson`
- `rom_ctrl_testplan.hjson` (L1) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_testplan.hjson`
- `testpoints` (L15) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_testplan.hjson`
- `desc` (L18) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_testplan.hjson`
- `stage` (L37) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_testplan.hjson`
- `tests` (L38) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_testplan.hjson`
- `covergroups` (L81) - `opentitan/hw/ip/rom_ctrl/data/rom_ctrl_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `Rom Controller Checklist` (L1) - `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `D2` (L32) - `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `D2S` (L74) - `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `D3` (L94) - `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `Verification Checklist` (L120) - `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `V1` (L122) - `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `V2` (L172) - `opentitan/hw/ip/rom_ctrl/doc/checklist.md`
- `V2S` (L218) - `opentitan/hw/ip/rom_ctrl/doc/checklist.md`

## Code Evidence

- `prim_prince` (L108) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv`
- `prim_rom_pkg` (L25) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv`
- `kmac_app_intf` (L30) - `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv`
- `rom_ctrl_cov_bind.sv` (L1) - `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv`
- `rom_ctrl_cov_bind` (L6) - `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv`
- `rom_ctrl_cov_if.sv` (L1) - `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_if.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv`
- `tb` (L8) - `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv`
- `rom_ctrl_reg_pkg` (L20) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_rom_reg_top.sv`
- `rom_ctrl_bind.sv` (L1) - `opentitan\hw\ip\rom_ctrl\dv\sva\rom_ctrl_bind.sv`
- `rom_ctrl_bind` (L5) - `opentitan\hw\ip\rom_ctrl\dv\sva\rom_ctrl_bind.sv`
- `rom_ctrl_compare_if.sv` (L1) - `opentitan\hw\ip\rom_ctrl\dv\tb\rom_ctrl_compare_if.sv`
- `rom_ctrl_fsm_if.sv` (L1) - `opentitan\hw\ip\rom_ctrl\dv\tb\rom_ctrl_fsm_if.sv`
- `rom_ctrl_if.sv` (L1) - `opentitan\hw\ip\rom_ctrl\dv\tb\rom_ctrl_if.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv`
- `rom_ctrl_env_pkg` (L9) - `opentitan\hw\ip\rom_ctrl\dv\tests\rom_ctrl_test_pkg.sv`
- `rom_ctrl_test_pkg` (L10) - `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv`
- `rom_ctrl_base_test.sv` (L1) - `opentitan\hw\ip\rom_ctrl\dv\tests\rom_ctrl_base_test.sv`
- `rom_ctrl_test_pkg.sv` (L1) - `opentitan\hw\ip\rom_ctrl\dv\tests\rom_ctrl_test_pkg.sv`
- `rom_ctrl.sv` (L1) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv`
- `rom_ctrl` (L7) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv`
- `rom_ctrl_pkg` (L50) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv`
- `rom_ctrl_mux` (L235) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv`
- `rom_ctrl_regs_reg_top` (L332) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv`
- `rom_ctrl_compare.sv` (L1) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_compare.sv`
- `rom_ctrl_compare` (L14) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_compare.sv`
- `rom_ctrl_counter.sv` (L1) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_counter.sv`
- `rom_ctrl_counter` (L33) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_counter.sv`
- `rom_ctrl_fsm.sv` (L1) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv`
- `rom_ctrl_fsm` (L47) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv`
- `rom_ctrl_counter` (L113) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv`
- `rom_ctrl_compare` (L131) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv`
- `rom_ctrl_mux.sv` (L1) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_mux.sv`
- `rom_ctrl_mux` (L9) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_mux.sv`
- `rom_ctrl_pkg.sv` (L1) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_pkg.sv`
- `rom_ctrl_regs_reg_top.sv` (L1) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_regs_reg_top.sv`
- `rom_ctrl_regs_reg_top` (L9) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_regs_reg_top.sv`
- `rom_ctrl_reg_pkg.sv` (L1) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_reg_pkg.sv`
- `rom_ctrl_rom_reg_top.sv` (L1) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_rom_reg_top.sv`
- `rom_ctrl_rom_reg_top` (L9) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_rom_reg_top.sv`
- `rom_ctrl_scrambled_rom.sv` (L1) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv`
- `rom_ctrl_scrambled_rom` (L24) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv`
- `prim_subst_perm` (L94) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv`
- `prim_rom_adv` (L135) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_base_test.sv` | `opentitan\hw\ip\rom_ctrl\dv\tests\rom_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_env_pkg` | `opentitan\hw\ip\rom_ctrl\dv\tests\rom_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_test_pkg.sv` | `opentitan\hw\ip\rom_ctrl\dv\tests\rom_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_scrambled_rom.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_scrambled_rom` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_compare_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\tb\rom_ctrl_compare_if.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_regs_reg_top.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_regs_reg_top` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_cov_bind.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_cov_bind` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_reg_pkg` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_rom_reg_top.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_rom_reg_top.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_rom_reg_top.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_rom_reg_top` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_rom_reg_top.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_cov_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_if.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_fsm_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\tb\rom_ctrl_fsm_if.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_bind.sv` | `opentitan\hw\ip\rom_ctrl\dv\sva\rom_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_bind` | `opentitan\hw\ip\rom_ctrl\dv\sva\rom_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_compare.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_compare.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_compare` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_compare.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_counter.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_counter.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_counter` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_counter.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_reg_pkg.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\tb\rom_ctrl_if.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_pkg` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_fsm.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_fsm` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_counter` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_compare` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_mux.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_mux.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_mux` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_mux.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_pkg.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl.sv` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_mux` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_regs_reg_top` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `rom_ctrl_test_pkg` | `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `prim_prince` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `prim_rom_pkg` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_component_matches_code` | `component:rom_ctrl` | `prim_subst_perm` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `prim_prince` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `prim_rom_pkg` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `kmac_app_intf` | `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `rom_ctrl_cov_bind.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `rom_ctrl_cov_bind` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `rom_ctrl_cov_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_if.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `tb.sv` | `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl.hjson` | `tb` | `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `prim_prince` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `prim_rom_pkg` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `kmac_app_intf` | `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `rom_ctrl_cov_bind.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `rom_ctrl_cov_bind` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `rom_ctrl_cov_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_if.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_testplan.hjson` | `prim_prince` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_testplan.hjson` | `prim_rom_pkg` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_testplan.hjson` | `kmac_app_intf` | `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_testplan.hjson` | `rom_ctrl_cov_bind.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_testplan.hjson` | `rom_ctrl_cov_bind` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_testplan.hjson` | `rom_ctrl_cov_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_if.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv` |
| `spec_path_matches_code_path` | `rom_ctrl_testplan.hjson` | `tb` | `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_prince` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_rom_pkg` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `kmac_app_intf` | `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rom_ctrl_cov_bind.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rom_ctrl_cov_bind` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rom_ctrl_cov_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_prince` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_rom_pkg` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `kmac_app_intf` | `opentitan\hw\ip\rom_ctrl\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rom_ctrl_cov_bind.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rom_ctrl_cov_bind` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rom_ctrl_cov_if.sv` | `opentitan\hw\ip\rom_ctrl\dv\cov\rom_ctrl_cov_if.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\rom_ctrl\dv\formal\tb.sv` |

## Retrieval Guidance

- When a code-only query mentions `rom_ctrl`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
