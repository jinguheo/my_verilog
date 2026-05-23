# Hardware Description: spi_device

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `spi_device`
- `approved_label`: `pending:spi_device`
- `doc_anchor`: `spi_device`
- `module_name_prefix`: `spi_device`
- `bridge_edge_count`: 112

## Inferred Hardware Role

`spi_device` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 94, component: 41, testplan: 28, theory: 19, interface: 15
- Code categories: rtl: 148, other_code: 35, dv: 28, sva: 22
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Anchors

- `component:spi_device` (L1) - `__graphify_spec_only__/components.md`
- `spi_device.hjson` (L1) - `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `human name` (L6) - `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `one line desc` (L7) - `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `cip id` (L14) - `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `design spec` (L15) - `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `dv doc` (L16) - `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `hw checklist` (L17) - `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `sw checklist` (L18) - `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `revisions` (L19) - `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `version` (L21) - `opentitan/hw/ip/spi_device/data/spi_device.hjson`
- `spi_device_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/spi_device/data/spi_device_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/spi_device/data/spi_device_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/spi_device/data/spi_device_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/spi_device/data/spi_device_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/spi_device/data/spi_device_sec_cm_testplan.hjson`
- `spi_device_testplan.hjson` (L1) - `opentitan/hw/ip/spi_device/data/spi_device_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/spi_device/data/spi_device_testplan.hjson`
- `testpoints` (L13) - `opentitan/hw/ip/spi_device/data/spi_device_testplan.hjson`
- `desc` (L16) - `opentitan/hw/ip/spi_device/data/spi_device_testplan.hjson`
- `stage` (L21) - `opentitan/hw/ip/spi_device/data/spi_device_testplan.hjson`
- `tests` (L22) - `opentitan/hw/ip/spi_device/data/spi_device_testplan.hjson`
- `covergroups` (L368) - `opentitan/hw/ip/spi_device/data/spi_device_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/spi_device/doc/checklist.md`
- `SPI DEVICE Checklist` (L1) - `opentitan/hw/ip/spi_device/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/spi_device/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/spi_device/doc/checklist.md`
- `D2` (L34) - `opentitan/hw/ip/spi_device/doc/checklist.md`
- `D2S` (L76) - `opentitan/hw/ip/spi_device/doc/checklist.md`
- `D3` (L96) - `opentitan/hw/ip/spi_device/doc/checklist.md`
- `Verification Checklist` (L122) - `opentitan/hw/ip/spi_device/doc/checklist.md`
- `V1` (L124) - `opentitan/hw/ip/spi_device/doc/checklist.md`
- `V2` (L174) - `opentitan/hw/ip/spi_device/doc/checklist.md`
- `V2S` (L220) - `opentitan/hw/ip/spi_device/doc/checklist.md`

## Code Evidence

- `prim_fifo_async_sram_adapter` (L486) - `opentitan\hw\ip\spi_device\rtl\spid_upload.sv`
- `prim_ram_2p_pkg` (L15) - `opentitan\hw\ip\spi_device\rtl\spid_dpram.sv`
- `prim_ram_2p_async_adv` (L552) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv`
- `prim_slicer` (L922) - `opentitan\hw\ip\spi_device\rtl\spi_tpm.sv`
- `spi_device_bind.sv` (L1) - `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv`
- `spi_device_bind` (L5) - `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\spi_device\dv\tb\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\spi_device\dv\tb\tb.sv`
- `spi_device_env_pkg` (L10) - `opentitan\hw\ip\spi_device\dv\tests\spi_device_test_pkg.sv`
- `spi_device_test_pkg` (L11) - `opentitan\hw\ip\spi_device\dv\tb\tb.sv`
- `spi_device_base_test.sv` (L1) - `opentitan\hw\ip\spi_device\dv\tests\spi_device_base_test.sv`
- `spi_device_test_pkg.sv` (L1) - `opentitan\hw\ip\spi_device\dv\tests\spi_device_test_pkg.sv`
- `prog_passthrough_host.sv` (L1) - `opentitan\hw\ip\spi_device\pre_dv\program\prog_passthrough_host.sv`
- `spid_common` (L11) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv`
- `prog_passthrough_sw.sv` (L1) - `opentitan\hw\ip\spi_device\pre_dv\program\prog_passthrough_sw.sv`
- `spiflash.sv` (L1) - `opentitan\hw\ip\spi_device\pre_dv\program\spiflash.sv`
- `spid_common.sv` (L1) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_common.sv`
- `spid_jedec_tb.sv` (L1) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_jedec_tb.sv`
- `spid_jedec_tb` (L7) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_jedec_tb.sv`
- `spid_jedec` (L1337) - `opentitan\hw\ip\spi_device\rtl\spi_device.sv`
- `spi_cmdparse` (L1172) - `opentitan\hw\ip\spi_device\rtl\spi_device.sv`
- `spi_s2p` (L1137) - `opentitan\hw\ip\spi_device\rtl\spi_device.sv`
- `spi_p2s` (L1152) - `opentitan\hw\ip\spi_device\rtl\spi_device.sv`
- `spid_passthrough_tb.sv` (L1) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv`
- `tb` (L7) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv`
- `prog_passthrough_host` (L97) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv`
- `prog_passthrough_sw` (L103) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv`
- `spiflash` (L115) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv`
- `spid_readcmd_tb.sv` (L1) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_readcmd_tb.sv`
- `tb` (L12) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_readcmd_tb.sv`
- `spid_status_tb.sv` (L1) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_status_tb.sv`
- `spid_status_tb` (L7) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_status_tb.sv`
- `spid_status` (L1283) - `opentitan\hw\ip\spi_device\rtl\spi_device.sv`
- `spid_upload_tb.sv` (L1) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv`
- `spid_upload_tb` (L7) - `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv`
- `spid_upload` (L1367) - `opentitan\hw\ip\spi_device\rtl\spi_device.sv`
- `prim_sram_arbiter` (L1525) - `opentitan\hw\ip\spi_device\rtl\spi_tpm.sv`
- `spi_tpm_tb.sv` (L1) - `opentitan\hw\ip\spi_device\pre_dv\tb\spi_tpm_tb.sv`
- `spi_tpm_tb` (L25) - `opentitan\hw\ip\spi_device\pre_dv\tb\spi_tpm_tb.sv`
- `spi_tpm` (L1572) - `opentitan\hw\ip\spi_device\rtl\spi_device.sv`
- `spid_addr_4b.sv` (L1) - `opentitan\hw\ip\spi_device\rtl\spid_addr_4b.sv`
- `spid_addr_4b` (L23) - `opentitan\hw\ip\spi_device\rtl\spid_addr_4b.sv`
- `spid_csb_sync.sv` (L1) - `opentitan\hw\ip\spi_device\rtl\spid_csb_sync.sv`
- `spid_csb_sync` (L18) - `opentitan\hw\ip\spi_device\rtl\spid_csb_sync.sv`
- `spid_dpram.sv` (L1) - `opentitan\hw\ip\spi_device\rtl\spid_dpram.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:spi_device` | `spi_device` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_base_test.sv` | `opentitan\hw\ip\spi_device\dv\tests\spi_device_base_test.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_env_pkg` | `opentitan\hw\ip\spi_device\dv\tests\spi_device_test_pkg.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_test_pkg.sv` | `opentitan\hw\ip\spi_device\dv\tests\spi_device_test_pkg.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_bind.sv` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_bind` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_reg_pkg.sv` | `opentitan\hw\ip\spi_device\rtl\spi_device_reg_pkg.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_reg_top.sv` | `opentitan\hw\ip\spi_device\rtl\spi_device_reg_top.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_reg_top` | `opentitan\hw\ip\spi_device\rtl\spi_device_reg_top.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_pkg.sv` | `opentitan\hw\ip\spi_device\rtl\spi_device_pkg.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device.sv` | `opentitan\hw\ip\spi_device\rtl\spi_device.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device` | `opentitan\hw\ip\spi_device\rtl\spi_device.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_reg_top` | `opentitan\hw\ip\spi_device\rtl\spi_device.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_reg_pkg` | `opentitan\hw\ip\spi_device\rtl\spi_tpm.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_device_test_pkg` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `prog_passthrough_host.sv` | `opentitan\hw\ip\spi_device\pre_dv\program\prog_passthrough_host.sv` |
| `spec_component_matches_code` | `component:spi_device` | `prog_passthrough_sw.sv` | `opentitan\hw\ip\spi_device\pre_dv\program\prog_passthrough_sw.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_passthrough_tb.sv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `tb` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `prog_passthrough_host` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `prog_passthrough_sw` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spiflash` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_passthrough_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_fifo2sram_adapter.sv` | `opentitan\hw\ip\spi_device\rtl\spid_fifo2sram_adapter.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_fifo2sram_adapter` | `opentitan\hw\ip\spi_device\rtl\spid_fifo2sram_adapter.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_readcmd_tb.sv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_readcmd_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `tb` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_readcmd_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `prim_ram_2p_async_adv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_common` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_status_tb.sv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_status_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_status_tb` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_status_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_upload_tb.sv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_upload_tb` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spiflash.sv` | `opentitan\hw\ip\spi_device\pre_dv\program\spiflash.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_jedec_tb.sv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_jedec_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_jedec_tb` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_jedec_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_common.sv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_common.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_tpm_tb.sv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spi_tpm_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spi_tpm_tb` | `opentitan\hw\ip\spi_device\pre_dv\tb\spi_tpm_tb.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_readbuffer.sv` | `opentitan\hw\ip\spi_device\rtl\spid_readbuffer.sv` |
| `spec_component_matches_code` | `component:spi_device` | `spid_readbuffer` | `opentitan\hw\ip\spi_device\rtl\spid_readbuffer.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `prim_fifo_async_sram_adapter` | `opentitan\hw\ip\spi_device\rtl\spid_upload.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `prim_ram_2p_pkg` | `opentitan\hw\ip\spi_device\rtl\spid_dpram.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `prim_ram_2p_async_adv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `prim_slicer` | `opentitan\hw\ip\spi_device\rtl\spi_tpm.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `spi_device_bind.sv` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `spi_device_bind` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `tb.sv` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `spi_device.hjson` | `tb` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `prim_fifo_async_sram_adapter` | `opentitan\hw\ip\spi_device\rtl\spid_upload.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `prim_ram_2p_pkg` | `opentitan\hw\ip\spi_device\rtl\spid_dpram.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `prim_ram_2p_async_adv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `prim_slicer` | `opentitan\hw\ip\spi_device\rtl\spi_tpm.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `spi_device_bind.sv` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `spi_device_bind` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `spi_device_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `spi_device_testplan.hjson` | `prim_fifo_async_sram_adapter` | `opentitan\hw\ip\spi_device\rtl\spid_upload.sv` |
| `spec_path_matches_code_path` | `spi_device_testplan.hjson` | `prim_ram_2p_pkg` | `opentitan\hw\ip\spi_device\rtl\spid_dpram.sv` |
| `spec_path_matches_code_path` | `spi_device_testplan.hjson` | `prim_ram_2p_async_adv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_path_matches_code_path` | `spi_device_testplan.hjson` | `prim_slicer` | `opentitan\hw\ip\spi_device\rtl\spi_tpm.sv` |
| `spec_path_matches_code_path` | `spi_device_testplan.hjson` | `spi_device_bind.sv` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_path_matches_code_path` | `spi_device_testplan.hjson` | `spi_device_bind` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_path_matches_code_path` | `spi_device_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `spi_device_testplan.hjson` | `tb` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_fifo_async_sram_adapter` | `opentitan\hw\ip\spi_device\rtl\spid_upload.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_ram_2p_pkg` | `opentitan\hw\ip\spi_device\rtl\spid_dpram.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_ram_2p_async_adv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_slicer` | `opentitan\hw\ip\spi_device\rtl\spi_tpm.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `spi_device_bind.sv` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `spi_device_bind` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_fifo_async_sram_adapter` | `opentitan\hw\ip\spi_device\rtl\spid_upload.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_ram_2p_pkg` | `opentitan\hw\ip\spi_device\rtl\spid_dpram.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_ram_2p_async_adv` | `opentitan\hw\ip\spi_device\pre_dv\tb\spid_upload_tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_slicer` | `opentitan\hw\ip\spi_device\rtl\spi_tpm.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `spi_device_bind.sv` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `spi_device_bind` | `opentitan\hw\ip\spi_device\dv\sva\spi_device_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\spi_device\dv\tb\tb.sv` |

## Retrieval Guidance

- When a code-only query mentions `spi_device`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
