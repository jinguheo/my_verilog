# Hardware Description: alert_esc_agent

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **covergroups**: //
- **desc**: // To enable these covergroups, please ensure the following variables are enabled:
- **covergroups**: //

## Identity

- `ip_block`: `alert_esc_agent`
- `bridge_edge_count`: 32
- Spec categories: testplan: 44
- Code categories: dv: 57
- Bridge relations: spec_path_matches_code_path: 32

## Spec Excerpts

### covergroups
_Source: `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_additional_testplan.hjson`_

```
// SPDX-License-Identifier: Apache-2.0
//
// This DV coverplan documents additional alert agent covergroups.
// To enable these covergroups, please ensure the following variables are enabled:
// `cfg.en_ping_cov` and `cfg.en_lpg_cov`
// Note that if LPG is enabled, the alert ping request handshake won't be initiated, so we cannot
// collect that coverage in this agent.
{
  covergroups: [
    {
…
```

### desc
_Source: `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_additional_testplan.hjson`_

```
// To enable these covergroups, please ensure the following variables are enabled:
// `cfg.en_ping_cov` and `cfg.en_lpg_cov`
// Note that if LPG is enabled, the alert ping request handshake won't be initiated, so we cannot
// collect that coverage in this agent.
{
  covergroups: [
    {
      name:  alert_trans_cg
      desc: '''Cover if the transaction is a ping request or an actual alert request
…
```

### covergroups
_Source: `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_basic_testplan.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
//
// This DV coverplan documents basic alert agent covergroups.
{
  covergroups: [
    {
      name: alert_handshake_complete_cg
      desc: '''Cover if the alert handshake completes.'''
    }
  ]
}
```

### desc
_Source: `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_basic_testplan.hjson`_

```
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
//
// This DV coverplan documents basic alert agent covergroups.
{
  covergroups: [
    {
      name: alert_handshake_complete_cg
      desc: '''Cover if the alert handshake completes.'''
    }
  ]
}
```

### covergroups
_Source: `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_additional_testplan.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
//
// This DV coverplan documents additional escalation agent covergroups.
// To enable these covergroups, please ensure the following variable is enabled:
// `cfg.en_ping_cov`
{
  covergroups: [
    {
      name:  esc_trans_cg
…
```

### desc
_Source: `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_additional_testplan.hjson`_

```
//
// This DV coverplan documents additional escalation agent covergroups.
// To enable these covergroups, please ensure the following variable is enabled:
// `cfg.en_ping_cov`
{
  covergroups: [
    {
      name:  esc_trans_cg
      desc: '''Cover if the transaction is a ping request or an actual escalation request.'''
    }
  ]
}
```

### covergroups
_Source: `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_basic_testplan.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
//
// This DV coverplan documents basic escalation agent covergroups.
{
  covergroups: [
    {
      name: esc_handshake_complete_cg
      desc: '''Cover if the escalation handshake completes.'''
    }
  ]
}
```

### desc
_Source: `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_basic_testplan.hjson`_

```
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
//
// This DV coverplan documents basic escalation agent covergroups.
{
  covergroups: [
    {
      name: esc_handshake_complete_cg
      desc: '''Cover if the escalation handshake completes.'''
    }
  ]
}
```

## Spec Anchors

- `alert_agent_additional_testplan.hjson` (L1) — `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_additional_testplan.hjson`
- `covergroups` (L11) — `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_additional_testplan.hjson`
- `desc` (L14) — `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_additional_testplan.hjson`
- `alert_agent_basic_testplan.hjson` (L1) — `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_basic_testplan.hjson`
- `covergroups` (L7) — `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_basic_testplan.hjson`
- `desc` (L10) — `opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_basic_testplan.hjson`
- `esc_agent_additional_testplan.hjson` (L1) — `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_additional_testplan.hjson`
- `covergroups` (L9) — `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_additional_testplan.hjson`
- `desc` (L12) — `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_additional_testplan.hjson`
- `esc_agent_basic_testplan.hjson` (L1) — `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_basic_testplan.hjson`
- `covergroups` (L7) — `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_basic_testplan.hjson`
- `desc` (L10) — `opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_basic_testplan.hjson`

## Code Evidence

**DV** (25)
  - `alert_base_driver.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\alert_base_driver.sv`
  - `alert_esc_agent.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent.sv`
  - `alert_esc_agent_cfg.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_cfg.sv`
  - `alert_esc_agent_cov.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_cov.sv`
  - `alert_esc_agent_pkg.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_agent_pkg.sv`
  - `alert_esc_base_monitor.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_base_monitor.sv`
  - `alert_esc_if.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_if.sv`
  - `alert_esc_probe_if.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_probe_if.sv`
  - `alert_esc_sequencer.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_sequencer.sv`
  - `alert_esc_seq_item.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\alert_esc_seq_item.sv`
  - `alert_monitor.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\alert_monitor.sv`
  - `alert_receiver_driver.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\alert_receiver_driver.sv`
  - `alert_sender_driver.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\alert_sender_driver.sv`
  - `esc_monitor.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\esc_monitor.sv`
  - `esc_receiver_driver.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\esc_receiver_driver.sv`
  - `esc_sender_driver.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\esc_sender_driver.sv`
  - `alert_receiver_alert_rsp_seq.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\seq_lib\alert_receiver_alert_rsp_seq.sv`
  - `alert_receiver_base_seq.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\seq_lib\alert_receiver_base_seq.sv`
  - `alert_receiver_ping_seq.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\seq_lib\alert_receiver_ping_seq.sv`
  - `alert_receiver_seq.sv`:L1 — `opentitan\hw\dv\sv\alert_esc_agent\seq_lib\alert_receiver_seq.sv`

## Neighbor Components

- `lowrisc_ibex` (2 refs; imports_from×2)
- `alert_handler` (2 refs; imports_from×2)

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

- For code-only queries mentioning `alert_esc_agent`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `alert_esc_agent`.
