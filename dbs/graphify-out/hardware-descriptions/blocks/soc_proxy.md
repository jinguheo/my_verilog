# Hardware Description: soc_proxy

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `soc_proxy`
- `approved_label`: `pending:soc_proxy`
- `doc_anchor`: `soc_proxy`
- `module_name_prefix`: `soc_proxy`
- `bridge_edge_count`: 43

## Inferred Hardware Role

`soc_proxy` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 36, component: 17, testplan: 2
- Code categories: rtl: 58
- Bridge relations: spec_path_matches_code_path: 27, spec_component_matches_code: 16

## Spec Anchors

- `component:soc_proxy` (L1) - `__graphify_spec_only__/components.md`
- `soc_proxy.hjson` (L1) - `opentitan/hw/top_darjeeling/ip/soc_proxy/data/soc_proxy.hjson`
- `human name` (L7) - `opentitan/hw/top_darjeeling/ip/soc_proxy/data/soc_proxy.hjson`
- `one line desc` (L8) - `opentitan/hw/top_darjeeling/ip/soc_proxy/data/soc_proxy.hjson`
- `cip id` (L9) - `opentitan/hw/top_darjeeling/ip/soc_proxy/data/soc_proxy.hjson`
- `design spec` (L10) - `opentitan/hw/top_darjeeling/ip/soc_proxy/data/soc_proxy.hjson`
- `dv doc` (L11) - `opentitan/hw/top_darjeeling/ip/soc_proxy/data/soc_proxy.hjson`
- `hw checklist` (L12) - `opentitan/hw/top_darjeeling/ip/soc_proxy/data/soc_proxy.hjson`
- `sw checklist` (L13) - `opentitan/hw/top_darjeeling/ip/soc_proxy/data/soc_proxy.hjson`
- `revisions` (L15) - `opentitan/hw/top_darjeeling/ip/soc_proxy/data/soc_proxy.hjson`
- `version` (L17) - `opentitan/hw/top_darjeeling/ip/soc_proxy/data/soc_proxy.hjson`
- `life stage` (L18) - `opentitan/hw/top_darjeeling/ip/soc_proxy/data/soc_proxy.hjson`
- `top_darjeeling.gen.hjson` (L1) - `opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.gen.hjson`
- `top_darjeeling.secrets.testing.gen.hjson` (L1) - `opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.secrets.testing.gen.hjson`
- `chip_cfg.hjson` (L1) - `opentitan/hw/top_darjeeling/data/chip_cfg.hjson`
- `chip_conn_testplan.hjson` (L1) - `opentitan/hw/top_darjeeling/data/chip_conn_testplan.hjson`
- `chip_testplan.hjson` (L1) - `opentitan/hw/top_darjeeling/data/chip_testplan.hjson`
- `all_rd_wr_mapping.hjson` (L1) - `opentitan/hw/top_darjeeling/data/racl/all_rd_wr_mapping.hjson`
- `racl.hjson` (L1) - `opentitan/hw/top_darjeeling/data/racl/racl.hjson`
- `soc_rot_mapping.hjson` (L1) - `opentitan/hw/top_darjeeling/data/racl/soc_rot_mapping.hjson`
- `top_darjeeling.hjson` (L1) - `opentitan/hw/top_darjeeling/data/top_darjeeling.hjson`
- `top_darjeeling_seed.testing.hjson` (L1) - `opentitan/hw/top_darjeeling/data/top_darjeeling_seed.testing.hjson`
- `datasheet.md` (L1) - `opentitan/hw/top_darjeeling/doc/datasheet.md`
- `memory_map.md` (L1) - `opentitan/hw/top_darjeeling/doc/memory_map.md`

## Code Evidence

- `tlul_cmd_intg_gen` (L46) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv`
- `bat.sv` (L1) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv`
- `bat` (L5) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv`
- `soc_proxy.sv` (L1) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy.sv`
- `soc_proxy` (L9) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy.sv`
- `soc_proxy_reg_pkg` (L20) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_ctn_reg_top.sv`
- `soc_proxy_pkg` (L11) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy.sv`
- `bat` (L103) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy.sv`
- `soc_proxy_core_reg_top` (L119) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy.sv`
- `soc_proxy_core_reg_top.sv` (L1) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_core_reg_top.sv`
- `soc_proxy_core_reg_top` (L9) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_core_reg_top.sv`
- `soc_proxy_ctn_reg_top.sv` (L1) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_ctn_reg_top.sv`
- `soc_proxy_ctn_reg_top` (L9) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_ctn_reg_top.sv`
- `soc_proxy_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_pkg.sv`
- `soc_proxy_reg_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_reg_pkg.sv`
- `soc_proxy` (L1600) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `prim_flop_en` (L269) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
- `prim_ram_1p_adv` (L1487) - `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
- `dma` (L2221) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `keymgr_dpe` (L1905) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `tlul_jtag_dtm` (L1340) - `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
- `mbx` (L2257) - `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
- `prim_onehot_enc` (L128) - `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:soc_proxy` | `soc_proxy_core_reg_top.sv` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_core_reg_top.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `soc_proxy_core_reg_top` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_core_reg_top.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `soc_proxy_reg_pkg` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_ctn_reg_top.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `soc_proxy_ctn_reg_top.sv` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_ctn_reg_top.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `soc_proxy_ctn_reg_top` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_ctn_reg_top.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `soc_proxy_reg_pkg.sv` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_reg_pkg.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `soc_proxy_pkg.sv` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_pkg.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `soc_proxy.sv` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `soc_proxy` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `soc_proxy_pkg` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `soc_proxy_core_reg_top` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `soc_proxy` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `bat` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `bat.sv` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_component_matches_code` | `component:soc_proxy` | `bat` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `top_darjeeling.gen.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `top_darjeeling.secrets.testing.gen.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `chip_cfg.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `chip_conn_testplan.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `chip_testplan.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `all_rd_wr_mapping.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `racl.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `soc_rot_mapping.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `top_darjeeling.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `top_darjeeling_seed.testing.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `datasheet.md` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `memory_map.md` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `bat.sv` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `bat` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `soc_proxy.sv` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `soc_proxy` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `soc_proxy_reg_pkg` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy_ctn_reg_top.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `soc_proxy_pkg` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy.sv` |
| `spec_path_matches_code_path` | `soc_proxy.hjson` | `bat` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\soc_proxy.sv` |

## Retrieval Guidance

- When a code-only query mentions `soc_proxy`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
