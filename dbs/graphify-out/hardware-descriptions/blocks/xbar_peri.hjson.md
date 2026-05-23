# Hardware Description: xbar_peri.hjson

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `xbar_peri.hjson`
- `approved_label`: `pending:xbar_peri.hjson`
- `doc_anchor`: `xbar_peri.hjson`
- `module_name_prefix`: `xbar_peri.hjson`
- `bridge_edge_count`: 48

## Inferred Hardware Role

`xbar_peri.hjson` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 81
- Code categories: rtl: 36, dv: 12
- Bridge relations: spec_path_matches_code_path: 48

## Spec Anchors

- `xbar_peri.hjson` (L1) - `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `clock primary` (L6) - `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `other clock list` (L7) - `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `reset primary` (L8) - `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `other reset list` (L9) - `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `nodes` (L11) - `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `addr space` (L14) - `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `clock` (L15) - `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `xbar` (L17) - `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `pipeline` (L18) - `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `connections` (L136) - `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `xbar_peri.hjson` (L1) - `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `clock primary` (L6) - `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `other clock list` (L7) - `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `reset primary` (L8) - `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `other reset list` (L9) - `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `nodes` (L11) - `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `addr space` (L14) - `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `clock` (L15) - `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `xbar` (L17) - `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `pipeline` (L18) - `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `connections` (L184) - `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `xbar_peri.hjson` (L1) - `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `clock primary` (L6) - `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `other clock list` (L7) - `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `reset primary` (L8) - `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `other reset list` (L9) - `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `nodes` (L11) - `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `addr space` (L14) - `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `clock` (L15) - `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `xbar` (L17) - `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `pipeline` (L18) - `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `connections` (L94) - `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`

## Code Evidence

- `prim_flop_en` (L269) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `prim_ram_1p_adv` (L1487) - `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
- `tlul_cmd_intg_gen` (L46) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv`
- `dma` (L2221) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `keymgr_dpe` (L1905) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `tlul_jtag_dtm` (L1340) - `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
- `mbx` (L2257) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `prim_onehot_enc` (L128) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `tlul_fifo_async` (L212) - `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv`
- `tb__xbar_connect.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\tb__xbar_connect.sv`
- `xbar_env_pkg__params.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_env_pkg__params.sv`
- `xbar_peri_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv`
- `xbar_peri_bind` (L6) - `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv`
- `tl_peri_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\tl_peri_pkg.sv`
- `xbar_peri.sv` (L1) - `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv`
- `xbar_peri` (L31) - `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv`
- `prim_alert_sender` (L268) - `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
- `prim_alert_pkg` (L11) - `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
- `prim_esc_pkg` (L12) - `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
- `prim_secded_inv_72_64_enc` (L39) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv`
- `prim_sec_anchor_flop` (L275) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv`
- `prim_packer_fifo` (L233) - `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv`
- `adc_ctrl` (L2047) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
- `csrng` (L2617) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
- `BUFG` (L92) - `opentitan\hw\top_englishbreakfast\rtl\clkgen_xil7series.sv`
- `prim_mubi_pkg` (L905) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `prim_esc_receiver` (L283) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `prim_arbiter_fixed` (L58) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv`
- `prim_arbiter_tree` (L163) - `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv`
- `prim_count` (L240) - `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv`
- `prim_secded_hamming_72_64_enc` (L775) - `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv`
- `prim_secded_hamming_76_68_enc` (L334) - `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tlul_fifo_async` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\tb__xbar_connect.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri_bind` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tl_peri_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\tl_peri_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tlul_fifo_async` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\tb__xbar_connect.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri_bind` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tl_peri_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\tl_peri_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `BUFG` | `opentitan\hw\top_englishbreakfast\rtl\clkgen_xil7series.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_mubi_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_esc_receiver` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_arbiter_fixed` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_arbiter_tree` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_count` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_secded_hamming_72_64_enc` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_secded_hamming_76_68_enc` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tlul_fifo_async` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\tb__xbar_connect.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri_bind` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tl_peri_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\tl_peri_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |

## Retrieval Guidance

- When a code-only query mentions `xbar_peri.hjson`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
