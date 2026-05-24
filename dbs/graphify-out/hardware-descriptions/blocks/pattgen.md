# Hardware Description: pattgen

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`pattgen`** has the following hardware interfaces defined
- **Peripheral Pins for Chip IO**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`pattgen`** has the following hardware interfaces defined

## Identity

- `ip_block`: `pattgen`
- `bridge_edge_count`: 112
- Spec categories: document: 87, component: 41, testplan: 30, interface: 16, theory: 13
- Code categories: dv: 94, rtl: 29, other_code: 12, sva: 4
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/pattgen/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/pattgen/data/pattgen.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`pattgen`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL
…
```

### Peripheral Pins for Chip IO
_Source: `opentitan/hw/ip/pattgen/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/pattgen/data/pattgen.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`pattgen`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`tl`**
- Bus Ho
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/pattgen/doc/interfaces.md`_

```
| Pin name   | Direction   | Description                                                |
|:-----------|:------------|:-----------------------------------------------------------|
| pda0_tx    | output      | Serial output data bit for pattern generation on Channel 0 |
| pcl0_tx    | output      | Clock corresponding to pattern data on Channel 0           |
| pda1_tx    | output      | Serial outp
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/pattgen/doc/programmers_guide.md`_

```
# Programmer's Guide

To start pattern generation, the register interface of the pattern generator HWIP should be properly initialized and configured.

The guide that follows provides instructions for configuring Channel 0.
To configure Channel 1, use the registers with the "CH1" suffix, instead of the "CH0" registers.

To configure a single channel:
```

### Using the inactive level feature
_Source: `opentitan/hw/ip/pattgen/doc/programmers_guide.md`_

```
The resulting clock frequency will be slower than the input I/O clock by a ratio of 2&times;(CLK_RATIO+1):
$$f_{pclx}=\frac{f_\textrm{I/O clk}}{2(\textrm{CLK\_RATIO}+1)}$$
1. Program the desired number of pattern repetitions using the repetition field [`SIZE.REPS_CH0`](registers.md#size).
Note that since the allowed number of pattern repetitions ranges from 1-1024, the value of this field should b
…
```

### Device Interface Functions DIFs
_Source: `opentitan/hw/ip/pattgen/doc/programmers_guide.md`_

```
{name: 'data',                    wave: 'x..|.3.4.5.6.x|.', node: '.....f', data: "[0]=1'b0 [1]=1'b1 [2]=1'b0 [3]=1'b1"},
  {name: 'pda',                     wave: '0.1|.0.1.0.1..|.', node: '..b...'},
  {name: 'pcl',                     wave: '0.1|.01010101.|.', node: '..d..'},
],
  edge: ['a~b', 'c~d', 'e~f']
}
```

## Device Interface Functions (DIFs)

- [Device Interface Functions](../../../../
…
```

### Summary
_Source: `opentitan/hw/ip/pattgen/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/pattgen/data/pattgen.hjson -->
## Summary

| Name                                  | Offset   |   Length | Description                                         |
|:--------------------------------------|:---------|---------:|:----------------------------------------------------|
| pattgen.[`INTR_STATE`](#intr_state)   | 0x0      |        4 |
…
```

### INTR STATE
_Source: `opentitan/hw/ip/pattgen/doc/registers.md`_

```
| pattgen.[`PREDIV_CH0`](#prediv_ch0)   | 0x14     |        4 | PATTGEN pre-divider register for Channel 0          |
| pattgen.[`PREDIV_CH1`](#prediv_ch1)   | 0x18     |        4 | PATTGEN pre-divider register for Channel 1          |
| pattgen.[`DATA_CH0_0`](#data_ch0)     | 0x1c     |        4 | PATTGEN seed pattern multi-registers for Channel 0. |
| pattgen.[`DATA_CH0_1`](#data_ch0)     | 0x20
…
```

## Spec Anchors

- `component:pattgen` (L1) — `__graphify_spec_only__/components.md`
- `pattgen.hjson` (L1) — `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `human name` (L7) — `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `one line desc` (L8) — `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `one paragraph desc` (L9) — `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `cip id` (L16) — `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `design spec` (L17) — `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `dv doc` (L18) — `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `hw checklist` (L19) — `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `sw checklist` (L20) — `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `revisions` (L21) — `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `version` (L23) — `opentitan/hw/ip/pattgen/data/pattgen.hjson`
- `pattgen_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/pattgen/data/pattgen_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/pattgen/data/pattgen_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/pattgen/data/pattgen_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/pattgen/data/pattgen_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/pattgen/data/pattgen_sec_cm_testplan.hjson`
- `pattgen_testplan.hjson` (L1) — `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `import testplans` (L7) — `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `testpoints` (L13) — `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `desc` (L16) — `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `Stimulus` (L20) — `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `Checking` (L26) — `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `stage` (L34) — `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `tests` (L35) — `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `covergroups` (L106) — `opentitan/hw/ip/pattgen/data/pattgen_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/pattgen/doc/checklist.md`
- `Pattgen Checklist` (L1) — `opentitan/hw/ip/pattgen/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/pattgen/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/pattgen/doc/checklist.md`
- `D2` (L32) — `opentitan/hw/ip/pattgen/doc/checklist.md`
- `D2S` (L74) — `opentitan/hw/ip/pattgen/doc/checklist.md`
- `D3` (L94) — `opentitan/hw/ip/pattgen/doc/checklist.md`
- `Verification Checklist` (L120) — `opentitan/hw/ip/pattgen/doc/checklist.md`
- `V1` (L122) — `opentitan/hw/ip/pattgen/doc/checklist.md`

## Code Evidence

**RTL** (15)
  - `pattgen.sv`:L1 — `opentitan\hw\ip\pattgen\rtl\pattgen.sv`
  - `pattgen`:L7 — `opentitan\hw\ip\pattgen\rtl\pattgen.sv`
  - `pattgen_reg_pkg`:L22 — `opentitan\hw\ip\pattgen\rtl\pattgen_reg_top.sv`
  - `pattgen_core`:L78 — `opentitan\hw\ip\pattgen\rtl\pattgen.sv`
  - `pattgen_chan.sv`:L1 — `opentitan\hw\ip\pattgen\rtl\pattgen_chan.sv`
  - `pattgen_chan`:L5 — `opentitan\hw\ip\pattgen\rtl\pattgen_chan.sv`
  - `pattgen_ctrl_pkg`:L9 — `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv`
  - `pattgen_core.sv`:L1 — `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv`
  - `pattgen_core`:L7 — `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv`
  - `pattgen_chan`:L51 — `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv`
  - `pattgen_ctrl_pkg.sv`:L1 — `opentitan\hw\ip\pattgen\rtl\pattgen_ctrl_pkg.sv`
  - `pattgen_reg_pkg.sv`:L1 — `opentitan\hw\ip\pattgen\rtl\pattgen_reg_pkg.sv`
  - `pattgen_reg_top.sv`:L1 — `opentitan\hw\ip\pattgen\rtl\pattgen_reg_top.sv`
  - `pattgen_reg_top`:L9 — `opentitan\hw\ip\pattgen\rtl\pattgen_reg_top.sv`
  - `pattgen`:L1444 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
**DV** (11)
  - `tb.sv`:L1 — `opentitan\hw\ip\pattgen\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\pattgen\dv\tb.sv`
  - `pattgen_env_pkg`:L10 — `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv`
  - `pattgen_test_pkg`:L10 — `opentitan\hw\ip\pattgen\dv\tb.sv`
  - `pattgen_agent_pkg`:L11 — `opentitan\hw\ip\pattgen\dv\tb.sv`
  - `pattgen_if`:L30 — `opentitan\hw\ip\pattgen\dv\tb.sv`
  - `pattgen_cov_bind.sv`:L1 — `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv`
  - `pattgen_cov_bind`:L6 — `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv`
  - `pattgen_cov_if.sv`:L1 — `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_if.sv`
  - `pattgen_base_test.sv`:L1 — `opentitan\hw\ip\pattgen\dv\tests\pattgen_base_test.sv`
  - `pattgen_test_pkg.sv`:L1 — `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv`
**SVA** (2)
  - `pattgen_bind.sv`:L1 — `opentitan\hw\ip\pattgen\dv\sva\pattgen_bind.sv`
  - `pattgen_bind`:L5 — `opentitan\hw\ip\pattgen\dv\sva\pattgen_bind.sv`
**OTHER_CODE** (12)
  - `pattgen_ios.rs`:L1 — `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
  - `PattGenChannelParams`:L97 — `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
  - `PattGenParams`:L187 — `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
  - `pattgen_ios()`:L367 — `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
  - `Opts`:L26 — `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
  - `TestCmd`:L71 — `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
  - `ChannelSymbols`:L79 — `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
  - `Symbols`:L90 — `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
  - `.from_rng()`:L109 — `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
  - `.pattern_clock_edges()`:L140 — `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
  - `.clock_period_ns()`:L180 — `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`
  - `.from_rng()`:L193 — `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs`

## Neighbor Components

- `rv_plic` (6 refs; instantiates×6)
- `lowrisc_ibex` (4 refs; imports_from×3, instantiates×1)
- `pwrmgr` (3 refs; instantiates×3)
- `rstmgr` (1 refs; imports_from×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:pattgen` | `pattgen_base_test.sv` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_base_test.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_env_pkg` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_test_pkg.sv` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_cov_bind.sv` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_cov_bind` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_cov_if.sv` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_if.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_ctrl_pkg.sv` | `opentitan\hw\ip\pattgen\rtl\pattgen_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_bind.sv` | `opentitan\hw\ip\pattgen\dv\sva\pattgen_bind.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_bind` | `opentitan\hw\ip\pattgen\dv\sva\pattgen_bind.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_reg_pkg` | `opentitan\hw\ip\pattgen\rtl\pattgen_reg_top.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_reg_pkg.sv` | `opentitan\hw\ip\pattgen\rtl\pattgen_reg_pkg.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_reg_top.sv` | `opentitan\hw\ip\pattgen\rtl\pattgen_reg_top.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_reg_top` | `opentitan\hw\ip\pattgen\rtl\pattgen_reg_top.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_chan.sv` | `opentitan\hw\ip\pattgen\rtl\pattgen_chan.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_chan` | `opentitan\hw\ip\pattgen\rtl\pattgen_chan.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_ctrl_pkg` | `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_core.sv` | `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_core` | `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_chan` | `opentitan\hw\ip\pattgen\rtl\pattgen_core.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen.sv` | `opentitan\hw\ip\pattgen\rtl\pattgen.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen` | `opentitan\hw\ip\pattgen\rtl\pattgen.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_core` | `opentitan\hw\ip\pattgen\rtl\pattgen.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_test_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_agent_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_if` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_component_matches_code` | `component:pattgen` | `tb.sv` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_component_matches_code` | `component:pattgen` | `tb` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_ios.rs` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `PattGenChannelParams` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `PattGenParams` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `pattgen_ios()` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `Opts` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `TestCmd` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `ChannelSymbols` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `Symbols` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `.from_rng()` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `.pattern_clock_edges()` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `.clock_period_ns()` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_component_matches_code` | `component:pattgen` | `.from_rng()` | `opentitan\sw\host\tests\chip\pattgen\pattgen_ios.rs` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `tb.sv` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `tb` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `pattgen_env_pkg` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `pattgen_test_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `pattgen_agent_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `pattgen_if` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `pattgen_cov_bind.sv` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_path_matches_code_path` | `pattgen.hjson` | `pattgen_cov_bind` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `pattgen_env_pkg` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `pattgen_test_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `pattgen_agent_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `pattgen_if` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `pattgen_cov_bind.sv` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_path_matches_code_path` | `pattgen_sec_cm_testplan.hjson` | `pattgen_cov_bind` | `opentitan\hw\ip\pattgen\dv\cov\pattgen_cov_bind.sv` |
| `spec_path_matches_code_path` | `pattgen_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_testplan.hjson` | `tb` | `opentitan\hw\ip\pattgen\dv\tb.sv` |
| `spec_path_matches_code_path` | `pattgen_testplan.hjson` | `pattgen_env_pkg` | `opentitan\hw\ip\pattgen\dv\tests\pattgen_test_pkg.sv` |
| `spec_path_matches_code_path` | `pattgen_testplan.hjson` | `pattgen_test_pkg` | `opentitan\hw\ip\pattgen\dv\tb.sv` |

## Retrieval Guidance

- For code-only queries mentioning `pattgen`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `pattgen`.
