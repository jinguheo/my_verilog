# Spec Document: opentitan/hw/top_earlgrey/ip_autogen/rv_core_ibex/data/top_earlgrey_rv_core_ibex.ipconfig.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\data\top_earlgrey_rv_core_ibex.ipconfig.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\data\top_earlgrey_rv_core_ibex.ipconfig.hjson`
- Original extension: `.hjson`
- Original bytes: 538

## Content

```hjson
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  instance_name: top_earlgrey_rv_core_ibex
  param_values:
  {
    num_regions: 2
    module_instance_name: rv_core_ibex
    topname: earlgrey
    uniquified_modules: {}
    racl_support: false
  }
  dtgen:
  {
    num_regions:
    {
      type: uint8
      name: num_regions
      doc: Number of translatable regions per ibex bus
    }
  }
}
```
