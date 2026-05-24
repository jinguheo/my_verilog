# Hardware Description: ascon

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Background**: This section provides simple diagrams on Sponge, Ascon, round based implementations, and the round function.
- **Duplex Sponge**: This section provides simple diagrams on Sponge, Ascon, round based implementations, and the round function.
- **Ascon AEAD**: In Figure 1, the tag consists of one block, so size of tag t=r.

## Identity

- `ip_block`: `ascon`
- `bridge_edge_count`: 92
- Spec categories: document: 98, component: 29, theory: 19, interface: 11
- Code categories: rtl: 104, other_code: 8, dv: 4
- Bridge relations: spec_path_matches_code_path: 64, spec_component_matches_code: 28

## Spec Excerpts

### Background
_Source: `opentitan/hw/ip/ascon/doc/background.md`_

```
## Background

This section provides simple diagrams on Sponge, Ascon, round based implementations, and the round function.
It describes the basic principles of Sponge and Ascon.
It also lists some performance figures from different (existing) implementations.


#### Duplex Sponge
```

### Duplex Sponge
_Source: `opentitan/hw/ip/ascon/doc/background.md`_

```
## Background

This section provides simple diagrams on Sponge, Ascon, round based implementations, and the round function.
It describes the basic principles of Sponge and Ascon.
It also lists some performance figures from different (existing) implementations.


#### Duplex Sponge

A cryptographic public permutation is a cryptographic primitive that efficiently applies a permutation over b-bit blo
…
```

### Ascon AEAD
_Source: `opentitan/hw/ip/ascon/doc/background.md`_

```
In Figure 1, the tag consists of one block, so size of tag t=r.



![alt_text](duplex.svg "Simplified view of the duplex construction.")
Fig 1. Simplified view of the duplex construction.


## Ascon AEAD

Ascon AEAD, depicted in Figure 2, is inspired by the duplex construction using Ascon-p, where the state size is 320 bits, with a few changes.
First, two similar permutations are used instead of 1
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/ascon/doc/interfaces.md`_

```
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_edn_i`**
- Bus Device Interfaces (TL-UL): **`tl`**
- Bus Host Interfaces (TL-UL): *none*
- Peripheral Pins for Chip IO: *none*
- Interrupts: *none*
- Security Countermeasures: *none*

## [Inter-Module Signals](https://opentitan.org/book/doc/contributing/hw/comportability/index.html#inter-signal-handling)

| Port Name      | Package::Struct
…
```

### Security Alerts
_Source: `opentitan/hw/ip/ascon/doc/interfaces.md`_

```
| Port Name      | Package::Struct        | Type    | Act   |   Width | Description   |
|:---------------|:-----------------------|:--------|:------|--------:|:--------------|
| idle           | prim_mubi_pkg::mubi4   | uni     | req   |       1 |               |
| lc_escalate_en | lc_ctrl_pkg::lc_tx     | uni     | rcv   |       1 |               |
| edn            | edn_pkg::edn           | req_
…
```

### Programmer’s Guide
_Source: `opentitan/hw/ip/ascon/doc/programmers_guide.md`_

```
# Programmer’s Guide

## Initializing the IP

As long as there is a key set, the IP can be used. However it is good practice not to rely on any default values but to configure the IP. The following settings should be configured in the following order:
1. Check if the IP is idle by reading STATUS.IDLE
2. Check for any errors by reading the STATUS.ascon_error. If there are any errors, perform a secu
…
```

### Initializing the IP
_Source: `opentitan/hw/ip/ascon/doc/programmers_guide.md`_

```
# Programmer’s Guide

## Initializing the IP

As long as there is a key set, the IP can be used. However it is good practice not to rely on any default values but to configure the IP. The following settings should be configured in the following order:
1. Check if the IP is idle by reading STATUS.IDLE
2. Check for any errors by reading the STATUS.ascon_error. If there are any errors, perform a secu
…
```

### Interrupt Configuration
_Source: `opentitan/hw/ip/ascon/doc/programmers_guide.md`_

```
As long as there is a key set, the IP can be used. However it is good practice not to rely on any default values but to configure the IP. The following settings should be configured in the following order:
1. Check if the IP is idle by reading STATUS.IDLE
2. Check for any errors by reading the STATUS.ascon_error. If there are any errors, perform a secure wipe by setting TRIGGER.wipe to 1.
3. Set C
…
```

## Spec Anchors

- `component:ascon` (L1) — `__graphify_spec_only__/components.md`
- `ascon.hjson` (L1) — `opentitan/hw/ip/ascon/data/ascon.hjson`
- `human name` (L8) — `opentitan/hw/ip/ascon/data/ascon.hjson`
- `one line desc` (L9) — `opentitan/hw/ip/ascon/data/ascon.hjson`
- `one paragraph desc` (L10) — `opentitan/hw/ip/ascon/data/ascon.hjson`
- `regwidth` (L17) — `opentitan/hw/ip/ascon/data/ascon.hjson`
- `cip id` (L18) — `opentitan/hw/ip/ascon/data/ascon.hjson`
- `design spec` (L19) — `opentitan/hw/ip/ascon/data/ascon.hjson`
- `hw checklist` (L20) — `opentitan/hw/ip/ascon/data/ascon.hjson`
- `version` (L21) — `opentitan/hw/ip/ascon/data/ascon.hjson`
- `life stage` (L22) — `opentitan/hw/ip/ascon/data/ascon.hjson`
- `design stage` (L23) — `opentitan/hw/ip/ascon/data/ascon.hjson`
- `background.md` (L1) — `opentitan/hw/ip/ascon/doc/background.md`
- `Background` (L1) — `opentitan/hw/ip/ascon/doc/background.md`
- `Duplex Sponge` (L8) — `opentitan/hw/ip/ascon/doc/background.md`
- `Ascon AEAD` (L30) — `opentitan/hw/ip/ascon/doc/background.md`
- `checklist.md` (L1) — `opentitan/hw/ip/ascon/doc/checklist.md`
- `Design Checklist` (L7) — `opentitan/hw/ip/ascon/doc/checklist.md`
- `D1` (L9) — `opentitan/hw/ip/ascon/doc/checklist.md`
- `D2` (L35) — `opentitan/hw/ip/ascon/doc/checklist.md`
- `D2S` (L77) — `opentitan/hw/ip/ascon/doc/checklist.md`
- `D3` (L97) — `opentitan/hw/ip/ascon/doc/checklist.md`
- `Verification Checklist` (L123) — `opentitan/hw/ip/ascon/doc/checklist.md`
- `V1` (L125) — `opentitan/hw/ip/ascon/doc/checklist.md`
- `V2` (L175) — `opentitan/hw/ip/ascon/doc/checklist.md`
- `V2S` (L221) — `opentitan/hw/ip/ascon/doc/checklist.md`
- `V3` (L237) — `opentitan/hw/ip/ascon/doc/checklist.md`
- `interfaces.md` (L1) — `opentitan/hw/ip/ascon/doc/interfaces.md`
- `Inter-Module Signals` (L10) — `opentitan/hw/ip/ascon/doc/interfaces.md`
- `Security Alerts` (L20) — `opentitan/hw/ip/ascon/doc/interfaces.md`
- `programmers_guide.md` (L1) — `opentitan/hw/ip/ascon/doc/programmers_guide.md`
- `Programmer’s Guide` (L1) — `opentitan/hw/ip/ascon/doc/programmers_guide.md`
- `Initializing the IP` (L3) — `opentitan/hw/ip/ascon/doc/programmers_guide.md`
- `Interrupt Configuration` (L12) — `opentitan/hw/ip/ascon/doc/programmers_guide.md`
- `Issuing Transactions` (L17) — `opentitan/hw/ip/ascon/doc/programmers_guide.md`

## Code Evidence

**RTL** (20)
  - `ascon_sim.sv`:L1 — `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv`
  - `ascon_sim`:L7 — `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv`
  - `ascon_pkg`:L9 — `opentitan\hw\ip\ascon\rtl\ascon_core.sv`
  - `ascon_reg_pkg`:L26 — `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv`
  - `ascon_tl_ul_stim`:L56 — `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv`
  - `ascon`:L145 — `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv`
  - `ascon_tl_ul_stim.sv`:L1 — `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv`
  - `ascon_tl_ul_stim`:L7 — `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv`
  - `ascon_tl_ul_stim_pkg`:L11 — `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv`
  - `ascon_tl_ul_stim_pkg.sv`:L1 — `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim_pkg.sv`
  - `ascon.sv`:L1 — `opentitan\hw\ip\ascon\rtl\ascon.sv`
  - `ascon`:L7 — `opentitan\hw\ip\ascon\rtl\ascon.sv`
  - `ascon_reg_top`:L61 — `opentitan\hw\ip\ascon\rtl\ascon.sv`
  - `ascon_core`:L74 — `opentitan\hw\ip\ascon\rtl\ascon.sv`
  - `ascon_core.sv`:L1 — `opentitan\hw\ip\ascon\rtl\ascon_core.sv`
  - `ascon_core`:L7 — `opentitan\hw\ip\ascon\rtl\ascon_core.sv`
  - `ascon_pkg.sv`:L1 — `opentitan\hw\ip\ascon\rtl\ascon_pkg.sv`
  - `ascon_reg_pkg.sv`:L1 — `opentitan\hw\ip\ascon\rtl\ascon_reg_pkg.sv`
  - `ascon_reg_top.sv`:L1 — `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv`
  - `ascon_reg_top`:L9 — `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv`
**DV** (4)
  - `ascon.h`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\ascon.h`
  - `ascon.h`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\ascon.h`
  - `ascon.h`:L1 — `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\ascon.h`
  - `ascon.h`:L1 — `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\ascon.h`
**OTHER_CODE** (4)
  - `ascon_tb.cc`:L1 — `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc`
  - `AsconSim`:L14 — `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc`
  - `OnClock()`:L31 — `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc`
  - `main()`:L37 — `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc`

## Neighbor Components

- `prim` (19 refs; imports×18, instantiates×1)
- `rv_plic` (6 refs; instantiates×6)
- `verilator_sim_ctrl.cc` (3 refs; calls×3)
- `flash_ctrl` (2 refs; instantiates×2)
- `lowrisc_ibex` (1 refs; instantiates×1)
- `rv_core_ibex` (1 refs; instantiates×1)
- `soc_proxy` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:ascon` | `ascon_tl_ul_stim_pkg.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim_pkg.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_tl_ul_stim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_tl_ul_stim_pkg` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_sim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_sim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_reg_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_reg_pkg.sv` | `opentitan\hw\ip\ascon\rtl\ascon_reg_pkg.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_reg_top.sv` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_reg_top` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_core.sv` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_core` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_pkg.sv` | `opentitan\hw\ip\ascon\rtl\ascon_pkg.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon.sv` | `opentitan\hw\ip\ascon\rtl\ascon.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon` | `opentitan\hw\ip\ascon\rtl\ascon.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_reg_top` | `opentitan\hw\ip\ascon\rtl\ascon.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_core` | `opentitan\hw\ip\ascon\rtl\ascon.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon.h` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\ascon.h` |
| `spec_component_matches_code` | `component:ascon` | `ascon.h` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\ascon.h` |
| `spec_component_matches_code` | `component:ascon` | `ascon.h` | `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\ascon.h` |
| `spec_component_matches_code` | `component:ascon` | `ascon.h` | `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\ascon.h` |
| `spec_component_matches_code` | `component:ascon` | `ascon_tb.cc` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc` |
| `spec_component_matches_code` | `component:ascon` | `AsconSim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc` |
| `spec_component_matches_code` | `component:ascon` | `OnClock()` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc` |
| `spec_component_matches_code` | `component:ascon` | `main()` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon_sim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon_sim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon_reg_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon_tl_ul_stim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon_sim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon_sim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon_reg_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon_tl_ul_stim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon_sim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon_sim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon_reg_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon_tl_ul_stim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon_sim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon_sim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon_reg_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon_tl_ul_stim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |

## Retrieval Guidance

- For code-only queries mentioning `ascon`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `ascon`.
