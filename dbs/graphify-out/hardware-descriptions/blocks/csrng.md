# Hardware Description: csrng

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`csrng`** has the following hardware interfaces defined
- **Inter-Module Signals**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`csrng`** has the following hardware interfaces defined

## Identity

- `ip_block`: `csrng`
- `bridge_edge_count`: 112
- Spec categories: document: 88, component: 41, testplan: 30, theory: 19, interface: 16
- Code categories: dv: 83, rtl: 69, sva: 6
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Excerpts

### Interfaces
_Source: `opentitan/hw/ip/csrng/doc/interfaces.md`_

```
# Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/csrng/data/csrng.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`csrng`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`tl`**
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/csrng/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/csrng/data/csrng.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`csrng`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`tl`**
- Bus Host Int
…
```

### Interrupts
_Source: `opentitan/hw/ip/csrng/doc/interfaces.md`_

```
| Port Name                | Package::Struct                    | Type    | Act   |   Width | Description   |
|:-------------------------|:-----------------------------------|:--------|:------|--------:|:--------------|
| csrng_cmd                | csrng_pkg::csrng                   | req_rsp | rsp   |       2 |               |
| entropy_src_hw_if        | entropy_src_pkg::entropy_src_hw_if | req_
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/csrng/doc/programmers_guide.md`_

```
# Programmer's Guide

This section discusses how software can interface with CSRNG.

## Module enable and disable

CSRNG may only be disabled if all EDNs are disabled.
```

### Module enable and disable
_Source: `opentitan/hw/ip/csrng/doc/programmers_guide.md`_

```
# Programmer's Guide

This section discusses how software can interface with CSRNG.

## Module enable and disable

CSRNG may only be disabled if all EDNs are disabled.

The recommended enable sequence for the entropy complex is to first enable ENTROPY_SRC, then CSRNG, and finally the EDNs.

## Running CSRNG with ENTROPY_SRC disabled
```

### Running CSRNG with ENTROPY SRC disabled
_Source: `opentitan/hw/ip/csrng/doc/programmers_guide.md`_

```
This section discusses how software can interface with CSRNG.

## Module enable and disable

CSRNG may only be disabled if all EDNs are disabled.

The recommended enable sequence for the entropy complex is to first enable ENTROPY_SRC, then CSRNG, and finally the EDNs.

## Running CSRNG with ENTROPY_SRC disabled

Once the entropy complex has been enabled and all configured CSRNG instances have been
…
```

### Summary
_Source: `opentitan/hw/ip/csrng/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/csrng/data/csrng.hjson -->
## Summary

| Name                                                                  | Offset   |   Length | Description                                                                |
|:----------------------------------------------------------------------|:---------|---------:|:----------------------------------
…
```

### INTR STATE
_Source: `opentitan/hw/ip/csrng/doc/registers.md`_

```
| csrng.[`INT_STATE_VAL`](#int_state_val)                               | 0x44     |        4 | Internal state read access register                                        |
| csrng.[`FIPS_FORCE`](#fips_force)                                     | 0x48     |        4 | FIPS/CC compliance flag forcing register                                   |
| csrng.[`HW_EXC_STS`](#hw_exc_sts)
…
```

## Spec Anchors

- `component:csrng` (L1) — `__graphify_spec_only__/components.md`
- `csrng.hjson` (L1) — `opentitan/hw/ip/csrng/data/csrng.hjson`
- `human name` (L5) — `opentitan/hw/ip/csrng/data/csrng.hjson`
- `one line desc` (L6) — `opentitan/hw/ip/csrng/data/csrng.hjson`
- `one paragraph desc` (L7) — `opentitan/hw/ip/csrng/data/csrng.hjson`
- `cip id` (L18) — `opentitan/hw/ip/csrng/data/csrng.hjson`
- `design spec` (L19) — `opentitan/hw/ip/csrng/data/csrng.hjson`
- `dv doc` (L20) — `opentitan/hw/ip/csrng/data/csrng.hjson`
- `hw checklist` (L21) — `opentitan/hw/ip/csrng/data/csrng.hjson`
- `sw checklist` (L22) — `opentitan/hw/ip/csrng/data/csrng.hjson`
- `version` (L23) — `opentitan/hw/ip/csrng/data/csrng.hjson`
- `life stage` (L24) — `opentitan/hw/ip/csrng/data/csrng.hjson`
- `csrng_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/csrng/data/csrng_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/csrng/data/csrng_sec_cm_testplan.hjson`
- `desc` (L29) — `opentitan/hw/ip/csrng/data/csrng_sec_cm_testplan.hjson`
- `stage` (L35) — `opentitan/hw/ip/csrng/data/csrng_sec_cm_testplan.hjson`
- `tests` (L36) — `opentitan/hw/ip/csrng/data/csrng_sec_cm_testplan.hjson`
- `csrng_testplan.hjson` (L1) — `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `testpoints` (L12) — `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `desc` (L15) — `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `stage` (L20) — `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `tests` (L21) — `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `covergroups` (L103) — `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `Cross` (L115) — `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `genbits fips cp` (L192) — `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/csrng/doc/checklist.md`
- `CSRNG Checklist` (L1) — `opentitan/hw/ip/csrng/doc/checklist.md`
- `Design Checklist` (L11) — `opentitan/hw/ip/csrng/doc/checklist.md`
- `D1` (L13) — `opentitan/hw/ip/csrng/doc/checklist.md`
- `D2` (L37) — `opentitan/hw/ip/csrng/doc/checklist.md`
- `D2S` (L79) — `opentitan/hw/ip/csrng/doc/checklist.md`
- `D3` (L99) — `opentitan/hw/ip/csrng/doc/checklist.md`
- `Verification Checklist` (L125) — `opentitan/hw/ip/csrng/doc/checklist.md`
- `V1` (L127) — `opentitan/hw/ip/csrng/doc/checklist.md`

## Code Evidence

**RTL** (27)
  - `csrng_pkg`:L13 — `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv`
  - `aes_cipher_core`:L64 — `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv`
  - `csrng.sv`:L1 — `opentitan\hw\ip\csrng\rtl\csrng.sv`
  - `csrng`:L9 — `opentitan\hw\ip\csrng\rtl\csrng.sv`
  - `csrng_reg_pkg`:L14 — `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv`
  - `csrng_core`:L77 — `opentitan\hw\ip\csrng\rtl\csrng.sv`
  - `csrng_block_encrypt.sv`:L1 — `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv`
  - `csrng_block_encrypt`:L8 — `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv`
  - `csrng_cmd_stage.sv`:L1 — `opentitan\hw\ip\csrng\rtl\csrng_cmd_stage.sv`
  - `csrng_cmd_stage`:L9 — `opentitan\hw\ip\csrng\rtl\csrng_cmd_stage.sv`
  - `csrng_core.sv`:L1 — `opentitan\hw\ip\csrng\rtl\csrng_core.sv`
  - `csrng_core`:L9 — `opentitan\hw\ip\csrng\rtl\csrng_core.sv`
  - `csrng_main_sm`:L778 — `opentitan\hw\ip\csrng\rtl\csrng_core.sv`
  - `csrng_state_db`:L840 — `opentitan\hw\ip\csrng\rtl\csrng_core.sv`
  - `csrng_ctr_drbg`:L912 — `opentitan\hw\ip\csrng\rtl\csrng_core.sv`
  - `csrng_block_encrypt`:L950 — `opentitan\hw\ip\csrng\rtl\csrng_core.sv`
  - `csrng_ctr_drbg.sv`:L1 — `opentitan\hw\ip\csrng\rtl\csrng_ctr_drbg.sv`
  - `csrng_ctr_drbg`:L9 — `opentitan\hw\ip\csrng\rtl\csrng_ctr_drbg.sv`
  - `csrng_main_sm.sv`:L1 — `opentitan\hw\ip\csrng\rtl\csrng_main_sm.sv`
  - `csrng_main_sm`:L11 — `opentitan\hw\ip\csrng\rtl\csrng_main_sm.sv`
**DV** (17)
  - `tb.sv`:L1 — `opentitan\hw\ip\csrng\dv\tb.sv`
  - `csrng_env_pkg`:L9 — `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv`
  - `csrng_test_pkg`:L10 — `opentitan\hw\ip\csrng\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\csrng\dv\tb.sv`
  - `csrng_agents_if`:L36 — `opentitan\hw\ip\csrng\dv\tb.sv`
  - `csrng_path_if`:L39 — `opentitan\hw\ip\csrng\dv\tb.sv`
  - `csrng_cov_bind.sv`:L1 — `opentitan\hw\ip\csrng\dv\cov\csrng_cov_bind.sv`
  - `csrng_cov_bind`:L6 — `opentitan\hw\ip\csrng\dv\cov\csrng_cov_bind.sv`
  - `csrng_cov_if.sv`:L1 — `opentitan\hw\ip\csrng\dv\cov\csrng_cov_if.sv`
  - `csrng_alert_test.sv`:L1 — `opentitan\hw\ip\csrng\dv\tests\csrng_alert_test.sv`
  - `csrng_base_test.sv`:L1 — `opentitan\hw\ip\csrng\dv\tests\csrng_base_test.sv`
  - `csrng_cmds_test.sv`:L1 — `opentitan\hw\ip\csrng\dv\tests\csrng_cmds_test.sv`
  - `csrng_intr_test.sv`:L1 — `opentitan\hw\ip\csrng\dv\tests\csrng_intr_test.sv`
  - `csrng_regwen_test.sv`:L1 — `opentitan\hw\ip\csrng\dv\tests\csrng_regwen_test.sv`
  - `csrng_smoke_test.sv`:L1 — `opentitan\hw\ip\csrng\dv\tests\csrng_smoke_test.sv`
  - `csrng_stress_all_test.sv`:L1 — `opentitan\hw\ip\csrng\dv\tests\csrng_stress_all_test.sv`
  - `csrng_test_pkg.sv`:L1 — `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv`
**SVA** (3)
  - `csrng_assert_if.sv`:L1 — `opentitan\hw\ip\csrng\dv\sva\csrng_assert_if.sv`
  - `csrng_bind.sv`:L1 — `opentitan\hw\ip\csrng\dv\sva\csrng_bind.sv`
  - `csrng_bind`:L5 — `opentitan\hw\ip\csrng\dv\sva\csrng_bind.sv`

## Neighbor Components

- `rv_plic` (6 refs; instantiates×6)
- `lowrisc_ibex` (5 refs; instantiates×3, imports_from×2)
- `rv_core_ibex` (4 refs; imports_from×3, instantiates×1)
- `pwrmgr` (3 refs; instantiates×3)
- `flash_ctrl` (2 refs; instantiates×2)
- `rstmgr` (2 refs; instantiates×1, imports_from×1)
- `aes` (2 refs; instantiates×2)
- `prim` (1 refs; instantiates×1)
- `pulp_riscv_dbg` (1 refs; instantiates×1)
- `ast` (1 refs; instantiates×1)
- `clkmgr` (1 refs; instantiates×1)
- `edn` (1 refs; imports_from×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:csrng` | `csrng_stress_all_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_stress_all_test.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_regwen_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_regwen_test.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_alert_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_alert_test.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_smoke_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_smoke_test.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_base_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_base_test.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_cmds_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_cmds_test.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_intr_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_intr_test.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_env_pkg` | `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_test_pkg.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_block_encrypt.sv` | `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_block_encrypt` | `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_assert_if.sv` | `opentitan\hw\ip\csrng\dv\sva\csrng_assert_if.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_cov_bind.sv` | `opentitan\hw\ip\csrng\dv\cov\csrng_cov_bind.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_cov_bind` | `opentitan\hw\ip\csrng\dv\cov\csrng_cov_bind.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_cov_if.sv` | `opentitan\hw\ip\csrng\dv\cov\csrng_cov_if.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_cmd_stage.sv` | `opentitan\hw\ip\csrng\rtl\csrng_cmd_stage.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_cmd_stage` | `opentitan\hw\ip\csrng\rtl\csrng_cmd_stage.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_pkg` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_reg_pkg` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_ctr_drbg.sv` | `opentitan\hw\ip\csrng\rtl\csrng_ctr_drbg.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_ctr_drbg` | `opentitan\hw\ip\csrng\rtl\csrng_ctr_drbg.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_state_db.sv` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_state_db` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_bind.sv` | `opentitan\hw\ip\csrng\dv\sva\csrng_bind.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_bind` | `opentitan\hw\ip\csrng\dv\sva\csrng_bind.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_main_sm.sv` | `opentitan\hw\ip\csrng\rtl\csrng_main_sm.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_main_sm` | `opentitan\hw\ip\csrng\rtl\csrng_main_sm.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_reg_pkg.sv` | `opentitan\hw\ip\csrng\rtl\csrng_reg_pkg.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_reg_top.sv` | `opentitan\hw\ip\csrng\rtl\csrng_reg_top.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_reg_top` | `opentitan\hw\ip\csrng\rtl\csrng_reg_top.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_core.sv` | `opentitan\hw\ip\csrng\rtl\csrng_core.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_core` | `opentitan\hw\ip\csrng\rtl\csrng_core.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_main_sm` | `opentitan\hw\ip\csrng\rtl\csrng_core.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_state_db` | `opentitan\hw\ip\csrng\rtl\csrng_core.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_ctr_drbg` | `opentitan\hw\ip\csrng\rtl\csrng_core.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_block_encrypt` | `opentitan\hw\ip\csrng\rtl\csrng_core.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_pkg.sv` | `opentitan\hw\ip\csrng\rtl\csrng_pkg.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng.sv` | `opentitan\hw\ip\csrng\rtl\csrng.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng` | `opentitan\hw\ip\csrng\rtl\csrng.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `csrng_pkg` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `aes_cipher_core` | `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `tb.sv` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `csrng_env_pkg` | `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `csrng_test_pkg` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `tb` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `csrng_agents_if` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `csrng_path_if` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `csrng_pkg` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `aes_cipher_core` | `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `csrng_env_pkg` | `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `csrng_test_pkg` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `csrng_agents_if` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `csrng_path_if` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_testplan.hjson` | `csrng_pkg` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_path_matches_code_path` | `csrng_testplan.hjson` | `aes_cipher_core` | `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv` |
| `spec_path_matches_code_path` | `csrng_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_testplan.hjson` | `csrng_env_pkg` | `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv` |

## Retrieval Guidance

- For code-only queries mentioning `csrng`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `csrng`.
