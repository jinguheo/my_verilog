# Hardware Description: shutdown

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `shutdown`
- `approved_label`: `pending:shutdown`
- `doc_anchor`: `shutdown`
- `module_name_prefix`: `shutdown`
- `bridge_edge_count`: 14

## Inferred Hardware Role

`shutdown` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 15
- Code categories: other_code: 14
- Bridge relations: spec_component_matches_code: 14

## Spec Anchors

- `component:shutdown` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `.shutdown()` (L83) - `opentitan\sw\host\ot_transports\verilator\src\transport.rs`
- `.shutdown()` (L206) - `opentitan\sw\host\opentitanlib\src\debug\openocd.rs`
- `shutdown.c` (L1) - `opentitan\sw\device\silicon_creator\lib\shutdown.c`
- `shutdown_init()` (L97) - `opentitan\sw\device\silicon_creator\lib\shutdown.c`
- `shutdown_redact_inline()` (L255) - `opentitan\sw\device\silicon_creator\lib\shutdown.c`
- `shutdown_redact()` (L278) - `opentitan\sw\device\silicon_creator\lib\shutdown.c`
- `shutdown_redact_policy_inline()` (L289) - `opentitan\sw\device\silicon_creator\lib\shutdown.c`
- `shutdown_redact_policy()` (L317) - `opentitan\sw\device\silicon_creator\lib\shutdown.c`
- `shutdown_tx_wait()` (L351) - `opentitan\sw\device\silicon_creator\lib\shutdown.c`
- `shutdown_print()` (L380) - `opentitan\sw\device\silicon_creator\lib\shutdown.c`
- `shutdown_finalize()` (L529) - `opentitan\sw\device\silicon_creator\lib\shutdown.c`
- `shutdown.h` (L1) - `opentitan\sw\device\silicon_creator\lib\shutdown.h`
- `uart0_base()` (L74) - `opentitan\sw\device\silicon_creator\lib\shutdown.c`
- `clsindex()` (L81) - `opentitan\sw\device\silicon_creator\lib\shutdown.c`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:shutdown` | `.shutdown()` | `opentitan\sw\host\ot_transports\verilator\src\transport.rs` |
| `spec_component_matches_code` | `component:shutdown` | `.shutdown()` | `opentitan\sw\host\opentitanlib\src\debug\openocd.rs` |
| `spec_component_matches_code` | `component:shutdown` | `shutdown.c` | `opentitan\sw\device\silicon_creator\lib\shutdown.c` |
| `spec_component_matches_code` | `component:shutdown` | `shutdown_init()` | `opentitan\sw\device\silicon_creator\lib\shutdown.c` |
| `spec_component_matches_code` | `component:shutdown` | `shutdown_redact_inline()` | `opentitan\sw\device\silicon_creator\lib\shutdown.c` |
| `spec_component_matches_code` | `component:shutdown` | `shutdown_redact()` | `opentitan\sw\device\silicon_creator\lib\shutdown.c` |
| `spec_component_matches_code` | `component:shutdown` | `shutdown_redact_policy_inline()` | `opentitan\sw\device\silicon_creator\lib\shutdown.c` |
| `spec_component_matches_code` | `component:shutdown` | `shutdown_redact_policy()` | `opentitan\sw\device\silicon_creator\lib\shutdown.c` |
| `spec_component_matches_code` | `component:shutdown` | `shutdown_tx_wait()` | `opentitan\sw\device\silicon_creator\lib\shutdown.c` |
| `spec_component_matches_code` | `component:shutdown` | `shutdown_print()` | `opentitan\sw\device\silicon_creator\lib\shutdown.c` |
| `spec_component_matches_code` | `component:shutdown` | `shutdown_finalize()` | `opentitan\sw\device\silicon_creator\lib\shutdown.c` |
| `spec_component_matches_code` | `component:shutdown` | `shutdown.h` | `opentitan\sw\device\silicon_creator\lib\shutdown.h` |
| `spec_component_matches_code` | `component:shutdown` | `uart0_base()` | `opentitan\sw\device\silicon_creator\lib\shutdown.c` |
| `spec_component_matches_code` | `component:shutdown` | `clsindex()` | `opentitan\sw\device\silicon_creator\lib\shutdown.c` |

## Retrieval Guidance

- When a code-only query mentions `shutdown`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
