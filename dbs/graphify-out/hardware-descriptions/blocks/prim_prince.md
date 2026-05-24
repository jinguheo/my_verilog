# Hardware Description: prim_prince

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `prim_prince`
- `bridge_edge_count`: 36
- Spec categories: component: 37
- Code categories: dv: 31, rtl: 5
- Bridge relations: spec_component_matches_code: 36

## Spec Anchors

- `component:prim_prince` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**RTL** (5)
  - `prim_prince`:L108 — `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv`
  - `prim_prince.sv`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_prince.sv`
  - `prim_prince`:L26 — `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_prince.sv`
  - `prim_prince.sv`:L1 — `opentitan\hw\ip\prim\rtl\prim_prince.sv`
  - `prim_prince`:L26 — `opentitan\hw\ip\prim\rtl\prim_prince.sv`
**DV** (31)
  - `prim_prince_tb.sv`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\tb\prim_prince_tb.sv`
  - `prim_prince_tb`:L13 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\tb\prim_prince_tb.sv`
  - `prim_prince_tb.sv`:L1 — `opentitan\hw\ip\prim\dv\prim_prince\tb\prim_prince_tb.sv`
  - `prim_prince_tb`:L13 — `opentitan\hw\ip\prim\dv\prim_prince\tb\prim_prince_tb.sv`
  - `crypto_dpi_prince_pkg.sv`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince_pkg.sv`
  - `crypto_dpi_prince_pkg.sv`:L1 — `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince_pkg.sv`
  - `crypto_dpi_prince.c`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince.c`
  - `prince_ref.h`:L1 — `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
  - `c_dpi_prince_encrypt()`:L16 — `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince.c`
  - `c_dpi_prince_decrypt()`:L23 — `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince.c`
  - `crypto_dpi_prince.c`:L1 — `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince.c`
  - `bytes_to_uint64()`:L52 — `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
  - `uint64_to_bytes()`:L65 — `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
  - `prince_k0_to_k0_prime()`:L74 — `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
  - `prince_round_constant()`:L80 — `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
  - `prince_sbox()`:L93 — `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
  - `prince_sbox_inv()`:L104 — `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
  - `prince_s_layer()`:L113 — `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
  - `prince_s_inv_layer()`:L127 — `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
  - `gf2_mat_mult16_1()`:L138 — `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:prim_prince` | `prim_prince_tb.sv` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\tb\prim_prince_tb.sv` |
| `spec_component_matches_code` | `component:prim_prince` | `prim_prince_tb` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\tb\prim_prince_tb.sv` |
| `spec_component_matches_code` | `component:prim_prince` | `prim_prince_tb.sv` | `opentitan\hw\ip\prim\dv\prim_prince\tb\prim_prince_tb.sv` |
| `spec_component_matches_code` | `component:prim_prince` | `prim_prince_tb` | `opentitan\hw\ip\prim\dv\prim_prince\tb\prim_prince_tb.sv` |
| `spec_component_matches_code` | `component:prim_prince` | `prim_prince` | `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv` |
| `spec_component_matches_code` | `component:prim_prince` | `prim_prince.sv` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_prince.sv` |
| `spec_component_matches_code` | `component:prim_prince` | `prim_prince` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_prince.sv` |
| `spec_component_matches_code` | `component:prim_prince` | `prim_prince.sv` | `opentitan\hw\ip\prim\rtl\prim_prince.sv` |
| `spec_component_matches_code` | `component:prim_prince` | `prim_prince` | `opentitan\hw\ip\prim\rtl\prim_prince.sv` |
| `spec_component_matches_code` | `component:prim_prince` | `crypto_dpi_prince_pkg.sv` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince_pkg.sv` |
| `spec_component_matches_code` | `component:prim_prince` | `crypto_dpi_prince_pkg.sv` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince_pkg.sv` |
| `spec_component_matches_code` | `component:prim_prince` | `crypto_dpi_prince.c` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince.c` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_ref.h` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `c_dpi_prince_encrypt()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince.c` |
| `spec_component_matches_code` | `component:prim_prince` | `c_dpi_prince_decrypt()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince.c` |
| `spec_component_matches_code` | `component:prim_prince` | `crypto_dpi_prince.c` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince.c` |
| `spec_component_matches_code` | `component:prim_prince` | `bytes_to_uint64()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `uint64_to_bytes()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_k0_to_k0_prime()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_round_constant()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_sbox()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_sbox_inv()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_s_layer()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_s_inv_layer()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `gf2_mat_mult16_1()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_m16_matrices()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_m_prime_layer()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_shift_rows()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_m_layer()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_m_inv_layer()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_core()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_enc_dec_uint64()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_enc_dec()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_encrypt()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_decrypt()` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |
| `spec_component_matches_code` | `component:prim_prince` | `prince_ref.h` | `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h` |

## Retrieval Guidance

- For code-only queries mentioning `prim_prince`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `prim_prince`.
