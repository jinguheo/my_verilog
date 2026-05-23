# Hardware Description: vendor

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `vendor`
- `approved_label`: `pending:vendor`
- `doc_anchor`: `vendor`
- `module_name_prefix`: `vendor`
- `bridge_edge_count`: 40

## Inferred Hardware Role

`vendor` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 41
- Code categories: dv: 39, rtl: 1
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:vendor` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `ibex_icache_core_back_line_seq.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_back_line_seq.sv`
- `ibex_mem_intf_response_agent_cfg.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_response_agent_cfg.sv`
- `ibex_mem_intf_response_sequencer.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_response_sequencer.sv`
- `ibex_mem_intf_response_seq_lib.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_response_seq_lib.sv`
- `ibex_mem_intf_response_driver.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_response_driver.sv`
- `ibex_icache_core_protocol_checker.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_protocol_checker.sv`
- `ibex_icache_core_base_seq.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_base_seq.sv`
- `ibex_icache_core_seq_list.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_seq_list.sv`
- `ibex_mem_intf_request_driver.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_request_driver.sv`
- `ibex_mem_intf_response_agent.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_response_agent.sv`
- `ibex_mem_intf_request_agent.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_request_agent.sv`
- `ibex_icache_mem_protocol_checker.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_protocol_checker.sv`
- `ibex_icache_mem_base_seq.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\seq_lib\ibex_icache_mem_base_seq.sv`
- `ibex_icache_mem_resp_seq.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\seq_lib\ibex_icache_mem_resp_seq.sv`
- `ibex_icache_mem_seq_list.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\seq_lib\ibex_icache_mem_seq_list.sv`
- `ibex_simple_system_cosim_checker_bind.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\verilator\simple_system_cosim\ibex_simple_system_cosim_checker_bind.sv`
- `ibex_simple_system_cosim_checker_bind` (L5) - `opentitan\hw\vendor\lowrisc_ibex\dv\verilator\simple_system_cosim\ibex_simple_system_cosim_checker_bind.sv`
- `mem_model_pkg` (L9) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_agent_pkg.sv`
- `ibex_mem_intf_agent_pkg.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_agent_pkg.sv`
- `ibex_mem_intf_seq_item.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_seq_item.sv`
- `ibex_icache_core_agent_cfg.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_agent_cfg.sv`
- `ibex_icache_core_agent_cov.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_agent_cov.sv`
- `ibex_icache_core_agent_pkg.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_agent_pkg.sv`
- `ibex_icache_core_sequencer.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_sequencer.sv`
- `prim_ascon_duplex_tb_pkg.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\pre_dv\prim_ascon\prim_ascon_duplex_tb\rtl\prim_ascon_duplex_tb_pkg.sv`
- `ibex_ifetch_pmp_seq_item.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_cosim_agent\ibex_ifetch_pmp_seq_item.sv`
- `ibex_mem_intf_monitor.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_monitor.sv`
- `ibex_debug_triggers_overrides.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_debug_triggers_overrides.sv`
- `ibex_icache_core_bus_item.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_bus_item.sv`
- `ibex_icache_core_req_item.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_req_item.sv`
- `ibex_icache_core_rsp_item.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_rsp_item.sv`
- `ibex_simple_system_cosim_checker.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\verilator\simple_system_cosim\ibex_simple_system_cosim_checker.sv`
- `ibex_simple_system_cosim_checker` (L5) - `opentitan\hw\vendor\lowrisc_ibex\dv\verilator\simple_system_cosim\ibex_simple_system_cosim_checker.sv`
- `core_ibex_ifetch_pmp_if.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_cosim_agent\core_ibex_ifetch_pmp_if.sv`
- `ibex_ifetch_pmp_monitor.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_cosim_agent\ibex_ifetch_pmp_monitor.sv`
- `ibex_icache_core_monitor.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_monitor.sv`
- `ibex_icache_mem_agent_cfg.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_agent_cfg.sv`
- `ibex_icache_mem_agent_cov.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_agent_cov.sv`
- `ibex_icache_mem_agent_pkg.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_agent_pkg.sv`
- `ibex_icache_mem_resp_item.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_resp_item.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_core_back_line_seq.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_back_line_seq.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_mem_intf_response_agent_cfg.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_response_agent_cfg.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_mem_intf_response_sequencer.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_response_sequencer.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_mem_intf_response_seq_lib.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_response_seq_lib.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_mem_intf_response_driver.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_response_driver.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_core_protocol_checker.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_protocol_checker.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_core_base_seq.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_base_seq.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_core_seq_list.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_seq_list.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_mem_intf_request_driver.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_request_driver.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_mem_intf_response_agent.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_response_agent.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_mem_intf_request_agent.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_request_agent.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_mem_protocol_checker.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_protocol_checker.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_mem_base_seq.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\seq_lib\ibex_icache_mem_base_seq.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_mem_resp_seq.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\seq_lib\ibex_icache_mem_resp_seq.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_mem_seq_list.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\seq_lib\ibex_icache_mem_seq_list.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_simple_system_cosim_checker_bind.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\verilator\simple_system_cosim\ibex_simple_system_cosim_checker_bind.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_simple_system_cosim_checker_bind` | `opentitan\hw\vendor\lowrisc_ibex\dv\verilator\simple_system_cosim\ibex_simple_system_cosim_checker_bind.sv` |
| `spec_component_matches_code` | `component:vendor` | `mem_model_pkg` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_agent_pkg.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_mem_intf_agent_pkg.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_agent_pkg.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_mem_intf_seq_item.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_seq_item.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_core_agent_cfg.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_agent_cfg.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_core_agent_cov.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_agent_cov.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_core_agent_pkg.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_agent_pkg.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_core_sequencer.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_sequencer.sv` |
| `spec_component_matches_code` | `component:vendor` | `prim_ascon_duplex_tb_pkg.sv` | `ibex\vendor\lowrisc_ip\ip\prim\pre_dv\prim_ascon\prim_ascon_duplex_tb\rtl\prim_ascon_duplex_tb_pkg.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_ifetch_pmp_seq_item.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_cosim_agent\ibex_ifetch_pmp_seq_item.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_mem_intf_monitor.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_mem_intf_agent\ibex_mem_intf_monitor.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_debug_triggers_overrides.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\riscv_dv_extension\ibex_debug_triggers_overrides.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_core_bus_item.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_bus_item.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_core_req_item.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_req_item.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_core_rsp_item.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_rsp_item.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_simple_system_cosim_checker.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\verilator\simple_system_cosim\ibex_simple_system_cosim_checker.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_simple_system_cosim_checker` | `opentitan\hw\vendor\lowrisc_ibex\dv\verilator\simple_system_cosim\ibex_simple_system_cosim_checker.sv` |
| `spec_component_matches_code` | `component:vendor` | `core_ibex_ifetch_pmp_if.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_cosim_agent\core_ibex_ifetch_pmp_if.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_ifetch_pmp_monitor.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\common\ibex_cosim_agent\ibex_ifetch_pmp_monitor.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_core_monitor.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_monitor.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_mem_agent_cfg.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_agent_cfg.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_mem_agent_cov.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_agent_cov.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_mem_agent_pkg.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_agent_pkg.sv` |
| `spec_component_matches_code` | `component:vendor` | `ibex_icache_mem_resp_item.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_resp_item.sv` |

## Retrieval Guidance

- When a code-only query mentions `vendor`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
