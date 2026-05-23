# Hardware Description: spi_host

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `spi_host`
- `approved_label`: `pending:spi_host`
- `doc_anchor`: `spi_host`
- `module_name_prefix`: `spi_host`
- `bridge_edge_count`: 112

## Inferred Hardware Role

`spi_host` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 89, component: 41, testplan: 30, theory: 19, interface: 15
- Code categories: dv: 84, rtl: 71, sva: 10
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Anchors

- `component:spi_host` (L1) - `__graphify_spec_only__/components.md`
- `spi_host.hjson` (L1) - `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `human name` (L6) - `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `one line desc` (L7) - `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `cip id` (L16) - `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `design spec` (L17) - `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `dv doc` (L18) - `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `hw checklist` (L19) - `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `sw checklist` (L20) - `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `revisions` (L21) - `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `version` (L23) - `opentitan/hw/ip/spi_host/data/spi_host.hjson`
- `spi_host_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/spi_host/data/spi_host_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/spi_host/data/spi_host_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/spi_host/data/spi_host_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/spi_host/data/spi_host_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/spi_host/data/spi_host_sec_cm_testplan.hjson`
- `spi_host_testplan.hjson` (L1) - `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `testpoints` (L13) - `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `desc` (L16) - `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `Stimulus` (L20) - `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `Checking` (L24) - `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `stage` (L27) - `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `tests` (L28) - `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `covergroups` (L291) - `opentitan/hw/ip/spi_host/data/spi_host_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/spi_host/doc/checklist.md`
- `SPI HOST Checklist` (L1) - `opentitan/hw/ip/spi_host/doc/checklist.md`
- `Design Checklist` (L11) - `opentitan/hw/ip/spi_host/doc/checklist.md`
- `D1` (L13) - `opentitan/hw/ip/spi_host/doc/checklist.md`
- `D2` (L37) - `opentitan/hw/ip/spi_host/doc/checklist.md`
- `D2S` (L79) - `opentitan/hw/ip/spi_host/doc/checklist.md`
- `D3` (L99) - `opentitan/hw/ip/spi_host/doc/checklist.md`
- `Verification Checklist` (L125) - `opentitan/hw/ip/spi_host/doc/checklist.md`
- `V1` (L127) - `opentitan/hw/ip/spi_host/doc/checklist.md`

## Code Evidence

- `tlul_adapter_reg_racl` (L52) - `opentitan\hw\ip\spi_host\rtl\spi_host_window.sv`
- `spi_if` (L46) - `opentitan\hw\ip\spi_host\dv\tb.sv`
- `spi_device_pkg` (L15) - `opentitan\hw\ip\spi_host\dv\tb.sv`
- `spi_host_fsm_if.sv` (L1) - `opentitan\hw\ip\spi_host\dv\spi_host_fsm_if.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\spi_host\dv\tb.sv`
- `tb` (L6) - `opentitan\hw\ip\spi_host\dv\tb.sv`
- `spi_host_env_pkg` (L10) - `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv`
- `spi_host_test_pkg` (L11) - `opentitan\hw\ip\spi_host\dv\tb.sv`
- `spi_host_reg_pkg` (L37) - `opentitan\hw\ip\spi_host\rtl\spi_host_reg_top.sv`
- `spi_host_cov_bind.sv` (L1) - `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_bind.sv`
- `spi_host_cov_bind` (L6) - `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_bind.sv`
- `spi_host_cov_if.sv` (L1) - `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_if.sv`
- `spi_host_pkg` (L13) - `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_if.sv`
- `spi_host_bind.sv` (L1) - `opentitan\hw\ip\spi_host\dv\sva\spi_host_bind.sv`
- `spi_host_bind` (L5) - `opentitan\hw\ip\spi_host\dv\sva\spi_host_bind.sv`
- `spi_host_data_stable_sva.sv` (L1) - `opentitan\hw\ip\spi_host\dv\sva\spi_host_data_stable_sva.sv`
- `spi_host_data_stable_sva` (L7) - `opentitan\hw\ip\spi_host\dv\sva\spi_host_data_stable_sva.sv`
- `whole_cycle_data_stable_signal_checker` (L43) - `opentitan\hw\ip\spi_host\dv\sva\spi_host_data_stable_sva.sv`
- `whole_cycle_data_stable_signal_checker` (L69) - `opentitan\hw\ip\spi_host\dv\sva\spi_host_data_stable_sva.sv`
- `spi_host_base_test.sv` (L1) - `opentitan\hw\ip\spi_host\dv\tests\spi_host_base_test.sv`
- `spi_host_test_pkg.sv` (L1) - `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv`
- `spi_host.sv` (L1) - `opentitan\hw\ip\spi_host\rtl\spi_host.sv`
- `spi_host` (L11) - `opentitan\hw\ip\spi_host\rtl\spi_host.sv`
- `spi_host_cmd_pkg` (L40) - `opentitan\hw\ip\spi_host\rtl\spi_host_shift_register.sv`
- `spi_host_reg_top` (L89) - `opentitan\hw\ip\spi_host\rtl\spi_host.sv`
- `spi_host_command_queue` (L305) - `opentitan\hw\ip\spi_host\rtl\spi_host.sv`
- `spi_host_window` (L333) - `opentitan\hw\ip\spi_host\rtl\spi_host.sv`
- `spi_host_data_fifos` (L431) - `opentitan\hw\ip\spi_host\rtl\spi_host.sv`
- `spi_host_core` (L480) - `opentitan\hw\ip\spi_host\rtl\spi_host.sv`
- `spi_host_byte_merge.sv` (L1) - `opentitan\hw\ip\spi_host\rtl\spi_host_byte_merge.sv`
- `spi_host_byte_merge` (L8) - `opentitan\hw\ip\spi_host\rtl\spi_host_byte_merge.sv`
- `spi_host_byte_select.sv` (L1) - `opentitan\hw\ip\spi_host\rtl\spi_host_byte_select.sv`
- `spi_host_byte_select` (L7) - `opentitan\hw\ip\spi_host\rtl\spi_host_byte_select.sv`
- `spi_host_cmd_pkg.sv` (L1) - `opentitan\hw\ip\spi_host\rtl\spi_host_cmd_pkg.sv`
- `spi_host_command_queue.sv` (L1) - `opentitan\hw\ip\spi_host\rtl\spi_host_command_queue.sv`
- `spi_host_command_queue` (L8) - `opentitan\hw\ip\spi_host\rtl\spi_host_command_queue.sv`
- `spi_host_core.sv` (L1) - `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv`
- `spi_host_core` (L8) - `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv`
- `spi_host_byte_merge` (L67) - `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv`
- `spi_host_byte_select` (L80) - `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv`
- `spi_host_shift_register` (L100) - `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv`
- `spi_host_fsm` (L126) - `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv`
- `spi_host_data_fifos.sv` (L1) - `opentitan\hw\ip\spi_host\rtl\spi_host_data_fifos.sv`
- `spi_host_data_fifos` (L10) - `opentitan\hw\ip\spi_host\rtl\spi_host_data_fifos.sv`
- `spi_host_fsm.sv` (L1) - `opentitan\hw\ip\spi_host\rtl\spi_host_fsm.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:spi_host` | `spi_host` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_data_stable_sva.sv` | `opentitan\hw\ip\spi_host\dv\sva\spi_host_data_stable_sva.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_data_stable_sva` | `opentitan\hw\ip\spi_host\dv\sva\spi_host_data_stable_sva.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_base_test.sv` | `opentitan\hw\ip\spi_host\dv\tests\spi_host_base_test.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_cmd_pkg` | `opentitan\hw\ip\spi_host\rtl\spi_host_shift_register.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_shift_register.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_shift_register.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_shift_register` | `opentitan\hw\ip\spi_host\rtl\spi_host_shift_register.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_env_pkg` | `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_test_pkg.sv` | `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_command_queue.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_command_queue.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_command_queue` | `opentitan\hw\ip\spi_host\rtl\spi_host_command_queue.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_cov_bind.sv` | `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_bind.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_cov_bind` | `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_bind.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_byte_select.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_byte_select.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_byte_select` | `opentitan\hw\ip\spi_host\rtl\spi_host_byte_select.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_byte_merge.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_byte_merge.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_byte_merge` | `opentitan\hw\ip\spi_host\rtl\spi_host_byte_merge.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_data_fifos.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_data_fifos.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_data_fifos` | `opentitan\hw\ip\spi_host\rtl\spi_host_data_fifos.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_cov_if.sv` | `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_if.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_pkg` | `opentitan\hw\ip\spi_host\dv\cov\spi_host_cov_if.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_reg_pkg` | `opentitan\hw\ip\spi_host\rtl\spi_host_reg_top.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_bind.sv` | `opentitan\hw\ip\spi_host\dv\sva\spi_host_bind.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_bind` | `opentitan\hw\ip\spi_host\dv\sva\spi_host_bind.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_cmd_pkg.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_cmd_pkg.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_reg_pkg.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_reg_pkg.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_reg_top.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_reg_top.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_reg_top` | `opentitan\hw\ip\spi_host\rtl\spi_host_reg_top.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_window.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_window.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_window` | `opentitan\hw\ip\spi_host\rtl\spi_host_window.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_fsm_if.sv` | `opentitan\hw\ip\spi_host\dv\spi_host_fsm_if.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_core.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_core` | `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_byte_merge` | `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_byte_select` | `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_shift_register` | `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_fsm` | `opentitan\hw\ip\spi_host\rtl\spi_host_core.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_fsm.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host_fsm.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host_fsm` | `opentitan\hw\ip\spi_host\rtl\spi_host_fsm.sv` |
| `spec_component_matches_code` | `component:spi_host` | `spi_host.sv` | `opentitan\hw\ip\spi_host\rtl\spi_host.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `tlul_adapter_reg_racl` | `opentitan\hw\ip\spi_host\rtl\spi_host_window.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `spi_if` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `spi_device_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `spi_host_fsm_if.sv` | `opentitan\hw\ip\spi_host\dv\spi_host_fsm_if.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `tb.sv` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `tb` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `spi_host_env_pkg` | `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv` |
| `spec_path_matches_code_path` | `spi_host.hjson` | `spi_host_test_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `tlul_adapter_reg_racl` | `opentitan\hw\ip\spi_host\rtl\spi_host_window.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `spi_if` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `spi_device_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `spi_host_fsm_if.sv` | `opentitan\hw\ip\spi_host\dv\spi_host_fsm_if.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `spi_host_env_pkg` | `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv` |
| `spec_path_matches_code_path` | `spi_host_sec_cm_testplan.hjson` | `spi_host_test_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_testplan.hjson` | `tlul_adapter_reg_racl` | `opentitan\hw\ip\spi_host\rtl\spi_host_window.sv` |
| `spec_path_matches_code_path` | `spi_host_testplan.hjson` | `spi_if` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_testplan.hjson` | `spi_device_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_testplan.hjson` | `spi_host_fsm_if.sv` | `opentitan\hw\ip\spi_host\dv\spi_host_fsm_if.sv` |
| `spec_path_matches_code_path` | `spi_host_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_testplan.hjson` | `tb` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `spi_host_testplan.hjson` | `spi_host_env_pkg` | `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv` |
| `spec_path_matches_code_path` | `spi_host_testplan.hjson` | `spi_host_test_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tlul_adapter_reg_racl` | `opentitan\hw\ip\spi_host\rtl\spi_host_window.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `spi_if` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `spi_device_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `spi_host_fsm_if.sv` | `opentitan\hw\ip\spi_host\dv\spi_host_fsm_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `spi_host_env_pkg` | `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `spi_host_test_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tlul_adapter_reg_racl` | `opentitan\hw\ip\spi_host\rtl\spi_host_window.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `spi_if` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `spi_device_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `spi_host_fsm_if.sv` | `opentitan\hw\ip\spi_host\dv\spi_host_fsm_if.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\spi_host\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `spi_host_env_pkg` | `opentitan\hw\ip\spi_host\dv\tests\spi_host_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `spi_host_test_pkg` | `opentitan\hw\ip\spi_host\dv\tb.sv` |

## Retrieval Guidance

- When a code-only query mentions `spi_host`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
