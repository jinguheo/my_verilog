# Hardware Description: hmac

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`hmac`** has the following hardware interfaces defined
- **Inter-Module Signals**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`hmac`** has the following hardware interfaces defined

## Identity

- `ip_block`: `hmac`
- `bridge_edge_count`: 112
- Spec categories: document: 87, component: 41, testplan: 28, theory: 17, interface: 15
- Code categories: dv: 95, rtl: 32, other_code: 24, sva: 22
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/hmac/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/hmac/data/hmac.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`hmac`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/hmac/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/hmac/data/hmac.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`hmac`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfaces (TL-UL): **`tl`**
- Bus Host Interf
…
```

### Interrupts
_Source: `opentitan/hw/ip/hmac/doc/interfaces.md`_

```
## [Inter-Module Signals](https://opentitan.org/book/doc/contributing/hw/comportability/index.html#inter-signal-handling)

| Port Name   | Package::Struct      | Type    | Act   |   Width | Description   |
|:------------|:---------------------|:--------|:------|--------:|:--------------|
| idle        | prim_mubi_pkg::mubi4 | uni     | req   |       1 |               |
| tl          | tlul_pkg::tl
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/hmac/doc/programmers_guide.md`_

```
# Programmer's Guide

This chapter shows how to use the HMAC/SHA-2 IP by showing some snippets such as initialization, initiating SHA-2 or HMAC process and processing the interrupts.
This code is not compilable but serves to demonstrate the IO required.
A more detailed SW implementation can be found in software under `sw/` in [cryptolib code](../../../../sw/device/lib/crypto/drivers/hmac.c) which
…
```

### Initialization
_Source: `opentitan/hw/ip/hmac/doc/programmers_guide.md`_

```
# Programmer's Guide

This chapter shows how to use the HMAC/SHA-2 IP by showing some snippets such as initialization, initiating SHA-2 or HMAC process and processing the interrupts.
This code is not compilable but serves to demonstrate the IO required.
A more detailed SW implementation can be found in software under `sw/` in [cryptolib code](../../../../sw/device/lib/crypto/drivers/hmac.c) which
…
```

### Triggering HMAC/SHA-2 engine
_Source: `opentitan/hw/ip/hmac/doc/programmers_guide.md`_

```
HMAC_KEY_3 = SECRET_KEY_3;
  HMAC_KEY_4 = SECRET_KEY_4;
  HMAC_KEY_5 = SECRET_KEY_5;
  HMAC_KEY_6 = SECRET_KEY_6;
  HMAC_KEY_7 = SECRET_KEY_7;
}
```

## Triggering HMAC/SHA-2 engine

The following code shows how to send a message to the HMAC, the procedure is the same whether a full HMAC or just a SHA-2 computation is required (choose between them using [`CFG.hmac_en`](registers.md#cfg)).
In both
…
```

### Summary
_Source: `opentitan/hw/ip/hmac/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/ip/hmac/data/hmac.hjson -->
## Summary

| Name                                         | Offset   |   Length | Description                                                          |
|:---------------------------------------------|:---------|---------:|:---------------------------------------------------------------------|
| hmac.[`INTR_STATE`]
…
```

### INTR STATE
_Source: `opentitan/hw/ip/hmac/doc/registers.md`_

```
| hmac.[`DIGEST_12`](#digest)                  | 0xd4     |        4 | Digest output.                                                       |
| hmac.[`DIGEST_13`](#digest)                  | 0xd8     |        4 | Digest output.                                                       |
| hmac.[`DIGEST_14`](#digest)                  | 0xdc     |        4 | Digest output.
…
```

## Spec Anchors

- `component:hmac` (L1) — `__graphify_spec_only__/components.md`
- `hmac.hjson` (L1) — `opentitan/hw/ip/hmac/data/hmac.hjson`
- `human name` (L6) — `opentitan/hw/ip/hmac/data/hmac.hjson`
- `one line desc` (L7) — `opentitan/hw/ip/hmac/data/hmac.hjson`
- `one paragraph desc` (L8) — `opentitan/hw/ip/hmac/data/hmac.hjson`
- `cip id` (L16) — `opentitan/hw/ip/hmac/data/hmac.hjson`
- `design spec` (L17) — `opentitan/hw/ip/hmac/data/hmac.hjson`
- `dv doc` (L18) — `opentitan/hw/ip/hmac/data/hmac.hjson`
- `hw checklist` (L19) — `opentitan/hw/ip/hmac/data/hmac.hjson`
- `sw checklist` (L20) — `opentitan/hw/ip/hmac/data/hmac.hjson`
- `revisions` (L21) — `opentitan/hw/ip/hmac/data/hmac.hjson`
- `version` (L23) — `opentitan/hw/ip/hmac/data/hmac.hjson`
- `hmac_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/hmac/data/hmac_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/hmac/data/hmac_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/hmac/data/hmac_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/hmac/data/hmac_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/hmac/data/hmac_sec_cm_testplan.hjson`
- `hmac_testplan.hjson` (L1) — `opentitan/hw/ip/hmac/data/hmac_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/hmac/data/hmac_testplan.hjson`
- `testpoints` (L12) — `opentitan/hw/ip/hmac/data/hmac_testplan.hjson`
- `desc` (L15) — `opentitan/hw/ip/hmac/data/hmac_testplan.hjson`
- `stage` (L27) — `opentitan/hw/ip/hmac/data/hmac_testplan.hjson`
- `tests` (L28) — `opentitan/hw/ip/hmac/data/hmac_testplan.hjson`
- `covergroups` (L163) — `opentitan/hw/ip/hmac/data/hmac_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/hmac/doc/checklist.md`
- `HMAC Checklist` (L1) — `opentitan/hw/ip/hmac/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/hmac/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/hmac/doc/checklist.md`
- `D2` (L34) — `opentitan/hw/ip/hmac/doc/checklist.md`
- `D2S` (L77) — `opentitan/hw/ip/hmac/doc/checklist.md`
- `D3` (L97) — `opentitan/hw/ip/hmac/doc/checklist.md`
- `Verification Checklist` (L125) — `opentitan/hw/ip/hmac/doc/checklist.md`
- `V1` (L127) — `opentitan/hw/ip/hmac/doc/checklist.md`
- `V2` (L177) — `opentitan/hw/ip/hmac/doc/checklist.md`
- `V2S` (L223) — `opentitan/hw/ip/hmac/doc/checklist.md`

## Code Evidence

**RTL** (1)
  - `prim_sha2_32`:L725 — `opentitan\hw\ip\hmac\rtl\hmac.sv`
**DV** (42)
  - `cryptoc_dpi.c`:L1 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
  - `collect_bytes()`:L22 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
  - `c_dpi_SHA_hash()`:L58 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
  - `c_dpi_SHA256_hash()`:L71 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
  - `c_dpi_SHA384_hash()`:L87 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
  - `c_dpi_SHA512_hash()`:L103 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
  - `c_dpi_HMAC_SHA()`:L119 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
  - `c_dpi_HMAC_SHA256()`:L137 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
  - `c_dpi_HMAC_SHA384()`:L158 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
  - `c_dpi_HMAC_SHA512()`:L180 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
  - `cryptoc_dpi_pkg.sv`:L1 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi_pkg.sv`
  - `hash-internal.h`:L1 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hash-internal.h`
  - `hmac.c`:L1 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac.c`
  - `HMAC_init_LITE()`:L48 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac.c`
  - `HMAC_SHA384_init()`:L83 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac.c`
  - `HMAC_SHA512_init()`:L88 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac.c`
  - `HMAC_final_LITE()`:L93 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac.c`
  - `hmac.h`:L1 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac.h`
  - `hmac_wrap.c`:L1 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac_wrap.c`
  - `HMAC_SHA()`:L14 — `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac_wrap.c`
**SVA** (2)
  - `hmac_bind.sv`:L1 — `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv`
  - `hmac_bind`:L5 — `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv`
**OTHER_CODE** (5)
  - `hmac_model.py`:L1 — `opentitan\hw\ip\hmac\model\hmac_model.py`
  - `rotr()`:L37 — `opentitan\hw\ip\hmac\model\hmac_model.py`
  - `shiftr()`:L41 — `opentitan\hw\ip\hmac\model\hmac_model.py`
  - `sha256()`:L45 — `opentitan\hw\ip\hmac\model\hmac_model.py`
  - `_hmac()`:L114 — `opentitan\hw\ip\hmac\model\hmac_model.py`

## Neighbor Components

- `cryptoc` (40 refs; contains×25, calls×15)
- `riscv-tests` (26 refs; calls×26)
- `rv_plic` (6 refs; instantiates×6)
- `lowrisc_ibex` (3 refs; calls×1, instantiates×1, imports_from×1)
- `prim` (3 refs; imports_from×2, instantiates×1)
- `pwrmgr` (2 refs; instantiates×2)
- `otbn` (2 refs; calls×2)
- `pulp_riscv_dbg` (1 refs; instantiates×1)
- `gpio` (1 refs; imports_from×1)
- `rstmgr` (1 refs; imports_from×1)
- `dma` (1 refs; instantiates×1)
- `kmac` (1 refs; calls×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:hmac` | `hmac` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_base_test.sv` | `opentitan\hw\ip\hmac\dv\tests\hmac_base_test.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_env_pkg` | `opentitan\hw\ip\hmac\dv\tests\hmac_test_pkg.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_test_pkg.sv` | `opentitan\hw\ip\hmac\dv\tests\hmac_test_pkg.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_bind.sv` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_bind` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_reg_pkg` | `opentitan\hw\ip\hmac\rtl\hmac_reg_top.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_reg_pkg.sv` | `opentitan\hw\ip\hmac\rtl\hmac_reg_pkg.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_reg_top.sv` | `opentitan\hw\ip\hmac\rtl\hmac_reg_top.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_reg_top` | `opentitan\hw\ip\hmac\rtl\hmac_reg_top.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_core.sv` | `opentitan\hw\ip\hmac\rtl\hmac_core.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_core` | `opentitan\hw\ip\hmac\rtl\hmac_core.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_test_pkg` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_if` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac.sv` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_core` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_reg_top` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_component_matches_code` | `component:hmac` | `cryptoc_dpi_pkg.sv` | `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi_pkg.sv` |
| `spec_component_matches_code` | `component:hmac` | `prim_sha2_32` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_component_matches_code` | `component:hmac` | `tb.sv` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:hmac` | `tb` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac.c` | `opentitan\sw\device\tests\crypto\cryptotest\firmware\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `handle_hmac()` | `opentitan\sw\device\tests\crypto\cryptotest\firmware\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac.h` | `opentitan\sw\device\tests\crypto\cryptotest\firmware\hmac.h` |
| `spec_component_matches_code` | `component:hmac` | `hmac_base()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac.c` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_configure()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `sc_hmac_hmac_sha256_configure()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_configure()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_start()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_update()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_update_words()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_process()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_final_truncated()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `sc_hmac_hmac_sha256()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_save()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_restore()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac.h` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.h` |
| `spec_path_matches_code_path` | `hmac.hjson` | `prim_sha2_32` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_path_matches_code_path` | `hmac.hjson` | `cryptoc_dpi_pkg.sv` | `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `hmac.hjson` | `hmac_bind.sv` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `hmac.hjson` | `hmac_bind` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `hmac.hjson` | `tb.sv` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `hmac.hjson` | `tb` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `hmac.hjson` | `hmac_env_pkg` | `opentitan\hw\ip\hmac\dv\tests\hmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `hmac.hjson` | `hmac_test_pkg` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `prim_sha2_32` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `cryptoc_dpi_pkg.sv` | `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `hmac_bind.sv` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `hmac_bind` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `hmac_env_pkg` | `opentitan\hw\ip\hmac\dv\tests\hmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `hmac_test_pkg` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `hmac_testplan.hjson` | `prim_sha2_32` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_path_matches_code_path` | `hmac_testplan.hjson` | `cryptoc_dpi_pkg.sv` | `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `hmac_testplan.hjson` | `hmac_bind.sv` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `hmac_testplan.hjson` | `hmac_bind` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |

## Retrieval Guidance

- For code-only queries mentioning `hmac`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `hmac`.
