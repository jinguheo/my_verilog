# Hardware Description: rv_core_ibex

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `rv_core_ibex`
- `approved_label`: `pending:rv_core_ibex`
- `doc_anchor`: `rv_core_ibex`
- `module_name_prefix`: `rv_core_ibex`
- `bridge_edge_count`: 585

## Inferred Hardware Role

`rv_core_ibex` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 542, testplan: 123, theory: 101, interface: 64, component: 41
- Code categories: rtl: 587, sva: 52
- Bridge relations: spec_path_matches_code_path: 545, spec_component_matches_code: 40

## Spec Anchors

- `component:rv_core_ibex` (L1) - `__graphify_spec_only__/components.md`
- `rv_core_ibex.tpldesc.hjson` (L1) - `opentitan/hw/ip_templates/rv_core_ibex/data/rv_core_ibex.tpldesc.hjson`
- `template param list` (L5) - `opentitan/hw/ip_templates/rv_core_ibex/data/rv_core_ibex.tpldesc.hjson`
- `desc` (L8) - `opentitan/hw/ip_templates/rv_core_ibex/data/rv_core_ibex.tpldesc.hjson`
- `dtgen` (L17) - `opentitan/hw/ip_templates/rv_core_ibex/data/rv_core_ibex.tpldesc.hjson`
- `boot-rom-patching.md` (L1) - `opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md`
- `Boot, ROM execution and Patching` (L1) - `opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md`
- `Glossary` (L3) - `opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md`
- `Scope` (L11) - `opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md`
- `Overview` (L16) - `opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md`
- `Programming method` (L43) - `opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md`
- `ROM Boot & Patching Building Blocks` (L54) - `opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md`
- `OpenTitan base ROM first ROM partition` (L60) - `opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md`
- `Second ROM partition` (L79) - `opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md`
- `Efuse / OTP patch` (L112) - `opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md`
- `Patch SRAM` (L162) - `opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md`
- `checklist.md` (L1) - `opentitan/hw/ip_templates/rv_core_ibex/doc/checklist.md`
- `Ibex Processor Core Checklist` (L1) - `opentitan/hw/ip_templates/rv_core_ibex/doc/checklist.md`
- `Design Checklist` (L9) - `opentitan/hw/ip_templates/rv_core_ibex/doc/checklist.md`
- `D1` (L11) - `opentitan/hw/ip_templates/rv_core_ibex/doc/checklist.md`
- `D1 Exceptions` (L36) - `opentitan/hw/ip_templates/rv_core_ibex/doc/checklist.md`
- `D2` (L40) - `opentitan/hw/ip_templates/rv_core_ibex/doc/checklist.md`
- `D2S` (L82) - `opentitan/hw/ip_templates/rv_core_ibex/doc/checklist.md`
- `D3` (L102) - `opentitan/hw/ip_templates/rv_core_ibex/doc/checklist.md`
- `Verification Checklist` (L126) - `opentitan/hw/ip_templates/rv_core_ibex/doc/checklist.md`
- `V1` (L134) - `opentitan/hw/ip_templates/rv_core_ibex/doc/checklist.md`
- `V2` (L138) - `opentitan/hw/ip_templates/rv_core_ibex/doc/checklist.md`
- `programmers_guide.md` (L1) - `opentitan/hw/ip_templates/rv_core_ibex/doc/programmers_guide.md`
- `Programmer's Guide` (L1) - `opentitan/hw/ip_templates/rv_core_ibex/doc/programmers_guide.md`
- `Device Interface Functions DIFs` (L3) - `opentitan/hw/ip_templates/rv_core_ibex/doc/programmers_guide.md`
- `theory_of_operation.md` (L1) - `opentitan/hw/ip_templates/rv_core_ibex/doc/theory_of_operation.md`
- `Theory of Operation` (L1) - `opentitan/hw/ip_templates/rv_core_ibex/doc/theory_of_operation.md`
- `Simple Address Translation` (L3) - `opentitan/hw/ip_templates/rv_core_ibex/doc/theory_of_operation.md`
- `Translation and Instruction Caching` (L26) - `opentitan/hw/ip_templates/rv_core_ibex/doc/theory_of_operation.md`
- `Random Number Generation` (L34) - `opentitan/hw/ip_templates/rv_core_ibex/doc/theory_of_operation.md`

## Code Evidence

- `prim_mubi_pkg` (L905) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `prim_esc_receiver` (L283) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `prim_arbiter_fixed` (L58) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv`
- `prim_sync_reqack_data` (L376) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `prim_sec_anchor_buf` (L359) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `prim_lc_sync` (L325) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `prim_lc_sender` (L406) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `tlul_adapter_host` (L668) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `tlul_socket_1n` (L107) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv`
- `prim_edn_req` (L979) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `tlul_lc_gate` (L769) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `rv_core_ibex_pkg.sv` (L1) - `opentitan\hw\ip\rv_core_ibex\rtl\rv_core_ibex_pkg.sv`
- `tlul_err_resp` (L1400) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `tlul_fifo_sync` (L694) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `rv_core_ibex_bind.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\dv\sva\rv_core_ibex_bind.sv`
- `rv_core_ibex_bind` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\dv\sva\rv_core_ibex_bind.sv`
- `rv_core_ibex.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `rv_core_ibex` (L13) - `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `rv_core_ibex_pkg` (L11) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv`
- `rv_core_ibex_reg_pkg` (L27) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv`
- `rv_core_ibex_addr_trans` (L652) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `rv_core_ibex_cfg_reg_top` (L829) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `rv_core_ibex_addr_trans.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv`
- `rv_core_ibex_addr_trans` (L11) - `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv`
- `rv_core_ibex_cfg_reg_top.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv`
- `rv_core_ibex_cfg_reg_top` (L9) - `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv`
- `rv_core_ibex_peri.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv`
- `rv_core_ibex_peri` (L10) - `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv`
- `rv_core_ibex_peri_pkg` (L11) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv`
- `rv_core_ibex_peri_reg_pkg` (L12) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv`
- `rv_core_ibex_peri_reg_top` (L44) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv`
- `rv_core_ibex_reg_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_reg_pkg.sv`
- `rv_core_ibex_bind.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\dv\sva\rv_core_ibex_bind.sv`
- `rv_core_ibex_bind` (L5) - `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\dv\sva\rv_core_ibex_bind.sv`
- `rv_core_ibex.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `rv_core_ibex` (L13) - `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `rv_core_ibex_addr_trans.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv`
- `rv_core_ibex_addr_trans` (L11) - `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv`
- `rv_core_ibex_cfg_reg_top.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv`
- `rv_core_ibex_cfg_reg_top` (L9) - `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv`
- `rv_core_ibex_peri.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv`
- `rv_core_ibex_peri` (L10) - `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv`
- `rv_core_ibex_reg_pkg.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_reg_pkg.sv`
- `rv_core_ibex_bind.sv` (L1) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\dv\sva\rv_core_ibex_bind.sv`
- `rv_core_ibex_bind` (L5) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\dv\sva\rv_core_ibex_bind.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_reg_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_cfg_reg_top.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_cfg_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_addr_trans.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_addr_trans` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_bind.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\dv\sva\rv_core_ibex_bind.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_bind` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\dv\sva\rv_core_ibex_bind.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_reg_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_reg_pkg.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_cfg_reg_top.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_cfg_reg_top` | `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_addr_trans.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_addr_trans` | `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_peri_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_peri_reg_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_peri_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_peri.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_peri` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_cfg_reg_top.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_cfg_reg_top` | `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_cfg_reg_top.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_addr_trans.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_addr_trans` | `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\dv\sva\rv_core_ibex_bind.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_bind` | `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\dv\sva\rv_core_ibex_bind.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_reg_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_reg_pkg.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_addr_trans` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_cfg_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_bind.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\dv\sva\rv_core_ibex_bind.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_bind` | `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\dv\sva\rv_core_ibex_bind.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_reg_pkg.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_peri.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_peri` | `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_peri.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex_peri` | `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_peri.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex.sv` | `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex` | `opentitan\hw\top_darjeeling\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex.sv` | `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_component_matches_code` | `component:rv_core_ibex` | `rv_core_ibex` | `opentitan\hw\top_earlgrey\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `prim_mubi_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `prim_esc_receiver` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `prim_arbiter_fixed` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `prim_sync_reqack_data` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `prim_sec_anchor_buf` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `prim_lc_sync` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `prim_lc_sender` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `rv_core_ibex.tpldesc.hjson` | `tlul_adapter_host` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `testbench.v` | `RTLLM\Miscellaneous\RISC-V\ROM\testbench.v` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `rom_tb` | `RTLLM\Miscellaneous\RISC-V\ROM\testbench.v` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `ROM` | `RTLLM\Miscellaneous\RISC-V\ROM\testbench.v` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `verified_ROM.v` | `RTLLM\Miscellaneous\RISC-V\ROM\verified_ROM.v` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `ROM` | `RTLLM\Miscellaneous\RISC-V\ROM\verified_ROM.v` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `prim_mubi_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `prim_esc_receiver` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `boot-rom-patching.md` | `prim_arbiter_fixed` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |

## Retrieval Guidance

- When a code-only query mentions `rv_core_ibex`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
