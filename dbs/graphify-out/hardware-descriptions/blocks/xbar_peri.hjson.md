# Hardware Description: xbar_peri.hjson

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **clock primary**: type: "xbar",
- **other clock list**: type: "xbar",
- **reset primary**: type: "xbar",

## Identity

- `ip_block`: `xbar_peri.hjson`
- `bridge_edge_count`: 48
- Spec categories: document: 81
- Code categories: rtl: 36, dv: 12
- Bridge relations: spec_path_matches_code_path: 48

## Spec Excerpts

### clock primary
_Source: `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{ name: "peri",
  type: "xbar",
  clock_primary: "clk_peri_i", // Main clock, used in sockets
  other_clock_list: [] // Secondary clocks used by specific nodes
  reset_primary: "rst_peri_ni", // Main reset, used in sockets
  other
…
```

### other clock list
_Source: `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{ name: "peri",
  type: "xbar",
  clock_primary: "clk_peri_i", // Main clock, used in sockets
  other_clock_list: [] // Secondary clocks used by specific nodes
  reset_primary: "rst_peri_ni", // Main reset, used in sockets
  other
…
```

### reset primary
_Source: `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{ name: "peri",
  type: "xbar",
  clock_primary: "clk_peri_i", // Main clock, used in sockets
  other_clock_list: [] // Secondary clocks used by specific nodes
  reset_primary: "rst_peri_ni", // Main reset, used in sockets
  other
…
```

### clock primary
_Source: `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{ name: "peri",
  type: "xbar",
  clock_primary: "clk_peri_i", // Main clock, used in sockets
  other_clock_list: [] // Secondary clocks used by specific nodes
  reset_primary: "rst_peri_ni", // Main reset, used in sockets
  other
…
```

### other clock list
_Source: `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{ name: "peri",
  type: "xbar",
  clock_primary: "clk_peri_i", // Main clock, used in sockets
  other_clock_list: [] // Secondary clocks used by specific nodes
  reset_primary: "rst_peri_ni", // Main reset, used in sockets
  other
…
```

### reset primary
_Source: `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{ name: "peri",
  type: "xbar",
  clock_primary: "clk_peri_i", // Main clock, used in sockets
  other_clock_list: [] // Secondary clocks used by specific nodes
  reset_primary: "rst_peri_ni", // Main reset, used in sockets
  other
…
```

### clock primary
_Source: `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{ name: "peri",
  type: "xbar",
  clock_primary: "clk_peri_i", // Main clock, used in sockets
  other_clock_list: [ "clk_spi_host0_i", "clk_usb_i" ] // Secondary clocks used by specific nodes
  reset_primary: "rst_peri_ni", // Mai
…
```

### other clock list
_Source: `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{ name: "peri",
  type: "xbar",
  clock_primary: "clk_peri_i", // Main clock, used in sockets
  other_clock_list: [ "clk_spi_host0_i", "clk_usb_i" ] // Secondary clocks used by specific nodes
  reset_primary: "rst_peri_ni", // Mai
…
```

## Spec Anchors

- `xbar_peri.hjson` (L1) — `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `clock primary` (L6) — `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `other clock list` (L7) — `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `reset primary` (L8) — `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `other reset list` (L9) — `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `nodes` (L11) — `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `addr space` (L14) — `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `clock` (L15) — `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `xbar` (L17) — `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `pipeline` (L18) — `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `connections` (L136) — `opentitan/hw/top_darjeeling/data/xbar_peri.hjson`
- `xbar_peri.hjson` (L1) — `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `clock primary` (L6) — `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `other clock list` (L7) — `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `reset primary` (L8) — `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `other reset list` (L9) — `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `nodes` (L11) — `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `addr space` (L14) — `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `clock` (L15) — `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `xbar` (L17) — `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `pipeline` (L18) — `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `connections` (L184) — `opentitan/hw/top_earlgrey/data/xbar_peri.hjson`
- `xbar_peri.hjson` (L1) — `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `clock primary` (L6) — `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `other clock list` (L7) — `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `reset primary` (L8) — `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `other reset list` (L9) — `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `nodes` (L11) — `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `addr space` (L14) — `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `clock` (L15) — `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `xbar` (L17) — `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `pipeline` (L18) — `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`
- `connections` (L94) — `opentitan/hw/top_englishbreakfast/data/xbar_peri.hjson`

## Code Evidence

**RTL** (28)
  - `prim_flop_en`:L269 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
  - `prim_ram_1p_adv`:L1487 — `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
  - `tlul_cmd_intg_gen`:L46 — `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv`
  - `dma`:L2221 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `keymgr_dpe`:L1905 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `tlul_jtag_dtm`:L1340 — `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
  - `mbx`:L2257 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `prim_onehot_enc`:L128 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
  - `tlul_fifo_async`:L212 — `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv`
  - `tl_peri_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\tl_peri_pkg.sv`
  - `xbar_peri.sv`:L1 — `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv`
  - `xbar_peri`:L31 — `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv`
  - `prim_alert_sender`:L268 — `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
  - `prim_alert_pkg`:L11 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `prim_esc_pkg`:L12 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `prim_secded_inv_72_64_enc`:L39 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv`
  - `prim_sec_anchor_flop`:L275 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv`
  - `prim_packer_fifo`:L233 — `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv`
  - `adc_ctrl`:L2047 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
  - `csrng`:L2617 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
**DV** (4)
  - `tb__xbar_connect.sv`:L1 — `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\tb__xbar_connect.sv`
  - `xbar_env_pkg__params.sv`:L1 — `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_env_pkg__params.sv`
  - `xbar_peri_bind.sv`:L1 — `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv`
  - `xbar_peri_bind`:L6 — `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tlul_fifo_async` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\tb__xbar_connect.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri_bind` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tl_peri_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\tl_peri_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tlul_fifo_async` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\tb__xbar_connect.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri_bind` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tl_peri_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\tl_peri_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `BUFG` | `opentitan\hw\top_englishbreakfast\rtl\clkgen_xil7series.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_mubi_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_esc_receiver` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_arbiter_fixed` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_arbiter_tree` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_count` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_secded_hamming_72_64_enc` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `prim_secded_hamming_76_68_enc` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tlul_fifo_async` | `opentitan\hw\top_englishbreakfast\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\tb__xbar_connect.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri_bind` | `opentitan\hw\top_darjeeling\ip\xbar_peri\dv\autogen\xbar_peri_bind.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `tl_peri_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\tl_peri_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri.sv` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |
| `spec_path_matches_code_path` | `xbar_peri.hjson` | `xbar_peri` | `opentitan\hw\top_darjeeling\ip\xbar_peri\rtl\autogen\xbar_peri.sv` |

## Retrieval Guidance

- For code-only queries mentioning `xbar_peri.hjson`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `xbar_peri.hjson`.
