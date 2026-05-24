# Hardware Description: icache

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `icache`
- `bridge_edge_count`: 40
- Spec categories: component: 41
- Code categories: dv: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:icache` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**DV** (40)
  - `ibex_icache_core_back_line_seq.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_back_line_seq.sv`
  - `ibex_icache_core_protocol_checker.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_protocol_checker.sv`
  - `ibex_icache_core_base_seq.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_base_seq.sv`
  - `ibex_icache_core_seq_list.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_seq_list.sv`
  - `ibex_icache_mem_protocol_checker.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_protocol_checker.sv`
  - `ibex_icache_mem_base_seq.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\seq_lib\ibex_icache_mem_base_seq.sv`
  - `ibex_icache_mem_resp_seq.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\seq_lib\ibex_icache_mem_resp_seq.sv`
  - `ibex_icache_mem_seq_list.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\seq_lib\ibex_icache_mem_seq_list.sv`
  - `ibex_icache_core_agent_cfg.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_agent_cfg.sv`
  - `ibex_icache_core_agent_cov.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_agent_cov.sv`
  - `ibex_icache_core_agent_pkg.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_agent_pkg.sv`
  - `ibex_icache_core_sequencer.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_sequencer.sv`
  - `ibex_icache_core_bus_item.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_bus_item.sv`
  - `ibex_icache_core_req_item.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_req_item.sv`
  - `ibex_icache_core_rsp_item.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_rsp_item.sv`
  - `ibex_icache_core_monitor.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_monitor.sv`
  - `ibex_icache_mem_agent_cfg.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_agent_cfg.sv`
  - `ibex_icache_mem_agent_cov.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_agent_cov.sv`
  - `ibex_icache_mem_agent_pkg.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_agent_pkg.sv`
  - `ibex_icache_mem_resp_item.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_resp_item.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_back_line_seq.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_back_line_seq.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_protocol_checker.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_protocol_checker.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_base_seq.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_base_seq.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_seq_list.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_seq_list.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_protocol_checker.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_protocol_checker.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_base_seq.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\seq_lib\ibex_icache_mem_base_seq.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_resp_seq.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\seq_lib\ibex_icache_mem_resp_seq.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_seq_list.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\seq_lib\ibex_icache_mem_seq_list.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_agent_cfg.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_agent_cfg.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_agent_cov.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_agent_cov.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_agent_pkg.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_agent_pkg.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_sequencer.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_sequencer.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_bus_item.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_bus_item.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_req_item.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_req_item.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_rsp_item.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_rsp_item.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_monitor.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_monitor.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_agent_cfg.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_agent_cfg.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_agent_cov.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_agent_cov.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_agent_pkg.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_agent_pkg.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_resp_item.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_resp_item.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_sequencer.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_sequencer.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_driver.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_driver.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_bus_item.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_bus_item.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_req_item.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_req_item.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_agent.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_agent.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_monitor.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_monitor.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_driver.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_driver.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_agent.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_agent.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_model.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_model.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_if.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_if.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_if.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_if.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_back_line_seq.sv` | `ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_back_line_seq.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_oldval_test.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\tests\ibex_icache_oldval_test.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_protocol_checker.sv` | `ibex\dv\uvm\icache\dv\ibex_icache_core_agent\ibex_icache_core_protocol_checker.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_base_seq.sv` | `ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_base_seq.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_core_seq_list.sv` | `ibex\dv\uvm\icache\dv\ibex_icache_core_agent\seq_lib\ibex_icache_core_seq_list.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_base_test.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\icache\dv\tests\ibex_icache_base_test.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_protocol_checker.sv` | `ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\ibex_icache_mem_protocol_checker.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_base_seq.sv` | `ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\seq_lib\ibex_icache_mem_base_seq.sv` |
| `spec_component_matches_code` | `component:icache` | `ibex_icache_mem_resp_seq.sv` | `ibex\dv\uvm\icache\dv\ibex_icache_mem_agent\seq_lib\ibex_icache_mem_resp_seq.sv` |

## Retrieval Guidance

- For code-only queries mentioning `icache`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `icache`.
