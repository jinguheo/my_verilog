# Hardware Description: sram_ctrl

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: The following table lists the instantiation parameters of the SRAM controller.
- **Parameters**: The following table lists the instantiation parameters of the SRAM controller.
- **Signals**: `AlertAsyncOn` | 1'b1 | 1'b1 |

## Identity

- `ip_block`: `sram_ctrl`
- `bridge_edge_count`: 102
- Spec categories: document: 79, component: 31, testplan: 28, interface: 19, theory: 18
- Code categories: dv: 61, rtl: 54, other_code: 12, sva: 4
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 30

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/sram_ctrl/doc/interfaces.md`_

```
# Hardware Interfaces

## Parameters

The following table lists the instantiation parameters of the SRAM controller.

Parameter                   | Default               | Top Earlgrey      | Description
----------------------------|-----------------------|-------------------|---------------
```

### Parameters
_Source: `opentitan/hw/ip/sram_ctrl/doc/interfaces.md`_

```
# Hardware Interfaces

## Parameters

The following table lists the instantiation parameters of the SRAM controller.

Parameter                   | Default               | Top Earlgrey      | Description
----------------------------|-----------------------|-------------------|---------------
`AlertAsyncOn`              | 1'b1                  | 1'b1              |
`InstrExec`                 | 1
…
```

### Signals
_Source: `opentitan/hw/ip/sram_ctrl/doc/interfaces.md`_

```
`AlertAsyncOn`              | 1'b1                  | 1'b1              |
`InstrExec`                 | 1                     | 1                 | Enables the execute from SRAM feature.
`MemSizeRam`                | 4096                  | (multiple values) | Number of 32bit words in the SRAM (can be overridden by `topgen`).
`RndCnstSramKey`            | (see RTL)             | (see RTL)
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/sram_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

The memory inside the SRAM controller can be used right away after a system reset.
However, since the scrambling key defaults to a predefined value, it is recommended that SW performs the following initialization steps as early in the boot process as possible.

1. Request an updated ephemeral scrambling key from OTP by writing 0x1 to [`CTRL.RENEW_SCR_KEY`](
…
```

### Initialization
_Source: `opentitan/hw/ip/sram_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

## Initialization

The memory inside the SRAM controller can be used right away after a system reset.
However, since the scrambling key defaults to a predefined value, it is recommended that SW performs the following initialization steps as early in the boot process as possible.

1. Request an updated ephemeral scrambling key from OTP by writing 0x1 to [`CTRL.RENEW_SCR_KEY`](
…
```

### Device Interface Functions DIFs
_Source: `opentitan/hw/ip/sram_ctrl/doc/programmers_guide.md`_

```
4. (optional) Lock down write access to [`CTRL`](registers.md#ctrl) by writing to [`CTRL_REGWEN`](registers.md#ctrl_regwen) if future key renewals and initializations should be disallowed until the next system reset.

Note that before (re-)requesting an updated SRAM key it is imperative to make sure that:
- The memory contents are not needed anymore. Requesting a key implicitly wipes all data in t
…
```

### Summary of the regs interface's registers
_Source: `opentitan/hw/ip/sram_ctrl/doc/registers.md`_

```
## Summary of the **`regs`** interface's registers

| Name                                            | Offset   |   Length | Description                                  |
|:------------------------------------------------|:---------|---------:|:---------------------------------------------|
| sram_ctrl.[`ALERT_TEST`](#alert_test)           | 0x0      |        4 | Alert Test Register
…
```

### ALERT TEST
_Source: `opentitan/hw/ip/sram_ctrl/doc/registers.md`_

```
| sram_ctrl.[`EXEC_REGWEN`](#exec_regwen)         | 0x8      |        4 | Lock register for execution enable register. |
| sram_ctrl.[`EXEC`](#exec)                       | 0xc      |        4 | Sram execution enable.                       |
| sram_ctrl.[`CTRL_REGWEN`](#ctrl_regwen)         | 0x10     |        4 | Lock register for control register.          |
| sram_ctrl.[`CTRL`](#ctrl)
…
```

## Spec Anchors

- `component:sram_ctrl` (L1) — `__graphify_spec_only__/components.md`
- `sram_ctrl.hjson` (L1) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `human name` (L6) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `one line desc` (L7) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `one paragraph desc` (L8) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `cip id` (L15) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `design spec` (L16) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `dv doc` (L17) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `hw checklist` (L18) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `sw checklist` (L19) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `version` (L20) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `life stage` (L21) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl.hjson`
- `sram_ctrl_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_sec_cm_testplan.hjson`
- `sram_ctrl_testplan.hjson` (L1) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_testplan.hjson`
- `testpoints` (L15) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_testplan.hjson`
- `desc` (L18) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_testplan.hjson`
- `covergroups` (L187) — `opentitan/hw/ip/sram_ctrl/data/sram_ctrl_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `SRAM CTRL Checklist` (L1) — `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `D2` (L32) — `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `D2S` (L74) — `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `D3` (L94) — `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `Verification Checklist` (L120) — `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `V1` (L122) — `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `V2` (L172) — `opentitan/hw/ip/sram_ctrl/doc/checklist.md`
- `V2S` (L218) — `opentitan/hw/ip/sram_ctrl/doc/checklist.md`

## Code Evidence

**RTL** (14)
  - `prim_ram_1p_scr`:L679 — `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv`
  - `tlul_adapter_sram_racl`:L529 — `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv`
  - `sram_ctrl_pkg`:L11 — `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv`
  - `sram_ctrl.sv`:L1 — `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv`
  - `sram_ctrl`:L10 — `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv`
  - `sram_ctrl_reg_pkg`:L32 — `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_regs_reg_top.sv`
  - `sram_ctrl_regs_reg_top`:L154 — `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv`
  - `sram_ctrl_pkg.sv`:L1 — `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_pkg.sv`
  - `sram_ctrl_ram_reg_top.sv`:L1 — `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_ram_reg_top.sv`
  - `sram_ctrl_ram_reg_top`:L9 — `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_ram_reg_top.sv`
  - `sram_ctrl_regs_reg_top.sv`:L1 — `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_regs_reg_top.sv`
  - `sram_ctrl_regs_reg_top`:L9 — `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_regs_reg_top.sv`
  - `sram_ctrl_reg_pkg.sv`:L1 — `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_reg_pkg.sv`
  - `sram_ctrl`:L1211 — `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
**DV** (8)
  - `tb.sv`:L1 — `opentitan\hw\ip\sram_ctrl\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\ip\sram_ctrl\dv\tb.sv`
  - `sram_ctrl_env_pkg`:L9 — `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv`
  - `sram_ctrl_test_pkg`:L11 — `opentitan\hw\ip\sram_ctrl\dv\tb.sv`
  - `sram_ctrl_cov_bind.sv`:L1 — `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv`
  - `sram_ctrl_cov_bind`:L6 — `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv`
  - `sram_ctrl_base_test.sv`:L1 — `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_base_test.sv`
  - `sram_ctrl_test_pkg.sv`:L1 — `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv`
**SVA** (2)
  - `sram_ctrl_bind.sv`:L1 — `opentitan\hw\ip\sram_ctrl\dv\sva\sram_ctrl_bind.sv`
  - `sram_ctrl_bind`:L5 — `opentitan\hw\ip\sram_ctrl\dv\sva\sram_ctrl_bind.sv`
**OTHER_CODE** (6)
  - `sram_ctrl_lc_escalation.rs`:L1 — `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs`
  - `Opts`:L28 — `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs`
  - `Addresses`:L46 — `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs`
  - `main()`:L52 — `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs`
  - `lc_escalation()`:L74 — `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs`
  - `write_read()`:L136 — `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs`

## Neighbor Components

- `rv_plic` (7 refs; instantiates×7)
- `lowrisc_ibex` (5 refs; instantiates×4, imports_from×1)
- `rv_core_ibex` (5 refs; instantiates×4, imports_from×1)
- `flash_ctrl` (3 refs; instantiates×3)
- `pwrmgr` (3 refs; instantiates×2, imports_from×1)
- `otbn` (2 refs; instantiates×2)
- `sensor_ctrl` (1 refs; instantiates×1)
- `rstmgr` (1 refs; imports_from×1)
- `spi_device` (1 refs; instantiates×1)
- `spi_passthru.rs` (1 refs; calls×1)
- `uart` (1 refs; calls×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_base_test.sv` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_env_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_test_pkg.sv` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_reg_pkg` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_regs_reg_top.sv` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_regs_reg_top` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_cov_bind.sv` | `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_cov_bind` | `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_ram_reg_top.sv` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_ram_reg_top.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_ram_reg_top` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_ram_reg_top.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_bind.sv` | `opentitan\hw\ip\sram_ctrl\dv\sva\sram_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_bind` | `opentitan\hw\ip\sram_ctrl\dv\sva\sram_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_reg_pkg.sv` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_pkg.sv` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_pkg` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl.sv` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_regs_reg_top` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_test_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `tb.sv` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `tb` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:sram_ctrl` | `sram_ctrl_lc_escalation.rs` | `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs` |
| `spec_component_matches_code` | `component:sram_ctrl` | `Opts` | `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs` |
| `spec_component_matches_code` | `component:sram_ctrl` | `Addresses` | `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs` |
| `spec_component_matches_code` | `component:sram_ctrl` | `main()` | `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs` |
| `spec_component_matches_code` | `component:sram_ctrl` | `lc_escalation()` | `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs` |
| `spec_component_matches_code` | `component:sram_ctrl` | `write_read()` | `opentitan\sw\host\tests\chip\sram_ctrl\src\sram_ctrl_lc_escalation.rs` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `tb.sv` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `tb` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `sram_ctrl_pkg` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `sram_ctrl_env_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `sram_ctrl_test_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl.hjson` | `sram_ctrl_cov_bind.sv` | `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `sram_ctrl_pkg` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `sram_ctrl_env_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `sram_ctrl_test_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_sec_cm_testplan.hjson` | `sram_ctrl_cov_bind.sv` | `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `tb` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `sram_ctrl_pkg` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `sram_ctrl_env_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `sram_ctrl_test_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `sram_ctrl_testplan.hjson` | `sram_ctrl_cov_bind.sv` | `opentitan\hw\ip\sram_ctrl\dv\cov\sram_ctrl_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_ram_1p_scr` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tlul_adapter_sram_racl` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\sram_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sram_ctrl_pkg` | `opentitan\hw\ip\sram_ctrl\rtl\sram_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sram_ctrl_env_pkg` | `opentitan\hw\ip\sram_ctrl\dv\tests\sram_ctrl_test_pkg.sv` |

## Retrieval Guidance

- For code-only queries mentioning `sram_ctrl`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `sram_ctrl`.
