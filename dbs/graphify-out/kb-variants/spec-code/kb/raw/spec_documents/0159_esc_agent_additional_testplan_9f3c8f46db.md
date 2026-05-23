# Spec Document: opentitan/hw/dv/sv/alert_esc_agent/data/esc_agent_additional_testplan.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\dv\sv\alert_esc_agent\data\esc_agent_additional_testplan.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\dv\sv\alert_esc_agent\data\esc_agent_additional_testplan.hjson`
- Original extension: `.hjson`
- Original bytes: 519

## Content

```hjson
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
      desc: '''Cover if the transaction is a ping request or an actual escalation request.'''
    }
  ]
}
```
