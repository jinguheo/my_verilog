# Hardware Description: aon_timer

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `aon_timer`
- `approved_label`: `pending:aon_timer`
- `doc_anchor`: `aon_timer`
- `module_name_prefix`: `aon_timer`
- `bridge_edge_count`: 93

## Inferred Hardware Role

`aon_timer` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 90, testplan: 28, component: 22, interface: 15, theory: 12
- Code categories: dv: 66, sva: 22, rtl: 21, other_code: 2
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 21

## Spec Anchors

- `component:aon_timer` (L1) - `__graphify_spec_only__/components.md`
- `aon_timer.hjson` (L1) - `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `human name` (L7) - `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `one line desc` (L8) - `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `one paragraph desc` (L9) - `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `cip id` (L17) - `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `design spec` (L18) - `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `dv doc` (L19) - `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `hw checklist` (L20) - `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `sw checklist` (L21) - `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `version` (L22) - `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `life stage` (L23) - `opentitan/hw/ip/aon_timer/data/aon_timer.hjson`
- `aon_timer_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/aon_timer/data/aon_timer_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/aon_timer/data/aon_timer_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/aon_timer/data/aon_timer_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/aon_timer/data/aon_timer_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/aon_timer/data/aon_timer_sec_cm_testplan.hjson`
- `aon_timer_testplan.hjson` (L1) - `opentitan/hw/ip/aon_timer/data/aon_timer_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/aon_timer/data/aon_timer_testplan.hjson`
- `testpoints` (L13) - `opentitan/hw/ip/aon_timer/data/aon_timer_testplan.hjson`
- `desc` (L16) - `opentitan/hw/ip/aon_timer/data/aon_timer_testplan.hjson`
- `stage` (L31) - `opentitan/hw/ip/aon_timer/data/aon_timer_testplan.hjson`
- `tests` (L32) - `opentitan/hw/ip/aon_timer/data/aon_timer_testplan.hjson`
- `covergroups` (L135) - `opentitan/hw/ip/aon_timer/data/aon_timer_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `AON Timer Checklist` (L1) - `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `D2` (L32) - `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `D2S` (L74) - `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `D3` (L94) - `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `Verification Checklist` (L120) - `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `V1` (L122) - `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `V2` (L172) - `opentitan/hw/ip/aon_timer/doc/checklist.md`
- `V2S` (L218) - `opentitan/hw/ip/aon_timer/doc/checklist.md`

## Code Evidence

- `tb.sv` (L1) - `opentitan\hw\ip\aon_timer\dv\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\aon_timer\dv\tb.sv`
- `aon_timer_env_pkg` (L10) - `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv`
- `aon_timer_test_pkg` (L10) - `opentitan\hw\ip\aon_timer\dv\tb.sv`
- `aon_timer_bind.sv` (L1) - `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv`
- `aon_timer_bind` (L5) - `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv`
- `aon_timer_base_test.sv` (L1) - `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv`
- `aon_timer_test_pkg.sv` (L1) - `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv`
- `aon_timer.sv` (L1) - `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv`
- `aon_timer` (L10) - `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv`
- `aon_timer_reg_pkg` (L34) - `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_top.sv`
- `aon_timer_reg_top` (L101) - `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv`
- `aon_timer_core` (L164) - `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv`
- `aon_timer_core.sv` (L1) - `opentitan\hw\ip\aon_timer\rtl\aon_timer_core.sv`
- `aon_timer_core` (L7) - `opentitan\hw\ip\aon_timer\rtl\aon_timer_core.sv`
- `aon_timer_reg_pkg.sv` (L1) - `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_pkg.sv`
- `aon_timer_reg_top.sv` (L1) - `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_top.sv`
- `aon_timer_reg_top` (L9) - `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_top.sv`
- `aon_timer` (L1049) - `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
- `aon_timer.rs` (L1) - `opentitan\sw\host\ot_hal\src\dif\aon_timer.rs`
- `AonTimerReg` (L7) - `opentitan\sw\host\ot_hal\src\dif\aon_timer.rs`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_base_test.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_test_pkg.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_bind.sv` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_bind` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_reg_pkg` | `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_top.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_reg_pkg.sv` | `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_pkg.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_reg_top.sv` | `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_top.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_reg_top` | `opentitan\hw\ip\aon_timer\rtl\aon_timer_reg_top.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_core.sv` | `opentitan\hw\ip\aon_timer\rtl\aon_timer_core.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_core` | `opentitan\hw\ip\aon_timer\rtl\aon_timer_core.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer.sv` | `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer` | `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_reg_top` | `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_core` | `opentitan\hw\ip\aon_timer\rtl\aon_timer.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer_test_pkg` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_component_matches_code` | `component:aon_timer` | `aon_timer.rs` | `opentitan\sw\host\ot_hal\src\dif\aon_timer.rs` |
| `spec_component_matches_code` | `component:aon_timer` | `AonTimerReg` | `opentitan\sw\host\ot_hal\src\dif\aon_timer.rs` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `aon_timer_test_pkg` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `aon_timer_bind.sv` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `aon_timer_bind` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `aon_timer_base_test.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv` |
| `spec_path_matches_code_path` | `aon_timer.hjson` | `aon_timer_test_pkg.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `aon_timer_test_pkg` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `aon_timer_bind.sv` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `aon_timer_bind` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `aon_timer_base_test.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv` |
| `spec_path_matches_code_path` | `aon_timer_sec_cm_testplan.hjson` | `aon_timer_test_pkg.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `aon_timer_test_pkg` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `aon_timer_bind.sv` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `aon_timer_bind` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `aon_timer_base_test.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv` |
| `spec_path_matches_code_path` | `aon_timer_testplan.hjson` | `aon_timer_test_pkg.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aon_timer_test_pkg` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aon_timer_bind.sv` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aon_timer_bind` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aon_timer_base_test.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aon_timer_test_pkg.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aon_timer_test_pkg` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aon_timer_bind.sv` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aon_timer_bind` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aon_timer_base_test.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aon_timer_test_pkg.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `aon_timer_test_pkg` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `aon_timer_bind.sv` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `aon_timer_bind` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `aon_timer_base_test.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `aon_timer_test_pkg.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `registers.md` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `registers.md` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `registers.md` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `registers.md` | `aon_timer_test_pkg` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `registers.md` | `aon_timer_bind.sv` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `registers.md` | `aon_timer_bind` | `opentitan\hw\ip\aon_timer\dv\sva\aon_timer_bind.sv` |
| `spec_path_matches_code_path` | `registers.md` | `aon_timer_base_test.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_base_test.sv` |
| `spec_path_matches_code_path` | `registers.md` | `aon_timer_test_pkg.sv` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `tb.sv` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `tb` | `opentitan\hw\ip\aon_timer\dv\tb.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `aon_timer_env_pkg` | `opentitan\hw\ip\aon_timer\dv\tests\aon_timer_test_pkg.sv` |

## Retrieval Guidance

- When a code-only query mentions `aon_timer`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
