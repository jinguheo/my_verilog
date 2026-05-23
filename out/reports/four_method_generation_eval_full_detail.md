# Four-Method Verilog Generation Evaluation - Full Detail

Generated: 2026-05-09T20:57:15

## Overall

| Method | hit@1 | hit@3 | hit@5 | MRR | Status counts |
|---|---:|---:|---:|---:|---|
| 1. Parser + LSP | 0.9481 | 1.0000 | 1.0000 | 0.9675 | HIT@1=73, HIT@3=4 |
| 2. Parser + LSP + Manticore | 0.8312 | 0.8961 | 0.9481 | 0.8645 | HIT@1=64, HIT@3=5, HIT@5=4, MISS=4 |
| 3. KG | 0.9481 | 0.9870 | 1.0000 | 0.9658 | HIT@1=73, HIT@3=3, HIT@5=1 |
| 4. Graphify | 0.9740 | 0.9740 | 0.9740 | 0.9740 | HIT@1=75, MISS=2 |

## Per-Question Detail

| Task | Level | Gold | Parser/LSP | Manticore | KG | Graphify |
|---|---|---|---|---|---|---|
| genctx_001_top_darjeeling | L3 | top_darjeeling | HIT@1 / r1 / top1=top_darjeeling | HIT@1 / r1 / top1=top_darjeeling | HIT@1 / r1 / top1=top_darjeeling | HIT@1 / r1 / top1=top_darjeeling |
| genctx_002_top_earlgrey | L4 | top_earlgrey | HIT@1 / r1 / top1=top_earlgrey | HIT@5 / r5 / top1=pinmux_jtag_breakout | HIT@5 / r5 / top1=pinmux_jtag_breakout | HIT@1 / r1 / top1=top_earlgrey |
| genctx_003_chip_darjeeling_asic | L5 | chip_darjeeling_asic | HIT@1 / r1 / top1=chip_darjeeling_asic | HIT@1 / r1 / top1=chip_darjeeling_asic | HIT@1 / r1 / top1=chip_darjeeling_asic | HIT@1 / r1 / top1=chip_darjeeling_asic |
| genctx_004_top_englishbreakfast | L3 | top_englishbreakfast | HIT@1 / r1 / top1=top_englishbreakfast | HIT@1 / r1 / top1=top_englishbreakfast | HIT@1 / r1 / top1=top_englishbreakfast | HIT@1 / r1 / top1=top_englishbreakfast |
| genctx_005_spi_device | L4 | spi_device | HIT@1 / r1 / top1=spi_device | HIT@1 / r1 / top1=spi_device | HIT@1 / r1 / top1=spi_device | HIT@1 / r1 / top1=spi_device |
| genctx_006_ast | L5 | ast | HIT@1 / r1 / top1=ast | HIT@3 / r3 / top1=prim_flop_2sync | HIT@1 / r1 / top1=ast | HIT@1 / r1 / top1=ast |
| genctx_007_flash_ctrl | L3 | flash_ctrl | HIT@1 / r1 / top1=flash_ctrl | HIT@1 / r1 / top1=flash_ctrl | HIT@1 / r1 / top1=flash_ctrl | HIT@1 / r1 / top1=flash_ctrl |
| genctx_008_flash_ctrl | L4 | flash_ctrl | HIT@3 / r3 / top1=flash_ctrl_region_cfg | HIT@3 / r3 / top1=flash_ctrl_region_cfg | HIT@3 / r3 / top1=flash_ctrl_region_cfg | HIT@1 / r1 / top1=flash_ctrl |
| genctx_009_chip_earlgrey_cw310 | L5 | chip_earlgrey_cw310 | HIT@1 / r1 / top1=chip_earlgrey_cw310 | HIT@1 / r1 / top1=chip_earlgrey_cw310 | HIT@1 / r1 / top1=chip_earlgrey_cw310 | HIT@1 / r1 / top1=chip_earlgrey_cw310 |
| genctx_010_chip_earlgrey_cw340 | L3 | chip_earlgrey_cw340 | HIT@1 / r1 / top1=chip_earlgrey_cw340 | HIT@1 / r1 / top1=chip_earlgrey_cw340 | HIT@1 / r1 / top1=chip_earlgrey_cw340 | HIT@1 / r1 / top1=chip_earlgrey_cw340 |
| genctx_011_otp_ctrl | L4 | otp_ctrl | HIT@1 / r1 / top1=otp_ctrl | HIT@1 / r1 / top1=otp_ctrl | HIT@1 / r1 / top1=otp_ctrl | HIT@1 / r1 / top1=otp_ctrl |
| genctx_012_usb_fs_nb_pe | L5 | usb_fs_nb_pe | HIT@1 / r1 / top1=usb_fs_nb_pe | HIT@1 / r1 / top1=usb_fs_nb_pe | HIT@1 / r1 / top1=usb_fs_nb_pe | HIT@1 / r1 / top1=usb_fs_nb_pe |
| genctx_013_otp_ctrl | L3 | otp_ctrl | HIT@1 / r1 / top1=otp_ctrl | HIT@1 / r1 / top1=otp_ctrl | HIT@1 / r1 / top1=otp_ctrl | HIT@1 / r1 / top1=otp_ctrl |
| genctx_014_entropy_src_core | L4 | entropy_src_core | HIT@1 / r1 / top1=entropy_src_core | HIT@1 / r1 / top1=entropy_src_core | HIT@1 / r1 / top1=entropy_src_core | HIT@1 / r1 / top1=entropy_src_core |
| genctx_015_rv_core_ibex | L5 | rv_core_ibex | HIT@1 / r1 / top1=rv_core_ibex | HIT@1 / r1 / top1=rv_core_ibex | HIT@1 / r1 / top1=rv_core_ibex | HIT@1 / r1 / top1=rv_core_ibex |
| genctx_016_rv_core_ibex | L3 | rv_core_ibex | HIT@1 / r1 / top1=rv_core_ibex | HIT@1 / r1 / top1=rv_core_ibex | HIT@1 / r1 / top1=rv_core_ibex | HIT@1 / r1 / top1=rv_core_ibex |
| genctx_017_rv_core_ibex | L4 | rv_core_ibex | HIT@1 / r1 / top1=rv_core_ibex | HIT@1 / r1 / top1=rv_core_ibex | HIT@1 / r1 / top1=rv_core_ibex | HIT@1 / r1 / top1=rv_core_ibex |
| genctx_018_ast | L5 | ast | HIT@1 / r1 / top1=ast | HIT@3 / r3 / top1=prim_flop_2sync | HIT@1 / r1 / top1=ast | HIT@1 / r1 / top1=ast |
| genctx_019_chip_earlgrey_asic | L3 | chip_earlgrey_asic | HIT@1 / r1 / top1=chip_earlgrey_asic | HIT@1 / r1 / top1=chip_earlgrey_asic | HIT@1 / r1 / top1=chip_earlgrey_asic | HIT@1 / r1 / top1=chip_earlgrey_asic |
| genctx_020_usbdev | L4 | usbdev | HIT@1 / r1 / top1=usbdev | HIT@3 / r3 / top1=prim_edge_detector | HIT@1 / r1 / top1=usbdev | HIT@1 / r1 / top1=usbdev |
| genctx_021_pwrmgr | L5 | pwrmgr | HIT@1 / r1 / top1=pwrmgr | MISS / miss / top1=prim_esc_receiver | HIT@1 / r1 / top1=pwrmgr | HIT@1 / r1 / top1=pwrmgr |
| genctx_022_otbn_core | L3 | otbn_core | HIT@1 / r1 / top1=otbn_core | HIT@1 / r1 / top1=otbn_core | HIT@1 / r1 / top1=otbn_core | HIT@1 / r1 / top1=otbn_core |
| genctx_023_clkmgr | L4 | clkmgr | HIT@1 / r1 / top1=clkmgr | MISS / miss / top1=prim_clock_div | HIT@1 / r1 / top1=clkmgr | HIT@1 / r1 / top1=clkmgr |
| genctx_024_clkmgr | L5 | clkmgr | HIT@1 / r1 / top1=clkmgr | MISS / miss / top1=clkmgr_reg_top | HIT@1 / r1 / top1=clkmgr | HIT@1 / r1 / top1=clkmgr |
| genctx_025_pwrmgr | L3 | pwrmgr | HIT@1 / r1 / top1=pwrmgr | HIT@1 / r1 / top1=pwrmgr | HIT@1 / r1 / top1=pwrmgr | HIT@1 / r1 / top1=pwrmgr |
| genctx_026_pwrmgr | L4 | pwrmgr | HIT@1 / r1 / top1=pwrmgr | HIT@5 / r5 / top1=prim_esc_receiver | HIT@1 / r1 / top1=pwrmgr | HIT@1 / r1 / top1=pwrmgr |
| genctx_027_rv_dm | L5 | rv_dm | HIT@1 / r1 / top1=rv_dm | HIT@1 / r1 / top1=rv_dm | HIT@1 / r1 / top1=rv_dm | HIT@1 / r1 / top1=rv_dm |
| genctx_028_sysrst_ctrl | L3 | sysrst_ctrl | HIT@1 / r1 / top1=sysrst_ctrl | HIT@1 / r1 / top1=sysrst_ctrl | HIT@1 / r1 / top1=sysrst_ctrl | HIT@1 / r1 / top1=sysrst_ctrl |
| genctx_029_kmac | L4 | kmac | HIT@3 / r2 / top1=kmac_core | HIT@5 / r4 / top1=prim_intr_hw | HIT@3 / r2 / top1=kmac_core | HIT@1 / r1 / top1=kmac |
| genctx_030_keymgr_dpe | L5 | keymgr_dpe | HIT@1 / r1 / top1=keymgr_dpe | HIT@1 / r1 / top1=keymgr_dpe | HIT@1 / r1 / top1=keymgr_dpe | HIT@1 / r1 / top1=keymgr_dpe |
| genctx_031_keymgr | L3 | keymgr | HIT@1 / r1 / top1=keymgr | HIT@1 / r1 / top1=keymgr | HIT@1 / r1 / top1=keymgr | HIT@1 / r1 / top1=keymgr |
| genctx_032_flash_phy_core | L4 | flash_phy_core | HIT@1 / r1 / top1=flash_phy_core | HIT@1 / r1 / top1=flash_phy_core | HIT@1 / r1 / top1=flash_phy_core | HIT@1 / r1 / top1=flash_phy_core |
| genctx_033_flash_phy_core | L5 | flash_phy_core | HIT@1 / r1 / top1=flash_phy_core | HIT@1 / r1 / top1=flash_phy_core | HIT@1 / r1 / top1=flash_phy_core | HIT@1 / r1 / top1=flash_phy_core |
| genctx_034_flash_phy_core | L3 | flash_phy_core | HIT@1 / r1 / top1=flash_phy_core | HIT@1 / r1 / top1=flash_phy_core | HIT@1 / r1 / top1=flash_phy_core | HIT@1 / r1 / top1=flash_phy_core |
| genctx_035_flash_phy_rd | L4 | flash_phy_rd | HIT@1 / r1 / top1=flash_phy_rd | HIT@5 / r4 / top1=flash_phy_rd_buf_dep | HIT@1 / r1 / top1=flash_phy_rd | HIT@1 / r1 / top1=flash_phy_rd |
| genctx_036_flash_phy_rd | L5 | flash_phy_rd | HIT@1 / r1 / top1=flash_phy_rd | HIT@1 / r1 / top1=flash_phy_rd | HIT@1 / r1 / top1=flash_phy_rd | HIT@1 / r1 / top1=flash_phy_rd |
| genctx_037_flash_phy_rd | L3 | flash_phy_rd | HIT@1 / r1 / top1=flash_phy_rd | HIT@1 / r1 / top1=flash_phy_rd | HIT@1 / r1 / top1=flash_phy_rd | HIT@1 / r1 / top1=flash_phy_rd |
| genctx_038_kmac_reduced | L4 | kmac_reduced | HIT@1 / r1 / top1=kmac_reduced | HIT@1 / r1 / top1=kmac_reduced | HIT@1 / r1 / top1=kmac_reduced | HIT@1 / r1 / top1=kmac_reduced |
| genctx_039_lc_ctrl_fsm | L5 | lc_ctrl_fsm | HIT@1 / r1 / top1=lc_ctrl_fsm | HIT@1 / r1 / top1=lc_ctrl_fsm | HIT@1 / r1 / top1=lc_ctrl_fsm | HIT@1 / r1 / top1=lc_ctrl_fsm |
| genctx_040_sram_ctrl | L3 | sram_ctrl | HIT@1 / r1 / top1=sram_ctrl | HIT@1 / r1 / top1=sram_ctrl | HIT@1 / r1 / top1=sram_ctrl | HIT@1 / r1 / top1=sram_ctrl |
| genctx_041_aes_core | L4 | aes_core | HIT@1 / r1 / top1=aes_core | HIT@1 / r1 / top1=aes_core | HIT@1 / r1 / top1=aes_core | HIT@1 / r1 / top1=aes_core |
| genctx_042_i2c_core | L5 | i2c_core | HIT@1 / r1 / top1=i2c_core | HIT@1 / r1 / top1=i2c_core | HIT@1 / r1 / top1=i2c_core | HIT@1 / r1 / top1=i2c_core |
| genctx_043_otbn | L3 | otbn | HIT@1 / r1 / top1=otbn | HIT@1 / r1 / top1=otbn | HIT@1 / r1 / top1=otbn | HIT@1 / r1 / top1=otbn |
| genctx_044_csrng_core | L4 | csrng_core | HIT@1 / r1 / top1=csrng_core | HIT@1 / r1 / top1=csrng_core | HIT@1 / r1 / top1=csrng_core | HIT@1 / r1 / top1=csrng_core |
| genctx_045_otp_ctrl_dai | L5 | otp_ctrl_dai | HIT@1 / r1 / top1=otp_ctrl_dai | HIT@1 / r1 / top1=otp_ctrl_dai | HIT@1 / r1 / top1=otp_ctrl_dai | HIT@1 / r1 / top1=otp_ctrl_dai |
| genctx_046_otp_ctrl_dai | L3 | otp_ctrl_dai | HIT@1 / r1 / top1=otp_ctrl_dai | HIT@1 / r1 / top1=otp_ctrl_dai | HIT@1 / r1 / top1=otp_ctrl_dai | HIT@1 / r1 / top1=otp_ctrl_dai |
| genctx_047_otp_ctrl_dai | L4 | otp_ctrl_dai | HIT@1 / r1 / top1=otp_ctrl_dai | HIT@1 / r1 / top1=otp_ctrl_dai | HIT@1 / r1 / top1=otp_ctrl_dai | HIT@1 / r1 / top1=otp_ctrl_dai |
| genctx_048_lc_ctrl | L5 | lc_ctrl | HIT@1 / r1 / top1=lc_ctrl | HIT@1 / r1 / top1=lc_ctrl | HIT@1 / r1 / top1=lc_ctrl | HIT@1 / r1 / top1=lc_ctrl |
| genctx_049_otp_ctrl_part_buf | L3 | otp_ctrl_part_buf | HIT@1 / r1 / top1=otp_ctrl_part_buf | HIT@1 / r1 / top1=otp_ctrl_part_buf | HIT@1 / r1 / top1=otp_ctrl_part_buf | HIT@1 / r1 / top1=otp_ctrl_part_buf |
| genctx_050_otp_ctrl_part_buf | L4 | otp_ctrl_part_buf | HIT@1 / r1 / top1=otp_ctrl_part_buf | HIT@1 / r1 / top1=otp_ctrl_part_buf | HIT@1 / r1 / top1=otp_ctrl_part_buf | HIT@1 / r1 / top1=otp_ctrl_part_buf |
| genctx_051_otp_ctrl_part_buf | L5 | otp_ctrl_part_buf | HIT@1 / r1 / top1=otp_ctrl_part_buf | HIT@1 / r1 / top1=otp_ctrl_part_buf | HIT@1 / r1 / top1=otp_ctrl_part_buf | HIT@1 / r1 / top1=otp_ctrl_part_buf |
| genctx_052_keymgr_dpe_ctrl | L3 | keymgr_dpe_ctrl | HIT@1 / r1 / top1=keymgr_dpe_ctrl | HIT@1 / r1 / top1=keymgr_dpe_ctrl | HIT@1 / r1 / top1=keymgr_dpe_ctrl | HIT@1 / r1 / top1=keymgr_dpe_ctrl |
| genctx_053_ast_clks_byp | L4 | ast_clks_byp | HIT@1 / r1 / top1=ast_clks_byp | HIT@1 / r1 / top1=ast_clks_byp | HIT@1 / r1 / top1=ast_clks_byp | HIT@1 / r1 / top1=ast_clks_byp |
| genctx_054_clkmgr | L5 | clkmgr | HIT@1 / r1 / top1=clkmgr | MISS / miss / top1=clkmgr_clk_status | HIT@1 / r1 / top1=clkmgr | HIT@1 / r1 / top1=clkmgr |
| genctx_055_otbn_alu_bignum | L3 | otbn_alu_bignum | HIT@1 / r1 / top1=otbn_alu_bignum | HIT@1 / r1 / top1=otbn_alu_bignum | HIT@1 / r1 / top1=otbn_alu_bignum | HIT@1 / r1 / top1=otbn_alu_bignum |
| genctx_056_soc_proxy | L4 | soc_proxy | HIT@1 / r1 / top1=soc_proxy | HIT@1 / r1 / top1=soc_proxy | HIT@1 / r1 / top1=soc_proxy | HIT@1 / r1 / top1=soc_proxy |
| genctx_057_chip_englishbreakfast_cw305 | L5 | chip_englishbreakfast_cw305 | HIT@1 / r1 / top1=chip_englishbreakfast_cw305 | HIT@1 / r1 / top1=chip_englishbreakfast_cw305 | HIT@1 / r1 / top1=chip_englishbreakfast_cw305 | HIT@1 / r1 / top1=chip_englishbreakfast_cw305 |
| genctx_058_clkmgr_reg_top | L3 | clkmgr_reg_top | HIT@1 / r1 / top1=clkmgr_reg_top | HIT@1 / r1 / top1=clkmgr_reg_top | HIT@1 / r1 / top1=clkmgr_reg_top | HIT@1 / r1 / top1=clkmgr_reg_top |
| genctx_059_flash_ctrl_lcmgr | L4 | flash_ctrl_lcmgr | HIT@1 / r1 / top1=flash_ctrl_lcmgr | HIT@1 / r1 / top1=flash_ctrl_lcmgr | HIT@1 / r1 / top1=flash_ctrl_lcmgr | HIT@1 / r1 / top1=flash_ctrl_lcmgr |
| genctx_060_flash_ctrl_lcmgr | L5 | flash_ctrl_lcmgr | HIT@1 / r1 / top1=flash_ctrl_lcmgr | HIT@1 / r1 / top1=flash_ctrl_lcmgr | HIT@1 / r1 / top1=flash_ctrl_lcmgr | HIT@1 / r1 / top1=flash_ctrl_lcmgr |
| genctx_061_dma | L3 | dma | HIT@1 / r1 / top1=dma | HIT@1 / r1 / top1=dma | HIT@1 / r1 / top1=dma | HIT@1 / r1 / top1=dma |
| genctx_062_uart | L4 | uart | HIT@3 / r3 / top1=uart_reg_top | HIT@3 / r3 / top1=uart_reg_top | HIT@3 / r3 / top1=uart_reg_top | HIT@1 / r1 / top1=uart |
| existing_063 | L3 | dma | HIT@1 / r1 / top1=dma | HIT@1 / r1 / top1=dma | HIT@1 / r1 / top1=dma | HIT@1 / r1 / top1=dma |
| existing_064 | L3 | ac_range_check_reg_top | HIT@1 / r1 / top1=ac_range_check_reg_top | HIT@1 / r1 / top1=ac_range_check_reg_top | HIT@1 / r1 / top1=ac_range_check_reg_top | HIT@1 / r1 / top1=ac_range_check_reg_top |
| existing_065 | L3 | ac_range_check | HIT@1 / r1 / top1=ac_range_check | HIT@1 / r1 / top1=ac_range_check | HIT@1 / r1 / top1=ac_range_check | HIT@1 / r1 / top1=ac_range_check |
| existing_066 | L3 | keymgr_dpe_reg_top | HIT@1 / r1 / top1=keymgr_dpe_reg_top | HIT@1 / r1 / top1=keymgr_dpe_reg_top | HIT@1 / r1 / top1=keymgr_dpe_reg_top | HIT@1 / r1 / top1=keymgr_dpe_reg_top |
| existing_067 | L3 | keymgr_reg_top | HIT@1 / r1 / top1=keymgr_reg_top | HIT@1 / r1 / top1=keymgr_reg_top | HIT@1 / r1 / top1=keymgr_reg_top | HIT@1 / r1 / top1=keymgr_reg_top |
| existing_068 | L4 | tlul_adapter_sram | HIT@1 / r1 / top1=tlul_adapter_sram | HIT@1 / r1 / top1=tlul_adapter_sram | HIT@1 / r1 / top1=tlul_adapter_sram | HIT@1 / r1 / top1=tlul_adapter_sram |
| existing_069 | L4 | uart_core | HIT@1 / r1 / top1=uart_core | HIT@1 / r1 / top1=uart_core | HIT@1 / r1 / top1=uart_core | HIT@1 / r1 / top1=uart_core |
| existing_070 | L4 | aes_dom_inverse_gf2p8 | HIT@1 / r1 / top1=aes_dom_inverse_gf2p8 | HIT@1 / r1 / top1=aes_dom_inverse_gf2p8 | HIT@1 / r1 / top1=aes_dom_inverse_gf2p8 | MISS / miss / top1=Extension |
| existing_071 | L4 | mbx | HIT@1 / r1 / top1=mbx | HIT@1 / r1 / top1=mbx | HIT@1 / r1 / top1=mbx | HIT@1 / r1 / top1=mbx |
| existing_072 | L4 | rv_dm_dmi_gate | HIT@1 / r1 / top1=rv_dm_dmi_gate | HIT@1 / r1 / top1=rv_dm_dmi_gate | HIT@1 / r1 / top1=rv_dm_dmi_gate | HIT@1 / r1 / top1=rv_dm_dmi_gate |
| existing_073 | L5 | adc_ctrl_core | HIT@1 / r1 / top1=adc_ctrl_core | HIT@1 / r1 / top1=adc_ctrl_core | HIT@1 / r1 / top1=adc_ctrl_core | HIT@1 / r1 / top1=adc_ctrl_core |
| existing_074 | L5 | ascon | HIT@3 / r3 / top1=prim_ascon_duplex | HIT@1 / r1 / top1=ascon | HIT@1 / r1 / top1=ascon | HIT@1 / r1 / top1=ascon |
| existing_075 | L5 | aes_dom_inverse_gf2p4 | HIT@1 / r1 / top1=aes_dom_inverse_gf2p4 | HIT@1 / r1 / top1=aes_dom_inverse_gf2p4 | HIT@1 / r1 / top1=aes_dom_inverse_gf2p4 | MISS / miss / top1=# NOTE: This list is likely to become out of date as the codebase evolves |
| existing_076 | L5 | usb_clk | HIT@1 / r1 / top1=usb_clk | HIT@1 / r1 / top1=usb_clk | HIT@1 / r1 / top1=usb_clk | HIT@1 / r1 / top1=usb_clk |
| existing_077 | L5 | xbar_main | HIT@1 / r1 / top1=xbar_main | HIT@1 / r1 / top1=xbar_main | HIT@1 / r1 / top1=xbar_main | HIT@1 / r1 / top1=xbar_main |

## Miss Details

### 1. Parser + LSP

No top-5 misses.

### 2. Parser + LSP + Manticore

- `genctx_021_pwrmgr` gold `pwrmgr` level `L5`
  - Question: Write a difficult spec-to-RTL generation brief for a module equivalent to `pwrmgr`. The generated RTL must preserve labels uart, child-role decomposition prim_flop_2sync, prim_clock_buf, prim_esc_receiver, prim_clock_timeout, and interface compatibility via clk_slow_i, clk_i, rst_slow_ni, rst_ni. Which existing module must anchor the context?
  - Top-5: prim_esc_receiver score=454.795; prim_esc_receiver score=453.33; prim_clock_timeout score=396.819; prim_clock_timeout score=395.44; prim_flop_2sync score=385.346
- `genctx_023_clkmgr` gold `clkmgr` level `L4`
  - Question: Create an implementation plan for a replacement `clkmgr` block that preserves child dependencies prim_clock_buf, prim_mubi4_sync, prim_clock_div and the key ports clk_i, rst_ni, rst_shadowed_ni. Which RTL module is the primary source of truth?
  - Top-5: prim_clock_div score=376.344; prim_clock_div score=375.153; prim_mubi4_sync score=368.187; prim_mubi4_sync score=366.869; prim_clock_div score=343.123
- `genctx_024_clkmgr` gold `clkmgr` level `L5`
  - Question: Write a difficult spec-to-RTL generation brief for a module equivalent to `clkmgr`. The generated RTL must preserve labels uart, child-role decomposition prim_clock_buf, prim_mubi4_sync, prim_clock_div, clkmgr_reg_top, and interface compatibility via clk_i, rst_ni, rst_shadowed_ni, clk_main_i. Which existing module must anchor the context?
  - Top-5: clkmgr_reg_top score=420.11; clkmgr_reg_top score=408.447; clkmgr_reg_top score=402.828; prim_clock_div score=376.344; prim_clock_div score=375.153
- `genctx_054_clkmgr` gold `clkmgr` level `L5`
  - Question: Write a difficult spec-to-RTL generation brief for a module equivalent to `clkmgr`. The generated RTL must preserve labels uart, child-role decomposition prim_clock_buf, clkmgr_reg_top, clkmgr_root_ctrl, clkmgr_clk_status, and interface compatibility via clk_i, rst_ni, rst_shadowed_ni, clk_main_i. Which existing module must anchor the context?
  - Top-5: clkmgr_clk_status score=427.167; clkmgr_clk_status score=426.224; clkmgr_clk_status score=426.224; clkmgr_clk_status score=426.224; clkmgr_reg_top score=416.049

### 3. KG

No top-5 misses.

### 4. Graphify

- `existing_070` gold `aes_dom_inverse_gf2p8` level `L4`
  - Question: Prepare a generation plan for a replacement or extension of `aes_dom_inverse_gf2p8` that preserves hierarchy, interface intent, and likely child dependencies.
  - Top-5: Extension score=13.5; extension score=13.5; Checks that loops will likely be properly cleared from loop stack score=13.0; prepare_verilogeval_generation score=13.0; Rewrite small SV constructs that current Icarus rejects in oracle refs score=9.5
- `existing_075` gold `aes_dom_inverse_gf2p4` level `L5`
  - Question: Write a design-generation brief for building a new module inspired by `aes_dom_inverse_gf2p4`, including preserved interfaces, child-role decomposition, and likely review risks.
  - Top-5: # NOTE: This list is likely to become out of date as the codebase evolves score=6.5; # TODO: This is an implicit assignment of alerts to reg interfaces score=6.5; # TODO: add new_node score=6.5; .__new__() score=6.5; ._interfaces() score=6.5

## Notes

- Direct functional pass rate still uses canonical RTL candidates, so it is a harness check, not true generated-code quality.
- This full-detail report measures whether each method supplies the correct source RTL context for difficult generation prompts.
