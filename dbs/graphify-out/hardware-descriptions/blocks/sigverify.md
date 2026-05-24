# Hardware Description: sigverify

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `sigverify`
- `bridge_edge_count`: 40
- Spec categories: component: 41
- Code categories: other_code: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:sigverify` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**OTHER_CODE** (40)
  - `sigverify_set_testvectors.py`:L1 — `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_set_testvectors.py`
  - `Compute -(n^-1) mod 2^256, a Montgomery constant.      Sigverify expects this`:L26 — `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_set_testvectors.py`
  - `sigverify_cryptotest.c`:L1 — `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_cryptotest.c`
  - `sigverify_p256_to_status()`:L72 — `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_cryptotest.c`
  - `sigverify_ecdsa_process_command()`:L102 — `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_tests\sigverify_cryptotest.c`
  - `sigverify_dynamic_functest.c`:L1 — `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_dynamic_functest.c`
  - `sigverify_test()`:L22 — `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_dynamic_functest.c`
  - `sigverify_mod_exp_ibex_test()`:L19 — `opentitan\sw\device\silicon_creator\lib\sigverify\mod_exp_ibex_functest.c`
  - `sigverify_unittest.cc`:L1 — `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_unittest.cc`
  - `SigverifyInLcState`:L98 — `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_unittest.cc`
  - `SigverifyUsageConstraints`:L130 — `opentitan\sw\device\silicon_creator\lib\sigverify\sigverify_unittest.cc`
  - `sigverify_spx_verify_enabled()`:L774 — `opentitan\sw\device\silicon_creator\lib\sigverify\spx_verify_functest.c`
  - `sigverify_mod_exp_ibex()`:L9 — `opentitan\sw\device\silicon_creator\lib\sigverify\mock_mod_exp_ibex.cc`
  - `sigverify_encoded_message_check()`:L49 — `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.c`
  - `sigverify_ecdsa_p256_start()`:L121 — `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.c`
  - `sigverify_ecdsa_p256_finish()`:L127 — `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.c`
  - `sigverify_ecdsa_p256_verify()`:L142 — `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.c`
  - `sigverify_ecdsa_p256_success_to_ok()`:L75 — `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_verify.h`
  - `sigverify_usage_constraints_get()`:L13 — `opentitan\sw\device\silicon_creator\lib\sigverify\usage_constraints.c`
  - `sigverify_ecdsa_p256_key_id_get()`:L88 — `opentitan\sw\device\silicon_creator\lib\sigverify\ecdsa_p256_key.h`

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

- For code-only queries mentioning `sigverify`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `sigverify`.
