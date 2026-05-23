# Spec Document: opentitan/hw/top_darjeeling/data/chip_cfg.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_darjeeling\data\chip_cfg.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\top_darjeeling\data\chip_cfg.hjson`
- Original extension: `.hjson`
- Original bytes: 735

## Content

```hjson
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  // Override existing project defaults to supply chip-specific values.
  overrides: [
    // Fusesoc core file directory hierarchy.
    {
      name: fusesoc_cores_root_dirs
      value: ["--cores-root {proj_root}/util",
              "--cores-root {proj_root}/hw/dv",
              "--cores-root {proj_root}/hw/formal",
              "--cores-root {proj_root}/hw/ip",
              "--cores-root {proj_root}/hw/lint",
              "--cores-root {proj_root}/hw/vendor",
              "--cores-root {proj_root}/hw/top_darjeeling"]
    }
  ]
}
```
