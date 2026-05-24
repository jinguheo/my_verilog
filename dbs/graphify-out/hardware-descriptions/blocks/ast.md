# Hardware Description: ast

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Interface Signals**: Naming here is compliant with the OpenTitan [names](https://github.com/lowRISC/style-guides/blob/master/VerilogCodingStyle.md#naming) and [suffixes](https://github.com/lowRISC/style-…
- **Table notes**: Naming here is compliant with the OpenTitan [names](https://github.com/lowRISC/style-guides/blob/master/VerilogCodingStyle.md#naming) and [suffixes](https://github.com/lowRISC/style-…
- **Signal naming conventions used in this document**: Naming here is compliant with the OpenTitan [names](https://github.com/lowRISC/style-guides/blob/master/VerilogCodingStyle.md#naming) and [suffixes](https://github.com/lowRISC/style-…

## Identity

- `ip_block`: `ast`
- `bridge_edge_count`: 95
- Spec categories: document: 60, component: 41, interface: 21, testplan: 2
- Code categories: rtl: 235
- Bridge relations: spec_path_matches_code_path: 55, spec_component_matches_code: 40

## Spec Excerpts

### Interface Signals
_Source: `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`_

```
# Interface Signals

## Table notes

### Signal naming conventions used in this document

Naming here is compliant with the OpenTitan [names](https://github.com/lowRISC/style-guides/blob/master/VerilogCodingStyle.md#naming) and [suffixes](https://github.com/lowRISC/style-guides/blob/master/VerilogCodingStyle.md#suffixes) specification, with the following augmentations:
```

### Table notes
_Source: `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`_

```
# Interface Signals

## Table notes

### Signal naming conventions used in this document

Naming here is compliant with the OpenTitan [names](https://github.com/lowRISC/style-guides/blob/master/VerilogCodingStyle.md#naming) and [suffixes](https://github.com/lowRISC/style-guides/blob/master/VerilogCodingStyle.md#suffixes) specification, with the following augmentations:

- Clock signals start with
…
```

### Signal naming conventions used in this document
_Source: `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`_

```
# Interface Signals

## Table notes

### Signal naming conventions used in this document

Naming here is compliant with the OpenTitan [names](https://github.com/lowRISC/style-guides/blob/master/VerilogCodingStyle.md#naming) and [suffixes](https://github.com/lowRISC/style-guides/blob/master/VerilogCodingStyle.md#suffixes) specification, with the following augmentations:

- Clock signals start with
…
```

### OpenTitan Earl Grey Discrete Chip Datasheet
_Source: `opentitan/hw/top_earlgrey/doc/datasheet.md`_

```
# OpenTitan Earl Grey (Discrete Chip) Datasheet

# Overview

![Top Level Block Diagram](top_earlgrey_block_diagram.svg)

The OpenTitan Earl Grey chip is a low-power secure microcontroller that is designed for several use cases requiring hardware security.
The block diagram is shown above and shows the system configuration, including the Ibex processor and all of the memories and comportable IPs.
```

### Overview
_Source: `opentitan/hw/top_earlgrey/doc/datasheet.md`_

```
# OpenTitan Earl Grey (Discrete Chip) Datasheet

# Overview

![Top Level Block Diagram](top_earlgrey_block_diagram.svg)

The OpenTitan Earl Grey chip is a low-power secure microcontroller that is designed for several use cases requiring hardware security.
The block diagram is shown above and shows the system configuration, including the Ibex processor and all of the memories and comportable IPs.
…
```

### Detailed Specification
_Source: `opentitan/hw/top_earlgrey/doc/datasheet.md`_

```
</ul>
        </li>
      </ul>
    </td>
  </tr>
</tbody>
</table>

# Detailed Specification

For more detailed documentation including the pinout and system address map, see [OpenTitan Earl Grey Chip Specification](./design/README.md).
The [OpenTitan Earl Grey Chip DV Document](../dv/README.md) describes the chip-level DV environment and contains the chip-level test plan.
```

### OpenTitan Earl Grey Chip Specification
_Source: `opentitan/hw/top_earlgrey/doc/design/README.md`_

```
# OpenTitan Earl Grey Chip Specification

This document describes the OpenTitan Earl Grey chip functionality in detail.
For an overview, refer to the [OpenTitan Earl Grey Chip Datasheet](../datasheet.md).

# Theory of Operations

The netlist `chip_earlgrey_asic` contains the features listed above and is intended for ASIC synthesis, whereas the netlist `chip_earlgrey_cw310` provides an emulation en
…
```

### Theory of Operations
_Source: `opentitan/hw/top_earlgrey/doc/design/README.md`_

```
# OpenTitan Earl Grey Chip Specification

This document describes the OpenTitan Earl Grey chip functionality in detail.
For an overview, refer to the [OpenTitan Earl Grey Chip Datasheet](../datasheet.md).

# Theory of Operations

The netlist `chip_earlgrey_asic` contains the features listed above and is intended for ASIC synthesis, whereas the netlist `chip_earlgrey_cw310` provides an emulation en
…
```

## Spec Anchors

- `component:ast` (L1) — `__graphify_spec_only__/components.md`
- `ast.hjson` (L1) — `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `cip id` (L10) — `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `design spec` (L11) — `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `dv doc` (L12) — `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `hw checklist` (L13) — `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `sw checklist` (L14) — `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `version` (L15) — `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `life stage` (L16) — `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `design stage` (L17) — `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `verification stage` (L18) — `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `dif stage` (L19) — `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `ast.hjson` (L1) — `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `cip id` (L10) — `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `design spec` (L11) — `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `dv doc` (L12) — `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `hw checklist` (L13) — `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `sw checklist` (L14) — `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `version` (L15) — `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `life stage` (L16) — `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `design stage` (L17) — `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `verification stage` (L18) — `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `dif stage` (L19) — `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `interfaces.md` (L1) — `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`
- `Interface Signals` (L1) — `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`
- `Table notes` (L3) — `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`
- `Signal naming conventions used in this document` (L5) — `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`
- `Clock domains column` (L15) — `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`
- `Table` (L26) — `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`
- `top_earlgrey.gen.hjson` (L1) — `opentitan/hw/top_earlgrey/data/autogen/top_earlgrey.gen.hjson`
- `top_earlgrey.secrets.testing.gen.hjson` (L1) — `opentitan/hw/top_earlgrey/data/autogen/top_earlgrey.secrets.testing.gen.hjson`
- `chip_conn_testplan.hjson` (L1) — `opentitan/hw/top_earlgrey/data/chip_conn_testplan.hjson`
- `chip_testplan.hjson` (L1) — `opentitan/hw/top_earlgrey/data/chip_testplan.hjson`
- `top_earlgrey.hjson` (L1) — `opentitan/hw/top_earlgrey/data/top_earlgrey.hjson`
- `top_earlgrey_seed.testing.hjson` (L1) — `opentitan/hw/top_earlgrey/data/top_earlgrey_seed.testing.hjson`

## Code Evidence

**RTL** (50)
  - `prim_packer_fifo`:L233 — `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv`
  - `aon_clk.sv`:L1 — `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_clk.sv`
  - `aon_clk`:L9 — `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_clk.sv`
  - `aon_osc.sv`:L1 — `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_osc.sv`
  - `aon_osc`:L9 — `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_osc.sv`
  - `ast.sv`:L1 — `opentitan\hw\top_darjeeling\ip\ast\rtl\ast.sv`
  - `ast`:L12 — `opentitan\hw\top_darjeeling\ip\ast\rtl\ast.sv`
  - `ast_pkg`:L159 — `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv`
  - `ast_reg_pkg`:L22 — `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_reg_top.sv`
  - `ast_bhv_pkg`:L161 — `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv`
  - `rglts_pdm_3p3v`:L309 — `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv`
  - `rng`:L665 — `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv`
  - `ast_alert`:L697 — `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv`
  - `ast_reg_top`:L837 — `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv`
  - `ast_dft`:L906 — `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv`
  - `ast_alert.sv`:L1 — `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_alert.sv`
  - `ast_alert`:L9 — `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_alert.sv`
  - `ast_bhv_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_bhv_pkg.sv`
  - `ast_dft.sv`:L1 — `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_dft.sv`
  - `ast_dft`:L11 — `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_dft.sv`

## Neighbor Components

- `rstmgr` (20 refs; instantiates×20)
- `rv_plic` (18 refs; instantiates×18)
- `lowrisc_ibex` (16 refs; instantiates×16)
- `pulp_riscv_dbg` (16 refs; instantiates×16)
- `prim` (2 refs; instantiates×2)
- `spi_host` (2 refs; instantiates×2)
- `csrng` (1 refs; instantiates×1)
- `edn` (1 refs; instantiates×1)
- `entropy_src` (1 refs; instantiates×1)
- `kmac` (1 refs; instantiates×1)
- `gpio` (1 refs; imports_from×1)
- `clkmgr` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:ast` | `ast` | `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pulse_sync.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_pulse_sync.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_clks_byp.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_clks_byp.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_pkg` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_reg_top.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_bhv_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_bhv_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_entropy.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_entropy.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_reg_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_top.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_reg_top.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_top` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_reg_top.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_alert.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_alert.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pulse_sync.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_pulse_sync.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pulse_sync` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_pulse_sync.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_dft.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_dft.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pulse_sync.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_pulse_sync.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pulse_sync` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_pulse_sync.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_bhv_pkg.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_bhv_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_entropy.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_entropy.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_entropy` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_entropy.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_pkg.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_reg_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_top.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_reg_top.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_top` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_reg_top.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_clks_byp.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_clks_byp.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_clks_byp` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_clks_byp.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_alert.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_alert.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_alert` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_alert.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_bhv_pkg.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_bhv_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_entropy.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_entropy.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_entropy` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_entropy.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_reg_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_top.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_reg_top.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_top` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_reg_top.sv` |
| `spec_component_matches_code` | `component:ast` | `ast.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_dft.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_dft.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_dft` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_dft.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pkg.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_alert.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_alert.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_alert` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_alert.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pulse_sync` | `opentitan\hw\top_earlgrey\ip\ast\rtl\usb_clk.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_dft.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_dft.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `aon_clk.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_clk.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `aon_clk` | `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_clk.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `aon_osc.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_osc.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `aon_osc` | `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_osc.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `ast.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `ast` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `ast_pkg` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv` |
| `spec_path_matches_code_path` | `top_earlgrey.gen.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `top_earlgrey.secrets.testing.gen.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `chip_conn_testplan.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `chip_testplan.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |

## Retrieval Guidance

- For code-only queries mentioning `ast`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `ast`.
