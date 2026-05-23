# Spec Document: opentitan/hw/top_earlgrey/data/otp/otp_ctrl_img_raw.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_earlgrey\data\otp\otp_ctrl_img_raw.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\top_earlgrey\data\otp\otp_ctrl_img_raw.hjson`
- Original extension: `.hjson`
- Original bytes: 791

## Content

```hjson
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
//
// Use the gen-otp-img.py script to convert this configuration into
// a MEM file for preloading the OTP in FPGA synthesis or simulation.
//

{
    // The partition and item names must correspond with the OTP memory map.
    partitions: [
        {
            name:  "LIFE_CYCLE",
            // Can be one of the following strings:
            // RAW, TEST_UNLOCKED0-3, TEST_LOCKED0-2, DEV, PROD, PROD_END, RMA, SCRAP
            state: "RAW",
            // Can range from 0 to 16.
            // Note that a value of 0 is only permissible in RAW state.
            count: 0
        }
    ]
}
```
