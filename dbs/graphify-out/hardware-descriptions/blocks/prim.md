# Hardware Description: prim

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Primitive Component: Flash Wrapper**: `prim_flash` is a wrapper interface for technology specific flash modules.
- **Overview**: `prim_flash` is a wrapper interface for technology specific flash modules.
- **Parameters**: `prim_flash` is a wrapper interface for technology specific flash modules.

## Identity

- `ip_block`: `prim`
- `bridge_edge_count`: 365
- Spec categories: document: 366, testplan: 72, component: 41, interface: 20, theory: 16
- Code categories: rtl: 808, dv: 628, other_code: 112, sva: 108
- Bridge relations: spec_path_matches_code_path: 325, spec_component_matches_code: 40

## Spec Excerpts

### Primitive Component: Flash Wrapper
_Source: `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`_

```
# Primitive Component: Flash Wrapper

# Overview
`prim_flash` is a wrapper interface for technology specific flash modules.

As the exact details of each technology can be different, this document mainly describes the interface requirements and their functions.
The wrapper however does assume that all page sizes are the same (they cannot be different between data and info partitions, or different
…
```

### Overview
_Source: `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`_

```
# Primitive Component: Flash Wrapper

# Overview
`prim_flash` is a wrapper interface for technology specific flash modules.

As the exact details of each technology can be different, this document mainly describes the interface requirements and their functions.
The wrapper however does assume that all page sizes are the same (they cannot be different between data and info partitions, or different
…
```

### Parameters
_Source: `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`_

```
# Primitive Component: Flash Wrapper

# Overview
`prim_flash` is a wrapper interface for technology specific flash modules.

As the exact details of each technology can be different, this document mainly describes the interface requirements and their functions.
The wrapper however does assume that all page sizes are the same (they cannot be different between data and info partitions, or different
…
```

### Primitive Component: Keccak permutation
_Source: `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`_

```
# Primitive Component: Keccak permutation

# Overview

`prim_keccak` is a single round implementation of the Keccak_p permutation stage in [SHA3 algorithm][fibs-pub-202].
Keccak primitive module assumes the number of rounds is less than or equal to 12 + 2L.
It supports all combinations of the data width described in the [spec][fibs-pub-202].
Note that this implementation does not include any count
…
```

### Overview
_Source: `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`_

```
# Primitive Component: Keccak permutation

# Overview

`prim_keccak` is a single round implementation of the Keccak_p permutation stage in [SHA3 algorithm][fibs-pub-202].
Keccak primitive module assumes the number of rounds is less than or equal to 12 + 2L.
It supports all combinations of the data width described in the [spec][fibs-pub-202].
Note that this implementation does not include any count
…
```

### Parameters
_Source: `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`_

```
`prim_keccak` is a single round implementation of the Keccak_p permutation stage in [SHA3 algorithm][fibs-pub-202].
Keccak primitive module assumes the number of rounds is less than or equal to 12 + 2L.
It supports all combinations of the data width described in the [spec][fibs-pub-202].
Note that this implementation does not include any countermeasures for security hardening against implementatio
…
```

### Primitive Component: LFSR
_Source: `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_lfsr.md`_

```
# Primitive Component: LFSR

# Overview

`prim_lfsr` is a parameterized linear feedback shift register (LFSR)
implementation that supports Galois (XOR form) and Fibonacci (XNOR form)
polynomials. The main difference between Galois and Fibonacci is that the
former has a shorter critical timing path since the XOR Gates are interleaved
```

### Overview
_Source: `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_lfsr.md`_

```
# Primitive Component: LFSR

# Overview

`prim_lfsr` is a parameterized linear feedback shift register (LFSR)
implementation that supports Galois (XOR form) and Fibonacci (XNOR form)
polynomials. The main difference between Galois and Fibonacci is that the
former has a shorter critical timing path since the XOR Gates are interleaved
with the shift register, whereas the latter combines several shif
…
```

## Spec Anchors

- `component:prim` (L1) — `__graphify_spec_only__/components.md`
- `prim_flash.md` (L1) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Primitive Component: Flash Wrapper` (L1) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Overview` (L3) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Parameters` (L9) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Signal Interfaces` (L24) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Overall Interface Signals` (L26) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Flash Request/Response Signals` (L54) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Theory of Operations` (L76) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Transactions` (L78) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Read` (L92) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Program` (L104) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `prim_keccak.md` (L1) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`
- `Primitive Component: Keccak permutation` (L1) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`
- `Overview` (L3) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`
- `Parameters` (L13) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`
- `Derived Parameters` (L19) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`
- `Signal Interfaces` (L30) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`
- `Theory of Operations` (L44) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`
- `prim_lfsr.md` (L1) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_lfsr.md`
- `Primitive Component: LFSR` (L1) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_lfsr.md`
- `Overview` (L3) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_lfsr.md`
- `Parameters` (L16) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_lfsr.md`
- `Signal Interfaces` (L28) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_lfsr.md`
- `Theory of Operations` (L38) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_lfsr.md`
- `prim_packer.md` (L1) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer.md`
- `Primitive Component: Packer` (L1) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer.md`
- `Overview` (L3) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer.md`
- `Parameters` (L10) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer.md`
- `Signal Interfaces` (L18) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer.md`
- `Theory of Operations` (L34) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer.md`
- `prim_packer_fifo.md` (L1) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer_fifo.md`
- `Primitive Component: Packer FIFO` (L1) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer_fifo.md`
- `Overview` (L3) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer_fifo.md`
- `Parameters` (L17) — `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer_fifo.md`

## Code Evidence

**RTL** (2)
  - `prim_ram_2p`:L109 — `opentitan\hw\ip\prim\rtl\prim_ram_2p_async_adv.sv`
  - `prim_alert_receiver`:L35 — `opentitan\hw\ip\prim\rtl\prim_alert_to_diff.sv`
**DV** (48)
  - `prim_alert_tb.sv`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_alert\tb\prim_alert_tb.sv`
  - `prim_alert_tb`:L17 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_alert\tb\prim_alert_tb.sv`
  - `ascon_model_dpi.c`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.c`
  - `c_dpi_aead_encrypt()`:L17 — `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.c`
  - `c_dpi_aead_decrypt()`:L75 — `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.c`
  - `c_dpi_ascon_round()`:L132 — `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.c`
  - `ascon_data_get()`:L147 — `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.c`
  - `ascon_data_put()`:L171 — `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.c`
  - `ascon_model_dpi.h`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.h`
  - `ascon_model_dpi_pkg.sv`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi_pkg.sv`
  - `aead.c`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\aead.c`
  - `crypto_aead_encrypt()`:L8 — `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\aead.c`
  - `crypto_aead_decrypt()`:L106 — `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\aead.c`
  - `api.h`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\api.h`
  - `ascon.h`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\ascon.h`
  - `constants.h`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\constants.h`
  - `crypto_aead.h`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\crypto_aead.h`
  - `permutations.h`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\permutations.h`
  - `P12()`:L11 — `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\permutations.h`
  - `P8()`:L26 — `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\permutations.h`

## Neighbor Components

- `rv_core_ibex` (104 refs; imports_from×72, instantiates×32)
- `lowrisc_ibex` (54 refs; instantiates×34, calls×14, imports_from×6)
- `riscv-tests` (42 refs; calls×42)
- `alert_handler` (20 refs; imports_from×20)
- `pulp_riscv_dbg` (20 refs; instantiates×20)
- `ascon` (19 refs; imports×18, instantiates×1)
- `verilator_sim_ctrl.cc` (15 refs; calls×15)
- `flash_ctrl` (14 refs; instantiates×14)
- `pwrmgr` (14 refs; imports_from×8, instantiates×6)
- `sensor_ctrl` (12 refs; instantiates×12)
- `spi_device` (12 refs; imports_from×8, instantiates×4)
- `rstmgr` (10 refs; instantiates×10)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:prim` | `prim_ascon_duplex_tb_pkg.sv` | `ibex\vendor\lowrisc_ip\ip\prim\pre_dv\prim_ascon\prim_ascon_duplex_tb\rtl\prim_ascon_duplex_tb_pkg.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_ascon_duplex_tb.sv` | `ibex\vendor\lowrisc_ip\ip\prim\pre_dv\prim_ascon\prim_ascon_duplex_tb\rtl\prim_ascon_duplex_tb.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_ascon_duplex_tb` | `ibex\vendor\lowrisc_ip\ip\prim\pre_dv\prim_ascon\prim_ascon_duplex_tb\rtl\prim_ascon_duplex_tb.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_ascon_round_tb.sv` | `ibex\vendor\lowrisc_ip\ip\prim\pre_dv\prim_ascon\prim_ascon_round_tb\rtl\prim_ascon_round_tb.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_ascon_round_tb` | `ibex\vendor\lowrisc_ip\ip\prim\pre_dv\prim_ascon\prim_ascon_round_tb\rtl\prim_ascon_round_tb.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_ascon_duplex_tb_pkg.sv` | `opentitan\hw\ip\prim\pre_dv\prim_ascon\prim_ascon_duplex_tb\rtl\prim_ascon_duplex_tb_pkg.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_ascon_duplex_tb_pkg` | `opentitan\hw\ip\prim\pre_dv\prim_ascon\prim_ascon_duplex_tb\rtl\prim_ascon_duplex_tb.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_ascon_duplex` | `opentitan\hw\ip\prim\pre_dv\prim_ascon\prim_ascon_duplex_tb\rtl\prim_ascon_duplex_tb.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_ascon_duplex_tb.sv` | `opentitan\hw\ip\prim\pre_dv\prim_ascon\prim_ascon_duplex_tb\rtl\prim_ascon_duplex_tb.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_ascon_duplex_tb` | `opentitan\hw\ip\prim\pre_dv\prim_ascon\prim_ascon_duplex_tb\rtl\prim_ascon_duplex_tb.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_ascon_round_tb.sv` | `opentitan\hw\ip\prim\pre_dv\prim_ascon\prim_ascon_round_tb\rtl\prim_ascon_round_tb.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_ascon_round_tb` | `opentitan\hw\ip\prim\pre_dv\prim_ascon\prim_ascon_round_tb\rtl\prim_ascon_round_tb.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_22_16_assert_fpv.sv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_inv_hamming_22_16_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_22_16_assert_fpv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_inv_hamming_22_16_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_39_32_assert_fpv.sv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_inv_hamming_39_32_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_39_32_assert_fpv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_inv_hamming_39_32_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_72_64_assert_fpv.sv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_inv_hamming_72_64_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_72_64_assert_fpv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_inv_hamming_72_64_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_76_68_assert_fpv.sv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_inv_hamming_76_68_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_76_68_assert_fpv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_inv_hamming_76_68_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_sync_reqack_tb.sv` | `ibex\vendor\lowrisc_ip\ip\prim\pre_dv\prim_sync_reqack\rtl\prim_sync_reqack_tb.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_sync_reqack_tb` | `ibex\vendor\lowrisc_ip\ip\prim\pre_dv\prim_sync_reqack\rtl\prim_sync_reqack_tb.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_22_16_bind_fpv.sv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_hamming_22_16_bind_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_22_16_bind_fpv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_hamming_22_16_bind_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_39_32_bind_fpv.sv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_hamming_39_32_bind_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_39_32_bind_fpv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_hamming_39_32_bind_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_72_64_bind_fpv.sv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_hamming_72_64_bind_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_72_64_bind_fpv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_hamming_72_64_bind_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_76_68_bind_fpv.sv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_hamming_76_68_bind_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_inv_hamming_76_68_bind_fpv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_secded_inv_hamming_76_68_bind_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_hamming_22_16_assert_fpv.sv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_hamming_22_16_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_hamming_22_16_assert_fpv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_hamming_22_16_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_hamming_39_32_assert_fpv.sv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_hamming_39_32_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_hamming_39_32_assert_fpv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_hamming_39_32_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_hamming_72_64_assert_fpv.sv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_hamming_72_64_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_hamming_72_64_assert_fpv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_hamming_72_64_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_hamming_76_68_assert_fpv.sv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_hamming_76_68_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_secded_hamming_76_68_assert_fpv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\vip\prim_secded_hamming_76_68_assert_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_alert_rxtx_async_fatal_bind_fpv.sv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_alert_rxtx_async_fatal_bind_fpv.sv` |
| `spec_component_matches_code` | `component:prim` | `prim_alert_rxtx_async_fatal_bind_fpv` | `ibex\vendor\lowrisc_ip\ip\prim\fpv\tb\prim_alert_rxtx_async_fatal_bind_fpv.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `clk_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_if.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `clk_rst_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_rst_if.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `common_ifs_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\common_ifs_pkg.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `entropy_subsys_fifo_exception_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_if.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `entropy_subsys_fifo_exception_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_pkg.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `pins_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\pins_if.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `rst_shadowed_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\rst_shadowed_if.sv` |
| `spec_path_matches_code_path` | `prim_flash.md` | `csr_seq_lib.sv` | `ibex\vendor\lowrisc_ip\dv\sv\csr_utils\csr_seq_lib.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `prim_keccak.sv` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_keccak.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `prim_keccak` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_keccak.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `prim_keccak.sv` | `opentitan\hw\ip\prim\rtl\prim_keccak.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `prim_keccak` | `opentitan\hw\ip\prim\rtl\prim_keccak.sv` |

## Retrieval Guidance

- For code-only queries mentioning `prim`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `prim`.
