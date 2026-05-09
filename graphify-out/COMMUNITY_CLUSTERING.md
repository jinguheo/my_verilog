# Community Clustering

- Source: graphify-out/GRAPH_REPORT.md
- Generated: 2026-04-29
- Method: parsed community sections from GRAPH_REPORT.md, then added size buckets and heuristic topic labels from sample node names.

## Graph Summary

| Metric | Value |
|---|---:|
| Corpus files | 9183 |
| Corpus words | 18352768 |
| Nodes | 37985 |
| Edges | 91947 |
| Communities detected | 815 |
| Communities parsed | 815 |
| Extracted edges | 53% |
| Inferred edges | 47% |
| Inferred edge count | 43558 |
| Inferred avg confidence | 0.79 |

## God Nodes

| Rank | Node | Edges |
|---:|---|---:|
| 1 | `OK()` | 1849 |
| 2 | `tohost_exit()` | 748 |
| 3 | `Format` | 737 |
| 4 | `get()` | 498 |
| 5 | `mmio_region_read32()` | 479 |
| 6 | `memcpy()` | 469 |
| 7 | `Open()` | 403 |
| 8 | `mmio_region_write32()` | 402 |
| 9 | `uvm_pkg` | 335 |
| 10 | `memset()` | 324 |

## Size Buckets

| Bucket | Communities | Nodes |
|---|---:|---:|
| thin <=2 | 500 | 526 |
| small 10-99 | 237 | 3459 |
| tiny 3-9 | 60 | 346 |
| medium 100-499 | 10 | 2376 |
| core >=1000 | 5 | 12246 |
| large 500-999 | 3 | 2325 |

## Topic Buckets

| Topic | Communities | Nodes |
|---|---:|---:|
| Thin/noise candidate | 500 | 526 |
| Mixed/uncategorized | 260 | 5604 |
| OpenTitan firmware and crypto | 24 | 9602 |
| KG platform services | 11 | 242 |
| RISC-V/OTBN/ISS tooling | 8 | 207 |
| SystemVerilog DV/UVM packages | 4 | 3654 |
| EDA, regression, and config tooling | 4 | 603 |
| Database/device metadata tooling | 2 | 222 |
| VerilogEval and generated RTL tests | 1 | 614 |
| Parser/source text utilities | 1 | 4 |

## Top Communities

| Rank | Community | Nodes | Cohesion | Size bucket | Topic label | Sample nodes |
|---:|---:|---:|---:|---|---|---|
| 1 | 0 | 3421 | 0 | core >=1000 | SystemVerilog DV/UVM packages | HwAccess<br>Return a UVM access string as used by uvm_base_reg_field abstraction.<br>Should the register for this field have a write-enable signal? This i<br>Return a UVM access string as used by uvm_field::set_access().<br>SwAccess<br>replace_module_name() |
| 2 | 3 | 3130 | 0 | core >=1000 | OpenTitan firmware and crypto | configure_adc_ctrl()<br>en_plic_irqs()<br>ottf_handle_irq()<br>test_main()<br>execute_test()<br>test_main() |
| 3 | 2 | 2439 | 0 | core >=1000 | OpenTitan firmware and crypto | debug_printf()<br>Func_1()<br>Func_2()<br>main()<br>DisParser<br>AsymCryptolibFiSim |
| 4 | 1 | 1861 | 0 | core >=1000 | Mixed/uncategorized | main()<br>Opts<br>test_access_after_hw_reset()<br>main()<br>Opts<br>test_access_after_wakeup() |
| 5 | 4 | 1395 | 0.01 | core >=1000 | OpenTitan firmware and crypto | absorb_bytes()<br>aes_base()<br>aes_begin()<br>aes_decrypt_begin()<br>aes_encrypt_begin()<br>aes_end() |
| 6 | 6 | 933 | 0 | large 500-999 | OpenTitan firmware and crypto | spx_addr_chain_set()<br>spx_addr_hash_set()<br>spx_addr_keypair_copy()<br>spx_addr_keypair_set()<br>spx_addr_layer_set()<br>spx_addr_set_byte() |
| 7 | 8 | 778 | 0.01 | large 500-999 | OpenTitan firmware and crypto | crypto_aead_decrypt()<br>crypto_aead_encrypt()<br>aes_add_round_key()<br>aes_decrypt_block()<br>aes_encrypt_block()<br>aes_get_num_rounds() |
| 8 | 10 | 614 | 0 | large 500-999 | VerilogEval and generated RTL tests | stimulus_gen<br>stimulus_gen<br>tb<br>stimulus_gen<br>tb<br>stimulus_gen |
| 9 | 9 | 492 | 0.01 | medium 100-499 | OpenTitan firmware and crypto | generate_build_info_c_source()<br>main()<br>Return the contents of a C source file that defines `kBuildInfo`. Args:<br>Creates build_info.c in `outdir`. Returns the path to the new file.<br>write_source_file()<br>gen_div_word_test() |
| 10 | 7 | 459 | 0 | medium 100-499 | EDA, regression, and config tooling | BaseRunner<br>Attempt to get the commit hash of the tool. The result is based on the<br>Get the top-level module from the params<br>or guess it<br>BnVecVecAdd<br>BnVecVecMul |
| 11 | 11 | 295 | 0.01 | medium 100-499 | Mixed/uncategorized | JsonEnum<br>SwRdAccess<br>SwWrAccess<br>check_sw_image()<br>Check that a sw_image is valid. Parameters: name: Name of the te<br>SwType |
| 12 | 5 | 226 | 0 | medium 100-499 | SystemVerilog DV/UVM packages | ac_range_check_env_pkg<br>ac_range_check_reg_pkg<br>ac_range_check_test_pkg<br>adc_ctrl_env_pkg<br>adc_ctrl_pkg<br>adc_ctrl_reg_pkg |
| 13 | 12 | 204 | 0.01 | medium 100-499 | Database/device metadata tooling | create_table()<br>create_table_string()<br>DB<br>DBConfig<br>query()<br>query_all() |
| 14 | 13 | 178 | 0.01 | medium 100-499 | OpenTitan firmware and crypto | ABC<br>Alert<br>ClkmgrExt<br>create_ext()<br>ClockMeasureConfig<br>config_clk_meas() |
| 15 | 14 | 169 | 0.02 | medium 100-499 | Mixed/uncategorized | prvCheckDelayedList()<br>prvCheckPendingReadyList()<br>prvInitialiseCoRoutineLists()<br>vCoRoutineAddToDelayedList()<br>vCoRoutineSchedule()<br>xCoRoutineCreate() |
| 16 | 17 | 126 | 0.03 | medium 100-499 | Mixed/uncategorized | calc_func()<br>cmp_complex()<br>cmp_idx()<br>copy_info()<br>core_bench_list()<br>core_list_find() |
| 17 | 16 | 116 | 0.02 | medium 100-499 | EDA, regression, and config tooling | WARN()<br>BazelQuery<br>BazelQueryRunner<br>Perform a Bazel query and return the resulting targets.<br>A collection of functions useful for constructing Bazel queries.<br>Find targets in //... with names containing disallowed characters. Ba |
| 18 | 15 | 111 | 0.02 | medium 100-499 | Mixed/uncategorized | Creates the launcher instance. Note that the launcher instance for AL<br>Launcher<br>ErrorMessage<br>Launcher<br>LauncherBusy<br>LauncherError |
| 19 | 18 | 82 | 0.03 | small 10-99 | RISC-V/OTBN/ISS tooling | BadAtEnd<br>A snippet generator that generates a loop/branch/jump at end of a loop Th<br>BadBranch<br>A snippet generator that generates program ending branch instructions. Th<br>BadGiantLoop<br>A generator for loops with end addresses that don't lie in memory This ge |
| 20 | 19 | 75 | 0.03 | small 10-99 | KG platform services | BusInterfaces<br>_if_dict()<br>Look up the given host/name pair and return its port name. Raises a K<br>CdcCfg<br>Derivative class for linting purposes.<br>gen_cfg_md() |
| 21 | 22 | 70 | 0.05 | small 10-99 | RISC-V/OTBN/ISS tooling | device_log_bypass_uart_address()<br>device_test_status_address()<br>rv_core_ibex_base()<br>check_crc32()<br>main()<br>roundtrip() |
| 22 | 23 | 68 | 0.08 | small 10-99 | Mixed/uncategorized | addM()<br>copyConditional()<br>copy_conditional()<br>felem_assign()<br>felem_diff()<br>felem_inv() |
| 23 | 24 | 58 | 0.07 | small 10-99 | OpenTitan firmware and crypto | dif_spi_host_transaction()<br>ConfigTest<br>ErrorEnableRegTest<br>ErrorStatusTest<br>EventEnableRegTest<br>FifoTest |
| 24 | 20 | 53 | 0.03 | small 10-99 | KG platform services | main()<br>process_file_data()<br>Print information about modules found in SystemVerilog file. This function<br>main()<br>process_file_data()<br>Print tree representation to the console. The function uses anytree module |
| 25 | 21 | 48 | 0.03 | small 10-99 | Mixed/uncategorized | blake2_provider<br>G()<br>initH()<br>initX()<br>round()<br>blake_provider |
| 26 | 27 | 37 | 0.06 | small 10-99 | Mixed/uncategorized | main()<br>Oid<br>Tag<br>pmp_csr_1_gen_class()<br>set_addr_offset()<br>set_cfg_idx() |
| 27 | 26 | 35 | 0.11 | small 10-99 | Mixed/uncategorized | kill_child_processes()<br>bmc()<br>bmc_mode()<br>build_strategy_rec()<br>construct_strategy()<br>decode_strategy() |
| 28 | 25 | 31 | 0.05 | small 10-99 | Mixed/uncategorized | matmul()<br>matmul()<br>matmul()<br>matmul()<br>matmul()<br>matmul() |
| 29 | 30 | 31 | 0.07 | small 10-99 | RISC-V/OTBN/ISS tooling | Prepare to start the execution. Use run() or step() to actually execu<br>Check the contents of the external registers after a successful run.<br>Test an invalid instruction is reflected in ERR_BITS.<br>test_ext_regs_err_bits_bad()<br>test_ext_regs_success()<br>ExecutionStats |
| 30 | 37 | 28 | 0.07 | small 10-99 | Mixed/uncategorized | BitbangEntryRequest<br>BitbangEntryResponse<br>DacBangEntryRequest<br>EmuRequest<br>EmuResponse<br>FgpaResponse |
| 31 | 38 | 27 | 0.07 | small 10-99 | Mixed/uncategorized | AutoOverrideConfigTest<br>AutoOverrideGetEnabledTest<br>AutoOverrideSetEnabledTest<br>InputChangeDetectConfigTest<br>InputChangeIrqClearCausesTest<br>InputChangeIrqGetCausesTest |
| 32 | 32 | 26 | 0.11 | small 10-99 | KG platform services | filter_tests_by_config()<br>GenError<br>get_compile_opts()<br>get_config()<br>get_isas_for_config()<br>get_sim_opts() |
| 33 | 40 | 26 | 0.07 | small 10-99 | OpenTitan firmware and crypto | ClearRecoverableAlertsTest<br>ConditionerStartTest<br>ConditionerStopTest<br>ConfigTest<br>ConfigTestAllParams<br>EntropySrcTest |
| 34 | 28 | 25 | 0.05 | small 10-99 | OpenTitan firmware and crypto | AesInitTest<br>AesTest<br>AesTestInitialized<br>AlertTest<br>CbcTest<br>CFBTest |
| 35 | 36 | 25 | 0.07 | small 10-99 | Mixed/uncategorized | Bus<br>CmdGetDeviceStatus<br>CmdPrepareReadData<br>CmdTransferLong<br>CmdTransferShort<br>DeviceStatus |
| 36 | 34 | 22 | 0.1 | small 10-99 | KG platform services | LLVMFuzzerTestOneInput()<br>RomMockGroup<br>AbstractBootstrapMockGroup()<br>ConfigureMocks()<br>Crash()<br>ParseCmdOr() |
| 37 | 43 | 21 | 0.17 | small 10-99 | Mixed/uncategorized | pmp_addr_csr_read()<br>pmp_addr_csr_write()<br>pmp_address_aligned()<br>pmp_cfg_csr_read()<br>pmp_cfg_csr_write()<br>pmp_cfg_mode_lock_set() |
| 38 | 44 | 21 | 0.21 | small 10-99 | Mixed/uncategorized | c_dpi_prince_decrypt()<br>c_dpi_prince_encrypt()<br>bytes_to_uint64()<br>gf2_mat_mult16_1()<br>prince_core()<br>prince_decrypt() |
| 39 | 50 | 20 | 0.09 | small 10-99 | OpenTitan firmware and crypto | AbortTest<br>ConfigureTest<br>DmaTest<br>DmaTestInitialized<br>ErrorTest<br>GetDigestLenTest |
| 40 | 46 | 19 | 0.08 | small 10-99 | Mixed/uncategorized | AdvanceStateTest<br>AdvanceToNonOperational<br>AdvanceToOperational<br>BadArgsTwo<br>ConfigureTest<br>DifKeymgrInitialized |
| 41 | 45 | 18 | 0.12 | small 10-99 | Mixed/uncategorized | check_regs()<br>format_block()<br>is_wdr()<br>Line<br>main()<br>make_half_word_writeback() |
| 42 | 48 | 18 | 0.09 | small 10-99 | Database/device metadata tooling | KeymgrBindingValue<br>LifecycleDeviceId<br>Manifest<br>ManifestExtHeader<br>ManifestExtImageType<br>ManifestExtIsfbErasePolicy |
| 43 | 55 | 18 | 0.11 | small 10-99 | Mixed/uncategorized | AttributeType<br>BasicConstraints<br>Certificate<br>CertificateExtension<br>Conversion<br>DiceTcbInfoExtension |
| 44 | 52 | 17 | 0.1 | small 10-99 | OpenTitan firmware and crypto | AlertInfoDumpReadTest<br>AlertInfoGetSizeTest<br>AlertInfoGetTest<br>AlertInfoSetTest<br>CpuInfoDumpReadTest<br>CpuInfoGetSizeTest |
| 45 | 57 | 17 | 0.11 | small 10-99 | Mixed/uncategorized | AdcCtrlTest<br>ConfigTest<br>FilterConfigTest<br>FilterMatchWakeupGetEnabledTest<br>FilterMatchWakeupSetEnabledTest<br>FilterStatusTest |
| 46 | 49 | 16 | 0.11 | small 10-99 | KG platform services | Bootstrap<br>BootstrapError<br>BootstrapOptions<br>BootstrapProtocol<br>Capabilities<br>EmptyTransport |
| 47 | 58 | 15 | 0.2 | small 10-99 | EDA, regression, and config tooling | all_paths_must_exist()<br>Config<br>DConfig<br>DirectedTestsYaml<br>DTest<br>make_valid_pathlib_path() |
| 48 | 61 | 15 | 0.12 | small 10-99 | Mixed/uncategorized | BytesReceivePolledTest<br>BytesReceiveTest<br>BytesSendPolledTest<br>BytesSendTest<br>ConfigTest<br>FifoResetTest |
| 49 | 33 | 14 | 0.07 | small 10-99 | OpenTitan firmware and crypto | Mark particular reset as requiring shadow<br>Get available domains for a reset<br>Get generated resets and return reset object<br>Get resets pushed to the top level<br>Get software controlled resets<br>Get path to lpg indication signals |
| 50 | 47 | 14 | 0.08 | small 10-99 | OpenTitan firmware and crypto | AbsorbalignmentMessage<br>ConfigLock<br>Cshake256Test<br>Kmac256Test<br>KmacConfigureTest<br>KmacEndTest |

## All Communities

| Community | Nodes | Cohesion | Size bucket | Topic label | Sample nodes | Omitted nodes |
|---:|---:|---:|---|---|---|---:|
| 0 | 3421 | 0 | core >=1000 | SystemVerilog DV/UVM packages | HwAccess<br>Return a UVM access string as used by uvm_base_reg_field abstraction.<br>Should the register for this field have a write-enable signal? This i<br>Return a UVM access string as used by uvm_field::set_access().<br>SwAccess | 3413 |
| 3 | 3130 | 0 | core >=1000 | OpenTitan firmware and crypto | configure_adc_ctrl()<br>en_plic_irqs()<br>ottf_handle_irq()<br>test_main()<br>execute_test() | 3122 |
| 2 | 2439 | 0 | core >=1000 | OpenTitan firmware and crypto | debug_printf()<br>Func_1()<br>Func_2()<br>main()<br>DisParser | 2431 |
| 1 | 1861 | 0 | core >=1000 | Mixed/uncategorized | main()<br>Opts<br>test_access_after_hw_reset()<br>main()<br>Opts | 1853 |
| 4 | 1395 | 0.01 | core >=1000 | OpenTitan firmware and crypto | absorb_bytes()<br>aes_base()<br>aes_begin()<br>aes_decrypt_begin()<br>aes_encrypt_begin() | 1387 |
| 6 | 933 | 0 | large 500-999 | OpenTitan firmware and crypto | spx_addr_chain_set()<br>spx_addr_hash_set()<br>spx_addr_keypair_copy()<br>spx_addr_keypair_set()<br>spx_addr_layer_set() | 925 |
| 8 | 778 | 0.01 | large 500-999 | OpenTitan firmware and crypto | crypto_aead_decrypt()<br>crypto_aead_encrypt()<br>aes_add_round_key()<br>aes_decrypt_block()<br>aes_encrypt_block() | 770 |
| 10 | 614 | 0 | large 500-999 | VerilogEval and generated RTL tests | stimulus_gen<br>stimulus_gen<br>tb<br>stimulus_gen<br>tb | 606 |
| 9 | 492 | 0.01 | medium 100-499 | OpenTitan firmware and crypto | generate_build_info_c_source()<br>main()<br>Return the contents of a C source file that defines `kBuildInfo`. Args:<br>Creates build_info.c in `outdir`. Returns the path to the new file.<br>write_source_file() | 484 |
| 7 | 459 | 0 | medium 100-499 | EDA, regression, and config tooling | BaseRunner<br>Attempt to get the commit hash of the tool. The result is based on the<br>Get the top-level module from the params<br>or guess it<br>BnVecVecAdd | 451 |
| 11 | 295 | 0.01 | medium 100-499 | Mixed/uncategorized | JsonEnum<br>SwRdAccess<br>SwWrAccess<br>check_sw_image()<br>Check that a sw_image is valid. Parameters: name: Name of the te | 287 |
| 5 | 226 | 0 | medium 100-499 | SystemVerilog DV/UVM packages | ac_range_check_env_pkg<br>ac_range_check_reg_pkg<br>ac_range_check_test_pkg<br>adc_ctrl_env_pkg<br>adc_ctrl_pkg | 218 |
| 12 | 204 | 0.01 | medium 100-499 | Database/device metadata tooling | create_table()<br>create_table_string()<br>DB<br>DBConfig<br>query() | 196 |
| 13 | 178 | 0.01 | medium 100-499 | OpenTitan firmware and crypto | ABC<br>Alert<br>ClkmgrExt<br>create_ext()<br>ClockMeasureConfig | 170 |
| 14 | 169 | 0.02 | medium 100-499 | Mixed/uncategorized | prvCheckDelayedList()<br>prvCheckPendingReadyList()<br>prvInitialiseCoRoutineLists()<br>vCoRoutineAddToDelayedList()<br>vCoRoutineSchedule() | 161 |
| 17 | 126 | 0.03 | medium 100-499 | Mixed/uncategorized | calc_func()<br>cmp_complex()<br>cmp_idx()<br>copy_info()<br>core_bench_list() | 118 |
| 16 | 116 | 0.02 | medium 100-499 | EDA, regression, and config tooling | WARN()<br>BazelQuery<br>BazelQueryRunner<br>Perform a Bazel query and return the resulting targets.<br>A collection of functions useful for constructing Bazel queries. | 108 |
| 15 | 111 | 0.02 | medium 100-499 | Mixed/uncategorized | Creates the launcher instance. Note that the launcher instance for AL<br>Launcher<br>ErrorMessage<br>Launcher<br>LauncherBusy | 103 |
| 18 | 82 | 0.03 | small 10-99 | RISC-V/OTBN/ISS tooling | BadAtEnd<br>A snippet generator that generates a loop/branch/jump at end of a loop Th<br>BadBranch<br>A snippet generator that generates program ending branch instructions. Th<br>BadGiantLoop | 74 |
| 19 | 75 | 0.03 | small 10-99 | KG platform services | BusInterfaces<br>_if_dict()<br>Look up the given host/name pair and return its port name. Raises a K<br>CdcCfg<br>Derivative class for linting purposes. | 67 |
| 22 | 70 | 0.05 | small 10-99 | RISC-V/OTBN/ISS tooling | device_log_bypass_uart_address()<br>device_test_status_address()<br>rv_core_ibex_base()<br>check_crc32()<br>main() | 62 |
| 23 | 68 | 0.08 | small 10-99 | Mixed/uncategorized | addM()<br>copyConditional()<br>copy_conditional()<br>felem_assign()<br>felem_diff() | 60 |
| 24 | 58 | 0.07 | small 10-99 | OpenTitan firmware and crypto | dif_spi_host_transaction()<br>ConfigTest<br>ErrorEnableRegTest<br>ErrorStatusTest<br>EventEnableRegTest | 50 |
| 20 | 53 | 0.03 | small 10-99 | KG platform services | main()<br>process_file_data()<br>Print information about modules found in SystemVerilog file. This function<br>main()<br>process_file_data() | 45 |
| 21 | 48 | 0.03 | small 10-99 | Mixed/uncategorized | blake2_provider<br>G()<br>initH()<br>initX()<br>round() | 40 |
| 27 | 37 | 0.06 | small 10-99 | Mixed/uncategorized | main()<br>Oid<br>Tag<br>pmp_csr_1_gen_class()<br>set_addr_offset() | 29 |
| 26 | 35 | 0.11 | small 10-99 | Mixed/uncategorized | kill_child_processes()<br>bmc()<br>bmc_mode()<br>build_strategy_rec()<br>construct_strategy() | 27 |
| 25 | 31 | 0.05 | small 10-99 | Mixed/uncategorized | matmul()<br>matmul()<br>matmul()<br>matmul()<br>matmul() | 23 |
| 30 | 31 | 0.07 | small 10-99 | RISC-V/OTBN/ISS tooling | Prepare to start the execution. Use run() or step() to actually execu<br>Check the contents of the external registers after a successful run.<br>Test an invalid instruction is reflected in ERR_BITS.<br>test_ext_regs_err_bits_bad()<br>test_ext_regs_success() | 23 |
| 37 | 28 | 0.07 | small 10-99 | Mixed/uncategorized | BitbangEntryRequest<br>BitbangEntryResponse<br>DacBangEntryRequest<br>EmuRequest<br>EmuResponse | 20 |
| 38 | 27 | 0.07 | small 10-99 | Mixed/uncategorized | AutoOverrideConfigTest<br>AutoOverrideGetEnabledTest<br>AutoOverrideSetEnabledTest<br>InputChangeDetectConfigTest<br>InputChangeIrqClearCausesTest | 19 |
| 32 | 26 | 0.11 | small 10-99 | KG platform services | filter_tests_by_config()<br>GenError<br>get_compile_opts()<br>get_config()<br>get_isas_for_config() | 18 |
| 40 | 26 | 0.07 | small 10-99 | OpenTitan firmware and crypto | ClearRecoverableAlertsTest<br>ConditionerStartTest<br>ConditionerStopTest<br>ConfigTest<br>ConfigTestAllParams | 18 |
| 28 | 25 | 0.05 | small 10-99 | OpenTitan firmware and crypto | AesInitTest<br>AesTest<br>AesTestInitialized<br>AlertTest<br>CbcTest | 17 |
| 36 | 25 | 0.07 | small 10-99 | Mixed/uncategorized | Bus<br>CmdGetDeviceStatus<br>CmdPrepareReadData<br>CmdTransferLong<br>CmdTransferShort | 17 |
| 34 | 22 | 0.1 | small 10-99 | KG platform services | LLVMFuzzerTestOneInput()<br>RomMockGroup<br>AbstractBootstrapMockGroup()<br>ConfigureMocks()<br>Crash() | 14 |
| 43 | 21 | 0.17 | small 10-99 | Mixed/uncategorized | pmp_addr_csr_read()<br>pmp_addr_csr_write()<br>pmp_address_aligned()<br>pmp_cfg_csr_read()<br>pmp_cfg_csr_write() | 13 |
| 44 | 21 | 0.21 | small 10-99 | Mixed/uncategorized | c_dpi_prince_decrypt()<br>c_dpi_prince_encrypt()<br>bytes_to_uint64()<br>gf2_mat_mult16_1()<br>prince_core() | 13 |
| 50 | 20 | 0.09 | small 10-99 | OpenTitan firmware and crypto | AbortTest<br>ConfigureTest<br>DmaTest<br>DmaTestInitialized<br>ErrorTest | 12 |
| 46 | 19 | 0.08 | small 10-99 | Mixed/uncategorized | AdvanceStateTest<br>AdvanceToNonOperational<br>AdvanceToOperational<br>BadArgsTwo<br>ConfigureTest | 11 |
| 45 | 18 | 0.12 | small 10-99 | Mixed/uncategorized | check_regs()<br>format_block()<br>is_wdr()<br>Line<br>main() | 10 |
| 48 | 18 | 0.09 | small 10-99 | Database/device metadata tooling | KeymgrBindingValue<br>LifecycleDeviceId<br>Manifest<br>ManifestExtHeader<br>ManifestExtImageType | 10 |
| 55 | 18 | 0.11 | small 10-99 | Mixed/uncategorized | AttributeType<br>BasicConstraints<br>Certificate<br>CertificateExtension<br>Conversion | 10 |
| 52 | 17 | 0.1 | small 10-99 | OpenTitan firmware and crypto | AlertInfoDumpReadTest<br>AlertInfoGetSizeTest<br>AlertInfoGetTest<br>AlertInfoSetTest<br>CpuInfoDumpReadTest | 9 |
| 57 | 17 | 0.11 | small 10-99 | Mixed/uncategorized | AdcCtrlTest<br>ConfigTest<br>FilterConfigTest<br>FilterMatchWakeupGetEnabledTest<br>FilterMatchWakeupSetEnabledTest | 9 |
| 49 | 16 | 0.11 | small 10-99 | KG platform services | Bootstrap<br>BootstrapError<br>BootstrapOptions<br>BootstrapProtocol<br>Capabilities | 8 |
| 58 | 15 | 0.2 | small 10-99 | EDA, regression, and config tooling | all_paths_must_exist()<br>Config<br>DConfig<br>DirectedTestsYaml<br>DTest | 7 |
| 61 | 15 | 0.12 | small 10-99 | Mixed/uncategorized | BytesReceivePolledTest<br>BytesReceiveTest<br>BytesSendPolledTest<br>BytesSendTest<br>ConfigTest | 7 |
| 33 | 14 | 0.07 | small 10-99 | OpenTitan firmware and crypto | Mark particular reset as requiring shadow<br>Get available domains for a reset<br>Get generated resets and return reset object<br>Get resets pushed to the top level<br>Get software controlled resets | 6 |
| 47 | 14 | 0.08 | small 10-99 | OpenTitan firmware and crypto | AbsorbalignmentMessage<br>ConfigLock<br>Cshake256Test<br>Kmac256Test<br>KmacConfigureTest | 6 |
| 59 | 14 | 0.12 | small 10-99 | Mixed/uncategorized | BitbangEntry<br>ClockNature<br>DacBangEntry<br>Edge<br>GpioBitbanging | 6 |
| 65 | 14 | 0.13 | small 10-99 | OpenTitan firmware and crypto | AlertCauseTest<br>AlertConfigTest<br>AlertHandlerTest<br>AlertLockTest<br>ClassConfigTest | 6 |
| 54 | 13 | 0.15 | small 10-99 | EDA, regression, and config tooling | test_read_version_file()<br>test_read_version_file_empty()<br>test_read_version_file_invalid_hex()<br>test_write_source_file()<br>TestFileOperations | 5 |
| 70 | 13 | 0.14 | small 10-99 | Mixed/uncategorized | AonTimerTest<br>WakeupGetCountTest<br>WakeupRestartTest<br>WakeupStartTest<br>WakeupStatusTest | 5 |
| 71 | 13 | 0.14 | small 10-99 | Mixed/uncategorized | BlockingIoTest<br>CheckTest<br>ConfigTest<br>DaiDigestTest<br>DaiProgramTest | 5 |
| 39 | 12 | 0.14 | small 10-99 | KG platform services | main()<br># TODO: struct assignment labels within concatenation<br>LintParser<br>LintParser<br>Extract messages from the string buffer log_content. The argument pat | 4 |
| 51 | 12 | 0.1 | small 10-99 | Mixed/uncategorized | EqTest<br>GeqTest<br>InsnInformationFlowTest<br>LeqTest<br>MultiTest | 4 |
| 63 | 12 | 0.14 | small 10-99 | OpenTitan firmware and crypto | AlertTestPeripheral<br>IrqTestPeripheral<br># TODO: We only know how to directly access irq test CSRs in this<br># TODO: Model alert domains with explicit connectivity<br># TODO: This is an implicit assignment of alerts to reg interfaces | 4 |
| 74 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 75 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 76 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 77 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 78 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 79 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 80 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 81 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 82 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 83 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 84 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 85 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 86 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 87 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 88 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 89 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 90 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 91 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 92 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 93 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 94 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 95 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 96 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 97 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 98 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 99 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 100 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 101 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 102 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 103 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 104 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 105 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 106 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 107 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 108 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 109 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 110 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 111 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 112 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 113 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 114 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 115 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 116 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 117 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 118 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 119 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 120 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 121 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 122 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 123 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 124 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 125 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 126 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 127 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 128 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 129 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 130 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 131 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 132 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 133 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 134 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 135 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 136 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 137 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 138 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 139 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 140 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 141 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 142 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 143 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 144 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 145 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 146 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 147 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 148 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 149 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 150 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 151 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 152 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 153 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 154 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 155 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 156 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 157 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 158 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 159 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 160 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 161 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 162 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 163 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 164 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 165 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 166 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 167 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 168 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 169 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 170 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 171 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 172 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 173 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 174 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 175 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 176 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 177 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 178 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 179 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 180 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 181 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 182 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 183 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 184 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 185 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 186 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 187 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 188 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 189 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 190 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 191 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 192 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 193 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 194 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 195 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 196 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 197 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 198 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 199 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 200 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 201 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 202 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 203 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 204 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 205 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 206 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 207 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 208 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 209 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 210 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 211 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 212 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 213 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 214 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 215 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 216 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 217 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 218 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 219 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 220 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 221 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 222 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 223 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 224 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 225 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 226 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 227 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 228 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 229 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 230 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 231 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 232 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 233 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 234 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 235 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 236 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 237 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 238 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 239 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 240 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 241 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 242 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 243 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 244 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 245 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 246 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 247 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 248 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 249 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 250 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 251 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 252 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 253 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 254 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 255 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 256 | 12 | 0.28 | small 10-99 | Mixed/uncategorized | checkTestResult()<br>detect_pmp_granularity()<br>handle_trap()<br>main()<br>mismatch_addr_offset() | 4 |
| 261 | 12 | 0.15 | small 10-99 | KG platform services | ApiError<br>CloudResult<br>KmsCreateKey<br>KmsDigest<br>KmsKeyList | 4 |
| 262 | 12 | 0.23 | small 10-99 | Mixed/uncategorized | get_header_snippet()<br>is_declaration()<br>is_enum()<br>is_func()<br>is_struct() | 4 |
| 42 | 11 | 0.1 | small 10-99 | OpenTitan firmware and crypto | AlertClass<br>AlertClassConfig<br>AlertClassRegs<br>AlertEnable<br>AlertEscalate | 3 |
| 67 | 11 | 0.26 | small 10-99 | Mixed/uncategorized | _xex_scramble()<br>main()<br>multiply()<br>prince()<br>prince_fwd_round() | 3 |
| 264 | 11 | 0.39 | small 10-99 | Mixed/uncategorized | list_clear()<br>list_getSize()<br>list_init()<br>list_pop()<br>list_push() | 3 |
| 265 | 11 | 0.17 | small 10-99 | Mixed/uncategorized | ClkMgrTest<br>ExternalClkRegwenTest<br>ExternalClkTest<br>FatalErrorTest<br>GateableClockTest | 3 |
| 266 | 11 | 0.17 | small 10-99 | Mixed/uncategorized | ControlSoftwareErrorsFatalTest<br>DmemReadTest<br>DmemWriteTest<br>GetErrBitsTest<br>GetInsnCntTest | 3 |
| 268 | 11 | 0.17 | small 10-99 | Mixed/uncategorized | ConfigurationFile<br>I2cConfiguration<br>IoExpander<br>IoExpanderDriver<br>IoExpanderPin | 3 |
| 53 | 10 | 0.1 | small 10-99 | Mixed/uncategorized | OperandType<br>Convert the operand value to an encoded value This expects a current<br>Convert the encoded value to an operand value This needs the current<br>Render an operand value as a string<br>Return the range of valid encoded values for this operand type The de | 2 |
| 66 | 10 | 0.13 | small 10-99 | Mixed/uncategorized | AssertChipSelect<br>ClockPhase<br>ClockPolarity<br>MaxSizes<br>SpiError | 2 |
| 68 | 10 | 0.2 | small 10-99 | Mixed/uncategorized | build_target()<br>get_rule_deps_of_kind()<br>get_target_files_with_ext()<br>Escape the Bazel sandbox if necessary. Without this step<br>other functions | 2 |
| 72 | 10 | 0.21 | small 10-99 | KG platform services | status_report()<br>test_main()<br>test_main()<br>status_report_unittest_c()<br>sudo_god() | 2 |
| 267 | 10 | 0.17 | small 10-99 | OpenTitan firmware and crypto | AddressTranslationTest<br>ErrorStatusTest<br>FatalErrorAlertTest<br>FpgaInfoTest<br>NMITest | 2 |
| 272 | 10 | 0.18 | small 10-99 | OpenTitan firmware and crypto | AlertTest<br>CommandTest<br>ConfigTest<br>DifEdnTest<br>ErrorTest | 2 |
| 60 | 9 | 0.12 | tiny 3-9 | Mixed/uncategorized | CmdChipSelect<br>CmdEepromTransferStart<br>CmdTransferContinue<br>CmdTransferStart<br>RspChipSelect | 1 |
| 62 | 9 | 0.15 | tiny 3-9 | Mixed/uncategorized | template_asn1_integer()<br>template_asn1_integer_impl()<br>template_asn1_uint32()<br>template_patch_size_be()<br>template_patch_size_be_impl() | 1 |
| 274 | 9 | 0.31 | tiny 3-9 | Mixed/uncategorized | gpio_base_addr()<br>gpio_masked_bit_write()<br>gpio_read()<br>gpio_set_output_mode()<br>gpio_write() | 1 |
| 275 | 9 | 0.36 | tiny 3-9 | Mixed/uncategorized | checkTestResult()<br>handle_trap()<br>main()<br>set_cfg()<br>switch_mode_access() | 1 |
| 276 | 9 | 0.36 | tiny 3-9 | Mixed/uncategorized | checkTestResult()<br>handle_trap()<br>main()<br>set_cfg()<br>switch_mode_access() | 1 |
| 277 | 9 | 0.36 | tiny 3-9 | Mixed/uncategorized | checkTestResult()<br>handle_trap()<br>main()<br>set_cfg()<br>switch_mode_access() | 1 |
| 278 | 9 | 0.36 | tiny 3-9 | Mixed/uncategorized | checkTestResult()<br>handle_trap()<br>main()<br>set_cfg()<br>switch_mode_access() | 1 |
| 279 | 9 | 0.36 | tiny 3-9 | Mixed/uncategorized | checkTestResult()<br>handle_trap()<br>main()<br>set_cfg()<br>switch_mode_access() | 1 |
| 280 | 9 | 0.36 | tiny 3-9 | Mixed/uncategorized | checkTestResult()<br>handle_trap()<br>main()<br>set_cfg()<br>switch_mode_access() | 1 |
| 281 | 9 | 0.36 | tiny 3-9 | Mixed/uncategorized | checkTestResult()<br>handle_trap()<br>main()<br>set_cfg()<br>switch_mode_access() | 1 |
| 282 | 9 | 0.36 | tiny 3-9 | Mixed/uncategorized | checkTestResult()<br>handle_trap()<br>main()<br>set_cfg()<br>switch_mode_access() | 1 |
| 283 | 9 | 0.36 | tiny 3-9 | Mixed/uncategorized | checkTestResult()<br>handle_trap()<br>main()<br>set_cfg()<br>switch_mode_access() | 1 |
| 284 | 9 | 0.36 | tiny 3-9 | Mixed/uncategorized | checkTestResult()<br>handle_trap()<br>main()<br>set_cfg()<br>switch_mode_access() | 1 |
| 285 | 9 | 0.2 | tiny 3-9 | Mixed/uncategorized | ConfigChannelTest<br>ConfigTest<br>PhaseCntrGetEnabledTest<br>PhaseCntrSetEnabledTest<br>PwmChannelGetEnabledTest | 1 |
| 287 | 9 | 0.47 | tiny 3-9 | Mixed/uncategorized | async_incomplete_test()<br>bad_args_test()<br>bad_test()<br>fatal_err_test()<br>good_test() | 1 |
| 35 | 8 | 0.06 | tiny 3-9 | OpenTitan firmware and crypto | Aes<br>Commands<br>Ecdsa<br>Kdf<br>Mldsa | 0 |
| 56 | 8 | 0.11 | tiny 3-9 | KG platform services | Service<br>NewConnectivityRepository()<br>connectivityRepo<br>moduleRepo<br>versionRepo | 0 |
| 291 | 8 | 0.44 | tiny 3-9 | Mixed/uncategorized | crc32()<br>crc32_add()<br>crc32_add32()<br>crc32_add8()<br>crc32_finish() | 0 |
| 31 | 7 | 0.05 | tiny 3-9 | Mixed/uncategorized | Annotation<br>Error<br>Field<br>FieldType<br>LenUnit | 0 |
| 69 | 7 | 0.18 | tiny 3-9 | RISC-V/OTBN/ISS tooling | ConstantContext<br>empty()<br>Represents known-constant GPRs. This datatype is used to track and evalua<br>Set the value of a GPR in the context.<br>Get the value of a GPR in the context. | 0 |
| 73 | 7 | 0.24 | tiny 3-9 | Mixed/uncategorized | DriveReset()<br>OnFinal()<br>OnInitial()<br>ResetDriver()<br>rst_deregister_intf() | 0 |
| 257 | 7 | 0.22 | tiny 3-9 | Mixed/uncategorized | closetrace()<br>reset()<br>tick()<br>main()<br>main() | 0 |
| 263 | 7 | 0.22 | tiny 3-9 | Mixed/uncategorized | main()<br>Insert the value of the item if it does not exist. Args: i<br>Get the value of the item if it exists. Args: item_name: T<br>Update the JSON with the ROM_EXT immutable section data. Args:<br>Checks if immutable ROM extension is enabled. This method retrieves t | 0 |
| 293 | 7 | 0.22 | tiny 3-9 | Mixed/uncategorized | GoodbyeCommand<br>GoodbyeMessage<br>Greetings<br>HelloMessage<br>HelloPeople | 0 |
| 41 | 6 | 0.1 | tiny 3-9 | Mixed/uncategorized | FlowControl<br>Rc<T><br>&T<br>Uart<br>UartError | 0 |
| 298 | 6 | 0.32 | tiny 3-9 | OpenTitan firmware and crypto | Hwre<br>Register opentitan specific UDPs (User Defined Properties)<br>register_udps()<br>Shadowed<br>UDPBoolean | 0 |
| 299 | 6 | 0.43 | tiny 3-9 | RISC-V/OTBN/ISS tooling | doc_tbl_head()<br>doc_tbl_line()<br>document()<br>genout()<br>generate_selfdocs() | 0 |
| 303 | 6 | 0.29 | tiny 3-9 | Mixed/uncategorized | ChipWhisperer<br>ChipWhispererBackend<br>ChipWhispererOpts<br>GetSam3xFwVersion<br>ResetSam3x | 0 |
| 259 | 5 | 0.18 | tiny 3-9 | Mixed/uncategorized | _ot_builtin_ashift_i64()<br>_ot_builtin_lshift_i64()<br>_ot_builtin_rshift_i64()<br>ShiftTest<br>TEST_P() | 0 |
| 271 | 5 | 0.22 | tiny 3-9 | Mixed/uncategorized | Cache<br>CacheEntry<br>Represents a single entry in a cache. The entry must hold two pieces of i<br>Returns whether this entry is a match for the key. In the simplest ca<br>Represents a cache to speed up recursive functions. The cache is structur | 0 |
| 273 | 5 | 0.18 | tiny 3-9 | OpenTitan firmware and crypto | HmacGetMessageLengthTest<br>HmacMacTest<br>HmacProcessTest<br>HmacSha256Test<br>HmacTest | 0 |
| 290 | 5 | 0.2 | tiny 3-9 | Mixed/uncategorized | An abstract class inherited by Register and MultiRegister This represents<br>Get the size of this register / these registers in bits See Field.get<br>Get an ordered list of the fields in the register(s) Registers are or<br>True if every field in the block is identical For a single register<br>RegBase | 0 |
| 292 | 5 | 0.22 | tiny 3-9 | Mixed/uncategorized | Decoder<br>DecodingState<br>Encoder<br>Sample<br>Symbol | 0 |
| 294 | 5 | 0.36 | tiny 3-9 | Mixed/uncategorized | crc32a()<br>reverse()<br>main()<br>rot13()<br>strlen() | 0 |
| 300 | 5 | 0.48 | tiny 3-9 | RISC-V/OTBN/ISS tooling | VMap<br>VMapWire<br>VMapWireGroup<br>WireExtractionInstruction<br>WireHierarchy | 0 |
| 307 | 5 | 0.33 | tiny 3-9 | Mixed/uncategorized | Dmi<br>DmiDebugger<br>DmiError<br>DmiHart<br>HartState | 0 |
| 313 | 5 | 0.33 | tiny 3-9 | KG platform services | Connectivity<br>Module<br>ModuleVersion<br>Port<br>SearchResult | 0 |
| 29 | 4 | 0.06 | tiny 3-9 | SystemVerilog DV/UVM packages | prim_ram_2p_pkg<br>spi_device_pkg<br>spi_device_reg_pkg<br>spid_common | 0 |
| 270 | 4 | 0.38 | tiny 3-9 | Parser/source text utilities | Construct a TokenPattern from the given `pattern`. Args: p<br>Process the given tokens and return all matches. Args: tok<br>RegisterTokenPattern<br>TestRegisterTokenPattern | 0 |
| 295 | 4 | 0.29 | tiny 3-9 | Mixed/uncategorized | BitRanges<br>from_list()<br>Represents the bit ranges used for a field in an encoding scheme<br>Encode the given value as bit fields | 0 |
| 309 | 4 | 0.33 | tiny 3-9 | Mixed/uncategorized | EraseMode<br>Error<br>ReadMode<br>ReadTypes | 0 |
| 310 | 4 | 0.33 | tiny 3-9 | Mixed/uncategorized | InternalUartCommand<br>UartCommand<br>UartOsDevice<br>UartOsDeviceResponse | 0 |
| 329 | 4 | 0.4 | tiny 3-9 | Mixed/uncategorized | Granularity<br>OtpCtrlReg<br>OtpParamMmap<br>Partition | 0 |
| 330 | 4 | 0.4 | tiny 3-9 | OpenTitan firmware and crypto | RstmgrAlertInfoCtrl<br>RstmgrCpuInfoCtrl<br>RstmgrCpuRegwen<br>RstmgrReg | 0 |
| 296 | 3 | 0.32 | tiny 3-9 | SystemVerilog DV/UVM packages | ast_bhv_pkg<br>ast_pkg<br>ast_reg_pkg | 0 |
| 297 | 3 | 0.25 | tiny 3-9 | Mixed/uncategorized | DecEncoded<br>DeferredValue<br>OctEncoded | 0 |
| 318 | 3 | 0.6 | tiny 3-9 | RISC-V/OTBN/ISS tooling | device_log_bypass_uart_address()<br>device_test_status_address()<br>rv_core_ibex_base() | 0 |
| 320 | 3 | 0.6 | tiny 3-9 | RISC-V/OTBN/ISS tooling | hardened_memshred_random_word()<br>ibex_rnd32_read()<br>random_order_random_word() | 0 |
| 326 | 3 | 0.5 | tiny 3-9 | Mixed/uncategorized | Key<br>List<br>ListResult | 0 |
| 327 | 3 | 0.4 | tiny 3-9 | Mixed/uncategorized | EmuError<br>Emulator<br>EmuState | 0 |
| 328 | 3 | 0.4 | tiny 3-9 | Mixed/uncategorized | SerializableError<br>SerializableErrorRegistration<br>SerializedError | 0 |
| 333 | 3 | 0.83 | tiny 3-9 | Mixed/uncategorized | ebreak()<br>fib()<br>main() | 0 |
| 334 | 3 | 0.5 | tiny 3-9 | Mixed/uncategorized | E51<br>HiFiveUnleashedFlash<br>U54 | 0 |
| 335 | 3 | 0.5 | tiny 3-9 | Mixed/uncategorized | E51<br>HiFiveUnleashed<br>U54 | 0 |
| 343 | 3 | 0.5 | tiny 3-9 | OpenTitan firmware and crypto | KeyEntry<br>KeyInfo<br>SpxInterface | 0 |
| 344 | 3 | 0.5 | tiny 3-9 | Mixed/uncategorized | Broadcaster<br>BroadcasterInner<br>WeakBroadcaster | 0 |
| 345 | 3 | 0.5 | tiny 3-9 | Mixed/uncategorized | Decoder<br>PwmPeriod<br>Sample | 0 |
| 346 | 3 | 0.5 | tiny 3-9 | Mixed/uncategorized | Board<br>Cw310<br>Cw340 | 0 |
| 347 | 3 | 0.5 | tiny 3-9 | Mixed/uncategorized | Inner<br>Watch<br>WatchResponse | 0 |
| 350 | 3 | 0.5 | tiny 3-9 | KG platform services | ConnectivityRepository<br>ModuleRepository<br>VersionRepository | 0 |
| 288 | 2 | 0.47 | thin <=2 | Thin/noise candidate | Decoder<SDA<br>SCL><br>Sample<SDA<br>SCL> | 0 |
| 305 | 2 | 0.33 | thin <=2 | Thin/noise candidate | pattgen_ctrl_pkg<br>pattgen_reg_pkg | 0 |
| 308 | 2 | 0.4 | thin <=2 | Thin/noise candidate | std::rc::Rc<T><br>&T | 0 |
| 312 | 2 | 0.4 | thin <=2 | Thin/noise candidate | Assert-PathExists()<br>Invoke-PythonScript() | 0 |
| 316 | 2 | 0.4 | thin <=2 | Thin/noise candidate | soc_proxy_pkg<br>soc_proxy_reg_pkg | 0 |
| 317 | 2 | 0.6 | thin <=2 | Thin/noise candidate | rv_core_ibex_peri_pkg<br>rv_core_ibex_peri_reg_pkg | 0 |
| 319 | 2 | 0.5 | thin <=2 | Thin/noise candidate | device_test_status_address()<br>rv_core_ibex_base() | 0 |
| 332 | 2 | 0.4 | thin <=2 | Thin/noise candidate | moore<br>moore_parse | 0 |
| 348 | 2 | 0.5 | thin <=2 | Thin/noise candidate | ImmutableSectionProcessor<br>Update the creator's manufacturing state with the immutable ROM_EXT hash. | 0 |
| 349 | 2 | 0.5 | thin <=2 | Thin/noise candidate | Slang<br>Slang_parse | 0 |
| 359 | 2 | 0.67 | thin <=2 | Thin/noise candidate | HiFive1Flash<br>HiFive1FlashHart | 0 |
| 360 | 2 | 0.67 | thin <=2 | Thin/noise candidate | HiFive1<br>HiFive1Hart | 0 |
| 361 | 2 | 0.67 | thin <=2 | Thin/noise candidate | E300<br>E300Hart | 0 |
| 362 | 2 | 0.67 | thin <=2 | Thin/noise candidate | U500<br>U500Hart | 0 |
| 372 | 2 | 0.67 | thin <=2 | Thin/noise candidate | ConsoleDevice<br>ConsoleError | 0 |
| 373 | 2 | 0.67 | thin <=2 | Thin/noise candidate | Buffered<br>Inner | 0 |
| 375 | 2 | 0.67 | thin <=2 | Thin/noise candidate | TransportError<br>TransportInterfaceType | 0 |
| 376 | 2 | 0.67 | thin <=2 | Thin/noise candidate | ClkmgrExtclkCtrl<br>ClkmgrReg | 0 |
| 377 | 2 | 0.67 | thin <=2 | Thin/noise candidate | Chip<br>Ft4232hq | 0 |
| 378 | 2 | 0.67 | thin <=2 | Thin/noise candidate | DecodeKey<br>EncodeKey | 0 |
| 379 | 2 | 0.67 | thin <=2 | Thin/noise candidate | stimulus_gen<br>tb | 0 |
| 380 | 2 | 0.67 | thin <=2 | Thin/noise candidate | stimulus_gen<br>tb | 0 |
| 381 | 2 | 0.67 | thin <=2 | Thin/noise candidate | stimulus_gen<br>tb | 0 |
| 382 | 2 | 0.67 | thin <=2 | Thin/noise candidate | stimulus_gen<br>tb | 0 |
| 383 | 2 | 0.67 | thin <=2 | Thin/noise candidate | stimulus_gen<br>tb | 0 |
| 384 | 2 | 0.67 | thin <=2 | Thin/noise candidate | stimulus_gen<br>tb | 0 |
| 64 | 1 | 0.22 | thin <=2 | Thin/noise candidate | MMGen | 0 |
| 258 | 1 | 0.15 | thin <=2 | Thin/noise candidate | rv_plic_reg_pkg | 0 |
| 286 | 1 | 0.2 | thin <=2 | Thin/noise candidate | EarlGrey | 0 |
| 289 | 1 | 0.2 | thin <=2 | Thin/noise candidate | TpmStatus | 0 |
| 304 | 1 | 0.33 | thin <=2 | Thin/noise candidate | sha1_provider | 0 |
| 306 | 1 | 0.33 | thin <=2 | Thin/noise candidate | ownership_key_validate() | 0 |
| 311 | 1 | 0.33 | thin <=2 | Thin/noise candidate | rstmgr_reset() | 0 |
| 314 | 1 | 0.4 | thin <=2 | Thin/noise candidate | prim_trivium_pkg | 0 |
| 315 | 1 | 0.4 | thin <=2 | Thin/noise candidate | usb_consts_pkg | 0 |
| 322 | 1 | 0.4 | thin <=2 | Thin/noise candidate | otp_read() | 0 |
| 324 | 1 | 0.4 | thin <=2 | Thin/noise candidate | Sign | 0 |
| 325 | 1 | 0.4 | thin <=2 | Thin/noise candidate | Verify | 0 |
| 331 | 1 | 0.7 | thin <=2 | Thin/noise candidate | OwnerConfigKind | 0 |
| 336 | 1 | 0.5 | thin <=2 | Thin/noise candidate | aon_timer_reg_pkg | 0 |
| 337 | 1 | 0.5 | thin <=2 | Thin/noise candidate | uart_reg_pkg | 0 |
| 342 | 1 | 0.5 | thin <=2 | Thin/noise candidate | test_main() | 0 |
| 351 | 1 | 0.67 | thin <=2 | Thin/noise candidate | Cosim() | 0 |
| 352 | 1 | 0.67 | thin <=2 | Thin/noise candidate | PRIVATE_NAMESPACE_BEGIN() | 0 |
| 353 | 1 | 0.67 | thin <=2 | Thin/noise candidate | get_unix_timestamp() | 0 |
| 354 | 1 | 0.67 | thin <=2 | Thin/noise candidate | ibex_tracer_pkg | 0 |
| 355 | 1 | 0.67 | thin <=2 | Thin/noise candidate | entropy_subsys_fifo_exception_pkg | 0 |
| 356 | 1 | 0.67 | thin <=2 | Thin/noise candidate | SimCtrlExtension() | 0 |
| 357 | 1 | 0.67 | thin <=2 | Thin/noise candidate | crypto_dpi_present_pkg | 0 |
| 358 | 1 | 0.67 | thin <=2 | Thin/noise candidate | prim_count_pkg | 0 |
| 363 | 1 | 0.67 | thin <=2 | Thin/noise candidate | rv_timer_reg_pkg | 0 |
| 364 | 1 | 0.67 | thin <=2 | Thin/noise candidate | alert_handler_reg_pkg | 0 |
| 365 | 1 | 0.67 | thin <=2 | Thin/noise candidate | dt_clock_frequency() | 0 |
| 366 | 1 | 0.67 | thin <=2 | Thin/noise candidate | pwm_reg_pkg | 0 |
| 367 | 1 | 0.67 | thin <=2 | Thin/noise candidate | dm | 0 |
| 374 | 1 | 0.67 | thin <=2 | Thin/noise candidate | Bit | 0 |
| 426 | 1 | 1 | thin <=2 | Thin/noise candidate | sw_test_status_pkg | 0 |
| 427 | 1 | 1 | thin <=2 | Thin/noise candidate | entropy_src_ack_sm_pkg | 0 |
| 428 | 1 | 1 | thin <=2 | Thin/noise candidate | blake2_mixin | 0 |
| 429 | 1 | 1 | thin <=2 | Thin/noise candidate | blake_mixin | 0 |
| 430 | 1 | 1 | thin <=2 | Thin/noise candidate | cshake_mixin | 0 |
| 431 | 1 | 1 | thin <=2 | Thin/noise candidate | k12m14_mixin | 0 |
| 432 | 1 | 1 | thin <=2 | Thin/noise candidate | kmac_mixin | 0 |
| 433 | 1 | 1 | thin <=2 | Thin/noise candidate | skein_mixin | 0 |
| 442 | 1 | 1 | thin <=2 | Thin/noise candidate | dm_tb_pkg | 0 |
| 479 | 1 | 1 | thin <=2 | Thin/noise candidate | HsmError | 0 |
| 480 | 1 | 1 | thin <=2 | Thin/noise candidate | KeyEncoding | 0 |
| 481 | 1 | 1 | thin <=2 | Thin/noise candidate | CommandDispatch | 0 |
| 482 | 1 | 1 | thin <=2 | Thin/noise candidate | ChipDataError | 0 |
| 483 | 1 | 1 | thin <=2 | Thin/noise candidate | SpiConsoleDevice | 0 |
| 484 | 1 | 1 | thin <=2 | Thin/noise candidate | ManifestExtTable | 0 |
| 485 | 1 | 1 | thin <=2 | Thin/noise candidate | IoExpander | 0 |
| 486 | 1 | 1 | thin <=2 | Thin/noise candidate | SoftwareFlowControl | 0 |
| 487 | 1 | 1 | thin <=2 | Thin/noise candidate | u8 | 0 |
| 488 | 1 | 1 | thin <=2 | Thin/noise candidate | RawTty | 0 |
| 490 | 1 | 1 | thin <=2 | Thin/noise candidate | anyhow::Error | 0 |
| 491 | 1 | 1 | thin <=2 | Thin/noise candidate | FpgaCommand | 0 |
| 492 | 1 | 1 | thin <=2 | Thin/noise candidate | CertFormat | 0 |
| 493 | 1 | 1 | thin <=2 | Thin/noise candidate | HashAlgorithm | 0 |
| 494 | 1 | 1 | thin <=2 | Thin/noise candidate | EcCurve | 0 |
| 495 | 1 | 1 | thin <=2 | Thin/noise candidate | AonTimerReg | 0 |
| 496 | 1 | 1 | thin <=2 | Thin/noise candidate | UartReg | 0 |
| 497 | 1 | 1 | thin <=2 | Thin/noise candidate | UjsonPayloads | 0 |
| 498 | 1 | 1 | thin <=2 | Thin/noise candidate | SpxError | 0 |
| 499 | 1 | 1 | thin <=2 | Thin/noise candidate | Value<T> | 0 |
| 502 | 1 | 1 | thin <=2 | Thin/noise candidate | test_pkg | 0 |
| 503 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 504 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 505 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 506 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 507 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 508 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 509 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 510 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 511 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 512 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 513 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 514 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 515 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 516 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 517 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 518 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 519 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 520 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 521 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 522 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 523 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 524 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 525 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 526 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 527 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 528 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 529 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 530 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 531 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 532 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 533 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 534 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 535 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 536 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 537 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 538 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 539 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 540 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 541 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 542 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 543 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 544 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 545 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 546 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 547 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 548 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 549 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 550 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 551 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 552 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 553 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 554 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 555 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 556 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 557 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 558 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 559 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 560 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 561 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 562 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 563 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 564 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 565 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 566 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 567 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 568 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 569 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 570 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 571 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 572 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 573 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 574 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 575 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 576 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 577 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 578 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 579 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 580 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 581 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 582 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 583 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 584 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 585 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 586 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 587 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 588 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 589 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 590 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 591 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 592 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 593 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 594 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 595 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 596 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 597 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 598 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 599 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 600 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 601 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 602 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 603 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 604 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 605 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 606 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 607 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 608 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 609 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 610 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 611 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 612 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 613 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 614 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 615 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 616 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 617 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 618 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 619 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 620 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 621 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 622 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 623 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 624 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 625 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 626 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 627 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 628 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 629 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 630 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 631 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 632 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 633 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 634 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 635 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 636 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 637 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 638 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 639 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 640 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 641 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 642 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 643 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 644 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 645 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 646 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 647 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 648 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 649 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 650 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 651 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 652 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 653 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 654 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 655 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 656 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 657 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 658 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 659 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 660 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 661 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 662 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 663 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 664 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 665 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 666 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 667 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 668 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 669 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 670 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 671 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 672 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 673 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 674 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 675 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 676 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 677 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 678 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 679 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 680 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 681 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 682 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 683 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 684 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 685 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 686 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 687 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 688 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 689 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 690 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 691 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 692 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 693 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 694 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 695 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 696 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 697 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 698 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 699 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 700 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 701 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 702 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 703 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 704 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 705 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 706 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 707 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 708 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 709 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 710 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 711 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 712 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 713 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 714 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 715 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 716 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 717 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 718 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 719 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 720 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 721 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 722 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 723 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 724 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 725 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 726 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 727 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 728 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 729 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 730 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 731 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 732 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 733 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 734 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 735 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 736 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 737 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 738 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 739 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 740 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 741 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 742 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 743 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 744 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 745 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 746 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 747 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 748 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 749 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 750 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 751 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 752 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 753 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 754 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 755 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 756 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 757 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 758 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 759 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 760 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 761 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 762 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 763 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 764 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 765 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 766 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 767 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 768 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 769 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 770 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 771 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 772 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 773 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 774 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 775 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 776 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 777 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 778 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 779 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 780 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 781 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 782 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 783 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 784 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 785 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 786 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 787 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 788 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 789 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 790 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 791 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 792 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 793 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 794 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 795 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 796 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 797 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 798 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 799 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 800 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 801 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 802 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 803 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 804 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 805 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 806 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 807 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 808 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 809 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 810 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 811 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 812 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 813 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 814 | 1 | 1 | thin <=2 | Thin/noise candidate | RefModule | 0 |
| 873 | 1 | 1 | thin <=2 | Thin/noise candidate | Check that the yaml file exists on disk. This field needs its own val | 0 |
| 874 | 1 | 1 | thin <=2 | Thin/noise candidate | A test may only specify common configs in the available list. | 0 |
| 875 | 1 | 1 | thin <=2 | Thin/noise candidate | Check that all fields specifying files exist on disk. We need to chec | 0 |
| 876 | 1 | 1 | thin <=2 | Thin/noise candidate | Allow easy construction of the data-structure from a file. | 0 |
| 877 | 1 | 1 | thin <=2 | Thin/noise candidate | Write the object to disk. Simultaneously write a pickle file and a ya | 0 |
| 878 | 1 | 1 | thin <=2 | Thin/noise candidate | Construct metadata object from exported object using default filenames. | 0 |
| 1273 | 1 | 1 | thin <=2 | Thin/noise candidate | Byte offset of node's first character in source text | 0 |
| 1274 | 1 | 1 | thin <=2 | Thin/noise candidate | Byte offset of a character just past the node in source text. | 0 |
| 1275 | 1 | 1 | thin <=2 | Thin/noise candidate | Source code fragment spanning all tokens in a node. | 0 |
| 1276 | 1 | 1 | thin <=2 | Thin/noise candidate | Byte offset of token's first character in source text | 0 |
| 1277 | 1 | 1 | thin <=2 | Thin/noise candidate | Byte offset of a character just past the token in source text. | 0 |
| 1278 | 1 | 1 | thin <=2 | Thin/noise candidate | Token text in source code. | 0 |
| 1311 | 1 | 1 | thin <=2 | Thin/noise candidate | Activate a python virtualenv if available. The env variable <PROJECT> | 0 |
| 1312 | 1 | 1 | thin <=2 | Thin/noise candidate | Prepare the workspace based on the chosen launcher's needs. This is d | 0 |
| 1313 | 1 | 1 | thin <=2 | Thin/noise candidate | Prepare the workspace for a cfg. This is invoked once for each cfg. | 0 |
| 1314 | 1 | 1 | thin <=2 | Thin/noise candidate | Create modes of type ModeType from a given list of raw dicts Process de | 0 |
| 1315 | 1 | 1 | thin <=2 | Thin/noise candidate | Returns true if the severity is known | 0 |
| 1316 | 1 | 1 | thin <=2 | Thin/noise candidate | Parses an input file with HJson and returns a dict. | 0 |
| 1317 | 1 | 1 | thin <=2 | Thin/noise candidate | Creates testplan elements from the list of raw dicts. kind is either | 0 |
| 1318 | 1 | 1 | thin <=2 | Thin/noise candidate | Returns a string representing percentage upto 2 decimal places. | 0 |
| 1319 | 1 | 1 | thin <=2 | Thin/noise candidate | Returns text with HTML CSS style for a table. | 0 |
| 1320 | 1 | 1 | thin <=2 | Thin/noise candidate | Parse imported testplans with correctly set paths. Paths of the impor | 0 |
| 1347 | 1 | 1 | thin <=2 | Thin/noise candidate | Match targets in `input` defined by `rule`. | 0 |
| 1348 | 1 | 1 | thin <=2 | Thin/noise candidate | Match targets in `input` that are tagged with `tag`. | 0 |
| 1349 | 1 | 1 | thin <=2 | Thin/noise candidate | Build a regex to find the given tag in a list. The query `attr("tags" | 0 |
| 1829 | 1 | 1 | thin <=2 | Thin/noise candidate | Generate flags for the result of an operation. C is the value for the | 0 |
| 1830 | 1 | 1 | thin <=2 | Thin/noise candidate | Interpret the signed value as a 2's complement u32 | 0 |
| 1831 | 1 | 1 | thin <=2 | Thin/noise candidate | Map any unknown integer value to INVALID. | 0 |
| 1832 | 1 | 1 | thin <=2 | Thin/noise candidate | Map any unknown integer value to INVALID. | 0 |
| 1833 | 1 | 1 | thin <=2 | Thin/noise candidate | Map any unknown integer value to INVALID. | 0 |
| 1834 | 1 | 1 | thin <=2 | Thin/noise candidate | Returns the current counter value. | 0 |
| 1835 | 1 | 1 | thin <=2 | Thin/noise candidate | Render a hex value in the format expected by RTL tracing | 0 |
| 1836 | 1 | 1 | thin <=2 | Thin/noise candidate | Convert a little-endian integer (bit j = state[j]) to a register tuple | 0 |
| 1839 | 1 | 1 | thin <=2 | Thin/noise candidate | Read init_data as parsed from json | 0 |
| 1840 | 1 | 1 | thin <=2 | Thin/noise candidate | Generate some initialised data This will be inserted into the program | 0 |
| 1841 | 1 | 1 | thin <=2 | Thin/noise candidate | The inverse of to_json. where is a textual description of where we ar | 0 |
| 1842 | 1 | 1 | thin <=2 | Thin/noise candidate | Read an instruction address from a parsed json object | 0 |
| 1843 | 1 | 1 | thin <=2 | Thin/noise candidate | Read a non-negative value from a parsed json object | 0 |
| 1844 | 1 | 1 | thin <=2 | Thin/noise candidate | The inverse of to_json | 0 |
| 1845 | 1 | 1 | thin <=2 | Thin/noise candidate | Merge a non-empty list of snippets as much as possible | 0 |
| 1846 | 1 | 1 | thin <=2 | Thin/noise candidate | Cons together one or two snippets | 0 |
| 1847 | 1 | 1 | thin <=2 | Thin/noise candidate | The inverse of to_json. | 0 |
| 1860 | 1 | 1 | thin <=2 | Thin/noise candidate | Extract a RegRef from state.gprs.get_reg(foo) Returns None if this is | 0 |
| 1862 | 1 | 1 | thin <=2 | Thin/noise candidate | Represents a context with no known constants. | 0 |
| 1863 | 1 | 1 | thin <=2 | Thin/noise candidate | Represents the graph for a path in which nothing is modified. For ins | 0 |
| 1864 | 1 | 1 | thin <=2 | Thin/noise candidate | Represents the graph for a nonexistent path. There is an important di | 0 |
| 1865 | 1 | 1 | thin <=2 | Thin/noise candidate | Turn X to . + X or . - X<br>as appropriate. | 0 |
| 1866 | 1 | 1 | thin <=2 | Thin/noise candidate | Smart constructor for a list of operands with "normal" syntax | 0 |
| 1867 | 1 | 1 | thin <=2 | Thin/noise candidate | Smart constructor that parses YAML syntax (see InsnSyntax) | 0 |
| 1868 | 1 | 1 | thin <=2 | Thin/noise candidate | Smart constructor for a list of operands with "normal" syntax | 0 |
| 1869 | 1 | 1 | thin <=2 | Thin/noise candidate | Parse the syntax in the YAML file | 0 |
| 1870 | 1 | 1 | thin <=2 | Thin/noise candidate | Parse a testcase HJSON string into a OtbnTestCase object. The HJSON s | 0 |
| 2150 | 1 | 1 | thin <=2 | Thin/noise candidate | Parse a line from a preprocessed vmem file Returns a pair (addr<br>word | 0 |
| 2151 | 1 | 1 | thin <=2 | Thin/noise candidate | Load a pre-processed file | 0 |
| 2152 | 1 | 1 | thin <=2 | Thin/noise candidate | Read a VMEM file This assumes that all words fit in the given width. | 0 |
| 2153 | 1 | 1 | thin <=2 | Thin/noise candidate | Read a little-endian 32-bit ELF file | 0 |
| 2811 | 1 | 1 | thin <=2 | Thin/noise candidate | Create a BitstreamCache with default parameters. | 0 |
| 3331 | 1 | 1 | thin <=2 | Thin/noise candidate | Convert a string from snake_case to StudlyCaps. Args: na | 0 |
| 3347 | 1 | 1 | thin <=2 | Thin/noise candidate | DfuError | 0 |
| 3399 | 1 | 1 | thin <=2 | Thin/noise candidate | Returns a string to create a table in the database. Args: | 0 |
| 3400 | 1 | 1 | thin <=2 | Thin/noise candidate | Creates a table in the database. Args: db: The database | 0 |
| 3401 | 1 | 1 | thin <=2 | Thin/noise candidate | Queries the database for the record. Args: db: The datab | 0 |
| 3402 | 1 | 1 | thin <=2 | Thin/noise candidate | Queries the database for all records. Args: db: The data | 0 |
| 3403 | 1 | 1 | thin <=2 | Thin/noise candidate | Creates a DeviceRecord object from a DUT object. Args: d | 0 |
| 3404 | 1 | 1 | thin <=2 | Thin/noise candidate | Creates a DeviceId object from a hex string. | 0 |
| 3405 | 1 | 1 | thin <=2 | Thin/noise candidate | Creates a DeviceId object from an int. | 0 |
| 3406 | 1 | 1 | thin <=2 | Thin/noise candidate | Creates a SKU configuration object from various subcomponent IDs. | 0 |
| 3454 | 1 | 1 | thin <=2 | Thin/noise candidate | Reading a properly-formatted version file produces the expected int. | 0 |
| 3455 | 1 | 1 | thin <=2 | Thin/noise candidate | Reading an empty version file raises an exception. | 0 |
| 3456 | 1 | 1 | thin <=2 | Thin/noise candidate | Reading an invalid version file raises an exception. | 0 |
| 3457 | 1 | 1 | thin <=2 | Thin/noise candidate | Calling write_source_file() produces the expected file. | 0 |
| 3459 | 1 | 1 | thin <=2 | Thin/noise candidate | Check that a path is valid for use in a mapping. This spots things li | 0 |
| 3460 | 1 | 1 | thin <=2 | Thin/noise candidate | Make a default mapping1<br>which copies everything straight through | 0 |
| 3469 | 1 | 1 | thin <=2 | Thin/noise candidate | Render the type definition. Example: "struct X {int field;};" | 0 |
| 3470 | 1 | 1 | thin <=2 | Thin/noise candidate | Render the declaration of a variable with this type and the name in arg | 0 |
| 3471 | 1 | 1 | thin <=2 | Thin/noise candidate | Render a value of this type. | 0 |
| 3472 | 1 | 1 | thin <=2 | Thin/noise candidate | This function must return an extension if it wants to modify the DT of | 0 |
| 3474 | 1 | 1 | thin <=2 | Thin/noise candidate | Create Test sets from a given list of raw dicts. Return a list of test | 0 |
| 3476 | 1 | 1 | thin <=2 | Thin/noise candidate | Runs git with `args`. Returns (returncode<br>stdout<br>stderr). | 0 |
| 3477 | 1 | 1 | thin <=2 | Thin/noise candidate | Like `_git()`<br>but doesn't capture stdout/stderr. | 0 |
| 3481 | 1 | 1 | thin <=2 | Thin/noise candidate | Produce a TemplateParams instance from an object as it is in Hjson. | 0 |
| 3482 | 1 | 1 | thin <=2 | Thin/noise candidate | Create an IpTemplate from a template directory. An IP template direct | 0 |
| 3483 | 1 | 1 | thin <=2 | Thin/noise candidate | Check that obj is a Hjson-serializable object. If not<br>raise a ValueE | 0 |
| 3484 | 1 | 1 | thin <=2 | Thin/noise candidate | Check if parameter values are valid. Returns the parameter values in | 0 |
| 3485 | 1 | 1 | thin <=2 | Thin/noise candidate | Load an IpConfig from a raw object | 0 |
| 3486 | 1 | 1 | thin <=2 | Thin/noise candidate | Load an IpConfig from an Hjson description in txt | 0 |
| 3494 | 1 | 1 | thin <=2 | Thin/noise candidate | Call a subprocess. Args: args: List[str]; List of argument | 0 |
| 3495 | 1 | 1 | thin <=2 | Thin/noise candidate | Create a dictionary representing an object file in the map. | 0 |
| 3498 | 1 | 1 | thin <=2 | Thin/noise candidate | Create a CounterMeasure object from a dict. The 'raw' dict must have | 0 |
| 3499 | 1 | 1 | thin <=2 | Thin/noise candidate | Create a list of CounterMeasure objects from a list of dicts. The dic | 0 |
| 3500 | 1 | 1 | thin <=2 | Thin/noise candidate | Find countermeasures in the given list of RTL files. The return value | 0 |
| 3501 | 1 | 1 | thin <=2 | Thin/noise candidate | Compare RTL to Hjson countermeasures. This compares a dictionary of c | 0 |
| 3502 | 1 | 1 | thin <=2 | Thin/noise candidate | Create a Feature object from a dict. The 'raw' dict must have the key | 0 |
| 3503 | 1 | 1 | thin <=2 | Thin/noise candidate | Create a list of Feature objects from a list of dicts. The dicts in ' | 0 |
| 3504 | 1 | 1 | thin <=2 | Thin/noise candidate | Calculate any specific resval for the field field_bits is an object g | 0 |
| 3505 | 1 | 1 | thin <=2 | Thin/noise candidate | Load an IpBlock from an hjson description in txt | 0 |
| 3506 | 1 | 1 | thin <=2 | Thin/noise candidate | Load an IpBlock from an hjson description in a file at path | 0 |
| 3507 | 1 | 1 | thin <=2 | Thin/noise candidate | Create a MultiRegister object from a dictionary. The underlying regis | 0 |
| 3508 | 1 | 1 | thin <=2 | Thin/noise candidate | Create a register that holds the fields from regs. The merged registe | 0 |
| 3509 | 1 | 1 | thin <=2 | Thin/noise candidate | Build a dictionary of blocks for a 'registers' field in the hjson The | 0 |
| 3514 | 1 | 1 | thin <=2 | Thin/noise candidate | Creates and registers a new pseudo-random number generator. If a gene | 0 |
| 3515 | 1 | 1 | thin <=2 | Thin/noise candidate | Retrieves a previously created pseudo-random number generator by its name. | 0 |

## Notes

- Topic labels are heuristic. They are intended for navigation, not as authoritative taxonomy.
- Many community names in GRAPH_REPORT.md are generic, so sample nodes drive the labels.
- Thin/noise communities are kept in the full table because they can reveal extraction gaps or duplicated test fixtures.
