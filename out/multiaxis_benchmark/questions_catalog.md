# Multi-Axis RTL Question Set

## L1

### structure_understanding

1. What are the top-level ports and child instances of module `top_darjeeling`?
   - gold: `top_darjeeling`
2. What are the top-level ports and child instances of module `top_earlgrey`?
   - gold: `top_earlgrey`
3. What are the top-level ports and child instances of module `spi_device`?
   - gold: `spi_device`
4. What are the top-level ports and child instances of module `top_englishbreakfast`?
   - gold: `top_englishbreakfast`
5. What are the top-level ports and child instances of module `flash_ctrl`?
   - gold: `flash_ctrl`

### search_navigation

1. Find the module named `bus` in the current RTL knowledge DB.
   - gold: `bus`
2. Find the module named `clkgen_xil7series` in the current RTL knowledge DB.
   - gold: `clkgen_xil7series`
3. Find the module named `ibex_alu` in the current RTL knowledge DB.
   - gold: `ibex_alu`
4. Find the module named `ibex_branch_predict` in the current RTL knowledge DB.
   - gold: `ibex_branch_predict`
5. Find the module named `ibex_compressed_decoder` in the current RTL knowledge DB.
   - gold: `ibex_compressed_decoder`

### comparison_similarity

1. Compare `top_darjeeling` and `top_earlgrey` at a high level using only project, labels, ports, and instance counts.
   - gold: `top_darjeeling, top_earlgrey`
2. Compare `top_darjeeling` and `spi_device` at a high level using only project, labels, ports, and instance counts.
   - gold: `top_darjeeling, spi_device`
3. Compare `top_darjeeling` and `top_englishbreakfast` at a high level using only project, labels, ports, and instance counts.
   - gold: `top_darjeeling, top_englishbreakfast`
4. Compare `top_darjeeling` and `flash_ctrl` at a high level using only project, labels, ports, and instance counts.
   - gold: `top_darjeeling, flash_ctrl`
5. In L1, compare `top_darjeeling` and `top_englishbreakfast` for similarity in role, structure, and reuse value.
   - gold: `top_darjeeling, top_englishbreakfast`

### function_similarity

1. Which module is tagged as `fifo` and would be the most direct example of that function?
   - gold: `i2c_fifo_sync_sram_adapter`
2. Which module is tagged as `spi` and would be the most direct example of that function?
   - gold: `spi_host`
3. Which module is tagged as `uart` and would be the most direct example of that function?
   - gold: `uart`
4. Which module is tagged as `i2c` and would be the most direct example of that function?
   - gold: `i2c_core`
5. In L1, identify the module that best represents `uart` behavior and justify it from the knowledge DB.
   - gold: `uart`

### generation_design

1. If you needed a very small wrapper around `ast`, which existing module should you inspect first as the reference block?
   - gold: `ast`
2. If you needed a very small wrapper around `otbn_core`, which existing module should you inspect first as the reference block?
   - gold: `otbn_core`
3. If you needed a very small wrapper around `pwrmgr`, which existing module should you inspect first as the reference block?
   - gold: `pwrmgr`
4. In L1, write a generation/design prompt for extending `sram_ctrl` while preserving its interface intent.
   - gold: `sram_ctrl`
5. In L1, write a generation/design prompt for extending `ast` while preserving its interface intent.
   - gold: `ast`

### code_explanation

1. Explain in simple terms what module `flash_ctrl` appears to do from its ports, labels, and file path.
   - gold: `flash_ctrl`
2. Explain in simple terms what module `entropy_src_core` appears to do from its ports, labels, and file path.
   - gold: `entropy_src_core`
3. Explain in simple terms what module `otp_ctrl` appears to do from its ports, labels, and file path.
   - gold: `otp_ctrl`
4. Explain in simple terms what module `rv_core_ibex` appears to do from its ports, labels, and file path.
   - gold: `rv_core_ibex`
5. In L1, explain `otbn` to another engineer using hierarchy, labels, and ports.
   - gold: `otbn`

### documentation_summary

1. Write a short design-note summary for module `rv_core_ibex` using only the current knowledge DB facts.
   - gold: `rv_core_ibex`
2. Write a short design-note summary for module `rv_dm` using only the current knowledge DB facts.
   - gold: `rv_dm`
3. Write a short design-note summary for module `keymgr_dpe` using only the current knowledge DB facts.
   - gold: `keymgr_dpe`
4. Write a short design-note summary for module `prim_sdc_example` using only the current knowledge DB facts.
   - gold: `prim_sdc_example`
5. In L1, produce a concise documentation summary for `pwrmgr` from the current knowledge DB.
   - gold: `pwrmgr`

## L2

### structure_understanding

1. Describe how `top_darjeeling` is structured by relating ports `mio_in_i`, `mio_out_o` and child `uart`.
   - gold: `top_darjeeling`
2. Describe how `top_earlgrey` is structured by relating ports `mio_in_i`, `mio_out_o` and child `pinmux_jtag_breakout`.
   - gold: `top_earlgrey`
3. Describe how `spi_device` is structured by relating ports `clk_i`, `rst_ni` and child `prim_buf`.
   - gold: `spi_device`
4. Describe how `top_englishbreakfast` is structured by relating ports `mio_in_i`, `mio_out_o` and child `pinmux_jtag_breakout`.
   - gold: `top_englishbreakfast`
5. Describe how `flash_ctrl` is structured by relating ports `clk_i`, `rst_ni` and child `flash_ctrl_core_reg_top`.
   - gold: `flash_ctrl`

### search_navigation

1. Find the `opentitan` module that combines port `enables` with the path `top_darjeeling.sv`.
   - gold: `top_darjeeling`
2. Find the `opentitan` module that combines port `enables` with the path `top_earlgrey.sv`.
   - gold: `top_earlgrey`
3. Find the `opentitan` module that combines port `enable` with the path `spi_device.sv`.
   - gold: `spi_device`
4. Find the `opentitan` module that combines port `enables` with the path `top_englishbreakfast.sv`.
   - gold: `top_englishbreakfast`
5. Find the `opentitan` module that combines port `shared` with the path `flash_ctrl.sv`.
   - gold: `flash_ctrl`

### comparison_similarity

1. Which of `top_darjeeling` and `entropy_src_core` are structurally closer based on shared labels and interface shape?
   - gold: `top_darjeeling, entropy_src_core`
2. Which of `top_darjeeling` and `otp_ctrl` are structurally closer based on shared labels and interface shape?
   - gold: `top_darjeeling, otp_ctrl`
3. Which of `top_darjeeling` and `rv_core_ibex` are structurally closer based on shared labels and interface shape?
   - gold: `top_darjeeling, rv_core_ibex`
4. In L2, compare `top_darjeeling` and `top_englishbreakfast` for similarity in role, structure, and reuse value.
   - gold: `top_darjeeling, top_englishbreakfast`
5. In L2, compare `top_darjeeling` and `flash_ctrl` for similarity in role, structure, and reuse value.
   - gold: `top_darjeeling, flash_ctrl`

### function_similarity

1. Find two modules that both behave like `fifo` blocks and explain the common function.
   - gold: `i2c_fifo_sync_sram_adapter, prim_fifo_sync`
2. Find two modules that both behave like `spi` blocks and explain the common function.
   - gold: `spi_host, spi_device`
3. Find two modules that both behave like `uart` blocks and explain the common function.
   - gold: `uart, uart_core`
4. Find two modules that both behave like `i2c` blocks and explain the common function.
   - gold: `i2c_core, i2c_reg_top`
5. In L2, identify the module that best represents `uart` behavior and justify it from the knowledge DB.
   - gold: `uart`

### generation_design

1. If you were generating a thin wrapper around `ast`, which child block and interface signals must be preserved first?
   - gold: `ast`
2. If you were generating a thin wrapper around `otbn_core`, which child block and interface signals must be preserved first?
   - gold: `otbn_core`
3. If you were generating a thin wrapper around `pwrmgr`, which child block and interface signals must be preserved first?
   - gold: `pwrmgr`
4. If you were generating a thin wrapper around `csrng_core`, which child block and interface signals must be preserved first?
   - gold: `csrng_core`
5. If you were generating a thin wrapper around `prim_sdc_example`, which child block and interface signals must be preserved first?
   - gold: `prim_sdc_example`

### code_explanation

1. Explain the likely role of `clkmgr_reg_top` from labels `clocked, hierarchical, resettable` and ports like `clk_i`.
   - gold: `clkmgr_reg_top`
2. Explain the likely role of `ast_clks_byp` from labels `clocked, hierarchical` and ports like `vcaon_pok_i`.
   - gold: `ast_clks_byp`
3. Explain the likely role of `aes_core` from labels `clocked, hierarchical, resettable` and ports like `clk_i`.
   - gold: `aes_core`
4. Explain the likely role of `kmac_reg_top` from labels `clocked, hierarchical, resettable` and ports like `clk_i`.
   - gold: `kmac_reg_top`
5. Explain the likely role of `usbdev_reg_top` from labels `clocked, hierarchical, resettable` and ports like `clk_i`.
   - gold: `usbdev_reg_top`

### documentation_summary

1. Summarize `edn_core` for an engineer who only needs interface, role, and integration context.
   - gold: `edn_core`
2. Summarize `chip_darjeeling_verilator` for an engineer who only needs interface, role, and integration context.
   - gold: `chip_darjeeling_verilator`
3. Summarize `aon_timer_reg_top` for an engineer who only needs interface, role, and integration context.
   - gold: `aon_timer_reg_top`
4. Summarize `racl_ctrl_reg_top` for an engineer who only needs interface, role, and integration context.
   - gold: `racl_ctrl_reg_top`
5. Summarize `aes_reg_top` for an engineer who only needs interface, role, and integration context.
   - gold: `aes_reg_top`

## L3

### structure_understanding

1. Reconstruct the local hierarchy under `top_darjeeling` and explain what each major child likely contributes.
   - gold: `top_darjeeling`
2. Reconstruct the local hierarchy under `top_earlgrey` and explain what each major child likely contributes.
   - gold: `top_earlgrey`
3. Reconstruct the local hierarchy under `spi_device` and explain what each major child likely contributes.
   - gold: `spi_device`
4. Reconstruct the local hierarchy under `top_englishbreakfast` and explain what each major child likely contributes.
   - gold: `top_englishbreakfast`
5. Reconstruct the local hierarchy under `flash_ctrl` and explain what each major child likely contributes.
   - gold: `flash_ctrl`

### search_navigation

1. Which parent module should be retrieved if the query is centered on child `BSCANE2` rather than the parent name itself?
   - gold: `dmi_jtag_tap`
2. Which parent module should be retrieved if the query is centered on child `prim_fifo_async_simple` rather than the parent name itself?
   - gold: `dmi_cdc`
3. Which parent module should be retrieved if the query is centered on child `dmi_jtag_tap` rather than the parent name itself?
   - gold: `dmi_jtag`
4. Which parent module should be retrieved if the query is centered on child `dmi_cdc` rather than the parent name itself?
   - gold: `dmi_jtag`
5. Which parent module should be retrieved if the query is centered on child `debug_rom` rather than the parent name itself?
   - gold: `dm_mem`

### comparison_similarity

1. Compare `top_darjeeling` and `ast` as candidate alternatives for the same subsystem role.
   - gold: `top_darjeeling, ast`
2. Compare `top_darjeeling` and `kmac` as candidate alternatives for the same subsystem role.
   - gold: `top_darjeeling, kmac`
3. Compare `top_darjeeling` and `clkmgr` as candidate alternatives for the same subsystem role.
   - gold: `top_darjeeling, clkmgr`
4. Compare `top_darjeeling` and `clkmgr_reg_top` as candidate alternatives for the same subsystem role.
   - gold: `top_darjeeling, clkmgr_reg_top`
5. Compare `top_darjeeling` and `ast_clks_byp` as candidate alternatives for the same subsystem role.
   - gold: `top_darjeeling, ast_clks_byp`

### function_similarity

1. Find cross-project modules that both implement a `fifo`-like function and explain the commonality.
   - gold: `ibex_fetch_fifo, csrng_cmd_stage`
2. Find cross-project modules that both implement a `fifo`-like function and explain the commonality.
   - gold: `ibex_fetch_fifo, csrng_core`
3. Find cross-project modules that both implement a `fifo`-like function and explain the commonality.
   - gold: `ibex_fetch_fifo, dev_entropy`
4. Find cross-project modules that both implement a `fifo`-like function and explain the commonality.
   - gold: `ibex_fetch_fifo, dm_csrs`
5. Find cross-project modules that both implement a `fifo`-like function and explain the commonality.
   - gold: `ibex_fetch_fifo, dmi_cdc`

### generation_design

1. Create a design brief for generating a compatible block around `dma` without breaking ports `clk_i` and `rst_ni`.
   - gold: `dma`
2. Create a design brief for generating a compatible block around `ac_range_check_reg_top` without breaking ports `clk_i` and `rst_ni`.
   - gold: `ac_range_check_reg_top`
3. Create a design brief for generating a compatible block around `ac_range_check` without breaking ports `clk_i` and `rst_ni`.
   - gold: `ac_range_check`
4. Create a design brief for generating a compatible block around `keymgr_dpe_reg_top` without breaking ports `clk_i` and `rst_ni`.
   - gold: `keymgr_dpe_reg_top`
5. Create a design brief for generating a compatible block around `keymgr_reg_top` without breaking ports `clk_i` and `rst_ni`.
   - gold: `keymgr_reg_top`

### code_explanation

1. Explain why `mbx_soc_reg_top` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `mbx_soc_reg_top`
2. Explain why `pinmux_reg_top` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `pinmux_reg_top`
3. Explain why `pwrmgr_reg_top` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `pwrmgr_reg_top`
4. Explain why `rv_timer_reg_top` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `rv_timer_reg_top`
5. Explain why `spi_device_reg_top` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `spi_device_reg_top`

### documentation_summary

1. Write a module reference summary for `sram_ctrl_regs_reg_top` including role, interface shape, and where it sits in the hierarchy.
   - gold: `sram_ctrl_regs_reg_top`
2. Write a module reference summary for `sysrst_ctrl_reg_top` including role, interface shape, and where it sits in the hierarchy.
   - gold: `sysrst_ctrl_reg_top`
3. Write a module reference summary for `uart_reg_top` including role, interface shape, and where it sits in the hierarchy.
   - gold: `uart_reg_top`
4. Write a module reference summary for `csrng_reg_top` including role, interface shape, and where it sits in the hierarchy.
   - gold: `csrng_reg_top`
5. Write a module reference summary for `edn_reg_top` including role, interface shape, and where it sits in the hierarchy.
   - gold: `edn_reg_top`

## L4

### structure_understanding

1. Explain the structural decomposition of `otbn_instruction_fetch` and how its major children likely partition responsibilities.
   - gold: `otbn_instruction_fetch`
2. Explain the structural decomposition of `i2c_core` and how its major children likely partition responsibilities.
   - gold: `i2c_core`
3. Explain the structural decomposition of `soc_proxy` and how its major children likely partition responsibilities.
   - gold: `soc_proxy`
4. Explain the structural decomposition of `spi_host` and how its major children likely partition responsibilities.
   - gold: `spi_host`
5. Explain the structural decomposition of `pinmux_strap_sampling` and how its major children likely partition responsibilities.
   - gold: `pinmux_strap_sampling`

### search_navigation

1. If the query starts from reused child `prim_flop_2sync`, which parent contexts should a graph-aware search inspect first?
   - gold: `i2c_core, prim_clock_meas`
2. If the query starts from reused child `prim_flop`, which parent contexts should a graph-aware search inspect first?
   - gold: `prim_flop_2sync, prim_sdc_example`
3. If the query starts from reused child `tlul_rsp_intg_gen`, which parent contexts should a graph-aware search inspect first?
   - gold: `tlul_adapter_sram, tlul_request_loopback`
4. If the query starts from reused child `tlul_adapter_reg`, which parent contexts should a graph-aware search inspect first?
   - gold: `tlul_adapter_reg_racl, rv_dm`
5. If the query starts from reused child `prim_subreg`, which parent contexts should a graph-aware search inspect first?
   - gold: `prim_subreg_shadow, clkmgr_reg_top`

### comparison_similarity

1. Compare `top_darjeeling` and `hmac` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `top_darjeeling, hmac`
2. Compare `top_darjeeling` and `gpio_reg_top` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `top_darjeeling, gpio_reg_top`
3. Compare `top_darjeeling` and `rstmgr_reg_top` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `top_darjeeling, rstmgr_reg_top`
4. Compare `top_darjeeling` and `rv_dm_regs_reg_top` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `top_darjeeling, rv_dm_regs_reg_top`
5. Compare `top_darjeeling` and `ast_reg_top` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `top_darjeeling, ast_reg_top`

### function_similarity

1. Which two modules would you shortlist as functionally similar candidates for `fifo` behavior, and why?
   - gold: `ibex_fetch_fifo, ibex_prefetch_buffer`
2. Which two modules would you shortlist as functionally similar candidates for `fifo` behavior, and why?
   - gold: `ibex_fetch_fifo, prim_edn_req`
3. Which two modules would you shortlist as functionally similar candidates for `fifo` behavior, and why?
   - gold: `ibex_fetch_fifo, prim_fifo_async_simple`
4. Which two modules would you shortlist as functionally similar candidates for `fifo` behavior, and why?
   - gold: `ibex_fetch_fifo, prim_fifo_async_sram_adapter`
5. Which two modules would you shortlist as functionally similar candidates for `fifo` behavior, and why?
   - gold: `ibex_fetch_fifo, prim_generic_flash_bank`

### generation_design

1. Prepare a generation plan for a replacement or extension of `tlul_adapter_sram` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `tlul_adapter_sram`
2. Prepare a generation plan for a replacement or extension of `uart_core` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `uart_core`
3. Prepare a generation plan for a replacement or extension of `aes_dom_inverse_gf2p8` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `aes_dom_inverse_gf2p8`
4. Prepare a generation plan for a replacement or extension of `mbx` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `mbx`
5. Prepare a generation plan for a replacement or extension of `rv_dm_dmi_gate` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `rv_dm_dmi_gate`

### code_explanation

1. Explain the design intent of `flash_ctrl_prim_reg_top` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `flash_ctrl_prim_reg_top`
2. Explain the design intent of `prim_esc_receiver` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `prim_esc_receiver`
3. Explain the design intent of `soc_proxy_core_reg_top` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `soc_proxy_core_reg_top`
4. Explain the design intent of `aes_sbox_tb` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `aes_sbox_tb`
5. Explain the design intent of `ibex_simple_system` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `ibex_simple_system`

### documentation_summary

1. Draft documentation for `chip_englishbreakfast_cw305` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `chip_englishbreakfast_cw305`
2. Draft documentation for `kmac_reduced` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `kmac_reduced`
3. Draft documentation for `otp_ctrl_dai` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `otp_ctrl_dai`
4. Draft documentation for `otp_ctrl_part_buf` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `otp_ctrl_part_buf`
5. Draft documentation for `mbx_sysif` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `mbx_sysif`

## L5

### structure_understanding

1. Reconstruct the likely subsystem architecture around `aes_cipher_core` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `aes_cipher_core`
2. Reconstruct the likely subsystem architecture around `otp_ctrl_kdi` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `otp_ctrl_kdi`
3. Reconstruct the likely subsystem architecture around `otbn_mac_bignum` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `otbn_mac_bignum`
4. Reconstruct the likely subsystem architecture around `spi_host_core` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `spi_host_core`
5. Reconstruct the likely subsystem architecture around `otbn_loop_controller` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `otbn_loop_controller`

### search_navigation

1. For a graph query starting from shared child `prim_flop_2sync`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `i2c_core, prim_clock_meas, prim_clock_gating_sync`
2. For a graph query starting from shared child `prim_flop`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `prim_flop_2sync, prim_sdc_example, prim_ram_1p_scr`
3. For a graph query starting from shared child `tlul_rsp_intg_gen`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `tlul_adapter_sram, tlul_request_loopback, tlul_adapter_reg`
4. For a graph query starting from shared child `tlul_adapter_reg`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `tlul_adapter_reg_racl, rv_dm, clkmgr_reg_top`
5. For a graph query starting from shared child `prim_subreg`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `prim_subreg_shadow, clkmgr_reg_top, kmac_reg_top`

### comparison_similarity

1. Make an architecture-level comparison between `top_earlgrey` and `alert_handler_reg_top` to decide which is the better template for a new subsystem.
   - gold: `top_earlgrey, alert_handler_reg_top`
2. Make an architecture-level comparison between `top_earlgrey` and `ascon_reg_top` to decide which is the better template for a new subsystem.
   - gold: `top_earlgrey, ascon_reg_top`
3. Make an architecture-level comparison between `top_earlgrey` and `flash_ctrl_core_reg_top` to decide which is the better template for a new subsystem.
   - gold: `top_earlgrey, flash_ctrl_core_reg_top`
4. Make an architecture-level comparison between `top_earlgrey` and `pwm_reg_top` to decide which is the better template for a new subsystem.
   - gold: `top_earlgrey, pwm_reg_top`
5. Make an architecture-level comparison between `top_earlgrey` and `rv_core_ibex_cfg_reg_top` to decide which is the better template for a new subsystem.
   - gold: `top_earlgrey, rv_core_ibex_cfg_reg_top`

### function_similarity

1. Across projects, which modules are the best semantic analogs for `fifo` behavior between `ibex_fetch_fifo` and `edn_ack_sm`, and where do they diverge functionally?
   - gold: `ibex_fetch_fifo, edn_ack_sm`
2. Across projects, which modules are the best semantic analogs for `fifo` behavior between `ibex_fetch_fifo` and `edn_core`, and where do they diverge functionally?
   - gold: `ibex_fetch_fifo, edn_core`
3. Across projects, which modules are the best semantic analogs for `fifo` behavior between `ibex_fetch_fifo` and `edn_main_sm`, and where do they diverge functionally?
   - gold: `ibex_fetch_fifo, edn_main_sm`
4. Across projects, which modules are the best semantic analogs for `fifo` behavior between `ibex_fetch_fifo` and `entropy_src`, and where do they diverge functionally?
   - gold: `ibex_fetch_fifo, entropy_src`
5. Across projects, which modules are the best semantic analogs for `fifo` behavior between `ibex_fetch_fifo` and `entropy_src_ack_sm`, and where do they diverge functionally?
   - gold: `ibex_fetch_fifo, entropy_src_ack_sm`

### generation_design

1. Write a design-generation brief for building a new module inspired by `adc_ctrl_core`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `adc_ctrl_core`
2. Write a design-generation brief for building a new module inspired by `ascon`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `ascon`
3. Write a design-generation brief for building a new module inspired by `aes_dom_inverse_gf2p4`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `aes_dom_inverse_gf2p4`
4. Write a design-generation brief for building a new module inspired by `usb_clk`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `usb_clk`
5. Write a design-generation brief for building a new module inspired by `xbar_main`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `xbar_main`

### code_explanation

1. Explain `rstmgr_por` deeply enough that another engineer could answer follow-up questions about hierarchy, behavior, and likely integration assumptions.
   - gold: `rstmgr_por`
2. Explain `tlul_request_loopback` deeply enough that another engineer could answer follow-up questions about hierarchy, behavior, and likely integration assumptions.
   - gold: `tlul_request_loopback`
3. Explain `prim_flop_2sync` deeply enough that another engineer could answer follow-up questions about hierarchy, behavior, and likely integration assumptions.
   - gold: `prim_flop_2sync`
4. In L5, explain `otbn` to another engineer using hierarchy, labels, and ports.
   - gold: `otbn`
5. In L5, explain `sram_ctrl` to another engineer using hierarchy, labels, and ports.
   - gold: `sram_ctrl`

### documentation_summary

1. Produce a high-value design document summary for `pinmux` that could seed internal docs or review notes for future maintainers.
   - gold: `pinmux`
2. Produce a high-value design document summary for `pwrmgr_cdc` that could seed internal docs or review notes for future maintainers.
   - gold: `pwrmgr_cdc`
3. Produce a high-value design document summary for `kmac_app` that could seed internal docs or review notes for future maintainers.
   - gold: `kmac_app`
4. Produce a high-value design document summary for `sha3` that could seed internal docs or review notes for future maintainers.
   - gold: `sha3`
5. Produce a high-value design document summary for `spi_passthrough` that could seed internal docs or review notes for future maintainers.
   - gold: `spi_passthrough`
