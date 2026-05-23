# Hardware Description: pinmux

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `pinmux`
- `approved_label`: `pending:pinmux`
- `doc_anchor`: `pinmux`
- `module_name_prefix`: `pinmux`
- `bridge_edge_count`: 664

## Inferred Hardware Role

`pinmux` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 613, testplan: 133, theory: 81, interface: 72, component: 41
- Code categories: rtl: 696, dv: 30, sva: 12
- Bridge relations: spec_path_matches_code_path: 624, spec_component_matches_code: 40

## Spec Anchors

- `component:pinmux` (L1) - `__graphify_spec_only__/components.md`
- `pinmux.hjson` (L1) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux.hjson`
- `human name` (L7) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux.hjson`
- `one line desc` (L8) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux.hjson`
- `one paragraph desc` (L9) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux.hjson`
- `cip id` (L15) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux.hjson`
- `design spec` (L16) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux.hjson`
- `dv doc` (L17) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux.hjson`
- `hw checklist` (L18) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux.hjson`
- `sw checklist` (L19) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux.hjson`
- `version` (L20) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux.hjson`
- `life stage` (L21) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux.hjson`
- `pinmux_fpv_testplan.hjson` (L1) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux_fpv_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux_fpv_testplan.hjson`
- `testpoints` (L7) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux_fpv_testplan.hjson`
- `desc` (L12) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux_fpv_testplan.hjson`
- `stage` (L14) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux_fpv_testplan.hjson`
- `tests` (L15) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux_fpv_testplan.hjson`
- `pinmux_sec_cm_testplan.hjson` (L1) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/pinmux_sec_cm_testplan.hjson`
- `top_darjeeling_pinmux.ipconfig.hjson` (L1) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/top_darjeeling_pinmux.ipconfig.hjson`
- `instance name` (L5) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/top_darjeeling_pinmux.ipconfig.hjson`
- `param values` (L6) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/top_darjeeling_pinmux.ipconfig.hjson`
- `n wkup detect` (L8) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/top_darjeeling_pinmux.ipconfig.hjson`
- `wkup cnt width` (L9) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/top_darjeeling_pinmux.ipconfig.hjson`
- `n mio pads` (L10) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/top_darjeeling_pinmux.ipconfig.hjson`
- `n mio periph in` (L11) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/top_darjeeling_pinmux.ipconfig.hjson`
- `n mio periph out` (L12) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/top_darjeeling_pinmux.ipconfig.hjson`
- `n dio pads` (L13) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/top_darjeeling_pinmux.ipconfig.hjson`
- `n dio periph in` (L14) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/top_darjeeling_pinmux.ipconfig.hjson`
- `n dio periph out` (L15) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/data/top_darjeeling_pinmux.ipconfig.hjson`
- `checklist.md` (L1) - `opentitan/hw/top_darjeeling/ip_autogen/pinmux/doc/checklist.md`

## Code Evidence

- `prim_reg_cdc` (L2975) - `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_reg_top.sv`
- `prim_lc_or_hardened` (L151) - `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv`
- `usbdev_aon_wake` (L394) - `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux.sv`
- `prim_filter` (L29) - `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_wkup.sv`
- `pinmux_pkg` (L6) - `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_wkup.sv`
- `pinmux_reg_pkg` (L7) - `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_wkup.sv`
- `pinmux_bind_fpv.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\fpv\tb\pinmux_bind_fpv.sv`
- `pinmux_bind_fpv` (L6) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\fpv\tb\pinmux_bind_fpv.sv`
- `pinmux_chip_tb.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\fpv\tb\pinmux_chip_tb.sv`
- `pinmux_chip_tb` (L8) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\fpv\tb\pinmux_chip_tb.sv`
- `pinmux_tb.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\fpv\tb\pinmux_tb.sv`
- `pinmux_tb` (L8) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\fpv\tb\pinmux_tb.sv`
- `pinmux_assert_fpv.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\fpv\vip\pinmux_assert_fpv.sv`
- `pinmux_assert_fpv` (L10) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\fpv\vip\pinmux_assert_fpv.sv`
- `pinmux.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux.sv`
- `pinmux` (L10) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux.sv`
- `pinmux_jtag_breakout.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_jtag_breakout.sv`
- `pinmux_jtag_breakout` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_jtag_breakout.sv`
- `pinmux_jtag_buf.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_jtag_buf.sv`
- `pinmux_jtag_buf` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_jtag_buf.sv`
- `pinmux_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_pkg.sv`
- `pinmux_reg_pkg.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_reg_pkg.sv`
- `pinmux_reg_top.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_reg_top.sv`
- `pinmux_reg_top` (L9) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_reg_top.sv`
- `pinmux_strap_sampling.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv`
- `pinmux_strap_sampling` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv`
- `pinmux_jtag_buf` (L366) - `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv`
- `pinmux_wkup.sv` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_wkup.sv`
- `pinmux_wkup` (L5) - `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_wkup.sv`
- `pinmux_bind_fpv.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\fpv\tb\pinmux_bind_fpv.sv`
- `pinmux_bind_fpv` (L6) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\fpv\tb\pinmux_bind_fpv.sv`
- `pinmux_chip_tb.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\fpv\tb\pinmux_chip_tb.sv`
- `pinmux_chip_tb` (L8) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\fpv\tb\pinmux_chip_tb.sv`
- `pinmux_tb.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\fpv\tb\pinmux_tb.sv`
- `pinmux_tb` (L8) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\fpv\tb\pinmux_tb.sv`
- `pinmux_assert_fpv.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\fpv\vip\pinmux_assert_fpv.sv`
- `pinmux_assert_fpv` (L10) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\fpv\vip\pinmux_assert_fpv.sv`
- `pinmux.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\rtl\pinmux.sv`
- `pinmux` (L10) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\rtl\pinmux.sv`
- `pinmux_strap_sampling` (L347) - `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux.sv`
- `pinmux_jtag_breakout.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\rtl\pinmux_jtag_breakout.sv`
- `pinmux_jtag_breakout` (L5) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\rtl\pinmux_jtag_breakout.sv`
- `pinmux_jtag_buf.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\rtl\pinmux_jtag_buf.sv`
- `pinmux_jtag_buf` (L5) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\rtl\pinmux_jtag_buf.sv`
- `pinmux_pkg.sv` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\pinmux\rtl\pinmux_pkg.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:pinmux` | `pinmux_jtag_buf` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_assert_fpv.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\fpv\vip\pinmux_assert_fpv.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_assert_fpv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\fpv\vip\pinmux_assert_fpv.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_strap_sampling.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_strap_sampling` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_jtag_breakout.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_jtag_breakout.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_jtag_breakout` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_jtag_breakout.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_bind_fpv.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\fpv\tb\pinmux_bind_fpv.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_bind_fpv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\fpv\tb\pinmux_bind_fpv.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_chip_tb.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\fpv\tb\pinmux_chip_tb.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_chip_tb` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\fpv\tb\pinmux_chip_tb.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_assert_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\pinmux\fpv\vip\pinmux_assert_fpv.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_assert_fpv` | `opentitan\hw\top_darjeeling\ip_autogen\pinmux\fpv\vip\pinmux_assert_fpv.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_strap_sampling.sv` | `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_strap_sampling` | `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_jtag_buf.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_jtag_buf.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_jtag_buf` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_jtag_buf.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_jtag_breakout.sv` | `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_jtag_breakout.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_jtag_breakout` | `opentitan\hw\top_darjeeling\ip_autogen\pinmux\rtl\pinmux_jtag_breakout.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_reg_pkg.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_reg_pkg.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_reg_top.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_reg_top.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_reg_top` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_reg_top.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_assert_fpv.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pinmux\fpv\vip\pinmux_assert_fpv.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_assert_fpv` | `opentitan\hw\top_earlgrey\ip_autogen\pinmux\fpv\vip\pinmux_assert_fpv.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_strap_sampling.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_strap_sampling` | `opentitan\hw\top_earlgrey\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_bind_fpv.sv` | `opentitan\hw\top_darjeeling\ip_autogen\pinmux\fpv\tb\pinmux_bind_fpv.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_bind_fpv` | `opentitan\hw\top_darjeeling\ip_autogen\pinmux\fpv\tb\pinmux_bind_fpv.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_jtag_breakout.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pinmux\rtl\pinmux_jtag_breakout.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_jtag_breakout` | `opentitan\hw\top_earlgrey\ip_autogen\pinmux\rtl\pinmux_jtag_breakout.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_tb.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\fpv\tb\pinmux_tb.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_tb` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\fpv\tb\pinmux_tb.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_wkup.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_reg_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_wkup.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_chip_tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\pinmux\fpv\tb\pinmux_chip_tb.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_chip_tb` | `opentitan\hw\top_darjeeling\ip_autogen\pinmux\fpv\tb\pinmux_chip_tb.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_wkup.sv` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_wkup.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_wkup` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_wkup.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_bind_fpv.sv` | `opentitan\hw\top_earlgrey\ip_autogen\pinmux\fpv\tb\pinmux_bind_fpv.sv` |
| `spec_component_matches_code` | `component:pinmux` | `pinmux_bind_fpv` | `opentitan\hw\top_earlgrey\ip_autogen\pinmux\fpv\tb\pinmux_bind_fpv.sv` |
| `spec_path_matches_code_path` | `pinmux.tpldesc.hjson` | `prim_reg_cdc` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_reg_top.sv` |
| `spec_path_matches_code_path` | `pinmux.tpldesc.hjson` | `prim_lc_or_hardened` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv` |
| `spec_path_matches_code_path` | `pinmux.tpldesc.hjson` | `usbdev_aon_wake` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux.sv` |
| `spec_path_matches_code_path` | `pinmux.tpldesc.hjson` | `prim_filter` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_wkup.sv` |
| `spec_path_matches_code_path` | `pinmux_fpv_testplan.hjson` | `prim_reg_cdc` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_reg_top.sv` |
| `spec_path_matches_code_path` | `pinmux_fpv_testplan.hjson` | `prim_lc_or_hardened` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv` |
| `spec_path_matches_code_path` | `pinmux_fpv_testplan.hjson` | `usbdev_aon_wake` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux.sv` |
| `spec_path_matches_code_path` | `pinmux_fpv_testplan.hjson` | `prim_filter` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_wkup.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_reg_cdc` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_reg_top.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_lc_or_hardened` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `usbdev_aon_wake` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_filter` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_wkup.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `prim_reg_cdc` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_reg_top.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `prim_lc_or_hardened` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `usbdev_aon_wake` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `prim_filter` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_wkup.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `prim_reg_cdc` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_reg_top.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `prim_lc_or_hardened` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_strap_sampling.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `usbdev_aon_wake` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `prim_filter` | `opentitan\hw\top_englishbreakfast\ip_autogen\pinmux\rtl\pinmux_wkup.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `pinmux_jtag_breakout.sv` | `opentitan\hw\ip_templates\pinmux\rtl\pinmux_jtag_breakout.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `pinmux_jtag_breakout` | `opentitan\hw\ip_templates\pinmux\rtl\pinmux_jtag_breakout.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `pinmux_jtag_buf.sv` | `opentitan\hw\ip_templates\pinmux\rtl\pinmux_jtag_buf.sv` |
| `spec_path_matches_code_path` | `pinmux.hjson` | `pinmux_jtag_buf` | `opentitan\hw\ip_templates\pinmux\rtl\pinmux_jtag_buf.sv` |
| `spec_path_matches_code_path` | `pinmux_fpv_testplan.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `pinmux_fpv_testplan.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `pinmux_fpv_testplan.hjson` | `tlul_cmd_intg_gen` | `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv` |
| `spec_path_matches_code_path` | `pinmux_fpv_testplan.hjson` | `dma` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `pinmux_fpv_testplan.hjson` | `keymgr_dpe` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `pinmux_fpv_testplan.hjson` | `tlul_jtag_dtm` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `pinmux_fpv_testplan.hjson` | `mbx` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_path_matches_code_path` | `pinmux_fpv_testplan.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |

## Retrieval Guidance

- When a code-only query mentions `pinmux`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
