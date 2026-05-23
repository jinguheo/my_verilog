# Hardware Description: cs_registers

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `cs_registers`
- `approved_label`: `pending:cs_registers`
- `doc_anchor`: `cs_registers`
- `module_name_prefix`: `cs_registers`
- `bridge_edge_count`: 40

## Inferred Hardware Role

`cs_registers` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 41
- Code categories: dv: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:cs_registers` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `tb_cs_registers.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\tb\tb_cs_registers.sv`
- `tb_cs_registers` (L5) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\tb\tb_cs_registers.sv`
- `tb_cs_registers.sv` (L1) - `ibex\dv\cs_registers\tb\tb_cs_registers.sv`
- `tb_cs_registers` (L5) - `ibex\dv\cs_registers\tb\tb_cs_registers.sv`
- `reg_dpi.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\reg_dpi.sv`
- `rst_dpi.sv` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\rst_dpi.sv`
- `reg_dpi.sv` (L1) - `ibex\dv\cs_registers\reg_driver\reg_dpi.sv`
- `rst_dpi.sv` (L1) - `ibex\dv\cs_registers\rst_driver\rst_dpi.sv`
- `tb_cs_registers.cc` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\tb\tb_cs_registers.cc`
- `tb_cs_registers.cc` (L1) - `ibex\dv\cs_registers\tb\tb_cs_registers.cc`
- `Randomize()` (L9) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc`
- `Print()` (L27) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc`
- `RegOpString()` (L37) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc`
- `RegAddrString()` (L52) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc`
- `register_transaction.cc` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.cc`
- `register_transaction.h` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_transaction.h`
- `OnInitial()` (L16) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc`
- `OnFinal()` (L25) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc`
- `Randomize()` (L31) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc`
- `CaptureTransaction()` (L40) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc`
- `DriveOutputs()` (L58) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc`
- `OnClock()` (L68) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc`
- `register_driver.cc` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.cc`
- `RegisterDriver()` (L18) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.h`
- `register_driver.h` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\reg_driver\register_driver.h`
- `OnInitial()` (L13) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\reset_driver.cc`
- `OnFinal()` (L20) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\reset_driver.cc`
- `DriveReset()` (L22) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\reset_driver.cc`
- `reset_driver.cc` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\reset_driver.cc`
- `ResetDriver()` (L14) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\reset_driver.h`
- `reset_driver.h` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\rst_driver\reset_driver.h`
- `RegisterReset()` (L100) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\register_model.cc`
- `NewTransaction()` (L106) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\register_model.cc`
- `register_model.cc` (L1) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\register_model.cc`
- `RegisterWrite()` (L14) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\base_register.cc`
- `RegisterSet()` (L22) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\base_register.cc`
- `RegisterClear()` (L29) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\base_register.cc`
- `MatchAddr()` (L36) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\base_register.cc`
- `ProcessTransaction()` (L40) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\base_register.cc`
- `RegisterReset()` (L80) - `opentitan\hw\vendor\lowrisc_ibex\dv\cs_registers\model\base_register.cc`

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

- When a code-only query mentions `cs_registers`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
