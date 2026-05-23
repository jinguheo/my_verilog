# Hardware Description: xbar_peri

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `xbar_peri`
- `approved_label`: `pending:xbar_peri`
- `doc_anchor`: `xbar_peri`
- `module_name_prefix`: `xbar_peri`
- `bridge_edge_count`: 114

## Inferred Hardware Role

`xbar_peri` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 147, component: 25
- Code categories: rtl: 113, dv: 24
- Bridge relations: spec_path_matches_code_path: 90, spec_component_matches_code: 24

## Spec Anchors

- `component:xbar_peri` (L1) - `__graphify_spec_only__/components.md`
- `xbar_peri.gen.hjson` (L1) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `clock srcs` (L11) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `clk peri i` (L13) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `clock group` (L15) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `reset connections` (L17) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `rst peri ni` (L19) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `domain` (L22) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `clock connections` (L25) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `connections` (L33) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `main` (L35) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `nodes` (L58) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `xbar_peri.hjson` (L1) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.hjson`
- `clock primary` (L7) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.hjson`
- `other clock list` (L8) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.hjson`
- `reset primary` (L9) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.hjson`
- `other reset list` (L10) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.hjson`
- `inter signal list` (L13) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.hjson`
- `act` (L18) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.hjson`
- `package` (L19) - `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.hjson`
- `xbar_peri.gen.hjson` (L1) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `clock srcs` (L11) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `clk peri i` (L13) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `clock group` (L15) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `reset connections` (L17) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `rst peri ni` (L19) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `domain` (L22) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `clock connections` (L25) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `connections` (L33) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `main` (L35) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `nodes` (L66) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- `xbar_peri.hjson` (L1) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.hjson`
- `clock primary` (L7) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.hjson`
- `other clock list` (L8) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.hjson`
- `reset primary` (L9) - `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.hjson`

## Code Evidence

- `tlul_fifo_async` (L212) - `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv`
- `tb__xbar_connect.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\tb__xbar_connect.sv`
- `xbar_env_pkg__params.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_env_pkg__params.sv`
- `xbar_peri_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv`
- `xbar_peri_bind` (L6) - `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv`
- `tl_peri_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\tl_peri_pkg.sv`
- `xbar_peri.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv`
- `xbar_peri` (L31) - `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv`
- `tl_peri_pkg` (L68) - `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv`
- `tb__xbar_connect.sv` (L1) - `opentitan\hw\top_earlgrey\ip\xbar_peri\dv\autogen\tb__xbar_connect.sv`
- `xbar_env_pkg__params.sv` (L1) - `opentitan\hw\top_earlgrey\ip\xbar_peri\dv\autogen\xbar_env_pkg__params.sv`
- `xbar_peri_bind.sv` (L1) - `opentitan\hw\top_earlgrey\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv`
- `xbar_peri_bind` (L6) - `opentitan\hw\top_earlgrey\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv`
- `tl_peri_pkg.sv` (L1) - `opentitan\hw\top_earlgrey\ip\xbar_peri\rtl\autogen\tl_peri_pkg.sv`
- `xbar_peri.sv` (L1) - `opentitan\hw\top_earlgrey\ip\xbar_peri\rtl\autogen\xbar_peri.sv`
- `xbar_peri` (L39) - `opentitan\hw\top_earlgrey\ip\xbar_peri\rtl\autogen\xbar_peri.sv`
- `tb__xbar_connect.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip\xbar_peri\dv\autogen\tb__xbar_connect.sv`
- `xbar_env_pkg__params.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip\xbar_peri\dv\autogen\xbar_env_pkg__params.sv`
- `xbar_peri_bind.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv`
- `xbar_peri_bind` (L6) - `opentitan\hw\top_englishbreakfast\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv`
- `tl_peri_pkg.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\tl_peri_pkg.sv`
- `xbar_peri.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv`
- `xbar_peri` (L26) - `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv`
- `xbar_peri` (L1499) - `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
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
- `prim_alert_sender` (L268) - `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
- `prim_alert_pkg` (L11) - `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
- `prim_esc_pkg` (L12) - `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
- `prim_secded_inv_72_64_enc` (L39) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv`
- `prim_sec_anchor_flop` (L275) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv`
- `prim_packer_fifo` (L233) - `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_peri_bind.sv` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_peri_bind` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_peri.sv` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_peri` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_peri_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_peri_bind` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_peri` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_peri_bind.sv` | `opentitan\hw\top_earlgrey\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_peri_bind` | `opentitan\hw\top_earlgrey\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_peri.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_peri` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_peri.sv` | `opentitan\hw\top_earlgrey\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_peri` | `opentitan\hw\top_earlgrey\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `tb__xbar_connect.sv` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\dv\autogen\tb__xbar_connect.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_earlgrey\ip\xbar_peri\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `tl_peri_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\tl_peri_pkg.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `tlul_fifo_async` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\tb__xbar_connect.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `tl_peri_pkg` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `tb__xbar_connect.sv` | `opentitan\hw\top_earlgrey\ip\xbar_peri\dv\autogen\tb__xbar_connect.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `tl_peri_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\tl_peri_pkg.sv` |
| `spec_component_matches_code` | `component:xbar_peri` | `tl_peri_pkg.sv` | `opentitan\hw\top_earlgrey\ip\xbar_peri\rtl\autogen\tl_peri_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `top_racl_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `prim_pad_wrapper_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `tlul_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `aes` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `aon_timer` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `top_racl_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_pad_wrapper_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tlul_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `aes` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `aon_timer` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `top_racl_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `prim_pad_wrapper_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `tlul_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `aes` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `aon_timer` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `xbar_peri.gen.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `top_racl_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_pad_wrapper_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tlul_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `aes` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `aon_timer` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |

## Retrieval Guidance

- When a code-only query mentions `xbar_peri`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
