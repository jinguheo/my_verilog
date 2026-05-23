# Hard Retrieval Benchmark Catalog

- Total tasks: 175
- Style: blind RTL retrieval
- Gold module names are removed from prompt text.
- Direct lookup tasks are converted into profile-based retrieval tasks.

## Level Counts

| Level | Count |
|---|---:|
| L4 | 105 |
| L5 | 70 |

## Type Counts

| Type | Count |
|---|---:|
| hard_retrieval_blind_code_explanation | 25 |
| hard_retrieval_blind_comparison_similarity | 25 |
| hard_retrieval_blind_documentation_summary | 25 |
| hard_retrieval_blind_function_similarity | 25 |
| hard_retrieval_blind_generation_design | 25 |
| hard_retrieval_blind_search_navigation | 25 |
| hard_retrieval_blind_structure_understanding | 25 |

## Samples

- `hardret_001` L4 gold=`bus`
  - Blind RTL retrieval task. The original module names are intentionally hidden. Identify the best matching RTL module or modules from the knowledge DB using only the profiles below. Do not answer with primitive cells, packages, testbench files, documentation pages, child-only helpers, or a neighbor that merely shares a port name. Return the primary owner module, not one of its children. Profile 1: role=module navigation target; project=ibex; coarse location=D: / ibex; exposed interface clues=clk_i, rst_ni, host_req_i, host_gnt_o, host_addr_i, host_we_i; child/dependency clues=few or no local child instances; semantic labels=clocked, resettable.
- `hardret_002` L4 gold=`clkgen_xil7series`
  - Blind RTL retrieval task. The original module names are intentionally hidden. Identify the best matching RTL module or modules from the knowledge DB using only the profiles below. Do not answer with primitive cells, packages, testbench files, documentation pages, child-only helpers, or a neighbor that merely shares a port name. Return the primary owner module, not one of its children. Profile 1: role=module navigation target; project=ibex; coarse location=D: / ibex / fpga / xilinx; exposed interface clues=IO_CLK, IO_RST_N, clk_sys, rst_sys_n, buffer, clock; child/dependency clues=IBUF, PLLE2_ADV, BUFG; semantic labels=clocked, hierarchical, resettable.
- `hardret_003` L4 gold=`ibex_alu`
  - Blind RTL retrieval task. The original module names are intentionally hidden. Identify the best matching RTL module or modules from the knowledge DB using only the profiles below. Do not answer with primitive cells, packages, testbench files, documentation pages, child-only helpers, or a neighbor that merely shares a port name. Return the primary owner module, not one of its children. Profile 1: role=module navigation target; project=ibex; coarse location=D:; exposed interface clues=ibex_pkg, operand_a_i, operand_b_i, instr_first_cycle_i, multdiv_operand_a_i, multdiv_operand_b_i; child/dependency clues=few or no local child instances; semantic labels=resettable.
- `hardret_004` L4 gold=`ibex_branch_predict`
  - Blind RTL retrieval task. The original module names are intentionally hidden. Identify the best matching RTL module or modules from the knowledge DB using only the profiles below. Do not answer with primitive cells, packages, testbench files, documentation pages, child-only helpers, or a neighbor that merely shares a port name. Return the primary owner module, not one of its children. Profile 1: role=module navigation target; project=ibex; coarse location=D:; exposed interface clues=clk_i, rst_ni, fetch_rdata_i, fetch_pc_i, fetch_valid_i, predict_branch_taken_o; child/dependency clues=few or no local child instances; semantic labels=clocked, resettable.
- `hardret_005` L4 gold=`ibex_compressed_decoder`
  - Blind RTL retrieval task. The original module names are intentionally hidden. Identify the best matching RTL module or modules from the knowledge DB using only the profiles below. Do not answer with primitive cells, packages, testbench files, documentation pages, child-only helpers, or a neighbor that merely shares a port name. Return the primary owner module, not one of its children. Profile 1: role=module navigation target; project=ibex; coarse location=D:; exposed interface clues=clk_i, rst_ni, valid_i, id_in_ready_i, instr_i, instr_o; child/dependency clues=few or no local child instances; semantic labels=spi.
- `hardret_006` L4 gold=`top_darjeeling`
  - Blind RTL retrieval task. The original module names are intentionally hidden. Identify the best matching RTL module or modules from the knowledge DB using only the profiles below. Do not answer with primitive cells, packages, testbench files, documentation pages, child-only helpers, or a neighbor that merely shares a port name. Return the primary owner module, not one of its children. Profile 1: role=top-level integration block; project=opentitan; coarse location=D: / opentitan; exposed interface clues=mio_in_i, mio_out_o, mio_oe_o, dio_in_i, dio_out_o, dio_oe_o; child/dependency clues=uart, gpio, spi_device, i2c, rv_timer, otp_ctrl; semantic labels=i2c, spi, uart.
- `hardret_007` L4 gold=`top_earlgrey`
  - Blind RTL retrieval task. The original module names are intentionally hidden. Identify the best matching RTL module or modules from the knowledge DB using only the profiles below. Do not answer with primitive cells, packages, testbench files, documentation pages, child-only helpers, or a neighbor that merely shares a port name. Return the primary owner module, not one of its children. Profile 1: role=top-level integration block; project=opentitan; coarse location=D: / opentitan; exposed interface clues=mio_in_i, mio_out_o, mio_oe_o, dio_in_i, dio_out_o, dio_oe_o; child/dependency clues=pinmux_jtag_breakout, uart, gpio, spi_device, i2c, pattgen; semantic labels=fifo, i2c, spi, uart.
- `hardret_008` L4 gold=`spi_device`
  - Blind RTL retrieval task. The original module names are intentionally hidden. Identify the best matching RTL module or modules from the knowledge DB using only the profiles below. Do not answer with primitive cells, packages, testbench files, documentation pages, child-only helpers, or a neighbor that merely shares a port name. Return the primary owner module, not one of its children. Profile 1: role=hierarchical RTL block; project=opentitan; coarse location=D: / opentitan; exposed interface clues=clk_i, rst_ni, tlul_pkg, prim_alert_pkg, top_racl_pkg, cio_sck_i; child/dependency clues=prim_buf, prim_edge_detector, prim_intr_hw, prim_pulse_sync, prim_mubi4_sync, prim_clock_buf; semantic labels=fifo, spi, uart.
- `hardret_009` L4 gold=`top_englishbreakfast`
  - Blind RTL retrieval task. The original module names are intentionally hidden. Identify the best matching RTL module or modules from the knowledge DB using only the profiles below. Do not answer with primitive cells, packages, testbench files, documentation pages, child-only helpers, or a neighbor that merely shares a port name. Return the primary owner module, not one of its children. Profile 1: role=top-level integration block; project=opentitan; coarse location=D: / opentitan; exposed interface clues=mio_in_i, mio_out_o, mio_oe_o, dio_in_i, dio_out_o, dio_oe_o; child/dependency clues=pinmux_jtag_breakout, uart, gpio, spi_device, spi_host, rv_timer; semantic labels=apb, fifo, spi, uart.
- `hardret_010` L4 gold=`flash_ctrl`
  - Blind RTL retrieval task. The original module names are intentionally hidden. Identify the best matching RTL module or modules from the knowledge DB using only the profiles below. Do not answer with primitive cells, packages, testbench files, documentation pages, child-only helpers, or a neighbor that merely shares a port name. Return the primary owner module, not one of its children. Profile 1: role=top-level integration block; project=opentitan; coarse location=D: / opentitan / top_englishbreakfast / ip_autogen; exposed interface clues=clk_i, rst_ni, rst_shadowed_ni, clk_otp_i, rst_otp_ni, lc_ctrl_pkg; child/dependency clues=[hidden-target]_core_reg_top, [hidden-target]_region_cfg, prim_lc_sync, prim_lfsr, [hidden-target]_arb, [hidden-target]_lcmgr; semantic labels=fifo, uart.
- `hardret_011` L4 gold=`flash_ctrl`
  - Blind RTL retrieval task. The original module names are intentionally hidden. Identify the best matching RTL module or modules from the knowledge DB using only the profiles below. Do not answer with primitive cells, packages, testbench files, documentation pages, child-only helpers, or a neighbor that merely shares a port name. Return the primary owner module, not one of its children. Profile 1: role=top-level integration block; project=opentitan; coarse location=D: / opentitan / top_earlgrey / ip_autogen; exposed interface clues=clk_i, rst_ni, rst_shadowed_ni, clk_otp_i, rst_otp_ni, lc_ctrl_pkg; child/dependency clues=[hidden-target]_core_reg_top, [hidden-target]_region_cfg, prim_lc_sync, prim_lfsr, [hidden-target]_arb, [hidden-target]_lcmgr; semantic labels=fifo, uart.
- `hardret_012` L4 gold=`entropy_src_core`
  - Blind RTL retrieval task. The original module names are intentionally hidden. Identify the best matching RTL module or modules from the knowledge DB using only the profiles below. Do not answer with primitive cells, packages, testbench files, documentation pages, child-only helpers, or a neighbor that merely shares a port name. Return the primary owner module, not one of its children. Profile 1: role=hierarchical RTL block; project=opentitan; coarse location=D: / opentitan; exposed interface clues=clk_i, rst_ni, entropy_src_reg_pkg, prim_mubi_pkg, rng_fips_o, entropy_src_hw_if_req_t; child/dependency clues=prim_mubi4_sync, entropy_src_enable_delay, prim_mubi8_sync, prim_intr_hw, prim_fifo_sync, entropy_src_watermark_reg; semantic labels=fifo.
