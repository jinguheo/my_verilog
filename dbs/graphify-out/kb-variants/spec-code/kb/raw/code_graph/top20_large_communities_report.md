# DBS Large Communities - Top 20

- Source graph: `dbs\graphify-out\graph.json`
- Source graph size: 39,694 nodes / 95,961 edges
- Limited member graph: 2,963 nodes / 11,065 edges, cap 150 nodes per community

## Top Communities

| Rank | Community | Nodes | Internal edges | Sampled | Top source files |
|---:|---:|---:|---:|---:|---|
| 1 | 0 | 4,551 | 12,891 | 150 | `opentitan\util\topgen\lib.py` (114)<br>`opentitan\hw\ip\otbn\util\shared\information_flow.py` (98)<br>`opentitan\util\topgen\merge.py` (72) |
| 2 | 1 | 4,320 | 14,640 | 150 | `opentitan\sw\host\opentitanlib\src\app\mod.rs` (70)<br>`opentitan\sw\host\opentitanlib\src\util\vcd.rs` (62)<br>`opentitan\sw\host\ot_certs\src\template\subst.rs` (57) |
| 3 | 2 | 3,770 | 4,895 | 150 | `ibex\vendor\riscv-tests\benchmarks\common\syscalls.c` (23)<br>`ibex\vendor\riscv-isa-sim\tests\mseccfg\gengen_src\outputs\test_pmp_ok_share_1_r0_x0_cfgl0_typex1_umode1.c` (10)<br>`ibex\vendor\riscv-isa-sim\tests\mseccfg\gengen_src\outputs\test_pmp_ok_share_1_r0_x1_cfgl1_typex0_umode1.c` (10) |
| 4 | 3 | 3,613 | 12,589 | 150 | `opentitan\sw\device\lib\dif\dif_spi_device.c` (66)<br>`opentitan\sw\device\lib\dif\dif_flash_ctrl.c` (55)<br>`opentitan\sw\device\lib\dif\dif_usbdev.c` (52) |
| 5 | 4 | 2,114 | 3,892 | 150 | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` (15)<br>`opentitan\hw\ip\spi_device\rtl\spi_device.sv` (14)<br>`opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_ctrl.sv` (13) |
| 6 | 5 | 1,732 | 6,854 | 150 | `opentitan\sw\device\tests\penetrationtests\firmware\fi\ibex_fi.c` (59)<br>`opentitan\sw\device\tests\penetrationtests\firmware\lib\pentest_lib.c` (35)<br>`opentitan\sw\device\tests\penetrationtests\firmware\sca\cryptolib_sca_asym.c` (35) |
| 7 | 6 | 1,300 | 3,183 | 150 | `opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c` (34)<br>`opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\scripts\gen_csr_test.py` (29)<br>`opentitan\sw\device\lib\crypto\drivers\entropy.c` (26) |
| 8 | 7 | 1,144 | 2,165 | 150 | `opentitan\hw\ip\otbn\dv\otbnsim\sim\insn.py` (170)<br>`opentitan\hw\ip\otbn\dv\otbnsim\sim\kmac_ispr.py` (95)<br>`opentitan\hw\ip\otbn\dv\otbnsim\sim\state.py` (68) |
| 9 | 8 | 1,129 | 3,741 | 150 | `opentitan\sw\host\penetrationtests\python\fi\communication\fi_ibex_commands.py` (94)<br>`opentitan\hw\ip\otbn\dv\otbnsim\test\generate_bn_simd_tests.py` (74)<br>`opentitan\sw\host\penetrationtests\python\fi\host_scripts\fi_ibex_functions.py` (48) |
| 10 | 9 | 1,081 | 2,715 | 150 | `opentitan\hw\ip\otbn\dv\model\otbn_model.cc` (59)<br>`sv-tests\conf\report\report.js` (42)<br>`opentitan\hw\vendor\lowrisc_ibex\dv\cosim\spike_cosim.cc` (40) |
| 11 | 10 | 952 | 1,593 | 150 | `opentitan\sw\host\opentitanlib\src\transport\mod.rs` (17)<br>`opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\tb\tb.sv` (10)<br>`RTLLM\Arithmetic\Adder\adder_32bit\verified_adder_32bit.v` (9) |
| 12 | 11 | 724 | 1,609 | 150 | `ibex\vendor\riscv-tests\debug\gdbserver.py` (246)<br>`ibex\vendor\riscv-tests\debug\testlib.py` (105)<br>`opentitan\sw\host\provisioning\orchestrator\tests\device_id_test.py` (21) |
| 13 | 12 | 651 | 1,754 | 150 | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_asm_program_gen.py` (66)<br>`opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_pkg.py` (51)<br>`opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_load_store_instr_lib.py` (26) |
| 14 | 13 | 500 | 1,367 | 150 | `opentitan\util\dvsim\Deploy.py` (77)<br>`opentitan\util\dvsim\Scheduler.py` (37)<br>`opentitan\util\dvsim\FlowCfg.py` (31) |
| 15 | 14 | 422 | 958 | 150 | `opentitan\hw\ip\otbn\dv\rig\rig\model.py` (73)<br>`opentitan\hw\ip\otbn\dv\rig\rig\snippet.py` (40)<br>`opentitan\hw\ip\otbn\dv\rig\rig\config.py` (26) |
| 16 | 15 | 377 | 1,096 | 150 | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py` (355)<br>`opentitan\sw\host\opentitanlib\src\debug\elf_debugger.rs` (8)<br>`opentitan\sw\host\hsmtool\src\commands\spx\export.rs` (2) |
| 17 | 16 | 294 | 665 | 150 | `opentitan\util\dtgen\helper.py` (109)<br>`opentitan\util\topgen\lib.py` (34)<br>`opentitan\hw\ip\otbn\util\docs\get_impl.py` (31) |
| 18 | 17 | 254 | 543 | 150 | `opentitan\sw\vendor\freertos_freertos_kernel\tasks.c` (86)<br>`opentitan\sw\vendor\freertos_freertos_kernel\queue.c` (51)<br>`opentitan\sw\vendor\freertos_freertos_kernel\timers.c` (28) |
| 19 | 18 | 180 | 498 | 150 | `opentitan\util\tlgen\item.py` (20)<br>`ibex\examples\sw\simple_system\common\simple_system_common.c` (17)<br>`opentitan\third_party\coremark\top_earlgrey\ee_printf.c` (14) |
| 20 | 19 | 113 | 205 | 113 | `opentitan\hw\ip\prim\util\vendor\google_verible_verilog_syntax_py\verible_verilog_syntax.py` (62)<br>`opentitan\hw\ip\prim\util\vendor\google_verible_verilog_syntax_py\verible_verilog_syntax_test.py` (19)<br>`opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\scripts\report_lib\svg.py` (15) |

## Strongest Cross-Community Edges

| Source | Target | Edges | Top relations |
|---:|---:|---:|---|
| 3 | 5 | 1,040 | calls:837, contains:106, imports:90, instantiates:7 |
| 0 | 1 | 966 | calls:924, method:27, contains:13, uses:1, imports_from:1 |
| 0 | 8 | 718 | calls:694, method:15, contains:9 |
| 3 | 6 | 573 | calls:408, imports:117, contains:42, instantiates:6 |
| 0 | 2 | 532 | calls:532 |
| 5 | 6 | 429 | calls:359, imports:43, contains:27 |
| 0 | 11 | 415 | calls:357, contains:31, method:18, inherits:9 |
| 0 | 12 | 374 | calls:244, method:61, contains:24, uses:17, imports_from:13 |
| 0 | 13 | 337 | calls:223, method:58, rationale_for:22, uses:16, contains:10 |
| 1 | 8 | 318 | calls:308, method:7, contains:3 |
| 0 | 9 | 241 | calls:214, imports:11, contains:10, method:6 |
| 0 | 14 | 215 | calls:171, method:38, contains:5, inherits:1 |
| 0 | 7 | 213 | calls:145, method:42, contains:20, imports_from:5, inherits:1 |
| 0 | 16 | 200 | calls:173, method:20, contains:6, imports:1 |
| 1 | 9 | 130 | calls:113, contains:9, method:6, inherits:2 |
| 11 | 8 | 116 | calls:97, method:19 |
| 10 | 4 | 113 | imports_from:91, instantiates:22 |
| 1 | 3 | 108 | calls:54, imports:28, imports_from:12, instantiates:9, contains:4 |
| 1 | 11 | 86 | calls:78, method:6, contains:2 |
| 3 | 4 | 71 | imports_from:33, imports:20, instantiates:18 |
| 5 | 9 | 70 | calls:62, imports:7, method:1 |
| 1 | 6 | 69 | calls:39, imports:23, contains:4, method:2, imports_from:1 |
| 12 | 8 | 51 | calls:50, contains:1 |
| 1 | 7 | 49 | calls:43, method:3, contains:2, inherits:1 |
| 0 | 6 | 42 | calls:39, imports:1, inherits:1, contains:1 |
| 0 | 19 | 40 | calls:36, imports_from:2, method:2 |
| 1 | 13 | 39 | calls:33, contains:2, method:2, inherits:1, imports_from:1 |
| 7 | 8 | 36 | calls:35, method:1 |
| 10 | 3 | 35 | instantiates:27, imports_from:8 |
| 8 | 9 | 28 | calls:26, contains:1, method:1 |
| 0 | 15 | 27 | calls:13, inherits:12, method:1, contains:1 |
| 1 | 15 | 26 | imports_from:17, calls:4, method:3, contains:2 |
| 0 | 18 | 24 | calls:13, contains:7, imports_from:4 |
| 12 | 7 | 24 | inherits:12, imports_from:5, calls:4, contains:3 |
| 6 | 9 | 24 | calls:22, imports:1, contains:1 |
| 13 | 8 | 23 | calls:23 |
| 1 | 16 | 22 | calls:21, method:1 |
| 1 | 5 | 22 | calls:19, imports:2, imports_from:1 |
| 14 | 8 | 21 | calls:20, imports_from:1 |
| 4 | 6 | 18 | imports:18 |
| 1 | 12 | 17 | calls:17 |
| 3 | 9 | 16 | calls:13, imports:2, imports_from:1 |
| 0 | 5 | 15 | calls:15 |
| 0 | 3 | 15 | calls:12, imports:1, contains:1, method:1 |
| 7 | 9 | 13 | calls:10, contains:3 |
| 1 | 10 | 13 | imports_from:6, calls:4, instantiates:2, method:1 |
| 1 | 18 | 12 | calls:10, contains:1, inherits:1 |
| 1 | 14 | 11 | calls:9, method:2 |
| 14 | 7 | 11 | calls:10, method:1 |
| 13 | 9 | 10 | calls:5, imports_from:2, contains:2, method:1 |
