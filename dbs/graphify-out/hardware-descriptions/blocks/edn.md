# Hardware Description: edn

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`edn`** has the following hardware interfaces defined
- **Inter-Module Signals**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`edn`** has the following hardware interfaces defined

## Identity

- `ip_block`: `edn`
- `bridge_edge_count`: 112
- Spec categories: document: 87, component: 41, testplan: 28, theory: 19, interface: 15
- Code categories: dv: 112, rtl: 35, sva: 6
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Excerpts

### Interfaces
_Source: `opentitan/hw/ip/edn/doc/interfaces.md`_

```
# Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/edn/data/edn.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`edn`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`tl`**
- Bus
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/edn/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/edn/data/edn.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`edn`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`tl`**
- Bus Host Interface
…
```

### Interrupts
_Source: `opentitan/hw/ip/edn/doc/interfaces.md`_

```
## [Inter-Module Signals](https://opentitan.org/book/doc/contributing/hw/comportability/index.html#inter-signal-handling)

| Port Name   | Package::Struct   | Type    | Act   | Width        | Description                                        |
|:------------|:------------------|:--------|:------|:-------------|:---------------------------------------------------|
| csrng_cmd   | csrng_pkg::csrng
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/edn/doc/programmers_guide.md`_

```
# Programmer's Guide

This section discusses how firmware can interface with EDN.

## Module enable and disable

EDN may only be enabled if CSRNG is enabled.
Once disabled, EDN may only be re-enabled after CSRNG has been disabled and re-enabled.
```

### Module enable and disable
_Source: `opentitan/hw/ip/edn/doc/programmers_guide.md`_

```
# Programmer's Guide

This section discusses how firmware can interface with EDN.

## Module enable and disable

EDN may only be enabled if CSRNG is enabled.
Once disabled, EDN may only be re-enabled after CSRNG has been disabled and re-enabled.
The only exception to this is when firmware takes care of properly uninstantiating the associated CSRNG instance before disabling EDN.
EDN can then be saf
…
```

### Uninstantiating CSRNG through EDN
_Source: `opentitan/hw/ip/edn/doc/programmers_guide.md`_

```
EDN may only be enabled if CSRNG is enabled.
Once disabled, EDN may only be re-enabled after CSRNG has been disabled and re-enabled.
The only exception to this is when firmware takes care of properly uninstantiating the associated CSRNG instance before disabling EDN.
EDN can then be safely re-enabled without disabling and re-enabling CSRNG first.
For details, refer to [Uninstantiating CSRNG instan
…
```

### Summary
_Source: `opentitan/hw/ip/edn/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/edn/data/edn.hjson -->
## Summary

| Name                                                                | Offset   |   Length | Description                                                  |
|:--------------------------------------------------------------------|:---------|---------:|:--------------------------------------------------------
…
```

### INTR STATE
_Source: `opentitan/hw/ip/edn/doc/registers.md`_

```
| edn.[`RESEED_CMD`](#reseed_cmd)                                     | 0x2c     |        4 | EDN csrng reseed command register                            |
| edn.[`GENERATE_CMD`](#generate_cmd)                                 | 0x30     |        4 | EDN csrng generate command register                          |
| edn.[`MAX_NUM_REQS_BETWEEN_RESEEDS`](#max_num_reqs_between_reseeds) | 0x34     |
…
```

## Spec Anchors

- `component:edn` (L1) — `__graphify_spec_only__/components.md`
- `edn.hjson` (L1) — `opentitan/hw/ip/edn/data/edn.hjson`
- `human name` (L6) — `opentitan/hw/ip/edn/data/edn.hjson`
- `one line desc` (L7) — `opentitan/hw/ip/edn/data/edn.hjson`
- `one paragraph desc` (L8) — `opentitan/hw/ip/edn/data/edn.hjson`
- `cip id` (L15) — `opentitan/hw/ip/edn/data/edn.hjson`
- `design spec` (L16) — `opentitan/hw/ip/edn/data/edn.hjson`
- `dv doc` (L17) — `opentitan/hw/ip/edn/data/edn.hjson`
- `hw checklist` (L18) — `opentitan/hw/ip/edn/data/edn.hjson`
- `sw checklist` (L19) — `opentitan/hw/ip/edn/data/edn.hjson`
- `version` (L20) — `opentitan/hw/ip/edn/data/edn.hjson`
- `life stage` (L21) — `opentitan/hw/ip/edn/data/edn.hjson`
- `edn_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/edn/data/edn_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/edn/data/edn_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/edn/data/edn_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/edn/data/edn_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/edn/data/edn_sec_cm_testplan.hjson`
- `edn_testplan.hjson` (L1) — `opentitan/hw/ip/edn/data/edn_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/edn/data/edn_testplan.hjson`
- `testpoints` (L12) — `opentitan/hw/ip/edn/data/edn_testplan.hjson`
- `desc` (L15) — `opentitan/hw/ip/edn/data/edn_testplan.hjson`
- `stage` (L20) — `opentitan/hw/ip/edn/data/edn_testplan.hjson`
- `tests` (L21) — `opentitan/hw/ip/edn/data/edn_testplan.hjson`
- `covergroups` (L103) — `opentitan/hw/ip/edn/data/edn_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/edn/doc/checklist.md`
- `EDN Checklist` (L1) — `opentitan/hw/ip/edn/doc/checklist.md`
- `Design Checklist` (L11) — `opentitan/hw/ip/edn/doc/checklist.md`
- `D1` (L13) — `opentitan/hw/ip/edn/doc/checklist.md`
- `D2` (L37) — `opentitan/hw/ip/edn/doc/checklist.md`
- `D2S` (L79) — `opentitan/hw/ip/edn/doc/checklist.md`
- `D3` (L99) — `opentitan/hw/ip/edn/doc/checklist.md`
- `Verification Checklist` (L125) — `opentitan/hw/ip/edn/doc/checklist.md`
- `V1` (L127) — `opentitan/hw/ip/edn/doc/checklist.md`
- `V2` (L177) — `opentitan/hw/ip/edn/doc/checklist.md`
- `V2S` (L223) — `opentitan/hw/ip/edn/doc/checklist.md`

## Code Evidence

**RTL** (18)
  - `edn.sv`:L1 — `opentitan\hw\ip\edn\rtl\edn.sv`
  - `edn`:L9 — `opentitan\hw\ip\edn\rtl\edn.sv`
  - `edn_reg_pkg`:L22 — `opentitan\hw\ip\edn\rtl\edn_reg_top.sv`
  - `edn_core`:L65 — `opentitan\hw\ip\edn\rtl\edn.sv`
  - `edn_ack_sm.sv`:L1 — `opentitan\hw\ip\edn\rtl\edn_ack_sm.sv`
  - `edn_ack_sm`:L10 — `opentitan\hw\ip\edn\rtl\edn_ack_sm.sv`
  - `edn_core.sv`:L1 — `opentitan\hw\ip\edn\rtl\edn_core.sv`
  - `edn_core`:L13 — `opentitan\hw\ip\edn\rtl\edn_core.sv`
  - `edn_main_sm`:L755 — `opentitan\hw\ip\edn\rtl\edn_core.sv`
  - `edn_field_en.sv`:L1 — `opentitan\hw\ip\edn\rtl\edn_field_en.sv`
  - `edn_field_en`:L14 — `opentitan\hw\ip\edn\rtl\edn_field_en.sv`
  - `edn_main_sm.sv`:L1 — `opentitan\hw\ip\edn\rtl\edn_main_sm.sv`
  - `edn_main_sm`:L11 — `opentitan\hw\ip\edn\rtl\edn_main_sm.sv`
  - `edn_pkg.sv`:L1 — `opentitan\hw\ip\edn\rtl\edn_pkg.sv`
  - `edn_reg_pkg.sv`:L1 — `opentitan\hw\ip\edn\rtl\edn_reg_pkg.sv`
  - `edn_reg_top.sv`:L1 — `opentitan\hw\ip\edn\rtl\edn_reg_top.sv`
  - `edn_reg_top`:L9 — `opentitan\hw\ip\edn\rtl\edn_reg_top.sv`
  - `edn`:L2692 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
**DV** (21)
  - `csrng_agent_pkg`:L14 — `opentitan\hw\ip\edn\dv\cov\edn_cov_if.sv`
  - `tb.sv`:L1 — `opentitan\hw\ip\edn\dv\tb.sv`
  - `edn_env_pkg`:L9 — `opentitan\hw\ip\edn\dv\tests\edn_test_pkg.sv`
  - `edn_test_pkg`:L10 — `opentitan\hw\ip\edn\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\edn\dv\tb.sv`
  - `csrng_if`:L29 — `opentitan\hw\ip\edn\dv\tb.sv`
  - `edn_if`:L32 — `opentitan\hw\ip\edn\dv\tb.sv`
  - `edn_cov_bind.sv`:L1 — `opentitan\hw\ip\edn\dv\cov\edn_cov_bind.sv`
  - `edn_cov_bind`:L6 — `opentitan\hw\ip\edn\dv\cov\edn_cov_bind.sv`
  - `edn_cov_if.sv`:L1 — `opentitan\hw\ip\edn\dv\cov\edn_cov_if.sv`
  - `edn_alert_test.sv`:L1 — `opentitan\hw\ip\edn\dv\tests\edn_alert_test.sv`
  - `edn_base_test.sv`:L1 — `opentitan\hw\ip\edn\dv\tests\edn_base_test.sv`
  - `edn_disable_auto_req_mode_test.sv`:L1 — `opentitan\hw\ip\edn\dv\tests\edn_disable_auto_req_mode_test.sv`
  - `edn_disable_test.sv`:L1 — `opentitan\hw\ip\edn\dv\tests\edn_disable_test.sv`
  - `edn_err_test.sv`:L1 — `opentitan\hw\ip\edn\dv\tests\edn_err_test.sv`
  - `edn_genbits_test.sv`:L1 — `opentitan\hw\ip\edn\dv\tests\edn_genbits_test.sv`
  - `edn_intr_test.sv`:L1 — `opentitan\hw\ip\edn\dv\tests\edn_intr_test.sv`
  - `edn_regwen_test.sv`:L1 — `opentitan\hw\ip\edn\dv\tests\edn_regwen_test.sv`
  - `edn_smoke_test.sv`:L1 — `opentitan\hw\ip\edn\dv\tests\edn_smoke_test.sv`
  - `edn_stress_all_test.sv`:L1 — `opentitan\hw\ip\edn\dv\tests\edn_stress_all_test.sv`
**SVA** (3)
  - `edn_assert_if.sv`:L1 — `opentitan\hw\ip\edn\dv\sva\edn_assert_if.sv`
  - `edn_bind.sv`:L1 — `opentitan\hw\ip\edn\dv\sva\edn_bind.sv`
  - `edn_bind`:L5 — `opentitan\hw\ip\edn\dv\sva\edn_bind.sv`

## Neighbor Components

- `rv_plic` (6 refs; instantiates×6)
- `lowrisc_ibex` (4 refs; instantiates×2, imports_from×2)
- `otbn` (4 refs; imports_from×4)
- `pwrmgr` (3 refs; instantiates×3)
- `rv_core_ibex` (2 refs; imports_from×2)
- `rstmgr` (2 refs; instantiates×1, imports_from×1)
- `prim` (1 refs; instantiates×1)
- `flash_ctrl` (1 refs; instantiates×1)
- `pulp_riscv_dbg` (1 refs; instantiates×1)
- `ast` (1 refs; instantiates×1)
- `clkmgr` (1 refs; instantiates×1)
- `csrng` (1 refs; imports_from×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:edn` | `edn_disable_auto_req_mode_test.sv` | `opentitan\hw\ip\edn\dv\tests\edn_disable_auto_req_mode_test.sv` |
| `spec_component_matches_code` | `component:edn` | `edn` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_stress_all_test.sv` | `opentitan\hw\ip\edn\dv\tests\edn_stress_all_test.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_disable_test.sv` | `opentitan\hw\ip\edn\dv\tests\edn_disable_test.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_genbits_test.sv` | `opentitan\hw\ip\edn\dv\tests\edn_genbits_test.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_regwen_test.sv` | `opentitan\hw\ip\edn\dv\tests\edn_regwen_test.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_alert_test.sv` | `opentitan\hw\ip\edn\dv\tests\edn_alert_test.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_smoke_test.sv` | `opentitan\hw\ip\edn\dv\tests\edn_smoke_test.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_base_test.sv` | `opentitan\hw\ip\edn\dv\tests\edn_base_test.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_intr_test.sv` | `opentitan\hw\ip\edn\dv\tests\edn_intr_test.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_env_pkg` | `opentitan\hw\ip\edn\dv\tests\edn_test_pkg.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_err_test.sv` | `opentitan\hw\ip\edn\dv\tests\edn_err_test.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_test_pkg.sv` | `opentitan\hw\ip\edn\dv\tests\edn_test_pkg.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_assert_if.sv` | `opentitan\hw\ip\edn\dv\sva\edn_assert_if.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_cov_bind.sv` | `opentitan\hw\ip\edn\dv\cov\edn_cov_bind.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_cov_bind` | `opentitan\hw\ip\edn\dv\cov\edn_cov_bind.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_cov_if.sv` | `opentitan\hw\ip\edn\dv\cov\edn_cov_if.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_field_en.sv` | `opentitan\hw\ip\edn\rtl\edn_field_en.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_field_en` | `opentitan\hw\ip\edn\rtl\edn_field_en.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_bind.sv` | `opentitan\hw\ip\edn\dv\sva\edn_bind.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_bind` | `opentitan\hw\ip\edn\dv\sva\edn_bind.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_reg_pkg` | `opentitan\hw\ip\edn\rtl\edn_reg_top.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_main_sm.sv` | `opentitan\hw\ip\edn\rtl\edn_main_sm.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_main_sm` | `opentitan\hw\ip\edn\rtl\edn_main_sm.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_reg_pkg.sv` | `opentitan\hw\ip\edn\rtl\edn_reg_pkg.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_reg_top.sv` | `opentitan\hw\ip\edn\rtl\edn_reg_top.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_reg_top` | `opentitan\hw\ip\edn\rtl\edn_reg_top.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_ack_sm.sv` | `opentitan\hw\ip\edn\rtl\edn_ack_sm.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_ack_sm` | `opentitan\hw\ip\edn\rtl\edn_ack_sm.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_core.sv` | `opentitan\hw\ip\edn\rtl\edn_core.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_core` | `opentitan\hw\ip\edn\rtl\edn_core.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_main_sm` | `opentitan\hw\ip\edn\rtl\edn_core.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_pkg.sv` | `opentitan\hw\ip\edn\rtl\edn_pkg.sv` |
| `spec_component_matches_code` | `component:edn` | `edn.sv` | `opentitan\hw\ip\edn\rtl\edn.sv` |
| `spec_component_matches_code` | `component:edn` | `edn` | `opentitan\hw\ip\edn\rtl\edn.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_core` | `opentitan\hw\ip\edn\rtl\edn.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_test_pkg` | `opentitan\hw\ip\edn\dv\tb.sv` |
| `spec_component_matches_code` | `component:edn` | `edn_if` | `opentitan\hw\ip\edn\dv\tb.sv` |
| `spec_component_matches_code` | `component:edn` | `csrng_agent_pkg` | `opentitan\hw\ip\edn\dv\cov\edn_cov_if.sv` |
| `spec_component_matches_code` | `component:edn` | `tb.sv` | `opentitan\hw\ip\edn\dv\tb.sv` |
| `spec_path_matches_code_path` | `edn.hjson` | `csrng_agent_pkg` | `opentitan\hw\ip\edn\dv\cov\edn_cov_if.sv` |
| `spec_path_matches_code_path` | `edn.hjson` | `tb.sv` | `opentitan\hw\ip\edn\dv\tb.sv` |
| `spec_path_matches_code_path` | `edn.hjson` | `edn_env_pkg` | `opentitan\hw\ip\edn\dv\tests\edn_test_pkg.sv` |
| `spec_path_matches_code_path` | `edn.hjson` | `edn_test_pkg` | `opentitan\hw\ip\edn\dv\tb.sv` |
| `spec_path_matches_code_path` | `edn.hjson` | `tb` | `opentitan\hw\ip\edn\dv\tb.sv` |
| `spec_path_matches_code_path` | `edn.hjson` | `csrng_if` | `opentitan\hw\ip\edn\dv\tb.sv` |
| `spec_path_matches_code_path` | `edn.hjson` | `edn_if` | `opentitan\hw\ip\edn\dv\tb.sv` |
| `spec_path_matches_code_path` | `edn.hjson` | `edn_cov_bind.sv` | `opentitan\hw\ip\edn\dv\cov\edn_cov_bind.sv` |
| `spec_path_matches_code_path` | `edn_sec_cm_testplan.hjson` | `csrng_agent_pkg` | `opentitan\hw\ip\edn\dv\cov\edn_cov_if.sv` |
| `spec_path_matches_code_path` | `edn_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\edn\dv\tb.sv` |
| `spec_path_matches_code_path` | `edn_sec_cm_testplan.hjson` | `edn_env_pkg` | `opentitan\hw\ip\edn\dv\tests\edn_test_pkg.sv` |
| `spec_path_matches_code_path` | `edn_sec_cm_testplan.hjson` | `edn_test_pkg` | `opentitan\hw\ip\edn\dv\tb.sv` |
| `spec_path_matches_code_path` | `edn_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\edn\dv\tb.sv` |
| `spec_path_matches_code_path` | `edn_sec_cm_testplan.hjson` | `csrng_if` | `opentitan\hw\ip\edn\dv\tb.sv` |
| `spec_path_matches_code_path` | `edn_sec_cm_testplan.hjson` | `edn_if` | `opentitan\hw\ip\edn\dv\tb.sv` |
| `spec_path_matches_code_path` | `edn_sec_cm_testplan.hjson` | `edn_cov_bind.sv` | `opentitan\hw\ip\edn\dv\cov\edn_cov_bind.sv` |
| `spec_path_matches_code_path` | `edn_testplan.hjson` | `csrng_agent_pkg` | `opentitan\hw\ip\edn\dv\cov\edn_cov_if.sv` |
| `spec_path_matches_code_path` | `edn_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\edn\dv\tb.sv` |
| `spec_path_matches_code_path` | `edn_testplan.hjson` | `edn_env_pkg` | `opentitan\hw\ip\edn\dv\tests\edn_test_pkg.sv` |
| `spec_path_matches_code_path` | `edn_testplan.hjson` | `edn_test_pkg` | `opentitan\hw\ip\edn\dv\tb.sv` |

## Retrieval Guidance

- For code-only queries mentioning `edn`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `edn`.
