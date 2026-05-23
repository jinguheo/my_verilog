# Spec Document: opentitan/hw/top_darjeeling/data/otp/otp_ctrl_img_test_unlocked1.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_darjeeling\data\otp\otp_ctrl_img_test_unlocked1.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\top_darjeeling\data\otp\otp_ctrl_img_test_unlocked1.hjson`
- Original extension: `.hjson`
- Original bytes: 1152

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
            name:  "CREATOR_SW_CFG",
            items: [
                {
                    name: "CREATOR_SW_CFG_ROM_EXEC_EN",
                    // ROM execution is enabled if this item is set to a
                    // non-zero value.
                    value: "0xffffffff",
                },
            ],
        }
        {
            name:  "LIFE_CYCLE",
            // Can be one of the following strings:
            // RAW, TEST_UNLOCKED0-3, TEST_LOCKED0-2, DEV, PROD, PROD_END, RMA, SCRAP
            state: "TEST_UNLOCKED1",
            // Can range from 0 to 16.
            // Note that a value of 0 is only permissible in RAW state.
            count: 3
        }
    ]
}
```
