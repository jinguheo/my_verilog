# Hardware Description: dma

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`dma`** has the following hardware interfaces defined
- **Inter-Module Signals**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`dma`** has the following hardware interfaces defined

## Identity

- `ip_block`: `dma`
- `bridge_edge_count`: 95
- Spec categories: document: 88, testplan: 30, component: 24, theory: 19, interface: 16
- Code categories: dv: 65, rtl: 28, sva: 24
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 23

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/dma/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/dma/data/dma.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`dma`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`tl_
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/dma/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/dma/data/dma.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`dma`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`tl_d`**
- Bus Host Interfa
…
```

### Interrupts
_Source: `opentitan/hw/ip/dma/doc/interfaces.md`_

```
| sys           | dma_pkg::sys                  | req_rsp | req   |       1 | SoC System Bus (requests and responses), synchronous                                                                                 |
| ctn_tl_h2d    | tlul_pkg::tl_h2d              | uni     | req   |       1 | TL-UL host port for egress into CTN (request part), synchronous
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/dma/doc/programmers_guide.md`_

```
# Programmer's Guide

This section details how software can interface with the Direct Memory Access (DMA) controller.

## Module Initialization

Before initiating memory transfers using the DMA for OpenTitan internal memory, software must define the accessible memory range for the DMA.
This involves a specific sequence of register writes:
```

### Module Initialization
_Source: `opentitan/hw/ip/dma/doc/programmers_guide.md`_

```
# Programmer's Guide

This section details how software can interface with the Direct Memory Access (DMA) controller.

## Module Initialization

Before initiating memory transfers using the DMA for OpenTitan internal memory, software must define the accessible memory range for the DMA.
This involves a specific sequence of register writes:

1.  **Define the Memory Range:** First, software must writ
…
```

### Initiate a Memory transfer
_Source: `opentitan/hw/ip/dma/doc/programmers_guide.md`_

```
Before initiating memory transfers using the DMA for OpenTitan internal memory, software must define the accessible memory range for the DMA.
This involves a specific sequence of register writes:

1.  **Define the Memory Range:** First, software must write the base address to the [`ENABLED_MEMORY_RANGE_BASE`](registers.md#enabled_memory_range_base) register and the upper limit of the accessible ra
…
```

### Summary
_Source: `opentitan/hw/ip/dma/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/dma/data/dma.hjson -->
## Summary

| Name                                                            | Offset   |   Length | Description                                                                                                                                              |
|:------------------------------------------------------------
…
```

### INTR STATE
_Source: `opentitan/hw/ip/dma/doc/registers.md`_

```
| dma.[`INTR_SRC_WR_VAL_4`](#intr_src_wr_val)                     | 0x134    |        4 | Write value for interrupt clearing write.                                                                                                                |
| dma.[`INTR_SRC_WR_VAL_5`](#intr_src_wr_val)                     | 0x138    |        4 | Write value for interrupt clearing write.
…
```

## Spec Anchors

- `component:dma` (L1) — `__graphify_spec_only__/components.md`
- `dma.hjson` (L1) — `opentitan/hw/ip/dma/data/dma.hjson`
- `human name` (L8) — `opentitan/hw/ip/dma/data/dma.hjson`
- `one line desc` (L9) — `opentitan/hw/ip/dma/data/dma.hjson`
- `one paragraph desc` (L10) — `opentitan/hw/ip/dma/data/dma.hjson`
- `cip id` (L16) — `opentitan/hw/ip/dma/data/dma.hjson`
- `design spec` (L17) — `opentitan/hw/ip/dma/data/dma.hjson`
- `dv doc` (L18) — `opentitan/hw/ip/dma/data/dma.hjson`
- `version` (L19) — `opentitan/hw/ip/dma/data/dma.hjson`
- `clocking` (L21) — `opentitan/hw/ip/dma/data/dma.hjson`
- `scan` (L22) — `opentitan/hw/ip/dma/data/dma.hjson`
- `bus interfaces` (L23) — `opentitan/hw/ip/dma/data/dma.hjson`
- `dma_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/dma/data/dma_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/dma/data/dma_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/dma/data/dma_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/dma/data/dma_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/dma/data/dma_sec_cm_testplan.hjson`
- `dma_testplan.hjson` (L1) — `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `testpoints` (L10) — `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `desc` (L16) — `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `Stimulus` (L19) — `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `Checking` (L31) — `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `stage` (L38) — `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `tests` (L39) — `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `covergroups` (L316) — `opentitan/hw/ip/dma/data/dma_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/dma/doc/checklist.md`
- `DMA Controller Checklist` (L1) — `opentitan/hw/ip/dma/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/dma/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/dma/doc/checklist.md`
- `D2` (L34) — `opentitan/hw/ip/dma/doc/checklist.md`
- `D2S` (L76) — `opentitan/hw/ip/dma/doc/checklist.md`
- `D3` (L96) — `opentitan/hw/ip/dma/doc/checklist.md`
- `Verification Checklist` (L122) — `opentitan/hw/ip/dma/doc/checklist.md`
- `V1` (L124) — `opentitan/hw/ip/dma/doc/checklist.md`

## Code Evidence

**RTL** (10)
  - `dma_reg_pkg`:L32 — `opentitan\hw\ip\dma\rtl\dma_reg_top.sv`
  - `dma_pkg`:L9 — `opentitan\hw\ip\dma\rtl\dma.sv`
  - `dma.sv`:L1 — `opentitan\hw\ip\dma\rtl\dma.sv`
  - `dma`:L7 — `opentitan\hw\ip\dma\rtl\dma.sv`
  - `dma_reg_top`:L164 — `opentitan\hw\ip\dma\rtl\dma.sv`
  - `dma_pkg.sv`:L1 — `opentitan\hw\ip\dma\rtl\dma_pkg.sv`
  - `dma_reg_pkg.sv`:L1 — `opentitan\hw\ip\dma\rtl\dma_reg_pkg.sv`
  - `dma_reg_top.sv`:L1 — `opentitan\hw\ip\dma\rtl\dma_reg_top.sv`
  - `dma_reg_top`:L9 — `opentitan\hw\ip\dma\rtl\dma_reg_top.sv`
  - `dma`:L2221 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
**DV** (10)
  - `dma_cov_bind.sv`:L1 — `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv`
  - `dma_cov_bind`:L5 — `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv`
  - `dma_cov_if.sv`:L1 — `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv`
  - `tb.sv`:L1 — `opentitan\hw\ip\dma\dv\tb\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\dma\dv\tb\tb.sv`
  - `dma_env_pkg`:L8 — `opentitan\hw\ip\dma\dv\tests\dma_test_pkg.sv`
  - `dma_test_pkg`:L12 — `opentitan\hw\ip\dma\dv\tb\tb.sv`
  - `dma_sys_tl_if`:L39 — `opentitan\hw\ip\dma\dv\tb\tb.sv`
  - `dma_base_test.sv`:L1 — `opentitan\hw\ip\dma\dv\tests\dma_base_test.sv`
  - `dma_test_pkg.sv`:L1 — `opentitan\hw\ip\dma\dv\tests\dma_test_pkg.sv`
**SVA** (3)
  - `dma_bind.sv`:L1 — `opentitan\hw\ip\dma\dv\sva\dma_bind.sv`
  - `dma_bind`:L5 — `opentitan\hw\ip\dma\dv\sva\dma_bind.sv`
  - `tlul_assert`:L44 — `opentitan\hw\ip\dma\dv\tb\tb.sv`

## Neighbor Components

- `rv_plic` (6 refs; instantiates×6)
- `lowrisc_ibex` (5 refs; instantiates×4, imports_from×1)
- `pwrmgr` (3 refs; instantiates×3)
- `rv_core_ibex` (2 refs; imports_from×1, instantiates×1)
- `ac_range_check` (1 refs; instantiates×1)
- `prim` (1 refs; imports_from×1)
- `rstmgr` (1 refs; imports_from×1)
- `hmac` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:dma` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_base_test.sv` | `opentitan\hw\ip\dma\dv\tests\dma_base_test.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_env_pkg` | `opentitan\hw\ip\dma\dv\tests\dma_test_pkg.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_test_pkg.sv` | `opentitan\hw\ip\dma\dv\tests\dma_test_pkg.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_cov_bind` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_cov_if.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_reg_pkg` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_bind.sv` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_bind` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_reg_pkg.sv` | `opentitan\hw\ip\dma\rtl\dma_reg_pkg.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_reg_top.sv` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_reg_top` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_pkg.sv` | `opentitan\hw\ip\dma\rtl\dma_pkg.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_test_pkg` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_sys_tl_if` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_pkg` | `opentitan\hw\ip\dma\rtl\dma.sv` |
| `spec_component_matches_code` | `component:dma` | `dma.sv` | `opentitan\hw\ip\dma\rtl\dma.sv` |
| `spec_component_matches_code` | `component:dma` | `dma` | `opentitan\hw\ip\dma\rtl\dma.sv` |
| `spec_component_matches_code` | `component:dma` | `dma_reg_top` | `opentitan\hw\ip\dma\rtl\dma.sv` |
| `spec_component_matches_code` | `component:dma` | `tb.sv` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:dma` | `tb` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:dma` | `tlul_assert` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `dma_cov_bind` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `dma_cov_if.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `dma_reg_pkg` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `dma_bind.sv` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `dma_bind` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `tb.sv` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `dma.hjson` | `tb` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `dma_cov_bind` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `dma_cov_if.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `dma_reg_pkg` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `dma_bind.sv` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `dma_bind` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `dma_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `dma_cov_bind` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `dma_cov_if.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `dma_reg_pkg` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `dma_bind.sv` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `dma_bind` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `dma_testplan.hjson` | `tb` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `dma_cov_bind` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `dma_cov_if.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `dma_reg_pkg` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `dma_bind.sv` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `dma_bind` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\dma\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `dma_cov_bind.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `dma_cov_bind` | `opentitan\hw\ip\dma\dv\cov\dma_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `dma_cov_if.sv` | `opentitan\hw\ip\dma\dv\cov\dma_cov_if.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `dma_reg_pkg` | `opentitan\hw\ip\dma\rtl\dma_reg_top.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `dma_bind.sv` | `opentitan\hw\ip\dma\dv\sva\dma_bind.sv` |

## Retrieval Guidance

- For code-only queries mentioning `dma`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `dma`.
