# Hardware Description: xbar_mbx

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `xbar_mbx`
- `approved_label`: `pending:xbar_mbx`
- `doc_anchor`: `xbar_mbx`
- `module_name_prefix`: `xbar_mbx`
- `bridge_edge_count`: 39

## Inferred Hardware Role

`xbar_mbx` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 49, component: 10
- Code categories: rtl: 39, dv: 8
- Bridge relations: spec_path_matches_code_path: 30, spec_component_matches_code: 9

## Spec Anchors

- `component:xbar_mbx` (L1) - `__graphify_spec_only__/components.md`
- `xbar_mbx.gen.hjson` (L1) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.gen.hjson`
- `clock srcs` (L11) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.gen.hjson`
- `clk mbx i` (L13) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.gen.hjson`
- `clock group` (L15) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.gen.hjson`
- `reset connections` (L17) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.gen.hjson`
- `rst mbx ni` (L19) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.gen.hjson`
- `domain` (L22) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.gen.hjson`
- `clock connections` (L25) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.gen.hjson`
- `connections` (L33) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.gen.hjson`
- `mbx` (L35) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.gen.hjson`
- `nodes` (L50) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.gen.hjson`
- `xbar_mbx.hjson` (L1) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.hjson`
- `clock primary` (L7) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.hjson`
- `other clock list` (L8) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.hjson`
- `reset primary` (L9) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.hjson`
- `other reset list` (L10) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.hjson`
- `inter signal list` (L13) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.hjson`
- `act` (L18) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.hjson`
- `package` (L19) - `opentitan/hw/top_darjeeling/ip/xbar_mbx/data/autogen/xbar_mbx.hjson`

## Code Evidence

- `tb__xbar_connect.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\tb__xbar_connect.sv`
- `xbar_env_pkg__params.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\xbar_env_pkg__params.sv`
- `xbar_mbx_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\xbar_mbx_bind.sv`
- `xbar_mbx_bind` (L6) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\xbar_mbx_bind.sv`
- `tl_mbx_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\tl_mbx_pkg.sv`
- `xbar_mbx.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\xbar_mbx.sv`
- `xbar_mbx` (L23) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\xbar_mbx.sv`
- `tl_mbx_pkg` (L59) - `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\xbar_mbx.sv`
- `xbar_mbx` (L3208) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
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
| `spec_component_matches_code` | `component:xbar_mbx` | `xbar_mbx_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\xbar_mbx_bind.sv` |
| `spec_component_matches_code` | `component:xbar_mbx` | `xbar_mbx_bind` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\xbar_mbx_bind.sv` |
| `spec_component_matches_code` | `component:xbar_mbx` | `xbar_mbx.sv` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\xbar_mbx.sv` |
| `spec_component_matches_code` | `component:xbar_mbx` | `xbar_mbx` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\xbar_mbx.sv` |
| `spec_component_matches_code` | `component:xbar_mbx` | `xbar_mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:xbar_mbx` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_component_matches_code` | `component:xbar_mbx` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\dv\autogen\tb__xbar_connect.sv` |
| `spec_component_matches_code` | `component:xbar_mbx` | `tl_mbx_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\tl_mbx_pkg.sv` |
| `spec_component_matches_code` | `component:xbar_mbx` | `tl_mbx_pkg` | `opentitan\hw\top_darjeeling\ip\xbar_mbx\rtl\autogen\xbar_mbx.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `top_racl_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `prim_pad_wrapper_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `tlul_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `aes` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `aon_timer` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.gen.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `top_racl_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `prim_pad_wrapper_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `tlul_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `aes` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `aon_timer` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_mbx.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |

## Retrieval Guidance

- When a code-only query mentions `xbar_mbx`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
