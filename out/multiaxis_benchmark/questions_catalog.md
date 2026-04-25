# Multi-Axis RTL Question Set

## L1

### structure_understanding

1. What are the top-level ports and child instances of module `entropy_src_core`?
   - gold: `entropy_src_core`
2. What are the top-level ports and child instances of module `clkmgr`?
   - gold: `clkmgr`
3. What are the top-level ports and child instances of module `ast_clks_byp`?
   - gold: `ast_clks_byp`
4. What are the top-level ports and child instances of module `spi_device`?
   - gold: `spi_device`
5. In L1, explain the structure of `i2c_core` using ports, labels, and child instances.
   - gold: `i2c_core`

### search_navigation

1. Find the module named `clkgen_xil7series` in the current RTL knowledge DB.
   - gold: `clkgen_xil7series`
2. Find the module named `ibex_alu` in the current RTL knowledge DB.
   - gold: `ibex_alu`
3. Find the module named `ibex_branch_predict` in the current RTL knowledge DB.
   - gold: `ibex_branch_predict`
4. Find the module named `ibex_controller` in the current RTL knowledge DB.
   - gold: `ibex_controller`
5. Find the module named `ibex_counter` in the current RTL knowledge DB.
   - gold: `ibex_counter`

### comparison_similarity

1. Compare `entropy_src_core` and `clkmgr` at a high level using only project, labels, ports, and instance counts.
   - gold: `entropy_src_core, clkmgr`
2. Compare `entropy_src_core` and `ast_clks_byp` at a high level using only project, labels, ports, and instance counts.
   - gold: `entropy_src_core, ast_clks_byp`
3. Compare `entropy_src_core` and `spi_device` at a high level using only project, labels, ports, and instance counts.
   - gold: `entropy_src_core, spi_device`
4. Compare `entropy_src_core` and `top_darjeeling` at a high level using only project, labels, ports, and instance counts.
   - gold: `entropy_src_core, top_darjeeling`
5. In L1, compare `entropy_src_core` and `ast_clks_byp` for similarity in role, structure, and reuse value.
   - gold: `entropy_src_core, ast_clks_byp`

### function_similarity

1. Which module is tagged as `fifo` and would be the most direct example of that function?
   - gold: `rv_core_ibex`
2. Which module is tagged as `uart` and would be the most direct example of that function?
   - gold: `flash_ctrl`
3. Which module is tagged as `hierarchical` and would be the most direct example of that function?
   - gold: `otbn_alu_bignum`
4. Which module is tagged as `uart` and would be the most direct example of that function?
   - gold: `clkmgr`
5. In L1, identify the module that best represents `apb` behavior and justify it from the knowledge DB.
   - gold: `ibex_cs_registers`

### generation_design

1. If you needed a very small wrapper around `ibex_cs_registers`, which existing module should you inspect first as the reference block?
   - gold: `ibex_cs_registers`
2. If you needed a very small wrapper around `keymgr_dpe`, which existing module should you inspect first as the reference block?
   - gold: `keymgr_dpe`
3. If you needed a very small wrapper around `top_englishbreakfast`, which existing module should you inspect first as the reference block?
   - gold: `top_englishbreakfast`
4. If you needed a very small wrapper around `aes_core`, which existing module should you inspect first as the reference block?
   - gold: `aes_core`
5. In L1, write a generation/design prompt for extending `clkmgr` while preserving its interface intent.
   - gold: `clkmgr`

### code_explanation

1. Explain in simple terms what module `top_darjeeling` appears to do from its ports, labels, and file path.
   - gold: `top_darjeeling`
2. Explain in simple terms what module `top_earlgrey` appears to do from its ports, labels, and file path.
   - gold: `top_earlgrey`
3. Explain in simple terms what module `dma` appears to do from its ports, labels, and file path.
   - gold: `dma`
4. Explain in simple terms what module `ast` appears to do from its ports, labels, and file path.
   - gold: `ast`
5. Explain in simple terms what module `otp_ctrl` appears to do from its ports, labels, and file path.
   - gold: `otp_ctrl`

### documentation_summary

1. Write a short design-note summary for module `otp_ctrl` using only the current knowledge DB facts.
   - gold: `otp_ctrl`
2. Write a short design-note summary for module `ast` using only the current knowledge DB facts.
   - gold: `ast`
3. Write a short design-note summary for module `usbdev` using only the current knowledge DB facts.
   - gold: `usbdev`
4. Write a short design-note summary for module `rv_core_ibex` using only the current knowledge DB facts.
   - gold: `rv_core_ibex`
5. In L1, produce a concise documentation summary for `top_englishbreakfast` from the current knowledge DB.
   - gold: `top_englishbreakfast`

## L2

### structure_understanding

1. Describe how `entropy_src_core` is structured by relating ports `clk_i`, `rst_ni` and child `prim_mubi4_sync`.
   - gold: `entropy_src_core`
2. Describe how `clkmgr` is structured by relating ports `clk_i`, `rst_ni` and child `prim_clock_buf`.
   - gold: `clkmgr`
3. Describe how `ast_clks_byp` is structured by relating ports `vcaon_pok_i`, `vcaon_pok_por_i` and child `prim_clock_buf`.
   - gold: `ast_clks_byp`
4. Describe how `spi_device` is structured by relating ports `clk_i`, `rst_ni` and child `prim_racl_error_arb`.
   - gold: `spi_device`
5. Describe how `top_darjeeling` is structured by relating ports `mio_in_i`, `mio_out_o` and child `uart`.
   - gold: `top_darjeeling`

### search_navigation

1. Find the `opentitan` module that combines port `and` with the path `entropy_src_core.sv`.
   - gold: `entropy_src_core`
2. Find the `opentitan` module that combines port `clkmgr_out_t` with the path `clkmgr.sv`.
   - gold: `clkmgr`
3. Find the `opentitan` module that combines port `always_ff` with the path `ast_clks_byp.sv`.
   - gold: `ast_clks_byp`
4. Find the `opentitan` module that combines port `of` with the path `spi_device.sv`.
   - gold: `spi_device`
5. Find the `opentitan` module that combines port `enables` with the path `top_darjeeling.sv`.
   - gold: `top_darjeeling`

### comparison_similarity

1. Which of `entropy_src_core` and `top_earlgrey` are structurally closer based on shared labels and interface shape?
   - gold: `entropy_src_core, top_earlgrey`
2. Which of `entropy_src_core` and `dma` are structurally closer based on shared labels and interface shape?
   - gold: `entropy_src_core, dma`
3. Which of `entropy_src_core` and `ast` are structurally closer based on shared labels and interface shape?
   - gold: `entropy_src_core, ast`
4. Which of `entropy_src_core` and `otp_ctrl` are structurally closer based on shared labels and interface shape?
   - gold: `entropy_src_core, otp_ctrl`
5. In L2, compare `entropy_src_core` and `ast_clks_byp` for similarity in role, structure, and reuse value.
   - gold: `entropy_src_core, ast_clks_byp`

### function_similarity

1. Find two modules that both behave like `hierarchical` blocks and explain the common function.
   - gold: `dmi_jtag_tap, dmi_cdc`
2. Find two modules that both behave like `clocked` blocks and explain the common function.
   - gold: `debug_rom, debug_rom_one_scratch`
3. Find two modules that both behave like `resettable` blocks and explain the common function.
   - gold: `debug_rom, debug_rom_one_scratch`
4. Find two modules that both behave like `uart` blocks and explain the common function.
   - gold: `top_englishbreakfast, rv_plic`
5. Find two modules that both behave like `fifo` blocks and explain the common function.
   - gold: `dmi_cdc, dm_csrs`

### generation_design

1. If you were generating a thin wrapper around `ibex_cs_registers`, which child block and interface signals must be preserved first?
   - gold: `ibex_cs_registers`
2. If you were generating a thin wrapper around `keymgr_dpe`, which child block and interface signals must be preserved first?
   - gold: `keymgr_dpe`
3. If you were generating a thin wrapper around `top_englishbreakfast`, which child block and interface signals must be preserved first?
   - gold: `top_englishbreakfast`
4. If you were generating a thin wrapper around `aes_core`, which child block and interface signals must be preserved first?
   - gold: `aes_core`
5. If you were generating a thin wrapper around `i2c_core`, which child block and interface signals must be preserved first?
   - gold: `i2c_core`

### code_explanation

1. Explain the likely role of `pwrmgr_cdc` from labels `clocked, hierarchical, resettable` and ports like `clk_slow_i`.
   - gold: `pwrmgr_cdc`
2. Explain the likely role of `otbn` from labels `clocked, hierarchical, resettable` and ports like `clk_i`.
   - gold: `otbn`
3. Explain the likely role of `pwrmgr` from labels `clocked, hierarchical, resettable` and ports like `clk_slow_i`.
   - gold: `pwrmgr`
4. Explain the likely role of `kmac` from labels `clocked, fifo, hierarchical` and ports like `clk_i`.
   - gold: `kmac`
5. Explain the likely role of `lc_ctrl_signal_decode` from labels `clocked, hierarchical, resettable` and ports like `clk_i`.
   - gold: `lc_ctrl_signal_decode`

### documentation_summary

1. Summarize `lc_ctrl` for an engineer who only needs interface, role, and integration context.
   - gold: `lc_ctrl`
2. Summarize `aes_masked_inverse_gf2p4_noreuse` for an engineer who only needs interface, role, and integration context.
   - gold: `aes_masked_inverse_gf2p4_noreuse`
3. Summarize `pinmux_strap_sampling` for an engineer who only needs interface, role, and integration context.
   - gold: `pinmux_strap_sampling`
4. Summarize `uart_core` for an engineer who only needs interface, role, and integration context.
   - gold: `uart_core`
5. Summarize `prim_ram_1p_adv` for an engineer who only needs interface, role, and integration context.
   - gold: `prim_ram_1p_adv`

## L3

### structure_understanding

1. Reconstruct the local hierarchy under `entropy_src_core` and explain what each major child likely contributes.
   - gold: `entropy_src_core`
2. Reconstruct the local hierarchy under `clkmgr` and explain what each major child likely contributes.
   - gold: `clkmgr`
3. Reconstruct the local hierarchy under `ast_clks_byp` and explain what each major child likely contributes.
   - gold: `ast_clks_byp`
4. Reconstruct the local hierarchy under `spi_device` and explain what each major child likely contributes.
   - gold: `spi_device`
5. Reconstruct the local hierarchy under `top_darjeeling` and explain what each major child likely contributes.
   - gold: `top_darjeeling`

### search_navigation

1. Which parent module should be retrieved if the query is centered on child `BSCANE2` rather than the parent name itself?
   - gold: `dmi_jtag_tap`
2. Which parent module should be retrieved if the query is centered on child `prim_fifo_async_simple` rather than the parent name itself?
   - gold: `dmi_cdc`
3. Which parent module should be retrieved if the query is centered on child `dm_csrs` rather than the parent name itself?
   - gold: `dm_top`
4. Which parent module should be retrieved if the query is centered on child `dm_sba` rather than the parent name itself?
   - gold: `dm_top`
5. Which parent module should be retrieved if the query is centered on child `dm_mem` rather than the parent name itself?
   - gold: `dm_top`

### comparison_similarity

1. Compare `entropy_src_core` and `aes_masked_inverse_gf2p4` as candidate alternatives for the same subsystem role.
   - gold: `entropy_src_core, aes_masked_inverse_gf2p4`
2. Compare `entropy_src_core` and `csrng_core` as candidate alternatives for the same subsystem role.
   - gold: `entropy_src_core, csrng_core`
3. Compare `entropy_src_core` and `keymgr` as candidate alternatives for the same subsystem role.
   - gold: `entropy_src_core, keymgr`
4. Compare `entropy_src_core` and `pwrmgr_cdc` as candidate alternatives for the same subsystem role.
   - gold: `entropy_src_core, pwrmgr_cdc`
5. Compare `entropy_src_core` and `otbn` as candidate alternatives for the same subsystem role.
   - gold: `entropy_src_core, otbn`

### function_similarity

1. In L3, identify the module that best represents `apb` behavior and justify it from the knowledge DB.
   - gold: `ibex_cs_registers`
2. In L3, identify the module that best represents `uart` behavior and justify it from the knowledge DB.
   - gold: `keymgr_dpe`
3. In L3, identify the module that best represents `apb` behavior and justify it from the knowledge DB.
   - gold: `top_englishbreakfast`
4. In L3, identify the module that best represents `uart` behavior and justify it from the knowledge DB.
   - gold: `aes_core`
5. In L3, identify the module that best represents `i2c` behavior and justify it from the knowledge DB.
   - gold: `i2c_core`

### generation_design

1. Create a design brief for generating a compatible block around `otp_ctrl_part_unbuf` without breaking ports `clk_i` and `rst_ni`.
   - gold: `otp_ctrl_part_unbuf`
2. Create a design brief for generating a compatible block around `aes_masked_inverse_gf2p8` without breaking ports `a` and `m`.
   - gold: `aes_masked_inverse_gf2p8`
3. Create a design brief for generating a compatible block around `spi_tpm` without breaking ports `clk_in_i` and `clk_out_i`.
   - gold: `spi_tpm`
4. Create a design brief for generating a compatible block around `mbx_ombx` without breaking ports `clk_i` and `rst_ni`.
   - gold: `mbx_ombx`
5. Create a design brief for generating a compatible block around `sysrst_ctrl` without breaking ports `clk_i` and `clk_aon_i`.
   - gold: `sysrst_ctrl`

### code_explanation

1. Explain why `alert_handler` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `alert_handler`
2. Explain why `rom_ctrl` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `rom_ctrl`
3. Explain why `otbn_rf_bignum` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `otbn_rf_bignum`
4. Explain why `ac_range_check` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `ac_range_check`
5. Explain why `clkmgr_byp` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `clkmgr_byp`

### documentation_summary

1. Write a module reference summary for `clkmgr_trans` including role, interface shape, and where it sits in the hierarchy.
   - gold: `clkmgr_trans`
2. Write a module reference summary for `chip_darjeeling_asic` including role, interface shape, and where it sits in the hierarchy.
   - gold: `chip_darjeeling_asic`
3. Write a module reference summary for `ibex_if_stage` including role, interface shape, and where it sits in the hierarchy.
   - gold: `ibex_if_stage`
4. Write a module reference summary for `pinmux` including role, interface shape, and where it sits in the hierarchy.
   - gold: `pinmux`
5. Write a module reference summary for `mbx_sysif` including role, interface shape, and where it sits in the hierarchy.
   - gold: `mbx_sysif`

## L4

### structure_understanding

1. Explain the structural decomposition of `flash_phy` and how its major children likely partition responsibilities.
   - gold: `flash_phy`
2. Explain the structural decomposition of `aes_dom_inverse_gf2p4` and how its major children likely partition responsibilities.
   - gold: `aes_dom_inverse_gf2p4`
3. Explain the structural decomposition of `aes_dom_inverse_gf2p8` and how its major children likely partition responsibilities.
   - gold: `aes_dom_inverse_gf2p8`
4. Explain the structural decomposition of `chip_darjeeling_verilator` and how its major children likely partition responsibilities.
   - gold: `chip_darjeeling_verilator`
5. Explain the structural decomposition of `keymgr_ctrl` and how its major children likely partition responsibilities.
   - gold: `keymgr_ctrl`

### search_navigation

1. If the query starts from reused child `prim_flop_2sync`, which parent contexts should a graph-aware search inspect first?
   - gold: `dmi_cdc, chip_englishbreakfast_cw305`
2. If the query starts from reused child `prim_buf`, which parent contexts should a graph-aware search inspect first?
   - gold: `ibex_if_stage, ibex_if_stage`
3. If the query starts from reused child `prim_flop`, which parent contexts should a graph-aware search inspect first?
   - gold: `pwrmgr_fsm, pwrmgr_fsm`
4. If the query starts from reused child `prim_intr_hw`, which parent contexts should a graph-aware search inspect first?
   - gold: `pwrmgr, gpio`
5. If the query starts from reused child `prim_lc_sync`, which parent contexts should a graph-aware search inspect first?
   - gold: `rv_core_ibex, rv_core_ibex`

### comparison_similarity

1. Compare `entropy_src_core` and `mbx_hostif` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `entropy_src_core, mbx_hostif`
2. Compare `entropy_src_core` and `pwrmgr_fsm` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `entropy_src_core, pwrmgr_fsm`
3. Compare `entropy_src_core` and `chip_englishbreakfast_cw305` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `entropy_src_core, chip_englishbreakfast_cw305`
4. Compare `entropy_src_core` and `i2c_fifos` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `entropy_src_core, i2c_fifos`
5. Compare `entropy_src_core` and `usbdev_iomux` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `entropy_src_core, usbdev_iomux`

### function_similarity

1. Which two modules would you shortlist as functionally similar candidates for `clocked` / `hierarchical` behavior, and why?
   - gold: `clkmgr, dma`
2. Which two modules would you shortlist as functionally similar candidates for `clocked` / `hierarchical` behavior, and why?
   - gold: `clkmgr, ast`
3. Which two modules would you shortlist as functionally similar candidates for `clocked` / `hierarchical` behavior, and why?
   - gold: `clkmgr, otp_ctrl`
4. Which two modules would you shortlist as functionally similar candidates for `clocked` / `hierarchical` behavior, and why?
   - gold: `clkmgr, usbdev`
5. Which two modules would you shortlist as functionally similar candidates for `clocked` / `hierarchical` behavior, and why?
   - gold: `clkmgr, rv_core_ibex`

### generation_design

1. Prepare a generation plan for a replacement or extension of `prim_subreg_shadow` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `prim_subreg_shadow`
2. Prepare a generation plan for a replacement or extension of `soc_dbg_ctrl` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `soc_dbg_ctrl`
3. Prepare a generation plan for a replacement or extension of `flash_ctrl_region_cfg` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `flash_ctrl_region_cfg`
4. Prepare a generation plan for a replacement or extension of `prim_ram_1r1w_async_adv` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `prim_ram_1r1w_async_adv`
5. Prepare a generation plan for a replacement or extension of `aes` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `aes`

### code_explanation

1. Explain the design intent of `otbn_predecode` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `otbn_predecode`
2. Explain the design intent of `rv_plic` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `rv_plic`
3. Explain the design intent of `clkgen_xil7series` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `clkgen_xil7series`
4. Explain the design intent of `prim_mubi12_sync` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `prim_mubi12_sync`
5. Explain the design intent of `prim_mubi16_sync` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `prim_mubi16_sync`

### documentation_summary

1. Draft documentation for `prim_mubi20_sync` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `prim_mubi20_sync`
2. Draft documentation for `prim_mubi24_sync` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `prim_mubi24_sync`
3. Draft documentation for `prim_mubi28_sync` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `prim_mubi28_sync`
4. Draft documentation for `prim_mubi32_sync` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `prim_mubi32_sync`
5. Draft documentation for `prim_mubi4_sync` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `prim_mubi4_sync`

## L5

### structure_understanding

1. Reconstruct the likely subsystem architecture around `prim_mubi8_sync` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `prim_mubi8_sync`
2. Reconstruct the likely subsystem architecture around `tlul_jtag_dtm` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `tlul_jtag_dtm`
3. Reconstruct the likely subsystem architecture around `soc_dbg_ctrl_decode` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `soc_dbg_ctrl_decode`
4. Reconstruct the likely subsystem architecture around `usb_osc` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `usb_osc`
5. Reconstruct the likely subsystem architecture around `prim_clock_div` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `prim_clock_div`

### search_navigation

1. For a graph query starting from shared child `prim_flop_2sync`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `dmi_cdc, chip_englishbreakfast_cw305, rv_plic`
2. For a graph query starting from shared child `prim_buf`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `ibex_if_stage, ibex_if_stage, ibex_load_store_unit`
3. For a graph query starting from shared child `prim_flop`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `pwrmgr_fsm, pwrmgr_fsm, pwrmgr_fsm`
4. For a graph query starting from shared child `prim_intr_hw`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `pwrmgr, gpio, flash_ctrl`
5. For a graph query starting from shared child `prim_lc_sync`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `rv_core_ibex, rv_core_ibex, pwrmgr`

### comparison_similarity

1. Make an architecture-level comparison between `clkmgr` and `flash_ctrl_lcmgr` to decide which is the better template for a new subsystem.
   - gold: `clkmgr, flash_ctrl_lcmgr`
2. Make an architecture-level comparison between `clkmgr` and `otp_ctrl_part_buf` to decide which is the better template for a new subsystem.
   - gold: `clkmgr, otp_ctrl_part_buf`
3. Make an architecture-level comparison between `clkmgr` and `sensor_ctrl` to decide which is the better template for a new subsystem.
   - gold: `clkmgr, sensor_ctrl`
4. Make an architecture-level comparison between `clkmgr` and `hmac` to decide which is the better template for a new subsystem.
   - gold: `clkmgr, hmac`
5. Make an architecture-level comparison between `clkmgr` and `lc_ctrl_fsm` to decide which is the better template for a new subsystem.
   - gold: `clkmgr, lc_ctrl_fsm`

### function_similarity

1. In L5, identify the module that best represents `apb` behavior and justify it from the knowledge DB.
   - gold: `ibex_cs_registers`
2. In L5, identify the module that best represents `uart` behavior and justify it from the knowledge DB.
   - gold: `keymgr_dpe`
3. In L5, identify the module that best represents `apb` behavior and justify it from the knowledge DB.
   - gold: `top_englishbreakfast`
4. In L5, identify the module that best represents `uart` behavior and justify it from the knowledge DB.
   - gold: `aes_core`
5. In L5, identify the module that best represents `i2c` behavior and justify it from the knowledge DB.
   - gold: `i2c_core`

### generation_design

1. Write a design-generation brief for building a new module inspired by `ast_pulse_sync`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `ast_pulse_sync`
2. Write a design-generation brief for building a new module inspired by `rv_timer`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `rv_timer`
3. Write a design-generation brief for building a new module inspired by `clkgen_xil7series`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `clkgen_xil7series`
4. Write a design-generation brief for building a new module inspired by `tlul_socket_m1`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `tlul_socket_m1`
5. Write a design-generation brief for building a new module inspired by `csrng_cmd_stage`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `csrng_cmd_stage`

### code_explanation

1. Explain `aes_key_expand` deeply enough that another engineer could answer follow-up questions about hierarchy, behavior, and likely integration assumptions.
   - gold: `aes_key_expand`
2. Explain `aes_dom_dep_mul_gf2pn_unopt` deeply enough that another engineer could answer follow-up questions about hierarchy, behavior, and likely integration assumptions.
   - gold: `aes_dom_dep_mul_gf2pn_unopt`
3. Explain `csrng` deeply enough that another engineer could answer follow-up questions about hierarchy, behavior, and likely integration assumptions.
   - gold: `csrng`
4. Explain `pattgen` deeply enough that another engineer could answer follow-up questions about hierarchy, behavior, and likely integration assumptions.
   - gold: `pattgen`
5. Explain `tlul_adapter_reg_racl` deeply enough that another engineer could answer follow-up questions about hierarchy, behavior, and likely integration assumptions.
   - gold: `tlul_adapter_reg_racl`

### documentation_summary

1. Produce a high-value design document summary for `sys_osc` that could seed internal docs or review notes for future maintainers.
   - gold: `sys_osc`
2. Produce a high-value design document summary for `aon_osc` that could seed internal docs or review notes for future maintainers.
   - gold: `aon_osc`
3. Produce a high-value design document summary for `io_osc` that could seed internal docs or review notes for future maintainers.
   - gold: `io_osc`
4. Produce a high-value design document summary for `prim_flop_en` that could seed internal docs or review notes for future maintainers.
   - gold: `prim_flop_en`
5. Produce a high-value design document summary for `prim_flop_2sync` that could seed internal docs or review notes for future maintainers.
   - gold: `prim_flop_2sync`
