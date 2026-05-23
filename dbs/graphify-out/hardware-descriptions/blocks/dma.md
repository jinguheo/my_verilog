# Hardware Description: dma

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `dma`
- `approved_label`: `pending:dma`
- `doc_anchor`: `dma`
- `module_name_prefix`: `dma`
- `bridge_edge_count`: 95

## Inferred Hardware Role

`dma` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 88, testplan: 30, component: 24, theory: 19, interface: 16
- Code categories: dv: 65, rtl: 28, sva: 24
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 23

## Spec Anchors

- `component:dma` (L1) - `__graphify_spec_only__/components.md`
- `dma.hjson` (L1) - `opentitan/hw/ip/dma/data/dma.hjson`
- `human name` (L8) - `opentitan/hw/ip/dma/data/dma.hjson`
- `one line desc` (L9) - `opentitan/hw/ip/dma/data/dma.hjson`
- `one paragraph desc` (L10) - `opentitan/hw/ip/dma/data/dma.hjson`
- `cip id` (L16) - `opentitan/hw/ip/dma/data/dma.hjson`
- `design spec` (L17) - `opentitan/hw/ip/dma/data/dma.hjson`
- `dv doc` (L18) - `opentitan/hw/ip/dma/data/dma.hjson`
- `version` (L19) - `opentitan/hw/ip/dma/data/dma.hjson`
- `clocking` (L21) - `opentitan/hw/ip/dma/data/dma.hjson`
- `scan` (L22) - `opentitan/hw/ip/dma/data/dma.hjson`
- `bus interfaces` (L23) - `opentitan/hw/ip/dma/data/dma.hjson`
- `dma_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/dma/data/dma_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/dma/data/dma_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/dma/data/dma_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/dma/data/dma_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/dma/data/dma_sec_cm_testplan.hjson`
- `dma_testplan.hjson` (L1) - `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `testpoints` (L10) - `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `desc` (L16) - `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `Stimulus` (L19) - `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `Checking` (L31) - `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `stage` (L38) - `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `tests` (L39) - `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `covergroups` (L316) - `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/dma/doc/checklist.md`
- `DMA Controller Checklist` (L1) - `opentitan/hw/ip/dma/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/dma/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/dma/doc/checklist.md`
- `D2` (L34) - `opentitan/hw/ip/dma/doc/checklist.md`
- `D2S` (L76) - `opentitan/hw/ip/dma/doc/checklist.md`
- `D3` (L96) - `opentitan/hw/ip/dma/doc/checklist.md`
- `Verification Checklist` (L122) - `opentitan/hw/ip/dma/doc/checklist.md`
- `V1` (L124) - `opentitan/hw/ip/dma/doc/checklist.md`

## Code Evidence

- `dma_cov_bind.sv` (L1) - `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv`
- `dma_cov_bind` (L5) - `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv`
- `dma_cov_if.sv` (L1) - `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv`
- `dma_reg_pkg` (L32) - `opentitan\hw\ip\dma\rtl\dma_reg_top.sv`
- `dma_bind.sv` (L1) - `opentitan\hw\ip\dma\dv\sva\dma_bind.sv`
- `dma_bind` (L5) - `opentitan\hw\ip\dma\dv\sva\dma_bind.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\dma\dv\tb\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\dma\dv\tb\tb.sv`
- `dma_pkg` (L9) - `opentitan\hw\ip\dma\rtl\dma.sv`
- `dma_env_pkg` (L8) - `opentitan\hw\ip\dma\dv\tests\dma_test_pkg.sv`
- `dma_test_pkg` (L12) - `opentitan\hw\ip\dma\dv\tb\tb.sv`
- `dma_sys_tl_if` (L39) - `opentitan\hw\ip\dma\dv\tb\tb.sv`
- `tlul_assert` (L44) - `opentitan\hw\ip\dma\dv\tb\tb.sv`
- `dma_base_test.sv` (L1) - `opentitan\hw\ip\dma\dv\tests\dma_base_test.sv`
- `dma_test_pkg.sv` (L1) - `opentitan\hw\ip\dma\dv\tests\dma_test_pkg.sv`
- `dma.sv` (L1) - `opentitan\hw\ip\dma\rtl\dma.sv`
- `dma` (L7) - `opentitan\hw\ip\dma\rtl\dma.sv`
- `dma_reg_top` (L164) - `opentitan\hw\ip\dma\rtl\dma.sv`
- `dma_pkg.sv` (L1) - `opentitan\hw\ip\dma\rtl\dma_pkg.sv`
- `dma_reg_pkg.sv` (L1) - `opentitan\hw\ip\dma\rtl\dma_reg_pkg.sv`
- `dma_reg_top.sv` (L1) - `opentitan\hw\ip\dma\rtl\dma_reg_top.sv`
- `dma_reg_top` (L9) - `opentitan\hw\ip\dma\rtl\dma_reg_top.sv`
- `dma` (L2221) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:dma` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_base_test.sv` | `opentitan\hw\ip\dma\dv\tests\dma_base_test.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_env_pkg` | `opentitan\hw\ip\dma\dv\tests\dma_test_pkg.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_test_pkg.sv` | `opentitan\hw\ip\dma\dv\tests\dma_test_pkg.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_cov_bind` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_cov_if.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_reg_pkg` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_bind.sv` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_bind` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_reg_pkg.sv` | `opentitan\hw\ip\dma\rtl\dma_reg_pkg.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_reg_top.sv` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_reg_top` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_pkg.sv` | `opentitan\hw\ip\dma\rtl\dma_pkg.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_test_pkg` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_sys_tl_if` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_pkg` | `opentitan\hw\ip\dma\rtl\dma.sv` |
| `spec_component_matches_code` | `component:dma` | `dma.sv` | `opentitan\hw\ip\dma\rtl\dma.sv` |
| `spec_component_matches_code` | `component:dma` | `dma` | `opentitan\hw\ip\dma\rtl\dma.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_reg_top` | `opentitan\hw\ip\dma\rtl\dma.sv` |
| `spec_component_matches_code` | `component:dma` | `tb.sv` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:dma` | `tb` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:dma` | `tlul_assert` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `dma_cov_bind` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `dma_cov_if.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `dma_reg_pkg` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `dma_bind.sv` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `dma_bind` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `tb.sv` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `tb` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `dma_cov_bind` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `dma_cov_if.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `dma_reg_pkg` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `dma_bind.sv` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `dma_bind` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `dma_cov_bind` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `dma_cov_if.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `dma_reg_pkg` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `dma_bind.sv` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `dma_bind` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `tb` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `dma_cov_bind` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `dma_cov_if.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `dma_reg_pkg` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `dma_bind.sv` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `dma_bind` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `dma_cov_bind` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `dma_cov_if.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `dma_reg_pkg` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `dma_bind.sv` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `dma_bind` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `dma_cov_bind` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `dma_cov_if.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `dma_reg_pkg` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `dma_bind.sv` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `dma_bind` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `tb.sv` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `tb` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `registers.md` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `registers.md` | `dma_cov_bind` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `registers.md` | `dma_cov_if.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv` |
| `spec_path_matches_code_path` | `registers.md` | `dma_reg_pkg` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_path_matches_code_path` | `registers.md` | `dma_bind.sv` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `registers.md` | `dma_bind` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `registers.md` | `tb.sv` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `registers.md` | `tb` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |

## Retrieval Guidance

- When a code-only query mentions `dma`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
