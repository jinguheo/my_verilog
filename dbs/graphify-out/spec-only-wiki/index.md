# Spec-Only Wiki

This wiki is generated from the Graphify spec-only graph. It shows document nodes, internal section nodes, component links, topic links, and source snippets around extracted section lines.

- Documents: 985
- Sections: 6748
- Components: 437
- Topics: 16

## Document Kinds

| Kind | Count |
|---|---:|
| `doc` | 418 |
| `testplan` | 186 |
| `hjson` | 185 |
| `checklist` | 73 |
| `theory` | 65 |
| `interface` | 55 |
| `other` | 3 |

## Top Documents By Section Count

| Document | Project | Kind | Sections | Components |
|---|---|---|---:|---|
| `ibex/doc/03_reference/coverage_plan.rst` | `ibex` | `doc` | 10 | component:coverage_plan, component:contributing, component:debug, component:fcov |
| `ibex/doc/03_reference/cs_registers.rst` | `ibex` | `doc` | 10 | component:cs_registers, component:debug, component:icache, component:integration |
| `ibex/doc/03_reference/icache.rst` | `ibex` | `doc` | 10 | component:icache, component:background, component:pmp, component:prim |
| `ibex/doc/03_reference/instruction_decode_execute.rst` | `ibex` | `doc` | 10 | component:instruction_decode_execute, component:interfaces, component:specification, component:targets |
| `ibex/doc/03_reference/security.rst` | `ibex` | `doc` | 10 | component:security, component:icache, component:software, component:system |
| `ibex/doc/03_reference/verification.rst` | `ibex` | `doc` | 10 | component:verification, component:compliance, component:debug, component:development_stages |
| `ibex/dv/uvm/icache/doc/ibex_icache_dv_plan.md` | `ibex` | `doc` | 10 | component:ibex_icache_dv_plan, component:development_stages, component:edit, component:ibex_icache_testplan |
| `ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md` | `ibex` | `doc` | 10 | component:prim, component:prim_flash, component:examples, component:interfaces |
| `ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md` | `ibex` | `doc` | 10 | component:design_doc, component:contributing, component:debug, component:glossary |
| `ibex/vendor/lowrisc_ip/util/dvsim/doc/glossary.md` | `ibex` | `doc` | 10 | component:glossary, component:contributing, component:cores, component:hjson_usage_style |
| `ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md` | `ibex` | `testplan` | 10 | component:testplanner, component:contributing, component:development_stages, component:examples |
| `opentitan/doc/contributing/bazel_notes.md` | `opentitan` | `doc` | 10 | component:bazel_notes, component:build_sw, component:contributing, component:examples |
| `opentitan/doc/contributing/detailed_contribution_guide/README.md` | `opentitan` | `doc` | 10 | component:readme, component:asm_coding_style, component:c_cpp_coding_style, component:committers |
| `opentitan/doc/contributing/doc/example_ip_block.md` | `opentitan` | `doc` | 10 | component:example_ip_block, component:contributing, component:integration, component:interfaces |
| `opentitan/doc/contributing/dv/methodology/README.md` | `opentitan` | `doc` | 10 | component:readme, component:build_docs, component:build_sw, component:cfg |
| `opentitan/doc/contributing/fpga/debugging_with_ila.md` | `opentitan` | `doc` | 10 | component:debugging_with_ila, component:background, component:bootstrap, component:debug |
| `opentitan/doc/contributing/fpga/ref_manual_fpga.md` | `opentitan` | `doc` | 10 | component:ref_manual_fpga, component:boot, component:bootstrap, component:examples |
| `opentitan/doc/contributing/github_notes.md` | `opentitan` | `doc` | 10 | component:github_notes, component:build_docs, component:cfg, component:contributing |
| `opentitan/doc/contributing/hw/comportability/README.md` | `opentitan` | `doc` | 10 | component:readme, component:aes, component:alert_handler, component:background |
| `opentitan/doc/contributing/hw/design.md` | `opentitan` | `doc` | 10 | component:aes, component:development_stages, component:lowrisc, component:markdown_usage_style |
| `opentitan/doc/contributing/hw/methodology.md` | `opentitan` | `doc` | 10 | component:methodology, component:build_docs, component:compliance, component:debug |
| `opentitan/doc/contributing/hw/racl/README.md` | `opentitan` | `doc` | 10 | component:readme, component:all_rd_wr_mapping, component:boot, component:examples |
| `opentitan/doc/contributing/hw/vendor.md` | `opentitan` | `doc` | 10 | component:vendor, component:background, component:contributing, component:history |
| `opentitan/doc/contributing/style_guides/asm_coding_style.md` | `opentitan` | `doc` | 10 | component:asm_coding_style, component:c_cpp_coding_style, component:isa, component:opentitan |
| `opentitan/doc/contributing/style_guides/c_cpp_coding_style.md` | `opentitan` | `doc` | 10 | component:c_cpp_coding_style, component:boot, component:examples, component:guidance_for_volatile |
| `opentitan/doc/contributing/style_guides/guidance_for_volatile.md` | `opentitan` | `doc` | 10 | component:guidance_for_volatile, component:boot, component:examples, component:lowrisc |
| `opentitan/doc/contributing/style_guides/hjson_usage_style.md` | `opentitan` | `doc` | 10 | component:hjson_usage_style, component:lowrisc, component:opentitan, component:tools |
| `opentitan/doc/contributing/style_guides/markdown_usage_style.md` | `opentitan` | `doc` | 10 | component:markdown_usage_style, component:contributing, component:opentitan, component:readme |
| `opentitan/doc/contributing/style_guides/otbn_style_guide.md` | `opentitan` | `doc` | 10 | component:otbn_style_guide, component:asm_coding_style, component:lowrisc, component:opentitan |
| `opentitan/doc/contributing/style_guides/python_coding_style.md` | `opentitan` | `doc` | 10 | component:python_coding_style, component:cfg, component:edit, component:lowrisc |
| `opentitan/doc/contributing/sw/device_interface_functions.md` | `opentitan` | `interface` | 10 | component:device_interface_functions, component:c_cpp_coding_style, component:development_stages, component:examples |
| `opentitan/doc/getting_started/README.md` | `opentitan` | `doc` | 10 | component:readme, component:build_docs, component:build_sw, component:contributing |
| `opentitan/doc/getting_started/build_sw.md` | `opentitan` | `doc` | 10 | component:build_sw, component:boot, component:debug, component:examples |
| `opentitan/doc/getting_started/setup_fpga.md` | `opentitan` | `doc` | 10 | component:setup_fpga, component:boot, component:bootstrap, component:cfg |
| `opentitan/doc/getting_started/setup_verilator.md` | `opentitan` | `doc` | 10 | component:setup_verilator, component:cfg, component:debug, component:gpio |
| `opentitan/doc/glossary.md` | `opentitan` | `doc` | 10 | component:glossary, component:aes, component:boot, component:contributing |
| `opentitan/doc/project_governance/checklist/README.md` | `opentitan` | `checklist` | 10 | component:readme, component:checklist, component:contributing, component:debug |
| `opentitan/doc/project_governance/development_stages.md` | `opentitan` | `doc` | 10 | component:development_stages, component:checklist, component:contributing, component:device_interface_functions |
| `opentitan/doc/project_governance/governing_board.md` | `opentitan` | `doc` | 10 | component:governing_board, component:code_of_conduct, component:governance, component:lowrisc |
| `opentitan/doc/project_governance/membership.md` | `opentitan` | `doc` | 10 | component:membership, component:checklist, component:committers, component:compliance |
| `opentitan/doc/project_governance/project_milestone_definitions.md` | `opentitan` | `doc` | 10 | component:project_milestone_definitions, component:checklist, component:compliance, component:contributing |
| `opentitan/doc/project_governance/technical_committee.md` | `opentitan` | `doc` | 10 | component:technical_committee, component:code_of_conduct, component:committers, component:compliance |
| `opentitan/doc/project_governance/useraccounts.md` | `opentitan` | `doc` | 10 | component:useraccounts, component:code_of_conduct, component:communications, component:compliance |
| `opentitan/doc/project_governance/working_group.md` | `opentitan` | `doc` | 10 | component:working_group, component:contributor, component:governance, component:membership |
| `opentitan/doc/rust_for_c_devs.md` | `opentitan` | `doc` | 10 | component:rust_for_c_devs, component:debug, component:examples, component:gpio |
| `opentitan/doc/security/README.md` | `opentitan` | `doc` | 10 | component:readme, component:aes, component:alert_handler, component:boot |
| `opentitan/doc/security/cryptolib/contributing.md` | `opentitan` | `doc` | 10 | component:contributing, component:background, component:c_cpp_coding_style, component:cryptolib_api |
| `opentitan/doc/security/cryptolib/cryptolib_api.md` | `opentitan` | `doc` | 10 | component:cryptolib_api, component:aes, component:compliance, component:csrng |
| `opentitan/doc/security/implementation_guidelines/hardware/README.md` | `opentitan` | `doc` | 10 | component:readme, component:aes, component:boot, component:contributing |
| `opentitan/doc/security/implementation_guidelines/reset_vs_non-reset_flops/README.md` | `opentitan` | `doc` | 10 | component:readme, component:aes, component:cores, component:examples |
| `opentitan/doc/security/logical_security_model/README.md` | `opentitan` | `doc` | 10 | component:readme, component:boot, component:bootstrap, component:examples |
| `opentitan/doc/security/specs/attestation/README.md` | `opentitan` | `doc` | 10 | component:readme, component:aes, component:boot, component:debug |
| `opentitan/doc/security/specs/device_life_cycle/README.md` | `opentitan` | `doc` | 10 | component:readme, component:background, component:debug, component:edit |
| `opentitan/doc/security/specs/device_provisioning/README.md` | `opentitan` | `doc` | 10 | component:readme, component:aes, component:boot, component:bootstrap |
| `opentitan/doc/security/specs/identities_and_root_keys/README.md` | `opentitan` | `doc` | 10 | component:readme, component:boot, component:debug, component:kmac |
| `opentitan/doc/security/specs/ownership_transfer/README.md` | `opentitan` | `doc` | 10 | component:readme, component:boot, component:edit, component:examples |
| `opentitan/doc/security/specs/secure_boot/README.md` | `opentitan` | `doc` | 10 | component:readme, component:boot, component:isa, component:keymgr |
| `opentitan/doc/use_cases/tpm/README.md` | `opentitan` | `doc` | 10 | component:readme, component:aes, component:boot, component:compliance |
| `opentitan/hw/data/common_project_cfg.hjson` | `opentitan` | `hjson` | 10 | component:common_project_cfg, component:lowrisc, component:opentitan |
| `opentitan/hw/dv/doc/dv_doc_template.md` | `opentitan` | `doc` | 10 | component:dv_doc_template, component:compliance, component:development_stages, component:hmac |
| `opentitan/hw/ip/adc_ctrl/data/adc_ctrl.hjson` | `opentitan` | `hjson` | 10 | component:adc_ctrl, component:checklist, component:debug, component:lowrisc |
| `opentitan/hw/ip/adc_ctrl/doc/checklist.md` | `opentitan` | `checklist` | 10 | component:adc_ctrl, component:checklist, component:development_stages, component:integration |
| `opentitan/hw/ip/adc_ctrl/doc/registers.md` | `opentitan` | `doc` | 10 | component:adc_ctrl, component:debug |
| `opentitan/hw/ip/aes/data/aes.hjson` | `opentitan` | `hjson` | 10 | component:aes, component:checklist, component:csrng, component:edn |
| `opentitan/hw/ip/aes/doc/checklist.md` | `opentitan` | `checklist` | 10 | component:aes, component:checklist, component:development_stages, component:integration |
| `opentitan/hw/ip/aes/doc/programmers_guide.md` | `opentitan` | `doc` | 10 | component:aes, component:programmers_guide, component:edn, component:software |
| `opentitan/hw/ip/aes/doc/registers.md` | `opentitan` | `doc` | 10 | component:aes, component:dma, component:edn, component:examples |
| `opentitan/hw/ip/aes/doc/theory_of_operation.md` | `opentitan` | `theory` | 10 | component:aes, component:theory_of_operation, component:csrng, component:edn |
| `opentitan/hw/ip/aon_timer/data/aon_timer.hjson` | `opentitan` | `hjson` | 10 | component:aon_timer, component:checklist, component:lowrisc, component:opentitan |
| `opentitan/hw/ip/aon_timer/doc/checklist.md` | `opentitan` | `checklist` | 10 | component:aon_timer, component:checklist, component:development_stages, component:integration |
| `opentitan/hw/ip/aon_timer/doc/programmers_guide.md` | `opentitan` | `doc` | 10 | component:aon_timer, component:programmers_guide, component:software |
| `opentitan/hw/ip/aon_timer/doc/registers.md` | `opentitan` | `doc` | 10 | component:aon_timer |
| `opentitan/hw/ip/ascon/data/ascon.hjson` | `opentitan` | `hjson` | 10 | component:ascon, component:checklist, component:edn, component:examples |
| `opentitan/hw/ip/ascon/doc/checklist.md` | `opentitan` | `checklist` | 10 | component:ascon, component:checklist, component:development_stages, component:integration |
| `opentitan/hw/ip/ascon/doc/registers.md` | `opentitan` | `doc` | 10 | component:ascon, component:examples, component:software |
| `opentitan/hw/ip/ascon/doc/theory_of_operation.md` | `opentitan` | `theory` | 10 | component:ascon, component:theory_of_operation, component:aes, component:dma |
| `opentitan/hw/ip/csrng/data/csrng.hjson` | `opentitan` | `hjson` | 10 | component:csrng, component:aes, component:checklist, component:compliance |
| `opentitan/hw/ip/csrng/doc/checklist.md` | `opentitan` | `checklist` | 10 | component:checklist, component:csrng, component:aes, component:development_stages |
| `opentitan/hw/ip/csrng/doc/registers.md` | `opentitan` | `doc` | 10 | component:csrng, component:aes, component:compliance, component:debug |
| `opentitan/hw/ip/csrng/doc/theory_of_operation.md` | `opentitan` | `theory` | 10 | component:csrng, component:theory_of_operation, component:aes, component:boot |
