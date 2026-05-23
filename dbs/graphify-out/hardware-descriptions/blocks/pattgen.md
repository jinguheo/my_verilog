# Hardware Description: pattgen

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `pattgen`
- `approved_label`: `pending:pattgen`
- `doc_anchor`: `pattgen`
- `module_name_prefix`: `pattgen`
- `bridge_edge_count`: 112

## Inferred Hardware Role

`pattgen` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 87, component: 41, testplan: 30, interface: 16, theory: 13
- Code categories: dv: 94, rtl: 29, other_code: 12, sva: 4
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Anchors

- `component:pattgen` (L1) - `__graphify_spec_only__/components.md`
- `pattgen.hjson` (L1) - `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `human name` (L7) - `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `one line desc` (L8) - `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `one paragraph desc` (L9) - `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `cip id` (L16) - `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `design spec` (L17) - `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `dv doc` (L18) - `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `hw checklist` (L19) - `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `sw checklist` (L20) - `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `revisions` (L21) - `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `version` (L23) - `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `pattgen_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/pattgen/data/pattgen_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/pattgen/data/pattgen_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/pattgen/data/pattgen_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/pattgen/data/pattgen_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/pattgen/data/pattgen_sec_cm_testplan.hjson`
- `pattgen_testplan.hjson` (L1) - `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `import testplans` (L7) - `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `testpoints` (L13) - `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `desc` (L16) - `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `Stimulus` (L20) - `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `Checking` (L26) - `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `stage` (L34) - `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `tests` (L35) - `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `covergroups` (L106) - `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/pattgen/doc/checklist.md`
- `Pattgen Checklist` (L1) - `opentitan/hw/ip/pattgen/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/pattgen/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/pattgen/doc/checklist.md`
- `D2` (L32) - `opentitan/hw/ip/pattgen/doc/checklist.md`
- `D2S` (L74) - `opentitan/hw/ip/pattgen/doc/checklist.md`
- `D3` (L94) - `opentitan/hw/ip/pattgen/doc/checklist.md`
- `Verification Checklist` (L120) - `opentitan/hw/ip/pattgen/doc/checklist.md`
- `V1` (L122) - `opentitan/hw/ip/pattgen/doc/checklist.md`

## Code Evidence

- `tb.sv` (L1) - `opentitan\hw\ip\pattgen\dv\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\pattgen\dv\tb.sv`
- `pattgen_env_pkg` (L10) - `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv`
- `pattgen_test_pkg` (L10) - `opentitan\hw\ip\pattgen\dv\tb.sv`
- `pattgen_agent_pkg` (L11) - `opentitan\hw\ip\pattgen\dv\tb.sv`
- `pattgen_if` (L30) - `opentitan\hw\ip\pattgen\dv\tb.sv`
- `pattgen_cov_bind.sv` (L1) - `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv`
- `pattgen_cov_bind` (L6) - `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv`
- `pattgen_cov_if.sv` (L1) - `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_if.sv`
- `pattgen_bind.sv` (L1) - `opentitan\hw\ip\pattgen\dv\sva\pattgen_bind.sv`
- `pattgen_bind` (L5) - `opentitan\hw\ip\pattgen\dv\sva\pattgen_bind.sv`
- `pattgen_base_test.sv` (L1) - `opentitan\hw\ip\pattgen\dv\tests\pattgen_base_test.sv`
- `pattgen_test_pkg.sv` (L1) - `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv`
- `pattgen.sv` (L1) - `opentitan\hw\ip\pattgen\rtl\pattgen.sv`
- `pattgen` (L7) - `opentitan\hw\ip\pattgen\rtl\pattgen.sv`
- `pattgen_reg_pkg` (L22) - `opentitan\hw\ip\pattgen\rtl\pattgen_reg_top.sv`
- `pattgen_core` (L78) - `opentitan\hw\ip\pattgen\rtl\pattgen.sv`
- `pattgen_chan.sv` (L1) - `opentitan\hw\ip\pattgen\rtl\pattgen_chan.sv`
- `pattgen_chan` (L5) - `opentitan\hw\ip\pattgen\rtl\pattgen_chan.sv`
- `pattgen_ctrl_pkg` (L9) - `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv`
- `pattgen_core.sv` (L1) - `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv`
- `pattgen_core` (L7) - `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv`
- `pattgen_chan` (L51) - `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv`
- `pattgen_ctrl_pkg.sv` (L1) - `opentitan\hw\ip\pattgen\rtl\pattgen_ctrl_pkg.sv`
- `pattgen_reg_pkg.sv` (L1) - `opentitan\hw\ip\pattgen\rtl\pattgen_reg_pkg.sv`
- `pattgen_reg_top.sv` (L1) - `opentitan\hw\ip\pattgen\rtl\pattgen_reg_top.sv`
- `pattgen_reg_top` (L9) - `opentitan\hw\ip\pattgen\rtl\pattgen_reg_top.sv`
- `pattgen` (L1444) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
- `pattgen_ios.rs` (L1) - `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
- `PattGenChannelParams` (L97) - `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
- `PattGenParams` (L187) - `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
- `pattgen_ios()` (L367) - `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
- `Opts` (L26) - `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
- `TestCmd` (L71) - `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
- `ChannelSymbols` (L79) - `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
- `Symbols` (L90) - `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
- `.from_rng()` (L109) - `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
- `.pattern_clock_edges()` (L140) - `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
- `.clock_period_ns()` (L180) - `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
- `.from_rng()` (L193) - `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:pattgen` | `pattgen_base_test.sv` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_base_test.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_env_pkg` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_test_pkg.sv` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_cov_bind.sv` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_cov_bind` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_cov_if.sv` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_if.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_ctrl_pkg.sv` | `opentitan\hw\ip\pattgen\rtl\pattgen_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_bind.sv` | `opentitan\hw\ip\pattgen\dv\sva\pattgen_bind.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_bind` | `opentitan\hw\ip\pattgen\dv\sva\pattgen_bind.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_reg_pkg` | `opentitan\hw\ip\pattgen\rtl\pattgen_reg_top.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_reg_pkg.sv` | `opentitan\hw\ip\pattgen\rtl\pattgen_reg_pkg.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_reg_top.sv` | `opentitan\hw\ip\pattgen\rtl\pattgen_reg_top.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_reg_top` | `opentitan\hw\ip\pattgen\rtl\pattgen_reg_top.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_chan.sv` | `opentitan\hw\ip\pattgen\rtl\pattgen_chan.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_chan` | `opentitan\hw\ip\pattgen\rtl\pattgen_chan.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_ctrl_pkg` | `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_core.sv` | `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_core` | `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_chan` | `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen.sv` | `opentitan\hw\ip\pattgen\rtl\pattgen.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen` | `opentitan\hw\ip\pattgen\rtl\pattgen.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_core` | `opentitan\hw\ip\pattgen\rtl\pattgen.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_test_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_agent_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_if` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_component_matches_code` | `component:pattgen` | `tb.sv` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_component_matches_code` | `component:pattgen` | `tb` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_ios.rs` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `PattGenChannelParams` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `PattGenParams` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_ios()` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `Opts` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `TestCmd` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `ChannelSymbols` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `Symbols` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `.from_rng()` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `.pattern_clock_edges()` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `.clock_period_ns()` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `.from_rng()` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `tb.sv` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `tb` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `pattgen_env_pkg` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `pattgen_test_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `pattgen_agent_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `pattgen_if` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `pattgen_cov_bind.sv` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `pattgen_cov_bind` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `pattgen_env_pkg` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `pattgen_test_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `pattgen_agent_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `pattgen_if` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `pattgen_cov_bind.sv` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `pattgen_cov_bind` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_path_matches_code_path` | `pattgen_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_testplan.hjson` | `tb` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_testplan.hjson` | `pattgen_env_pkg` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv` |
| `spec_path_matches_code_path` | `pattgen_testplan.hjson` | `pattgen_test_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_testplan.hjson` | `pattgen_agent_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_testplan.hjson` | `pattgen_if` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_testplan.hjson` | `pattgen_cov_bind.sv` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_path_matches_code_path` | `pattgen_testplan.hjson` | `pattgen_cov_bind` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `pattgen_env_pkg` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `pattgen_test_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `pattgen_agent_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `pattgen_if` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `pattgen_cov_bind.sv` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `pattgen_cov_bind` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `pattgen_env_pkg` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `pattgen_test_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `pattgen_agent_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `pattgen_if` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `pattgen_cov_bind.sv` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `pattgen_cov_bind` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |

## Retrieval Guidance

- When a code-only query mentions `pattgen`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
