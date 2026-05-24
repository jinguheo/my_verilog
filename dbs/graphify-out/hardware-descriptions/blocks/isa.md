# Hardware Description: isa

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `isa`
- `bridge_edge_count`: 40
- Spec categories: component: 41
- Code categories: rtl: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:isa` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**RTL** (40)
  - `riscv_custom_instr_enum.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\custom\riscv_custom_instr_enum.sv`
  - `riscv_floating_point_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_floating_point_instr.sv`
  - `riscv_custom_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\custom\riscv_custom_instr.sv`
  - `riscv_compressed_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_compressed_instr.sv`
  - `riscv_vector_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_vector_instr.sv`
  - `rv32x_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\custom\rv32x_instr.sv`
  - `rv64x_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\custom\rv64x_instr.sv`
  - `riscv_amo_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_amo_instr.sv`
  - `riscv_csr_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_csr_instr.sv`
  - `riscv_zba_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_zba_instr.sv`
  - `riscv_zbb_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_zbb_instr.sv`
  - `riscv_zbc_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_zbc_instr.sv`
  - `riscv_zbs_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_zbs_instr.sv`
  - `riscv_b_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_b_instr.sv`
  - `rv32zba_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32zba_instr.sv`
  - `rv32zbb_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32zbb_instr.sv`
  - `rv32zbc_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32zbc_instr.sv`
  - `rv32zbs_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32zbs_instr.sv`
  - `rv64zba_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv64zba_instr.sv`
  - `rv64zbb_instr.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv64zbb_instr.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:isa` | `riscv_custom_instr_enum.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\custom\riscv_custom_instr_enum.sv` |
| `spec_component_matches_code` | `component:isa` | `riscv_floating_point_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_floating_point_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `riscv_custom_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\custom\riscv_custom_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `riscv_compressed_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_compressed_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `riscv_vector_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_vector_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32x_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\custom\rv32x_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv64x_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\custom\rv64x_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `riscv_amo_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_amo_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `riscv_csr_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_csr_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `riscv_zba_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_zba_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `riscv_zbb_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_zbb_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `riscv_zbc_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_zbc_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `riscv_zbs_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_zbs_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `riscv_b_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_b_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32zba_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32zba_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32zbb_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32zbb_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32zbc_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32zbc_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32zbs_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32zbs_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv64zba_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv64zba_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv64zbb_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv64zbb_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv128c_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv128c_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32dc_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32dc_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32fc_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32fc_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `riscv_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\riscv_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32a_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32a_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32b_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32b_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32c_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32c_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32d_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32d_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32f_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32f_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32i_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32i_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32m_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32m_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv32v_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv32v_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv64a_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv64a_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv64b_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv64b_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv64c_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv64c_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv64d_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv64d_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv64f_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv64f_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv64i_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv64i_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `rv64m_instr.sv` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\src\isa\rv64m_instr.sv` |
| `spec_component_matches_code` | `component:isa` | `riscv_custom_instr_enum.sv` | `ibex\vendor\google_riscv-dv\src\isa\custom\riscv_custom_instr_enum.sv` |

## Retrieval Guidance

- For code-only queries mentioning `isa`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `isa`.
