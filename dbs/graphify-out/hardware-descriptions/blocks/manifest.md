# Hardware Description: manifest

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `manifest`
- `approved_label`: `pending:manifest`
- `doc_anchor`: `manifest`
- `module_name_prefix`: `manifest`
- `bridge_edge_count`: 33

## Inferred Hardware Role

`manifest` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 34
- Code categories: other_code: 33
- Bridge relations: spec_component_matches_code: 33

## Spec Anchors

- `component:manifest` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `manifest.rs` (L1) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `Manifest` (L72) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `ManifestVersion` (L96) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `ManifestExtHeader` (L119) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `ManifestExtSpxSignature` (L134) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `ManifestExtSpxKey` (L149) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `ManifestExtImageType` (L169) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `ManifestExtSecVerWrite` (L177) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `ManifestExtIsfbProductExpr` (L184) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `ManifestExtIsfb` (L191) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `ManifestExtIsfbErasePolicy` (L219) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `ManifestUsageConstraints` (L234) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `ManifestExtTableEntry` (L272) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `ManifestExtTable` (L279) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `test_manifest_layout()` (L293) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `manifest.c` (L1) - `opentitan\sw\device\silicon_creator\lib\manifest.c`
- `manifest.h` (L1) - `opentitan\sw\device\silicon_creator\lib\manifest.h`
- `manifest_check()` (L578) - `opentitan\sw\device\silicon_creator\lib\manifest.h`
- `manifest_digest_region_get()` (L627) - `opentitan\sw\device\silicon_creator\lib\manifest.h`
- `manifest_code_region_get()` (L646) - `opentitan\sw\device\silicon_creator\lib\manifest.h`
- `manifest_entry_point_get()` (L665) - `opentitan\sw\device\silicon_creator\lib\manifest.h`
- `SigverifySpxSignature` (L104) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `.default()` (L109) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `.write()` (L125) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `SigverifySpxKey` (L142) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `SigverifyBuffer` (L157) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `.default()` (L162) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `.write()` (L199) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `.to_vec()` (L210) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `LifecycleDeviceId` (L227) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `.default()` (L243) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `Timestamp` (L259) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
- `KeymgrBindingValue` (L266) - `opentitan\sw\host\opentitanlib\src\image\manifest.rs`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:manifest` | `manifest.rs` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `Manifest` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `ManifestVersion` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `ManifestExtHeader` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `ManifestExtSpxSignature` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `ManifestExtSpxKey` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `ManifestExtImageType` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `ManifestExtSecVerWrite` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `ManifestExtIsfbProductExpr` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `ManifestExtIsfb` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `ManifestExtIsfbErasePolicy` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `ManifestUsageConstraints` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `ManifestExtTableEntry` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `ManifestExtTable` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `test_manifest_layout()` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `manifest.c` | `opentitan\sw\device\silicon_creator\lib\manifest.c` |
| `spec_component_matches_code` | `component:manifest` | `manifest.h` | `opentitan\sw\device\silicon_creator\lib\manifest.h` |
| `spec_component_matches_code` | `component:manifest` | `manifest_check()` | `opentitan\sw\device\silicon_creator\lib\manifest.h` |
| `spec_component_matches_code` | `component:manifest` | `manifest_digest_region_get()` | `opentitan\sw\device\silicon_creator\lib\manifest.h` |
| `spec_component_matches_code` | `component:manifest` | `manifest_code_region_get()` | `opentitan\sw\device\silicon_creator\lib\manifest.h` |
| `spec_component_matches_code` | `component:manifest` | `manifest_entry_point_get()` | `opentitan\sw\device\silicon_creator\lib\manifest.h` |
| `spec_component_matches_code` | `component:manifest` | `SigverifySpxSignature` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `.default()` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `.write()` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `SigverifySpxKey` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `SigverifyBuffer` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `.default()` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `.write()` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `.to_vec()` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `LifecycleDeviceId` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `.default()` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `Timestamp` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |
| `spec_component_matches_code` | `component:manifest` | `KeymgrBindingValue` | `opentitan\sw\host\opentitanlib\src\image\manifest.rs` |

## Retrieval Guidance

- When a code-only query mentions `manifest`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
