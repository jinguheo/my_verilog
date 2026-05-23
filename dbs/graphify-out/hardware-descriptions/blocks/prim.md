# Hardware Description: prim

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `prim`
- `approved_label`: `pending:prim`
- `doc_anchor`: `prim`
- `module_name_prefix`: `prim`
- `bridge_edge_count`: 365

## Inferred Hardware Role

`prim` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 366, testplan: 72, component: 41, interface: 20, theory: 16
- Code categories: rtl: 808, dv: 628, other_code: 112, sva: 108
- Bridge relations: spec_path_matches_code_path: 325, spec_component_matches_code: 40

## Spec Anchors

- `component:prim` (L1) - `__graphify_spec_only__/components.md`
- `prim_flash.md` (L1) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Primitive Component: Flash Wrapper` (L1) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Overview` (L3) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Parameters` (L9) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Signal Interfaces` (L24) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Overall Interface Signals` (L26) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Flash Request/Response Signals` (L54) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Theory of Operations` (L76) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Transactions` (L78) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Read` (L92) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `Program` (L104) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md`
- `prim_keccak.md` (L1) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`
- `Primitive Component: Keccak permutation` (L1) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`
- `Overview` (L3) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`
- `Parameters` (L13) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`
- `Derived Parameters` (L19) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`
- `Signal Interfaces` (L30) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`
- `Theory of Operations` (L44) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md`
- `prim_lfsr.md` (L1) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_lfsr.md`
- `Primitive Component: LFSR` (L1) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_lfsr.md`
- `Overview` (L3) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_lfsr.md`
- `Parameters` (L16) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_lfsr.md`
- `Signal Interfaces` (L28) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_lfsr.md`
- `Theory of Operations` (L38) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_lfsr.md`
- `prim_packer.md` (L1) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer.md`
- `Primitive Component: Packer` (L1) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer.md`
- `Overview` (L3) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer.md`
- `Parameters` (L10) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer.md`
- `Signal Interfaces` (L18) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer.md`
- `Theory of Operations` (L34) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer.md`
- `prim_packer_fifo.md` (L1) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer_fifo.md`
- `Primitive Component: Packer FIFO` (L1) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer_fifo.md`
- `Overview` (L3) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer_fifo.md`
- `Parameters` (L17) - `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer_fifo.md`

## Code Evidence

- `prim_ram_2p` (L109) - `opentitan\hw\ip\prim\rtl\prim_ram_2p_async_adv.sv`
- `prim_alert_tb.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_alert\tb\prim_alert_tb.sv`
- `prim_alert_tb` (L17) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_alert\tb\prim_alert_tb.sv`
- `prim_alert_receiver` (L35) - `opentitan\hw\ip\prim\rtl\prim_alert_to_diff.sv`
- `ascon_model_dpi.c` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.c`
- `c_dpi_aead_encrypt()` (L17) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.c`
- `c_dpi_aead_decrypt()` (L75) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.c`
- `c_dpi_ascon_round()` (L132) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.c`
- `ascon_data_get()` (L147) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.c`
- `ascon_data_put()` (L171) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.c`
- `ascon_model_dpi.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi.h`
- `ascon_model_dpi_pkg.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\ascon_model_dpi_pkg.sv`
- `aead.c` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\aead.c`
- `crypto_aead_encrypt()` (L8) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\aead.c`
- `crypto_aead_decrypt()` (L106) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\aead.c`
- `api.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\api.h`
- `ascon.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\ascon.h`
- `constants.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\constants.h`
- `crypto_aead.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\crypto_aead.h`
- `permutations.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\permutations.h`
- `P12()` (L11) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\permutations.h`
- `P8()` (L26) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\permutations.h`
- `P6()` (L37) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\permutations.h`
- `printstate.c` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\printstate.c`
- `printword()` (L17) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\printstate.c`
- `printstate()` (L21) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\printstate.c`
- `printstate.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\printstate.h`
- `round.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\round.h`
- `ROR()` (L8) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\round.h`
- `ROUND()` (L12) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\round.h`
- `word.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\word.h`
- `LOADBYTES()` (L19) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\word.h`
- `STOREBYTES()` (L27) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\word.h`
- `CLEARBYTES()` (L33) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\word.h`
- `aead.c` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\aead.c`
- `api.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\api.h`
- `ascon.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\ascon.h`
- `constants.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\constants.h`
- `crypto_aead.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\crypto_aead.h`
- `permutations.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\permutations.h`
- `printstate.c` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\printstate.c`
- `printstate.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\printstate.h`
- `round.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\round.h`
- `word.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\word.h`
- `prim_esc_tb.sv` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_esc\tb\prim_esc_tb.sv`

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
| `spec_path_matches_code_path` | `prim_keccak.md` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `clk_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_if.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `clk_rst_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\clk_rst_if.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `common_ifs_pkg.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\common_ifs_pkg.sv` |
| `spec_path_matches_code_path` | `prim_keccak.md` | `entropy_subsys_fifo_exception_if.sv` | `ibex\vendor\lowrisc_ip\dv\sv\common_ifs\entropy_subsys_fifo_exception_if.sv` |
| `spec_path_matches_code_path` | `prim_lfsr.md` | `ibex_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_core.sv` |
| `spec_path_matches_code_path` | `prim_lfsr.md` | `ibex_pkg` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_wb_stage.sv` |
| `spec_path_matches_code_path` | `prim_lfsr.md` | `ibex_top` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_top_tracing.sv` |
| `spec_path_matches_code_path` | `prim_lfsr.md` | `ibex_compressed_decoder` | `opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_if_stage.sv` |
| `spec_path_matches_code_path` | `prim_lfsr.md` | `mem_assume_t` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `prim_lfsr.md` | `sail_ibexspec` | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\spec\spec_api.sv` |
| `spec_path_matches_code_path` | `prim_lfsr.md` | `bus` | `opentitan\hw\vendor\lowrisc_ibex\dv\riscv_compliance\rtl\ibex_riscv_compliance.sv` |
| `spec_path_matches_code_path` | `prim_lfsr.md` | `ibex_top_tracing` | `opentitan\hw\vendor\lowrisc_ibex\dv\uvm\core_ibex\tb\core_ibex_tb_top.sv` |

## Retrieval Guidance

- When a code-only query mentions `prim`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
