# Spec Document: opentitan/hw/top_earlgrey/ip_autogen/pwm/data/top_earlgrey_pwm.ipconfig.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_earlgrey\ip_autogen\pwm\data\top_earlgrey_pwm.ipconfig.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\top_earlgrey\ip_autogen\pwm\data\top_earlgrey_pwm.ipconfig.hjson`
- Original extension: `.hjson`
- Original bytes: 500

## Content

```hjson
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  instance_name: top_earlgrey_pwm
  param_values:
  {
    module_instance_name: pwm
    topname: earlgrey
    uniquified_modules: {}
    nr_output_channels: 6
  }
  dtgen:
  {
    nr_output_channels:
    {
      type: uint8
      name: output_channel_count
      doc: Number of output channels
    }
  }
}
```
