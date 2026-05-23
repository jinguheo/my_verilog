# Hardware Description: ac_range_check

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `ac_range_check`
- `approved_label`: `pending:ac_range_check`
- `doc_anchor`: `ac_range_check`
- `module_name_prefix`: `ac_range_check`
- `bridge_edge_count`: 174

## Inferred Hardware Role

`ac_range_check` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 134, testplan: 35, theory: 25, component: 21, interface: 21
- Code categories: rtl: 111, dv: 56, sva: 26
- Bridge relations: spec_path_matches_code_path: 154, spec_component_matches_code: 20

## Spec Anchors

- `component:ac_range_check` (L1) - `__graphify_spec_only__/components.md`
- `ac_range_check.hjson` (L1) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `human name` (L8) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `one line desc` (L9) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `one paragraph desc` (L10) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `cip id` (L12) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `design spec` (L13) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `dv doc` (L14) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `version` (L15) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `clocking` (L17) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `bus interfaces` (L18) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `param list` (L21) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `ac_range_check_testplan.hjson` (L1) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `testpoints` (L12) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `desc` (L15) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `Stimulus` (L19) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `Checking` (L29) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `stage` (L46) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `tests` (L47) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `covergroups` (L105) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `top_darjeeling_ac_range_check.ipconfig.hjson` (L1) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `instance name` (L5) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `param values` (L6) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `num ranges` (L8) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `nr role bits` (L9) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `nr ctn uid bits` (L10) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `module instance name` (L11) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `topname` (L12) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `uniquified modules` (L13) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `dtgen` (L15) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `checklist.md` (L1) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md`
- `Design Checklist` (L13) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md`
- `D1` (L15) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md`
- `D2` (L41) - `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md`

## Code Evidence

- `prim_flop_en` (L269) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `prim_onehot_enc` (L128) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `ac_range_check_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv`
- `ac_range_check_bind` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv`
- `tb.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv`
- `tb` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv`
- `ac_range_check_env_pkg` (L9) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv`
- `ac_range_check_test_pkg` (L10) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv`
- `ac_range_check_base_test.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_base_test.sv`
- `ac_range_check_test_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv`
- `ac_range_check.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `ac_range_check` (L7) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `ac_range_check_reg_pkg` (L36) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_top.sv`
- `ac_range_check_reg_top` (L53) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `prim_leading_one_ppc` (L217) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `tlul_request_loopback` (L245) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `ac_range_check_reg_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_pkg.sv`
- `ac_range_check_reg_top.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_top.sv`
- `ac_range_check_reg_top` (L9) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_top.sv`
- `ac_range_check` (L2684) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `prim_ram_1p_adv` (L1487) - `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
- `tlul_cmd_intg_gen` (L46) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv`
- `dma` (L2221) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `keymgr_dpe` (L1905) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `tlul_jtag_dtm` (L1340) - `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
- `mbx` (L2257) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_base_test.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_base_test.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_test_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_bind` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_reg_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_top.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_reg_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_pkg.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_reg_top.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_top.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_reg_top` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_top.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_reg_top` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_test_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `prim_leading_one_ppc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `tlul_request_loopback` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `ac_range_check_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `ac_range_check_bind` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `ac_range_check_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `ac_range_check_test_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `ac_range_check_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `ac_range_check_bind` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `ac_range_check_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `ac_range_check_test_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ac_range_check_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ac_range_check_bind` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ac_range_check_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ac_range_check_test_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `ac_range_check_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `ac_range_check_bind` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `ac_range_check_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `ac_range_check_test_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `top_darjeeling.gen.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `top_darjeeling.gen.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `top_darjeeling.secrets.testing.gen.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `top_darjeeling.secrets.testing.gen.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `chip_cfg.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `chip_cfg.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `chip_conn_testplan.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `chip_conn_testplan.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `chip_testplan.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `chip_testplan.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `all_rd_wr_mapping.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `all_rd_wr_mapping.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `racl.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `racl.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `soc_rot_mapping.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `soc_rot_mapping.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `top_darjeeling.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `top_darjeeling.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `top_darjeeling_seed.testing.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `top_darjeeling_seed.testing.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `datasheet.md` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `datasheet.md` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `memory_map.md` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `memory_map.md` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `ac_range_check.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `ac_range_check.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `ac_range_check.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `ac_range_check.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |

## Retrieval Guidance

- When a code-only query mentions `ac_range_check`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
