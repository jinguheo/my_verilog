# Hardware Description: prim_present

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `prim_present`
- `approved_label`: `pending:prim_present`
- `doc_anchor`: `prim_present`
- `module_name_prefix`: `prim_present`
- `bridge_edge_count`: 26

## Inferred Hardware Role

`prim_present` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 27
- Code categories: dv: 21, rtl: 5
- Bridge relations: spec_component_matches_code: 26

## Spec Anchors

- `component:prim_present` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `prim_present_tb.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_present\tb\prim_present_tb.sv`
- `prim_present_tb` (L13) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_present\tb\prim_present_tb.sv`
- `prim_present` (L450) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_scrmbl.sv`
- `prim_present_tb.sv` (L1) - `opentitan\hw\ip\prim\dv\prim_present\tb\prim_present_tb.sv`
- `prim_present_tb` (L13) - `opentitan\hw\ip\prim\dv\prim_present\tb\prim_present_tb.sv`
- `prim_present.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_present.sv`
- `prim_present` (L25) - `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_present.sv`
- `prim_present.sv` (L1) - `opentitan\hw\ip\prim\rtl\prim_present.sv`
- `prim_present` (L25) - `opentitan\hw\ip\prim\rtl\prim_present.sv`
- `crypto_dpi_present_pkg.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present_pkg.sv`
- `crypto_dpi_present_pkg.sv` (L1) - `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present_pkg.sv`
- `crypto_dpi_present_pkg` (L16) - `opentitan\hw\ip\prim\dv\prim_present\tb\prim_present_tb.sv`
- `crypto_dpi_present.cc` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc`
- `mask64()` (L34) - `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc`
- `PresentState` (L41) - `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc`
- `enc_round()` (L78) - `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc`
- `dec_round()` (L99) - `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc`
- `next_round_key()` (L122) - `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc`
- `add_round_key()` (L183) - `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc`
- `sbox_layer()` (L190) - `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc`
- `perm_layer()` (L200) - `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc`
- `c_dpi_present_mk()` (L211) - `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc`
- `c_dpi_present_free()` (L230) - `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc`
- `c_dpi_present_enc_round()` (L232) - `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc`
- `c_dpi_present_dec_round()` (L245) - `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc`
- `crypto_dpi_present.cc` (L1) - `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:prim_present` | `prim_present_tb.sv` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_present\tb\prim_present_tb.sv` |
| `spec_component_matches_code` | `component:prim_present` | `prim_present_tb` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_present\tb\prim_present_tb.sv` |
| `spec_component_matches_code` | `component:prim_present` | `prim_present` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_scrmbl.sv` |
| `spec_component_matches_code` | `component:prim_present` | `prim_present_tb.sv` | `opentitan\hw\ip\prim\dv\prim_present\tb\prim_present_tb.sv` |
| `spec_component_matches_code` | `component:prim_present` | `prim_present_tb` | `opentitan\hw\ip\prim\dv\prim_present\tb\prim_present_tb.sv` |
| `spec_component_matches_code` | `component:prim_present` | `prim_present.sv` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_present.sv` |
| `spec_component_matches_code` | `component:prim_present` | `prim_present` | `ibex\vendor\lowrisc_ip\ip\prim\rtl\prim_present.sv` |
| `spec_component_matches_code` | `component:prim_present` | `prim_present.sv` | `opentitan\hw\ip\prim\rtl\prim_present.sv` |
| `spec_component_matches_code` | `component:prim_present` | `prim_present` | `opentitan\hw\ip\prim\rtl\prim_present.sv` |
| `spec_component_matches_code` | `component:prim_present` | `crypto_dpi_present_pkg.sv` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present_pkg.sv` |
| `spec_component_matches_code` | `component:prim_present` | `crypto_dpi_present_pkg.sv` | `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present_pkg.sv` |
| `spec_component_matches_code` | `component:prim_present` | `crypto_dpi_present_pkg` | `opentitan\hw\ip\prim\dv\prim_present\tb\prim_present_tb.sv` |
| `spec_component_matches_code` | `component:prim_present` | `crypto_dpi_present.cc` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc` |
| `spec_component_matches_code` | `component:prim_present` | `mask64()` | `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc` |
| `spec_component_matches_code` | `component:prim_present` | `PresentState` | `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc` |
| `spec_component_matches_code` | `component:prim_present` | `enc_round()` | `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc` |
| `spec_component_matches_code` | `component:prim_present` | `dec_round()` | `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc` |
| `spec_component_matches_code` | `component:prim_present` | `next_round_key()` | `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc` |
| `spec_component_matches_code` | `component:prim_present` | `add_round_key()` | `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc` |
| `spec_component_matches_code` | `component:prim_present` | `sbox_layer()` | `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc` |
| `spec_component_matches_code` | `component:prim_present` | `perm_layer()` | `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc` |
| `spec_component_matches_code` | `component:prim_present` | `c_dpi_present_mk()` | `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc` |
| `spec_component_matches_code` | `component:prim_present` | `c_dpi_present_free()` | `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc` |
| `spec_component_matches_code` | `component:prim_present` | `c_dpi_present_enc_round()` | `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc` |
| `spec_component_matches_code` | `component:prim_present` | `c_dpi_present_dec_round()` | `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc` |
| `spec_component_matches_code` | `component:prim_present` | `crypto_dpi_present.cc` | `opentitan\hw\ip\prim\dv\prim_present\crypto_dpi_present\crypto_dpi_present.cc` |

## Retrieval Guidance

- When a code-only query mentions `prim_present`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
