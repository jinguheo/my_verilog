# Spec Document: opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\data\top_darjeeling_ac_range_check.ipconfig.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\data\top_darjeeling_ac_range_check.ipconfig.hjson`
- Original extension: `.hjson`
- Original bytes: 546

## Content

```hjson
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  instance_name: top_darjeeling_ac_range_check
  param_values:
  {
    num_ranges: 32
    nr_role_bits: 4
    nr_ctn_uid_bits: 5
    module_instance_name: ac_range_check
    topname: darjeeling
    uniquified_modules: {}
  }
  dtgen:
  {
    num_ranges:
    {
      type: uint8
      name: num_ranges
      doc: Number of range registers
    }
  }
}
```
