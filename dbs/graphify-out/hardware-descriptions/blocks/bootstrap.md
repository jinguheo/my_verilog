# Hardware Description: bootstrap

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `bootstrap`
- `approved_label`: `pending:bootstrap`
- `doc_anchor`: `bootstrap`
- `module_name_prefix`: `bootstrap`
- `bridge_edge_count`: 40

## Inferred Hardware Role

`bootstrap` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 41
- Code categories: other_code: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:bootstrap` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `rom_e2e_bootstrap_rma_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\bootstrap\rom_e2e_bootstrap_rma_test.c`
- `.uses_common_bootstrap_reset()` (L305) - `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs`
- `Bootstrap` (L14) - `opentitan\sw\host\opentitanlib\src\test_utils\bootstrap.rs`
- `bootstrap.rs` (L1) - `opentitan\sw\host\opentitanlib\src\test_utils\bootstrap.rs`
- `.uses_common_bootstrap_reset()` (L122) - `opentitan\sw\host\opentitanlib\src\bootstrap\primitive.rs`
- `bootstrap.rs` (L1) - `opentitan\sw\host\opentitantool\src\command\bootstrap.rs`
- `BootstrapCommand` (L19) - `opentitan\sw\host\opentitantool\src\command\bootstrap.rs`
- `.bootstrap_using_direct_emulator_integration()` (L34) - `opentitan\sw\host\opentitantool\src\command\bootstrap.rs`
- `.uses_common_bootstrap_reset()` (L35) - `opentitan\sw\host\opentitanlib\src\bootstrap\eeprom.rs`
- `LegacyBootstrapError` (L141) - `opentitan\sw\host\opentitanlib\src\bootstrap\legacy.rs`
- `.uses_common_bootstrap_reset()` (L220) - `opentitan\sw\host\opentitanlib\src\bootstrap\legacy.rs`
- `bootstrap.c` (L1) - `opentitan\sw\device\silicon_creator\lib\bootstrap.c`
- `bootstrap_sector_erase()` (L74) - `opentitan\sw\device\silicon_creator\lib\bootstrap.c`
- `bootstrap_page_program()` (L123) - `opentitan\sw\device\silicon_creator\lib\bootstrap.c`
- `bootstrap_handle_erase()` (L207) - `opentitan\sw\device\silicon_creator\lib\bootstrap.c`
- `bootstrap_handle_erase_verify()` (L246) - `opentitan\sw\device\silicon_creator\lib\bootstrap.c`
- `bootstrap_handle_program()` (L265) - `opentitan\sw\device\silicon_creator\lib\bootstrap.c`
- `enter_bootstrap()` (L321) - `opentitan\sw\device\silicon_creator\lib\bootstrap.c`
- `bootstrap.h` (L1) - `opentitan\sw\device\silicon_creator\lib\bootstrap.h`
- `bootstrap.c` (L1) - `opentitan\sw\device\silicon_creator\rom\bootstrap.c`
- `bootstrap_chip_erase()` (L21) - `opentitan\sw\device\silicon_creator\rom\bootstrap.c`
- `bootstrap_erase_verify()` (L32) - `opentitan\sw\device\silicon_creator\rom\bootstrap.c`
- `bootstrap_requested()` (L40) - `opentitan\sw\device\silicon_creator\rom\bootstrap.c`
- `bootstrap.h` (L1) - `opentitan\sw\device\silicon_creator\rom\bootstrap.h`
- `BootstrapError` (L29) - `opentitan\sw\host\opentitanlib\src\bootstrap\mod.rs`
- `BootstrapProtocol` (L44) - `opentitan\sw\host\opentitanlib\src\bootstrap\mod.rs`
- `BootstrapOptions` (L77) - `opentitan\sw\host\opentitanlib\src\bootstrap\mod.rs`
- `Bootstrap<'a>` (L114) - `opentitan\sw\host\opentitanlib\src\bootstrap\mod.rs`
- `Bootstrap` (L198) - `opentitan\sw\host\opentitanlib\src\transport\mod.rs`
- `.bootstrap()` (L250) - `opentitan\sw\host\ot_transports\proxy\src\lib.rs`
- `test_main()` (L13) - `opentitan\sw\device\silicon_creator\rom\e2e\bootstrap\rom_e2e_bootstrap_rma_test.c`
- `legacy_rescue.rs` (L1) - `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs`
- `FrameHeader` (L20) - `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs`
- `Frame` (L28) - `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs`
- `.default()` (L34) - `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs`
- `.header_hash()` (L56) - `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs`
- `.frame_hash()` (L63) - `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs`
- `.from_payload()` (L75) - `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs`
- `LegacyRescueError` (L164) - `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs`
- `LegacyRescue` (L175) - `opentitan\sw\host\opentitanlib\src\bootstrap\legacy_rescue.rs`

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

- When a code-only query mentions `bootstrap`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
