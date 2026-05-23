# Spec Document: opentitan/hw/dv/sv/mem_bkdr_scb/data/mem_access_testplan.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\dv\sv\mem_bkdr_scb\data\mem_access_testplan.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\dv\sv\mem_bkdr_scb\data\mem_access_testplan.hjson`
- Original extension: `.hjson`
- Original bytes: 645

## Content

```hjson
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
//
// This DV coverplan documents basic memory access covergroups.
{
  covergroups: [
    {
      name: b2b_access_types_cg
      desc: '''
            - Covers that any combination of access types (R/R, R/W, W/R, W/W) can be present in b2b
            transaction scenarios.
            - Covers b2b access with the same address.
            - Covers b2b access with partial access or not.
            - Cross all above cases.
            '''
    }
  ]
}
```
