# Hardware Description: chip_aon_timer_testplan.hjson

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **testpoints**: name: aon_timer
- **desc**: name: aon_timer
- **stage**: desc: '''Verify the AON timer wake up interrupt in normal operating state.

## Identity

- `ip_block`: `chip_aon_timer_testplan.hjson`
- `bridge_edge_count`: 8
- Spec categories: testplan: 17
- Code categories: rtl: 8
- Bridge relations: spec_path_matches_code_path: 8

## Spec Excerpts

### testpoints
_Source: `opentitan/hw/top_earlgrey/data/ip/chip_aon_timer_testplan.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  name: aon_timer
  testpoints: [
    {
      name: chip_sw_aon_timer_wakeup_irq
      desc: '''Verify the AON timer wake up interrupt in normal operating state.

            - Program the PLIC to let the AON timer wake up inter
…
```

### desc
_Source: `opentitan/hw/top_earlgrey/data/ip/chip_aon_timer_testplan.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  name: aon_timer
  testpoints: [
    {
      name: chip_sw_aon_timer_wakeup_irq
      desc: '''Verify the AON timer wake up interrupt in normal operating state.

            - Program the PLIC to let the AON timer wake up inter
…
```

### stage
_Source: `opentitan/hw/top_earlgrey/data/ip/chip_aon_timer_testplan.hjson`_

```
desc: '''Verify the AON timer wake up interrupt in normal operating state.

            - Program the PLIC to let the AON timer wake up interrupt the CPU.
            - Program the AON timer to generate the wake up timeout interrupt after some time.
            - Issue a WFI to wait for the interrupt to trigger.
            - Service the interrupt when it triggers; verify that it came from AON tim
…
```

## Spec Anchors

- `chip_aon_timer_testplan.hjson` (L1) — `opentitan/hw/top_earlgrey/data/ip/chip_aon_timer_testplan.hjson`
- `testpoints` (L6) — `opentitan/hw/top_earlgrey/data/ip/chip_aon_timer_testplan.hjson`
- `desc` (L9) — `opentitan/hw/top_earlgrey/data/ip/chip_aon_timer_testplan.hjson`
- `stage` (L17) — `opentitan/hw/top_earlgrey/data/ip/chip_aon_timer_testplan.hjson`
- `si stage` (L18) — `opentitan/hw/top_earlgrey/data/ip/chip_aon_timer_testplan.hjson`
- `lc states` (L19) — `opentitan/hw/top_earlgrey/data/ip/chip_aon_timer_testplan.hjson`
- `features` (L20) — `opentitan/hw/top_earlgrey/data/ip/chip_aon_timer_testplan.hjson`
- `tests` (L21) — `opentitan/hw/top_earlgrey/data/ip/chip_aon_timer_testplan.hjson`
- `bazel` (L22) — `opentitan/hw/top_earlgrey/data/ip/chip_aon_timer_testplan.hjson`

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
| `spec_path_matches_code_path` | `chip_aon_timer_testplan.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `chip_aon_timer_testplan.hjson` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `chip_aon_timer_testplan.hjson` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `chip_aon_timer_testplan.hjson` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `chip_aon_timer_testplan.hjson` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `chip_aon_timer_testplan.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `chip_aon_timer_testplan.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `chip_aon_timer_testplan.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |

## Retrieval Guidance

- For code-only queries mentioning `chip_aon_timer_testplan.hjson`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `chip_aon_timer_testplan.hjson`.
