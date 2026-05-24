# Hardware Description: cs_registers

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `cs_registers`
- `bridge_edge_count`: 40
- Spec categories: component: 41
- Code categories: dv: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:cs_registers` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**DV** (40)
  - `tb_cs_registers.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\tb\tb_cs_registers.sv`
  - `tb_cs_registers`:L5 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\tb\tb_cs_registers.sv`
  - `tb_cs_registers.sv`:L1 — `ibex\dv\cs_registers\tb\tb_cs_registers.sv`
  - `tb_cs_registers`:L5 — `ibex\dv\cs_registers\tb\tb_cs_registers.sv`
  - `reg_dpi.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\reg_dpi.sv`
  - `rst_dpi.sv`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\rst_dpi.sv`
  - `reg_dpi.sv`:L1 — `ibex\dv\cs_registers\reg_driver\reg_dpi.sv`
  - `rst_dpi.sv`:L1 — `ibex\dv\cs_registers\rst_driver\rst_dpi.sv`
  - `tb_cs_registers.cc`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\tb\tb_cs_registers.cc`
  - `tb_cs_registers.cc`:L1 — `ibex\dv\cs_registers\tb\tb_cs_registers.cc`
  - `Randomize()`:L9 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc`
  - `Print()`:L27 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc`
  - `RegOpString()`:L37 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc`
  - `RegAddrString()`:L52 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc`
  - `register_transaction.cc`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc`
  - `register_transaction.h`:L1 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.h`
  - `OnInitial()`:L16 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc`
  - `OnFinal()`:L25 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc`
  - `Randomize()`:L31 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc`
  - `CaptureTransaction()`:L40 — `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:cs_registers` | `tb_cs_registers.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_component_matches_code` | `component:cs_registers` | `tb_cs_registers` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_component_matches_code` | `component:cs_registers` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_component_matches_code` | `component:cs_registers` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_component_matches_code` | `component:cs_registers` | `reg_dpi.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_component_matches_code` | `component:cs_registers` | `rst_dpi.sv` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_component_matches_code` | `component:cs_registers` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_component_matches_code` | `component:cs_registers` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_component_matches_code` | `component:cs_registers` | `tb_cs_registers.cc` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\tb\tb_cs_registers.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `tb_cs_registers.cc` | `ibex\dv\cs_registers\tb\tb_cs_registers.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `Randomize()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `Print()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `RegOpString()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `RegAddrString()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `register_transaction.cc` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `register_transaction.h` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.h` |
| `spec_component_matches_code` | `component:cs_registers` | `OnInitial()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `OnFinal()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `Randomize()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `CaptureTransaction()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `DriveOutputs()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `OnClock()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `register_driver.cc` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `RegisterDriver()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.h` |
| `spec_component_matches_code` | `component:cs_registers` | `register_driver.h` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.h` |
| `spec_component_matches_code` | `component:cs_registers` | `OnInitial()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\reset_driver.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `OnFinal()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\reset_driver.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `DriveReset()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\reset_driver.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `reset_driver.cc` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\reset_driver.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `ResetDriver()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\reset_driver.h` |
| `spec_component_matches_code` | `component:cs_registers` | `reset_driver.h` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\reset_driver.h` |
| `spec_component_matches_code` | `component:cs_registers` | `RegisterReset()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\register_model.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `NewTransaction()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\register_model.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `register_model.cc` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\register_model.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `RegisterWrite()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\base_register.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `RegisterSet()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\base_register.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `RegisterClear()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\base_register.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `MatchAddr()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\base_register.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `ProcessTransaction()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\base_register.cc` |
| `spec_component_matches_code` | `component:cs_registers` | `RegisterReset()` | `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\base_register.cc` |

## Retrieval Guidance

- For code-only queries mentioning `cs_registers`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `cs_registers`.
