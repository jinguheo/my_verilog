# Hardware Description: manifest

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `manifest`
- `bridge_edge_count`: 33
- Spec categories: component: 34
- Code categories: other_code: 33
- Bridge relations: spec_component_matches_code: 33

## Spec Anchors

- `component:manifest` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**OTHER_CODE** (33)
  - `manifest.rs`:L1 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `Manifest`:L72 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `ManifestVersion`:L96 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `ManifestExtHeader`:L119 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `ManifestExtSpxSignature`:L134 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `ManifestExtSpxKey`:L149 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `ManifestExtImageType`:L169 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `ManifestExtSecVerWrite`:L177 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `ManifestExtIsfbProductExpr`:L184 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `ManifestExtIsfb`:L191 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `ManifestExtIsfbErasePolicy`:L219 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `ManifestUsageConstraints`:L234 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `ManifestExtTableEntry`:L272 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `ManifestExtTable`:L279 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `test_manifest_layout()`:L293 — `opentitan\sw\host\opentitanlib\src\image\manifest.rs`
  - `manifest.c`:L1 — `opentitan\sw\device\silicon_creator\lib\manifest.c`
  - `manifest.h`:L1 — `opentitan\sw\device\silicon_creator\lib\manifest.h`
  - `manifest_check()`:L578 — `opentitan\sw\device\silicon_creator\lib\manifest.h`
  - `manifest_digest_region_get()`:L627 — `opentitan\sw\device\silicon_creator\lib\manifest.h`
  - `manifest_code_region_get()`:L646 — `opentitan\sw\device\silicon_creator\lib\manifest.h`

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

- For code-only queries mentioning `manifest`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `manifest`.
