# Hardware Description: otp_macro

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `otp_macro`
- `approved_label`: `pending:otp_macro`
- `doc_anchor`: `otp_macro`
- `module_name_prefix`: `otp_macro`
- `bridge_edge_count`: 33

## Inferred Hardware Role

`otp_macro` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 31, testplan: 13, component: 10
- Code categories: rtl: 41
- Bridge relations: spec_path_matches_code_path: 24, spec_component_matches_code: 9

## Spec Anchors

- `component:otp_macro` (L1) - `__graphify_spec_only__/components.md`
- `otp_macro.hjson` (L1) - `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `human name` (L6) - `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `one line desc` (L7) - `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `cip id` (L15) - `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `design spec` (L16) - `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `revisions` (L20) - `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `version` (L22) - `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `life stage` (L23) - `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `design stage` (L24) - `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `verification stage` (L25) - `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `otp_macro_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/otp_macro/data/otp_macro_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/otp_macro/data/otp_macro_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/otp_macro/data/otp_macro_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/otp_macro/data/otp_macro_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/otp_macro/data/otp_macro_sec_cm_testplan.hjson`
- `README.md` (L1) - `opentitan/hw/ip/otp_macro/README.md`
- `OTP MACRO HWIP Technical Specification` (L1) - `opentitan/hw/ip/otp_macro/README.md`
- `Overview` (L3) - `opentitan/hw/ip/otp_macro/README.md`
- `Features` (L9) - `opentitan/hw/ip/otp_macro/README.md`

## Code Evidence

- `otp_macro.sv` (L1) - `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv`
- `otp_macro` (L7) - `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv`
- `otp_macro_reg_pkg` (L32) - `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv`
- `otp_macro_prim_reg_top` (L160) - `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv`
- `otp_macro_pkg.sv` (L1) - `opentitan\hw\ip\otp_macro\rtl\otp_macro_pkg.sv`
- `otp_macro_prim_reg_top.sv` (L1) - `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv`
- `otp_macro_prim_reg_top` (L9) - `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv`
- `otp_macro_reg_pkg.sv` (L1) - `opentitan\hw\ip\otp_macro\rtl\otp_macro_reg_pkg.sv`
- `otp_macro` (L1559) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro_reg_pkg` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro_prim_reg_top.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro_reg_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_reg_pkg.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_pkg.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro_reg_pkg` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_pkg.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro_prim_reg_top.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro_reg_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_reg_pkg.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro_reg_pkg` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_pkg.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro_prim_reg_top.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro_reg_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_reg_pkg.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro_reg_pkg` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_pkg.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro_prim_reg_top.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro_reg_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_reg_pkg.sv` |

## Retrieval Guidance

- When a code-only query mentions `otp_macro`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
