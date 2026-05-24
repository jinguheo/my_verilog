# Hardware Description: chip_rv_plic_testplan.hjson

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **testpoints**: name: rv_plic
- **desc**: name: rv_plic
- **stage**: The automated SW test enables all interrupts at the PLIC to interrupt the core. It uses

## Identity

- `ip_block`: `chip_rv_plic_testplan.hjson`
- `bridge_edge_count`: 8
- Spec categories: testplan: 17
- Code categories: rtl: 8
- Bridge relations: spec_path_matches_code_path: 8

## Spec Excerpts

### testpoints
_Source: `opentitan/hw/top_earlgrey/data/ip/chip_rv_plic_testplan.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  name: rv_plic
  testpoints: [
    // PLIC integration tests:
    {
      name: chip_sw_plic_all_irqs
      desc: '''Verify all interrupts from all peripherals aggregated at the PLIC.

            The automated SW test enables
…
```

### desc
_Source: `opentitan/hw/top_earlgrey/data/ip/chip_rv_plic_testplan.hjson`_

```
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{
  name: rv_plic
  testpoints: [
    // PLIC integration tests:
    {
      name: chip_sw_plic_all_irqs
      desc: '''Verify all interrupts from all peripherals aggregated at the PLIC.

            The automated SW test enables all interrupts at the PLIC to interrupt the core. It us
…
```

### stage
_Source: `opentitan/hw/top_earlgrey/data/ip/chip_rv_plic_testplan.hjson`_

```
The automated SW test enables all interrupts at the PLIC to interrupt the core. It uses
            the `intr_test` CSR in each peripheral to mock assert an interrupt, looping through all
            available interrupts in that peripheral. The ISR verifies that the right interrupt
            occurred. This is used as a catch-all interrupt test for all peripheral integration
            testing w
…
```

## Spec Anchors

- `chip_rv_plic_testplan.hjson` (L1) — `opentitan/hw/top_earlgrey/data/ip/chip_rv_plic_testplan.hjson`
- `testpoints` (L6) — `opentitan/hw/top_earlgrey/data/ip/chip_rv_plic_testplan.hjson`
- `desc` (L10) — `opentitan/hw/top_earlgrey/data/ip/chip_rv_plic_testplan.hjson`
- `stage` (L19) — `opentitan/hw/top_earlgrey/data/ip/chip_rv_plic_testplan.hjson`
- `si stage` (L20) — `opentitan/hw/top_earlgrey/data/ip/chip_rv_plic_testplan.hjson`
- `lc states` (L21) — `opentitan/hw/top_earlgrey/data/ip/chip_rv_plic_testplan.hjson`
- `features` (L22) — `opentitan/hw/top_earlgrey/data/ip/chip_rv_plic_testplan.hjson`
- `tests` (L23) — `opentitan/hw/top_earlgrey/data/ip/chip_rv_plic_testplan.hjson`
- `bazel` (L28) — `opentitan/hw/top_earlgrey/data/ip/chip_rv_plic_testplan.hjson`

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
| `spec_path_matches_code_path` | `chip_rv_plic_testplan.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `chip_rv_plic_testplan.hjson` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `chip_rv_plic_testplan.hjson` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `chip_rv_plic_testplan.hjson` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `chip_rv_plic_testplan.hjson` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `chip_rv_plic_testplan.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `chip_rv_plic_testplan.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `chip_rv_plic_testplan.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |

## Retrieval Guidance

- For code-only queries mentioning `chip_rv_plic_testplan.hjson`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `chip_rv_plic_testplan.hjson`.
