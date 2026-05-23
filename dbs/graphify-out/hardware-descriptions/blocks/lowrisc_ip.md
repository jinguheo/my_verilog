# Hardware Description: lowrisc_ip

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `lowrisc_ip`
- `approved_label`: `pending:lowrisc_ip`
- `doc_anchor`: `lowrisc_ip`
- `module_name_prefix`: `lowrisc_ip`
- `bridge_edge_count`: 48

## Inferred Hardware Role

`lowrisc_ip` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 54, testplan: 27
- Code categories: dv: 114, other_code: 46, rtl: 12
- Bridge relations: spec_path_matches_code_path: 48

## Spec Anchors

- `design_doc.md` (L1) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `DVSim design doc` (L1) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `Context` (L6) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `Goals` (L16) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `Non-goals` (L107) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `Architecture` (L111) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `EDA tool flow steps` (L115) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `Flow-specific Makefile` (L127) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `DUT configuration` (L138) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `Parser stage` (L144) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `Mode object creation stage` (L150) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md`
- `glossary.md` (L1) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `Glossary of Terms` (L1) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `Build` (L3) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `Build configuration` (L13) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `Build modes` (L15) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `Compute infrastructure` (L23) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `Design level` (L30) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `DUT` (L55) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `DUT configuration file` (L60) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `EDA tool flow` (L66) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `Filelist` (L84) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md`
- `testplanner.md` (L1) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `DVSIM Testplanner tool` (L1) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Hjson testplan` (L10) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Testpoints` (L14) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Covergroups` (L111) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Import shared testplans` (L141) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Example sources` (L206) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Limitations` (L216) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Usage examples` (L222) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `Standalone tool invocations` (L224) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`
- `APIs for external tools` (L275) - `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md`

## Code Evidence

- `clk_if.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_if.sv`
- `clk_rst_if.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_rst_if.sv`
- `common_ifs_pkg.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\common_ifs_pkg.sv`
- `entropy_subsys_fifo_exception_if.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_if.sv`
- `entropy_subsys_fifo_exception_pkg.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_pkg.sv`
- `pins_if.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\pins_if.sv`
- `rst_shadowed_if.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\rst_shadowed_if.sv`
- `csr_seq_lib.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\csr_utils\csr_seq_lib.sv`
- `csr_utils_pkg.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\csr_utils\csr_utils_pkg.sv`
- `csr_excl_item.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\csr_excl_item.sv`
- `dv_base_lockable_field_cov.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_lockable_field_cov.sv`
- `dv_base_mem.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_mem.sv`
- `dv_base_mubi_cov.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_mubi_cov.sv`
- `dv_base_reg.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_reg.sv`
- `dv_base_reg_block.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_reg_block.sv`
- `dv_base_reg_field.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_reg_field.sv`
- `dv_base_reg_map.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_reg_map.sv`
- `dv_base_reg_pkg.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_reg_pkg.sv`
- `dv_base_shadowed_field_cov.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_base_reg\dv_base_shadowed_field_cov.sv`
- `dv_base_agent.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_agent.sv`
- `dv_base_agent_cfg.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_agent_cfg.sv`
- `dv_base_agent_cov.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_agent_cov.sv`
- `dv_base_driver.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_driver.sv`
- `dv_base_env.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_env.sv`
- `dv_base_env_cfg.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_env_cfg.sv`
- `dv_base_env_cov.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_env_cov.sv`
- `dv_base_monitor.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_monitor.sv`
- `dv_base_scoreboard.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_scoreboard.sv`
- `dv_base_seq.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_seq.sv`
- `dv_base_sequencer.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_sequencer.sv`
- `dv_base_test.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_test.sv`
- `dv_base_virtual_sequencer.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_virtual_sequencer.sv`
- `dv_base_vseq.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_base_vseq.sv`
- `dv_lib_pkg.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_lib\dv_lib_pkg.sv`
- `dv_report_catcher.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_utils\dv_report_catcher.sv`
- `dv_report_server.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_utils\dv_report_server.sv`
- `dv_test_status_pkg.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_utils\dv_test_status_pkg.sv`
- `dv_utils_pkg.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_utils\dv_utils_pkg.sv`
- `dv_vif_wrap.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\dv_utils\dv_vif_wrap.sv`
- `mem_bkdr_util.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\mem_bkdr_util\mem_bkdr_util.sv`
- `mem_bkdr_util_pkg.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\mem_bkdr_util\mem_bkdr_util_pkg.sv`
- `mem_bkdr_util_row_adapter.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\mem_bkdr_util\mem_bkdr_util_row_adapter.sv`
- `mem_model.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\mem_model\mem_model.sv`
- `mem_model_pkg.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\mem_model\mem_model_pkg.sv`
- `push_pull_agent.sv` (L1) - `ibex\vendor\lowrisc_ip\dv\sv\push_pull_agent\push_pull_agent.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `design_doc.md` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `clk_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_if.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `clk_rst_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_rst_if.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `common_ifs_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\common_ifs_pkg.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `entropy_subsys_fifo_exception_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_if.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `entropy_subsys_fifo_exception_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_pkg.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `pins_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\pins_if.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `rst_shadowed_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\rst_shadowed_if.sv` |
| `spec_path_matches_code_path` | `design_doc.md` | `csr_seq_lib.sv` | `ibex\vendor\lowrisc_ip\dv\sv\csr_utils\csr_seq_lib.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `clk_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_if.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `clk_rst_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_rst_if.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `common_ifs_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\common_ifs_pkg.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `entropy_subsys_fifo_exception_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_if.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `entropy_subsys_fifo_exception_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_pkg.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `pins_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\pins_if.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `rst_shadowed_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\rst_shadowed_if.sv` |
| `spec_path_matches_code_path` | `glossary.md` | `csr_seq_lib.sv` | `ibex\vendor\lowrisc_ip\dv\sv\csr_utils\csr_seq_lib.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `clk_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_if.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `clk_rst_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_rst_if.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `common_ifs_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\common_ifs_pkg.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `entropy_subsys_fifo_exception_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_if.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `entropy_subsys_fifo_exception_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_pkg.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `pins_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\pins_if.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `rst_shadowed_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\rst_shadowed_if.sv` |
| `spec_path_matches_code_path` | `testplanner.md` | `csr_seq_lib.sv` | `ibex\vendor\lowrisc_ip\dv\sv\csr_utils\csr_seq_lib.sv` |

## Retrieval Guidance

- When a code-only query mentions `lowrisc_ip`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
