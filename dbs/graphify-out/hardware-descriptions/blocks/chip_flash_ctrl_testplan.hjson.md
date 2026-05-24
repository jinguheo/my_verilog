# Hardware Description: chip_flash_ctrl_testplan.hjson

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **testpoints**: name: flash_ctrl
- **desc**: name: flash_ctrl
- **stage**: - Verify that the flash ctrl sent the creator and owner seeds to keymgr. Verify with

## Identity

- `ip_block`: `chip_flash_ctrl_testplan.hjson`
- `bridge_edge_count`: 8
- Spec categories: testplan: 18
- Code categories: rtl: 8
- Bridge relations: spec_path_matches_code_path: 8

## Spec Excerpts

### testpoints
_Source: `opentitan/hw/top_earlgrey/data/ip/chip_flash_ctrl_testplan.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  name: flash_ctrl
  testpoints: [
    // FLASH integration tests
    {
      name: chip_sw_flash_init
      desc: '''Verify that flash initialization routine works correctly.

            - Initialize the flash ctrl by writing
…
```

### desc
_Source: `opentitan/hw/top_earlgrey/data/ip/chip_flash_ctrl_testplan.hjson`_

```
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  name: flash_ctrl
  testpoints: [
    // FLASH integration tests
    {
      name: chip_sw_flash_init
      desc: '''Verify that flash initialization routine works correctly.

            - Initialize the flash ctrl by writing 1 to the INIT register.
            - Poll the status r
…
```

### stage
_Source: `opentitan/hw/top_earlgrey/data/ip/chip_flash_ctrl_testplan.hjson`_

```
- Verify that the flash ctrl sent the creator and owner seeds to keymgr. Verify with
              different seed values.

            - This test needs to execute as a boot rom image.
            - In silicon, this will be covered by manuf_ft_provision_rma_token_and_personalization.
            '''
      features: ["FLASH_CTRL.INIT.SCRAMBLING_KEYS", "FLASH_CTRL.INIT.ROOT_SEEDS",
…
```

## Spec Anchors

- `chip_flash_ctrl_testplan.hjson` (L1) — `opentitan/hw/top_earlgrey/data/ip/chip_flash_ctrl_testplan.hjson`
- `testpoints` (L6) — `opentitan/hw/top_earlgrey/data/ip/chip_flash_ctrl_testplan.hjson`
- `desc` (L10) — `opentitan/hw/top_earlgrey/data/ip/chip_flash_ctrl_testplan.hjson`
- `features` (L23) — `opentitan/hw/top_earlgrey/data/ip/chip_flash_ctrl_testplan.hjson`
- `stage` (L25) — `opentitan/hw/top_earlgrey/data/ip/chip_flash_ctrl_testplan.hjson`
- `si stage` (L26) — `opentitan/hw/top_earlgrey/data/ip/chip_flash_ctrl_testplan.hjson`
- `lc states` (L27) — `opentitan/hw/top_earlgrey/data/ip/chip_flash_ctrl_testplan.hjson`
- `tests` (L28) — `opentitan/hw/top_earlgrey/data/ip/chip_flash_ctrl_testplan.hjson`
- `bazel` (L29) — `opentitan/hw/top_earlgrey/data/ip/chip_flash_ctrl_testplan.hjson`
- `boot stages` (L162) — `opentitan/hw/top_earlgrey/data/ip/chip_flash_ctrl_testplan.hjson`

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
| `spec_path_matches_code_path` | `chip_flash_ctrl_testplan.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `chip_flash_ctrl_testplan.hjson` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `chip_flash_ctrl_testplan.hjson` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `chip_flash_ctrl_testplan.hjson` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `chip_flash_ctrl_testplan.hjson` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `chip_flash_ctrl_testplan.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `chip_flash_ctrl_testplan.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `chip_flash_ctrl_testplan.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |

## Retrieval Guidance

- For code-only queries mentioning `chip_flash_ctrl_testplan.hjson`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `chip_flash_ctrl_testplan.hjson`.
