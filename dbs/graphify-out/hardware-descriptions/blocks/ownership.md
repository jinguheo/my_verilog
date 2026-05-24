# Hardware Description: ownership

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `ownership`
- `bridge_edge_count`: 40
- Spec categories: component: 41
- Code categories: other_code: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:ownership` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**OTHER_CODE** (40)
  - `ownership_ecdsa_keys_fake.c`:L1 — `opentitan\sw\device\silicon_creator\lib\ownership\keys\fake\ownership_ecdsa_keys_fake.c`
  - `ownership_activate_unittest.cc`:L1 — `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc`
  - `OwnershipActivateTest`:L37 — `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc`
  - `OwnershipActivateInvalidStateTest`:L115 — `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc`
  - `OwnershipActivateValidStateTest`:L119 — `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc`
  - `OwnershipActivateNextBl0Slot`:L123 — `opentitan\sw\device\silicon_creator\lib\ownership\ownership_activate_unittest.cc`
  - `ownership_unlock_unittest.cc`:L1 — `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
  - `OwnershipUnlockTest`:L40 — `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
  - `OwnershipUnlockAnyStateTest`:L71 — `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
  - `OwnershipUnlockEndorsedStateTest`:L75 — `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
  - `OwnershipUnlockedUpdateStateTest`:L79 — `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
  - `OwnershipUnlockAbortValidStateTest`:L83 — `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
  - `OwnershipUnlockAbortInvalidStateTest`:L87 — `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
  - `OwnershipUnlockUpdateModesTest`:L91 — `opentitan\sw\device\silicon_creator\lib\ownership\ownership_unlock_unittest.cc`
  - `mock_ownership_key.cc`:L1 — `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc`
  - `ownership_key_validate()`:L10 — `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc`
  - `ownership_seal_init()`:L19 — `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc`
  - `ownership_seal_page()`:L23 — `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc`
  - `ownership_seal_check()`:L27 — `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc`
  - `ownership_secret_new()`:L31 — `opentitan\sw\device\silicon_creator\lib\ownership\mock_ownership_key.cc`

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

- For code-only queries mentioning `ownership`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `ownership`.
