# Hardware Description: testplanner

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `testplanner`
- `bridge_edge_count`: 3
- Spec categories: testplan: 4
- Code categories: other_code: 3
- Bridge relations: spec_component_matches_code: 3

## Spec Anchors

- `component:testplanner` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**OTHER_CODE** (3)
  - `testplanner.py`:L1 — `ibex\vendor\lowrisc_ip\util\dvsim\testplanner.py`
  - `testplanner.py`:L1 — `opentitan\util\dvsim\testplanner.py`
  - `main()`:L14 — `opentitan\util\dvsim\testplanner.py`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:testplanner` | `testplanner.py` | `ibex\vendor\lowrisc_ip\util\dvsim\testplanner.py` |
| `spec_component_matches_code` | `component:testplanner` | `testplanner.py` | `opentitan\util\dvsim\testplanner.py` |
| `spec_component_matches_code` | `component:testplanner` | `main()` | `opentitan\util\dvsim\testplanner.py` |

## Retrieval Guidance

- For code-only queries mentioning `testplanner`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `testplanner`.
