# Hardware Description: xbar_dbg.hjson

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **clock primary**: type: "xbar",
- **other clock list**: type: "xbar",
- **reset primary**: type: "xbar",

## Identity

- `ip_block`: `xbar_dbg.hjson`
- `bridge_edge_count`: 16
- Spec categories: document: 27
- Code categories: rtl: 12, dv: 4
- Bridge relations: spec_path_matches_code_path: 16

## Spec Excerpts

### clock primary
_Source: `opentitan/hw/top_darjeeling/data/xbar_dbg.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{ name: "dbg",
  type: "xbar",
  clock_primary: "clk_dbg_i", // Main clock, used in sockets
  other_clock_list: [ "clk_peri_i" ], // Secondary clocks used by specific nodes
  reset_primary: "rst_dbg_ni", // Main reset, used in soc
…
```

### other clock list
_Source: `opentitan/hw/top_darjeeling/data/xbar_dbg.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{ name: "dbg",
  type: "xbar",
  clock_primary: "clk_dbg_i", // Main clock, used in sockets
  other_clock_list: [ "clk_peri_i" ], // Secondary clocks used by specific nodes
  reset_primary: "rst_dbg_ni", // Main reset, used in soc
…
```

### reset primary
_Source: `opentitan/hw/top_darjeeling/data/xbar_dbg.hjson`_

```
// Copyright lowRISC contributors (OpenTitan project).
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0
{ name: "dbg",
  type: "xbar",
  clock_primary: "clk_dbg_i", // Main clock, used in sockets
  other_clock_list: [ "clk_peri_i" ], // Secondary clocks used by specific nodes
  reset_primary: "rst_dbg_ni", // Main reset, used in soc
…
```

## Spec Anchors

- `xbar_dbg.hjson` (L1) — `opentitan/hw/top_darjeeling/data/xbar_dbg.hjson`
- `clock primary` (L6) — `opentitan/hw/top_darjeeling/data/xbar_dbg.hjson`
- `other clock list` (L7) — `opentitan/hw/top_darjeeling/data/xbar_dbg.hjson`
- `reset primary` (L8) — `opentitan/hw/top_darjeeling/data/xbar_dbg.hjson`
- `other reset list` (L9) — `opentitan/hw/top_darjeeling/data/xbar_dbg.hjson`
- `nodes` (L11) — `opentitan/hw/top_darjeeling/data/xbar_dbg.hjson`
- `addr space` (L14) — `opentitan/hw/top_darjeeling/data/xbar_dbg.hjson`
- `clock` (L15) — `opentitan/hw/top_darjeeling/data/xbar_dbg.hjson`
- `xbar` (L17) — `opentitan/hw/top_darjeeling/data/xbar_dbg.hjson`
- `pipeline` (L18) — `opentitan/hw/top_darjeeling/data/xbar_dbg.hjson`
- `connections` (L46) — `opentitan/hw/top_darjeeling/data/xbar_dbg.hjson`

## Code Evidence

**RTL** (12)
  - `prim_flop_en`:L269 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
  - `prim_ram_1p_adv`:L1487 — `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
  - `tlul_cmd_intg_gen`:L46 — `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv`
  - `dma`:L2221 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `keymgr_dpe`:L1905 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `tlul_jtag_dtm`:L1340 — `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
  - `mbx`:L2257 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `prim_onehot_enc`:L128 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
  - `tl_dbg_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\tl_dbg_pkg.sv`
  - `xbar_dbg.sv`:L1 — `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\xbar_dbg.sv`
  - `xbar_dbg`:L18 — `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\xbar_dbg.sv`
  - `tl_dbg_pkg`:L42 — `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\xbar_dbg.sv`
**DV** (4)
  - `tb__xbar_connect.sv`:L1 — `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\tb__xbar_connect.sv`
  - `xbar_dbg_bind.sv`:L1 — `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\xbar_dbg_bind.sv`
  - `xbar_dbg_bind`:L6 — `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\xbar_dbg_bind.sv`
  - `xbar_env_pkg__params.sv`:L1 — `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\xbar_env_pkg__params.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `tb__xbar_connect.sv` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\tb__xbar_connect.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `xbar_dbg_bind.sv` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\xbar_dbg_bind.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `xbar_dbg_bind` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\xbar_dbg_bind.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `xbar_env_pkg__params.sv` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\dv\autogen\xbar_env_pkg__params.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `tl_dbg_pkg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\tl_dbg_pkg.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `xbar_dbg.sv` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\xbar_dbg.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `xbar_dbg` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\xbar_dbg.sv` |
| `spec_path_matches_code_path` | `xbar_dbg.hjson` | `tl_dbg_pkg` | `opentitan\hw\top_darjeeling\ip\xbar_dbg\rtl\autogen\xbar_dbg.sv` |

## Retrieval Guidance

- For code-only queries mentioning `xbar_dbg.hjson`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `xbar_dbg.hjson`.
