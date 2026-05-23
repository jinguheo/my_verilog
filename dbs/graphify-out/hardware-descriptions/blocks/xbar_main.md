# Hardware Description: xbar_main

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `xbar_main`
- `approved_label`: `pending:xbar_main`
- `doc_anchor`: `xbar_main`
- `module_name_prefix`: `xbar_main`
- `bridge_edge_count`: 119

## Inferred Hardware Role

`xbar_main` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 153, component: 24
- Code categories: rtl: 93, dv: 48
- Bridge relations: spec_path_matches_code_path: 96, spec_component_matches_code: 23

## Spec Anchors

- `component:xbar_main` (L1) - `__graphify_spec_only__/components.md`
- `xbar_main.gen.hjson` (L1) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `clock srcs` (L11) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `clk main i` (L13) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `clk fixed i` (L14) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `clock group` (L16) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `reset connections` (L18) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `rst main ni` (L20) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `domain` (L23) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `rst fixed ni` (L25) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `clock connections` (L31) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `connections` (L40) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `xbar_main.hjson` (L1) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.hjson`
- `clock primary` (L7) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.hjson`
- `other clock list` (L8) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.hjson`
- `reset primary` (L9) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.hjson`
- `other reset list` (L10) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.hjson`
- `inter signal list` (L13) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.hjson`
- `act` (L18) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.hjson`
- `package` (L19) - `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.hjson`
- `xbar_main.gen.hjson` (L1) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `clock srcs` (L11) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `clk main i` (L13) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `clk fixed i` (L14) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `clk usb i` (L15) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `clk spi host0 i` (L16) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `clk spi host1 i` (L17) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `clock group` (L19) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `reset connections` (L21) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `rst main ni` (L23) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `domain` (L26) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- `xbar_main.hjson` (L1) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.hjson`
- `clock primary` (L7) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.hjson`
- `other clock list` (L8) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.hjson`
- `reset primary` (L9) - `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.hjson`

## Code Evidence

- `tlul_socket_m1` (L273) - `opentitan\hw\top_englishbreakfast\ip\xbar_main\rtl\autogen\xbar_main.sv`
- `tb__xbar_connect.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\tb__xbar_connect.sv`
- `xbar_env_pkg__params.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_env_pkg__params.sv`
- `xbar_main_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_main_bind.sv`
- `xbar_main_bind` (L6) - `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_main_bind.sv`
- `tl_main_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\tl_main_pkg.sv`
- `xbar_main.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\xbar_main.sv`
- `xbar_main` (L229) - `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\xbar_main.sv`
- `tb__xbar_connect.sv` (L1) - `opentitan\hw\top_earlgrey\ip\xbar_main\dv\autogen\tb__xbar_connect.sv`
- `xbar_env_pkg__params.sv` (L1) - `opentitan\hw\top_earlgrey\ip\xbar_main\dv\autogen\xbar_env_pkg__params.sv`
- `xbar_main_bind.sv` (L1) - `opentitan\hw\top_earlgrey\ip\xbar_main\dv\autogen\xbar_main_bind.sv`
- `xbar_main_bind` (L6) - `opentitan\hw\top_earlgrey\ip\xbar_main\dv\autogen\xbar_main_bind.sv`
- `tl_main_pkg.sv` (L1) - `opentitan\hw\top_earlgrey\ip\xbar_main\rtl\autogen\tl_main_pkg.sv`
- `xbar_main.sv` (L1) - `opentitan\hw\top_earlgrey\ip\xbar_main\rtl\autogen\xbar_main.sv`
- `xbar_main` (L128) - `opentitan\hw\top_earlgrey\ip\xbar_main\rtl\autogen\xbar_main.sv`
- `tb__xbar_connect.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip\xbar_main\dv\autogen\tb__xbar_connect.sv`
- `xbar_env_pkg__params.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip\xbar_main\dv\autogen\xbar_env_pkg__params.sv`
- `xbar_main_bind.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip\xbar_main\dv\autogen\xbar_main_bind.sv`
- `xbar_main_bind` (L6) - `opentitan\hw\top_englishbreakfast\ip\xbar_main\dv\autogen\xbar_main_bind.sv`
- `tl_main_pkg.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip\xbar_main\rtl\autogen\tl_main_pkg.sv`
- `xbar_main.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip\xbar_main\rtl\autogen\xbar_main.sv`
- `xbar_main` (L35) - `opentitan\hw\top_englishbreakfast\ip\xbar_main\rtl\autogen\xbar_main.sv`
- `xbar_main` (L1438) - `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
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
- `BUFG` (L92) - `opentitan\hw\top_englishbreakfast\rtl\clkgen_xil7series.sv`
- `prim_mubi_pkg` (L905) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `prim_esc_receiver` (L283) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `prim_arbiter_fixed` (L58) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv`
- `prim_arbiter_tree` (L163) - `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv`
- `prim_count` (L240) - `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv`
- `prim_secded_hamming_72_64_enc` (L775) - `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:xbar_main` | `xbar_main_bind.sv` | `opentitan\hw\top_englishbreakfast\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_main_bind` | `opentitan\hw\top_englishbreakfast\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_main.sv` | `opentitan\hw\top_englishbreakfast\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_main` | `opentitan\hw\top_englishbreakfast\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_main_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_main_bind` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_main` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_main_bind.sv` | `opentitan\hw\top_earlgrey\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_main_bind` | `opentitan\hw\top_earlgrey\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_main.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_main` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_main.sv` | `opentitan\hw\top_earlgrey\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_main` | `opentitan\hw\top_earlgrey\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_englishbreakfast\ip\xbar_main\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `tb__xbar_connect.sv` | `opentitan\hw\top_englishbreakfast\ip\xbar_main\dv\autogen\tb__xbar_connect.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_earlgrey\ip\xbar_main\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `tl_main_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip\xbar_main\rtl\autogen\tl_main_pkg.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `tlul_socket_m1` | `opentitan\hw\top_englishbreakfast\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\tb__xbar_connect.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `tb__xbar_connect.sv` | `opentitan\hw\top_earlgrey\ip\xbar_main\dv\autogen\tb__xbar_connect.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `tl_main_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\tl_main_pkg.sv` |
| `spec_component_matches_code` | `component:xbar_main` | `tl_main_pkg.sv` | `opentitan\hw\top_earlgrey\ip\xbar_main\rtl\autogen\tl_main_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `tlul_socket_m1` | `opentitan\hw\top_englishbreakfast\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\tb__xbar_connect.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `xbar_main_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `xbar_main_bind` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `tl_main_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\tl_main_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `xbar_main.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `xbar_main` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `tlul_socket_m1` | `opentitan\hw\top_englishbreakfast\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\tb__xbar_connect.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `xbar_main_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `xbar_main_bind` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `tl_main_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\tl_main_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `xbar_main.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `xbar_main` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `tlul_socket_m1` | `opentitan\hw\top_englishbreakfast\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\tb__xbar_connect.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `xbar_main_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `xbar_main_bind` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `tl_main_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\tl_main_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `xbar_main.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `xbar_main` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `top_racl_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `prim_pad_wrapper_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `tlul_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `aes` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `aon_timer` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_main.gen.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `tlul_socket_m1` | `opentitan\hw\top_englishbreakfast\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\tb__xbar_connect.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `xbar_main_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `xbar_main_bind` | `opentitan\hw\top_darjeeling\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `tl_main_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\tl_main_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `xbar_main.sv` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `xbar_main` | `opentitan\hw\top_darjeeling\ip\xbar_main\rtl\autogen\xbar_main.sv` |
| `spec_path_matches_code_path` | `xbar_main.hjson` | `top_racl_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv` |

## Retrieval Guidance

- When a code-only query mentions `xbar_main`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
