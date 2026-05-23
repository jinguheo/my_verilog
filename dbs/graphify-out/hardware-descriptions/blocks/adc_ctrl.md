# Hardware Description: adc_ctrl

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `adc_ctrl`
- `approved_label`: `pending:adc_ctrl`
- `doc_anchor`: `adc_ctrl`
- `module_name_prefix`: `adc_ctrl`
- `bridge_edge_count`: 104

## Inferred Hardware Role

`adc_ctrl` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 84, component: 33, testplan: 30, interface: 16, theory: 16
- Code categories: dv: 81, rtl: 46, sva: 8
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 32

## Spec Anchors

- `component:adc_ctrl` (L1) - `__graphify_spec_only__/components.md`
- `adc_ctrl.hjson` (L1) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `human name` (L5) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `one line desc` (L6) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `one paragraph desc` (L7) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `cip id` (L15) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `design spec` (L16) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `dv doc` (L17) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `hw checklist` (L18) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `sw checklist` (L19) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `version` (L20) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `life stage` (L21) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson`
- `adc_ctrl_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_sec_cm_testplan.hjson`
- `adc_ctrl_testplan.hjson` (L1) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `testpoints` (L12) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `desc` (L15) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `stage` (L31) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `tests` (L32) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `Stimulus` (L232) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `Checking` (L235) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `covergroups` (L244) - `opentitan/hw/ip/adc_ctrl/data/adc_ctrl_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `ADC CTRL Checklist` (L1) - `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `Design Checklist` (L11) - `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `D1` (L13) - `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `D2` (L37) - `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `D2S` (L79) - `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `D3` (L99) - `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `Verification Checklist` (L125) - `opentitan/hw/ip/adc_ctrl/doc/checklist.md`
- `V1` (L127) - `opentitan/hw/ip/adc_ctrl/doc/checklist.md`

## Code Evidence

- `tb.sv` (L1) - `opentitan\hw\ip\adc_ctrl\dv\tb.sv`
- `adc_ctrl_env_pkg` (L9) - `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv`
- `adc_ctrl_test_pkg` (L34) - `opentitan\hw\ip\adc_ctrl\dv\tb.sv`
- `tb` (L28) - `opentitan\hw\ip\adc_ctrl\dv\tb.sv`
- `adc_ctrl_core_cov_if.sv` (L1) - `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_core_cov_if.sv`
- `adc_ctrl_pkg` (L11) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv`
- `adc_ctrl_cov_bind.sv` (L1) - `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv`
- `adc_ctrl_cov_bind` (L6) - `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv`
- `adc_ctrl_bind.sv` (L1) - `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_bind.sv`
- `adc_ctrl_bind` (L5) - `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_bind.sv`
- `adc_ctrl_fsm_sva_if.sv` (L1) - `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_fsm_sva_if.sv`
- `adc_ctrl_sva_if.sv` (L1) - `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_sva_if.sv`
- `adc_ctrl_base_test.sv` (L1) - `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_base_test.sv`
- `adc_ctrl_test_pkg.sv` (L1) - `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv`
- `adc_ctrl.sv` (L1) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv`
- `adc_ctrl` (L9) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv`
- `adc_ctrl_reg_pkg` (L24) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_top.sv`
- `adc_ctrl_reg_top` (L71) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv`
- `adc_ctrl_core` (L85) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv`
- `adc_ctrl_core.sv` (L1) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv`
- `adc_ctrl_core` (L9) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv`
- `adc_ctrl_fsm` (L153) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv`
- `adc_ctrl_intr` (L193) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv`
- `adc_ctrl_fsm.sv` (L1) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv`
- `adc_ctrl_fsm` (L9) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv`
- `adc_ctrl_intr.sv` (L1) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_intr.sv`
- `adc_ctrl_intr` (L7) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_intr.sv`
- `adc_ctrl_pkg.sv` (L1) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_pkg.sv`
- `adc_ctrl_reg_pkg.sv` (L1) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_pkg.sv`
- `adc_ctrl_reg_top.sv` (L1) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_top.sv`
- `adc_ctrl_reg_top` (L9) - `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_top.sv`
- `adc_ctrl` (L2047) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_core_cov_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_core_cov_if.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_base_test.sv` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_env_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_fsm_sva_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_fsm_sva_if.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_test_pkg.sv` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_cov_bind.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_cov_bind` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_sva_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_sva_if.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_bind.sv` | `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_bind` | `opentitan\hw\ip\adc_ctrl\dv\sva\adc_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_reg_pkg` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_reg_pkg.sv` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_reg_top.sv` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_reg_top` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_core.sv` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_core` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_fsm` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_intr` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_core.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_intr.sv` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_intr.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_intr` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_intr.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_pkg` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_fsm.sv` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_fsm` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_pkg.sv` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl.sv` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_reg_top` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_core` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `adc_ctrl_test_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `tb.sv` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:adc_ctrl` | `tb` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `tb.sv` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `adc_ctrl_env_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `adc_ctrl_test_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `tb` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `adc_ctrl_core_cov_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_core_cov_if.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `adc_ctrl_pkg` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `adc_ctrl_cov_bind.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `adc_ctrl.hjson` | `adc_ctrl_cov_bind` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `adc_ctrl_env_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `adc_ctrl_test_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `adc_ctrl_core_cov_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_core_cov_if.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `adc_ctrl_pkg` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `adc_ctrl_cov_bind.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_sec_cm_testplan.hjson` | `adc_ctrl_cov_bind` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `adc_ctrl_env_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `adc_ctrl_test_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `tb` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `adc_ctrl_core_cov_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_core_cov_if.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `adc_ctrl_pkg` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `adc_ctrl_cov_bind.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `adc_ctrl_testplan.hjson` | `adc_ctrl_cov_bind` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `adc_ctrl_env_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `adc_ctrl_test_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `adc_ctrl_core_cov_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_core_cov_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `adc_ctrl_pkg` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `adc_ctrl_cov_bind.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `adc_ctrl_cov_bind` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `adc_ctrl_env_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `adc_ctrl_test_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `adc_ctrl_core_cov_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_core_cov_if.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `adc_ctrl_pkg` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `adc_ctrl_cov_bind.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `adc_ctrl_cov_bind` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `tb.sv` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `adc_ctrl_env_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tests\adc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `adc_ctrl_test_pkg` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `tb` | `opentitan\hw\ip\adc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `adc_ctrl_core_cov_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_core_cov_if.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `adc_ctrl_pkg` | `opentitan\hw\ip\adc_ctrl\rtl\adc_ctrl_fsm.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `adc_ctrl_cov_bind.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `adc_ctrl_cov_bind` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_cov_bind.sv` |

## Retrieval Guidance

- When a code-only query mentions `adc_ctrl`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
