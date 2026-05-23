# Hardware Description: ibex

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `ibex`
- `approved_label`: `pending:ibex`
- `doc_anchor`: `ibex`
- `module_name_prefix`: `ibex`
- `bridge_edge_count`: 370

## Inferred Hardware Role

`ibex` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 537, testplan: 36, interface: 7
- Code categories: dv: 534, rtl: 100, other_code: 64
- Bridge relations: spec_path_matches_code_path: 370

## Spec Anchors

- `compliance.rst` (L1) - `ibex/doc/01_overview/compliance.rst`
- `Standards Compliance` (L1) - `ibex/doc/01_overview/compliance.rst`
- `index.rst` (L1) - `ibex/doc/01_overview/index.rst`
- `Introduction to Ibex` (L1) - `ibex/doc/01_overview/index.rst`
- `licensing.rst` (L1) - `ibex/doc/01_overview/licensing.rst`
- `Licensing` (L1) - `ibex/doc/01_overview/licensing.rst`
- `targets.rst` (L1) - `ibex/doc/01_overview/targets.rst`
- `Synthesis Targets` (L1) - `ibex/doc/01_overview/targets.rst`
- `ASIC Synthesis` (L4) - `ibex/doc/01_overview/targets.rst`
- `FPGA Synthesis` (L11) - `ibex/doc/01_overview/targets.rst`
- `verification_overview.rst` (L1) - `ibex/doc/01_overview/verification_overview.rst`
- `Verification Overview` (L1) - `ibex/doc/01_overview/verification_overview.rst`
- `Verification Status` (L9) - `ibex/doc/01_overview/verification_overview.rst`
- `configuration.rst` (L1) - `ibex/doc/02_user/configuration.rst`
- `Ibex Configurations` (L3) - `ibex/doc/02_user/configuration.rst`
- `Configuration Tool` (L11) - `ibex/doc/02_user/configuration.rst`
- `Supported Configurations` (L35) - `ibex/doc/02_user/configuration.rst`
- `examples.rst` (L1) - `ibex/doc/02_user/examples.rst`
- `Examples` (L3) - `ibex/doc/02_user/examples.rst`
- `Simple System` (L14) - `ibex/doc/02_user/examples.rst`
- `getting_started.rst` (L1) - `ibex/doc/02_user/getting_started.rst`
- `Getting Started with Ibex` (L3) - `ibex/doc/02_user/getting_started.rst`
- `index.rst` (L1) - `ibex/doc/02_user/index.rst`
- `Ibex User Guide` (L1) - `ibex/doc/02_user/index.rst`
- `integration.rst` (L1) - `ibex/doc/02_user/integration.rst`
- `Core Integration` (L3) - `ibex/doc/02_user/integration.rst`
- `Register File` (L10) - `ibex/doc/02_user/integration.rst`
- `Identification CSRs` (L17) - `ibex/doc/02_user/integration.rst`
- `Primitives` (L33) - `ibex/doc/02_user/integration.rst`
- `RTL File List` (L65) - `ibex/doc/02_user/integration.rst`
- `Instantiation Template` (L86) - `ibex/doc/02_user/integration.rst`
- `Parameters` (L183) - `ibex/doc/02_user/integration.rst`
- `Interfaces` (L271) - `ibex/doc/02_user/integration.rst`
- `system_requirements.rst` (L1) - `ibex/doc/02_user/system_requirements.rst`
- `System and Tool Requirements` (L1) - `ibex/doc/02_user/system_requirements.rst`

## Code Evidence

- `__init__.py` (L1) - `ibex\__init__.py`
- `conf.py` (L1) - `ibex\doc\conf.py`
- `cosim.h` (L1) - `ibex\dv\cosim\cosim.h`
- `cosim_dpi.cc` (L1) - `ibex\dv\cosim\cosim_dpi.cc`
- `cosim_dpi.h` (L1) - `ibex\dv\cosim\cosim_dpi.h`
- `spike_cosim.cc` (L1) - `ibex\dv\cosim\spike_cosim.cc`
- `spike_cosim.h` (L1) - `ibex\dv\cosim\spike_cosim.h`
- `base_register.cc` (L1) - `ibex\dv\cs_registers\model\base_register.cc`
- `base_register.h` (L1) - `ibex\dv\cs_registers\model\base_register.h`
- `register_model.cc` (L1) - `ibex\dv\cs_registers\model\register_model.cc`
- `register_model.h` (L1) - `ibex\dv\cs_registers\model\register_model.h`
- `register_driver.cc` (L1) - `ibex\dv\cs_registers\reg_driver\register_driver.cc`
- `register_driver.h` (L1) - `ibex\dv\cs_registers\reg_driver\register_driver.h`
- `register_transaction.cc` (L1) - `ibex\dv\cs_registers\reg_driver\register_transaction.cc`
- `register_transaction.h` (L1) - `ibex\dv\cs_registers\reg_driver\register_transaction.h`
- `reg_dpi.cc` (L1) - `ibex\dv\cs_registers\reg_driver\reg_dpi.cc`
- `reg_dpi.sv` (L1) - `ibex\dv\cs_registers\reg_driver\reg_dpi.sv`
- `reset_driver.cc` (L1) - `ibex\dv\cs_registers\rst_driver\reset_driver.cc`
- `reset_driver.h` (L1) - `ibex\dv\cs_registers\rst_driver\reset_driver.h`
- `rst_dpi.cc` (L1) - `ibex\dv\cs_registers\rst_driver\rst_dpi.cc`
- `rst_dpi.sv` (L1) - `ibex\dv\cs_registers\rst_driver\rst_dpi.sv`
- `tb_cs_registers.cc` (L1) - `ibex\dv\cs_registers\tb\tb_cs_registers.cc`
- `tb_cs_registers.sv` (L1) - `ibex\dv\cs_registers\tb\tb_cs_registers.sv`
- `tb_cs_registers` (L5) - `ibex\dv\cs_registers\tb\tb_cs_registers.sv`
- `conductor.py` (L1) - `ibex\dv\formal\conductor.py`
- `smt2manip.py` (L1) - `ibex\dv\formal\smt2manip.py`
- `aiw.rs` (L1) - `ibex\dv\formal\aig-manip\src\aiw.rs`
- `bitvec.rs` (L1) - `ibex\dv\formal\aig-manip\src\bitvec.rs`
- `main.rs` (L1) - `ibex\dv\formal\aig-manip\src\main.rs`
- `vmap.rs` (L1) - `ibex\dv\formal\aig-manip\src\vmap.rs`
- `ywmap.rs` (L1) - `ibex\dv\formal\aig-manip\src\ywmap.rs`
- `encodings.sv` (L1) - `ibex\dv\formal\check\encodings.sv`
- `spec_instance.sv` (L1) - `ibex\dv\formal\check\spec_instance.sv`
- `top.sv` (L1) - `ibex\dv\formal\check\top.sv`
- `top` (L37) - `ibex\dv\formal\check\top.sv`
- `abs.sv` (L1) - `ibex\dv\formal\check\peek\abs.sv`
- `alt_lsu.sv` (L1) - `ibex\dv\formal\check\peek\alt_lsu.sv`
- `alt_lsu` (L17) - `ibex\dv\formal\check\peek\alt_lsu.sv`
- `compare_helper.sv` (L1) - `ibex\dv\formal\check\peek\compare_helper.sv`
- `follower.sv` (L1) - `ibex\dv\formal\check\peek\follower.sv`
- `mem.sv` (L1) - `ibex\dv\formal\check\peek\mem.sv`
- `irqs.sv` (L1) - `ibex\dv\formal\check\protocol\irqs.sv`
- `mem.sv` (L1) - `ibex\dv\formal\check\protocol\mem.sv`
- `fix_bugs.py` (L1) - `ibex\dv\formal\spec\fix_bugs.py`
- `spec_api.sv` (L1) - `ibex\dv\formal\spec\spec_api.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `compliance.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `index.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `index.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `index.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `index.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `index.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `index.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `index.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `index.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `index.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `index.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `index.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `index.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `index.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `index.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `index.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `index.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `integration.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `integration.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `integration.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `integration.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `integration.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `integration.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `integration.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `integration.rst` | `top` | `ibex\dv\formal\check\top.sv` |

## Retrieval Guidance

- When a code-only query mentions `ibex`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
