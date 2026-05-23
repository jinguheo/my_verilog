# Hardware Description: rv_dm

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `rv_dm`
- `approved_label`: `pending:rv_dm`
- `doc_anchor`: `rv_dm`
- `module_name_prefix`: `rv_dm`
- `bridge_edge_count`: 112

## Inferred Hardware Role

`rv_dm` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 79, component: 41, testplan: 29, interface: 21, theory: 15
- Code categories: dv: 59, other_code: 53, rtl: 50, sva: 26
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Anchors

- `component:rv_dm` (L1) - `__graphify_spec_only__/components.md`
- `rv_dm.hjson` (L1) - `opentitan/hw/ip/rv_dm/data/rv_dm.hjson`
- `human name` (L6) - `opentitan/hw/ip/rv_dm/data/rv_dm.hjson`
- `one line desc` (L7) - `opentitan/hw/ip/rv_dm/data/rv_dm.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/ip/rv_dm/data/rv_dm.hjson`
- `cip id` (L14) - `opentitan/hw/ip/rv_dm/data/rv_dm.hjson`
- `design spec` (L15) - `opentitan/hw/ip/rv_dm/data/rv_dm.hjson`
- `dv doc` (L16) - `opentitan/hw/ip/rv_dm/data/rv_dm.hjson`
- `hw checklist` (L17) - `opentitan/hw/ip/rv_dm/data/rv_dm.hjson`
- `sw checklist` (L18) - `opentitan/hw/ip/rv_dm/data/rv_dm.hjson`
- `version` (L19) - `opentitan/hw/ip/rv_dm/data/rv_dm.hjson`
- `life stage` (L20) - `opentitan/hw/ip/rv_dm/data/rv_dm.hjson`
- `rv_dm_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/rv_dm/data/rv_dm_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/rv_dm/data/rv_dm_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/rv_dm/data/rv_dm_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/rv_dm/data/rv_dm_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/rv_dm/data/rv_dm_sec_cm_testplan.hjson`
- `rv_dm_testplan.hjson` (L1) - `opentitan/hw/ip/rv_dm/data/rv_dm_testplan.hjson`
- `import testplans` (L7) - `opentitan/hw/ip/rv_dm/data/rv_dm_testplan.hjson`
- `testpoints` (L13) - `opentitan/hw/ip/rv_dm/data/rv_dm_testplan.hjson`
- `desc` (L18) - `opentitan/hw/ip/rv_dm/data/rv_dm_testplan.hjson`
- `stage` (L32) - `opentitan/hw/ip/rv_dm/data/rv_dm_testplan.hjson`
- `tests` (L33) - `opentitan/hw/ip/rv_dm/data/rv_dm_testplan.hjson`
- `ways` (L227) - `opentitan/hw/ip/rv_dm/data/rv_dm_testplan.hjson`
- `covergroups` (L557) - `opentitan/hw/ip/rv_dm/data/rv_dm_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/rv_dm/doc/checklist.md`
- `RV DM Checklist` (L1) - `opentitan/hw/ip/rv_dm/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/rv_dm/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/rv_dm/doc/checklist.md`
- `D2` (L32) - `opentitan/hw/ip/rv_dm/doc/checklist.md`
- `D2S` (L75) - `opentitan/hw/ip/rv_dm/doc/checklist.md`
- `D3` (L95) - `opentitan/hw/ip/rv_dm/doc/checklist.md`
- `Verification Checklist` (L121) - `opentitan/hw/ip/rv_dm/doc/checklist.md`
- `V1` (L123) - `opentitan/hw/ip/rv_dm/doc/checklist.md`
- `V2` (L173) - `opentitan/hw/ip/rv_dm/doc/checklist.md`

## Code Evidence

- `prim_mubi8_sync` (L232) - `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\rv_dm\dv\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\rv_dm\dv\tb.sv`
- `rv_dm_env_pkg` (L9) - `opentitan\hw\ip\rv_dm\dv\tests\rv_dm_test_pkg.sv`
- `rv_dm_test_pkg` (L10) - `opentitan\hw\ip\rv_dm\dv\tb.sv`
- `rv_dm_if` (L29) - `opentitan\hw\ip\rv_dm\dv\tb.sv`
- `rv_dm_bind.sv` (L1) - `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_bind.sv`
- `rv_dm_bind` (L5) - `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_bind.sv`
- `rv_dm_enable_checker.sv` (L1) - `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_enable_checker.sv`
- `rv_dm_enable_checker` (L5) - `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_enable_checker.sv`
- `rv_dm_reg_pkg` (L31) - `opentitan\hw\ip\rv_dm\rtl\rv_dm_regs_reg_top.sv`
- `rv_dm_base_test.sv` (L1) - `opentitan\hw\ip\rv_dm\dv\tests\rv_dm_base_test.sv`
- `rv_dm_test_pkg.sv` (L1) - `opentitan\hw\ip\rv_dm\dv\tests\rv_dm_test_pkg.sv`
- `jtag_pkg.sv` (L1) - `opentitan\hw\ip\rv_dm\rtl\jtag_pkg.sv`
- `rv_dm.sv` (L1) - `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv`
- `rv_dm` (L15) - `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv`
- `rv_dm_regs_reg_top` (L133) - `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv`
- `prim_mubi32_sync` (L242) - `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv`
- `rv_dm_dbg_reg_top` (L493) - `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv`
- `rv_dm_dmi_gate` (L503) - `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv`
- `rv_dm_dbg_reg_top.sv` (L1) - `opentitan\hw\ip\rv_dm\rtl\rv_dm_dbg_reg_top.sv`
- `rv_dm_dbg_reg_top` (L9) - `opentitan\hw\ip\rv_dm\rtl\rv_dm_dbg_reg_top.sv`
- `rv_dm_dmi_gate.sv` (L1) - `opentitan\hw\ip\rv_dm\rtl\rv_dm_dmi_gate.sv`
- `rv_dm_dmi_gate` (L13) - `opentitan\hw\ip\rv_dm\rtl\rv_dm_dmi_gate.sv`
- `tlul_adapter_dmi` (L250) - `opentitan\hw\ip\rv_dm\rtl\rv_dm_dmi_gate.sv`
- `rv_dm_mem_reg_top.sv` (L1) - `opentitan\hw\ip\rv_dm\rtl\rv_dm_mem_reg_top.sv`
- `rv_dm_mem_reg_top` (L9) - `opentitan\hw\ip\rv_dm\rtl\rv_dm_mem_reg_top.sv`
- `rv_dm_pkg.sv` (L1) - `opentitan\hw\ip\rv_dm\rtl\rv_dm_pkg.sv`
- `rv_dm_regs_reg_top.sv` (L1) - `opentitan\hw\ip\rv_dm\rtl\rv_dm_regs_reg_top.sv`
- `rv_dm_regs_reg_top` (L9) - `opentitan\hw\ip\rv_dm\rtl\rv_dm_regs_reg_top.sv`
- `rv_dm_reg_pkg.sv` (L1) - `opentitan\hw\ip\rv_dm\rtl\rv_dm_reg_pkg.sv`
- `access_after_hw_reset.rs` (L1) - `opentitan\sw\host\tests\chip\rv_dm\src\access_after_hw_reset.rs`
- `Opts` (L20) - `opentitan\sw\host\tests\chip\rv_dm\src\access_after_hw_reset.rs`
- `test_access_after_hw_reset()` (L33) - `opentitan\sw\host\tests\chip\rv_dm\src\access_after_hw_reset.rs`
- `main()` (L79) - `opentitan\sw\host\tests\chip\rv_dm\src\access_after_hw_reset.rs`
- `access_after_wakeup.rs` (L1) - `opentitan\sw\host\tests\chip\rv_dm\src\access_after_wakeup.rs`
- `Opts` (L21) - `opentitan\sw\host\tests\chip\rv_dm\src\access_after_wakeup.rs`
- `test_access_after_wakeup()` (L34) - `opentitan\sw\host\tests\chip\rv_dm\src\access_after_wakeup.rs`
- `main()` (L149) - `opentitan\sw\host\tests\chip\rv_dm\src\access_after_wakeup.rs`
- `control_status.rs` (L1) - `opentitan\sw\host\tests\chip\rv_dm\src\control_status.rs`
- `Opts` (L14) - `opentitan\sw\host\tests\chip\rv_dm\src\control_status.rs`
- `test_control_status()` (L22) - `opentitan\sw\host\tests\chip\rv_dm\src\control_status.rs`
- `main()` (L63) - `opentitan\sw\host\tests\chip\rv_dm\src\control_status.rs`
- `csr_rw.rs` (L1) - `opentitan\sw\host\tests\chip\rv_dm\src\csr_rw.rs`
- `Opts` (L21) - `opentitan\sw\host\tests\chip\rv_dm\src\csr_rw.rs`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_enable_checker.sv` | `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_enable_checker.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_enable_checker` | `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_enable_checker.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_base_test.sv` | `opentitan\hw\ip\rv_dm\dv\tests\rv_dm_base_test.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_env_pkg` | `opentitan\hw\ip\rv_dm\dv\tests\rv_dm_test_pkg.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_test_pkg.sv` | `opentitan\hw\ip\rv_dm\dv\tests\rv_dm_test_pkg.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_reg_pkg` | `opentitan\hw\ip\rv_dm\rtl\rv_dm_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_regs_reg_top.sv` | `opentitan\hw\ip\rv_dm\rtl\rv_dm_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_regs_reg_top` | `opentitan\hw\ip\rv_dm\rtl\rv_dm_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_dbg_reg_top.sv` | `opentitan\hw\ip\rv_dm\rtl\rv_dm_dbg_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_dbg_reg_top` | `opentitan\hw\ip\rv_dm\rtl\rv_dm_dbg_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_mem_reg_top.sv` | `opentitan\hw\ip\rv_dm\rtl\rv_dm_mem_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_mem_reg_top` | `opentitan\hw\ip\rv_dm\rtl\rv_dm_mem_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_dmi_gate.sv` | `opentitan\hw\ip\rv_dm\rtl\rv_dm_dmi_gate.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_dmi_gate` | `opentitan\hw\ip\rv_dm\rtl\rv_dm_dmi_gate.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_bind.sv` | `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_bind.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_bind` | `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_bind.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_reg_pkg.sv` | `opentitan\hw\ip\rv_dm\rtl\rv_dm_reg_pkg.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_pkg.sv` | `opentitan\hw\ip\rv_dm\rtl\rv_dm_pkg.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm.sv` | `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm` | `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_regs_reg_top` | `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_dbg_reg_top` | `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_dmi_gate` | `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_test_pkg` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `rv_dm_if` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `tlul_adapter_dmi` | `opentitan\hw\ip\rv_dm\rtl\rv_dm_dmi_gate.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `jtag_pkg.sv` | `opentitan\hw\ip\rv_dm\rtl\jtag_pkg.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `prim_mubi8_sync` | `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `prim_mubi32_sync` | `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `tb.sv` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `tb` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_component_matches_code` | `component:rv_dm` | `ndm_reset_req_when_cpu_halted.rs` | `opentitan\sw\host\tests\chip\rv_dm\src\ndm_reset_req_when_cpu_halted.rs` |
| `spec_component_matches_code` | `component:rv_dm` | `Opts` | `opentitan\sw\host\tests\chip\rv_dm\src\ndm_reset_req_when_cpu_halted.rs` |
| `spec_component_matches_code` | `component:rv_dm` | `test_ndm_reset_req_when_halted()` | `opentitan\sw\host\tests\chip\rv_dm\src\ndm_reset_req_when_cpu_halted.rs` |
| `spec_component_matches_code` | `component:rv_dm` | `main()` | `opentitan\sw\host\tests\chip\rv_dm\src\ndm_reset_req_when_cpu_halted.rs` |
| `spec_component_matches_code` | `component:rv_dm` | `access_after_hw_reset.rs` | `opentitan\sw\host\tests\chip\rv_dm\src\access_after_hw_reset.rs` |
| `spec_component_matches_code` | `component:rv_dm` | `Opts` | `opentitan\sw\host\tests\chip\rv_dm\src\access_after_hw_reset.rs` |
| `spec_component_matches_code` | `component:rv_dm` | `test_access_after_hw_reset()` | `opentitan\sw\host\tests\chip\rv_dm\src\access_after_hw_reset.rs` |
| `spec_component_matches_code` | `component:rv_dm` | `main()` | `opentitan\sw\host\tests\chip\rv_dm\src\access_after_hw_reset.rs` |
| `spec_path_matches_code_path` | `rv_dm.hjson` | `prim_mubi8_sync` | `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv` |
| `spec_path_matches_code_path` | `rv_dm.hjson` | `tb.sv` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `rv_dm.hjson` | `tb` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `rv_dm.hjson` | `rv_dm_env_pkg` | `opentitan\hw\ip\rv_dm\dv\tests\rv_dm_test_pkg.sv` |
| `spec_path_matches_code_path` | `rv_dm.hjson` | `rv_dm_test_pkg` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `rv_dm.hjson` | `rv_dm_if` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `rv_dm.hjson` | `rv_dm_bind.sv` | `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_bind.sv` |
| `spec_path_matches_code_path` | `rv_dm.hjson` | `rv_dm_bind` | `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_bind.sv` |
| `spec_path_matches_code_path` | `rv_dm_sec_cm_testplan.hjson` | `prim_mubi8_sync` | `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv` |
| `spec_path_matches_code_path` | `rv_dm_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `rv_dm_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `rv_dm_sec_cm_testplan.hjson` | `rv_dm_env_pkg` | `opentitan\hw\ip\rv_dm\dv\tests\rv_dm_test_pkg.sv` |
| `spec_path_matches_code_path` | `rv_dm_sec_cm_testplan.hjson` | `rv_dm_test_pkg` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `rv_dm_sec_cm_testplan.hjson` | `rv_dm_if` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `rv_dm_sec_cm_testplan.hjson` | `rv_dm_bind.sv` | `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_bind.sv` |
| `spec_path_matches_code_path` | `rv_dm_sec_cm_testplan.hjson` | `rv_dm_bind` | `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_bind.sv` |
| `spec_path_matches_code_path` | `rv_dm_testplan.hjson` | `prim_mubi8_sync` | `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv` |
| `spec_path_matches_code_path` | `rv_dm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `rv_dm_testplan.hjson` | `tb` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `rv_dm_testplan.hjson` | `rv_dm_env_pkg` | `opentitan\hw\ip\rv_dm\dv\tests\rv_dm_test_pkg.sv` |
| `spec_path_matches_code_path` | `rv_dm_testplan.hjson` | `rv_dm_test_pkg` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `rv_dm_testplan.hjson` | `rv_dm_if` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `rv_dm_testplan.hjson` | `rv_dm_bind.sv` | `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_bind.sv` |
| `spec_path_matches_code_path` | `rv_dm_testplan.hjson` | `rv_dm_bind` | `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_mubi8_sync` | `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_dm_env_pkg` | `opentitan\hw\ip\rv_dm\dv\tests\rv_dm_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_dm_test_pkg` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_dm_if` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_dm_bind.sv` | `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_dm_bind` | `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_mubi8_sync` | `opentitan\hw\ip\rv_dm\rtl\rv_dm.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rv_dm_env_pkg` | `opentitan\hw\ip\rv_dm\dv\tests\rv_dm_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rv_dm_test_pkg` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rv_dm_if` | `opentitan\hw\ip\rv_dm\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rv_dm_bind.sv` | `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rv_dm_bind` | `opentitan\hw\ip\rv_dm\dv\sva\rv_dm_bind.sv` |

## Retrieval Guidance

- When a code-only query mentions `rv_dm`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
