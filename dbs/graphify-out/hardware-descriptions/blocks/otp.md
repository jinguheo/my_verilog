# Hardware Description: otp

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `otp`
- `approved_label`: `pending:otp`
- `doc_anchor`: `otp`
- `module_name_prefix`: `otp`
- `bridge_edge_count`: 208

## Inferred Hardware Role

`otp` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 344
- Code categories: rtl: 208, other_code: 59
- Bridge relations: spec_path_matches_code_path: 208

## Spec Anchors

- `otp_ctrl_img_creator_sw_cfg.hjson` (L1) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_creator_sw_cfg.hjson`
- `partitions` (L11) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_creator_sw_cfg.hjson`
- `items` (L14) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_creator_sw_cfg.hjson`
- `otp_ctrl_img_dev.hjson` (L1) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`
- `partitions` (L11) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`
- `lock` (L14) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`
- `items` (L15) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`
- `state` (L58) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`
- `count` (L61) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_dev.hjson`
- `otp_ctrl_img_hw_cfg.hjson` (L1) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_hw_cfg.hjson`
- `partitions` (L11) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_hw_cfg.hjson`
- `lock` (L16) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_hw_cfg.hjson`
- `items` (L17) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_hw_cfg.hjson`
- `otp_ctrl_img_owner_sw_cfg.hjson` (L1) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_owner_sw_cfg.hjson`
- `partitions` (L11) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_owner_sw_cfg.hjson`
- `items` (L14) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_owner_sw_cfg.hjson`
- `otp_ctrl_img_prod.hjson` (L1) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_prod.hjson`
- `partitions` (L11) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_prod.hjson`
- `lock` (L14) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_prod.hjson`
- `items` (L15) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_prod.hjson`
- `state` (L58) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_prod.hjson`
- `count` (L61) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_prod.hjson`
- `otp_ctrl_img_raw.hjson` (L1) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_raw.hjson`
- `partitions` (L11) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_raw.hjson`
- `state` (L16) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_raw.hjson`
- `count` (L19) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_raw.hjson`
- `otp_ctrl_img_rma.hjson` (L1) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_rma.hjson`
- `partitions` (L11) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_rma.hjson`
- `lock` (L14) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_rma.hjson`
- `items` (L15) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_rma.hjson`
- `state` (L58) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_rma.hjson`
- `count` (L61) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_rma.hjson`
- `otp_ctrl_img_test_locked0.hjson` (L1) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_test_locked0.hjson`
- `partitions` (L11) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_test_locked0.hjson`
- `items` (L14) - `opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_test_locked0.hjson`

## Code Evidence

- `alert_handler.rs` (L1) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `AlertClassRegs` (L14) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `AlertRegs` (L24) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `AlertClass` (L48) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.index()` (L57) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.from_index()` (L67) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `AlertEnable` (L80) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `AlertEscalate` (L88) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `AlertClassConfig` (L96) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.default()` (L105) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.default()` (L117) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.crc32()` (L133) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.try_new()` (L144) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.configure()` (L200) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.local_configure()` (L225) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.class_configure()` (L255) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `Crc32Add` (L318) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `u32` (L322) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.crc32_add()` (L323) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `[T; N]` (L328) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.crc32_add()` (L329) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.crc32_add()` (L335) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.crc32_add()` (L345) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `new_crc()` (L356) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `TestOtpAlertsDisabled` (L443) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.read32_offset()` (L447) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `TestOtpAlertsEnabled` (L467) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `.read32_offset()` (L471) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `test_new_crc()` (L496) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `test_crc_from_regs()` (L514) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `test_regs_from_otp()` (L519) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `test_crc_disabled()` (L527) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `test_crc_enabled()` (L537) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs`
- `alert_handler_regs.rs` (L1) - `opentitan\sw\host\opentitanlib\src\otp\alert_handler_regs.rs`
- `lc_state.rs` (L1) - `opentitan\sw\host\opentitanlib\src\otp\lc_state.rs`
- `LcSecded` (L12) - `opentitan\sw\host\opentitanlib\src\otp\lc_state.rs`
- `LcState` (L23) - `opentitan\sw\host\opentitanlib\src\otp\lc_state.rs`
- `LcStateVal` (L29) - `opentitan\sw\host\opentitanlib\src\otp\lc_state.rs`
- `.new()` (L38) - `opentitan\sw\host\opentitanlib\src\otp\lc_state.rs`
- `.bit_index()` (L47) - `opentitan\sw\host\opentitanlib\src\otp\lc_state.rs`
- `.ecc_encode()` (L53) - `opentitan\sw\host\opentitanlib\src\otp\lc_state.rs`
- `.ecc_byte_len()` (L74) - `opentitan\sw\host\opentitanlib\src\otp\lc_state.rs`
- `test_lc_state_deserialize()` (L92) - `opentitan\sw\host\opentitanlib\src\otp\lc_state.rs`
- `test_ecc_encode()` (L98) - `opentitan\sw\host\opentitanlib\src\otp\lc_state.rs`
- `mod.rs` (L1) - `opentitan\sw\host\opentitanlib\src\otp\mod.rs`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_creator_sw_cfg.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_dev.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_hw_cfg.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_owner_sw_cfg.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_prod.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_raw.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_rma.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked0.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked0.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked0.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked0.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked0.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked0.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked0.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked0.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked1.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked1.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked1.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked1.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked1.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked1.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked1.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_locked1.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_unlocked0.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_unlocked0.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_unlocked0.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_unlocked0.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_unlocked0.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_unlocked0.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_unlocked0.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `otp_ctrl_img_test_unlocked0.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |

## Retrieval Guidance

- When a code-only query mentions `otp`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
