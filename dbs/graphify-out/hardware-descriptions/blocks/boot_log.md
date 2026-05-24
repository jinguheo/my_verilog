# Hardware Description: boot_log

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `boot_log`
- `bridge_edge_count`: 10
- Spec categories: component: 11
- Code categories: other_code: 10
- Bridge relations: spec_component_matches_code: 10

## Spec Anchors

- `component:boot_log` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**OTHER_CODE** (10)
  - `boot_log.rs`:L1 — `opentitan\sw\host\opentitanlib\src\chip\boot_log.rs`
  - `boot_log.c`:L1 — `opentitan\sw\device\silicon_creator\lib\boot_log.c`
  - `boot_log_digest_compute()`:L10 — `opentitan\sw\device\silicon_creator\lib\boot_log.c`
  - `boot_log_digest_update()`:L22 — `opentitan\sw\device\silicon_creator\lib\boot_log.c`
  - `boot_log_check()`:L49 — `opentitan\sw\device\silicon_creator\lib\boot_log.c`
  - `boot_log_check_or_init()`:L74 — `opentitan\sw\device\silicon_creator\lib\boot_log.c`
  - `boot_log.h`:L1 — `opentitan\sw\device\silicon_creator\lib\boot_log.h`
  - `BootLog`:L29 — `opentitan\sw\host\opentitanlib\src\chip\boot_log.rs`
  - `.try_from()`:L62 — `opentitan\sw\host\opentitanlib\src\chip\boot_log.rs`
  - `.valid_digest()`:L90 — `opentitan\sw\host\opentitanlib\src\chip\boot_log.rs`

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

- For code-only queries mentioning `boot_log`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `boot_log`.
