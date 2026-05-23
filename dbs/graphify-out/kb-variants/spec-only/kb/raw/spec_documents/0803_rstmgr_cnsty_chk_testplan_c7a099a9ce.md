# Spec Document: opentitan/hw/top_earlgrey/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_earlgrey\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\data\rstmgr_cnsty_chk_testplan.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\top_earlgrey\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\data\rstmgr_cnsty_chk_testplan.hjson`
- Original extension: `.hjson`
- Original bytes: 1131

## Content

```hjson
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  name: "rstmgr_cnsty_chk"
  testpoints: [
    {
      name: unexpected_child_reset_activity
      desc: '''Verify unexpected child_reset activity flags an error.
            '''
      stage: V2S
      tests: ["rstmgr_cnsty_chk_smoke"]
    }
    {
      name: child_reset_asserts_late
      desc: '''Verify error triggered if child reset asserts late.
            '''
      stage: V2S
      tests: []
    }
    {
      name: child_reset_releases_late
      desc: '''Verify error triggered if child reset releases late.
            '''
      stage: V2S
      tests: []
    }
    {
      name: parent_reset_asserts_late
      desc: '''Verify error triggered if parent reset asserts late.
            '''
      stage: V2S
      tests: []
    }
    {
      name: parent_reset_releases_late
      desc: '''Verify error triggered if parent reset releases late.
            '''
      stage: V2S
      tests: []
    }
  ]
}
```
