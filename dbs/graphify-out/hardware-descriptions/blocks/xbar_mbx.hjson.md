# Hardware Description: xbar_mbx.hjson

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `xbar_mbx.hjson`
- `approved_label`: `pending:xbar_mbx.hjson`
- `doc_anchor`: `xbar_mbx.hjson`
- `module_name_prefix`: `xbar_mbx.hjson`
- `bridge_edge_count`: 16

## Inferred Hardware Role

`xbar_mbx.hjson` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 27
- Code categories: rtl: 12, dv: 4
- Bridge relations: spec_path_matches_code_path: 16

## Spec Anchors

- `xbar_mbx.hjson` (L1) - `opentitan/hw/top_darjeeling/data/xbar_mbx.hjson`
- `clock primary` (L6) - `opentitan/hw/top_darjeeling/data/xbar_mbx.hjson`
- `other clock list` (L7) - `opentitan/hw/top_darjeeling/data/xbar_mbx.hjson`
- `reset primary` (L8) - `opentitan/hw/top_darjeeling/data/xbar_mbx.hjson`
- `other reset list` (L9) - `opentitan/hw/top_darjeeling/data/xbar_mbx.hjson`
- `nodes` (L11) - `opentitan/hw/top_darjeeling/data/xbar_mbx.hjson`
- `addr space` (L14) - `opentitan/hw/top_darjeeling/data/xbar_mbx.hjson`
- `clock` (L15) - `opentitan/hw/top_darjeeling/data/xbar_mbx.hjson`
- `xbar` (L17) - `opentitan/hw/top_darjeeling/data/xbar_mbx.hjson`
- `pipeline` (L18) - `opentitan/hw/top_darjeeling/data/xbar_mbx.hjson`
- `connections` (L99) - `opentitan/hw/top_darjeeling/data/xbar_mbx.hjson`

## Code Evidence

- `prim_flop_en` (L269) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `prim_ram_1p_adv` (L1487) - `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
- `tlul_cmd_intg_gen` (L46) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv`
- `dma` (L2221) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `keymgr_dpe` (L1905) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `tlul_jtag_dtm` (L1340) - `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
- `mbx` (L2257) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `prim_onehot_enc` (L128) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `tb__xbar_connect.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\tb__xbar_connect.sv`
- `xbar_env_pkg__params.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\xbar_env_pkg__params.sv`
- `xbar_mbx_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\xbar_mbx_bind.sv`
- `xbar_mbx_bind` (L6) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\xbar_mbx_bind.sv`
- `tl_mbx_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\tl_mbx_pkg.sv`
- `xbar_mbx.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\xbar_mbx.sv`
- `xbar_mbx` (L23) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\xbar_mbx.sv`
- `tl_mbx_pkg` (L59) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\xbar_mbx.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\tb__xbar_connect.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `xbar_mbx_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\xbar_mbx_bind.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `xbar_mbx_bind` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\xbar_mbx_bind.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `tl_mbx_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\tl_mbx_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `xbar_mbx.sv` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\xbar_mbx.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `xbar_mbx` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\xbar_mbx.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `tl_mbx_pkg` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\xbar_mbx.sv` |

## Retrieval Guidance

- When a code-only query mentions `xbar_mbx.hjson`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
