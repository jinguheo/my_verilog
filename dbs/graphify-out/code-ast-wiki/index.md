# Code-AST Wiki

This wiki is generated from the Graphify code-ast graph. It shows module-level AST details instead of community-level clusters.

- Modules: 277
- Ports: 2734
- Params: 664
- Always blocks: 507
- Functions: 80

## Module Kinds

| Kind | Count |
|---|---:|
| `rtl` | 187 |
| `other` | 46 |
| `testbench` | 34 |
| `dv` | 7 |
| `dv/formal` | 3 |

## Top Modules By Interface Size

| Module | Project | Kind | Ports | Params | Always | Functions | File |
|---|---|---|---:|---:|---:|---:|---|
| `ibex_id_stage` | `ibex` | `rtl` | 118 | 8 | 12 | 0 | `dbs\ibex\rtl\ibex_id_stage.sv` |
| `ibex_top` | `ibex` | `rtl` | 92 | 37 | 9 | 2 | `dbs\ibex\rtl\ibex_top.sv` |
| `ibex_cs_registers` | `ibex` | `rtl` | 71 | 19 | 11 | 1 | `dbs\ibex\rtl\ibex_cs_registers.sv` |
| `ibex_controller` | `ibex` | `rtl` | 65 | 3 | 9 | 0 | `dbs\ibex\rtl\ibex_controller.sv` |
| `ibex_if_stage` | `ibex` | `rtl` | 62 | 17 | 15 | 2 | `dbs\ibex\rtl\ibex_if_stage.sv` |
| `ibex_lockstep` | `ibex` | `rtl` | 58 | 41 | 5 | 0 | `dbs\ibex\rtl\ibex_lockstep.sv` |
| `top` | `ibex` | `dv/formal` | 55 | 7 | 1 | 0 | `dbs\ibex\dv\formal\check\top.sv` |
| `spec_api` | `ibex` | `dv/formal` | 55 | 2 | 0 | 0 | `dbs\ibex\dv\formal\spec\spec_api.sv` |
| `ibex_top_tracing` | `ibex` | `rtl` | 54 | 29 | 0 | 0 | `dbs\ibex\rtl\ibex_top_tracing.sv` |
| `ibex_decoder` | `ibex` | `rtl` | 51 | 4 | 4 | 0 | `dbs\ibex\rtl\ibex_decoder.sv` |
| `prim_fifo_async_sram_adapter` | `ibex` | `rtl` | 33 | 5 | 5 | 2 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_fifo_async_sram_adapter.sv` |
| `ibex_load_store_unit` | `ibex` | `rtl` | 31 | 2 | 12 | 0 | `dbs\ibex\rtl\ibex_load_store_unit.sv` |
| `ibex_wb_stage` | `ibex` | `rtl` | 30 | 3 | 5 | 0 | `dbs\ibex\rtl\ibex_wb_stage.sv` |
| `ibex_tracer` | `ibex` | `rtl` | 28 | 0 | 2 | 41 | `dbs\ibex\rtl\ibex_tracer.sv` |
| `ibex_ex_block` | `ibex` | `rtl` | 26 | 3 | 0 | 0 | `dbs\ibex\rtl\ibex_ex_block.sv` |
| `prim_flash` | `ibex` | `rtl` | 25 | 8 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim_generic\rtl\prim_flash.sv` |
| `alt_lsu` | `ibex` | `dv/formal` | 24 | 2 | 4 | 0 | `dbs\ibex\dv\formal\check\peek\alt_lsu.sv` |
| `prim_ascon_duplex` | `ibex` | `rtl` | 24 | 0 | 13 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ascon_duplex.sv` |
| `prim_ram_1p_scr` | `ibex` | `rtl` | 23 | 10 | 2 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ram_1p_scr.sv` |
| `prim_ram_2p_async_adv` | `ibex` | `rtl` | 22 | 9 | 7 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ram_2p_async_adv.sv` |
| `prim_generic_flash_bank` | `ibex` | `rtl` | 22 | 6 | 6 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim_generic\rtl\prim_generic_flash_bank.sv` |
| `ibex_multdiv_fast` | `ibex` | `rtl` | 22 | 1 | 7 | 0 | `dbs\ibex\rtl\ibex_multdiv_fast.sv` |
| `formal_tb` | `ibex` | `testbench` | 70 | 4 | 10 | 0 | `dbs\ibex\formal\data_ind_timing\formal_tb.sv` |
| `ibex_multdiv_slow` | `ibex` | `rtl` | 22 | 0 | 3 | 0 | `dbs\ibex\rtl\ibex_multdiv_slow.sv` |
| `bus` | `ibex` | `rtl` | 21 | 4 | 5 | 0 | `dbs\ibex\shared\rtl\bus.sv` |
| `prim_sha2_32` | `ibex` | `rtl` | 21 | 1 | 6 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_sha2_32.sv` |
| `prim_alert_rxtx_async_fatal_tb` | `ibex` | `testbench` | 20 | 0 | 1 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_alert_rxtx_async_fatal_tb.sv` |
| `prim_alert_rxtx_async_tb` | `ibex` | `testbench` | 20 | 0 | 1 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_alert_rxtx_async_tb.sv` |
| `prim_alert_rxtx_async_assert_fpv` | `ibex` | `other` | 20 | 0 | 1 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_alert_rxtx_async_assert_fpv.sv` |
| `prim_ram_2p_adv` | `ibex` | `rtl` | 19 | 9 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ram_2p_adv.sv` |
| `prim_sram_arbiter` | `ibex` | `rtl` | 19 | 5 | 1 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_sram_arbiter.sv` |
| `ibex_prefetch_buffer` | `ibex` | `rtl` | 18 | 1 | 5 | 0 | `dbs\ibex\rtl\ibex_prefetch_buffer.sv` |
| `prim_reg_cdc` | `ibex` | `rtl` | 17 | 4 | 2 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_reg_cdc.sv` |
| `prim_sha2_pad` | `ibex` | `rtl` | 17 | 1 | 7 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_sha2_pad.sv` |
| `prim_alert_rxtx_fatal_tb` | `ibex` | `testbench` | 17 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_alert_rxtx_fatal_tb.sv` |
| `prim_alert_rxtx_tb` | `ibex` | `testbench` | 17 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_alert_rxtx_tb.sv` |
| `prim_alert_rxtx_assert_fpv` | `ibex` | `other` | 17 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_alert_rxtx_assert_fpv.sv` |
| `ram_2p` | `ibex` | `rtl` | 16 | 3 | 2 | 0 | `dbs\ibex\shared\rtl\ram_2p.sv` |
| `prim_ram_1p_adv` | `ibex` | `rtl` | 15 | 10 | 9 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ram_1p_adv.sv` |
| `prim_ram_1r1w_async_adv` | `ibex` | `rtl` | 15 | 9 | 5 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ram_1r1w_async_adv.sv` |
| `prim_subreg_shadow` | `ibex` | `rtl` | 15 | 4 | 1 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_subreg_shadow.sv` |
| `ibex_alu` | `ibex` | `rtl` | 15 | 1 | 25 | 0 | `dbs\ibex\rtl\ibex_alu.sv` |
| `riscv_testutil` | `ibex` | `dv` | 15 | 0 | 6 | 0 | `dbs\ibex\dv\riscv_compliance\rtl\riscv_testutil.sv` |
| `prim_sdc_example` | `ibex` | `rtl` | 15 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_sdc_example.sv` |
| `prim_trivium` | `ibex` | `rtl` | 14 | 6 | 6 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_trivium.sv` |
| `ibex_fetch_fifo` | `ibex` | `rtl` | 14 | 2 | 6 | 0 | `dbs\ibex\rtl\ibex_fetch_fifo.sv` |
| `prim_ram_1r1w_adv` | `ibex` | `rtl` | 13 | 9 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_ram_1r1w_adv.sv` |
| `prim_packer` | `ibex` | `rtl` | 13 | 4 | 9 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer.sv` |
| `prim_ram_1r1w` | `ibex` | `rtl` | 13 | 4 | 2 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim_generic\rtl\prim_ram_1r1w.sv` |
| `prim_packer_tb` | `ibex` | `testbench` | 13 | 2 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_packer_tb.sv` |
| `ibex_register_file_fpga` | `ibex` | `rtl` | 12 | 4 | 1 | 0 | `dbs\ibex\rtl\ibex_register_file_fpga.sv` |
| `ibex_register_file_latch` | `ibex` | `rtl` | 12 | 4 | 4 | 0 | `dbs\ibex\rtl\ibex_register_file_latch.sv` |
| `prim_clock_meas` | `ibex` | `rtl` | 12 | 4 | 4 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_clock_meas.sv` |
| `prim_count` | `ibex` | `rtl` | 12 | 4 | 1 | 2 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_count.sv` |
| `prim_edn_req` | `ibex` | `rtl` | 12 | 4 | 6 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_edn_req.sv` |
| `prim_fifo_async` | `ibex` | `rtl` | 12 | 4 | 7 | 2 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_fifo_async.sv` |
| `prim_fifo_sync_tb` | `ibex` | `testbench` | 12 | 3 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_fifo_sync_tb.sv` |
| `prim_reg_cdc_arb` | `ibex` | `rtl` | 12 | 3 | 6 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_reg_cdc_arb.sv` |
| `prim_count_tb` | `ibex` | `testbench` | 12 | 2 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_count_tb.sv` |
| `prim_sync_reqack_data` | `ibex` | `rtl` | 11 | 5 | 3 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_sync_reqack_data.sv` |
| `prim_arbiter_tree_dup` | `ibex` | `rtl` | 11 | 4 | 1 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_arbiter_tree_dup.sv` |
| `timer` | `ibex` | `rtl` | 11 | 2 | 6 | 0 | `dbs\ibex\shared\rtl\timer.sv` |
| `prim_dom_and_2share` | `ibex` | `rtl` | 11 | 2 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_dom_and_2share.sv` |
| `prim_esc_rxtx_assert_fpv` | `ibex` | `other` | 11 | 1 | 2 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_esc_rxtx_assert_fpv.sv` |
| `prim_esc_rxtx_tb` | `ibex` | `testbench` | 11 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_esc_rxtx_tb.sv` |
| `prim_subreg` | `ibex` | `rtl` | 10 | 4 | 1 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_subreg.sv` |
| `prim_ram_1p` | `ibex` | `rtl` | 20 | 8 | 2 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim_generic\rtl\prim_ram_1p.sv` |
| `prim_arbiter_ppc_tb` | `ibex` | `testbench` | 10 | 3 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_arbiter_ppc_tb.sv` |
| `prim_arbiter_tree_tb` | `ibex` | `testbench` | 10 | 3 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_arbiter_tree_tb.sv` |
| `prim_arbiter_ppc` | `ibex` | `rtl` | 10 | 3 | 3 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_arbiter_ppc.sv` |
| `prim_arbiter_tree` | `ibex` | `rtl` | 10 | 3 | 2 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_arbiter_tree.sv` |
| `prim_fifo_async_simple` | `ibex` | `rtl` | 10 | 3 | 2 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_fifo_async_simple.sv` |
| `prim_intr_hw` | `ibex` | `rtl` | 10 | 3 | 2 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_intr_hw.sv` |
| `prim_packer_fifo` | `ibex` | `rtl` | 10 | 3 | 2 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_packer_fifo.sv` |
| `ibex_dummy_instr` | `ibex` | `rtl` | 10 | 2 | 3 | 0 | `dbs\ibex\rtl\ibex_dummy_instr.sv` |
| `prim_pad_wrapper` | `ibex` | `rtl` | 20 | 4 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim_generic\rtl\prim_pad_wrapper.sv` |
| `prim_arbiter_fixed_tb` | `ibex` | `testbench` | 9 | 3 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_arbiter_fixed_tb.sv` |
| `prim_fifo_async_sram_adapter_tb` | `ibex` | `testbench` | 9 | 3 | 7 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_fifo_async_sram_adapter_tb.sv` |
| `prim_arbiter_fixed` | `ibex` | `rtl` | 9 | 3 | 1 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_arbiter_fixed.sv` |
| `ibex_compressed_decoder` | `ibex` | `rtl` | 9 | 2 | 4 | 13 | `dbs\ibex\rtl\ibex_compressed_decoder.sv` |
| `ram_1p` | `ibex` | `rtl` | 9 | 2 | 2 | 0 | `dbs\ibex\shared\rtl\ram_1p.sv` |
| `simulator_ctrl` | `ibex` | `rtl` | 9 | 2 | 1 | 0 | `dbs\ibex\shared\rtl\sim\simulator_ctrl.sv` |
| `prim_alert_receiver` | `ibex` | `rtl` | 9 | 2 | 2 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_alert_receiver.sv` |
| `prim_sync_reqack` | `ibex` | `rtl` | 9 | 2 | 11 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_sync_reqack.sv` |
| `prim_subreg_ext` | `ibex` | `rtl` | 9 | 1 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_subreg_ext.sv` |
| `prim_usb_diff_rx` | `ibex` | `rtl` | 9 | 1 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim_generic\rtl\prim_usb_diff_rx.sv` |
| `prim_prince` | `ibex` | `rtl` | 8 | 6 | 12 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_prince.sv` |
| `ibex_pmp` | `ibex` | `rtl` | 8 | 5 | 0 | 4 | `dbs\ibex\rtl\ibex_pmp.sv` |
| `prim_xoshiro256pp` | `ibex` | `rtl` | 8 | 3 | 1 | 1 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_xoshiro256pp.sv` |
| `ibex_counter` | `ibex` | `rtl` | 8 | 2 | 3 | 0 | `dbs\ibex\rtl\ibex_counter.sv` |
| `prim_esc_sender` | `ibex` | `rtl` | 8 | 1 | 2 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_esc_sender.sv` |
| `prim_secded_22_16_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_22_16_tb.sv` |
| `prim_secded_28_22_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_28_22_tb.sv` |
| `prim_secded_39_32_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_39_32_tb.sv` |
| `prim_secded_64_57_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_64_57_tb.sv` |
| `prim_secded_72_64_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_72_64_tb.sv` |
| `prim_secded_hamming_22_16_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_hamming_22_16_tb.sv` |
| `prim_secded_hamming_39_32_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_hamming_39_32_tb.sv` |
| `prim_secded_hamming_72_64_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_hamming_72_64_tb.sv` |
| `prim_secded_hamming_76_68_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_hamming_76_68_tb.sv` |
| `prim_secded_inv_22_16_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_22_16_tb.sv` |
| `prim_secded_inv_28_22_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_28_22_tb.sv` |
| `prim_secded_inv_39_32_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_39_32_tb.sv` |
| `prim_secded_inv_64_57_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_64_57_tb.sv` |
| `prim_secded_inv_72_64_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_72_64_tb.sv` |
| `prim_secded_inv_hamming_22_16_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_hamming_22_16_tb.sv` |
| `prim_secded_inv_hamming_39_32_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_hamming_39_32_tb.sv` |
| `prim_secded_inv_hamming_72_64_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_hamming_72_64_tb.sv` |
| `prim_secded_inv_hamming_76_68_tb` | `ibex` | `testbench` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_hamming_76_68_tb.sv` |
| `prim_secded_22_16_assert_fpv` | `ibex` | `other` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_22_16_assert_fpv.sv` |
| `prim_secded_28_22_assert_fpv` | `ibex` | `other` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_28_22_assert_fpv.sv` |
| `prim_secded_39_32_assert_fpv` | `ibex` | `other` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_39_32_assert_fpv.sv` |
| `prim_secded_64_57_assert_fpv` | `ibex` | `other` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_64_57_assert_fpv.sv` |
| `prim_secded_72_64_assert_fpv` | `ibex` | `other` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_72_64_assert_fpv.sv` |
| `prim_secded_hamming_22_16_assert_fpv` | `ibex` | `other` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_hamming_22_16_assert_fpv.sv` |
| `prim_secded_hamming_39_32_assert_fpv` | `ibex` | `other` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_hamming_39_32_assert_fpv.sv` |
| `prim_secded_hamming_72_64_assert_fpv` | `ibex` | `other` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_hamming_72_64_assert_fpv.sv` |
| `prim_secded_hamming_76_68_assert_fpv` | `ibex` | `other` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_hamming_76_68_assert_fpv.sv` |
| `prim_secded_inv_22_16_assert_fpv` | `ibex` | `other` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_inv_22_16_assert_fpv.sv` |
| `prim_secded_inv_28_22_assert_fpv` | `ibex` | `other` | 8 | 0 | 0 | 0 | `dbs\ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_inv_28_22_assert_fpv.sv` |
