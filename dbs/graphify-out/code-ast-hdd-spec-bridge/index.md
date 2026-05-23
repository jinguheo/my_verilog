# Code-AST + HDD + Spec-Only Bridge

This report lists information that is not visible from code-ast-only or spec-only alone. Each row connects spec anchors to HDD modules and then to AST internals such as ports, params, always blocks, and functions.

- Integrated records: 96
- Spec bridge edges considered: 12598
- HAS_HDD edges: 277

## Top Integrated Modules

| HDD / AST module | Component | Spec anchors | Code bridge nodes | Ports | Params | Always | Functions |
|---|---|---:|---:|---:|---:|---:|---:|
| `bus` | `ibex` | 114 | 80 | 21 | 4 | 5 | 0 |
| `tb` | `ibex` | 120 | 60 | 0 | 2 | 4 | 0 |
| `formal_tb` | `ibex` | 72 | 80 | 70 | 4 | 10 | 0 |
| `alt_lsu` | `ibex` | 72 | 80 | 24 | 2 | 4 | 0 |
| `prim_ram_1p_adv` | `prim` | 120 | 1 | 15 | 10 | 9 | 0 |
| `prim_packer_fifo` | `prim` | 120 | 5 | 10 | 3 | 2 | 0 |
| `prim_count` | `prim` | 120 | 1 | 12 | 4 | 1 | 2 |
| `clkgen_xil7series` | `ibex` | 72 | 80 | 4 | 0 | 0 | 0 |
| `prim_arbiter_tree` | `prim` | 120 | 1 | 10 | 3 | 2 | 0 |
| `core_ibex_fcov_bind` | `ibex` | 72 | 80 | 0 | 0 | 0 | 0 |
| `prim_arbiter_fixed` | `prim` | 120 | 1 | 9 | 3 | 1 | 0 |
| `prim_esc_receiver` | `prim` | 120 | 1 | 6 | 4 | 3 | 0 |
| `prim_flop_en` | `prim_generic` | 120 | 1 | 5 | 3 | 1 | 0 |
| `prim_sec_anchor_flop` | `prim` | 120 | 1 | 4 | 2 | 0 | 0 |
| `prim_onehot_enc` | `prim` | 120 | 1 | 3 | 1 | 0 | 0 |
| `prim_secded_hamming_72_64_enc` | `prim` | 120 | 1 | 2 | 0 | 1 | 0 |
| `prim_secded_inv_72_64_enc` | `prim` | 120 | 1 | 2 | 0 | 1 | 0 |
| `prim_secded_hamming_76_68_enc` | `prim` | 104 | 1 | 2 | 0 | 1 | 0 |
| `ibex_top` | `ibex` | 55 | 1 | 80 | 37 | 9 | 2 |
| `prim_alert_rxtx_async_assert_fpv` | `prim` | 30 | 80 | 20 | 0 | 1 | 0 |
| `ibex_cs_registers` | `ibex` | 55 | 1 | 71 | 19 | 11 | 1 |
| `prim_alert_rxtx_assert_fpv` | `prim` | 30 | 80 | 17 | 0 | 0 | 0 |
| `prim_alert_receiver` | `prim` | 30 | 80 | 9 | 2 | 2 | 0 |
| `ibex_top_tracing` | `ibex` | 55 | 1 | 54 | 29 | 0 | 0 |
| `prim_alert_rxtx_async_bind_fpv` | `prim` | 30 | 80 | 0 | 0 | 0 | 0 |
| `prim_alert_rxtx_async_fatal_bind_fpv` | `prim` | 30 | 80 | 0 | 0 | 0 | 0 |
| `ibex_compressed_decoder` | `ibex` | 55 | 1 | 9 | 2 | 4 | 13 |
| `top` | `ibex` | 40 | 4 | 55 | 7 | 1 | 0 |
| `prim_reg_cdc` | `prim` | 42 | 1 | 17 | 4 | 2 | 0 |
| `prim_sync_reqack` | `prim` | 40 | 1 | 9 | 2 | 11 | 0 |
| `tb_cs_registers` | `ibex` | 40 | 4 | 3 | 10 | 2 | 0 |
| `prim_filter` | `prim` | 42 | 1 | 5 | 2 | 2 | 0 |
| `prim_clock_buf` | `prim_generic` | 38 | 6 | 4 | 4 | 0 | 0 |
| `prim_lc_or_hardened` | `prim` | 42 | 1 | 5 | 0 | 0 | 0 |
| `prim_rst_sync` | `prim_generic` | 40 | 1 | 5 | 2 | 0 | 0 |
| `prim_mubi4_sync` | `prim` | 36 | 1 | 4 | 4 | 3 | 0 |
| `prim_mubi4_sender` | `prim` | 36 | 1 | 4 | 3 | 1 | 0 |
| `prim_intr_hw` | `prim` | 33 | 1 | 10 | 3 | 2 | 0 |
| `prim_sync_reqack_data` | `prim` | 31 | 1 | 11 | 5 | 3 | 0 |
| `prim_pulse_sync` | `prim` | 33 | 1 | 6 | 0 | 3 | 0 |
| `prim_lc_sync` | `prim` | 31 | 1 | 4 | 3 | 2 | 0 |
| `prim_edge_detector` | `prim` | 30 | 1 | 6 | 3 | 1 | 0 |
| `prim_lc_sender` | `prim` | 31 | 1 | 4 | 2 | 1 | 0 |
| `prim_sec_anchor_buf` | `prim` | 31 | 1 | 2 | 1 | 0 | 0 |
| `prim_ram_1p_scr` | `prim` | 13 | 5 | 23 | 10 | 2 | 0 |
| `prim_secded_hamming_76_68_dec` | `prim` | 24 | 1 | 4 | 0 | 1 | 0 |
| `prim_prince` | `prim` | 13 | 5 | 8 | 6 | 12 | 0 |
| `prim_fifo_async_sram_adapter` | `prim` | 9 | 1 | 33 | 5 | 5 | 2 |
| `prim_ram_2p_async_adv` | `prim` | 10 | 1 | 22 | 9 | 7 | 0 |
| `prim_sha2_32` | `prim` | 10 | 1 | 21 | 1 | 6 | 0 |
| `prim_esc_sender` | `prim` | 12 | 1 | 8 | 1 | 2 | 0 |
| `prim_flash` | `prim_generic` | 2 | 5 | 25 | 8 | 0 | 0 |
| `prim_packer` | `prim` | 3 | 5 | 13 | 4 | 9 | 0 |
| `prim_mubi8_sync` | `prim` | 10 | 1 | 4 | 4 | 3 | 0 |
| `prim_ascon_duplex` | `prim` | 1 | 1 | 24 | 0 | 13 | 0 |
| `prim_fifo_async` | `prim` | 5 | 1 | 12 | 4 | 7 | 2 |
| `prim_slicer` | `prim` | 9 | 1 | 3 | 3 | 0 | 0 |
| `prim_subreg` | `prim` | 6 | 1 | 10 | 4 | 1 | 0 |
| `prim_max_tree` | `prim` | 6 | 1 | 7 | 2 | 0 | 2 |
| `prim_present` | `prim` | 3 | 5 | 6 | 5 | 0 | 0 |
| `prim_subreg_ext` | `prim` | 6 | 1 | 9 | 1 | 0 | 0 |
| `prim_xoshiro256pp` | `prim` | 3 | 4 | 8 | 3 | 1 | 1 |
| `prim_ascon_duplex_tb` | `prim` | 1 | 4 | 4 | 6 | 7 | 0 |
| `prim_lfsr_tb` | `prim` | 2 | 4 | 7 | 7 | 0 | 0 |
| `prim_clock_div` | `prim_generic` | 2 | 5 | 6 | 2 | 3 | 0 |
| `prim_clock_inv` | `prim_generic` | 3 | 6 | 3 | 2 | 0 | 0 |
| `prim_reg_we_check` | `prim` | 6 | 1 | 5 | 1 | 0 | 0 |
| `prim_subreg_shadow` | `prim` | 1 | 1 | 15 | 4 | 1 | 0 |
| `ibex_icache_fcov_bind` | `ibex` | 5 | 4 | 0 | 0 | 0 | 0 |
| `prim_secded_inv_39_32_dec` | `prim` | 5 | 1 | 4 | 0 | 1 | 0 |
| `prim_secded_inv_64_57_dec` | `prim` | 5 | 1 | 4 | 0 | 1 | 0 |
| `prim_sync_reqack_tb` | `prim` | 1 | 2 | 4 | 0 | 10 | 0 |
| `prim_and2` | `prim_generic` | 2 | 5 | 3 | 1 | 0 | 0 |
| `prim_secded_inv_39_32_enc` | `prim` | 5 | 1 | 2 | 0 | 1 | 0 |
| `prim_secded_inv_64_57_enc` | `prim` | 5 | 1 | 2 | 0 | 1 | 0 |
| `prim_ascon_round_tb` | `prim` | 1 | 4 | 4 | 1 | 3 | 0 |
| `prim_buf` | `prim_generic` | 2 | 5 | 2 | 1 | 0 | 0 |
| `prim_mubi32_sync` | `prim` | 1 | 1 | 4 | 4 | 3 | 0 |
| `prim_clock_mux2` | `prim_generic` | 1 | 1 | 8 | 2 | 0 | 0 |
| `prim_secded_hamming_22_16_assert_fpv` | `prim` | 1 | 2 | 8 | 0 | 0 | 0 |
| `prim_secded_hamming_39_32_assert_fpv` | `prim` | 1 | 2 | 8 | 0 | 0 | 0 |
| `prim_secded_hamming_72_64_assert_fpv` | `prim` | 1 | 2 | 8 | 0 | 0 | 0 |
| `prim_secded_hamming_76_68_assert_fpv` | `prim` | 1 | 2 | 8 | 0 | 0 | 0 |
| `prim_secded_inv_hamming_22_16_assert_fpv` | `prim` | 1 | 2 | 8 | 0 | 0 | 0 |
| `prim_secded_inv_hamming_39_32_assert_fpv` | `prim` | 1 | 2 | 8 | 0 | 0 | 0 |
| `prim_secded_inv_hamming_72_64_assert_fpv` | `prim` | 1 | 2 | 8 | 0 | 0 | 0 |
| `prim_secded_inv_hamming_76_68_assert_fpv` | `prim` | 1 | 2 | 8 | 0 | 0 | 0 |
| `prim_flop_2sync` | `prim_generic` | 1 | 1 | 4 | 3 | 1 | 0 |
| `prim_subst_perm` | `prim` | 1 | 1 | 3 | 3 | 2 | 0 |
| `prim_leading_one_ppc` | `prim` | 1 | 1 | 4 | 1 | 2 | 0 |
| `prim_racl_error_arb` | `prim` | 1 | 1 | 4 | 1 | 0 | 0 |
| `ibex_simple_system_cosim_checker_bind` | `ibex` | 1 | 2 | 0 | 0 | 0 | 0 |
| `prim_secded_inv_hamming_22_16_bind_fpv` | `prim` | 1 | 2 | 0 | 0 | 0 | 0 |
| `prim_secded_inv_hamming_39_32_bind_fpv` | `prim` | 1 | 2 | 0 | 0 | 0 | 0 |
| `prim_secded_inv_hamming_72_64_bind_fpv` | `prim` | 1 | 2 | 0 | 0 | 0 | 0 |
| `prim_secded_inv_hamming_76_68_bind_fpv` | `prim` | 1 | 2 | 0 | 0 | 0 | 0 |
