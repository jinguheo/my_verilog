# Spec Document: opentitan/hw/top_darjeeling/ip_autogen/gpio/data/top_darjeeling_gpio.ipconfig.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_darjeeling\ip_autogen\gpio\data\top_darjeeling_gpio.ipconfig.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\top_darjeeling\ip_autogen\gpio\data\top_darjeeling_gpio.ipconfig.hjson`
- Original extension: `.hjson`
- Original bytes: 528

## Content

```hjson
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  instance_name: top_darjeeling_gpio
  param_values:
  {
    num_inp_period_counters: 8
    module_instance_name: gpio
    topname: darjeeling
    uniquified_modules: {}
  }
  dtgen:
  {
    num_inp_period_counters:
    {
      type: uint8
      name: input_period_counter_count
      doc: number of input period counters
    }
  }
}
```
