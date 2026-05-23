# Hardware Description: sigverify

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `sigverify`
- `approved_label`: `pending:sigverify`
- `doc_anchor`: `sigverify`
- `module_name_prefix`: `sigverify`
- `bridge_edge_count`: 40

## Inferred Hardware Role

`sigverify` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 41
- Code categories: other_code: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:sigverify` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `sigverify_set_testvectors.py` (L1) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_set_testvectors.py`
- `Compute -(n^-1) mod 2^256, a Montgomery constant.      Sigverify expects this` (L26) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_set_testvectors.py`
- `sigverify_cryptotest.c` (L1) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_cryptotest.c`
- `sigverify_p256_to_status()` (L72) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_cryptotest.c`
- `sigverify_ecdsa_process_command()` (L102) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_cryptotest.c`
- `sigverify_dynamic_functest.c` (L1) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_dynamic_functest.c`
- `sigverify_test()` (L22) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_dynamic_functest.c`
- `sigverify_mod_exp_ibex_test()` (L19) - `opentitan\sw\device\silicon_creator\lib\sigverify\mod_exp_ibex_functest.c`
- `sigverify_unittest.cc` (L1) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_unittest.cc`
- `SigverifyInLcState` (L98) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_unittest.cc`
- `SigverifyUsageConstraints` (L130) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_unittest.cc`
- `sigverify_spx_verify_enabled()` (L774) - `opentitan\sw\device\silicon_creator\lib\sigverify\spx_verify_functest.c`
- `sigverify_mod_exp_ibex()` (L9) - `opentitan\sw\device\silicon_creator\lib\sigverify\mock_mod_exp_ibex.cc`
- `sigverify_encoded_message_check()` (L49) - `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.c`
- `sigverify_ecdsa_p256_start()` (L121) - `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.c`
- `sigverify_ecdsa_p256_finish()` (L127) - `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.c`
- `sigverify_ecdsa_p256_verify()` (L142) - `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.c`
- `sigverify_ecdsa_p256_success_to_ok()` (L75) - `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.h`
- `sigverify_usage_constraints_get()` (L13) - `opentitan\sw\device\silicon_creator\lib\sigverify\usage_constraints.c`
- `sigverify_ecdsa_p256_key_id_get()` (L88) - `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_key.h`
- `sigverify_mod_exp_ibex()` (L170) - `opentitan\sw\device\silicon_creator\lib\sigverify\mod_exp_ibex.c`
- `sigverify_encoded_message_check()` (L70) - `opentitan\sw\device\silicon_creator\lib\sigverify\rsa_verify.c`
- `sigverify_rsa_verify()` (L154) - `opentitan\sw\device\silicon_creator\lib\sigverify\rsa_verify.c`
- `sigverify_rsa_success_to_ok()` (L54) - `opentitan\sw\device\silicon_creator\lib\sigverify\rsa_verify.h`
- `sigverify_spx_verify_enabled()` (L16) - `opentitan\sw\device\silicon_creator\lib\sigverify\spx_verify.c`
- `sigverify_spx_verify()` (L94) - `opentitan\sw\device\silicon_creator\lib\sigverify\spx_verify.c`
- `sigverify_spx_success_to_ok()` (L92) - `opentitan\sw\device\silicon_creator\lib\sigverify\spx_verify.h`
- `sigverify.h` (L1) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify.h`
- `sigverify_rsa_key_id_get()` (L68) - `opentitan\sw\device\silicon_creator\lib\sigverify\rsa_key.h`
- `sigverify_spx_key_id_get()` (L121) - `opentitan\sw\device\silicon_creator\lib\sigverify\spx_key.h`
- `sphincsplus_set_testvectors.py` (L1) - `opentitan\sw\device\silicon_creator\lib\sigverify\sphincsplus\test\sphincsplus_set_testvectors.py`
- `hex_to_hexbytes()` (L18) - `opentitan\sw\device\silicon_creator\lib\sigverify\sphincsplus\test\sphincsplus_set_testvectors.py`
- `hex_to_hexwords()` (L33) - `opentitan\sw\device\silicon_creator\lib\sigverify\sphincsplus\test\sphincsplus_set_testvectors.py`
- `main()` (L53) - `opentitan\sw\device\silicon_creator\lib\sigverify\sphincsplus\test\sphincsplus_set_testvectors.py`
- `Convert a hex string to a list of bytes as hex strings.` (L19) - `opentitan\sw\device\silicon_creator\lib\sigverify\sphincsplus\test\sphincsplus_set_testvectors.py`
- `Convert a hex string little-endian 32-bit words as hex strings.` (L34) - `opentitan\sw\device\silicon_creator\lib\sigverify\sphincsplus\test\sphincsplus_set_testvectors.py`
- `compute_n0_inv()` (L25) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_set_testvectors.py`
- `encode_message()` (L33) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_set_testvectors.py`
- `rsa_3072_int_to_hexwords()` (L60) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_set_testvectors.py`
- `int_256_to_hexwords()` (L72) - `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_set_testvectors.py`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:sigverify` | `sigverify_set_testvectors.py` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_set_testvectors.py` |
| `spec_component_matches_code` | `component:sigverify` | `Compute -(n^-1) mod 2^256, a Montgomery constant.      Sigverify expects this` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_set_testvectors.py` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_cryptotest.c` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_cryptotest.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_p256_to_status()` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_cryptotest.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_ecdsa_process_command()` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_cryptotest.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_dynamic_functest.c` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_dynamic_functest.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_test()` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_dynamic_functest.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_mod_exp_ibex_test()` | `opentitan\sw\device\silicon_creator\lib\sigverify\mod_exp_ibex_functest.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_unittest.cc` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_unittest.cc` |
| `spec_component_matches_code` | `component:sigverify` | `SigverifyInLcState` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_unittest.cc` |
| `spec_component_matches_code` | `component:sigverify` | `SigverifyUsageConstraints` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_unittest.cc` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_spx_verify_enabled()` | `opentitan\sw\device\silicon_creator\lib\sigverify\spx_verify_functest.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_mod_exp_ibex()` | `opentitan\sw\device\silicon_creator\lib\sigverify\mock_mod_exp_ibex.cc` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_encoded_message_check()` | `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_ecdsa_p256_start()` | `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_ecdsa_p256_finish()` | `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_ecdsa_p256_verify()` | `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_ecdsa_p256_success_to_ok()` | `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.h` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_usage_constraints_get()` | `opentitan\sw\device\silicon_creator\lib\sigverify\usage_constraints.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_ecdsa_p256_key_id_get()` | `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_key.h` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_mod_exp_ibex()` | `opentitan\sw\device\silicon_creator\lib\sigverify\mod_exp_ibex.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_encoded_message_check()` | `opentitan\sw\device\silicon_creator\lib\sigverify\rsa_verify.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_rsa_verify()` | `opentitan\sw\device\silicon_creator\lib\sigverify\rsa_verify.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_rsa_success_to_ok()` | `opentitan\sw\device\silicon_creator\lib\sigverify\rsa_verify.h` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_spx_verify_enabled()` | `opentitan\sw\device\silicon_creator\lib\sigverify\spx_verify.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_spx_verify()` | `opentitan\sw\device\silicon_creator\lib\sigverify\spx_verify.c` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_spx_success_to_ok()` | `opentitan\sw\device\silicon_creator\lib\sigverify\spx_verify.h` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify.h` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify.h` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_rsa_key_id_get()` | `opentitan\sw\device\silicon_creator\lib\sigverify\rsa_key.h` |
| `spec_component_matches_code` | `component:sigverify` | `sigverify_spx_key_id_get()` | `opentitan\sw\device\silicon_creator\lib\sigverify\spx_key.h` |
| `spec_component_matches_code` | `component:sigverify` | `sphincsplus_set_testvectors.py` | `opentitan\sw\device\silicon_creator\lib\sigverify\sphincsplus\test\sphincsplus_set_testvectors.py` |
| `spec_component_matches_code` | `component:sigverify` | `hex_to_hexbytes()` | `opentitan\sw\device\silicon_creator\lib\sigverify\sphincsplus\test\sphincsplus_set_testvectors.py` |
| `spec_component_matches_code` | `component:sigverify` | `hex_to_hexwords()` | `opentitan\sw\device\silicon_creator\lib\sigverify\sphincsplus\test\sphincsplus_set_testvectors.py` |
| `spec_component_matches_code` | `component:sigverify` | `main()` | `opentitan\sw\device\silicon_creator\lib\sigverify\sphincsplus\test\sphincsplus_set_testvectors.py` |
| `spec_component_matches_code` | `component:sigverify` | `Convert a hex string to a list of bytes as hex strings.` | `opentitan\sw\device\silicon_creator\lib\sigverify\sphincsplus\test\sphincsplus_set_testvectors.py` |
| `spec_component_matches_code` | `component:sigverify` | `Convert a hex string little-endian 32-bit words as hex strings.` | `opentitan\sw\device\silicon_creator\lib\sigverify\sphincsplus\test\sphincsplus_set_testvectors.py` |
| `spec_component_matches_code` | `component:sigverify` | `compute_n0_inv()` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_set_testvectors.py` |
| `spec_component_matches_code` | `component:sigverify` | `encode_message()` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_set_testvectors.py` |
| `spec_component_matches_code` | `component:sigverify` | `rsa_3072_int_to_hexwords()` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_set_testvectors.py` |
| `spec_component_matches_code` | `component:sigverify` | `int_256_to_hexwords()` | `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_set_testvectors.py` |

## Retrieval Guidance

- When a code-only query mentions `sigverify`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
