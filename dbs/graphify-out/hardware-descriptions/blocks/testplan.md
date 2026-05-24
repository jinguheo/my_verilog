# Hardware Description: testplan

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `testplan`
- `bridge_edge_count`: 40
- Spec categories: testplan: 41
- Code categories: other_code: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:testplan` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**OTHER_CODE** (40)
  - `Testplan`:L14 — `opentitan\util\testplantool\testplanlib\lib.py`
  - `Testplan.py`:L1 — `ibex\vendor\lowrisc_ip\util\dvsim\Testplan.py`
  - `Testplan`:L40 — `opentitan\util\py\scripts\gh_testplan.py`
  - `Testplan`:L235 — `opentitan\util\dvsim\Testplan.py`
  - `_create_testplan_elements()`:L256 — `opentitan\util\dvsim\Testplan.py`
  - `_get_imported_testplan_paths()`:L362 — `opentitan\util\dvsim\Testplan.py`
  - `._parse_testplan()`:L407 — `opentitan\util\dvsim\Testplan.py`
  - `.write_testplan_doc()`:L485 — `opentitan\util\dvsim\Testplan.py`
  - `An element of the testplan.      This is either a testpoint or a covergroup.`:L37 — `opentitan\util\dvsim\Testplan.py`
  - `Initialize the testplan element.          raw_dict is the dictionary parsed fr`:L48 — `opentitan\util\dvsim\Testplan.py`
  - `An testcase entry in the testplan.      A testpoint maps to a unique design fe`:L128 — `opentitan\util\dvsim\Testplan.py`
  - `The full testplan      The list of Testpoints and Covergroups make up the test`:L236 — `opentitan\util\dvsim\Testplan.py`
  - `Creates testplan elements from the list of raw dicts.          kind is either`:L257 — `opentitan\util\dvsim\Testplan.py`
  - `Initialize the testplan.          filename is the HJson file that captures the`:L320 — `opentitan\util\dvsim\Testplan.py`
  - `Parse imported testplans with correctly set paths.          Paths of the impor`:L365 — `opentitan\util\dvsim\Testplan.py`
  - `Parse testplan Hjson file and create the testplan elements.          It create`:L408 — `opentitan\util\dvsim\Testplan.py`
  - `Write testplan documentation in markdown from the hjson testplan.`:L486 — `opentitan\util\dvsim\Testplan.py`
  - `Map the covergroups found from simulation to the testplan.          For now, t`:L605 — `opentitan\util\dvsim\Testplan.py`
  - `Returns the current progress of the effort towards the testplan.`:L671 — `opentitan\util\dvsim\Testplan.py`
  - `Testplan.py`:L1 — `opentitan\util\dvsim\Testplan.py`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:testplan` | `Testplan` | `opentitan\util\testplantool\testplanlib\lib.py` |
| `spec_component_matches_code` | `component:testplan` | `Testplan.py` | `ibex\vendor\lowrisc_ip\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Testplan` | `opentitan\util\py\scripts\gh_testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Testplan` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `_create_testplan_elements()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `_get_imported_testplan_paths()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `._parse_testplan()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `.write_testplan_doc()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `An element of the testplan.      This is either a testpoint or a covergroup.` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Initialize the testplan element.          raw_dict is the dictionary parsed fr` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `An testcase entry in the testplan.      A testpoint maps to a unique design fe` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `The full testplan      The list of Testpoints and Covergroups make up the test` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Creates testplan elements from the list of raw dicts.          kind is either` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Initialize the testplan.          filename is the HJson file that captures the` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Parse imported testplans with correctly set paths.          Paths of the impor` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Parse testplan Hjson file and create the testplan elements.          It create` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Write testplan documentation in markdown from the hjson testplan.` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Map the covergroups found from simulation to the testplan.          For now, t` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Returns the current progress of the effort towards the testplan.` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Testplan.py` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Result` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `.__init__()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Element` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `.__init__()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `.__str__()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `._validate()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `.has_tags()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Covergroup` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `._validate()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `Testpoint` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `.__init__()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `.__str__()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `._validate()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `.do_substitutions()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `.map_test_results()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `_parse_hjson()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `_get_percentage()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `get_dv_style_css()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `.__str__()` | `opentitan\util\dvsim\Testplan.py` |
| `spec_component_matches_code` | `component:testplan` | `.__init__()` | `opentitan\util\dvsim\Testplan.py` |

## Retrieval Guidance

- For code-only queries mentioning `testplan`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `testplan`.
