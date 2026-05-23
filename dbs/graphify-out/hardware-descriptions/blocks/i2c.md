# Hardware Description: i2c

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `i2c`
- `approved_label`: `pending:i2c`
- `doc_anchor`: `i2c`
- `module_name_prefix`: `i2c`
- `bridge_edge_count`: 112

## Inferred Hardware Role

`i2c` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 87, component: 41, testplan: 30, theory: 19, interface: 16
- Code categories: rtl: 64, dv: 47, sva: 44
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Anchors

- `component:i2c` (L1) - `__graphify_spec_only__/components.md`
- `i2c.hjson` (L1) - `opentitan/hw/ip/i2c/data/i2c.hjson`
- `human name` (L7) - `opentitan/hw/ip/i2c/data/i2c.hjson`
- `one line desc` (L8) - `opentitan/hw/ip/i2c/data/i2c.hjson`
- `one paragraph desc` (L9) - `opentitan/hw/ip/i2c/data/i2c.hjson`
- `cip id` (L16) - `opentitan/hw/ip/i2c/data/i2c.hjson`
- `design spec` (L17) - `opentitan/hw/ip/i2c/data/i2c.hjson`
- `dv doc` (L18) - `opentitan/hw/ip/i2c/data/i2c.hjson`
- `hw checklist` (L19) - `opentitan/hw/ip/i2c/data/i2c.hjson`
- `sw checklist` (L20) - `opentitan/hw/ip/i2c/data/i2c.hjson`
- `revisions` (L21) - `opentitan/hw/ip/i2c/data/i2c.hjson`
- `version` (L23) - `opentitan/hw/ip/i2c/data/i2c.hjson`
- `i2c_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/i2c/data/i2c_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/i2c/data/i2c_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/i2c/data/i2c_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/i2c/data/i2c_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/i2c/data/i2c_sec_cm_testplan.hjson`
- `i2c_testplan.hjson` (L1) - `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `testpoints` (L11) - `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `desc` (L17) - `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `Stimulus` (L21) - `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `Checking` (L30) - `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `stage` (L35) - `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `tests` (L36) - `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `covergroups` (L955) - `opentitan/hw/ip/i2c/data/i2c_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/i2c/doc/checklist.md`
- `I2C Checklist` (L1) - `opentitan/hw/ip/i2c/doc/checklist.md`
- `Design Checklist` (L8) - `opentitan/hw/ip/i2c/doc/checklist.md`
- `D1` (L10) - `opentitan/hw/ip/i2c/doc/checklist.md`
- `D2` (L34) - `opentitan/hw/ip/i2c/doc/checklist.md`
- `D2S` (L76) - `opentitan/hw/ip/i2c/doc/checklist.md`
- `D3` (L96) - `opentitan/hw/ip/i2c/doc/checklist.md`
- `Verification Checklist` (L122) - `opentitan/hw/ip/i2c/doc/checklist.md`
- `V1` (L124) - `opentitan/hw/ip/i2c/doc/checklist.md`

## Code Evidence

- `i2c_pkg` (L9) - `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv`
- `i2c_bind.sv` (L1) - `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv`
- `i2c_bind` (L5) - `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv`
- `i2c_protocol_cov.sv` (L1) - `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv`
- `i2c_protocol_cov` (L6) - `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv`
- `i2c_port_conv.sv` (L1) - `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv`
- `i2c_port_conv` (L6) - `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\i2c\dv\tb\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\i2c\dv\tb\tb.sv`
- `i2c_env_pkg` (L10) - `opentitan\hw\ip\i2c\dv\tests\i2c_test_pkg.sv`
- `i2c_test_pkg` (L10) - `opentitan\hw\ip\i2c\dv\tb\tb.sv`
- `i2c_if` (L50) - `opentitan\hw\ip\i2c\dv\tb\tb.sv`
- `i2c_dv_if` (L58) - `opentitan\hw\ip\i2c\dv\tb\tb.sv`
- `i2c_port_conv` (L68) - `opentitan\hw\ip\i2c\dv\tb\tb.sv`
- `i2c_base_test.sv` (L1) - `opentitan\hw\ip\i2c\dv\tests\i2c_base_test.sv`
- `i2c_test_pkg.sv` (L1) - `opentitan\hw\ip\i2c\dv\tests\i2c_test_pkg.sv`
- `i2c.sv` (L1) - `opentitan\hw\ip\i2c\rtl\i2c.sv`
- `i2c` (L9) - `opentitan\hw\ip\i2c\rtl\i2c.sv`
- `i2c_reg_pkg` (L32) - `opentitan\hw\ip\i2c\rtl\i2c_reg_top.sv`
- `i2c_reg_top` (L70) - `opentitan\hw\ip\i2c\rtl\i2c.sv`
- `i2c_core` (L112) - `opentitan\hw\ip\i2c\rtl\i2c.sv`
- `i2c_bus_monitor.sv` (L1) - `opentitan\hw\ip\i2c\rtl\i2c_bus_monitor.sv`
- `i2c_bus_monitor` (L8) - `opentitan\hw\ip\i2c\rtl\i2c_bus_monitor.sv`
- `i2c_controller_fsm.sv` (L1) - `opentitan\hw\ip\i2c\rtl\i2c_controller_fsm.sv`
- `i2c_controller_fsm` (L9) - `opentitan\hw\ip\i2c\rtl\i2c_controller_fsm.sv`
- `i2c_core.sv` (L1) - `opentitan\hw\ip\i2c\rtl\i2c_core.sv`
- `i2c_core` (L9) - `opentitan\hw\ip\i2c\rtl\i2c_core.sv`
- `i2c_fifos` (L376) - `opentitan\hw\ip\i2c\rtl\i2c_core.sv`
- `i2c_bus_monitor` (L502) - `opentitan\hw\ip\i2c\rtl\i2c_core.sv`
- `i2c_controller_fsm` (L527) - `opentitan\hw\ip\i2c\rtl\i2c_core.sv`
- `i2c_target_fsm` (L583) - `opentitan\hw\ip\i2c\rtl\i2c_core.sv`
- `i2c_fifos.sv` (L1) - `opentitan\hw\ip\i2c\rtl\i2c_fifos.sv`
- `i2c_fifos` (L7) - `opentitan\hw\ip\i2c\rtl\i2c_fifos.sv`
- `i2c_fifo_sync_sram_adapter` (L89) - `opentitan\hw\ip\i2c\rtl\i2c_fifos.sv`
- `i2c_fifo_sync_sram_adapter.sv` (L1) - `opentitan\hw\ip\i2c\rtl\i2c_fifo_sync_sram_adapter.sv`
- `i2c_fifo_sync_sram_adapter` (L10) - `opentitan\hw\ip\i2c\rtl\i2c_fifo_sync_sram_adapter.sv`
- `prim_fifo_sync_cnt` (L136) - `opentitan\hw\ip\i2c\rtl\i2c_fifo_sync_sram_adapter.sv`
- `i2c_pkg.sv` (L1) - `opentitan\hw\ip\i2c\rtl\i2c_pkg.sv`
- `i2c_reg_pkg.sv` (L1) - `opentitan\hw\ip\i2c\rtl\i2c_reg_pkg.sv`
- `i2c_reg_top.sv` (L1) - `opentitan\hw\ip\i2c\rtl\i2c_reg_top.sv`
- `i2c_reg_top` (L9) - `opentitan\hw\ip\i2c\rtl\i2c_reg_top.sv`
- `i2c_target_fsm.sv` (L1) - `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv`
- `i2c_target_fsm` (L9) - `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv`
- `i2c` (L1297) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:i2c` | `i2c_fifo_sync_sram_adapter.sv` | `opentitan\hw\ip\i2c\rtl\i2c_fifo_sync_sram_adapter.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_fifo_sync_sram_adapter` | `opentitan\hw\ip\i2c\rtl\i2c_fifo_sync_sram_adapter.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_protocol_cov.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_protocol_cov` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_base_test.sv` | `opentitan\hw\ip\i2c\dv\tests\i2c_base_test.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_controller_fsm.sv` | `opentitan\hw\ip\i2c\rtl\i2c_controller_fsm.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_controller_fsm` | `opentitan\hw\ip\i2c\rtl\i2c_controller_fsm.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_env_pkg` | `opentitan\hw\ip\i2c\dv\tests\i2c_test_pkg.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_test_pkg.sv` | `opentitan\hw\ip\i2c\dv\tests\i2c_test_pkg.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_port_conv.sv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_port_conv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_bus_monitor.sv` | `opentitan\hw\ip\i2c\rtl\i2c_bus_monitor.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_bus_monitor` | `opentitan\hw\ip\i2c\rtl\i2c_bus_monitor.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_pkg` | `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_target_fsm.sv` | `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_target_fsm` | `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_bind.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_bind` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_reg_pkg` | `opentitan\hw\ip\i2c\rtl\i2c_reg_top.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_reg_pkg.sv` | `opentitan\hw\ip\i2c\rtl\i2c_reg_pkg.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_reg_top.sv` | `opentitan\hw\ip\i2c\rtl\i2c_reg_top.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_reg_top` | `opentitan\hw\ip\i2c\rtl\i2c_reg_top.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_fifos.sv` | `opentitan\hw\ip\i2c\rtl\i2c_fifos.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_fifos` | `opentitan\hw\ip\i2c\rtl\i2c_fifos.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_fifo_sync_sram_adapter` | `opentitan\hw\ip\i2c\rtl\i2c_fifos.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_core.sv` | `opentitan\hw\ip\i2c\rtl\i2c_core.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_core` | `opentitan\hw\ip\i2c\rtl\i2c_core.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_fifos` | `opentitan\hw\ip\i2c\rtl\i2c_core.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_bus_monitor` | `opentitan\hw\ip\i2c\rtl\i2c_core.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_controller_fsm` | `opentitan\hw\ip\i2c\rtl\i2c_core.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_target_fsm` | `opentitan\hw\ip\i2c\rtl\i2c_core.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_pkg.sv` | `opentitan\hw\ip\i2c\rtl\i2c_pkg.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_test_pkg` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_if` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_dv_if` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_port_conv` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c.sv` | `opentitan\hw\ip\i2c\rtl\i2c.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c` | `opentitan\hw\ip\i2c\rtl\i2c.sv` |
| `spec_component_matches_code` | `component:i2c` | `i2c_reg_top` | `opentitan\hw\ip\i2c\rtl\i2c.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `i2c_pkg` | `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `i2c_bind.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `i2c_bind` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `i2c_protocol_cov.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `i2c_protocol_cov` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `i2c_port_conv.sv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `i2c_port_conv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_path_matches_code_path` | `i2c.hjson` | `tb.sv` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `i2c_pkg` | `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `i2c_bind.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `i2c_bind` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `i2c_protocol_cov.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `i2c_protocol_cov` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `i2c_port_conv.sv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `i2c_port_conv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_path_matches_code_path` | `i2c_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `i2c_testplan.hjson` | `i2c_pkg` | `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv` |
| `spec_path_matches_code_path` | `i2c_testplan.hjson` | `i2c_bind.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `i2c_testplan.hjson` | `i2c_bind` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `i2c_testplan.hjson` | `i2c_protocol_cov.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_path_matches_code_path` | `i2c_testplan.hjson` | `i2c_protocol_cov` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_path_matches_code_path` | `i2c_testplan.hjson` | `i2c_port_conv.sv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_path_matches_code_path` | `i2c_testplan.hjson` | `i2c_port_conv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_path_matches_code_path` | `i2c_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `i2c_pkg` | `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `i2c_bind.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `i2c_bind` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `i2c_protocol_cov.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `i2c_protocol_cov` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `i2c_port_conv.sv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `i2c_port_conv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `i2c_pkg` | `opentitan\hw\ip\i2c\rtl\i2c_target_fsm.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `i2c_bind.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `i2c_bind` | `opentitan\hw\ip\i2c\dv\sva\i2c_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `i2c_protocol_cov.sv` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `i2c_protocol_cov` | `opentitan\hw\ip\i2c\dv\sva\i2c_protocol_cov.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `i2c_port_conv.sv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `i2c_port_conv` | `opentitan\hw\ip\i2c\dv\tb\i2c_port_conv.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\i2c\dv\tb\tb.sv` |

## Retrieval Guidance

- When a code-only query mentions `i2c`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
