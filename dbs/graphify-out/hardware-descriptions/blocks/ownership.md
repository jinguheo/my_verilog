# Hardware Description: ownership

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `ownership`
- `approved_label`: `pending:ownership`
- `doc_anchor`: `ownership`
- `module_name_prefix`: `ownership`
- `bridge_edge_count`: 40

## Inferred Hardware Role

`ownership` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 41
- Code categories: other_code: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:ownership` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `ownership_ecdsa_keys_fake.c` (L1) - `opentitan\sw\device\silicon_creator\lib\ownership\keys\fake\ownership_ecdsa_keys_fake.c`
- `ownership_activate_unittest.cc` (L1) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc`
- `OwnershipActivateTest` (L37) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc`
- `OwnershipActivateInvalidStateTest` (L115) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc`
- `OwnershipActivateValidStateTest` (L119) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc`
- `OwnershipActivateNextBl0Slot` (L123) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc`
- `ownership_unlock_unittest.cc` (L1) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
- `OwnershipUnlockTest` (L40) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
- `OwnershipUnlockAnyStateTest` (L71) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
- `OwnershipUnlockEndorsedStateTest` (L75) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
- `OwnershipUnlockedUpdateStateTest` (L79) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
- `OwnershipUnlockAbortValidStateTest` (L83) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
- `OwnershipUnlockAbortInvalidStateTest` (L87) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
- `OwnershipUnlockUpdateModesTest` (L91) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
- `mock_ownership_key.cc` (L1) - `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc`
- `ownership_key_validate()` (L10) - `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc`
- `ownership_seal_init()` (L19) - `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc`
- `ownership_seal_page()` (L23) - `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc`
- `ownership_seal_check()` (L27) - `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc`
- `ownership_secret_new()` (L31) - `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc`
- `ownership_unittest.cc` (L1) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unittest.cc`
- `OwnershipInitTest` (L42) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unittest.cc`
- `OwnershipInitInvalidPagesTest` (L80) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unittest.cc`
- `mock_ownership_key.h` (L1) - `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.h`
- `ownership_activate.c` (L1) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate.c`
- `ownership_activate()` (L18) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate.c`
- `ownership_activate_handler()` (L125) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate.c`
- `ownership_activate.h` (L1) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate.h`
- `ownership_unlock.c` (L1) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock.c`
- `ownership_unlock_handler()` (L179) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock.c`
- `ownership_unlock.h` (L1) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock.h`
- `ownership_key.c` (L1) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c`
- `ownership_signature_scan()` (L32) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c`
- `ownership_key_validate()` (L52) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c`
- `ownership_seal_init()` (L119) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c`
- `ownership_seal_clear()` (L131) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c`
- `ownership_seal_page()` (L142) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c`
- `ownership_seal_check()` (L147) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c`
- `ownership_secret_new()` (L180) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c`
- `ownership_history_get()` (L254) - `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:ownership` | `ownership_ecdsa_keys_fake.c` | `opentitan\sw\device\silicon_creator\lib\ownership\keys\fake\ownership_ecdsa_keys_fake.c` |
| `spec_component_matches_code` | `component:ownership` | `ownership_activate_unittest.cc` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `OwnershipActivateTest` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `OwnershipActivateInvalidStateTest` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `OwnershipActivateValidStateTest` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `OwnershipActivateNextBl0Slot` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `ownership_unlock_unittest.cc` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `OwnershipUnlockTest` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `OwnershipUnlockAnyStateTest` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `OwnershipUnlockEndorsedStateTest` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `OwnershipUnlockedUpdateStateTest` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `OwnershipUnlockAbortValidStateTest` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `OwnershipUnlockAbortInvalidStateTest` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `OwnershipUnlockUpdateModesTest` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `mock_ownership_key.cc` | `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc` |
| `spec_component_matches_code` | `component:ownership` | `ownership_key_validate()` | `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc` |
| `spec_component_matches_code` | `component:ownership` | `ownership_seal_init()` | `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc` |
| `spec_component_matches_code` | `component:ownership` | `ownership_seal_page()` | `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc` |
| `spec_component_matches_code` | `component:ownership` | `ownership_seal_check()` | `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc` |
| `spec_component_matches_code` | `component:ownership` | `ownership_secret_new()` | `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc` |
| `spec_component_matches_code` | `component:ownership` | `ownership_unittest.cc` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `OwnershipInitTest` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `OwnershipInitInvalidPagesTest` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unittest.cc` |
| `spec_component_matches_code` | `component:ownership` | `mock_ownership_key.h` | `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.h` |
| `spec_component_matches_code` | `component:ownership` | `ownership_activate.c` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate.c` |
| `spec_component_matches_code` | `component:ownership` | `ownership_activate()` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate.c` |
| `spec_component_matches_code` | `component:ownership` | `ownership_activate_handler()` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate.c` |
| `spec_component_matches_code` | `component:ownership` | `ownership_activate.h` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate.h` |
| `spec_component_matches_code` | `component:ownership` | `ownership_unlock.c` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock.c` |
| `spec_component_matches_code` | `component:ownership` | `ownership_unlock_handler()` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock.c` |
| `spec_component_matches_code` | `component:ownership` | `ownership_unlock.h` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock.h` |
| `spec_component_matches_code` | `component:ownership` | `ownership_key.c` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c` |
| `spec_component_matches_code` | `component:ownership` | `ownership_signature_scan()` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c` |
| `spec_component_matches_code` | `component:ownership` | `ownership_key_validate()` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c` |
| `spec_component_matches_code` | `component:ownership` | `ownership_seal_init()` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c` |
| `spec_component_matches_code` | `component:ownership` | `ownership_seal_clear()` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c` |
| `spec_component_matches_code` | `component:ownership` | `ownership_seal_page()` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c` |
| `spec_component_matches_code` | `component:ownership` | `ownership_seal_check()` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c` |
| `spec_component_matches_code` | `component:ownership` | `ownership_secret_new()` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c` |
| `spec_component_matches_code` | `component:ownership` | `ownership_history_get()` | `opentitan\sw\device\silicon_creator\lib\ownership\ownership_key.c` |

## Retrieval Guidance

- When a code-only query mentions `ownership`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
