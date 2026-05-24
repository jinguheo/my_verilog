# Hardware Description: mbx

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **OpenTitan-defined DOE objects**: Please refer to the following pages for additional details on the DMA controller.
- **Simple DMA transfer request**: Please refer to the following pages for additional details on the DMA controller.
- **Simple DMA completion response object**: Destination Address High (Used only if targeting 64

## Identity

- `ip_block`: `mbx`
- `bridge_edge_count`: 117
- Spec categories: document: 103, component: 38, testplan: 27, theory: 19, interface: 16
- Code categories: dv: 72, rtl: 57, sva: 24
- Bridge relations: spec_path_matches_code_path: 80, spec_component_matches_code: 37

## Spec Excerpts

### OpenTitan-defined DOE objects
_Source: `opentitan/hw/ip/mbx/doc/DOE.md`_

```
# OpenTitan-defined DOE objects

Please refer to the following pages for additional details on the DMA controller.
- [OpenTitan DMA Controller specification](../../dma/README.md)

## Simple DMA transfer request

Requester specifies Source address, Destination address, source space ID and Destination space ID as required by the DMA transfer operation.
```

### Simple DMA transfer request
_Source: `opentitan/hw/ip/mbx/doc/DOE.md`_

```
# OpenTitan-defined DOE objects

Please refer to the following pages for additional details on the DMA controller.
- [OpenTitan DMA Controller specification](../../dma/README.md)

## Simple DMA transfer request

Requester specifies Source address, Destination address, source space ID and Destination space ID as required by the DMA transfer operation.
Integrated OpenTitan Host firmware parses the o
…
```

### Simple DMA completion response object
_Source: `opentitan/hw/ip/mbx/doc/DOE.md`_

```
Destination Address High (Used only if targeting 64
bit address space; else all zero)

</td>
<td markdown="1" class="c109" colspan="1" rowspan="1">0x1C</td>
</tr>
</table>

## Simple DMA completion response object

DMA transfer completion response to the requester.
Response object conveys the status of the operation.

<table markdown="1" class="c80">
<tr markdown="1" class="c5">
<td markdown="1" c
…
```

### Hardware Interfaces
_Source: `opentitan/hw/ip/mbx/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/mbx/data/mbx.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`mbx`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`cor
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/mbx/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/mbx/data/mbx.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`mbx`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`core_tl_d`**, **`soc_tl_d`
…
```

### Interrupts
_Source: `opentitan/hw/ip/mbx/doc/interfaces.md`_

```
| doe_intr              | logic                         | uni     | req   |       1 |                                                                                                                                      |
| doe_async_msg_support | logic                         | uni     | req   |       1 |
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/mbx/doc/programmers_guide.md`_

```
# Programmer's Guide

In a typical use case there are two software agents involved in the mailbox communication:

- RoT firmware configures the mailbox IP block and awaits requests from the SoC side.
- SoC-side software makes requests of the RoT firmware and awaits its responses.

A note on terminology: The request is received from the SoC side into an _Inbox_ on the RoT and the response is deposi
…
```

### Initialization
_Source: `opentitan/hw/ip/mbx/doc/programmers_guide.md`_

```
- RoT firmware configures the mailbox IP block and awaits requests from the SoC side.
- SoC-side software makes requests of the RoT firmware and awaits its responses.

A note on terminology: The request is received from the SoC side into an _Inbox_ on the RoT and the response is deposited into the _Outbox_ by the RoT, i.e. the mailbox directions are named from the perspective of the RoT.

Each of
…
```

## Spec Anchors

- `component:mbx` (L1) — `__graphify_spec_only__/components.md`
- `mbx.hjson` (L1) — `opentitan/hw/ip/mbx/data/mbx.hjson`
- `human name` (L8) — `opentitan/hw/ip/mbx/data/mbx.hjson`
- `one line desc` (L9) — `opentitan/hw/ip/mbx/data/mbx.hjson`
- `one paragraph desc` (L10) — `opentitan/hw/ip/mbx/data/mbx.hjson`
- `cip id` (L15) — `opentitan/hw/ip/mbx/data/mbx.hjson`
- `design spec` (L16) — `opentitan/hw/ip/mbx/data/mbx.hjson`
- `dv doc` (L17) — `opentitan/hw/ip/mbx/data/mbx.hjson`
- `version` (L18) — `opentitan/hw/ip/mbx/data/mbx.hjson`
- `clocking` (L20) — `opentitan/hw/ip/mbx/data/mbx.hjson`
- `bus interfaces` (L21) — `opentitan/hw/ip/mbx/data/mbx.hjson`
- `inter signal list` (L26) — `opentitan/hw/ip/mbx/data/mbx.hjson`
- `mbx_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/mbx/data/mbx_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/mbx/data/mbx_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/mbx/data/mbx_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/mbx/data/mbx_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/mbx/data/mbx_sec_cm_testplan.hjson`
- `mbx_testplan.hjson` (L1) — `opentitan/hw/ip/mbx/data/mbx_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/mbx/data/mbx_testplan.hjson`
- `testpoints` (L14) — `opentitan/hw/ip/mbx/data/mbx_testplan.hjson`
- `desc` (L16) — `opentitan/hw/ip/mbx/data/mbx_testplan.hjson`
- `stage` (L27) — `opentitan/hw/ip/mbx/data/mbx_testplan.hjson`
- `tests` (L28) — `opentitan/hw/ip/mbx/data/mbx_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/mbx/doc/checklist.md`
- `Mailbox Checklist` (L1) — `opentitan/hw/ip/mbx/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/mbx/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/mbx/doc/checklist.md`
- `D2` (L34) — `opentitan/hw/ip/mbx/doc/checklist.md`
- `D2S` (L76) — `opentitan/hw/ip/mbx/doc/checklist.md`
- `D3` (L96) — `opentitan/hw/ip/mbx/doc/checklist.md`
- `Verification Checklist` (L122) — `opentitan/hw/ip/mbx/doc/checklist.md`
- `V1` (L124) — `opentitan/hw/ip/mbx/doc/checklist.md`
- `V2` (L174) — `opentitan/hw/ip/mbx/doc/checklist.md`
- `V2S` (L220) — `opentitan/hw/ip/mbx/doc/checklist.md`
- `DOE.md` (L1) — `opentitan/hw/ip/mbx/doc/DOE.md`

## Code Evidence

**RTL** (29)
  - `mbx.sv`:L1 — `opentitan\hw\ip\mbx\rtl\mbx.sv`
  - `mbx`:L7 — `opentitan\hw\ip\mbx\rtl\mbx.sv`
  - `mbx_reg_pkg`:L9 — `opentitan\hw\ip\mbx\rtl\mbx_sysif.sv`
  - `mbx_hostif`:L124 — `opentitan\hw\ip\mbx\rtl\mbx.sv`
  - `mbx_sysif`:L224 — `opentitan\hw\ip\mbx\rtl\mbx.sv`
  - `mbx_imbx`:L282 — `opentitan\hw\ip\mbx\rtl\mbx.sv`
  - `mbx_ombx`:L317 — `opentitan\hw\ip\mbx\rtl\mbx.sv`
  - `mbx_sramrwarb`:L361 — `opentitan\hw\ip\mbx\rtl\mbx.sv`
  - `mbx_core_reg_top.sv`:L1 — `opentitan\hw\ip\mbx\rtl\mbx_core_reg_top.sv`
  - `mbx_core_reg_top`:L9 — `opentitan\hw\ip\mbx\rtl\mbx_core_reg_top.sv`
  - `mbx_fsm.sv`:L1 — `opentitan\hw\ip\mbx\rtl\mbx_fsm.sv`
  - `mbx_fsm`:L7 — `opentitan\hw\ip\mbx\rtl\mbx_fsm.sv`
  - `mbx_hostif.sv`:L1 — `opentitan\hw\ip\mbx\rtl\mbx_hostif.sv`
  - `mbx_hostif`:L7 — `opentitan\hw\ip\mbx\rtl\mbx_hostif.sv`
  - `mbx_core_reg_top`:L111 — `opentitan\hw\ip\mbx\rtl\mbx_hostif.sv`
  - `mbx_imbx.sv`:L1 — `opentitan\hw\ip\mbx\rtl\mbx_imbx.sv`
  - `mbx_imbx`:L7 — `opentitan\hw\ip\mbx\rtl\mbx_imbx.sv`
  - `mbx_fsm`:L250 — `opentitan\hw\ip\mbx\rtl\mbx_ombx.sv`
  - `mbx_ombx.sv`:L1 — `opentitan\hw\ip\mbx\rtl\mbx_ombx.sv`
  - `mbx_ombx`:L7 — `opentitan\hw\ip\mbx\rtl\mbx_ombx.sv`
**DV** (6)
  - `tb.sv`:L1 — `opentitan\hw\ip\mbx\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\mbx\dv\tb.sv`
  - `mbx_env_pkg`:L9 — `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv`
  - `mbx_test_pkg`:L10 — `opentitan\hw\ip\mbx\dv\tb.sv`
  - `mbx_base_test.sv`:L1 — `opentitan\hw\ip\mbx\dv\tests\mbx_base_test.sv`
  - `mbx_test_pkg.sv`:L1 — `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv`
**SVA** (2)
  - `mbx_bind.sv`:L1 — `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv`
  - `mbx_bind`:L5 — `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv`

## Neighbor Components

- `rv_plic` (13 refs; instantiates×13)
- `lowrisc_ibex` (8 refs; instantiates×7, imports_from×1)
- `rv_core_ibex` (3 refs; instantiates×2, imports_from×1)
- `ac_range_check` (3 refs; instantiates×3)
- `pwrmgr` (3 refs; instantiates×3)
- `rstmgr` (1 refs; imports_from×1)
- `spi_host` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:mbx` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_base_test.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_base_test.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_env_pkg` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_test_pkg.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_core_reg_top.sv` | `opentitan\hw\ip\mbx\rtl\mbx_core_reg_top.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_core_reg_top` | `opentitan\hw\ip\mbx\rtl\mbx_core_reg_top.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_soc_reg_top.sv` | `opentitan\hw\ip\mbx\rtl\mbx_soc_reg_top.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_soc_reg_top` | `opentitan\hw\ip\mbx\rtl\mbx_soc_reg_top.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_sramrwarb.sv` | `opentitan\hw\ip\mbx\rtl\mbx_sramrwarb.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_sramrwarb` | `opentitan\hw\ip\mbx\rtl\mbx_sramrwarb.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_bind.sv` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_bind` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_reg_pkg.sv` | `opentitan\hw\ip\mbx\rtl\mbx_reg_pkg.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_hostif.sv` | `opentitan\hw\ip\mbx\rtl\mbx_hostif.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_hostif` | `opentitan\hw\ip\mbx\rtl\mbx_hostif.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_core_reg_top` | `opentitan\hw\ip\mbx\rtl\mbx_hostif.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_reg_pkg` | `opentitan\hw\ip\mbx\rtl\mbx_sysif.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_sysif.sv` | `opentitan\hw\ip\mbx\rtl\mbx_sysif.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_sysif` | `opentitan\hw\ip\mbx\rtl\mbx_sysif.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_soc_reg_top` | `opentitan\hw\ip\mbx\rtl\mbx_sysif.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_imbx.sv` | `opentitan\hw\ip\mbx\rtl\mbx_imbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_imbx` | `opentitan\hw\ip\mbx\rtl\mbx_imbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_fsm` | `opentitan\hw\ip\mbx\rtl\mbx_ombx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_ombx.sv` | `opentitan\hw\ip\mbx\rtl\mbx_ombx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_ombx` | `opentitan\hw\ip\mbx\rtl\mbx_ombx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_fsm.sv` | `opentitan\hw\ip\mbx\rtl\mbx_fsm.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_fsm` | `opentitan\hw\ip\mbx\rtl\mbx_fsm.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx.sv` | `opentitan\hw\ip\mbx\rtl\mbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx` | `opentitan\hw\ip\mbx\rtl\mbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_hostif` | `opentitan\hw\ip\mbx\rtl\mbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_sysif` | `opentitan\hw\ip\mbx\rtl\mbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_imbx` | `opentitan\hw\ip\mbx\rtl\mbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_ombx` | `opentitan\hw\ip\mbx\rtl\mbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_sramrwarb` | `opentitan\hw\ip\mbx\rtl\mbx.sv` |
| `spec_component_matches_code` | `component:mbx` | `mbx_test_pkg` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_component_matches_code` | `component:mbx` | `tb.sv` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_component_matches_code` | `component:mbx` | `tb` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `tb.sv` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `tb` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `mbx_env_pkg` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `mbx_test_pkg` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `mbx_bind.sv` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `mbx_bind` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `mbx_base_test.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_base_test.sv` |
| `spec_path_matches_code_path` | `mbx.hjson` | `mbx_test_pkg.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `mbx_env_pkg` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `mbx_test_pkg` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `mbx_bind.sv` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `mbx_bind` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `mbx_base_test.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_base_test.sv` |
| `spec_path_matches_code_path` | `mbx_sec_cm_testplan.hjson` | `mbx_test_pkg.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `tb` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `mbx_env_pkg` | `opentitan\hw\ip\mbx\dv\tests\mbx_test_pkg.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `mbx_test_pkg` | `opentitan\hw\ip\mbx\dv\tb.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `mbx_bind.sv` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `mbx_bind` | `opentitan\hw\ip\mbx\dv\sva\mbx_bind.sv` |
| `spec_path_matches_code_path` | `mbx_testplan.hjson` | `mbx_base_test.sv` | `opentitan\hw\ip\mbx\dv\tests\mbx_base_test.sv` |

## Retrieval Guidance

- For code-only queries mentioning `mbx`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `mbx`.
