# Hardware Description: compliance

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `compliance`
- `approved_label`: `pending:compliance`
- `doc_anchor`: `compliance`
- `module_name_prefix`: `compliance`
- `bridge_edge_count`: 2

## Inferred Hardware Role

`compliance` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 3
- Code categories: other_code: 2
- Bridge relations: spec_component_matches_code: 2

## Spec Anchors

- `component:compliance` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `compliance_main.c` (L1) - `opentitan\third_party\riscv-compliance\compliance_main.c`
- `test_main()` (L23) - `opentitan\third_party\riscv-compliance\compliance_main.c`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:compliance` | `compliance_main.c` | `opentitan\third_party\riscv-compliance\compliance_main.c` |
| `spec_component_matches_code` | `component:compliance` | `test_main()` | `opentitan\third_party\riscv-compliance\compliance_main.c` |

## Retrieval Guidance

- When a code-only query mentions `compliance`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
