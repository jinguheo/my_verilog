# Hardware Description: sensor_ctrl

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`sensor_ctrl`** has the following hardware interfaces defined
- **Peripheral Pins for Chip IO**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`sensor_ctrl`** has the following hardware interfaces defined
- **Inter-Module Signals**: - Security Countermeasures: *none*

## Identity

- `ip_block`: `sensor_ctrl`
- `bridge_edge_count`: 113
- Spec categories: document: 99, interface: 22, theory: 20, component: 15, testplan: 2
- Code categories: rtl: 120, other_code: 3
- Bridge relations: spec_path_matches_code_path: 99, spec_component_matches_code: 14

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`sensor_ctrl`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_ao
…
```

### Peripheral Pins for Chip IO
_Source: `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`sensor_ctrl`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_aon_i`**
- Bus Device Int
…
```

### Inter-Module Signals
_Source: `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`_

```
- Security Countermeasures: *none*

## Peripheral Pins for Chip IO

| Pin name           | Direction   | Description                 |
|:-------------------|:------------|:----------------------------|
| ast_debug_out[8:0] | output      | ast debug outputs to pinmux |

## [Inter-Module Signals](https://opentitan.org/book/doc/contributing/hw/comportability/index.html#inter-signal-handling)

| Port
…
```

### Programmer's Guide
_Source: `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

Each available alert has a corresponding fatality configuration.
If an alert event is set to 1 in [`FATAL_ALERT_EN`](registers.md#fatal_alert_en), `sensor control` treats it as a fatal event instead of a recoverable event.
Fatal events are not acknowledged, and continuously send alert events in the system until some kind of escalation is seen.

## Device Interface Functions (
…
```

### Device Interface Functions DIFs
_Source: `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

Each available alert has a corresponding fatality configuration.
If an alert event is set to 1 in [`FATAL_ALERT_EN`](registers.md#fatal_alert_en), `sensor control` treats it as a fatal event instead of a recoverable event.
Fatal events are not acknowledged, and continuously send alert events in the system until some kind of escalation is seen.

## Device Interface Functions (
…
```

### Summary
_Source: `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson -->
## Summary

| Name                                                              | Offset   |   Length | Description                                                                   |
|:------------------------------------------------------------------|:---------|---------:|:--------------
…
```

### INTR STATE
_Source: `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`_

```
| sensor_ctrl.[`MANUAL_PAD_ATTR_REGWEN_1`](#manual_pad_attr_regwen) | 0x58     |        4 | Register write enable for attributes of manual pads                           |
| sensor_ctrl.[`MANUAL_PAD_ATTR_REGWEN_2`](#manual_pad_attr_regwen) | 0x5c     |        4 | Register write enable for attributes of manual pads                           |
| sensor_ctrl.[`MANUAL_PAD_ATTR_REGWEN_3`](#manual_pad_a
…
```

### Fields
_Source: `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`_

```
| sensor_ctrl.[`MANUAL_PAD_ATTR_3`](#manual_pad_attr)               | 0x70     |        4 | Attributes of manual pads.                                                    |

## INTR_STATE
Interrupt State Register
- Offset: `0x0`
- Reset default: `0x0`
- Reset mask: `0x3`

### Fields

```wavejson
{"reg": [{"name": "io_status_change", "bits": 1, "attr": ["rw1c"], "rotate": -90}, {"name": "init_status
…
```

## Spec Anchors

- `component:sensor_ctrl` (L1) — `__graphify_spec_only__/components.md`
- `sensor_ctrl.hjson` (L1) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `cip id` (L10) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `design spec` (L11) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `dv doc` (L12) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `hw checklist` (L13) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `sw checklist` (L14) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `revisions` (L15) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `version` (L17) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `life stage` (L18) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `design stage` (L19) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `verification stage` (L21) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `checklist.md` (L1) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `SENSOR CTRL Checklist` (L1) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `D2` (L32) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `D2S` (L74) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `D3` (L94) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `Verification Checklist` (L120) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `interfaces.md` (L1) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`
- `Hardware Interfaces` (L1) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`
- `Peripheral Pins for Chip IO` (L11) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`
- `Inter-Module Signals` (L17) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`
- `Interrupts` (L29) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`
- `Security Alerts` (L36) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`
- `programmers_guide.md` (L1) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/programmers_guide.md`
- `Programmer's Guide` (L1) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/programmers_guide.md`
- `Device Interface Functions DIFs` (L7) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/programmers_guide.md`
- `registers.md` (L1) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`
- `Registers` (L1) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`
- `Summary` (L4) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`
- `INTR STATE` (L38) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`
- `Fields` (L44) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`
- `INTR ENABLE` (L56) — `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`

## Code Evidence

**RTL** (18)
  - `prim_alert_sender`:L268 — `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
  - `sensor_ctrl.sv`:L1 — `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
  - `sensor_ctrl`:L9 — `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
  - `sensor_ctrl_pkg`:L10 — `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
  - `sensor_ctrl_reg_pkg`:L22 — `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv`
  - `sensor_ctrl_reg_top`:L105 — `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
  - `sensor_ctrl_pkg.sv`:L1 — `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_pkg.sv`
  - `sensor_ctrl_reg_pkg.sv`:L1 — `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_pkg.sv`
  - `sensor_ctrl_reg_top.sv`:L1 — `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv`
  - `sensor_ctrl_reg_top`:L9 — `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv`
  - `sensor_ctrl`:L2194 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
  - `prim_alert_pkg`:L11 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `prim_esc_pkg`:L12 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `prim_secded_inv_72_64_enc`:L39 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv`
  - `prim_sec_anchor_flop`:L275 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv`
  - `prim_packer_fifo`:L233 — `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv`
  - `adc_ctrl`:L2047 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
  - `csrng`:L2617 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
**OTHER_CODE** (3)
  - `sensor_ctrl.c`:L1 — `opentitan\sw\device\silicon_creator\lib\drivers\sensor_ctrl.c`
  - `sensor_ctrl_configure()`:L27 — `opentitan\sw\device\silicon_creator\lib\drivers\sensor_ctrl.c`
  - `sensor_ctrl.h`:L1 — `opentitan\sw\device\silicon_creator\lib\drivers\sensor_ctrl.h`

## Neighbor Components

- `prim` (12 refs; instantiates×12)
- `rv_plic` (6 refs; instantiates×6)
- `rv_core_ibex` (2 refs; imports_from×1, instantiates×1)
- `keymgr` (1 refs; instantiates×1)
- `keymgr_dpe` (1 refs; instantiates×1)
- `sram_ctrl` (1 refs; instantiates×1)
- `soc_proxy` (1 refs; instantiates×1)
- `pulp_riscv_dbg` (1 refs; instantiates×1)
- `pwrmgr` (1 refs; instantiates×1)
- `clkmgr` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_reg_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_reg_top.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_reg_top` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_reg_top` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl.c` | `opentitan\sw\device\silicon_creator\lib\drivers\sensor_ctrl.c` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_configure()` | `opentitan\sw\device\silicon_creator\lib\drivers\sensor_ctrl.c` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl.h` | `opentitan\sw\device\silicon_creator\lib\drivers\sensor_ctrl.h` |
| `spec_path_matches_code_path` | `top_earlgrey.gen.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `top_earlgrey.secrets.testing.gen.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `chip_conn_testplan.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `chip_testplan.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `top_earlgrey.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `top_earlgrey_seed.testing.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `datasheet.md` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `memory_map.md` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `sensor_ctrl.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `sensor_ctrl` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `sensor_ctrl_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `sensor_ctrl_reg_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `sensor_ctrl_reg_top` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `sensor_ctrl_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_pkg.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `sensor_ctrl_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_pkg.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sensor_ctrl.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sensor_ctrl` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sensor_ctrl_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sensor_ctrl_reg_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sensor_ctrl_reg_top` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sensor_ctrl_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sensor_ctrl_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sensor_ctrl.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sensor_ctrl` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sensor_ctrl_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sensor_ctrl_reg_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sensor_ctrl_reg_top` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sensor_ctrl_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_pkg.sv` |

## Retrieval Guidance

- For code-only queries mentioning `sensor_ctrl`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `sensor_ctrl`.
