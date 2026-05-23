# Spec Document: opentitan/hw/top_darjeeling/data/top_darjeeling_seed.testing.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_darjeeling\data\top_darjeeling_seed.testing.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\top_darjeeling\data\top_darjeeling_seed.testing.hjson`
- Original extension: `.hjson`
- Original bytes: 926

## Content

```hjson
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
//
//////////////////////////////////////////////////////////////////////////////////////
// Seed configuration for topgen and subsequent flows                               //
// 256 bit seeds for compile-time random constants. All seeds must be different     //
// NOTE: REPLACE THIS FILE WITH A PRODUCTION SEED CONFIGURATION BEFORE THE TAPEOUT  //
//////////////////////////////////////////////////////////////////////////////////////
{
  name: "testing"
  topgen_seed: 30303603493614338660957087945302489777030192937656386903877022866265637632015
  otp_img_seed: 85452983286950371191603618368782861611109037138182535346147818831008789508651
  lc_ctrl_seed: 73183785937994765942105269559576336430731269166614113490738802526276329963158
}
```
