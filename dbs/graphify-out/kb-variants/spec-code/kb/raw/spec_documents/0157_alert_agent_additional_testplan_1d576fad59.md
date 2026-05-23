# Spec Document: opentitan/hw/dv/sv/alert_esc_agent/data/alert_agent_additional_testplan.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\dv\sv\alert_esc_agent\data\alert_agent_additional_testplan.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\dv\sv\alert_esc_agent\data\alert_agent_additional_testplan.hjson`
- Original extension: `.hjson`
- Original bytes: 885

## Content

```hjson
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
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
      name:  alert_trans_cg
      desc: '''Cover if the transaction is a ping request or an actual alert request.'''
    }
    {
      name:  alert_lpg_cg
      desc: '''Covers alert lpg status during an alert request.

      Cover if its lower-power-group (lpg) is enabled or disabled during an alert request.
      '''
    }
  ]
}
```
