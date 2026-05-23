# Hardware Description: testplan

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `testplan`
- `approved_label`: `pending:testplan`
- `doc_anchor`: `testplan`
- `module_name_prefix`: `testplan`
- `bridge_edge_count`: 40

## Inferred Hardware Role

`testplan` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: testplan: 41
- Code categories: other_code: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:testplan` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `Testplan` (L14) - `opentitan\util\testplantool\testplanlib\lib.py`
- `Testplan.py` (L1) - `ibex\vendor\lowrisc_ip\util\dvsim\Testplan.py`
- `Testplan` (L40) - `opentitan\util\py\scripts\gh_testplan.py`
- `Testplan` (L235) - `opentitan\util\dvsim\Testplan.py`
- `_create_testplan_elements()` (L256) - `opentitan\util\dvsim\Testplan.py`
- `_get_imported_testplan_paths()` (L362) - `opentitan\util\dvsim\Testplan.py`
- `._parse_testplan()` (L407) - `opentitan\util\dvsim\Testplan.py`
- `.write_testplan_doc()` (L485) - `opentitan\util\dvsim\Testplan.py`
- `An element of the testplan.      This is either a testpoint or a covergroup.` (L37) - `opentitan\util\dvsim\Testplan.py`
- `Initialize the testplan element.          raw_dict is the dictionary parsed fr` (L48) - `opentitan\util\dvsim\Testplan.py`
- `An testcase entry in the testplan.      A testpoint maps to a unique design fe` (L128) - `opentitan\util\dvsim\Testplan.py`
- `The full testplan      The list of Testpoints and Covergroups make up the test` (L236) - `opentitan\util\dvsim\Testplan.py`
- `Creates testplan elements from the list of raw dicts.          kind is either` (L257) - `opentitan\util\dvsim\Testplan.py`
- `Initialize the testplan.          filename is the HJson file that captures the` (L320) - `opentitan\util\dvsim\Testplan.py`
- `Parse imported testplans with correctly set paths.          Paths of the impor` (L365) - `opentitan\util\dvsim\Testplan.py`
- `Parse testplan Hjson file and create the testplan elements.          It create` (L408) - `opentitan\util\dvsim\Testplan.py`
- `Write testplan documentation in markdown from the hjson testplan.` (L486) - `opentitan\util\dvsim\Testplan.py`
- `Map the covergroups found from simulation to the testplan.          For now, t` (L605) - `opentitan\util\dvsim\Testplan.py`
- `Returns the current progress of the effort towards the testplan.` (L671) - `opentitan\util\dvsim\Testplan.py`
- `Testplan.py` (L1) - `opentitan\util\dvsim\Testplan.py`
- `Result` (L19) - `opentitan\util\dvsim\Testplan.py`
- `.__init__()` (L22) - `opentitan\util\dvsim\Testplan.py`
- `Element` (L36) - `opentitan\util\dvsim\Testplan.py`
- `.__init__()` (L47) - `opentitan\util\dvsim\Testplan.py`
- `.__str__()` (L70) - `opentitan\util\dvsim\Testplan.py`
- `._validate()` (L77) - `opentitan\util\dvsim\Testplan.py`
- `.has_tags()` (L87) - `opentitan\util\dvsim\Testplan.py`
- `Covergroup` (L110) - `opentitan\util\dvsim\Testplan.py`
- `._validate()` (L120) - `opentitan\util\dvsim\Testplan.py`
- `Testpoint` (L127) - `opentitan\util\dvsim\Testplan.py`
- `.__init__()` (L143) - `opentitan\util\dvsim\Testplan.py`
- `.__str__()` (L156) - `opentitan\util\dvsim\Testplan.py`
- `._validate()` (L160) - `opentitan\util\dvsim\Testplan.py`
- `.do_substitutions()` (L171) - `opentitan\util\dvsim\Testplan.py`
- `.map_test_results()` (L202) - `opentitan\util\dvsim\Testplan.py`
- `_parse_hjson()` (L245) - `opentitan\util\dvsim\Testplan.py`
- `_get_percentage()` (L286) - `opentitan\util\dvsim\Testplan.py`
- `get_dv_style_css()` (L294) - `opentitan\util\dvsim\Testplan.py`
- `.__str__()` (L311) - `opentitan\util\dvsim\Testplan.py`
- `.__init__()` (L319) - `opentitan\util\dvsim\Testplan.py`

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

- When a code-only query mentions `testplan`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
