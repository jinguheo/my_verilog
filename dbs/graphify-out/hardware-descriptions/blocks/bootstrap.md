# Hardware Description: bootstrap

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `bootstrap`
- `bridge_edge_count`: 40
- Spec categories: component: 41
- Code categories: other_code: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:bootstrap` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**OTHER_CODE** (40)
  - `rom_e2e_bootstrap_rma_test.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\bootstrap\rom_e2e_bootstrap_rma_test.c`
  - `.uses_common_bootstrap_reset()`:L305 — `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs`
  - `Bootstrap`:L14 — `opentitan\sw\host\opentitanlib\src\test_utils\bootstrap.rs`
  - `bootstrap.rs`:L1 — `opentitan\sw\host\opentitanlib\src\test_utils\bootstrap.rs`
  - `.uses_common_bootstrap_reset()`:L122 — `opentitan\sw\host\opentitanlib\src\bootstrap\primitive.rs`
  - `bootstrap.rs`:L1 — `opentitan\sw\host\opentitantool\src\command\bootstrap.rs`
  - `BootstrapCommand`:L19 — `opentitan\sw\host\opentitantool\src\command\bootstrap.rs`
  - `.bootstrap_using_direct_emulator_integration()`:L34 — `opentitan\sw\host\opentitantool\src\command\bootstrap.rs`
  - `.uses_common_bootstrap_reset()`:L35 — `opentitan\sw\host\opentitanlib\src\bootstrap\eeprom.rs`
  - `LegacyBootstrapError`:L141 — `opentitan\sw\host\opentitanlib\src\bootstrap\legacy.rs`
  - `.uses_common_bootstrap_reset()`:L220 — `opentitan\sw\host\opentitanlib\src\bootstrap\legacy.rs`
  - `bootstrap.c`:L1 — `opentitan\sw\device\silicon_creator\lib\bootstrap.c`
  - `bootstrap_sector_erase()`:L74 — `opentitan\sw\device\silicon_creator\lib\bootstrap.c`
  - `bootstrap_page_program()`:L123 — `opentitan\sw\device\silicon_creator\lib\bootstrap.c`
  - `bootstrap_handle_erase()`:L207 — `opentitan\sw\device\silicon_creator\lib\bootstrap.c`
  - `bootstrap_handle_erase_verify()`:L246 — `opentitan\sw\device\silicon_creator\lib\bootstrap.c`
  - `bootstrap_handle_program()`:L265 — `opentitan\sw\device\silicon_creator\lib\bootstrap.c`
  - `enter_bootstrap()`:L321 — `opentitan\sw\device\silicon_creator\lib\bootstrap.c`
  - `bootstrap.h`:L1 — `opentitan\sw\device\silicon_creator\lib\bootstrap.h`
  - `bootstrap.c`:L1 — `opentitan\sw\device\silicon_creator\rom\bootstrap.c`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:bootstrap` | `rom_e2e_bootstrap_rma_test.c` | `opentitan\sw\device\silicon_creator\rom\e2e\bootstrap\rom_e2e_bootstrap_rma_test.c` |
| `spec_component_matches_code` | `component:bootstrap` | `.uses_common_bootstrap_reset()` | `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `Bootstrap` | `opentitan\sw\host\opentitanlib\src\test_utils\bootstrap.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `bootstrap.rs` | `opentitan\sw\host\opentitanlib\src\test_utils\bootstrap.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `.uses_common_bootstrap_reset()` | `opentitan\sw\host\opentitanlib\src\bootstrap\primitive.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `bootstrap.rs` | `opentitan\sw\host\opentitantool\src\command\bootstrap.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `BootstrapCommand` | `opentitan\sw\host\opentitantool\src\command\bootstrap.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `.bootstrap_using_direct_emulator_integration()` | `opentitan\sw\host\opentitantool\src\command\bootstrap.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `.uses_common_bootstrap_reset()` | `opentitan\sw\host\opentitanlib\src\bootstrap\eeprom.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `LegacyBootstrapError` | `opentitan\sw\host\opentitanlib\src\bootstrap\legacy.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `.uses_common_bootstrap_reset()` | `opentitan\sw\host\opentitanlib\src\bootstrap\legacy.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `bootstrap.c` | `opentitan\sw\device\silicon_creator\lib\bootstrap.c` |
| `spec_component_matches_code` | `component:bootstrap` | `bootstrap_sector_erase()` | `opentitan\sw\device\silicon_creator\lib\bootstrap.c` |
| `spec_component_matches_code` | `component:bootstrap` | `bootstrap_page_program()` | `opentitan\sw\device\silicon_creator\lib\bootstrap.c` |
| `spec_component_matches_code` | `component:bootstrap` | `bootstrap_handle_erase()` | `opentitan\sw\device\silicon_creator\lib\bootstrap.c` |
| `spec_component_matches_code` | `component:bootstrap` | `bootstrap_handle_erase_verify()` | `opentitan\sw\device\silicon_creator\lib\bootstrap.c` |
| `spec_component_matches_code` | `component:bootstrap` | `bootstrap_handle_program()` | `opentitan\sw\device\silicon_creator\lib\bootstrap.c` |
| `spec_component_matches_code` | `component:bootstrap` | `enter_bootstrap()` | `opentitan\sw\device\silicon_creator\lib\bootstrap.c` |
| `spec_component_matches_code` | `component:bootstrap` | `bootstrap.h` | `opentitan\sw\device\silicon_creator\lib\bootstrap.h` |
| `spec_component_matches_code` | `component:bootstrap` | `bootstrap.c` | `opentitan\sw\device\silicon_creator\rom\bootstrap.c` |
| `spec_component_matches_code` | `component:bootstrap` | `bootstrap_chip_erase()` | `opentitan\sw\device\silicon_creator\rom\bootstrap.c` |
| `spec_component_matches_code` | `component:bootstrap` | `bootstrap_erase_verify()` | `opentitan\sw\device\silicon_creator\rom\bootstrap.c` |
| `spec_component_matches_code` | `component:bootstrap` | `bootstrap_requested()` | `opentitan\sw\device\silicon_creator\rom\bootstrap.c` |
| `spec_component_matches_code` | `component:bootstrap` | `bootstrap.h` | `opentitan\sw\device\silicon_creator\rom\bootstrap.h` |
| `spec_component_matches_code` | `component:bootstrap` | `BootstrapError` | `opentitan\sw\host\opentitanlib\src\bootstrap\mod.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `BootstrapProtocol` | `opentitan\sw\host\opentitanlib\src\bootstrap\mod.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `BootstrapOptions` | `opentitan\sw\host\opentitanlib\src\bootstrap\mod.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `Bootstrap<'a>` | `opentitan\sw\host\opentitanlib\src\bootstrap\mod.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `Bootstrap` | `opentitan\sw\host\opentitanlib\src\transport\mod.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `.bootstrap()` | `opentitan\sw\host\ot_transports\proxy\src\lib.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `test_main()` | `opentitan\sw\device\silicon_creator\rom\e2e\bootstrap\rom_e2e_bootstrap_rma_test.c` |
| `spec_component_matches_code` | `component:bootstrap` | `legacy_rescue.rs` | `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `FrameHeader` | `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `Frame` | `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `.default()` | `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `.header_hash()` | `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `.frame_hash()` | `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `.from_payload()` | `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `LegacyRescueError` | `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs` |
| `spec_component_matches_code` | `component:bootstrap` | `LegacyRescue` | `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs` |

## Retrieval Guidance

- For code-only queries mentioning `bootstrap`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `bootstrap`.
