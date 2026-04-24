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
5. In L1, explain the structure of `top_englishbreakfast` using ports, labels, and child instances.
   - gold: `top_englishbreakfast`

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
3. Which module is tagged as `fifo` and would be the most direct example of that function?
   - gold: `flash_ctrl`
4. Which module is tagged as `fifo` and would be the most direct example of that function?
   - gold: `generated`
5. In L1, identify the module that best represents `uart` behavior and justify it from the knowledge DB.
   - gold: `clkmgr`

### generation_design

1. If you needed a very small wrapper around `otbn_alu_bignum`, which existing module should you inspect first as the reference block?
   - gold: `otbn_alu_bignum`
2. If you needed a very small wrapper around `clkmgr`, which existing module should you inspect first as the reference block?
   - gold: `clkmgr`
3. If you needed a very small wrapper around `ibex_cs_registers`, which existing module should you inspect first as the reference block?
   - gold: `ibex_cs_registers`
4. If you needed a very small wrapper around `keymgr_dpe`, which existing module should you inspect first as the reference block?
   - gold: `keymgr_dpe`
5. In L1, write a generation/design prompt for extending `generated` while preserving its interface intent.
   - gold: `generated`

### code_explanation

1. Explain in simple terms what module `top_darjeeling` appears to do from its ports, labels, and file path.
   - gold: `top_darjeeling`
2. Explain in simple terms what module `generated` appears to do from its ports, labels, and file path.
   - gold: `generated`
3. Explain in simple terms what module `top_earlgrey` appears to do from its ports, labels, and file path.
   - gold: `top_earlgrey`
4. Explain in simple terms what module `dma` appears to do from its ports, labels, and file path.
   - gold: `dma`
5. Explain in simple terms what module `ast` appears to do from its ports, labels, and file path.
   - gold: `ast`

### documentation_summary

1. Write a short design-note summary for module `otp_ctrl` using only the current knowledge DB facts.
   - gold: `otp_ctrl`
2. Write a short design-note summary for module `ast` using only the current knowledge DB facts.
   - gold: `ast`
3. Write a short design-note summary for module `usbdev` using only the current knowledge DB facts.
   - gold: `usbdev`
4. Write a short design-note summary for module `rv_core_ibex` using only the current knowledge DB facts.
   - gold: `rv_core_ibex`
5. In L1, produce a concise documentation summary for `ibex_cs_registers` from the current knowledge DB.
   - gold: `ibex_cs_registers`

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

1. Which of `entropy_src_core` and `generated` are structurally closer based on shared labels and interface shape?
   - gold: `entropy_src_core, generated`
2. Which of `entropy_src_core` and `top_earlgrey` are structurally closer based on shared labels and interface shape?
   - gold: `entropy_src_core, top_earlgrey`
3. Which of `entropy_src_core` and `dma` are structurally closer based on shared labels and interface shape?
   - gold: `entropy_src_core, dma`
4. Which of `entropy_src_core` and `ast` are structurally closer based on shared labels and interface shape?
   - gold: `entropy_src_core, ast`
5. Which of `entropy_src_core` and `otp_ctrl` are structurally closer based on shared labels and interface shape?
   - gold: `entropy_src_core, otp_ctrl`

### function_similarity

1. Find two modules that both behave like `clocked` blocks and explain the common function.
   - gold: `debug_rom, debug_rom_one_scratch`
2. Find two modules that both behave like `hierarchical` blocks and explain the common function.
   - gold: `dmi_jtag_tap, dmi_cdc`
3. Find two modules that both behave like `resettable` blocks and explain the common function.
   - gold: `debug_rom, debug_rom_one_scratch`
4. Find two modules that both behave like `uart` blocks and explain the common function.
   - gold: `top_englishbreakfast, rv_plic`
5. Find two modules that both behave like `fifo` blocks and explain the common function.
   - gold: `dmi_cdc, dm_csrs`

### generation_design

1. If you were generating a thin wrapper around `otbn_alu_bignum`, which child block and interface signals must be preserved first?
   - gold: `otbn_alu_bignum`
2. If you were generating a thin wrapper around `clkmgr`, which child block and interface signals must be preserved first?
   - gold: `clkmgr`
3. If you were generating a thin wrapper around `ibex_cs_registers`, which child block and interface signals must be preserved first?
   - gold: `ibex_cs_registers`
4. If you were generating a thin wrapper around `keymgr_dpe`, which child block and interface signals must be preserved first?
   - gold: `keymgr_dpe`
5. If you were generating a thin wrapper around `top_englishbreakfast`, which child block and interface signals must be preserved first?
   - gold: `top_englishbreakfast`

### code_explanation

1. Explain the likely role of `sram_ctrl` from labels `clocked, hierarchical, resettable` and ports like `clk_i`.
   - gold: `sram_ctrl`
2. Explain the likely role of `aes_masked_inverse_gf2p4` from labels `hierarchical` and ports like `b`.
   - gold: `aes_masked_inverse_gf2p4`
3. Explain the likely role of `instantiates` from labels `clocked, hierarchical, spi` and ports like `clk_scan_i`.
   - gold: `instantiates`
4. Explain the likely role of `csrng_core` from labels `clocked, fifo, hierarchical` and ports like `clk_i`.
   - gold: `csrng_core`
5. Explain the likely role of `keymgr` from labels `clocked, hierarchical, resettable` and ports like `clk_i`.
   - gold: `keymgr`

### documentation_summary

1. Summarize `pwrmgr` for an engineer who only needs interface, role, and integration context.
   - gold: `pwrmgr`
2. Summarize `kmac` for an engineer who only needs interface, role, and integration context.
   - gold: `kmac`
3. Summarize `lc_ctrl_signal_decode` for an engineer who only needs interface, role, and integration context.
   - gold: `lc_ctrl_signal_decode`
4. Summarize `otbn_controller` for an engineer who only needs interface, role, and integration context.
   - gold: `otbn_controller`
5. Summarize `lc_ctrl` for an engineer who only needs interface, role, and integration context.
   - gold: `lc_ctrl`

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

1. Compare `entropy_src_core` and `aes_core` as candidate alternatives for the same subsystem role.
   - gold: `entropy_src_core, aes_core`
2. Compare `entropy_src_core` and `i2c_core` as candidate alternatives for the same subsystem role.
   - gold: `entropy_src_core, i2c_core`
3. Compare `entropy_src_core` and `supports` as candidate alternatives for the same subsystem role.
   - gold: `entropy_src_core, supports`
4. Compare `entropy_src_core` and `sram_ctrl` as candidate alternatives for the same subsystem role.
   - gold: `entropy_src_core, sram_ctrl`
5. Compare `entropy_src_core` and `aes_masked_inverse_gf2p4` as candidate alternatives for the same subsystem role.
   - gold: `entropy_src_core, aes_masked_inverse_gf2p4`

### function_similarity

1. In L3, identify the module that best represents `uart` behavior and justify it from the knowledge DB.
   - gold: `clkmgr`
2. In L3, identify the module that best represents `apb` behavior and justify it from the knowledge DB.
   - gold: `ibex_cs_registers`
3. In L3, identify the module that best represents `uart` behavior and justify it from the knowledge DB.
   - gold: `keymgr_dpe`
4. In L3, identify the module that best represents `fifo` behavior and justify it from the knowledge DB.
   - gold: `top_englishbreakfast`
5. In L3, identify the module that best represents `uart` behavior and justify it from the knowledge DB.
   - gold: `implements`

### generation_design

1. Create a design brief for generating a compatible block around `flash_ctrl_lcmgr` without breaking ports `clk_i` and `rst_ni`.
   - gold: `flash_ctrl_lcmgr`
2. Create a design brief for generating a compatible block around `otp_ctrl_part_buf` without breaking ports `clk_i` and `rst_ni`.
   - gold: `otp_ctrl_part_buf`
3. Create a design brief for generating a compatible block around `sensor_ctrl` without breaking ports `clk_i` and `rst_ni`.
   - gold: `sensor_ctrl`
4. Create a design brief for generating a compatible block around `hmac` without breaking ports `clk_i` and `rst_ni`.
   - gold: `hmac`
5. Create a design brief for generating a compatible block around `lc_ctrl_fsm` without breaking ports `clk_i` and `rst_ni`.
   - gold: `lc_ctrl_fsm`

### code_explanation

1. Explain why `otp_ctrl_part_unbuf` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `otp_ctrl_part_unbuf`
2. Explain why `spi_tpm` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `spi_tpm`
3. Explain why `mbx_ombx` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `mbx_ombx`
4. Explain why `latches` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `latches`
5. Explain why `sysrst_ctrl` probably exists in the design, using both its semantic labels and its child-instance graph.
   - gold: `sysrst_ctrl`

### documentation_summary

1. Write a module reference summary for `prim_ram_2p_async_adv` including role, interface shape, and where it sits in the hierarchy.
   - gold: `prim_ram_2p_async_adv`
2. Write a module reference summary for `spi_host` including role, interface shape, and where it sits in the hierarchy.
   - gold: `spi_host`
3. Write a module reference summary for `alert_handler` including role, interface shape, and where it sits in the hierarchy.
   - gold: `alert_handler`
4. Write a module reference summary for `rom_ctrl` including role, interface shape, and where it sits in the hierarchy.
   - gold: `rom_ctrl`
5. Write a module reference summary for `otbn_rf_bignum` including role, interface shape, and where it sits in the hierarchy.
   - gold: `otbn_rf_bignum`

## L4

### structure_understanding

1. Explain the structural decomposition of `clkmgr_byp` and how its major children likely partition responsibilities.
   - gold: `clkmgr_byp`
2. Explain the structural decomposition of `clkmgr_trans` and how its major children likely partition responsibilities.
   - gold: `clkmgr_trans`
3. Explain the structural decomposition of `chip_darjeeling_asic` and how its major children likely partition responsibilities.
   - gold: `chip_darjeeling_asic`
4. Explain the structural decomposition of `ibex_if_stage` and how its major children likely partition responsibilities.
   - gold: `ibex_if_stage`
5. Explain the structural decomposition of `instantiates` and how its major children likely partition responsibilities.
   - gold: `instantiates`

### search_navigation

1. If the query starts from reused child `prim_flop_2sync`, which parent contexts should a graph-aware search inspect first?
   - gold: `dmi_cdc, chip_englishbreakfast_cw305`
2. If the query starts from reused child `prim_buf`, which parent contexts should a graph-aware search inspect first?
   - gold: `ibex_if_stage, ibex_if_stage`
3. If the query starts from reused child `prim_flop`, which parent contexts should a graph-aware search inspect first?
   - gold: `instantiates, instantiates`
4. If the query starts from reused child `prim_intr_hw`, which parent contexts should a graph-aware search inspect first?
   - gold: `pwrmgr, gpio`
5. If the query starts from reused child `prim_lc_sync`, which parent contexts should a graph-aware search inspect first?
   - gold: `rv_core_ibex, rv_core_ibex`

### comparison_similarity

1. Compare `entropy_src_core` and `flash_phy` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `entropy_src_core, flash_phy`
2. Compare `entropy_src_core` and `which` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `entropy_src_core, which`
3. Compare `entropy_src_core` and `aes_dom_inverse_gf2p4` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `entropy_src_core, aes_dom_inverse_gf2p4`
4. Compare `entropy_src_core` and `aes_dom_inverse_gf2p8` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `entropy_src_core, aes_dom_inverse_gf2p8`
5. Compare `entropy_src_core` and `chip_darjeeling_verilator` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.
   - gold: `entropy_src_core, chip_darjeeling_verilator`

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

1. Prepare a generation plan for a replacement or extension of `chip_englishbreakfast_cw305` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `chip_englishbreakfast_cw305`
2. Prepare a generation plan for a replacement or extension of `i2c_fifos` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `i2c_fifos`
3. Prepare a generation plan for a replacement or extension of `generated` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `generated`
4. Prepare a generation plan for a replacement or extension of `usbdev_iomux` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `usbdev_iomux`
5. Prepare a generation plan for a replacement or extension of `otbn_rf_base` that preserves hierarchy, interface intent, and likely child dependencies.
   - gold: `otbn_rf_base`

### code_explanation

1. Explain the design intent of `generates` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `generates`
2. Explain the design intent of `otbn_rf_bignum_ff` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `otbn_rf_bignum_ff`
3. Explain the design intent of `tlul_fifo_sync` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `tlul_fifo_sync`
4. Explain the design intent of `clkgen_xil_ultrascale` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `clkgen_xil_ultrascale`
5. Explain the design intent of `tlul_request_loopback` as if onboarding another RTL engineer who needs both behavior and integration context.
   - gold: `tlul_request_loopback`

### documentation_summary

1. Draft documentation for `pinmux_jtag_buf` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `pinmux_jtag_buf`
2. Draft documentation for `prim_trivium_tb` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `prim_trivium_tb`
3. Draft documentation for `usb_fs_nb_pe` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `usb_fs_nb_pe`
4. Draft documentation for `controls` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `controls`
5. Draft documentation for `keymgr_dpe_ctrl` that includes role, dependencies, exposed interface, and likely upstream/downstream context.
   - gold: `keymgr_dpe_ctrl`

## L5

### structure_understanding

1. Reconstruct the likely subsystem architecture around `mbx_imbx` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `mbx_imbx`
2. Reconstruct the likely subsystem architecture around `prim_subreg_shadow` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `prim_subreg_shadow`
3. Reconstruct the likely subsystem architecture around `soc_dbg_ctrl` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `soc_dbg_ctrl`
4. Reconstruct the likely subsystem architecture around `that` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `that`
5. Reconstruct the likely subsystem architecture around `flash_ctrl_region_cfg` and identify which child blocks are control, buffering, or transport oriented.
   - gold: `flash_ctrl_region_cfg`

### search_navigation

1. For a graph query starting from shared child `prim_flop_2sync`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `dmi_cdc, chip_englishbreakfast_cw305, rv_plic`
2. For a graph query starting from shared child `prim_buf`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `ibex_if_stage, ibex_if_stage, ibex_load_store_unit`
3. For a graph query starting from shared child `prim_flop`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `instantiates, instantiates, stretches`
4. For a graph query starting from shared child `prim_intr_hw`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `pwrmgr, gpio, flash_ctrl`
5. For a graph query starting from shared child `prim_lc_sync`, how should retrieval disambiguate among multiple parent contexts?
   - gold: `rv_core_ibex, rv_core_ibex, pwrmgr`

### comparison_similarity

1. Make an architecture-level comparison between `clkmgr` and `will` to decide which is the better template for a new subsystem.
   - gold: `clkmgr, will`
2. Make an architecture-level comparison between `clkmgr` and `aes_masked_inverse_gf2p4_noreuse` to decide which is the better template for a new subsystem.
   - gold: `clkmgr, aes_masked_inverse_gf2p4_noreuse`
3. Make an architecture-level comparison between `clkmgr` and `pinmux_strap_sampling` to decide which is the better template for a new subsystem.
   - gold: `clkmgr, pinmux_strap_sampling`
4. Make an architecture-level comparison between `clkmgr` and `uart_core` to decide which is the better template for a new subsystem.
   - gold: `clkmgr, uart_core`
5. Make an architecture-level comparison between `clkmgr` and `prim_ram_1p_adv` to decide which is the better template for a new subsystem.
   - gold: `clkmgr, prim_ram_1p_adv`

### function_similarity

1. In L5, identify the module that best represents `uart` behavior and justify it from the knowledge DB.
   - gold: `clkmgr`
2. In L5, identify the module that best represents `apb` behavior and justify it from the knowledge DB.
   - gold: `ibex_cs_registers`
3. In L5, identify the module that best represents `uart` behavior and justify it from the knowledge DB.
   - gold: `keymgr_dpe`
4. In L5, identify the module that best represents `apb` behavior and justify it from the knowledge DB.
   - gold: `top_englishbreakfast`
5. In L5, identify the module that best represents `uart` behavior and justify it from the knowledge DB.
   - gold: `implements`

### generation_design

1. Write a design-generation brief for building a new module inspired by `decodes`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `decodes`
2. Write a design-generation brief for building a new module inspired by `prim_clock_div`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `prim_clock_div`
3. Write a design-generation brief for building a new module inspired by `stretches`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `stretches`
4. Write a design-generation brief for building a new module inspired by `aes_sbox_tb`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `aes_sbox_tb`
5. Write a design-generation brief for building a new module inspired by `chip_earlgrey_asic`, including preserved interfaces, child-role decomposition, and likely review risks.
   - gold: `chip_earlgrey_asic`

### code_explanation

1. Explain `prim_pad_wrapper` deeply enough that another engineer could answer follow-up questions about hierarchy, behavior, and likely integration assumptions.
   - gold: `prim_pad_wrapper`
2. Explain `dmi_cdc` deeply enough that another engineer could answer follow-up questions about hierarchy, behavior, and likely integration assumptions.
   - gold: `dmi_cdc`
3. Explain `clkmgr_meas_chk` deeply enough that another engineer could answer follow-up questions about hierarchy, behavior, and likely integration assumptions.
   - gold: `clkmgr_meas_chk`
4. Explain `entropy_src_markov_ht` deeply enough that another engineer could answer follow-up questions about hierarchy, behavior, and likely integration assumptions.
   - gold: `entropy_src_markov_ht`
5. Explain `entropy_src_adaptp_ht` deeply enough that another engineer could answer follow-up questions about hierarchy, behavior, and likely integration assumptions.
   - gold: `entropy_src_adaptp_ht`

### documentation_summary

1. Produce a high-value design document summary for `ascon` that could seed internal docs or review notes for future maintainers.
   - gold: `ascon`
2. Produce a high-value design document summary for `instantiates` that could seed internal docs or review notes for future maintainers.
   - gold: `instantiates`
3. Produce a high-value design document summary for `will` that could seed internal docs or review notes for future maintainers.
   - gold: `will`
4. Produce a high-value design document summary for `that` that could seed internal docs or review notes for future maintainers.
   - gold: `that`
5. Produce a high-value design document summary for `racl_ctrl` that could seed internal docs or review notes for future maintainers.
   - gold: `racl_ctrl`
