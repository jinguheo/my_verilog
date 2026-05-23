# Hardware Description: rv_timer

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `rv_timer`
- `approved_label`: `pending:rv_timer`
- `doc_anchor`: `rv_timer`
- `module_name_prefix`: `rv_timer`
- `bridge_edge_count`: 98

## Inferred Hardware Role

`rv_timer` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 87, component: 27, testplan: 27, interface: 15, theory: 14
- Code categories: dv: 70, sva: 30, rtl: 19, other_code: 4
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 26

## Spec Anchors

- `component:rv_timer` (L1) - `__graphify_spec_only__/components.md`
- `rv_timer.hjson` (L1) - `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `human name` (L7) - `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `one line desc` (L8) - `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `one paragraph desc` (L9) - `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `cip id` (L14) - `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `design spec` (L15) - `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `dv doc` (L16) - `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `hw checklist` (L17) - `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `sw checklist` (L18) - `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `revisions` (L19) - `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `version` (L21) - `opentitan/hw/ip/rv_timer/data/rv_timer.hjson`
- `rv_timer_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/rv_timer/data/rv_timer_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/rv_timer/data/rv_timer_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/rv_timer/data/rv_timer_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/rv_timer/data/rv_timer_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/rv_timer/data/rv_timer_sec_cm_testplan.hjson`
- `rv_timer_testplan.hjson` (L1) - `opentitan/hw/ip/rv_timer/data/rv_timer_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/rv_timer/data/rv_timer_testplan.hjson`
- `testpoints` (L12) - `opentitan/hw/ip/rv_timer/data/rv_timer_testplan.hjson`
- `desc` (L15) - `opentitan/hw/ip/rv_timer/data/rv_timer_testplan.hjson`
- `stage` (L21) - `opentitan/hw/ip/rv_timer/data/rv_timer_testplan.hjson`
- `tests` (L22) - `opentitan/hw/ip/rv_timer/data/rv_timer_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `RV TIMER Checklist` (L1) - `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `Design Checklist` (L7) - `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `D1` (L9) - `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `D2` (L35) - `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `D2S` (L79) - `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `D3` (L99) - `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `Verification Checklist` (L127) - `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `V1` (L129) - `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `V2` (L179) - `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `V2S` (L227) - `opentitan/hw/ip/rv_timer/doc/checklist.md`
- `interfaces.md` (L1) - `opentitan/hw/ip/rv_timer/doc/interfaces.md`

## Code Evidence

- `rv_timer_bind.sv` (L1) - `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv`
- `rv_timer_bind` (L5) - `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\rv_timer\dv\tb\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\rv_timer\dv\tb\tb.sv`
- `rv_timer_env_pkg` (L9) - `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv`
- `rv_timer_test_pkg` (L11) - `opentitan\hw\ip\rv_timer\dv\tb\tb.sv`
- `rv_timer_base_test.sv` (L1) - `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_base_test.sv`
- `rv_timer_test_pkg.sv` (L1) - `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv`
- `rv_timer_bind_fpv.sv` (L1) - `opentitan\hw\ip\rv_timer\fpv\tb\rv_timer_bind_fpv.sv`
- `rv_timer_bind_fpv` (L9) - `opentitan\hw\ip\rv_timer\fpv\tb\rv_timer_bind_fpv.sv`
- `rv_timer_core_assert_fpv.sv` (L1) - `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_core_assert_fpv.sv`
- `rv_timer_core_assert_fpv` (L8) - `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_core_assert_fpv.sv`
- `rv_timer_interrupts_assert_fpv.sv` (L1) - `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_interrupts_assert_fpv.sv`
- `rv_timer_interrupts_assert_fpv` (L8) - `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_interrupts_assert_fpv.sv`
- `rv_timer.sv` (L1) - `opentitan\hw\ip\rv_timer\rtl\rv_timer.sv`
- `rv_timer` (L9) - `opentitan\hw\ip\rv_timer\rtl\rv_timer.sv`
- `rv_timer_reg_pkg` (L32) - `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_top.sv`
- `rv_timer_reg_top` (L126) - `opentitan\hw\ip\rv_timer\rtl\rv_timer.sv`
- `rv_timer_reg_pkg.sv` (L1) - `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_pkg.sv`
- `rv_timer_reg_top.sv` (L1) - `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_top.sv`
- `rv_timer_reg_top` (L9) - `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_top.sv`
- `timer_core.sv` (L1) - `opentitan\hw\ip\rv_timer\rtl\timer_core.sv`
- `timer_core` (L7) - `opentitan\hw\ip\rv_timer\rtl\timer_core.sv`
- `reg_timer.py` (L1) - `opentitan\hw\ip\rv_timer\util\reg_timer.py`
- `main()` (L14) - `opentitan\hw\ip\rv_timer\util\reg_timer.py`
- `rv_timer` (L750) - `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_interrupts_assert_fpv.sv` | `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_interrupts_assert_fpv.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_interrupts_assert_fpv` | `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_interrupts_assert_fpv.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_core_assert_fpv.sv` | `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_core_assert_fpv.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_core_assert_fpv` | `opentitan\hw\ip\rv_timer\fpv\vip\rv_timer_core_assert_fpv.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_base_test.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_base_test.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_env_pkg` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_test_pkg.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_bind_fpv.sv` | `opentitan\hw\ip\rv_timer\fpv\tb\rv_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_bind_fpv` | `opentitan\hw\ip\rv_timer\fpv\tb\rv_timer_bind_fpv.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_bind.sv` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_bind` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_reg_pkg` | `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_reg_pkg.sv` | `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_pkg.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_reg_top.sv` | `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_reg_top` | `opentitan\hw\ip\rv_timer\rtl\rv_timer_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer.sv` | `opentitan\hw\ip\rv_timer\rtl\rv_timer.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer` | `opentitan\hw\ip\rv_timer\rtl\rv_timer.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_reg_top` | `opentitan\hw\ip\rv_timer\rtl\rv_timer.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `rv_timer_test_pkg` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `timer_core.sv` | `opentitan\hw\ip\rv_timer\rtl\timer_core.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `timer_core` | `opentitan\hw\ip\rv_timer\rtl\timer_core.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `tb.sv` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `tb` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:rv_timer` | `reg_timer.py` | `opentitan\hw\ip\rv_timer\util\reg_timer.py` |
| `spec_component_matches_code` | `component:rv_timer` | `main()` | `opentitan\hw\ip\rv_timer\util\reg_timer.py` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `rv_timer_bind.sv` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `rv_timer_bind` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `tb.sv` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `tb` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `rv_timer_env_pkg` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `rv_timer_test_pkg` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `rv_timer_base_test.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_base_test.sv` |
| `spec_path_matches_code_path` | `rv_timer.hjson` | `rv_timer_test_pkg.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `rv_timer_bind.sv` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `rv_timer_bind` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `rv_timer_env_pkg` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `rv_timer_test_pkg` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `rv_timer_base_test.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_base_test.sv` |
| `spec_path_matches_code_path` | `rv_timer_sec_cm_testplan.hjson` | `rv_timer_test_pkg.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `rv_timer_bind.sv` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `rv_timer_bind` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `tb` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `rv_timer_env_pkg` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `rv_timer_test_pkg` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `rv_timer_base_test.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_base_test.sv` |
| `spec_path_matches_code_path` | `rv_timer_testplan.hjson` | `rv_timer_test_pkg.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_timer_bind.sv` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_timer_bind` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_timer_env_pkg` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_timer_test_pkg` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_timer_base_test.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_base_test.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `rv_timer_test_pkg.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rv_timer_bind.sv` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rv_timer_bind` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rv_timer_env_pkg` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rv_timer_test_pkg` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rv_timer_base_test.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_base_test.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `rv_timer_test_pkg.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `rv_timer_bind.sv` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `rv_timer_bind` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `tb.sv` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `tb` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `rv_timer_env_pkg` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `rv_timer_test_pkg` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `rv_timer_base_test.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_base_test.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `rv_timer_test_pkg.sv` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `registers.md` | `rv_timer_bind.sv` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `registers.md` | `rv_timer_bind` | `opentitan\hw\ip\rv_timer\dv\sva\rv_timer_bind.sv` |
| `spec_path_matches_code_path` | `registers.md` | `tb.sv` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `registers.md` | `tb` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `registers.md` | `rv_timer_env_pkg` | `opentitan\hw\ip\rv_timer\dv\tests\rv_timer_test_pkg.sv` |
| `spec_path_matches_code_path` | `registers.md` | `rv_timer_test_pkg` | `opentitan\hw\ip\rv_timer\dv\tb\tb.sv` |

## Retrieval Guidance

- When a code-only query mentions `rv_timer`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
