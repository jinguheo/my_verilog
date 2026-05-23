# Hardware Description: tlul

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `tlul`
- `approved_label`: `pending:tlul`
- `doc_anchor`: `tlul`
- `module_name_prefix`: `tlul`
- `bridge_edge_count`: 80

## Inferred Hardware Role

`tlul` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 70, component: 41, testplan: 14, theory: 1
- Code categories: rtl: 142, sva: 6, package: 2
- Bridge relations: spec_component_matches_code: 40, spec_path_matches_code_path: 40

## Spec Anchors

- `component:tlul` (L1) - `__graphify_spec_only__/components.md`
- `tlul.prj.hjson` (L1) - `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `design spec` (L7) - `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `dv doc` (L8) - `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `hw checklist` (L9) - `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `revisions` (L10) - `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `version` (L12) - `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `life stage` (L13) - `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `design stage` (L14) - `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `verification stage` (L15) - `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `commit id` (L16) - `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `notes` (L17) - `opentitan/hw/ip/tlul/data/tlul.prj.hjson`
- `tlul_testplan.hjson` (L1) - `opentitan/hw/ip/tlul/data/tlul_testplan.hjson`
- `testpoints` (L8) - `opentitan/hw/ip/tlul/data/tlul_testplan.hjson`
- `desc` (L11) - `opentitan/hw/ip/tlul/data/tlul_testplan.hjson`
- `stage` (L12) - `opentitan/hw/ip/tlul/data/tlul_testplan.hjson`
- `si stage` (L13) - `opentitan/hw/ip/tlul/data/tlul_testplan.hjson`
- `tests` (L14) - `opentitan/hw/ip/tlul/data/tlul_testplan.hjson`
- `README.md` (L1) - `opentitan/hw/ip/tlul/doc/dv/README.md`
- `TLUL XBAR DV document` (L1) - `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Goals` (L4) - `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Current status` (L11) - `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Design features` (L16) - `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Testbench architecture` (L29) - `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Block diagram` (L32) - `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Top level testbench` (L35) - `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Common DV utility components` (L41) - `opentitan/hw/ip/tlul/doc/dv/README.md`
- `Global types & methods` (L46) - `opentitan/hw/ip/tlul/doc/dv/README.md`
- `TL agent` (L56) - `opentitan/hw/ip/tlul/doc/dv/README.md`
- `TlulProtocolChecker.md` (L1) - `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`
- `TL-UL Protocol Checker` (L1) - `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`
- `TileLink-UL Protocol Checker` (L3) - `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`
- `Overview` (L6) - `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`
- `Request Channel Channel A` (L42) - `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`
- `Response Channel Channel D` (L136) - `opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md`

## Code Evidence

- `prim_secded_inv_39_32_enc` (L17) - `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv`
- `prim_secded_inv_39_32_dec` (L18) - `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv`
- `prim_secded_inv_64_57_enc` (L24) - `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv`
- `prim_secded_inv_64_57_dec` (L25) - `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_chk.sv`
- `tlul_err` (L167) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv`
- `prim_fifo_async` (L28) - `opentitan\hw\ip\tlul\rtl\tlul_fifo_async.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv`
- `xbar_base_test.sv` (L1) - `opentitan\hw\ip\tlul\generic_dv\tests\xbar_base_test.sv`
- `xbar_error_test.sv` (L1) - `opentitan\hw\ip\tlul\generic_dv\tests\xbar_error_test.sv`
- `xbar_test_pkg.sv` (L1) - `opentitan\hw\ip\tlul\generic_dv\tests\xbar_test_pkg.sv`
- `xbar_env_pkg` (L11) - `opentitan\hw\ip\tlul\generic_dv\tests\xbar_test_pkg.sv`
- `sram2tlul.sv` (L1) - `opentitan\hw\ip\tlul\rtl\sram2tlul.sv`
- `sram2tlul` (L12) - `opentitan\hw\ip\tlul\rtl\sram2tlul.sv`
- `tlul_adapter_dmi.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_dmi.sv`
- `tlul_adapter_dmi` (L11) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_dmi.sv`
- `tlul_adapter_host.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_host.sv`
- `tlul_adapter_host` (L24) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_host.sv`
- `tlul_adapter_racl.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_racl.sv`
- `tlul_adapter_racl` (L14) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_racl.sv`
- `tlul_adapter_reg.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_reg.sv`
- `tlul_adapter_reg` (L95) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_reg.sv`
- `tlul_adapter_reg_racl.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_reg_racl.sv`
- `tlul_adapter_reg_racl` (L11) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_reg_racl.sv`
- `tlul_adapter_shim.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_shim.sv`
- `tlul_adapter_sram.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv`
- `tlul_adapter_sram` (L20) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv`
- `tlul_sram_byte` (L199) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv`
- `tlul_adapter_sram_racl.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram_racl.sv`
- `tlul_adapter_sram_racl` (L20) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram_racl.sv`
- `tlul_adapter_racl` (L85) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram_racl.sv`
- `tlul_adapter_vh.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_vh.sv`
- `tlul_adapter_vh` (L7) - `opentitan\hw\ip\tlul\rtl\tlul_adapter_vh.sv`
- `tlul_assert.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_assert.sv`
- `tlul_assert` (L10) - `opentitan\hw\ip\tlul\rtl\tlul_assert.sv`
- `tlul_assert_multiple.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_assert_multiple.sv`
- `tlul_assert_multiple` (L7) - `opentitan\hw\ip\tlul\rtl\tlul_assert_multiple.sv`
- `tlul_cmd_intg_chk.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_chk.sv`
- `tlul_cmd_intg_chk` (L11) - `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_chk.sv`
- `tlul_cmd_intg_gen.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv`
- `tlul_cmd_intg_gen` (L11) - `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv`
- `tlul_data_integ_dec.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv`
- `tlul_data_integ_dec` (L11) - `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv`
- `tlul_data_integ_enc.sv` (L1) - `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv`
- `tlul_data_integ_enc` (L11) - `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_sram_racl.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram_racl.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram_racl.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_racl` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram_racl.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_reg_racl.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_reg_racl.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_reg_racl` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_reg_racl.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_request_loopback.sv` | `opentitan\hw\ip\tlul\rtl\tlul_request_loopback.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_request_loopback` | `opentitan\hw\ip\tlul\rtl\tlul_request_loopback.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_assert_multiple.sv` | `opentitan\hw\ip\tlul\rtl\tlul_assert_multiple.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_assert_multiple` | `opentitan\hw\ip\tlul\rtl\tlul_assert_multiple.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_data_integ_dec.sv` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_data_integ_dec` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_data_integ_enc.sv` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_data_integ_enc` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_err` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_host.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_host.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_host` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_host.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_racl.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_racl.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_racl` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_racl.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_shim.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_shim.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_sram.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_sram` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_sram_byte` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_cmd_intg_chk.sv` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_chk.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_cmd_intg_chk` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_chk.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_cmd_intg_gen.sv` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_cmd_intg_gen` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_rsp_intg_chk.sv` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_chk.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_rsp_intg_chk` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_chk.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_rsp_intg_gen.sv` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_gen.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_rsp_intg_gen` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_gen.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_dmi.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_dmi.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_dmi` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_dmi.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_reg.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_reg.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_reg` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_reg.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_vh.sv` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_vh.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_adapter_vh` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_vh.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_fifo_async.sv` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_async.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_fifo_async` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_async.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_fifo_sync.sv` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_sync.sv` |
| `spec_component_matches_code` | `component:tlul` | `tlul_fifo_sync` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_sync.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `prim_secded_inv_39_32_enc` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `prim_secded_inv_39_32_dec` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `prim_secded_inv_64_57_enc` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `prim_secded_inv_64_57_dec` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_chk.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `tlul_err` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `prim_fifo_async` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_async.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `tb.sv` | `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `tlul.prj.hjson` | `tb` | `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `prim_secded_inv_39_32_enc` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `prim_secded_inv_39_32_dec` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `prim_secded_inv_64_57_enc` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `prim_secded_inv_64_57_dec` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_chk.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `tlul_err` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `prim_fifo_async` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_async.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `tlul_testplan.hjson` | `tb` | `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_secded_inv_39_32_enc` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_secded_inv_39_32_dec` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_secded_inv_64_57_enc` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_secded_inv_64_57_dec` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_chk.sv` |
| `spec_path_matches_code_path` | `README.md` | `tlul_err` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_fifo_async` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_async.sv` |
| `spec_path_matches_code_path` | `README.md` | `tb.sv` | `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `README.md` | `tb` | `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `TlulProtocolChecker.md` | `prim_secded_inv_39_32_enc` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv` |
| `spec_path_matches_code_path` | `TlulProtocolChecker.md` | `prim_secded_inv_39_32_dec` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv` |
| `spec_path_matches_code_path` | `TlulProtocolChecker.md` | `prim_secded_inv_64_57_enc` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv` |
| `spec_path_matches_code_path` | `TlulProtocolChecker.md` | `prim_secded_inv_64_57_dec` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_chk.sv` |
| `spec_path_matches_code_path` | `TlulProtocolChecker.md` | `tlul_err` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_path_matches_code_path` | `TlulProtocolChecker.md` | `prim_fifo_async` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_async.sv` |
| `spec_path_matches_code_path` | `TlulProtocolChecker.md` | `tb.sv` | `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `TlulProtocolChecker.md` | `tb` | `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_secded_inv_39_32_enc` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_enc.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_secded_inv_39_32_dec` | `opentitan\hw\ip\tlul\rtl\tlul_data_integ_dec.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_secded_inv_64_57_enc` | `opentitan\hw\ip\tlul\rtl\tlul_cmd_intg_gen.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_secded_inv_64_57_dec` | `opentitan\hw\ip\tlul\rtl\tlul_rsp_intg_chk.sv` |
| `spec_path_matches_code_path` | `README.md` | `tlul_err` | `opentitan\hw\ip\tlul\rtl\tlul_adapter_sram.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_fifo_async` | `opentitan\hw\ip\tlul\rtl\tlul_fifo_async.sv` |
| `spec_path_matches_code_path` | `README.md` | `tb.sv` | `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `README.md` | `tb` | `opentitan\hw\ip\tlul\generic_dv\tb\tb.sv` |

## Retrieval Guidance

- When a code-only query mentions `tlul`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
