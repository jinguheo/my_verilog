# Hardware Description: entropy_src

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`entropy_src`** has the following hardware interfaces defined
- **Inter-Module Signals**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`entropy_src`** has the following hardware interfaces defined

## Identity

- `ip_block`: `entropy_src`
- `bridge_edge_count`: 112
- Spec categories: document: 90, component: 41, testplan: 29, theory: 19, interface: 14
- Code categories: rtl: 98, dv: 86, sva: 3
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Excerpts

### Interfaces
_Source: `opentitan/hw/ip/entropy_src/doc/interfaces.md`_

```
# Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/entropy_src/data/entropy_src.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`entropy_src`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/entropy_src/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/entropy_src/data/entropy_src.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`entropy_src`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`tl
…
```

### Interrupts
_Source: `opentitan/hw/ip/entropy_src/doc/interfaces.md`_

```
| entropy_src_xht_bit_sel            | logic                                 | uni     | req   | RngBusBitSelWidth     | Provides bit selection information for the raw entropy data. It specifies which specific bit or subset of bits from `entropy_src_xht_bit` should be used. The width is determined by `RngBusBitSelWidth` parametrization.
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/entropy_src/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

To initialize the ENTROPY_SRC block, see the Device Interface Functions (DIFs) section.


## Entropy Processing
```

### Initialization
_Source: `opentitan/hw/ip/entropy_src/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

To initialize the ENTROPY_SRC block, see the Device Interface Functions (DIFs) section.


## Entropy Processing

Once entropy has been prepared for delivery, it can be consumed by either hardware (CSRNG block hardware instance) or by a software interface (CSRNG software instance).
```

### Entropy Processing
_Source: `opentitan/hw/ip/entropy_src/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

To initialize the ENTROPY_SRC block, see the Device Interface Functions (DIFs) section.


## Entropy Processing

Once entropy has been prepared for delivery, it can be consumed by either hardware (CSRNG block hardware instance) or by a software interface (CSRNG software instance).

Note that when software makes frequent re-seed requests to CSRNG, any stored
…
```

### Summary
_Source: `opentitan/hw/ip/entropy_src/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/entropy_src/data/entropy_src.hjson -->
## Summary

| Name                                                                  | Offset   |   Length | Description                                                  |
|:----------------------------------------------------------------------|:---------|---------:|:------------------------------------
…
```

### INTR STATE
_Source: `opentitan/hw/ip/entropy_src/doc/registers.md`_

```
| entropy_src.[`OBSERVE_FIFO_THRESH`](#observe_fifo_thresh)             | 0xac     |        4 | Observe FIFO threshold register                              |
| entropy_src.[`OBSERVE_FIFO_DEPTH`](#observe_fifo_depth)               | 0xb0     |        4 | Observe FIFO depth register                                  |
| entropy_src.[`DEBUG_STATUS`](#debug_status)                           | 0xb4
…
```

## Spec Anchors

- `component:entropy_src` (L1) — `__graphify_spec_only__/components.md`
- `entropy_src.hjson` (L1) — `opentitan/hw/ip/entropy_src/data/entropy_src.hjson`
- `human name` (L5) — `opentitan/hw/ip/entropy_src/data/entropy_src.hjson`
- `one line desc` (L6) — `opentitan/hw/ip/entropy_src/data/entropy_src.hjson`
- `one paragraph desc` (L7) — `opentitan/hw/ip/entropy_src/data/entropy_src.hjson`
- `cip id` (L17) — `opentitan/hw/ip/entropy_src/data/entropy_src.hjson`
- `design spec` (L18) — `opentitan/hw/ip/entropy_src/data/entropy_src.hjson`
- `dv doc` (L19) — `opentitan/hw/ip/entropy_src/data/entropy_src.hjson`
- `hw checklist` (L20) — `opentitan/hw/ip/entropy_src/data/entropy_src.hjson`
- `sw checklist` (L21) — `opentitan/hw/ip/entropy_src/data/entropy_src.hjson`
- `version` (L22) — `opentitan/hw/ip/entropy_src/data/entropy_src.hjson`
- `life stage` (L23) — `opentitan/hw/ip/entropy_src/data/entropy_src.hjson`
- `entropy_src_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/entropy_src/data/entropy_src_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/entropy_src/data/entropy_src_sec_cm_testplan.hjson`
- `desc` (L30) — `opentitan/hw/ip/entropy_src/data/entropy_src_sec_cm_testplan.hjson`
- `stage` (L37) — `opentitan/hw/ip/entropy_src/data/entropy_src_sec_cm_testplan.hjson`
- `tests` (L38) — `opentitan/hw/ip/entropy_src/data/entropy_src_sec_cm_testplan.hjson`
- `entropy_src_testplan.hjson` (L1) — `opentitan/hw/ip/entropy_src/data/entropy_src_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/entropy_src/data/entropy_src_testplan.hjson`
- `testpoints` (L12) — `opentitan/hw/ip/entropy_src/data/entropy_src_testplan.hjson`
- `desc` (L15) — `opentitan/hw/ip/entropy_src/data/entropy_src_testplan.hjson`
- `stage` (L18) — `opentitan/hw/ip/entropy_src/data/entropy_src_testplan.hjson`
- `tests` (L19) — `opentitan/hw/ip/entropy_src/data/entropy_src_testplan.hjson`
- `covergroups` (L147) — `opentitan/hw/ip/entropy_src/data/entropy_src_testplan.hjson`
- `need` (L309) — `opentitan/hw/ip/entropy_src/data/entropy_src_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/entropy_src/doc/checklist.md`
- `ENTROPY SRC Checklist` (L1) — `opentitan/hw/ip/entropy_src/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/entropy_src/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/entropy_src/doc/checklist.md`
- `D2` (L32) — `opentitan/hw/ip/entropy_src/doc/checklist.md`
- `D2S` (L74) — `opentitan/hw/ip/entropy_src/doc/checklist.md`
- `D3` (L94) — `opentitan/hw/ip/entropy_src/doc/checklist.md`
- `Verification Checklist` (L120) — `opentitan/hw/ip/entropy_src/doc/checklist.md`
- `V1` (L122) — `opentitan/hw/ip/entropy_src/doc/checklist.md`
- `V2` (L172) — `opentitan/hw/ip/entropy_src/doc/checklist.md`

## Code Evidence

**RTL** (24)
  - `entropy_src_pkg`:L9 — `opentitan\hw\ip\entropy_src\rtl\entropy_src_core.sv`
  - `entropy_src_reg_pkg`:L22 — `opentitan\hw\ip\entropy_src\rtl\entropy_src_reg_top.sv`
  - `entropy_src_main_sm_pkg`:L12 — `opentitan\hw\ip\entropy_src\rtl\entropy_src_main_sm.sv`
  - `entropy_src_tb.sv`:L1 — `opentitan\hw\ip\entropy_src\pre_dv\entropy_src_tb.sv`
  - `entropy_src_tb`:L11 — `opentitan\hw\ip\entropy_src\pre_dv\entropy_src_tb.sv`
  - `entropy_src.sv`:L1 — `opentitan\hw\ip\entropy_src\rtl\entropy_src.sv`
  - `entropy_src`:L10 — `opentitan\hw\ip\entropy_src\rtl\entropy_src.sv`
  - `entropy_src_reg_top`:L155 — `opentitan\hw\ip\entropy_src\rtl\entropy_src.sv`
  - `entropy_src_core`:L165 — `opentitan\hw\ip\entropy_src\rtl\entropy_src.sv`
  - `entropy_src_ack_sm.sv`:L1 — `opentitan\hw\ip\entropy_src\rtl\entropy_src_ack_sm.sv`
  - `entropy_src_ack_sm`:L10 — `opentitan\hw\ip\entropy_src\rtl\entropy_src_ack_sm.sv`
  - `entropy_src_ack_sm_pkg`:L23 — `opentitan\hw\ip\entropy_src\rtl\entropy_src_ack_sm.sv`
  - `entropy_src_ack_sm_pkg.sv`:L1 — `opentitan\hw\ip\entropy_src\rtl\entropy_src_ack_sm_pkg.sv`
  - `entropy_src_adaptp_ht.sv`:L1 — `opentitan\hw\ip\entropy_src\rtl\entropy_src_adaptp_ht.sv`
  - `entropy_src_adaptp_ht`:L8 — `opentitan\hw\ip\entropy_src\rtl\entropy_src_adaptp_ht.sv`
  - `entropy_src_bucket_ht.sv`:L1 — `opentitan\hw\ip\entropy_src\rtl\entropy_src_bucket_ht.sv`
  - `entropy_src_bucket_ht`:L8 — `opentitan\hw\ip\entropy_src\rtl\entropy_src_bucket_ht.sv`
  - `entropy_src_cntr_reg.sv`:L1 — `opentitan\hw\ip\entropy_src\rtl\entropy_src_cntr_reg.sv`
  - `entropy_src_cntr_reg`:L8 — `opentitan\hw\ip\entropy_src\rtl\entropy_src_cntr_reg.sv`
  - `entropy_src_core.sv`:L1 — `opentitan\hw\ip\entropy_src\rtl\entropy_src_core.sv`
**DV** (24)
  - `entropy_src_cov_bind.sv`:L1 — `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_bind.sv`
  - `entropy_src_cov_bind`:L6 — `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_bind.sv`
  - `entropy_src_cov_if.sv`:L1 — `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_if.sv`
  - `entropy_src_env_pkg`:L9 — `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_test_pkg.sv`
  - `entropy_src_fsm_cov_if.sv`:L1 — `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_fsm_cov_if.sv`
  - `tb.sv`:L1 — `opentitan\hw\ip\entropy_src\dv\tb\tb.sv`
  - `entropy_src_test_pkg`:L10 — `opentitan\hw\ip\entropy_src\dv\tb\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\entropy_src\dv\tb\tb.sv`
  - `entropy_src_xht_if`:L41 — `opentitan\hw\ip\entropy_src\dv\tb\tb.sv`
  - `entropy_src_path_if`:L42 — `opentitan\hw\ip\entropy_src\dv\tb\tb.sv`
  - `entropy_subsys_fifo_exception_if`:L94 — `opentitan\hw\ip\entropy_src\dv\tb\tb.sv`
  - `entropy_src_fsm_cov_if`:L120 — `opentitan\hw\ip\entropy_src\dv\tb\tb.sv`
  - `entropy_src_alert_test.sv`:L1 — `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_alert_test.sv`
  - `entropy_src_base_test.sv`:L1 — `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_base_test.sv`
  - `entropy_src_cfg_regwen_test.sv`:L1 — `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_cfg_regwen_test.sv`
  - `entropy_src_functional_errors_test.sv`:L1 — `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_functional_errors_test.sv`
  - `entropy_src_fw_ov_contiguous_test.sv`:L1 — `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_fw_ov_contiguous_test.sv`
  - `entropy_src_fw_ov_test.sv`:L1 — `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_fw_ov_test.sv`
  - `entropy_src_intr_test.sv`:L1 — `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_intr_test.sv`
  - `entropy_src_rng_max_rate_test.sv`:L1 — `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_rng_max_rate_test.sv`
**SVA** (2)
  - `entropy_src_bind.sv`:L1 — `opentitan\hw\ip\entropy_src\dv\sva\entropy_src_bind.sv`
  - `entropy_src_bind`:L5 — `opentitan\hw\ip\entropy_src\dv\sva\entropy_src_bind.sv`

## Neighbor Components

- `rv_plic` (10 refs; instantiates×10)
- `lowrisc_ibex` (6 refs; instantiates×4, imports_from×2)
- `rv_core_ibex` (5 refs; imports_from×5)
- `flash_ctrl` (3 refs; instantiates×3)
- `pwrmgr` (3 refs; instantiates×3)
- `rstmgr` (2 refs; instantiates×1, imports_from×1)
- `otp_ctrl` (2 refs; instantiates×2)
- `pulp_riscv_dbg` (1 refs; instantiates×1)
- `ast` (1 refs; instantiates×1)
- `clkmgr` (1 refs; instantiates×1)
- `rv_dm` (1 refs; instantiates×1)
- `kmac` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_functional_errors_test.sv` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_functional_errors_test.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_fw_ov_contiguous_test.sv` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_fw_ov_contiguous_test.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_rng_max_rate_test.sv` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_rng_max_rate_test.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_cfg_regwen_test.sv` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_cfg_regwen_test.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_stress_all_test.sv` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_stress_all_test.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_alert_test.sv` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_alert_test.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_fw_ov_test.sv` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_fw_ov_test.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_smoke_test.sv` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_smoke_test.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_base_test.sv` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_base_test.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_intr_test.sv` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_intr_test.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_env_pkg` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_test_pkg.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_fsm_cov_if.sv` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_fsm_cov_if.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_rng_test.sv` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_rng_test.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_test_pkg.sv` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_test_pkg.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_watermark_reg.sv` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_watermark_reg.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_watermark_reg` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_watermark_reg.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_enable_delay.sv` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_enable_delay.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_enable_delay` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_enable_delay.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_cov_bind.sv` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_bind.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_cov_bind` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_bind.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_main_sm_pkg.sv` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_main_sm_pkg.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_ack_sm_pkg.sv` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_ack_sm_pkg.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_repcnts_ht.sv` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_repcnts_ht.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_repcnts_ht` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_repcnts_ht.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_cov_if.sv` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_if.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_adaptp_ht.sv` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_adaptp_ht.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_adaptp_ht` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_adaptp_ht.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_bucket_ht.sv` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_bucket_ht.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_bucket_ht` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_bucket_ht.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_markov_ht.sv` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_markov_ht.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_markov_ht` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_markov_ht.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_repcnt_ht.sv` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_repcnt_ht.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_repcnt_ht` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_repcnt_ht.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_cntr_reg.sv` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_cntr_reg.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_cntr_reg` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_cntr_reg.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_field_en.sv` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_field_en.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_field_en` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_field_en.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_reg_pkg` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_reg_top.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_main_sm_pkg` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_main_sm.sv` |
| `spec_component_matches_code` | `component:entropy_src` | `entropy_src_bind.sv` | `opentitan\hw\ip\entropy_src\dv\sva\entropy_src_bind.sv` |
| `spec_path_matches_code_path` | `entropy_src.hjson` | `entropy_src_pkg` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_core.sv` |
| `spec_path_matches_code_path` | `entropy_src.hjson` | `entropy_src_cov_bind.sv` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_bind.sv` |
| `spec_path_matches_code_path` | `entropy_src.hjson` | `entropy_src_cov_bind` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_bind.sv` |
| `spec_path_matches_code_path` | `entropy_src.hjson` | `entropy_src_cov_if.sv` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_if.sv` |
| `spec_path_matches_code_path` | `entropy_src.hjson` | `entropy_src_reg_pkg` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_reg_top.sv` |
| `spec_path_matches_code_path` | `entropy_src.hjson` | `entropy_src_env_pkg` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_test_pkg.sv` |
| `spec_path_matches_code_path` | `entropy_src.hjson` | `entropy_src_fsm_cov_if.sv` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_fsm_cov_if.sv` |
| `spec_path_matches_code_path` | `entropy_src.hjson` | `entropy_src_main_sm_pkg` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_main_sm.sv` |
| `spec_path_matches_code_path` | `entropy_src_sec_cm_testplan.hjson` | `entropy_src_pkg` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_core.sv` |
| `spec_path_matches_code_path` | `entropy_src_sec_cm_testplan.hjson` | `entropy_src_cov_bind.sv` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_bind.sv` |
| `spec_path_matches_code_path` | `entropy_src_sec_cm_testplan.hjson` | `entropy_src_cov_bind` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_bind.sv` |
| `spec_path_matches_code_path` | `entropy_src_sec_cm_testplan.hjson` | `entropy_src_cov_if.sv` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_if.sv` |
| `spec_path_matches_code_path` | `entropy_src_sec_cm_testplan.hjson` | `entropy_src_reg_pkg` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_reg_top.sv` |
| `spec_path_matches_code_path` | `entropy_src_sec_cm_testplan.hjson` | `entropy_src_env_pkg` | `opentitan\hw\ip\entropy_src\dv\tests\entropy_src_test_pkg.sv` |
| `spec_path_matches_code_path` | `entropy_src_sec_cm_testplan.hjson` | `entropy_src_fsm_cov_if.sv` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_fsm_cov_if.sv` |
| `spec_path_matches_code_path` | `entropy_src_sec_cm_testplan.hjson` | `entropy_src_main_sm_pkg` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_main_sm.sv` |
| `spec_path_matches_code_path` | `entropy_src_testplan.hjson` | `entropy_src_pkg` | `opentitan\hw\ip\entropy_src\rtl\entropy_src_core.sv` |
| `spec_path_matches_code_path` | `entropy_src_testplan.hjson` | `entropy_src_cov_bind.sv` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_bind.sv` |
| `spec_path_matches_code_path` | `entropy_src_testplan.hjson` | `entropy_src_cov_bind` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_bind.sv` |
| `spec_path_matches_code_path` | `entropy_src_testplan.hjson` | `entropy_src_cov_if.sv` | `opentitan\hw\ip\entropy_src\dv\cov\entropy_src_cov_if.sv` |

## Retrieval Guidance

- For code-only queries mentioning `entropy_src`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `entropy_src`.
