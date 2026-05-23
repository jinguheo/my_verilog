# Hardware Description: boot_log

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `boot_log`
- `approved_label`: `pending:boot_log`
- `doc_anchor`: `boot_log`
- `module_name_prefix`: `boot_log`
- `bridge_edge_count`: 10

## Inferred Hardware Role

`boot_log` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 11
- Code categories: other_code: 10
- Bridge relations: spec_component_matches_code: 10

## Spec Anchors

- `component:boot_log` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `boot_log.rs` (L1) - `opentitan\sw\host\opentitanlib\src\chip\boot_log.rs`
- `boot_log.c` (L1) - `opentitan\sw\device\silicon_creator\lib\boot_log.c`
- `boot_log_digest_compute()` (L10) - `opentitan\sw\device\silicon_creator\lib\boot_log.c`
- `boot_log_digest_update()` (L22) - `opentitan\sw\device\silicon_creator\lib\boot_log.c`
- `boot_log_check()` (L49) - `opentitan\sw\device\silicon_creator\lib\boot_log.c`
- `boot_log_check_or_init()` (L74) - `opentitan\sw\device\silicon_creator\lib\boot_log.c`
- `boot_log.h` (L1) - `opentitan\sw\device\silicon_creator\lib\boot_log.h`
- `BootLog` (L29) - `opentitan\sw\host\opentitanlib\src\chip\boot_log.rs`
- `.try_from()` (L62) - `opentitan\sw\host\opentitanlib\src\chip\boot_log.rs`
- `.valid_digest()` (L90) - `opentitan\sw\host\opentitanlib\src\chip\boot_log.rs`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:boot_log` | `boot_log.rs` | `opentitan\sw\host\opentitanlib\src\chip\boot_log.rs` |
| `spec_component_matches_code` | `component:boot_log` | `boot_log.c` | `opentitan\sw\device\silicon_creator\lib\boot_log.c` |
| `spec_component_matches_code` | `component:boot_log` | `boot_log_digest_compute()` | `opentitan\sw\device\silicon_creator\lib\boot_log.c` |
| `spec_component_matches_code` | `component:boot_log` | `boot_log_digest_update()` | `opentitan\sw\device\silicon_creator\lib\boot_log.c` |
| `spec_component_matches_code` | `component:boot_log` | `boot_log_check()` | `opentitan\sw\device\silicon_creator\lib\boot_log.c` |
| `spec_component_matches_code` | `component:boot_log` | `boot_log_check_or_init()` | `opentitan\sw\device\silicon_creator\lib\boot_log.c` |
| `spec_component_matches_code` | `component:boot_log` | `boot_log.h` | `opentitan\sw\device\silicon_creator\lib\boot_log.h` |
| `spec_component_matches_code` | `component:boot_log` | `BootLog` | `opentitan\sw\host\opentitanlib\src\chip\boot_log.rs` |
| `spec_component_matches_code` | `component:boot_log` | `.try_from()` | `opentitan\sw\host\opentitanlib\src\chip\boot_log.rs` |
| `spec_component_matches_code` | `component:boot_log` | `.valid_digest()` | `opentitan\sw\host\opentitanlib\src\chip\boot_log.rs` |

## Retrieval Guidance

- When a code-only query mentions `boot_log`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
