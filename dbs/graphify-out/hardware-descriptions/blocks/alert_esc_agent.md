# Hardware Description: alert_esc_agent

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `alert_esc_agent`
- `approved_label`: `pending:alert_esc_agent`
- `doc_anchor`: `alert_esc_agent`
- `module_name_prefix`: `alert_esc_agent`
- `bridge_edge_count`: 32

## Inferred Hardware Role

`alert_esc_agent` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: testplan: 44
- Code categories: dv: 57
- Bridge relations: spec_path_matches_code_path: 32

## Spec Anchors

- `alert_agent_additional_testplan.hjson` (L1) - `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_additional_testplan.hjson`
- `covergroups` (L11) - `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_additional_testplan.hjson`
- `desc` (L14) - `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_additional_testplan.hjson`
- `alert_agent_basic_testplan.hjson` (L1) - `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_basic_testplan.hjson`
- `covergroups` (L7) - `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_basic_testplan.hjson`
- `desc` (L10) - `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_basic_testplan.hjson`
- `esc_agent_additional_testplan.hjson` (L1) - `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_additional_testplan.hjson`
- `covergroups` (L9) - `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_additional_testplan.hjson`
- `desc` (L12) - `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_additional_testplan.hjson`
- `esc_agent_basic_testplan.hjson` (L1) - `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_basic_testplan.hjson`
- `covergroups` (L7) - `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_basic_testplan.hjson`
- `desc` (L10) - `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_basic_testplan.hjson`

## Code Evidence

- `alert_base_driver.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\alert_base_driver.sv`
- `alert_esc_agent.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent.sv`
- `alert_esc_agent_cfg.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_cfg.sv`
- `alert_esc_agent_cov.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_cov.sv`
- `alert_esc_agent_pkg.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_pkg.sv`
- `alert_esc_base_monitor.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_base_monitor.sv`
- `alert_esc_if.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_if.sv`
- `alert_esc_probe_if.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_probe_if.sv`
- `alert_esc_sequencer.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_sequencer.sv`
- `alert_esc_seq_item.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_seq_item.sv`
- `alert_monitor.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\alert_monitor.sv`
- `alert_receiver_driver.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\alert_receiver_driver.sv`
- `alert_sender_driver.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\alert_sender_driver.sv`
- `esc_monitor.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\esc_monitor.sv`
- `esc_receiver_driver.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\esc_receiver_driver.sv`
- `esc_sender_driver.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\esc_sender_driver.sv`
- `alert_receiver_alert_rsp_seq.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\seq_lib\alert_receiver_alert_rsp_seq.sv`
- `alert_receiver_base_seq.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\seq_lib\alert_receiver_base_seq.sv`
- `alert_receiver_ping_seq.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\seq_lib\alert_receiver_ping_seq.sv`
- `alert_receiver_seq.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\seq_lib\alert_receiver_seq.sv`
- `alert_sender_base_seq.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\seq_lib\alert_sender_base_seq.sv`
- `alert_sender_ping_rsp_seq.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\seq_lib\alert_sender_ping_rsp_seq.sv`
- `alert_sender_seq.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\seq_lib\alert_sender_seq.sv`
- `esc_receiver_base_seq.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\seq_lib\esc_receiver_base_seq.sv`
- `esc_receiver_esc_rsp_seq.sv` (L1) - `opentitan\hw\dv\sv\alert_esc_agent\seq_lib\esc_receiver_esc_rsp_seq.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `alert_agent_additional_testplan.hjson` | `alert_base_driver.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_base_driver.sv` |
| `spec_path_matches_code_path` | `alert_agent_additional_testplan.hjson` | `alert_esc_agent.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent.sv` |
| `spec_path_matches_code_path` | `alert_agent_additional_testplan.hjson` | `alert_esc_agent_cfg.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_cfg.sv` |
| `spec_path_matches_code_path` | `alert_agent_additional_testplan.hjson` | `alert_esc_agent_cov.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_cov.sv` |
| `spec_path_matches_code_path` | `alert_agent_additional_testplan.hjson` | `alert_esc_agent_pkg.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_pkg.sv` |
| `spec_path_matches_code_path` | `alert_agent_additional_testplan.hjson` | `alert_esc_base_monitor.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_base_monitor.sv` |
| `spec_path_matches_code_path` | `alert_agent_additional_testplan.hjson` | `alert_esc_if.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_if.sv` |
| `spec_path_matches_code_path` | `alert_agent_additional_testplan.hjson` | `alert_esc_probe_if.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_probe_if.sv` |
| `spec_path_matches_code_path` | `alert_agent_basic_testplan.hjson` | `alert_base_driver.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_base_driver.sv` |
| `spec_path_matches_code_path` | `alert_agent_basic_testplan.hjson` | `alert_esc_agent.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent.sv` |
| `spec_path_matches_code_path` | `alert_agent_basic_testplan.hjson` | `alert_esc_agent_cfg.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_cfg.sv` |
| `spec_path_matches_code_path` | `alert_agent_basic_testplan.hjson` | `alert_esc_agent_cov.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_cov.sv` |
| `spec_path_matches_code_path` | `alert_agent_basic_testplan.hjson` | `alert_esc_agent_pkg.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_pkg.sv` |
| `spec_path_matches_code_path` | `alert_agent_basic_testplan.hjson` | `alert_esc_base_monitor.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_base_monitor.sv` |
| `spec_path_matches_code_path` | `alert_agent_basic_testplan.hjson` | `alert_esc_if.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_if.sv` |
| `spec_path_matches_code_path` | `alert_agent_basic_testplan.hjson` | `alert_esc_probe_if.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_probe_if.sv` |
| `spec_path_matches_code_path` | `esc_agent_additional_testplan.hjson` | `alert_base_driver.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_base_driver.sv` |
| `spec_path_matches_code_path` | `esc_agent_additional_testplan.hjson` | `alert_esc_agent.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent.sv` |
| `spec_path_matches_code_path` | `esc_agent_additional_testplan.hjson` | `alert_esc_agent_cfg.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_cfg.sv` |
| `spec_path_matches_code_path` | `esc_agent_additional_testplan.hjson` | `alert_esc_agent_cov.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_cov.sv` |
| `spec_path_matches_code_path` | `esc_agent_additional_testplan.hjson` | `alert_esc_agent_pkg.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_pkg.sv` |
| `spec_path_matches_code_path` | `esc_agent_additional_testplan.hjson` | `alert_esc_base_monitor.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_base_monitor.sv` |
| `spec_path_matches_code_path` | `esc_agent_additional_testplan.hjson` | `alert_esc_if.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_if.sv` |
| `spec_path_matches_code_path` | `esc_agent_additional_testplan.hjson` | `alert_esc_probe_if.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_probe_if.sv` |
| `spec_path_matches_code_path` | `esc_agent_basic_testplan.hjson` | `alert_base_driver.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_base_driver.sv` |
| `spec_path_matches_code_path` | `esc_agent_basic_testplan.hjson` | `alert_esc_agent.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent.sv` |
| `spec_path_matches_code_path` | `esc_agent_basic_testplan.hjson` | `alert_esc_agent_cfg.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_cfg.sv` |
| `spec_path_matches_code_path` | `esc_agent_basic_testplan.hjson` | `alert_esc_agent_cov.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_cov.sv` |
| `spec_path_matches_code_path` | `esc_agent_basic_testplan.hjson` | `alert_esc_agent_pkg.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_pkg.sv` |
| `spec_path_matches_code_path` | `esc_agent_basic_testplan.hjson` | `alert_esc_base_monitor.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_base_monitor.sv` |
| `spec_path_matches_code_path` | `esc_agent_basic_testplan.hjson` | `alert_esc_if.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_if.sv` |
| `spec_path_matches_code_path` | `esc_agent_basic_testplan.hjson` | `alert_esc_probe_if.sv` | `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_probe_if.sv` |

## Retrieval Guidance

- When a code-only query mentions `alert_esc_agent`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
