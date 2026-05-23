# Hardware Description: ast

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `ast`
- `approved_label`: `pending:ast`
- `doc_anchor`: `ast`
- `module_name_prefix`: `ast`
- `bridge_edge_count`: 95

## Inferred Hardware Role

`ast` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 60, component: 41, interface: 21, testplan: 2
- Code categories: rtl: 235
- Bridge relations: spec_path_matches_code_path: 55, spec_component_matches_code: 40

## Spec Anchors

- `component:ast` (L1) - `__graphify_spec_only__/components.md`
- `ast.hjson` (L1) - `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `cip id` (L10) - `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `design spec` (L11) - `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `dv doc` (L12) - `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `hw checklist` (L13) - `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `sw checklist` (L14) - `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `version` (L15) - `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `life stage` (L16) - `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `design stage` (L17) - `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `verification stage` (L18) - `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `dif stage` (L19) - `opentitan/hw/top_darjeeling/ip/ast/data/ast.hjson`
- `ast.hjson` (L1) - `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `cip id` (L10) - `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `design spec` (L11) - `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `dv doc` (L12) - `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `hw checklist` (L13) - `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `sw checklist` (L14) - `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `version` (L15) - `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `life stage` (L16) - `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `design stage` (L17) - `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `verification stage` (L18) - `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `dif stage` (L19) - `opentitan/hw/top_earlgrey/ip/ast/data/ast.hjson`
- `interfaces.md` (L1) - `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`
- `Interface Signals` (L1) - `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`
- `Table notes` (L3) - `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`
- `Signal naming conventions used in this document` (L5) - `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`
- `Clock domains column` (L15) - `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`
- `Table` (L26) - `opentitan/hw/top_earlgrey/ip/ast/doc/interfaces.md`
- `top_earlgrey.gen.hjson` (L1) - `opentitan/hw/top_earlgrey/data/autogen/top_earlgrey.gen.hjson`
- `top_earlgrey.secrets.testing.gen.hjson` (L1) - `opentitan/hw/top_earlgrey/data/autogen/top_earlgrey.secrets.testing.gen.hjson`
- `chip_conn_testplan.hjson` (L1) - `opentitan/hw/top_earlgrey/data/chip_conn_testplan.hjson`
- `chip_testplan.hjson` (L1) - `opentitan/hw/top_earlgrey/data/chip_testplan.hjson`
- `top_earlgrey.hjson` (L1) - `opentitan/hw/top_earlgrey/data/top_earlgrey.hjson`
- `top_earlgrey_seed.testing.hjson` (L1) - `opentitan/hw/top_earlgrey/data/top_earlgrey_seed.testing.hjson`

## Code Evidence

- `prim_packer_fifo` (L233) - `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv`
- `aon_clk.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_clk.sv`
- `aon_clk` (L9) - `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_clk.sv`
- `aon_osc.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_osc.sv`
- `aon_osc` (L9) - `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_osc.sv`
- `ast.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast.sv`
- `ast` (L12) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast.sv`
- `ast_pkg` (L159) - `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv`
- `ast_reg_pkg` (L22) - `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_reg_top.sv`
- `ast_bhv_pkg` (L161) - `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv`
- `rglts_pdm_3p3v` (L309) - `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv`
- `rng` (L665) - `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv`
- `ast_alert` (L697) - `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv`
- `ast_reg_top` (L837) - `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv`
- `ast_dft` (L906) - `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv`
- `ast_alert.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_alert.sv`
- `ast_alert` (L9) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_alert.sv`
- `ast_bhv_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_bhv_pkg.sv`
- `ast_dft.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_dft.sv`
- `ast_dft` (L11) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_dft.sv`
- `ast_entropy.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_entropy.sv`
- `ast_entropy` (L9) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_entropy.sv`
- `dev_entropy` (L100) - `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_entropy.sv`
- `ast_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_pkg.sv`
- `ast_pulse_sync.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_pulse_sync.sv`
- `ast_pulse_sync` (L18) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_pulse_sync.sv`
- `ast_reg_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_reg_pkg.sv`
- `ast_reg_top.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_reg_top.sv`
- `ast_reg_top` (L9) - `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_reg_top.sv`
- `dev_entropy.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\dev_entropy.sv`
- `dev_entropy` (L9) - `opentitan\hw\top_darjeeling\ip\ast\rtl\dev_entropy.sv`
- `prim_multibit_sync` (L56) - `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv`
- `gfr_clk_mux2.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\gfr_clk_mux2.sv`
- `gfr_clk_mux2` (L10) - `opentitan\hw\top_darjeeling\ip\ast\rtl\gfr_clk_mux2.sv`
- `io_clk.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\io_clk.sv`
- `io_clk` (L9) - `opentitan\hw\top_darjeeling\ip\ast\rtl\io_clk.sv`
- `io_osc.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\io_osc.sv`
- `io_osc` (L9) - `opentitan\hw\top_darjeeling\ip\ast\rtl\io_osc.sv`
- `rglts_pdm_3p3v.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\rglts_pdm_3p3v.sv`
- `rglts_pdm_3p3v` (L11) - `opentitan\hw\top_darjeeling\ip\ast\rtl\rglts_pdm_3p3v.sv`
- `rng.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\rng.sv`
- `rng` (L12) - `opentitan\hw\top_darjeeling\ip\ast\rtl\rng.sv`
- `ast_pulse_sync` (L63) - `opentitan\hw\top_earlgrey\ip\ast\rtl\usb_clk.sv`
- `sys_clk.sv` (L1) - `opentitan\hw\top_darjeeling\ip\ast\rtl\sys_clk.sv`
- `sys_clk` (L9) - `opentitan\hw\top_darjeeling\ip\ast\rtl\sys_clk.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:ast` | `ast` | `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pulse_sync.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_pulse_sync.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_clks_byp.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_clks_byp.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_pkg` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_reg_top.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_bhv_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_bhv_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_entropy.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_entropy.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_reg_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_top.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_reg_top.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_top` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_reg_top.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_alert.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_alert.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pulse_sync.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_pulse_sync.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pulse_sync` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_pulse_sync.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_dft.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_dft.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pulse_sync.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_pulse_sync.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pulse_sync` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_pulse_sync.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_bhv_pkg.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_bhv_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_entropy.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_entropy.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_entropy` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_entropy.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_pkg.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_reg_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_top.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_reg_top.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_top` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_reg_top.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_clks_byp.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_clks_byp.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_clks_byp` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_clks_byp.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_alert.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_alert.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_alert` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_alert.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_bhv_pkg.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_bhv_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_entropy.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_entropy.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_entropy` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_entropy.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_reg_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_top.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_reg_top.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_reg_top` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_reg_top.sv` |
| `spec_component_matches_code` | `component:ast` | `ast.sv` | `opentitan\hw\top_englishbreakfast\ip\ast\rtl\ast.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_dft.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_dft.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_dft` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_dft.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pkg.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast_pkg.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_alert.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_alert.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_alert` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_alert.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_pulse_sync` | `opentitan\hw\top_earlgrey\ip\ast\rtl\usb_clk.sv` |
| `spec_component_matches_code` | `component:ast` | `ast_dft.sv` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast_dft.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `aon_clk.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_clk.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `aon_clk` | `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_clk.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `aon_osc.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_osc.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `aon_osc` | `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_osc.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `ast.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `ast` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `ast_pkg` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv` |
| `spec_path_matches_code_path` | `top_earlgrey.gen.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `top_earlgrey.secrets.testing.gen.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `chip_conn_testplan.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `chip_testplan.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `top_earlgrey.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `top_earlgrey_seed.testing.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `datasheet.md` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `memory_map.md` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `aon_clk.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_clk.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `aon_clk` | `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_clk.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `aon_osc.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_osc.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `aon_osc` | `opentitan\hw\top_darjeeling\ip\ast\rtl\aon_osc.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `ast.sv` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `ast` | `opentitan\hw\top_darjeeling\ip\ast\rtl\ast.sv` |
| `spec_path_matches_code_path` | `ast.hjson` | `ast_pkg` | `opentitan\hw\top_earlgrey\ip\ast\rtl\ast.sv` |

## Retrieval Guidance

- When a code-only query mentions `ast`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
