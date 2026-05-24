# Hardware Description: chip_lc_ctrl_testplan.hjson

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **testpoints**: name: lc_ctrl
- **desc**: name: lc_ctrl
- **tags**: In silicon and FPGA test targets, verify that the device debug interfaces are not

## Identity

- `ip_block`: `chip_lc_ctrl_testplan.hjson`
- `bridge_edge_count`: 8
- Spec categories: testplan: 19
- Code categories: rtl: 8
- Bridge relations: spec_path_matches_code_path: 8

## Spec Excerpts

### testpoints
_Source: `opentitan/hw/top_earlgrey/data/ip/chip_lc_ctrl_testplan.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  name: lc_ctrl
  testpoints: [
    // LC_CTRL integration tests
    {
      name: chip_sw_lc_ctrl_alert_handler_escalation
      desc: '''Verify that the escalation signals from the alert handler are connected to LC ctrl.
…
```

### desc
_Source: `opentitan/hw/top_earlgrey/data/ip/chip_lc_ctrl_testplan.hjson`_

```
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  name: lc_ctrl
  testpoints: [
    // LC_CTRL integration tests
    {
      name: chip_sw_lc_ctrl_alert_handler_escalation
      desc: '''Verify that the escalation signals from the alert handler are connected to LC ctrl.

            - Trigger an alert to initiate the escalations.
…
```

### tags
_Source: `opentitan/hw/top_earlgrey/data/ip/chip_lc_ctrl_testplan.hjson`_

```
In silicon and FPGA test targets, verify that the device debug interfaces are not
            accessible when testing in `TEST_UNLOCKED`, `DEV` or `RMA` states.

            X-ref'ed with chip_sw_lc_ctrl_broadcast test, which verifies the connectivity of the LC
            decoded outputs to other IPs.
            X-ref'ed with alert_handler's escalation test.
            '''
      features: ["LC_
…
```

## Spec Anchors

- `chip_lc_ctrl_testplan.hjson` (L1) — `opentitan/hw/top_earlgrey/data/ip/chip_lc_ctrl_testplan.hjson`
- `testpoints` (L6) — `opentitan/hw/top_earlgrey/data/ip/chip_lc_ctrl_testplan.hjson`
- `desc` (L10) — `opentitan/hw/top_earlgrey/data/ip/chip_lc_ctrl_testplan.hjson`
- `features` (L28) — `opentitan/hw/top_earlgrey/data/ip/chip_lc_ctrl_testplan.hjson`
- `tags` (L29) — `opentitan/hw/top_earlgrey/data/ip/chip_lc_ctrl_testplan.hjson`
- `stage` (L30) — `opentitan/hw/top_earlgrey/data/ip/chip_lc_ctrl_testplan.hjson`
- `si stage` (L31) — `opentitan/hw/top_earlgrey/data/ip/chip_lc_ctrl_testplan.hjson`
- `lc states` (L32) — `opentitan/hw/top_earlgrey/data/ip/chip_lc_ctrl_testplan.hjson`
- `tests` (L33) — `opentitan/hw/top_earlgrey/data/ip/chip_lc_ctrl_testplan.hjson`
- `bazel` (L34) — `opentitan/hw/top_earlgrey/data/ip/chip_lc_ctrl_testplan.hjson`
- `otp mutate` (L112) — `opentitan/hw/top_earlgrey/data/ip/chip_lc_ctrl_testplan.hjson`

## Code Evidence

**RTL** (8)
  - `prim_alert_sender`:L268 — `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
  - `prim_alert_pkg`:L11 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `prim_esc_pkg`:L12 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `prim_secded_inv_72_64_enc`:L39 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv`
  - `prim_sec_anchor_flop`:L275 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv`
  - `prim_packer_fifo`:L233 — `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv`
  - `adc_ctrl`:L2047 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
  - `csrng`:L2617 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `chip_lc_ctrl_testplan.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `chip_lc_ctrl_testplan.hjson` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `chip_lc_ctrl_testplan.hjson` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `chip_lc_ctrl_testplan.hjson` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `chip_lc_ctrl_testplan.hjson` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `chip_lc_ctrl_testplan.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `chip_lc_ctrl_testplan.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `chip_lc_ctrl_testplan.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |

## Retrieval Guidance

- For code-only queries mentioning `chip_lc_ctrl_testplan.hjson`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `chip_lc_ctrl_testplan.hjson`.
