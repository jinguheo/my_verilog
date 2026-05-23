# Hardware Description: xbar_dbg

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `xbar_dbg`
- `approved_label`: `pending:xbar_dbg`
- `doc_anchor`: `xbar_dbg`
- `module_name_prefix`: `xbar_dbg`
- `bridge_edge_count`: 39

## Inferred Hardware Role

`xbar_dbg` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 49, component: 10
- Code categories: rtl: 39, dv: 8
- Bridge relations: spec_path_matches_code_path: 30, spec_component_matches_code: 9

## Spec Anchors

- `component:xbar_dbg` (L1) - `__graphify_spec_only__/components.md`
- `xbar_dbg.gen.hjson` (L1) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.gen.hjson`
- `clock srcs` (L11) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.gen.hjson`
- `clk dbg i` (L13) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.gen.hjson`
- `clk peri i` (L14) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.gen.hjson`
- `clock group` (L16) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.gen.hjson`
- `reset connections` (L18) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.gen.hjson`
- `rst dbg ni` (L20) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.gen.hjson`
- `domain` (L23) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.gen.hjson`
- `rst peri ni` (L25) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.gen.hjson`
- `clock connections` (L31) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.gen.hjson`
- `connections` (L40) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.gen.hjson`
- `xbar_dbg.hjson` (L1) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.hjson`
- `clock primary` (L7) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.hjson`
- `other clock list` (L8) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.hjson`
- `reset primary` (L9) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.hjson`
- `other reset list` (L10) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.hjson`
- `inter signal list` (L13) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.hjson`
- `act` (L18) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.hjson`
- `package` (L19) - `opentitan/hw/top_darjeeling/ip/xbar_dbg/data/autogen/xbar_dbg.hjson`

## Code Evidence

- `tb__xbar_connect.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\tb__xbar_connect.sv`
- `xbar_dbg_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\xbar_dbg_bind.sv`
- `xbar_dbg_bind` (L6) - `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\xbar_dbg_bind.sv`
- `xbar_env_pkg__params.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\xbar_env_pkg__params.sv`
- `tl_dbg_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\tl_dbg_pkg.sv`
- `xbar_dbg.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\xbar_dbg.sv`
- `xbar_dbg` (L18) - `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\xbar_dbg.sv`
- `tl_dbg_pkg` (L42) - `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\xbar_dbg.sv`
- `xbar_dbg` (L3263) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `prim_flop_en` (L269) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `prim_ram_1p_adv` (L1487) - `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
- `tlul_cmd_intg_gen` (L46) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv`
- `dma` (L2221) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `keymgr_dpe` (L1905) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `tlul_jtag_dtm` (L1340) - `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
- `mbx` (L2257) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `prim_onehot_enc` (L128) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `top_racl_pkg` (L13) - `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv`
- `prim_pad_wrapper_pkg` (L61) - `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv`
- `tlul_pkg` (L165) - `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
- `adc_ctrl` (L2047) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
- `aes` (L1174) - `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
- `aon_timer` (L1049) - `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
- `csrng` (L2617) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:xbar_dbg` | `xbar_dbg_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\xbar_dbg_bind.sv` |
| `spec_component_matches_code` | `component:xbar_dbg` | `xbar_dbg_bind` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\xbar_dbg_bind.sv` |
| `spec_component_matches_code` | `component:xbar_dbg` | `xbar_dbg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\xbar_dbg.sv` |
| `spec_component_matches_code` | `component:xbar_dbg` | `xbar_dbg` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\xbar_dbg.sv` |
| `spec_component_matches_code` | `component:xbar_dbg` | `xbar_dbg` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:xbar_dbg` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_component_matches_code` | `component:xbar_dbg` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\tb__xbar_connect.sv` |
| `spec_component_matches_code` | `component:xbar_dbg` | `tl_dbg_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\tl_dbg_pkg.sv` |
| `spec_component_matches_code` | `component:xbar_dbg` | `tl_dbg_pkg` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\xbar_dbg.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `top_racl_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `prim_pad_wrapper_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `tlul_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `aes` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `aon_timer` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.gen.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `top_racl_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `prim_pad_wrapper_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `tlul_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `aes` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `aon_timer` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |

## Retrieval Guidance

- When a code-only query mentions `xbar_dbg`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
