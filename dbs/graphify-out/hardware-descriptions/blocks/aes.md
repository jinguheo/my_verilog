# Hardware Description: aes

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`aes`** has the following hardware interfaces defined
- **Inter-Module Signals**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`aes`** has the following hardware interfaces defined

## Identity

- `ip_block`: `aes`
- `bridge_edge_count`: 112
- Spec categories: document: 89, component: 41, testplan: 28, theory: 19, interface: 14
- Code categories: rtl: 188, dv: 131, other_code: 73, sva: 7
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/ip/aes/doc/interfaces.md`_

```
# Hardware Interfaces
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/aes/data/aes.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`aes`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_edn_i`**
- Bus Device Interfaces (TL-UL)
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/aes/doc/interfaces.md`_

```
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`aes`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_edn_i`**
- Bus Device Interfaces (TL-UL): **`tl`**
- Bus Host Interfaces (TL-UL): *none*
- Peripheral Pins for Chip IO: *none*
- Interrupts:
…
```

### Security Alerts
_Source: `opentitan/hw/ip/aes/doc/interfaces.md`_

```
| Port Name      | Package::Struct        | Type    | Act   |   Width | Description   |
|:---------------|:-----------------------|:--------|:------|--------:|:--------------|
| idle           | prim_mubi_pkg::mubi4   | uni     | req   |       1 |               |
| lc_escalate_en | lc_ctrl_pkg::lc_tx     | uni     | rcv   |       1 |               |
| edn            | edn_pkg::edn           | req_
…
```

### Programmer's Guide
_Source: `opentitan/hw/ip/aes/doc/programmers_guide.md`_

```
# Programmer's Guide

This section discusses how software can interface with the AES unit.


## Clear upon Reset

Upon reset, the AES unit will first reseed the internal PRNGs for register clearing and masking via EDN, and then clear all key, IV and data registers with pseudo-random data.
```

### Clear upon Reset
_Source: `opentitan/hw/ip/aes/doc/programmers_guide.md`_

```
# Programmer's Guide

This section discusses how software can interface with the AES unit.


## Clear upon Reset

Upon reset, the AES unit will first reseed the internal PRNGs for register clearing and masking via EDN, and then clear all key, IV and data registers with pseudo-random data.
Only after this sequence has finished, the unit becomes idle (indicated in [`STATUS.IDLE`](registers.md#status
…
```

### Initialization
_Source: `opentitan/hw/ip/aes/doc/programmers_guide.md`_

```
## Clear upon Reset

Upon reset, the AES unit will first reseed the internal PRNGs for register clearing and masking via EDN, and then clear all key, IV and data registers with pseudo-random data.
Only after this sequence has finished, the unit becomes idle (indicated in [`STATUS.IDLE`](registers.md#status)).
The AES unit is then ready for software initialization.
Note that at this point, the key,
…
```

### Summary
_Source: `opentitan/hw/ip/aes/doc/registers.md`_

```
- Usability: critical corner cases where software updates input data or the key partially only are easier to avoid using separate registers and the `hwqe`-signals provided by the Register Tool.
- Easier interaction with DMA engines

Also, using a FIFO interface for something that is not actually FIFO (internally, 16B of input/output data are consumed/produced at once) is less natural.

For a detai
…
```

### ALERT TEST
_Source: `opentitan/hw/ip/aes/doc/registers.md`_

```
| aes.[`DATA_OUT_3`](#data_out)                 | 0x70     |        4 | Output Data Register.                       |
| aes.[`CTRL_SHADOWED`](#ctrl_shadowed)         | 0x74     |        4 | Control Register.                           |
| aes.[`CTRL_AUX_SHADOWED`](#ctrl_aux_shadowed) | 0x78     |        4 | Auxiliary Control Register.                 |
| aes.[`CTRL_AUX_REGWEN`](#ctrl_aux_regwen)
…
```

## Spec Anchors

- `component:aes` (L1) — `__graphify_spec_only__/components.md`
- `aes.hjson` (L1) — `opentitan/hw/ip/aes/data/aes.hjson`
- `human name` (L8) — `opentitan/hw/ip/aes/data/aes.hjson`
- `one line desc` (L9) — `opentitan/hw/ip/aes/data/aes.hjson`
- `one paragraph desc` (L10) — `opentitan/hw/ip/aes/data/aes.hjson`
- `cip id` (L20) — `opentitan/hw/ip/aes/data/aes.hjson`
- `design spec` (L21) — `opentitan/hw/ip/aes/data/aes.hjson`
- `dv doc` (L22) — `opentitan/hw/ip/aes/data/aes.hjson`
- `hw checklist` (L23) — `opentitan/hw/ip/aes/data/aes.hjson`
- `sw checklist` (L24) — `opentitan/hw/ip/aes/data/aes.hjson`
- `version` (L25) — `opentitan/hw/ip/aes/data/aes.hjson`
- `life stage` (L26) — `opentitan/hw/ip/aes/data/aes.hjson`
- `aes_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/aes/data/aes_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/aes/data/aes_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/aes/data/aes_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/aes/data/aes_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/aes/data/aes_sec_cm_testplan.hjson`
- `aes_testplan.hjson` (L1) — `opentitan/hw/ip/aes/data/aes_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/aes/data/aes_testplan.hjson`
- `testpoints` (L12) — `opentitan/hw/ip/aes/data/aes_testplan.hjson`
- `desc` (L22) — `opentitan/hw/ip/aes/data/aes_testplan.hjson`
- `stage` (L24) — `opentitan/hw/ip/aes/data/aes_testplan.hjson`
- `tests` (L25) — `opentitan/hw/ip/aes/data/aes_testplan.hjson`
- `covergroups` (L174) — `opentitan/hw/ip/aes/data/aes_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/aes/doc/checklist.md`
- `AES Checklist` (L1) — `opentitan/hw/ip/aes/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/aes/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/aes/doc/checklist.md`
- `D2` (L32) — `opentitan/hw/ip/aes/doc/checklist.md`
- `D2S` (L74) — `opentitan/hw/ip/aes/doc/checklist.md`
- `D3` (L94) — `opentitan/hw/ip/aes/doc/checklist.md`
- `Verification Checklist` (L120) — `opentitan/hw/ip/aes/doc/checklist.md`
- `V1` (L122) — `opentitan/hw/ip/aes/doc/checklist.md`
- `V2` (L172) — `opentitan/hw/ip/aes/doc/checklist.md`
- `V2S` (L218) — `opentitan/hw/ip/aes/doc/checklist.md`

## Code Evidence

**RTL** (2)
  - `aes_pkg`:L8 — `opentitan\hw\ip\aes\rtl\aes_wrap.sv`
  - `aes_reg_pkg`:L35 — `opentitan\hw\ip\aes\rtl\aes_wrap.sv`
**DV** (42)
  - `aes_model_dpi.c`:L1 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
  - `c_dpi_aes_crypt_block()`:L16 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
  - `c_dpi_aes_crypt_message()`:L123 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
  - `c_dpi_aes_sub_bytes()`:L259 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
  - `c_dpi_aes_shift_rows()`:L277 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
  - `c_dpi_aes_mix_columns()`:L295 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
  - `c_dpi_aes_key_expand()`:L313 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
  - `aes_data_get()`:L352 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
  - `aes_data_put()`:L371 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
  - `aes_data_unpacked_get()`:L389 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
  - `aes_data_unpacked_put()`:L408 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
  - `aes_key_get()`:L428 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
  - `aes_key_put()`:L448 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
  - `aes_model_dpi.h`:L1 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.h`
  - `aes_model_dpi_pkg.sv`:L1 — `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi_pkg.sv`
  - `aes_cov_bind.sv`:L1 — `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv`
  - `aes_cov_bind`:L6 — `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv`
  - `aes_cov_if.sv`:L1 — `opentitan\hw\ip\aes\dv\cov\aes_cov_if.sv`
  - `aes_err_injection_bind.sv`:L1 — `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv`
  - `aes_err_injection_bind`:L4 — `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv`
**SVA** (6)
  - `aes_bind.sv`:L1 — `opentitan\hw\ip\aes\dv\sva\aes_bind.sv`
  - `aes_bind`:L5 — `opentitan\hw\ip\aes\dv\sva\aes_bind.sv`
  - `aes_idle_check.sv`:L1 — `opentitan\hw\ip\aes\dv\sva\aes_idle_check.sv`
  - `aes_idle_check`:L7 — `opentitan\hw\ip\aes\dv\sva\aes_idle_check.sv`
  - `aes_masking_reseed_if.sv`:L1 — `opentitan\hw\ip\aes\dv\sva\aes_masking_reseed_if.sv`
  - `aes_reseed_if.sv`:L1 — `opentitan\hw\ip\aes\dv\sva\aes_reseed_if.sv`

## Neighbor Components

- `riscv-tests` (42 refs; calls×42)
- `aes.c` (25 refs; calls×18, contains×7)
- `lowrisc_ibex` (22 refs; instantiates×19, imports_from×2, calls×1)
- `verilator_sim_ctrl.cc` (12 refs; calls×12)
- `rv_plic` (6 refs; instantiates×6)
- `ac_range_check` (5 refs; instantiates×5)
- `flash_ctrl` (4 refs; instantiates×4)
- `otbn` (4 refs; calls×3, instantiates×1)
- `rv_core_ibex` (3 refs; instantiates×3)
- `prim` (3 refs; instantiates×3)
- `kmac` (3 refs; calls×3)
- `aes_gcm` (2 refs; calls×2)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:aes` | `aes_cipher_core_tb.sv` | `opentitan\hw\ip\aes\pre_dv\aes_cipher_core_tb\rtl\aes_cipher_core_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_cipher_core_tb` | `opentitan\hw\ip\aes\pre_dv\aes_cipher_core_tb\rtl\aes_cipher_core_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_masked_wrapper.sv` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_lec\aes_sbox_masked_wrapper.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_masked_wrapper` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_lec\aes_sbox_masked_wrapper.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_masked` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_lec\aes_sbox_masked_wrapper.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_err_injection_bind.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_err_injection_bind` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_canright_masked_noreuse.sv` | `opentitan\hw\ip\aes\rtl\aes_sbox_canright_masked_noreuse.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_masked_inverse_gf2p4_noreuse` | `opentitan\hw\ip\aes\rtl\aes_sbox_canright_masked_noreuse.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_masked_inverse_gf2p8_noreuse` | `opentitan\hw\ip\aes\rtl\aes_sbox_canright_masked_noreuse.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_masked_inverse_gf2p4_noreuse` | `opentitan\hw\ip\aes\rtl\aes_sbox_canright_masked_noreuse.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_canright_masked_noreuse` | `opentitan\hw\ip\aes\rtl\aes_sbox_canright_masked_noreuse.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_masked_inverse_gf2p8_noreuse` | `opentitan\hw\ip\aes\rtl\aes_sbox_canright_masked_noreuse.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_manual_config_err_test.sv` | `opentitan\hw\ip\aes\dv\tests\aes_manual_config_err_test.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_model_dpi_pkg.sv` | `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi_pkg.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_gcm_save_restore_test.sv` | `opentitan\hw\ip\aes\dv\tests\aes_gcm_save_restore_test.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_tb.sv` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_tb\rtl\aes_sbox_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_tb` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_tb\rtl\aes_sbox_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_lut` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_tb\rtl\aes_sbox_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_canright` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_tb\rtl\aes_sbox_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_canright_masked_noreuse` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_tb\rtl\aes_sbox_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_canright_masked` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_tb\rtl\aes_sbox_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_dom` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_tb\rtl\aes_sbox_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_wrap_tb.sv` | `opentitan\hw\ip\aes\pre_dv\aes_wrap_tb\rtl\aes_wrap_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_wrap_tb` | `opentitan\hw\ip\aes\pre_dv\aes_wrap_tb\rtl\aes_wrap_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_wrap` | `opentitan\hw\ip\aes\pre_dv\aes_wrap_tb\rtl\aes_wrap_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_config_error_test.sv` | `opentitan\hw\ip\aes\dv\tests\aes_config_error_test.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_tb_c_dpi.sv` | `opentitan\hw\ip\aes\pre_dv\aes_tb\rtl\aes_tb_c_dpi.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_tb_c_dpi` | `opentitan\hw\ip\aes\pre_dv\aes_tb\rtl\aes_tb_c_dpi.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_model_dpi_pkg` | `opentitan\hw\ip\aes\pre_dv\aes_tb\rtl\aes_tb_c_dpi.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_alert_reset_test.sv` | `opentitan\hw\ip\aes\dv\tests\aes_alert_reset_test.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_tb_pkg` | `opentitan\hw\ip\aes\pre_dv\aes_tb\rtl\aes_tb_reqs.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_tb_reqs.sv` | `opentitan\hw\ip\aes\pre_dv\aes_tb\rtl\aes_tb_reqs.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_tb_reqs` | `opentitan\hw\ip\aes\pre_dv\aes_tb\rtl\aes_tb_reqs.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_ctrl_gcm_reg_shadowed.sv` | `opentitan\hw\ip\aes\rtl\aes_ctrl_gcm_reg_shadowed.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_ctrl_gcm_reg_shadowed` | `opentitan\hw\ip\aes\rtl\aes_ctrl_gcm_reg_shadowed.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_masking_reseed_if.sv` | `opentitan\hw\ip\aes\dv\sva\aes_masking_reseed_if.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_tb_pkg.sv` | `opentitan\hw\ip\aes\pre_dv\aes_tb\rtl\aes_tb_pkg.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_cipher_control_fsm_n.sv` | `opentitan\hw\ip\aes\rtl\aes_cipher_control_fsm_n.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `aes_model_dpi_pkg.sv` | `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `aes_pkg` | `opentitan\hw\ip\aes\rtl\aes_wrap.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `aes_cov_bind.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `aes_cov_bind` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `aes_cov_if.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_if.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `aes_err_injection_bind.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `aes_err_injection_bind` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `fi_cipher_fsm_wrapper.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\fi_cipher_fsm_wrapper.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `aes_model_dpi_pkg.sv` | `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `aes_pkg` | `opentitan\hw\ip\aes\rtl\aes_wrap.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `aes_cov_bind.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `aes_cov_bind` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `aes_cov_if.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_if.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `aes_err_injection_bind.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `aes_err_injection_bind` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `fi_cipher_fsm_wrapper.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\fi_cipher_fsm_wrapper.sv` |
| `spec_path_matches_code_path` | `aes_testplan.hjson` | `aes_model_dpi_pkg.sv` | `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `aes_testplan.hjson` | `aes_pkg` | `opentitan\hw\ip\aes\rtl\aes_wrap.sv` |
| `spec_path_matches_code_path` | `aes_testplan.hjson` | `aes_cov_bind.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `aes_testplan.hjson` | `aes_cov_bind` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |

## Retrieval Guidance

- For code-only queries mentioning `aes`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `aes`.
