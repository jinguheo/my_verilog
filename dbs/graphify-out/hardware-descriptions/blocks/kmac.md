# Hardware Description: kmac

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`kmac`** has the following hardware interfaces defined
- **Inter-Module Signals**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`kmac`** has the following hardware interfaces defined

## Identity

- `ip_block`: `kmac`
- `bridge_edge_count`: 112
- Spec categories: document: 89, component: 41, testplan: 28, theory: 19, interface: 14
- Code categories: dv: 260, rtl: 96, other_code: 7, sva: 5
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/kmac/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/kmac/data/kmac.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`kmac`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_edn_i`**
- Bus Device Interfaces (TL
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/kmac/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/kmac/data/kmac.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`kmac`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_edn_i`**
- Bus Device Interfaces (TL-UL): **`tl`**
- Bus Ho
…
```

### Interrupts
_Source: `opentitan/hw/ip/kmac/doc/interfaces.md`_

```
| keymgr_key     | keymgr_pkg::hw_key_req | uni     | rcv   | 1          |               |
| app            | kmac_pkg::app          | req_rsp | rsp   | NumAppIntf |               |
| entropy        | edn_pkg::edn           | req_rsp | req   | 1          |               |
| idle           | prim_mubi_pkg::mubi4   | uni     | req   | 1          |               |
| en_masking     | logic
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/kmac/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

The software can update the KMAC/SHA3 configurations only when the IP is in the idle state.
The software should check [`STATUS.sha3_idle`](registers.md#status) before updating the configurations.
The software must first program [`CFG_SHADOWED.msg_endianness`](registers.md#cfg_shadowed) and [`CFG_SHADOWED.state_endianness`](registers.md#cfg_shadowed) at the
…
```

### Initialization
_Source: `opentitan/hw/ip/kmac/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

The software can update the KMAC/SHA3 configurations only when the IP is in the idle state.
The software should check [`STATUS.sha3_idle`](registers.md#status) before updating the configurations.
The software must first program [`CFG_SHADOWED.msg_endianness`](registers.md#cfg_shadowed) and [`CFG_SHADOWED.state_endianness`](registers.md#cfg_shadowed) at the
…
```

### Software Initiated KMAC/SHA3 process
_Source: `opentitan/hw/ip/kmac/doc/programmers_guide.md`_

```
## Initialization

The software can update the KMAC/SHA3 configurations only when the IP is in the idle state.
The software should check [`STATUS.sha3_idle`](registers.md#status) before updating the configurations.
The software must first program [`CFG_SHADOWED.msg_endianness`](registers.md#cfg_shadowed) and [`CFG_SHADOWED.state_endianness`](registers.md#cfg_shadowed) at the initialization stage.
…
```

### Summary
_Source: `opentitan/hw/ip/kmac/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/kmac/data/kmac.hjson -->
## Summary

| Name                                                                             | Offset   |   Length | Description                                                               |
|:---------------------------------------------------------------------------------|:---------|---------:|:---------------
…
```

### INTR STATE
_Source: `opentitan/hw/ip/kmac/doc/registers.md`_

```
| kmac.[`PREFIX_7`](#prefix)                                                       | 0xd0     |        4 | cSHAKE Prefix register.                                                   |
| kmac.[`PREFIX_8`](#prefix)                                                       | 0xd4     |        4 | cSHAKE Prefix register.                                                   |
| kmac.[`PREFIX_9`](#prefix)
…
```

## Spec Anchors

- `component:kmac` (L1) — `__graphify_spec_only__/components.md`
- `kmac.hjson` (L1) — `opentitan/hw/ip/kmac/data/kmac.hjson`
- `human name` (L7) — `opentitan/hw/ip/kmac/data/kmac.hjson`
- `one line desc` (L8) — `opentitan/hw/ip/kmac/data/kmac.hjson`
- `one paragraph desc` (L9) — `opentitan/hw/ip/kmac/data/kmac.hjson`
- `cip id` (L20) — `opentitan/hw/ip/kmac/data/kmac.hjson`
- `design spec` (L21) — `opentitan/hw/ip/kmac/data/kmac.hjson`
- `dv doc` (L22) — `opentitan/hw/ip/kmac/data/kmac.hjson`
- `hw checklist` (L23) — `opentitan/hw/ip/kmac/data/kmac.hjson`
- `sw checklist` (L24) — `opentitan/hw/ip/kmac/data/kmac.hjson`
- `revisions` (L25) — `opentitan/hw/ip/kmac/data/kmac.hjson`
- `version` (L27) — `opentitan/hw/ip/kmac/data/kmac.hjson`
- `kmac_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/kmac/data/kmac_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/kmac/data/kmac_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/kmac/data/kmac_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/kmac/data/kmac_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/kmac/data/kmac_sec_cm_testplan.hjson`
- `kmac_testplan.hjson` (L1) — `opentitan/hw/ip/kmac/data/kmac_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/kmac/data/kmac_testplan.hjson`
- `testpoints` (L14) — `opentitan/hw/ip/kmac/data/kmac_testplan.hjson`
- `desc` (L17) — `opentitan/hw/ip/kmac/data/kmac_testplan.hjson`
- `stage` (L46) — `opentitan/hw/ip/kmac/data/kmac_testplan.hjson`
- `tests` (L47) — `opentitan/hw/ip/kmac/data/kmac_testplan.hjson`
- `covergroups` (L285) — `opentitan/hw/ip/kmac/data/kmac_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/kmac/doc/checklist.md`
- `KMAC Checklist` (L1) — `opentitan/hw/ip/kmac/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/kmac/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/kmac/doc/checklist.md`
- `D2` (L32) — `opentitan/hw/ip/kmac/doc/checklist.md`
- `D2S` (L74) — `opentitan/hw/ip/kmac/doc/checklist.md`
- `D3` (L94) — `opentitan/hw/ip/kmac/doc/checklist.md`
- `Verification Checklist` (L120) — `opentitan/hw/ip/kmac/doc/checklist.md`
- `V1` (L122) — `opentitan/hw/ip/kmac/doc/checklist.md`
- `V2` (L173) — `opentitan/hw/ip/kmac/doc/checklist.md`
- `V2S` (L219) — `opentitan/hw/ip/kmac/doc/checklist.md`

## Code Evidence

**RTL** (3)
  - `sha3`:L199 — `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv`
  - `kmac_reg_pkg`:L31 — `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv`
  - `sha3_pkg`:L10 — `opentitan\hw\ip\kmac\rtl\sha3pad.sv`
**DV** (46)
  - `tb.sv`:L1 — `opentitan\hw\ip\kmac\dv\tb.sv`
  - `kmac_env_pkg`:L9 — `opentitan\hw\ip\kmac\dv\tests\kmac_test_pkg.sv`
  - `kmac_test_pkg`:L10 — `opentitan\hw\ip\kmac\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\kmac\dv\tb.sv`
  - `kmac_if`:L28 — `opentitan\hw\ip\kmac\dv\tb.sv`
  - `kmac_cov_bind.sv`:L1 — `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv`
  - `kmac_cov_bind`:L5 — `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv`
  - `kmac_cov_if.sv`:L1 — `opentitan\hw\ip\kmac\dv\cov\kmac_cov_if.sv`
  - `digestpp_dpi.cc`:L1 — `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
  - `load_arr_from_simulator()`:L25 — `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
  - `write_array_to_simulator()`:L37 — `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
  - `get_sha3_digest()`:L54 — `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
  - `c_dpi_sha3_224()`:L81 — `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
  - `c_dpi_sha3_256()`:L89 — `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
  - `c_dpi_sha3_384()`:L97 — `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
  - `c_dpi_sha3_512()`:L105 — `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
  - `c_dpi_shake128()`:L113 — `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
  - `c_dpi_shake256()`:L137 — `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
  - `c_dpi_cshake128()`:L161 — `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
  - `c_dpi_cshake256()`:L189 — `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
**SVA** (1)
  - `sha3pad_assert_if.sv`:L1 — `opentitan\hw\ip\kmac\dv\cov\sha3pad_assert_if.sv`

## Neighbor Components

- `riscv-tests` (76 refs; calls×76)
- `lowrisc_ibex` (8 refs; calls×5, instantiates×2, imports_from×1)
- `flash_ctrl` (8 refs; instantiates×8)
- `rv_core_ibex` (7 refs; instantiates×5, imports_from×2)
- `rv_plic` (6 refs; instantiates×6)
- `otbn` (4 refs; calls×3, instantiates×1)
- `verilator_sim_ctrl.cc` (3 refs; calls×3)
- `rstmgr` (3 refs; instantiates×2, imports_from×1)
- `pwrmgr` (3 refs; instantiates×3)
- `aes` (3 refs; calls×3)
- `prim` (2 refs; instantiates×2)
- `primitive.rs` (2 refs; calls×2)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:kmac` | `kmac_reduced_tb.sv` | `opentitan\hw\ip\kmac\pre_dv\kmac_reduced_tb\rtl\kmac_reduced_tb.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reduced_tb` | `opentitan\hw\ip\kmac\pre_dv\kmac_reduced_tb\rtl\kmac_reduced_tb.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_base_test.sv` | `opentitan\hw\ip\kmac\dv\tests\kmac_base_test.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_env_pkg` | `opentitan\hw\ip\kmac\dv\tests\kmac_test_pkg.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_test_pkg.sv` | `opentitan\hw\ip\kmac\dv\tests\kmac_test_pkg.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_cov_bind.sv` | `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_cov_bind` | `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_cov_if.sv` | `opentitan\hw\ip\kmac\dv\cov\kmac_cov_if.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reg_pkg` | `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_bind.sv` | `opentitan\hw\ip\kmac\dv\sva\kmac_bind.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_bind` | `opentitan\hw\ip\kmac\dv\sva\kmac_bind.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_pkg` | `opentitan\hw\ip\kmac\rtl\kmac_staterd.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_entropy.sv` | `opentitan\hw\ip\kmac\rtl\kmac_entropy.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_entropy` | `opentitan\hw\ip\kmac\rtl\kmac_entropy.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_msgfifo.sv` | `opentitan\hw\ip\kmac\rtl\kmac_msgfifo.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_msgfifo` | `opentitan\hw\ip\kmac\rtl\kmac_msgfifo.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reduced.sv` | `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reduced` | `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_entropy` | `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reg_pkg.sv` | `opentitan\hw\ip\kmac\rtl\kmac_reg_pkg.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reg_top.sv` | `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reg_top` | `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_staterd.sv` | `opentitan\hw\ip\kmac\rtl\kmac_staterd.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_staterd` | `opentitan\hw\ip\kmac\rtl\kmac_staterd.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_errchk.sv` | `opentitan\hw\ip\kmac\rtl\kmac_errchk.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_errchk` | `opentitan\hw\ip\kmac\rtl\kmac_errchk.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_core.sv` | `opentitan\hw\ip\kmac\rtl\kmac_core.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_core` | `opentitan\hw\ip\kmac\rtl\kmac_core.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_app.sv` | `opentitan\hw\ip\kmac\rtl\kmac_app.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_app` | `opentitan\hw\ip\kmac\rtl\kmac_app.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_pkg.sv` | `opentitan\hw\ip\kmac\rtl\kmac_pkg.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac.sv` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_core` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_app` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_msgfifo` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_staterd` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_errchk` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reg_top` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `sha3` | `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `tb.sv` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `kmac_env_pkg` | `opentitan\hw\ip\kmac\dv\tests\kmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `kmac_test_pkg` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `kmac_reg_pkg` | `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `tb` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `kmac_if` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `kmac_cov_bind.sv` | `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `sha3` | `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `kmac_env_pkg` | `opentitan\hw\ip\kmac\dv\tests\kmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `kmac_test_pkg` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `kmac_reg_pkg` | `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `kmac_if` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `kmac_cov_bind.sv` | `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv` |
| `spec_path_matches_code_path` | `kmac_testplan.hjson` | `sha3` | `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv` |
| `spec_path_matches_code_path` | `kmac_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac_testplan.hjson` | `kmac_env_pkg` | `opentitan\hw\ip\kmac\dv\tests\kmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `kmac_testplan.hjson` | `kmac_test_pkg` | `opentitan\hw\ip\kmac\dv\tb.sv` |

## Retrieval Guidance

- For code-only queries mentioning `kmac`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `kmac`.
