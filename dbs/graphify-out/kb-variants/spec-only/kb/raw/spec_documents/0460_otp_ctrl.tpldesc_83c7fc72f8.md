# Spec Document: opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl.tpldesc.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\ip_templates\otp_ctrl\data\otp_ctrl.tpldesc.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\ip_templates\otp_ctrl\data\otp_ctrl.tpldesc.hjson`
- Original extension: `.hjson`
- Original bytes: 1018

## Content

```hjson
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  template_param_list: [
    {
      name: "topname"
      desc: "Name of top-level design, e.g., 'darjeeling' or 'earlgrey'"
      type: "string"
      default: ""
    }
    {
      name: "uniquified_modules"
      desc: "A dictionary mapping template_names to uniquified_names"
      type: "object"
      default: {"clkmgr": "clkmgr1"}
    }
    {
      name: "otp_mmap"
      desc: "An object containing the memory map and all attributes"
      type: "object"
      default: {}
    }
    {
      name: "module_instance_name"
      desc: "instance name in case there are multiple otp_ctrl instances. Not yet implemented."
      type: "string"
      default: "otp_ctrl"
    }
    {
      name: "enable_nvm_key"
      desc: "Enable the nvm key interface."
      type: "bool"
      default: "true"
    }
  ]
}
```
