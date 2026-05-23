# Hardware Description: sram_ctrl

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `sram_ctrl`
- `approved_label`: `pending:sram_ctrl`
- `doc_anchor`: `sram_ctrl`
- `module_name_prefix`: `sram_ctrl`
- `bridge_edge_count`: 102

## Inferred Hardware Role

`sram_ctrl` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 79, component: 31, testplan: 28, interface: 19, theory: 18
- Code categories: dv: 61, rtl: 54, other_code: 12, sva: 4
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 30

## Spec Anchors

- `component:sram_ctrl` (L1) - `__graphify_spec_only__/components.md`
- `sram_ctrl.hjson` (L1) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `human name` (L6) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `one line desc` (L7) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `cip id` (L15) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `design spec` (L16) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `dv doc` (L17) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `hw checklist` (L18) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `sw checklist` (L19) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `version` (L20) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `life stage` (L21) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `sram_ctrl_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_sec_cm_testplan.hjson`
- `sram_ctrl_testplan.hjson` (L1) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_testplan.hjson`
- `testpoints` (L15) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_testplan.hjson`
- `desc` (L18) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_testplan.hjson`
- `covergroups` (L187) - `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `SRAM CTRL Checklist` (L1) - `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `D2` (L32) - `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `D2S` (L74) - `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `D3` (L94) - `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `Verification Checklist` (L120) - `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `V1` (L122) - `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `V2` (L172) - `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `V2S` (L218) - `opentitan/hw/ip/sram_ctrl/doc/checklist.md`

## Code Evidence

- `prim_ram_1p_scr` (L679) - `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv`
- `tlul_adapter_sram_racl` (L529) - `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\sram_ctrl\dv\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\sram_ctrl\dv\tb.sv`
- `sram_ctrl_pkg` (L11) - `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv`
- `sram_ctrl_env_pkg` (L9) - `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv`
- `sram_ctrl_test_pkg` (L11) - `opentitan\hw\ip\sram_ctrl\dv\tb.sv`
- `sram_ctrl_cov_bind.sv` (L1) - `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv`
- `sram_ctrl_cov_bind` (L6) - `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv`
- `sram_ctrl_bind.sv` (L1) - `opentitan\hw\ip\sram_ctrl\dv\sva\sram_ctrl_bind.sv`
- `sram_ctrl_bind` (L5) - `opentitan\hw\ip\sram_ctrl\dv\sva\sram_ctrl_bind.sv`
- `sram_ctrl_base_test.sv` (L1) - `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_base_test.sv`
- `sram_ctrl_test_pkg.sv` (L1) - `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv`
- `sram_ctrl.sv` (L1) - `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv`
- `sram_ctrl` (L10) - `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv`
- `sram_ctrl_reg_pkg` (L32) - `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_regs_reg_top.sv`
- `sram_ctrl_regs_reg_top` (L154) - `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv`
- `sram_ctrl_pkg.sv` (L1) - `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_pkg.sv`
- `sram_ctrl_ram_reg_top.sv` (L1) - `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_ram_reg_top.sv`
- `sram_ctrl_ram_reg_top` (L9) - `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_ram_reg_top.sv`
- `sram_ctrl_regs_reg_top.sv` (L1) - `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_regs_reg_top.sv`
- `sram_ctrl_regs_reg_top` (L9) - `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_regs_reg_top.sv`
- `sram_ctrl_reg_pkg.sv` (L1) - `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_reg_pkg.sv`
- `sram_ctrl_lc_escalation.rs` (L1) - `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs`
- `Opts` (L28) - `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs`
- `Addresses` (L46) - `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs`
- `main()` (L52) - `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs`
- `lc_escalation()` (L74) - `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs`
- `write_read()` (L136) - `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs`
- `sram_ctrl` (L1211) - `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_base_test.sv` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_env_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_test_pkg.sv` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_reg_pkg` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_regs_reg_top.sv` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_regs_reg_top` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_cov_bind.sv` | `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_cov_bind` | `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_ram_reg_top.sv` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_ram_reg_top.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_ram_reg_top` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_ram_reg_top.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_bind.sv` | `opentitan\hw\ip\sram_ctrl\dv\sva\sram_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_bind` | `opentitan\hw\ip\sram_ctrl\dv\sva\sram_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_reg_pkg.sv` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_pkg.sv` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_pkg` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl.sv` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_regs_reg_top` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_test_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `tb.sv` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `tb` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_lc_escalation.rs` | `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs` |
| `spec_component_matches_code` | `component:sram_ctrl` | `Opts` | `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs` |
| `spec_component_matches_code` | `component:sram_ctrl` | `Addresses` | `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs` |
| `spec_component_matches_code` | `component:sram_ctrl` | `main()` | `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs` |
| `spec_component_matches_code` | `component:sram_ctrl` | `lc_escalation()` | `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs` |
| `spec_component_matches_code` | `component:sram_ctrl` | `write_read()` | `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `tb.sv` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `tb` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `sram_ctrl_pkg` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `sram_ctrl_env_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `sram_ctrl_test_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `sram_ctrl_cov_bind.sv` | `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `sram_ctrl_pkg` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `sram_ctrl_env_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `sram_ctrl_test_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `sram_ctrl_cov_bind.sv` | `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `tb` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `sram_ctrl_pkg` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `sram_ctrl_env_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `sram_ctrl_test_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `sram_ctrl_cov_bind.sv` | `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sram_ctrl_pkg` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sram_ctrl_env_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sram_ctrl_test_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sram_ctrl_cov_bind.sv` | `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sram_ctrl_pkg` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sram_ctrl_env_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sram_ctrl_test_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sram_ctrl_cov_bind.sv` | `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `tb.sv` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `tb` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `sram_ctrl_pkg` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `sram_ctrl_env_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `sram_ctrl_test_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `sram_ctrl_cov_bind.sv` | `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `registers.md` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `registers.md` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |

## Retrieval Guidance

- When a code-only query mentions `sram_ctrl`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
