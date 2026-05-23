# Code Graph Relation Samples

## calls

| Source | Target | Evidence file | Location |
| --- | --- | --- | --- |
| riscv_cosim_step() | assert() | ibex\dv\cosim\cosim_dpi.cc | L16 |
| riscv_cosim_step() | .step() | ibex\dv\cosim\cosim_dpi.cc | L18 |
| riscv_cosim_set_mip() | assert() | ibex\dv\cosim\cosim_dpi.cc | L26 |
| riscv_cosim_set_mip() | set_mip() | ibex\dv\cosim\cosim_dpi.cc | L28 |
| riscv_cosim_set_nmi() | assert() | ibex\dv\cosim\cosim_dpi.cc | L32 |
| riscv_cosim_set_nmi() | set_nmi() | ibex\dv\cosim\cosim_dpi.cc | L34 |
| riscv_cosim_set_nmi_int() | assert() | ibex\dv\cosim\cosim_dpi.cc | L38 |
| riscv_cosim_set_nmi_int() | set_nmi_int() | ibex\dv\cosim\cosim_dpi.cc | L40 |
| riscv_cosim_set_debug_req() | assert() | ibex\dv\cosim\cosim_dpi.cc | L43 |
| riscv_cosim_set_debug_req() | set_debug_req() | ibex\dv\cosim\cosim_dpi.cc | L45 |
| riscv_cosim_set_mcycle() | assert() | ibex\dv\cosim\cosim_dpi.cc | L49 |
| riscv_cosim_set_mcycle() | set_mcycle() | ibex\dv\cosim\cosim_dpi.cc | L52 |
| riscv_cosim_set_csr() | assert() | ibex\dv\cosim\cosim_dpi.cc | L57 |
| riscv_cosim_set_csr() | set_csr() | ibex\dv\cosim\cosim_dpi.cc | L59 |
| riscv_cosim_set_ic_scr_key_valid() | assert() | ibex\dv\cosim\cosim_dpi.cc | L63 |
| riscv_cosim_set_ic_scr_key_valid() | set_ic_scr_key_valid() | ibex\dv\cosim\cosim_dpi.cc | L65 |
| riscv_cosim_notify_dside_access() | assert() | ibex\dv\cosim\cosim_dpi.cc | L75 |
| riscv_cosim_notify_dside_access() | notify_dside_access() | ibex\dv\cosim\cosim_dpi.cc | L77 |
| riscv_cosim_set_iside_error() | assert() | ibex\dv\cosim\cosim_dpi.cc | L90 |
| riscv_cosim_set_iside_error() | set_iside_error() | ibex\dv\cosim\cosim_dpi.cc | L92 |
| riscv_cosim_get_num_errors() | assert() | ibex\dv\cosim\cosim_dpi.cc | L96 |
| riscv_cosim_get_num_errors() | Size | ibex\dv\cosim\cosim_dpi.cc | L98 |
| riscv_cosim_get_error() | assert() | ibex\dv\cosim\cosim_dpi.cc | L102 |
| riscv_cosim_get_error() | Size | ibex\dv\cosim\cosim_dpi.cc | L104 |
| riscv_cosim_clear_errors() | assert() | ibex\dv\cosim\cosim_dpi.cc | L112 |
| riscv_cosim_clear_errors() | clear_errors() | ibex\dv\cosim\cosim_dpi.cc | L114 |
| riscv_cosim_write_mem_byte() | assert() | ibex\dv\cosim\cosim_dpi.cc | L119 |
| riscv_cosim_write_mem_byte() | backdoor_write_mem() | ibex\dv\cosim\cosim_dpi.cc | L121 |
| riscv_cosim_get_insn_cnt() | assert() | ibex\dv\cosim\cosim_dpi.cc | L125 |
| riscv_cosim_get_insn_cnt() | get_insn_cnt() | ibex\dv\cosim\cosim_dpi.cc | L127 |
| SpikeCosim() | initial_proc_setup() | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc | L73 |
| SpikeCosim() | get() | ibex\dv\cosim\spike_cosim.cc | L46 |
| SpikeCosim() | .set_debug() | ibex\dv\cosim\spike_cosim.cc | L76 |
| mmio_load() | check_mem_access() | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc | L106 |
| mmio_load() | .load() | ibex\dv\cosim\spike_cosim.cc | L85 |
| mmio_load() | .get_state() | ibex\dv\cosim\spike_cosim.cc | L92 |
| mmio_store() | check_mem_access() | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc | L117 |
| add_memory() | get() | ibex\dv\cosim\spike_cosim.cc | L128 |
| add_memory() | spike_cosim_init() | ibex\dv\uvm\core_ibex\common\ibex_cosim_agent\spike_cosim_dpi.cc | L34 |
| backdoor_read_mem() | pc_is_mret() | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc | L1042 |
| backdoor_read_mem() | pc_is_debug_ebreak() | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc | L1062 |
| backdoor_read_mem() | pc_is_load() | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc | L1109 |
| backdoor_read_mem() | .load() | ibex\dv\cosim\spike_cosim.cc | L139 |
| step() | pc_is_debug_ebreak() | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc | L186 |
| step() | check_debug_ebreak() | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc | L187 |
| step() | check_suppress_reg_write() | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc | L202 |
| step() | check_sync_trap() | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc | L273 |
| step() | handle_cpuctrl_exception_entry() | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc | L277 |
| step() | pc_is_mret() | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc | L288 |
| step() | change_cpuctrlsts_sync_exc_seen() | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc | L289 |

## contains

| Source | Target | Evidence file | Location |
| --- | --- | --- | --- |
| cosim.h | Cosim() | ibex\dv\cosim\cosim.h | L44 |
| Cosim() | cosim.h | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim.h | L44 |
| cosim_dpi.cc | riscv_cosim_step() | ibex\dv\cosim\cosim_dpi.cc | L13 |
| cosim_dpi.cc | riscv_cosim_set_mip() | ibex\dv\cosim\cosim_dpi.cc | L24 |
| cosim_dpi.cc | riscv_cosim_set_nmi() | ibex\dv\cosim\cosim_dpi.cc | L31 |
| cosim_dpi.cc | riscv_cosim_set_nmi_int() | ibex\dv\cosim\cosim_dpi.cc | L37 |
| cosim_dpi.cc | riscv_cosim_set_debug_req() | ibex\dv\cosim\cosim_dpi.cc | L42 |
| cosim_dpi.cc | riscv_cosim_set_mcycle() | ibex\dv\cosim\cosim_dpi.cc | L48 |
| cosim_dpi.cc | riscv_cosim_set_csr() | ibex\dv\cosim\cosim_dpi.cc | L55 |
| cosim_dpi.cc | riscv_cosim_set_ic_scr_key_valid() | ibex\dv\cosim\cosim_dpi.cc | L62 |
| cosim_dpi.cc | riscv_cosim_notify_dside_access() | ibex\dv\cosim\cosim_dpi.cc | L68 |
| cosim_dpi.cc | riscv_cosim_set_iside_error() | ibex\dv\cosim\cosim_dpi.cc | L89 |
| cosim_dpi.cc | riscv_cosim_get_num_errors() | ibex\dv\cosim\cosim_dpi.cc | L95 |
| cosim_dpi.cc | riscv_cosim_get_error() | ibex\dv\cosim\cosim_dpi.cc | L101 |
| cosim_dpi.cc | riscv_cosim_clear_errors() | ibex\dv\cosim\cosim_dpi.cc | L111 |
| cosim_dpi.cc | riscv_cosim_write_mem_byte() | ibex\dv\cosim\cosim_dpi.cc | L117 |
| cosim_dpi.cc | riscv_cosim_get_insn_cnt() | ibex\dv\cosim\cosim_dpi.cc | L124 |
| riscv_cosim_step() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L13 |
| riscv_cosim_set_mip() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L24 |
| riscv_cosim_set_nmi() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L31 |
| riscv_cosim_set_nmi_int() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L37 |
| riscv_cosim_set_debug_req() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L42 |
| riscv_cosim_set_mcycle() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L48 |
| riscv_cosim_set_csr() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L55 |
| riscv_cosim_set_ic_scr_key_valid() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L62 |
| riscv_cosim_notify_dside_access() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L68 |
| riscv_cosim_set_iside_error() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L89 |
| riscv_cosim_get_num_errors() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L95 |
| riscv_cosim_get_error() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L101 |
| riscv_cosim_clear_errors() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L111 |
| riscv_cosim_write_mem_byte() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L117 |
| riscv_cosim_get_insn_cnt() | cosim_dpi.cc | opentitan\hw\vendor\lowrisc_ibex\dv\cosim\cosim_dpi.cc | L124 |
| spike_cosim.cc | SpikeCosim() | ibex\dv\cosim\spike_cosim.cc | L36 |
| spike_cosim.cc | addr_to_mem() | ibex\dv\cosim\spike_cosim.cc | L82 |
| spike_cosim.cc | mmio_load() | ibex\dv\cosim\spike_cosim.cc | L84 |
| spike_cosim.cc | mmio_store() | ibex\dv\cosim\spike_cosim.cc | L113 |
| spike_cosim.cc | proc_reset() | ibex\dv\cosim\spike_cosim.cc | L122 |
| spike_cosim.cc | get_symbol() | ibex\dv\cosim\spike_cosim.cc | L124 |
| spike_cosim.cc | add_memory() | ibex\dv\cosim\spike_cosim.cc | L126 |
| spike_cosim.cc | backdoor_write_mem() | ibex\dv\cosim\spike_cosim.cc | L132 |
| spike_cosim.cc | backdoor_read_mem() | ibex\dv\cosim\spike_cosim.cc | L137 |
| spike_cosim.cc | step() | ibex\dv\cosim\spike_cosim.cc | L172 |
| spike_cosim.cc | check_retired_instr() | ibex\dv\cosim\spike_cosim.cc | L321 |
| spike_cosim.cc | check_sync_trap() | ibex\dv\cosim\spike_cosim.cc | L389 |
| spike_cosim.cc | check_gpr_write() | ibex\dv\cosim\spike_cosim.cc | L435 |
| spike_cosim.cc | check_suppress_reg_write() | ibex\dv\cosim\spike_cosim.cc | L475 |
| spike_cosim.cc | on_csr_write() | ibex\dv\cosim\spike_cosim.cc | L500 |
| spike_cosim.cc | leave_nmi_mode() | ibex\dv\cosim\spike_cosim.cc | L513 |
| spike_cosim.cc | handle_cpuctrl_exception_entry() | ibex\dv\cosim\spike_cosim.cc | L533 |
| spike_cosim.cc | change_cpuctrlsts_sync_exc_seen() | ibex\dv\cosim\spike_cosim.cc | L542 |

## defines

| Source | Target | Evidence file | Location |
| --- | --- | --- | --- |
| tb_cs_registers.sv | tb_cs_registers | ibex\dv\cs_registers\tb\tb_cs_registers.sv | L5 |
| top.sv | top | ibex\dv\formal\check\top.sv | L37 |
| alt_lsu.sv | alt_lsu | ibex\dv\formal\check\peek\alt_lsu.sv | L17 |
| spec_api.sv | spec_api | ibex\dv\formal\spec\spec_api.sv | L20 |
| ibex_riscv_compliance.sv | ibex_riscv_compliance | ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv | L13 |
| riscv_testutil.sv | riscv_testutil | ibex\dv\riscv_compliance\rtl\riscv_testutil.sv | L23 |
| core_ibex_fcov_bind.sv | core_ibex_fcov_bind | ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_bind.sv | L5 |
| core_ibex_tb_top.sv | core_ibex_tb_top | ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv | L9 |
| ibex_icache_fcov_bind.sv | ibex_icache_fcov_bind | ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_bind.sv | L7 |
| tb.sv | tb | ibex\dv\uvm\icache\dv\tb\tb.sv | L6 |
| ibex_simple_system_cosim_checker.sv | ibex_simple_system_cosim_checker | ibex\dv\verilator\simple_system_cosim\ibex_simple_system_cosim_checker.sv | L5 |
| ibex_simple_system_cosim_checker_bind.sv | ibex_simple_system_cosim_checker_bind | ibex\dv\verilator\simple_system_cosim\ibex_simple_system_cosim_checker_bind.sv | L5 |
| ibex_simple_system.sv | ibex_simple_system | ibex\examples\simple_system\rtl\ibex_simple_system.sv | L41 |
| formal_tb.sv | formal_tb | ibex\formal\data_ind_timing\formal_tb.sv | L9 |
| formal_tb.sv | formal_tb | ibex\formal\icache\formal_tb.sv | L18 |
| ibex_alu.sv | ibex_alu | ibex\rtl\ibex_alu.sv | L9 |
| ibex_branch_predict.sv | ibex_branch_predict | ibex\rtl\ibex_branch_predict.sv | L20 |
| ibex_compressed_decoder.sv | ibex_compressed_decoder | ibex\rtl\ibex_compressed_decoder.sv | L16 |
| ibex_controller.sv | ibex_controller | ibex\rtl\ibex_controller.sv | L13 |
| ibex_core.sv | ibex_core | ibex\rtl\ibex_core.sv | L16 |
| ibex_counter.sv | ibex_counter | ibex\rtl\ibex_counter.sv | L5 |
| ibex_csr.sv | ibex_csr | ibex\rtl\ibex_csr.sv | L11 |
| ibex_cs_registers.sv | ibex_cs_registers | ibex\rtl\ibex_cs_registers.sv | L12 |
| ibex_decoder.sv | ibex_decoder | ibex\rtl\ibex_decoder.sv | L16 |
| ibex_dummy_instr.sv | ibex_dummy_instr | ibex\rtl\ibex_dummy_instr.sv | L12 |
| ibex_ex_block.sv | ibex_ex_block | ibex\rtl\ibex_ex_block.sv | L11 |
| ibex_fetch_fifo.sv | ibex_fetch_fifo | ibex\rtl\ibex_fetch_fifo.sv | L15 |
| ibex_icache.sv | ibex_icache | ibex\rtl\ibex_icache.sv | L13 |
| ibex_id_stage.sv | ibex_id_stage | ibex\rtl\ibex_id_stage.sv | L20 |
| ibex_if_stage.sv | ibex_if_stage | ibex\rtl\ibex_if_stage.sv | L16 |
| ibex_load_store_unit.sv | ibex_load_store_unit | ibex\rtl\ibex_load_store_unit.sv | L17 |
| ibex_lockstep.sv | ibex_lockstep | ibex\rtl\ibex_lockstep.sv | L11 |
| ibex_multdiv_fast.sv | ibex_multdiv_fast | ibex\rtl\ibex_multdiv_fast.sv | L17 |
| ibex_multdiv_slow.sv | ibex_multdiv_slow | ibex\rtl\ibex_multdiv_slow.sv | L14 |
| ibex_pmp.sv | ibex_pmp | ibex\rtl\ibex_pmp.sv | L7 |
| ibex_prefetch_buffer.sv | ibex_prefetch_buffer | ibex\rtl\ibex_prefetch_buffer.sv | L12 |
| ibex_register_file_ff.sv | ibex_register_file_ff | ibex\rtl\ibex_register_file_ff.sv | L7 |
| ibex_register_file_fpga.sv | ibex_register_file_fpga | ibex\rtl\ibex_register_file_fpga.sv | L14 |
| ibex_register_file_latch.sv | ibex_register_file_latch | ibex\rtl\ibex_register_file_latch.sv | L14 |
| ibex_top.sv | ibex_top | ibex\rtl\ibex_top.sv | L15 |
| ibex_top_tracing.sv | ibex_top_tracing | ibex\rtl\ibex_top_tracing.sv | L9 |
| ibex_tracer.sv | ibex_tracer | ibex\rtl\ibex_tracer.sv | L37 |
| ibex_wb_stage.sv | ibex_wb_stage | ibex\rtl\ibex_wb_stage.sv | L17 |
| bus.sv | bus | ibex\shared\rtl\bus.sv | L17 |
| ram_1p.sv | ram_1p | ibex\shared\rtl\ram_1p.sv | L11 |
| ram_2p.sv | ram_2p | ibex\shared\rtl\ram_2p.sv | L15 |
| timer.sv | timer | ibex\shared\rtl\timer.sv | L9 |
| clkgen_xil7series.sv | clkgen_xil7series | ibex\shared\rtl\fpga\xilinx\clkgen_xil7series.sv | L5 |
| simulator_ctrl.sv | simulator_ctrl | ibex\shared\rtl\sim\simulator_ctrl.sv | L22 |
| prim_clock_gating.v | prim_clock_gating | ibex\syn\rtl\prim_clock_gating.v | L7 |

## imports

| Source | Target | Evidence file | Location |
| --- | --- | --- | --- |
| Exception | tb_top_verilator.cpp | opentitan\hw\vendor\pulp_riscv_dbg\tb\tb_top_verilator.cpp | L28 |
| metadata.py | Signal | ibex\dv\uvm\core_ibex\scripts\metadata.py | L22 |
| Enum | utils.py | ibex\vendor\google_riscv-dv\pygen\experimental\utils.py | L19 |
| Enum | utils.py | opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\experimental\utils.py | L19 |
| Enum | gen-rng-health-thresholds.py | opentitan\util\design\gen-rng-health-thresholds.py | L45 |
| Enum | bitstream_bisect.py | opentitan\util\fpga\bitstream_bisect.py | L30 |
| lib.py | Signal | ibex\vendor\google_riscv-dv\scripts\lib.py | L27 |
| verilator_sim_ctrl.cc | Signal | ibex\vendor\lowrisc_ip\dv\verilator\simutil_verilator\cpp\verilator_sim_ctrl.cc | L9 |
| ascon_model_dpi.h | ascon | ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.h | L9 |
| aead.c | ascon | ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\aead.c | L2 |
| permutations.h | ascon | ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\permutations.h | L6 |
| printstate.h | ascon | ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\printstate.h | L6 |
| round.h | ascon | ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\round.h | L4 |
| aead.c | ascon | ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\aead.c | L2 |
| permutations.h | ascon | ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\permutations.h | L6 |
| printstate.h | ascon | ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\printstate.h | L6 |
| round.h | ascon | ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\round.h | L4 |
| prim_ascon_duplex_tb.cc | Signal | ibex\vendor\lowrisc_ip\ip\prim\pre_dv\prim_ascon\prim_ascon_duplex_tb\cpp\prim_ascon_duplex_tb.cc | L7 |
| prim_ascon_round_tb.cc | Signal | ibex\vendor\lowrisc_ip\ip\prim\pre_dv\prim_ascon\prim_ascon_round_tb\cpp\prim_ascon_round_tb.cc | L7 |
| prim_sync_reqack_tb.cc | Signal | ibex\vendor\lowrisc_ip\ip\prim\pre_dv\prim_sync_reqack\cpp\prim_sync_reqack_tb.cc | L7 |
| prim_trivium_tb.cc | Signal | ibex\vendor\lowrisc_ip\ip\prim\pre_dv\prim_trivium\cpp\prim_trivium_tb.cc | L7 |
| LintCfg | CfgFactory.py | ibex\vendor\lowrisc_ip\util\dvsim\CfgFactory.py | L14 |
| LintCfg | CfgFactory.py | opentitan\util\dvsim\CfgFactory.py | L14 |
| dvsim.py | Launcher | ibex\vendor\lowrisc_ip\util\dvsim\dvsim.py | L33 |
| Launcher | dvsim.py | opentitan\util\dvsim\dvsim.py | L33 |
| syscalls.c | Signal | ibex\vendor\riscv-isa-sim\tests\mseccfg\syscalls.c | L8 |
| syscalls.c | Signal | ibex\vendor\riscv-tests\benchmarks\common\syscalls.c | L8 |
| gpiodpi.c | gpiodpi | opentitan\hw\dv\dpi\gpiodpi\gpiodpi.c | L5 |
| monitor_spi.c | spidpi | opentitan\hw\dv\dpi\spidpi\monitor_spi.c | L10 |
| spidpi.c | spidpi | opentitan\hw\dv\dpi\spidpi\spidpi.c | L24 |
| uartdpi.c | uartdpi | opentitan\hw\dv\dpi\uartdpi\uartdpi.c | L10 |
| usbdpi.c | usbdpi | opentitan\hw\dv\dpi\usbdpi\usbdpi.c | L5 |
| usbdpi_stream.c | usbdpi | opentitan\hw\dv\dpi\usbdpi\usbdpi_stream.c | L10 |
| usbdpi_test.c | usbdpi | opentitan\hw\dv\dpi\usbdpi\usbdpi_test.c | L9 |
| usb_crc.c | usbdpi | opentitan\hw\dv\dpi\usbdpi\usb_crc.c | L25 |
| usb_monitor.c | usbdpi | opentitan\hw\dv\dpi\usbdpi\usb_monitor.c | L12 |
| usb_transfer.c | usbdpi | opentitan\hw\dv\dpi\usbdpi\usb_transfer.c | L9 |
| verilator_sim_ctrl.cc | Signal | opentitan\hw\dv\verilator\simutil_verilator\cpp\verilator_sim_ctrl.cc | L9 |
| adc_ctrl | flash_ctrl_idle_low_power_test.c | opentitan\sw\device\tests\flash_ctrl_idle_low_power_test.c | L5 |
| adc_ctrl | pwrmgr_sleep_all_wake_ups_impl.c | opentitan\sw\device\tests\pwrmgr_sleep_all_wake_ups_impl.c | L21 |
| adc_ctrl | rv_dm_ndm_reset_req.c | opentitan\sw\device\tests\rv_dm_ndm_reset_req.c | L17 |
| adc_ctrl | all_escalation_resets_test.c | opentitan\sw\device\tests\sim_dv\all_escalation_resets_test.c | L31 |
| adc_ctrl | pwrmgr_random_sleep_power_glitch_reset_test.c | opentitan\sw\device\tests\sim_dv\pwrmgr_random_sleep_power_glitch_reset_test.c | L10 |
| aes_model_dpi.c | aes | opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c | L12 |
| aes | aes.c | opentitan\hw\ip\aes\model\aes.c | L5 |
| aes | aes_example.c | opentitan\hw\ip\aes\model\aes_example.c | L12 |
| aes | aes_modes.c | opentitan\hw\ip\aes\model\aes_modes.c | L12 |
| aes | aes.c | opentitan\sw\device\lib\crypto\drivers\aes.c | L7 |
| aes | aes_test.c | opentitan\sw\device\lib\crypto\drivers\aes_test.c | L5 |
| aes | aes.c | opentitan\sw\device\lib\crypto\impl\aes.c | L11 |

## imports_from

| Source | Target | Evidence file | Location |
| --- | --- | --- | --- |
| top | ibex_pkg | ibex\dv\formal\check\top.sv | L37 |
| ibex_pkg | core_ibex_fcov_if.sv | ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_if.sv | L8 |
| ibex_pkg | core_ibex_pmp_fcov_if.sv | ibex\dv\uvm\core_ibex\fcov\core_ibex_pmp_fcov_if.sv | L7 |
| ibex_pkg | core_ibex_test_pkg.sv | ibex\dv\uvm\core_ibex\tests\core_ibex_test_pkg.sv | L16 |
| ibex_pkg | ibex_icache_fcov_if.sv | ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_if.sv | L5 |
| ibex_pkg | tb.sv | ibex\dv\uvm\icache\dv\tb\tb.sv | L5 |
| ibex_pkg | ibex_simple_system_cosim_checker | ibex\dv\verilator\simple_system_cosim\ibex_simple_system_cosim_checker.sv | L34 |
| ibex_pkg | formal_tb | ibex\formal\data_ind_timing\formal_tb.sv | L40 |
| ibex_pkg | formal_tb | ibex\formal\icache\formal_tb.sv | L19 |
| ibex_pkg | ibex_alu | ibex\rtl\ibex_alu.sv | L34 |
| ibex_pkg | ibex_branch_predict | ibex\rtl\ibex_branch_predict.sv | L33 |
| ibex_pkg | ibex_compressed_decoder | ibex\rtl\ibex_compressed_decoder.sv | L30 |
| ibex_pkg | ibex_controller | ibex\rtl\ibex_controller.sv | L114 |
| ibex_pkg | ibex_core | ibex\rtl\ibex_core.sv | L16 |
| ibex_pkg | ibex_cs_registers | ibex\rtl\ibex_cs_registers.sv | L12 |
| ibex_pkg | ibex_decoder | ibex\rtl\ibex_decoder.sv | L101 |
| ibex_pkg | ibex_dummy_instr | ibex\rtl\ibex_dummy_instr.sv | L12 |
| ibex_pkg | ibex_ex_block | ibex\rtl\ibex_ex_block.sv | L56 |
| ibex_pkg | ibex_icache | ibex\rtl\ibex_icache.sv | L13 |
| ibex_pkg | ibex_id_stage | ibex\rtl\ibex_id_stage.sv | L195 |
| ibex_pkg | ibex_if_stage | ibex\rtl\ibex_if_stage.sv | L16 |
| ibex_pkg | ibex_lockstep | ibex\rtl\ibex_lockstep.sv | L11 |
| ibex_pkg | ibex_multdiv_fast | ibex\rtl\ibex_multdiv_fast.sv | L48 |
| ibex_pkg | ibex_multdiv_slow | ibex\rtl\ibex_multdiv_slow.sv | L45 |
| ibex_pkg | ibex_pmp | ibex\rtl\ibex_pmp.sv | L7 |
| ibex_pkg | ibex_top | ibex\rtl\ibex_top.sv | L15 |
| ibex_pkg | ibex_top_tracing | ibex\rtl\ibex_top_tracing.sv | L9 |
| ibex_pkg | ibex_tracer_pkg.sv | ibex\rtl\ibex_tracer_pkg.sv | L7 |
| ibex_pkg | ibex_wb_stage | ibex\rtl\ibex_wb_stage.sv | L64 |
| ibex_pkg | ibex_pmp_reset_pkg.sv | opentitan\hw\top_darjeeling\rtl\ibex_pmp_reset_pkg.sv | L6 |
| ibex_pkg | ibex_pmp_reset_pkg.sv | opentitan\hw\top_earlgrey\rtl\ibex_pmp_reset_pkg.sv | L6 |
| ibex_pkg | top | opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv | L37 |
| ibex_pkg | core_ibex_fcov_if.sv | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\fcov\core_ibex_fcov_if.sv | L8 |
| ibex_pkg | core_ibex_pmp_fcov_if.sv | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\fcov\core_ibex_pmp_fcov_if.sv | L7 |
| ibex_pkg | core_ibex_test_pkg.sv | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tests\core_ibex_test_pkg.sv | L16 |
| ibex_pkg | ibex_icache_fcov_if.sv | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\fcov\ibex_icache_fcov_if.sv | L5 |
| ibex_pkg | tb.sv | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\tb\tb.sv | L5 |
| ibex_pkg | ibex_simple_system_cosim_checker | opentitan\hw\vendor\lowrisc_ibex\dv\verilator\simple_system_cosim\ibex_simple_system_cosim_checker.sv | L34 |
| ibex_pkg | ibex_alu | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_alu.sv | L34 |
| ibex_pkg | ibex_branch_predict | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_branch_predict.sv | L33 |
| ibex_pkg | ibex_compressed_decoder | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_compressed_decoder.sv | L30 |
| ibex_pkg | ibex_controller | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_controller.sv | L114 |
| ibex_pkg | ibex_core | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv | L16 |
| ibex_pkg | ibex_cs_registers | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_cs_registers.sv | L12 |
| ibex_pkg | ibex_decoder | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_decoder.sv | L101 |
| ibex_pkg | ibex_dummy_instr | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_dummy_instr.sv | L12 |
| ibex_pkg | ibex_ex_block | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_ex_block.sv | L56 |
| ibex_pkg | ibex_icache | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_icache.sv | L13 |
| ibex_pkg | ibex_id_stage | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_id_stage.sv | L195 |
| ibex_pkg | ibex_if_stage | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv | L16 |

## inherits

| Source | Target | Evidence file | Location |
| --- | --- | --- | --- |
| DConfig | DTest | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\directed_test_schema.py | L71 |
| GenError | Exception | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\ibex_cmd.py | L29 |
| Exception | ReqErr | opentitan\hw\vendor\lowrisc_ibex\util\check_tool_requirements.py | L35 |
| Exception | ConfigException | opentitan\hw\vendor\lowrisc_ibex\util\ibex_config.py | L17 |
| Exception | LauncherError | opentitan\util\dvsim\Launcher.py | L17 |
| Exception | LauncherBusy | opentitan\util\dvsim\Launcher.py | L22 |
| Exception | NoGCPError | opentitan\util\dvsim\results_server.py | L18 |
| Exception | CompileError | ibex\vendor\riscv-tests\debug\testlib.py | L32 |
| Exception | CannotAccess | ibex\vendor\riscv-tests\debug\testlib.py | L463 |
| Exception | CannotInsertBreakpoint | ibex\vendor\riscv-tests\debug\testlib.py | L468 |
| Exception | CouldNotFetch | ibex\vendor\riscv-tests\debug\testlib.py | L473 |
| Exception | CouldNotReadRegisters | ibex\vendor\riscv-tests\debug\testlib.py | L479 |
| Exception | NoSymbol | ibex\vendor\riscv-tests\debug\testlib.py | L484 |
| Exception | UnknownThread | ibex\vendor\riscv-tests\debug\testlib.py | L492 |
| Exception | TestFailed | ibex\vendor\riscv-tests\debug\testlib.py | L1326 |
| Exception | TestNotApplicable | ibex\vendor\riscv-tests\debug\testlib.py | L1333 |
| Exception | JsonError | opentitan\util\vendor.py | L188 |
| Exception | ParserBug | opentitan\util\fpga\bitstream_bisect.py | L71 |
| Exception | TemplateParseError | opentitan\util\ipgen\lib.py | L14 |
| Exception | TemplateRenderError | opentitan\util\ipgen\lib.py | L18 |
| Exception | EmptyMultiRegException | opentitan\util\reggen\multi_register.py | L50 |
| Ops | Enum | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L336 |
| Enum | TestType | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\test_run_result.py | L19 |
| Enum | Failure_Modes | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\test_run_result.py | L26 |
| Enum | pmp_addr_mode_t | opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_pkg.py | L1189 |
| Enum | vtype_t | opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_pkg.py | L1196 |
| Enum | vxrm_t | opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_pkg.py | L1204 |
| Enum | b_ext_group_t | opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_pkg.py | L1211 |
| Enum | all_gpr | opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_pkg.py | L1224 |
| Enum | SwType | opentitan\ci\scripts\check_dv_sw_images.py | L25 |
| Enum | KmacMode | opentitan\hw\ip\otbn\dv\otbnsim\sim\kmac.py | L30 |
| Enum | KmacStrength | opentitan\hw\ip\otbn\dv\otbnsim\sim\kmac.py | L44 |
| Enum | KmacCmd | opentitan\hw\ip\otbn\dv\otbnsim\sim\kmac.py | L75 |
| Enum | KmacState | opentitan\hw\ip\otbn\dv\otbnsim\sim\kmac.py | L90 |
| Enum | StopPoint | opentitan\hw\ip\otbn\util\shared\instruction_count_range.py | L16 |
| Enum | ScramblingMode | opentitan\hw\ip\rom_ctrl\util\scramble_image.py | L21 |
| Enum | FlashScramblingKeyType | opentitan\util\design\gen-flash-img.py | L58 |
| Enum | DtIpPos | opentitan\util\dtgen\helper.py | L327 |
| Enum | LogLevel | opentitan\util\py\packages\lib\ot_logging.py | L15 |
| Enum | sw_type_e | opentitan\util\py\scripts\build_sw_collateral_for_sim.py | L140 |
| Enum | OutputFormat | opentitan\util\py\scripts\committer_stats.py | L56 |
| Enum | JsonEnum | opentitan\util\reggen\access.py | L13 |
| Enum | ImType | opentitan\util\topgen\intermodule.py | L27 |
| Enum | ImAct | opentitan\util\topgen\intermodule.py | L32 |
| Enum | ImConn | opentitan\util\topgen\intermodule.py | L38 |
| Enum | PadType | opentitan\util\topgen\validate.py | L460 |
| Enum | TargetType | opentitan\util\topgen\validate.py | L478 |
| ToolReq | VerilatorToolReq | opentitan\hw\vendor\lowrisc_ibex\util\check_tool_requirements.py | L201 |
| ToolReq | VeribleToolReq | opentitan\hw\vendor\lowrisc_ibex\util\check_tool_requirements.py | L217 |
| ToolReq | VivadoToolReq | opentitan\hw\vendor\lowrisc_ibex\util\check_tool_requirements.py | L232 |

## instantiates

| Source | Target | Evidence file | Location |
| --- | --- | --- | --- |
| tb_cs_registers | ibex_cs_registers | ibex\dv\cs_registers\tb\tb_cs_registers.sv | L65 |
| ibex_cs_registers | ibex_core | ibex\rtl\ibex_core.sv | L1055 |
| ibex_cs_registers | tb_cs_registers | opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\tb\tb_cs_registers.sv | L65 |
| ibex_cs_registers | ibex_core | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv | L1055 |
| top | ibex_top | ibex\dv\formal\check\top.sv | L144 |
| top | ibex_compressed_decoder | ibex\dv\formal\check\top.sv | L478 |
| top | mem_assume_t | ibex\dv\formal\check\top.sv | L504 |
| ibex_top | ibex_top_tracing | ibex\rtl\ibex_top_tracing.sv | L197 |
| ibex_top | top | opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv | L144 |
| ibex_top | ibex_top_tracing | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv | L197 |
| ibex_compressed_decoder | ibex_if_stage | ibex\rtl\ibex_if_stage.sv | L414 |
| ibex_compressed_decoder | top | opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv | L478 |
| ibex_compressed_decoder | ibex_if_stage | opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv | L414 |
| mem_assume_t | top | opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv | L504 |
| spec_api | sail_ibexspec | ibex\dv\formal\spec\spec_api.sv | L166 |
| sail_ibexspec | spec_api | opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv | L166 |
| ibex_riscv_compliance | bus | ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv | L93 |
| ibex_riscv_compliance | ibex_top_tracing | ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv | L143 |
| ibex_riscv_compliance | ram_1p | ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv | L238 |
| ibex_riscv_compliance | riscv_testutil | ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv | L254 |
| bus | ibex_simple_system | ibex\examples\simple_system\rtl\ibex_simple_system.sv | L150 |
| bus | ibex_riscv_compliance | opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv | L93 |
| ibex_top_tracing | core_ibex_tb_top | ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv | L97 |
| ibex_top_tracing | ibex_simple_system | ibex\examples\simple_system\rtl\ibex_simple_system.sv | L200 |
| ibex_top_tracing | ibex_riscv_compliance | opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv | L143 |
| ibex_top_tracing | core_ibex_tb_top | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv | L97 |
| ram_1p | otbn_top_coco | opentitan\hw\ip\otbn\pre_sca\alma\rtl\otbn_top_coco.v | L231 |
| ram_1p | ibex_riscv_compliance | opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv | L238 |
| riscv_testutil | ibex_riscv_compliance | opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv | L254 |
| core_ibex_tb_top | clk_rst_if | ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv | L17 |
| core_ibex_tb_top | push_pull_if | ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv | L87 |
| clk_rst_if | tb | ibex\dv\uvm\icache\dv\tb\tb.sv | L23 |
| clk_rst_if | prim_prince_tb | ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\tb\prim_prince_tb.sv | L60 |
| clk_rst_if | tb | opentitan\hw\ip\adc_ctrl\dv\tb.sv | L59 |
| clk_rst_if | tb | opentitan\hw\ip\aes\dv\tb\tb.sv | L27 |
| clk_rst_if | tb | opentitan\hw\ip\aon_timer\dv\tb.sv | L29 |
| clk_rst_if | tb | opentitan\hw\ip\csrng\dv\tb.sv | L28 |
| clk_rst_if | tb | opentitan\hw\ip\dma\dv\tb\tb.sv | L21 |
| clk_rst_if | tb | opentitan\hw\ip\edn\dv\tb.sv | L24 |
| clk_rst_if | tb | opentitan\hw\ip\entropy_src\dv\tb\tb.sv | L32 |
| clk_rst_if | tb | opentitan\hw\ip\hmac\dv\tb\tb.sv | L25 |
| clk_rst_if | tb | opentitan\hw\ip\i2c\dv\tb\tb.sv | L44 |
| clk_rst_if | tb | opentitan\hw\ip\keymgr\dv\tb.sv | L20 |
| clk_rst_if | tb | opentitan\hw\ip\keymgr_dpe\dv\tb.sv | L22 |
| clk_rst_if | tb | opentitan\hw\ip\kmac\dv\tb.sv | L24 |
| clk_rst_if | tb | opentitan\hw\ip\lc_ctrl\dv\tb.sv | L55 |
| clk_rst_if | tb | opentitan\hw\ip\mbx\dv\tb.sv | L21 |
| clk_rst_if | tb | opentitan\hw\ip\otbn\dv\uvm\tb.sv | L64 |
| clk_rst_if | tb | opentitan\hw\ip\pattgen\dv\tb.sv | L28 |
| clk_rst_if | prim_prince_tb | opentitan\hw\ip\prim\dv\prim_prince\tb\prim_prince_tb.sv | L60 |

## method

| Source | Target | Evidence file | Location |
| --- | --- | --- | --- |
| ProcessFuture | .__init__() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py | L103 |
| ProcessFuture | .cancel() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py | L107 |
| ProcessResult | .__init__() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py | L115 |
| Process | .__init__() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py | L138 |
| Process | .kill() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py | L165 |
| Process | .kill_restart() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py | L170 |
| Process | .poll() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py | L173 |
| ProcessRunner | .__init__() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py | L227 |
| ProcessRunner | .append() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py | L235 |
| ProcessRunner | .start_loop() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py | L238 |
| ProcessRunner | .children_used_mem() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py | L241 |
| ProcessRunner | .mem_avail() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py | L244 |
| ProcessRunner | .poll() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py | L249 |
| Strategy | .__init__() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py | L386 |
| AigerWitness | .parse() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\aiw.rs | L22 |
| AigerWitness | .init_simulation() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\aiw.rs | L61 |
| AigerWitness | .simulate_to_step() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\aiw.rs | L66 |
| BitVec | .new() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\bitvec.rs | L14 |
| BitVec | .fill_zero() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\bitvec.rs | L21 |
| BitVec | .set() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\bitvec.rs | L28 |
| BitVec | .push() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\bitvec.rs | L37 |
| BitVec | .get() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\bitvec.rs | L46 |
| BitVec | .iter() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\bitvec.rs | L54 |
| BitVec | .from_iter() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\bitvec.rs | L60 |
| VMapWire | .aig_edge() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\vmap.rs | L18 |
| VMap | .parse() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\vmap.rs | L36 |
| VMap | .to_hierarchy() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\vmap.rs | L81 |
| VMapWireGroup<'a> | .aig_edges() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\vmap.rs | L68 |
| WireHierarchy<'a> | .walk() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\vmap.rs | L137 |
| WireHierarchy<'a> | .find() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\vmap.rs | L146 |
| WireHierarchy<'a> | .append_to_vcd() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\vmap.rs | L155 |
| WireHierarchy<'a> | .named_aiger_vars() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\vmap.rs | L180 |
| YWMap | .parse() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\ywmap.rs | L31 |
| YWMap | .decode_name() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\ywmap.rs | L37 |
| YWMap | .vmap_wires() | opentitan\hw\vendor\lowrisc_ibex\dv\formal\aig-manip\src\ywmap.rs | L44 |
| RegressionMetadata | .__post_init__() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L126 |
| RegressionMetadata | ._setup_directories() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L143 |
| RegressionMetadata | ._get_ibex_metadata() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L160 |
| RegressionMetadata | .get_tests_and_counts() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L260 |
| RegressionMetadata | .process_riscvdv_testlist() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L300 |
| RegressionMetadata | .process_directed_testlist() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L316 |
| Ops | .__str__() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L342 |
| LockedMetadata | ._handler() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L488 |
| LockedMetadata | .__init__() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L492 |
| LockedMetadata | .__enter__() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L502 |
| LockedMetadata | .__exit__() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L520 |
| testdata_cls | .format_to_printable_dict() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\scripts_lib.py | L317 |
| Failure_Modes | .__str__() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\test_run_result.py | L34 |
| TestRunResult | .format_to_printable_dict() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\test_run_result.py | L116 |
| DashboardElement | .__init__() | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\report_lib\svg.py | L26 |

## rationale_for

| Source | Target | Evidence file | Location |
| --- | --- | --- | --- |
| _process_ibex_sim_log_fd() | Process ibex simulation log.      Reads from log_fd, which should be a file ob | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L44 |
| process_ibex_sim_log() | Process ibex simulation log.      Extract instruction and affected register in | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L92 |
| convert_operands_to_abi() | Convert the operand string to use ABI register naming.      At this stage in t | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L113 |
| expand_trace_entry() | Expands a CSV trace entry for a single instruction.      Operands are added to | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L138 |
| process_imm() | Process imm to follow RISC-V standard convention | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L161 |
| check_ibex_uvm_log() | Process Ibex UVM simulation log.      Process the UVM simulation log produced | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L178 |
| compare_test_run() | Compare results for a single run of a single test.      Use any log-processing | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\check_logs.py | L28 |
| main() | Collect all test results into summary files.      Locate all the individual te | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\collect_results.py | L33 |
| get_riscvdv_compile_cmds() | Run riscv-dv to get a list of build/compilation commands.      These will need | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\compile_test.py | L28 |
| get_directed_compile_cmds() | Construct the build/compilation commands from the directed_testlist data. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\compile_test.py | L153 |
| make_valid_pathlib_path() | Pre-converter to ensure input can be converted to a Path. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\directed_test_schema.py | L20 |
| validate_path_exists() | Validatate that a path object exists, relative to a common file (dt). | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\directed_test_schema.py | L30 |
| DConfig | Represent a common configuration for building directed tests.      This object | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\directed_test_schema.py | L38 |
| DTest | Represent a entry for a single directed test.      Each directed test (DTest) | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\directed_test_schema.py | L72 |
| DirectedTestsYaml | Represent the schema for the <directed-tests>.yaml file.      The file on-disk | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\directed_test_schema.py | L100 |
| import_model() | Import and validate data against the model schema, return data as dict.      I | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\directed_test_schema.py | L166 |
| ibex_cmd.py | # NOTE: This logic should match the code in the get_isa_string() function | ibex\dv\uvm\core_ibex\scripts\ibex_cmd.py | L96 |
| get_isas_for_config() | Get ISA and ISS_ISA keys for the given Ibex config. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\ibex_cmd.py | L95 |
| filter_tests_by_config() | Filter out any unsupported tests from being executed.      e.g. if the "small" | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\ibex_cmd.py | L128 |
| # NOTE: This logic should match the code in the get_isa_string() function | ibex_cmd.py | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\ibex_cmd.py | L96 |
| find_cov_dbs() | Gather a set of the coverage databases. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\merge_cov.py | L22 |
| merge_cov_xlm() | Merge xcelium-generated coverage using the OT scripts.      The vendored-in Op | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\merge_cov.py | L60 |
| main() | Entry point when run as a script | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\merge_cov.py | L134 |
| RegressionMetadata | Holds metadata about the current builds.      Optional fields mean that they h | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L44 |
| .__post_init__() | Construct all the dependent metadata. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L127 |
| ._setup_directories() | Set the directory variables which contain all other build factors. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L144 |
| ._get_ibex_metadata() | Get the desired ibex_config parameters.          # Any extra derivative data c | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L161 |
| .get_tests_and_counts() | Get a list of tests and the number of iterations to run of each.          ibex | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L261 |
| .process_riscvdv_testlist() | Extract test information from the riscvdv testlist yaml. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L301 |
| .process_directed_testlist() | Extract test information from the directed_test yaml.          Employ a simila | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L317 |
| Ops | Type of operations that can be specified by an argparse arg. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L337 |
| LockedMetadata | Construct instance of RegressionMetadata, while locking the on-disk file. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L468 |
| .__init__() | Construct object corresponding to the on-disk file.          Args: | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L493 |
| .__enter__() | Provide a way to access the in-filesystem object safely (holds a lock). | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L503 |
| .__exit__() | Close our exclusive access to the file, committing any changes to disk. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\metadata.py | L521 |
| _main() | Renders a mako template providing parameters from the metadata ibex     config | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\render_config_template.py | L22 |
| riscvdv_interface.py | Defines the interface to riscvdv features for random instruction generation and | ibex\dv\uvm\core_ibex\scripts\riscvdv_interface.py | L1 |
| get_run_cmd() | Return the command parts of a call to riscv-dv's run.py. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\riscvdv_interface.py | L42 |
| get_cov_cmd() | Return the the command to generate riscv-dv's functional coverage. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\riscvdv_interface.py | L62 |
| get_tool_cmds() | Substitute options and environment variables to construct a final command. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\riscvdv_interface.py | L86 |
| _get_yaml_for_simulator() | Get the entry for the simulator in RTL simulation yaml.      riscv-dv specifie | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\riscvdv_interface.py | L175 |
| Defines the interface to riscvdv features for random instruction generation and | riscvdv_interface.py | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\riscvdv_interface.py | L1 |
| reloc_commands() | Read (one) line in src and apply relocations to it.      The result should be | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\run_instr_gen.py | L34 |
| reloc_word() | Helper function for reloc_commands that relocates just one word. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\run_instr_gen.py | L57 |
| do_file_copies() | Copy files back from src_dir to dst_dir, following copy_rules.      These rule | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\run_instr_gen.py | L127 |
| _main() | Generate and run rtl simulation commands. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\run_rtl.py | L25 |
| run_one() | Run a command, returning its retcode.      If verbose is true, print the comma | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\scripts_lib.py | L31 |
| format_to_cmd() | Format useful compound-lists into list[str], suitable for subprocess.      Can | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\scripts_lib.py | L108 |
| subst_opt() | Substitute the <name> option in string with 'replacement'. | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\scripts_lib.py | L124 |
| subst_dict() | Apply substitutions in var_dict to string.      If <K> in string, substitute < | opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\scripts_lib.py | L137 |

## uses

| Source | Target | Evidence file | Location |
| --- | --- | --- | --- |
| Process ibex simulation log.      Reads from log_fd, which should be a file ob | RiscvInstructionTraceCsv | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L22 |
| Process ibex simulation log.      Reads from log_fd, which should be a file ob | RiscvInstructionTraceEntry | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L22 |
| Process ibex simulation log.      Reads from log_fd, which should be a file ob | Failure_Modes | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L32 |
| Process ibex simulation log.      Extract instruction and affected register in | RiscvInstructionTraceCsv | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L22 |
| Process ibex simulation log.      Extract instruction and affected register in | RiscvInstructionTraceEntry | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L22 |
| Process ibex simulation log.      Extract instruction and affected register in | Failure_Modes | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L32 |
| Convert the operand string to use ABI register naming.      At this stage in t | RiscvInstructionTraceCsv | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L22 |
| Convert the operand string to use ABI register naming.      At this stage in t | RiscvInstructionTraceEntry | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L22 |
| Convert the operand string to use ABI register naming.      At this stage in t | Failure_Modes | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L32 |
| Expands a CSV trace entry for a single instruction.      Operands are added to | RiscvInstructionTraceCsv | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L22 |
| Expands a CSV trace entry for a single instruction.      Operands are added to | RiscvInstructionTraceEntry | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L22 |
| Expands a CSV trace entry for a single instruction.      Operands are added to | Failure_Modes | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L32 |
| Process imm to follow RISC-V standard convention | RiscvInstructionTraceCsv | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L22 |
| Process imm to follow RISC-V standard convention | RiscvInstructionTraceEntry | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L22 |
| Process imm to follow RISC-V standard convention | Failure_Modes | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L32 |
| Process Ibex UVM simulation log.      Process the UVM simulation log produced | RiscvInstructionTraceCsv | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L22 |
| Process Ibex UVM simulation log.      Process the UVM simulation log produced | RiscvInstructionTraceEntry | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L22 |
| Process Ibex UVM simulation log.      Process the UVM simulation log produced | Failure_Modes | ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_log_to_trace_csv.py | L32 |
| Compare results for a single run of a single test.      Use any log-processing | TestRunResult | ibex\dv\uvm\core_ibex\scripts\check_logs.py | L17 |
| Compare results for a single run of a single test.      Use any log-processing | Failure_Modes | ibex\dv\uvm\core_ibex\scripts\check_logs.py | L17 |
| Collect all test results into summary files.      Locate all the individual te | RegressionMetadata | ibex\dv\uvm\core_ibex\scripts\collect_results.py | L11 |
| Collect all test results into summary files.      Locate all the individual te | LockedMetadata | ibex\dv\uvm\core_ibex\scripts\collect_results.py | L11 |
| Collect all test results into summary files.      Locate all the individual te | TestRunResult | ibex\dv\uvm\core_ibex\scripts\collect_results.py | L12 |
| Collect all test results into summary files.      Locate all the individual te | Failure_Modes | ibex\dv\uvm\core_ibex\scripts\collect_results.py | L12 |
| Run riscv-dv to get a list of build/compilation commands.      These will need | RegressionMetadata | ibex\dv\uvm\core_ibex\scripts\compile_test.py | L20 |
| Run riscv-dv to get a list of build/compilation commands.      These will need | TestRunResult | ibex\dv\uvm\core_ibex\scripts\compile_test.py | L21 |
| Run riscv-dv to get a list of build/compilation commands.      These will need | TestType | ibex\dv\uvm\core_ibex\scripts\compile_test.py | L21 |
| Construct the build/compilation commands from the directed_testlist data. | RegressionMetadata | ibex\dv\uvm\core_ibex\scripts\compile_test.py | L20 |
| Construct the build/compilation commands from the directed_testlist data. | TestRunResult | ibex\dv\uvm\core_ibex\scripts\compile_test.py | L21 |
| Construct the build/compilation commands from the directed_testlist data. | TestType | ibex\dv\uvm\core_ibex\scripts\compile_test.py | L21 |
| GenError | Config | ibex\dv\uvm\core_ibex\scripts\ibex_cmd.py | L11 |
| Get ISA and ISS_ISA keys for the given Ibex config. | Config | ibex\dv\uvm\core_ibex\scripts\ibex_cmd.py | L11 |
| Filter out any unsupported tests from being executed.      e.g. if the "small" | Config | ibex\dv\uvm\core_ibex\scripts\ibex_cmd.py | L11 |
| # NOTE: This logic should match the code in the get_isa_string() function | Config | ibex\dv\uvm\core_ibex\scripts\ibex_cmd.py | L11 |
| Gather a set of the coverage databases. | RegressionMetadata | ibex\dv\uvm\core_ibex\scripts\merge_cov.py | L16 |
| Gather a set of the coverage databases. | LockedMetadata | ibex\dv\uvm\core_ibex\scripts\merge_cov.py | L16 |
| Merge xcelium-generated coverage using the OT scripts.      The vendored-in Op | RegressionMetadata | ibex\dv\uvm\core_ibex\scripts\merge_cov.py | L16 |
| Merge xcelium-generated coverage using the OT scripts.      The vendored-in Op | LockedMetadata | ibex\dv\uvm\core_ibex\scripts\merge_cov.py | L16 |
| Entry point when run as a script | RegressionMetadata | ibex\dv\uvm\core_ibex\scripts\merge_cov.py | L16 |
| Entry point when run as a script | LockedMetadata | ibex\dv\uvm\core_ibex\scripts\merge_cov.py | L16 |
| RegressionMetadata | TestRunResult | ibex\dv\uvm\core_ibex\scripts\metadata.py | L31 |
| RegressionMetadata | TestType | ibex\dv\uvm\core_ibex\scripts\metadata.py | L31 |
| RegressionMetadata | Renders a mako template providing parameters from the metadata ibex     config | ibex\dv\uvm\core_ibex\scripts\render_config_template.py | L11 |
| RegressionMetadata | Defines the interface to riscvdv features for random instruction generation and | ibex\dv\uvm\core_ibex\scripts\riscvdv_interface.py | L24 |
| RegressionMetadata | Return the command parts of a call to riscv-dv's run.py. | ibex\dv\uvm\core_ibex\scripts\riscvdv_interface.py | L24 |
| RegressionMetadata | Return the the command to generate riscv-dv's functional coverage. | ibex\dv\uvm\core_ibex\scripts\riscvdv_interface.py | L24 |
| RegressionMetadata | Substitute options and environment variables to construct a final command. | ibex\dv\uvm\core_ibex\scripts\riscvdv_interface.py | L24 |
| RegressionMetadata | Get the entry for the simulator in RTL simulation yaml.      riscv-dv specifie | ibex\dv\uvm\core_ibex\scripts\riscvdv_interface.py | L24 |
| RegressionMetadata | Read (one) line in src and apply relocations to it.      The result should be | ibex\dv\uvm\core_ibex\scripts\run_instr_gen.py | L21 |
| RegressionMetadata | Helper function for reloc_commands that relocates just one word. | ibex\dv\uvm\core_ibex\scripts\run_instr_gen.py | L21 |
