# Hardware Description: prim_prince

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `prim_prince`
- `approved_label`: `pending:prim_prince`
- `doc_anchor`: `prim_prince`
- `module_name_prefix`: `prim_prince`
- `bridge_edge_count`: 36

## Inferred Hardware Role

`prim_prince` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 37
- Code categories: dv: 31, rtl: 5
- Bridge relations: spec_component_matches_code: 36

## Spec Anchors

- `component:prim_prince` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `prim_prince_tb.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\tb\prim_prince_tb.sv`
- `prim_prince_tb` (L13) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\tb\prim_prince_tb.sv`
- `prim_prince_tb.sv` (L1) - `opentitan\hw\ip\prim\dv\prim_prince\tb\prim_prince_tb.sv`
- `prim_prince_tb` (L13) - `opentitan\hw\ip\prim\dv\prim_prince\tb\prim_prince_tb.sv`
- `prim_prince` (L108) - `opentitan\hw\ip\rom_ctrl\rtl\rom_ctrl_scrambled_rom.sv`
- `prim_prince.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_prince.sv`
- `prim_prince` (L26) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_prince.sv`
- `prim_prince.sv` (L1) - `opentitan\hw\ip\prim\rtl\prim_prince.sv`
- `prim_prince` (L26) - `opentitan\hw\ip\prim\rtl\prim_prince.sv`
- `crypto_dpi_prince_pkg.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince_pkg.sv`
- `crypto_dpi_prince_pkg.sv` (L1) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince_pkg.sv`
- `crypto_dpi_prince.c` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince.c`
- `prince_ref.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `c_dpi_prince_encrypt()` (L16) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince.c`
- `c_dpi_prince_decrypt()` (L23) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince.c`
- `crypto_dpi_prince.c` (L1) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\crypto_dpi_prince.c`
- `bytes_to_uint64()` (L52) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `uint64_to_bytes()` (L65) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_k0_to_k0_prime()` (L74) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_round_constant()` (L80) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_sbox()` (L93) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_sbox_inv()` (L104) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_s_layer()` (L113) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_s_inv_layer()` (L127) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `gf2_mat_mult16_1()` (L138) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_m16_matrices()` (L150) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_m_prime_layer()` (L175) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_shift_rows()` (L198) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_m_layer()` (L212) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_m_inv_layer()` (L221) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_core()` (L230) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_enc_dec_uint64()` (L275) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_enc_dec()` (L302) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_encrypt()` (L320) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_decrypt()` (L334) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`
- `prince_ref.h` (L1) - `opentitan\hw\ip\prim\dv\prim_prince\crypto_dpi_prince\prince_ref.h`

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

- When a code-only query mentions `prim_prince`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
