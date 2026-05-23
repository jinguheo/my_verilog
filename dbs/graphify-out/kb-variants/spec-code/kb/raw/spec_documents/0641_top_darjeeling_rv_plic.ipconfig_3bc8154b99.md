# Spec Document: opentitan/hw/top_darjeeling/ip_autogen/rv_plic/data/top_darjeeling_rv_plic.ipconfig.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_darjeeling\ip_autogen\rv_plic\data\top_darjeeling_rv_plic.ipconfig.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\top_darjeeling\ip_autogen\rv_plic\data\top_darjeeling_rv_plic.ipconfig.hjson`
- Original extension: `.hjson`
- Original bytes: 535

## Content

```hjson
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  instance_name: top_darjeeling_rv_plic
  param_values:
  {
    module_instance_name: rv_plic
    src: 132
    target: 1
    prio: 3
    topname: darjeeling
    uniquified_modules: {}
    racl_support: false
  }
  dtgen:
  {
    src:
    {
      type: uint16
      name: num_irq_sources
      doc: Number of interrupt sources
    }
  }
}
```
