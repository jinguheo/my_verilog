# Hardware Descriptions From Graphify

Intermediate documents generated from code/spec bridge evidence.
Each page includes spec excerpts, code inventory (grouped by rtl/dv/sva), and neighbor components.

- Components: 129
- Bridge edges: 12598
- Code references: 4517
- Spec references: 4280

## Components

| Component | Bridge edges | Code refs | Spec refs | Document |
|---|---:|---:|---:|---|
| `rstmgr` | 680 | 80 | 80 ✓ | [blocks/rstmgr.md](blocks/rstmgr.md) |
| `pinmux` | 664 | 80 | 80 ✓ | [blocks/pinmux.md](blocks/pinmux.md) |
| `rv_core_ibex` | 585 | 80 | 80 ✓ | [blocks/rv_core_ibex.md](blocks/rv_core_ibex.md) |
| `pwrmgr` | 568 | 80 | 80 ✓ | [blocks/pwrmgr.md](blocks/pwrmgr.md) |
| `clkmgr` | 563 | 80 | 80 ✓ | [blocks/clkmgr.md](blocks/clkmgr.md) |
| `otp_ctrl` | 528 | 80 | 80 ✓ | [blocks/otp_ctrl.md](blocks/otp_ctrl.md) |
| `gpio` | 520 | 80 | 80 ✓ | [blocks/gpio.md](blocks/gpio.md) |
| `rv_plic` | 456 | 80 | 80 ✓ | [blocks/rv_plic.md](blocks/rv_plic.md) |
| `flash_ctrl` | 408 | 80 | 80 ✓ | [blocks/flash_ctrl.md](blocks/flash_ctrl.md) |
| `ibex` | 370 | 80 | 80 ✓ | [blocks/ibex.md](blocks/ibex.md) |
| `prim` | 365 | 80 | 80 ✓ | [blocks/prim.md](blocks/prim.md) |
| `lowrisc_ibex` | 343 | 80 | 80 ✓ | [blocks/lowrisc_ibex.md](blocks/lowrisc_ibex.md) |
| `alert_handler` | 332 | 80 | 80 ✓ | [blocks/alert_handler.md](blocks/alert_handler.md) |
| `pwm` | 272 | 48 | 80 ✓ | [blocks/pwm.md](blocks/pwm.md) |
| `otp` | 208 | 75 | 80 ✓ | [blocks/otp.md](blocks/otp.md) |
| `racl_ctrl` | 206 | 38 | 80 ✓ | [blocks/racl_ctrl.md](blocks/racl_ctrl.md) |
| `unknown` | 196 | 25 | 44 ✓ | [blocks/unknown.md](blocks/unknown.md) |
| `lc_ctrl` | 192 | 44 | 80 ✓ | [blocks/lc_ctrl.md](blocks/lc_ctrl.md) |
| `ac_range_check` | 174 | 26 | 78 ✓ | [blocks/ac_range_check.md](blocks/ac_range_check.md) |
| `otbn` | 160 | 80 | 80 ✓ | [blocks/otbn.md](blocks/otbn.md) |
| `usbdev` | 120 | 56 | 80 ✓ | [blocks/usbdev.md](blocks/usbdev.md) |
| `xbar_main` | 119 | 46 | 58 ✓ | [blocks/xbar_main.md](blocks/xbar_main.md) |
| `mbx` | 117 | 37 | 80 ✓ | [blocks/mbx.md](blocks/mbx.md) |
| `xbar_peri` | 114 | 53 | 58 ✓ | [blocks/xbar_peri.md](blocks/xbar_peri.md) |
| `sensor_ctrl` | 113 | 21 | 54 ✓ | [blocks/sensor_ctrl.md](blocks/sensor_ctrl.md) |
| `aes` | 112 | 80 | 79 ✓ | [blocks/aes.md](blocks/aes.md) |
| `csrng` | 112 | 47 | 80 ✓ | [blocks/csrng.md](blocks/csrng.md) |
| `edn` | 112 | 42 | 78 ✓ | [blocks/edn.md](blocks/edn.md) |
| `entropy_src` | 112 | 75 | 80 ✓ | [blocks/entropy_src.md](blocks/entropy_src.md) |
| `hmac` | 112 | 80 | 76 ✓ | [blocks/hmac.md](blocks/hmac.md) |
| `i2c` | 112 | 44 | 80 ✓ | [blocks/i2c.md](blocks/i2c.md) |
| `keymgr` | 112 | 46 | 76 ✓ | [blocks/keymgr.md](blocks/keymgr.md) |
| `kmac` | 112 | 80 | 79 ✓ | [blocks/kmac.md](blocks/kmac.md) |
| `pattgen` | 112 | 40 | 75 ✓ | [blocks/pattgen.md](blocks/pattgen.md) |
| `rom_ctrl` | 112 | 80 | 66 ✓ | [blocks/rom_ctrl.md](blocks/rom_ctrl.md) |
| `rv_dm` | 112 | 77 | 73 ✓ | [blocks/rv_dm.md](blocks/rv_dm.md) |
| `spi_device` | 112 | 80 | 80 ✓ | [blocks/spi_device.md](blocks/spi_device.md) |
| `spi_host` | 112 | 54 | 80 ✓ | [blocks/spi_host.md](blocks/spi_host.md) |
| `uart` | 112 | 80 | 76 ✓ | [blocks/uart.md](blocks/uart.md) |
| `keymgr_dpe` | 107 | 35 | 74 ✓ | [blocks/keymgr_dpe.md](blocks/keymgr_dpe.md) |
| `adc_ctrl` | 104 | 32 | 75 ✓ | [blocks/adc_ctrl.md](blocks/adc_ctrl.md) |
| `sysrst_ctrl` | 104 | 80 | 70 ✓ | [blocks/sysrst_ctrl.md](blocks/sysrst_ctrl.md) |
| `sram_ctrl` | 102 | 30 | 73 ✓ | [blocks/sram_ctrl.md](blocks/sram_ctrl.md) |
| `rv_timer` | 98 | 26 | 72 ✓ | [blocks/rv_timer.md](blocks/rv_timer.md) |
| `ast` | 95 | 80 | 38 ✓ | [blocks/ast.md](blocks/ast.md) |
| `dma` | 95 | 23 | 80 ✓ | [blocks/dma.md](blocks/dma.md) |
| `soc_dbg_ctrl` | 95 | 23 | 62 ✓ | [blocks/soc_dbg_ctrl.md](blocks/soc_dbg_ctrl.md) |
| `aon_timer` | 93 | 21 | 74 ✓ | [blocks/aon_timer.md](blocks/aon_timer.md) |
| `ascon` | 92 | 28 | 65 ✓ | [blocks/ascon.md](blocks/ascon.md) |
| `tlul` | 80 | 70 | 46 ✓ | [blocks/tlul.md](blocks/tlul.md) |
| `lowrisc_ip` | 48 | 80 | 33 ✓ | [blocks/lowrisc_ip.md](blocks/lowrisc_ip.md) |
| `xbar_main.hjson` | 48 | 32 | 33 ✓ | [blocks/xbar_main.hjson.md](blocks/xbar_main.hjson.md) |
| `xbar_peri.hjson` | 48 | 32 | 33 ✓ | [blocks/xbar_peri.hjson.md](blocks/xbar_peri.hjson.md) |
| `soc_proxy` | 43 | 23 | 24 ✓ | [blocks/soc_proxy.md](blocks/soc_proxy.md) |
| `bitbanging` | 40 | 40 | 1  | [blocks/bitbanging.md](blocks/bitbanging.md) |
| `bootstrap` | 40 | 40 | 1  | [blocks/bootstrap.md](blocks/bootstrap.md) |
| `cosim` | 40 | 40 | 1  | [blocks/cosim.md](blocks/cosim.md) |
| `cs_registers` | 40 | 40 | 1  | [blocks/cs_registers.md](blocks/cs_registers.md) |
| `gen` | 40 | 40 | 1  | [blocks/gen.md](blocks/gen.md) |
| `icache` | 40 | 40 | 1  | [blocks/icache.md](blocks/icache.md) |
| `isa` | 40 | 40 | 1  | [blocks/isa.md](blocks/isa.md) |
| `ownership` | 40 | 40 | 1  | [blocks/ownership.md](blocks/ownership.md) |
| `rescue` | 40 | 40 | 1  | [blocks/rescue.md](blocks/rescue.md) |
| `rom` | 40 | 40 | 1  | [blocks/rom.md](blocks/rom.md) |
| `sigverify` | 40 | 40 | 1  | [blocks/sigverify.md](blocks/sigverify.md) |
| `targets` | 40 | 40 | 1  | [blocks/targets.md](blocks/targets.md) |
| `testplan` | 40 | 40 | 1  | [blocks/testplan.md](blocks/testplan.md) |
| `top_darjeeling` | 40 | 40 | 1  | [blocks/top_darjeeling.md](blocks/top_darjeeling.md) |
| `top_earlgrey` | 40 | 40 | 1  | [blocks/top_earlgrey.md](blocks/top_earlgrey.md) |
| `top_englishbreakfast` | 40 | 40 | 1  | [blocks/top_englishbreakfast.md](blocks/top_englishbreakfast.md) |
| `vendor` | 40 | 40 | 1  | [blocks/vendor.md](blocks/vendor.md) |
| `xbar_dbg` | 39 | 24 | 20 ✓ | [blocks/xbar_dbg.md](blocks/xbar_dbg.md) |
| `xbar_mbx` | 39 | 24 | 20 ✓ | [blocks/xbar_mbx.md](blocks/xbar_mbx.md) |
| `prim_prince` | 36 | 36 | 1  | [blocks/prim_prince.md](blocks/prim_prince.md) |
| `pmp` | 35 | 35 | 1  | [blocks/pmp.md](blocks/pmp.md) |
| `manifest` | 33 | 33 | 1  | [blocks/manifest.md](blocks/manifest.md) |
| `otp_macro` | 33 | 9 | 21 ✓ | [blocks/otp_macro.md](blocks/otp_macro.md) |
| `alert_esc_agent` | 32 | 25 | 12 ✓ | [blocks/alert_esc_agent.md](blocks/alert_esc_agent.md) |
| `xbar` | 31 | 31 | 12 ✓ | [blocks/xbar.md](blocks/xbar.md) |
| `prim_present` | 26 | 26 | 1  | [blocks/prim_present.md](blocks/prim_present.md) |
| `tracer` | 17 | 17 | 1  | [blocks/tracer.md](blocks/tracer.md) |
| `outgoing_alerts_englishbreakfast.hjson` | 16 | 16 | 6 ✓ | [blocks/outgoing_alerts_englishbreakfast.hjson.md](blocks/outgoing_alerts_englishbreakfast.hjson.md) |
| `pulp_riscv_dbg` | 16 | 80 | 11 ✓ | [blocks/pulp_riscv_dbg.md](blocks/pulp_riscv_dbg.md) |
| `xbar_dbg.hjson` | 16 | 16 | 11 ✓ | [blocks/xbar_dbg.hjson.md](blocks/xbar_dbg.hjson.md) |
| `xbar_mbx.hjson` | 16 | 16 | 11 ✓ | [blocks/xbar_mbx.hjson.md](blocks/xbar_mbx.hjson.md) |
| `fcov` | 14 | 14 | 1  | [blocks/fcov.md](blocks/fcov.md) |
| `shutdown` | 14 | 14 | 1  | [blocks/shutdown.md](blocks/shutdown.md) |
| `boot_log` | 10 | 10 | 1  | [blocks/boot_log.md](blocks/boot_log.md) |
| `ipconfig` | 10 | 10 | 1  | [blocks/ipconfig.md](blocks/ipconfig.md) |
| `prim_lfsr` | 9 | 9 | 1  | [blocks/prim_lfsr.md](blocks/prim_lfsr.md) |
| `chip_adc_ctrl_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_adc_ctrl_testplan.hjson.md](blocks/chip_adc_ctrl_testplan.hjson.md) |
| `chip_aes_testplan.hjson` | 8 | 8 | 10 ✓ | [blocks/chip_aes_testplan.hjson.md](blocks/chip_aes_testplan.hjson.md) |
| `chip_alert_handler_testplan.hjson` | 8 | 8 | 11 ✓ | [blocks/chip_alert_handler_testplan.hjson.md](blocks/chip_alert_handler_testplan.hjson.md) |
| `chip_aon_timer_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_aon_timer_testplan.hjson.md](blocks/chip_aon_timer_testplan.hjson.md) |
| `chip_clkmgr_testplan.hjson` | 8 | 8 | 10 ✓ | [blocks/chip_clkmgr_testplan.hjson.md](blocks/chip_clkmgr_testplan.hjson.md) |
| `chip_csrng_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_csrng_testplan.hjson.md](blocks/chip_csrng_testplan.hjson.md) |
| `chip_edn_testplan.hjson` | 8 | 8 | 11 ✓ | [blocks/chip_edn_testplan.hjson.md](blocks/chip_edn_testplan.hjson.md) |
| `chip_entropy_src_testplan.hjson` | 8 | 8 | 10 ✓ | [blocks/chip_entropy_src_testplan.hjson.md](blocks/chip_entropy_src_testplan.hjson.md) |
| `chip_flash_ctrl_testplan.hjson` | 8 | 8 | 10 ✓ | [blocks/chip_flash_ctrl_testplan.hjson.md](blocks/chip_flash_ctrl_testplan.hjson.md) |
| `chip_gpio_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_gpio_testplan.hjson.md](blocks/chip_gpio_testplan.hjson.md) |
| `chip_hmac_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_hmac_testplan.hjson.md](blocks/chip_hmac_testplan.hjson.md) |
| `chip_i2c_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_i2c_testplan.hjson.md](blocks/chip_i2c_testplan.hjson.md) |
| `chip_keymgr_testplan.hjson` | 8 | 8 | 10 ✓ | [blocks/chip_keymgr_testplan.hjson.md](blocks/chip_keymgr_testplan.hjson.md) |
| `chip_kmac_testplan.hjson` | 8 | 8 | 11 ✓ | [blocks/chip_kmac_testplan.hjson.md](blocks/chip_kmac_testplan.hjson.md) |
| `chip_lc_ctrl_testplan.hjson` | 8 | 8 | 11 ✓ | [blocks/chip_lc_ctrl_testplan.hjson.md](blocks/chip_lc_ctrl_testplan.hjson.md) |
| `chip_otbn_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_otbn_testplan.hjson.md](blocks/chip_otbn_testplan.hjson.md) |
| `chip_otp_ctrl_testplan.hjson` | 8 | 8 | 10 ✓ | [blocks/chip_otp_ctrl_testplan.hjson.md](blocks/chip_otp_ctrl_testplan.hjson.md) |
| `chip_pwm_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_pwm_testplan.hjson.md](blocks/chip_pwm_testplan.hjson.md) |
| `chip_pwrmgr_testplan.hjson` | 8 | 8 | 10 ✓ | [blocks/chip_pwrmgr_testplan.hjson.md](blocks/chip_pwrmgr_testplan.hjson.md) |
| `chip_rom_ctrl_testplan.hjson` | 8 | 8 | 10 ✓ | [blocks/chip_rom_ctrl_testplan.hjson.md](blocks/chip_rom_ctrl_testplan.hjson.md) |
| `chip_rstmgr_testplan.hjson` | 8 | 8 | 10 ✓ | [blocks/chip_rstmgr_testplan.hjson.md](blocks/chip_rstmgr_testplan.hjson.md) |
| `chip_rv_core_ibex_testplan.hjson` | 8 | 8 | 10 ✓ | [blocks/chip_rv_core_ibex_testplan.hjson.md](blocks/chip_rv_core_ibex_testplan.hjson.md) |
| `chip_rv_dm_testplan.hjson` | 8 | 8 | 10 ✓ | [blocks/chip_rv_dm_testplan.hjson.md](blocks/chip_rv_dm_testplan.hjson.md) |
| `chip_rv_plic_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_rv_plic_testplan.hjson.md](blocks/chip_rv_plic_testplan.hjson.md) |
| `chip_rv_timer_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_rv_timer_testplan.hjson.md](blocks/chip_rv_timer_testplan.hjson.md) |
| `chip_spi_device_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_spi_device_testplan.hjson.md](blocks/chip_spi_device_testplan.hjson.md) |
| `chip_spi_host_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_spi_host_testplan.hjson.md](blocks/chip_spi_host_testplan.hjson.md) |
| `chip_sram_ctrl_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_sram_ctrl_testplan.hjson.md](blocks/chip_sram_ctrl_testplan.hjson.md) |
| `chip_sysrst_ctrl_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_sysrst_ctrl_testplan.hjson.md](blocks/chip_sysrst_ctrl_testplan.hjson.md) |
| `chip_uart_testplan.hjson` | 8 | 8 | 10 ✓ | [blocks/chip_uart_testplan.hjson.md](blocks/chip_uart_testplan.hjson.md) |
| `chip_usbdev_testplan.hjson` | 8 | 8 | 9 ✓ | [blocks/chip_usbdev_testplan.hjson.md](blocks/chip_usbdev_testplan.hjson.md) |
| `prim_flash` | 6 | 6 | 1  | [blocks/prim_flash.md](blocks/prim_flash.md) |
| `prim_keccak` | 5 | 5 | 1  | [blocks/prim_keccak.md](blocks/prim_keccak.md) |
| `prim_packer` | 5 | 5 | 1  | [blocks/prim_packer.md](blocks/prim_packer.md) |
| `prim_packer_fifo` | 5 | 5 | 1  | [blocks/prim_packer_fifo.md](blocks/prim_packer_fifo.md) |
| `prim_ram_1p_scr` | 5 | 5 | 1  | [blocks/prim_ram_1p_scr.md](blocks/prim_ram_1p_scr.md) |
| `prim_xoshiro256pp` | 4 | 4 | 1  | [blocks/prim_xoshiro256pp.md](blocks/prim_xoshiro256pp.md) |
| `testplanner` | 3 | 3 | 1  | [blocks/testplanner.md](blocks/testplanner.md) |
| `compliance` | 2 | 2 | 1  | [blocks/compliance.md](blocks/compliance.md) |
