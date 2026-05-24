# Hardware Description: compliance

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `compliance`
- `bridge_edge_count`: 2
- Spec categories: component: 3
- Code categories: other_code: 2
- Bridge relations: spec_component_matches_code: 2

## Spec Anchors

- `component:compliance` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**OTHER_CODE** (2)
  - `compliance_main.c`:L1 — `opentitan\third_party\riscv-compliance\compliance_main.c`
  - `test_main()`:L23 — `opentitan\third_party\riscv-compliance\compliance_main.c`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:compliance` | `compliance_main.c` | `opentitan\third_party\riscv-compliance\compliance_main.c` |
| `spec_component_matches_code` | `component:compliance` | `test_main()` | `opentitan\third_party\riscv-compliance\compliance_main.c` |

## Retrieval Guidance

- For code-only queries mentioning `compliance`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `compliance`.
