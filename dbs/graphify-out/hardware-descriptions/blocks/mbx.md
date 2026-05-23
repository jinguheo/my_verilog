# Hardware Description: mbx

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `mbx`
- `approved_label`: `pending:mbx`
- `doc_anchor`: `mbx`
- `module_name_prefix`: `mbx`
- `bridge_edge_count`: 117

## Inferred Hardware Role

`mbx` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 103, component: 38, testplan: 27, theory: 19, interface: 16
- Code categories: dv: 72, rtl: 57, sva: 24
- Bridge relations: spec_path_matches_code_path: 80, spec_component_matches_code: 37

## Spec Anchors

- `component:mbx` (L1) - `__graphify_spec_only__/components.md`
- `mbx.hjson` (L1) - `opentitan/hw/ip/mbx/data/mbx.hjson`
- `human name` (L8) - `opentitan/hw/ip/mbx/data/mbx.hjson`
- `one line desc` (L9) - `opentitan/hw/ip/mbx/data/mbx.hjson`
- `one paragraph desc` (L10) - `opentitan/hw/ip/mbx/data/mbx.hjson`
- `cip id` (L15) - `opentitan/hw/ip/mbx/data/mbx.hjson`
- `design spec` (L16) - `opentitan/hw/ip/mbx/data/mbx.hjson`
- `dv doc` (L17) - `opentitan/hw/ip/mbx/data/mbx.hjson`
- `version` (L18) - `opentitan/hw/ip/mbx/data/mbx.hjson`
- `clocking` (L20) - `opentitan/hw/ip/mbx/data/mbx.hjson`
- `bus interfaces` (L21) - `opentitan/hw/ip/mbx/data/mbx.hjson`
- `inter signal list` (L26) - `opentitan/hw/ip/mbx/data/mbx.hjson`
- `mbx_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/mbx/data/mbx_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/mbx/data/mbx_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/mbx/data/mbx_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/mbx/data/mbx_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/mbx/data/mbx_sec_cm_testplan.hjson`
- `mbx_testplan.hjson` (L1) - `opentitan/hw/ip/mbx/data/mbx_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/mbx/data/mbx_testplan.hjson`
- `testpoints` (L14) - `opentitan/hw/ip/mbx/data/mbx_testplan.hjson`
- `desc` (L16) - `opentitan/hw/ip/mbx/data/mbx_testplan.hjson`
- `stage` (L27) - `opentitan/hw/ip/mbx/data/mbx_testplan.hjson`
- `tests` (L28) - `opentitan/hw/ip/mbx/data/mbx_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/mbx/doc/checklist.md`
- `Mailbox Checklist` (L1) - `opentitan/hw/ip/mbx/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/mbx/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/mbx/doc/checklist.md`
- `D2` (L34) - `opentitan/hw/ip/mbx/doc/checklist.md`
- `D2S` (L76) - `opentitan/hw/ip/mbx/doc/checklist.md`
- `D3` (L96) - `opentitan/hw/ip/mbx/doc/checklist.md`
- `Verification Checklist` (L122) - `opentitan/hw/ip/mbx/doc/checklist.md`
- `V1` (L124) - `opentitan/hw/ip/mbx/doc/checklist.md`
- `V2` (L174) - `opentitan/hw/ip/mbx/doc/checklist.md`
- `V2S` (L220) - `opentitan/hw/ip/mbx/doc/checklist.md`
- `DOE.md` (L1) - `opentitan/hw/ip/mbx/doc/DOE.md`

## Code Evidence

- `tb.sv` (L1) - `opentitan\hw\ip\mbx\dv\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\mbx\dv\tb.sv`
- `mbx_env_pkg` (L9) - `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv`
- `mbx_test_pkg` (L10) - `opentitan\hw\ip\mbx\dv\tb.sv`
- `mbx_bind.sv` (L1) - `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv`
- `mbx_bind` (L5) - `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv`
- `mbx_base_test.sv` (L1) - `opentitan\hw\ip\mbx\dv\tests\mbx_base_test.sv`
- `mbx_test_pkg.sv` (L1) - `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv`
- `mbx.sv` (L1) - `opentitan\hw\ip\mbx\rtl\mbx.sv`
- `mbx` (L7) - `opentitan\hw\ip\mbx\rtl\mbx.sv`
- `mbx_reg_pkg` (L9) - `opentitan\hw\ip\mbx\rtl\mbx_sysif.sv`
- `mbx_hostif` (L124) - `opentitan\hw\ip\mbx\rtl\mbx.sv`
- `mbx_sysif` (L224) - `opentitan\hw\ip\mbx\rtl\mbx.sv`
- `mbx_imbx` (L282) - `opentitan\hw\ip\mbx\rtl\mbx.sv`
- `mbx_ombx` (L317) - `opentitan\hw\ip\mbx\rtl\mbx.sv`
- `mbx_sramrwarb` (L361) - `opentitan\hw\ip\mbx\rtl\mbx.sv`
- `mbx_core_reg_top.sv` (L1) - `opentitan\hw\ip\mbx\rtl\mbx_core_reg_top.sv`
- `mbx_core_reg_top` (L9) - `opentitan\hw\ip\mbx\rtl\mbx_core_reg_top.sv`
- `mbx_fsm.sv` (L1) - `opentitan\hw\ip\mbx\rtl\mbx_fsm.sv`
- `mbx_fsm` (L7) - `opentitan\hw\ip\mbx\rtl\mbx_fsm.sv`
- `mbx_hostif.sv` (L1) - `opentitan\hw\ip\mbx\rtl\mbx_hostif.sv`
- `mbx_hostif` (L7) - `opentitan\hw\ip\mbx\rtl\mbx_hostif.sv`
- `mbx_core_reg_top` (L111) - `opentitan\hw\ip\mbx\rtl\mbx_hostif.sv`
- `mbx_imbx.sv` (L1) - `opentitan\hw\ip\mbx\rtl\mbx_imbx.sv`
- `mbx_imbx` (L7) - `opentitan\hw\ip\mbx\rtl\mbx_imbx.sv`
- `mbx_fsm` (L250) - `opentitan\hw\ip\mbx\rtl\mbx_ombx.sv`
- `mbx_ombx.sv` (L1) - `opentitan\hw\ip\mbx\rtl\mbx_ombx.sv`
- `mbx_ombx` (L7) - `opentitan\hw\ip\mbx\rtl\mbx_ombx.sv`
- `mbx_reg_pkg.sv` (L1) - `opentitan\hw\ip\mbx\rtl\mbx_reg_pkg.sv`
- `mbx_soc_reg_top.sv` (L1) - `opentitan\hw\ip\mbx\rtl\mbx_soc_reg_top.sv`
- `mbx_soc_reg_top` (L9) - `opentitan\hw\ip\mbx\rtl\mbx_soc_reg_top.sv`
- `mbx_sramrwarb.sv` (L1) - `opentitan\hw\ip\mbx\rtl\mbx_sramrwarb.sv`
- `mbx_sramrwarb` (L7) - `opentitan\hw\ip\mbx\rtl\mbx_sramrwarb.sv`
- `mbx_sysif.sv` (L1) - `opentitan\hw\ip\mbx\rtl\mbx_sysif.sv`
- `mbx_sysif` (L7) - `opentitan\hw\ip\mbx\rtl\mbx_sysif.sv`
- `mbx_soc_reg_top` (L96) - `opentitan\hw\ip\mbx\rtl\mbx_sysif.sv`
- `mbx` (L2257) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:mbx` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_base_test.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_base_test.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_env_pkg` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_test_pkg.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_core_reg_top.sv` | `opentitan\hw\ip\mbx\rtl\mbx_core_reg_top.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_core_reg_top` | `opentitan\hw\ip\mbx\rtl\mbx_core_reg_top.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_soc_reg_top.sv` | `opentitan\hw\ip\mbx\rtl\mbx_soc_reg_top.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_soc_reg_top` | `opentitan\hw\ip\mbx\rtl\mbx_soc_reg_top.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_sramrwarb.sv` | `opentitan\hw\ip\mbx\rtl\mbx_sramrwarb.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_sramrwarb` | `opentitan\hw\ip\mbx\rtl\mbx_sramrwarb.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_bind.sv` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_bind` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_reg_pkg.sv` | `opentitan\hw\ip\mbx\rtl\mbx_reg_pkg.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_hostif.sv` | `opentitan\hw\ip\mbx\rtl\mbx_hostif.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_hostif` | `opentitan\hw\ip\mbx\rtl\mbx_hostif.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_core_reg_top` | `opentitan\hw\ip\mbx\rtl\mbx_hostif.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_reg_pkg` | `opentitan\hw\ip\mbx\rtl\mbx_sysif.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_sysif.sv` | `opentitan\hw\ip\mbx\rtl\mbx_sysif.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_sysif` | `opentitan\hw\ip\mbx\rtl\mbx_sysif.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_soc_reg_top` | `opentitan\hw\ip\mbx\rtl\mbx_sysif.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_imbx.sv` | `opentitan\hw\ip\mbx\rtl\mbx_imbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_imbx` | `opentitan\hw\ip\mbx\rtl\mbx_imbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_fsm` | `opentitan\hw\ip\mbx\rtl\mbx_ombx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_ombx.sv` | `opentitan\hw\ip\mbx\rtl\mbx_ombx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_ombx` | `opentitan\hw\ip\mbx\rtl\mbx_ombx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_fsm.sv` | `opentitan\hw\ip\mbx\rtl\mbx_fsm.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_fsm` | `opentitan\hw\ip\mbx\rtl\mbx_fsm.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx.sv` | `opentitan\hw\ip\mbx\rtl\mbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx` | `opentitan\hw\ip\mbx\rtl\mbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_hostif` | `opentitan\hw\ip\mbx\rtl\mbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_sysif` | `opentitan\hw\ip\mbx\rtl\mbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_imbx` | `opentitan\hw\ip\mbx\rtl\mbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_ombx` | `opentitan\hw\ip\mbx\rtl\mbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_sramrwarb` | `opentitan\hw\ip\mbx\rtl\mbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_test_pkg` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_component_matches_code` | `component:mbx` | `tb.sv` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_component_matches_code` | `component:mbx` | `tb` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `tb.sv` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `tb` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `mbx_env_pkg` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `mbx_test_pkg` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `mbx_bind.sv` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `mbx_bind` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `mbx_base_test.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_base_test.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `mbx_test_pkg.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `mbx_env_pkg` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `mbx_test_pkg` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `mbx_bind.sv` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `mbx_bind` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `mbx_base_test.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_base_test.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `mbx_test_pkg.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `tb` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `mbx_env_pkg` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `mbx_test_pkg` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `mbx_bind.sv` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `mbx_bind` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `mbx_base_test.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_base_test.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `mbx_test_pkg.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `mbx_env_pkg` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `mbx_test_pkg` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `mbx_bind.sv` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `mbx_bind` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `mbx_base_test.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_base_test.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `mbx_test_pkg.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `DOE.md` | `tb.sv` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `DOE.md` | `tb` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `DOE.md` | `mbx_env_pkg` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `DOE.md` | `mbx_test_pkg` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `DOE.md` | `mbx_bind.sv` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `DOE.md` | `mbx_bind` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `DOE.md` | `mbx_base_test.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_base_test.sv` |
| `spec_path_matches_code_path` | `DOE.md` | `mbx_test_pkg.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `mbx_env_pkg` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |

## Retrieval Guidance

- When a code-only query mentions `mbx`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
