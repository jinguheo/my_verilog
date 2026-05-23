# Spec Document: opentitan/hw/top_earlgrey/data/ip/chip_pwm_testplan.hjson

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_earlgrey\data\ip\chip_pwm_testplan.hjson`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\top_earlgrey\data\ip\chip_pwm_testplan.hjson`
- Original extension: `.hjson`
- Original bytes: 784

## Content

```hjson
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  name: pwm
  testpoints: [
    {
      name: chip_sw_pwm_smoketest
      desc: '''Verify that the PWM outputs correct wave.

              - Program the PWM to output waves of 24hz, 48, 98hz.
              - Program the duty cycle to 11%, 36%, 50%, 71%, and 91%.
              - The test harness should check that the frequency and duty cycle is correct within a tolerance of 2%.
            '''
      features:["PWM.DUTYCYCLE", "PWM.CLOCKDIVIDER"]
      stage: V3
      si_stage: SV3
      lc_states: ["PROD"]
      tests: []
      bazel: ["//sw/device/tests:pwm_smoketest"]
    }
  ]
}
```
