# Spec-Code Only Bridge Summary

This report keeps only relationships that require both spec and code graphs.

- Source graph: `D:\MyWork\verilog\dbs\graphify-out\spec-code-graphify\graph.json`
- Total bridge links: 12598
- Displayed bridge links: 2600
- Displayed nodes: 398

## Bridge Relations

| Relation | Count |
|---|---:|
| `spec_path_matches_code_path` | 9983 |
| `spec_component_matches_code` | 2615 |

## Top Components

| Component | Bridge edges | Sample spec | Sample code | Sample code file |
|---|---:|---|---|---|
| `rstmgr` | 680 | `component:rstmgr` | `rstmgr_rst_en_track_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\sva\rstmgr_rst_en_track_sva_if.sv` |
| `pinmux` | 664 | `component:pinmux` | `pinmux_jtag_buf` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv` |
| `clkmgr` | 611 | `component:clkmgr` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `rv_core_ibex` | 591 | `component:rv_core_ibex` | `rv_core_ibex_reg_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv` |
| `pwrmgr` | 568 | `component:pwrmgr` | `pwrmgr_sec_cm_checker_assert.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pwrmgr\dv\sva\pwrmgr_sec_cm_checker_assert.sv` |
| `otp_ctrl` | 532 | `component:otp_ctrl` | `otp_ctrl_top_specific_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv` |
| `gpio` | 520 | `component:gpio` | `gpio_straps_if.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\gpio\dv\interfaces\gpio_straps_if.sv` |
| `rv_plic` | 456 | `component:rv_plic` | `rv_plic_assert_fpv.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\fpv\vip\rv_plic_assert_fpv.sv` |
| `ibex` | 418 | `compliance.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `flash_ctrl` | 416 | `component:flash_ctrl` | `flash_ctrl_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl_top_specific_pkg.sv` |
| `prim` | 365 | `component:prim` | `prim_ascon_duplex_tb_pkg.sv` | `ibex\vendor\lowrisc_ip\ip\prim\pre_dv\prim_ascon\prim_ascon_duplex_tb\rtl\prim_ascon_duplex_tb_pkg.sv` |
| `lowrisc_ibex` | 351 | `vendor.md` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `alert_handler` | 336 | `component:alert_handler` | `alert_handler_ping_timer_assert_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\alert_handler\fpv\vip\alert_handler_ping_timer_assert_fpv.sv` |
| `unknown` | 230 | `mem_access_testplan.hjson` | `mem_bkdr_scb.sv` | `opentitan\hw\dv\sv\mem_bkdr_scb\mem_bkdr_scb.sv` |
| `pwm` | 224 | `component:pwm` | `pwm_base_test.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pwm\dv\tests\pwm_base_test.sv` |
| `racl_ctrl` | 206 | `component:racl_ctrl` | `racl_ctrl_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\sva\racl_ctrl_bind.sv` |
| `lc_ctrl` | 192 | `component:lc_ctrl` | `lc_ctrl_state_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `ac_range_check` | 182 | `component:ac_range_check` | `ac_range_check_base_test.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_base_test.sv` |
| `otbn` | 160 | `component:otbn` | `otbn_model_agent_cfg.sv` | `opentitan\hw\ip\otbn\dv\uvm\otbn_model_agent\otbn_model_agent_cfg.sv` |
| `xbar_main` | 143 | `component:xbar_main` | `xbar_main_bind.sv` | `opentitan\hw\top_englishbreakfast\ip\xbar_main\dv\autogen\xbar_main_bind.sv` |
| `xbar_peri` | 138 | `component:xbar_peri` | `xbar_peri_bind.sv` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `usbdev` | 120 | `component:usbdev` | `usbdev` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `mbx` | 117 | `component:mbx` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `sensor_ctrl` | 115 | `component:sensor_ctrl` | `sensor_ctrl_reg_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv` |
| `aes` | 112 | `component:aes` | `aes_cipher_core_tb.sv` | `opentitan\hw\ip\aes\pre_dv\aes_cipher_core_tb\rtl\aes_cipher_core_tb.sv` |
| `csrng` | 112 | `component:csrng` | `csrng_stress_all_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_stress_all_test.sv` |
| `edn` | 112 | `component:edn` | `edn_disable_auto_req_mode_test.sv` | `opentitan\hw\ip\edn\dv\tests\edn_disable_auto_req_mode_test.sv` |
| `entropy_src` | 112 | `component:entropy_src` | `entropy_src_functional_errors_test.sv` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_functional_errors_test.sv` |
| `hmac` | 112 | `component:hmac` | `hmac` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `i2c` | 112 | `component:i2c` | `i2c_fifo_sync_sram_adapter.sv` | `opentitan\hw\ip\i2c\rtl\i2c_fifo_sync_sram_adapter.sv` |
| `keymgr` | 112 | `component:keymgr` | `keymgr_sideload_key_ctrl.sv` | `opentitan\hw\ip\keymgr\rtl\keymgr_sideload_key_ctrl.sv` |
| `kmac` | 112 | `component:kmac` | `kmac_reduced_tb.sv` | `opentitan\hw\ip\kmac\pre_dv\kmac_reduced_tb\rtl\kmac_reduced_tb.sv` |
| `pattgen` | 112 | `component:pattgen` | `pattgen_base_test.sv` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_base_test.sv` |
| `rom_ctrl` | 112 | `component:rom_ctrl` | `rom_ctrl` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `rv_dm` | 112 | `component:rv_dm` | `rv_dm` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spi_device` | 112 | `component:spi_device` | `spi_device` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spi_host` | 112 | `component:spi_host` | `spi_host` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `uart` | 112 | `component:uart` | `uart` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `keymgr_dpe` | 107 | `component:keymgr_dpe` | `keymgr_dpe_base_test.sv` | `opentitan\hw\ip\keymgr_dpe\dv\tests\keymgr_dpe_base_test.sv` |
| `adc_ctrl` | 104 | `component:adc_ctrl` | `adc_ctrl_core_cov_if.sv` | `opentitan\hw\ip\adc_ctrl\dv\cov\adc_ctrl_core_cov_if.sv` |
