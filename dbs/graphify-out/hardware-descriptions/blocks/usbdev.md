# Hardware Description: usbdev

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `usbdev`
- `approved_label`: `pending:usbdev`
- `doc_anchor`: `usbdev`
- `module_name_prefix`: `usbdev`
- `bridge_edge_count`: 120

## Inferred Hardware Role

`usbdev` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 105, component: 41, testplan: 29, theory: 19, interface: 16
- Code categories: rtl: 76, dv: 75, sva: 24
- Bridge relations: spec_path_matches_code_path: 80, spec_component_matches_code: 40

## Spec Anchors

- `component:usbdev` (L1) - `__graphify_spec_only__/components.md`
- `usbdev.hjson` (L1) - `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `human name` (L6) - `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `one line desc` (L7) - `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `cip id` (L16) - `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `design spec` (L17) - `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `dv doc` (L18) - `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `hw checklist` (L19) - `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `sw checklist` (L20) - `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `version` (L21) - `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `life stage` (L22) - `opentitan/hw/ip/usbdev/data/usbdev.hjson`
- `usbdev_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/usbdev/data/usbdev_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/usbdev/data/usbdev_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/usbdev/data/usbdev_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/usbdev/data/usbdev_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/usbdev/data/usbdev_sec_cm_testplan.hjson`
- `usbdev_testplan.hjson` (L1) - `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `import testplans` (L7) - `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `testpoints` (L13) - `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `desc` (L16) - `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `stage` (L43) - `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `tests` (L44) - `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `Background` (L1020) - `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `covergroups` (L1276) - `opentitan/hw/ip/usbdev/data/usbdev_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/usbdev/doc/checklist.md`
- `USB Device Checklist` (L1) - `opentitan/hw/ip/usbdev/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/usbdev/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/usbdev/doc/checklist.md`
- `D2` (L32) - `opentitan/hw/ip/usbdev/doc/checklist.md`
- `D2S` (L74) - `opentitan/hw/ip/usbdev/doc/checklist.md`
- `D3` (L94) - `opentitan/hw/ip/usbdev/doc/checklist.md`
- `Verification Checklist` (L120) - `opentitan/hw/ip/usbdev/doc/checklist.md`
- `V1` (L122) - `opentitan/hw/ip/usbdev/doc/checklist.md`
- `V2` (L172) - `opentitan/hw/ip/usbdev/doc/checklist.md`

## Code Evidence

- `usbdev_bind.sv` (L1) - `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv`
- `usbdev_bind` (L5) - `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\usbdev\dv\tb\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\usbdev\dv\tb\tb.sv`
- `usbdev_env_pkg` (L9) - `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv`
- `usbdev_test_pkg` (L10) - `opentitan\hw\ip\usbdev\dv\tb\tb.sv`
- `usb20_if` (L93) - `opentitan\hw\ip\usbdev\dv\tb\tb.sv`
- `usb20_block_if` (L98) - `opentitan\hw\ip\usbdev\dv\tb\tb.sv`
- `usb20_usbdpi` (L203) - `opentitan\hw\ip\usbdev\dv\tb\tb.sv`
- `usbdev_osc_tuning_if` (L278) - `opentitan\hw\ip\usbdev\dv\tb\tb.sv`
- `usbdev_base_test.sv` (L1) - `opentitan\hw\ip\usbdev\dv\tests\usbdev_base_test.sv`
- `usbdev_test_pkg.sv` (L1) - `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv`
- `usbdev.sv` (L1) - `opentitan\hw\ip\usbdev\rtl\usbdev.sv`
- `usbdev` (L9) - `opentitan\hw\ip\usbdev\rtl\usbdev.sv`
- `usbdev_pkg` (L10) - `opentitan\hw\ip\usbdev\rtl\usbdev_aon_wake.sv`
- `usbdev_reg_pkg` (L29) - `opentitan\hw\ip\usbdev\rtl\usbdev_reg_top.sv`
- `usbdev_usbif` (L583) - `opentitan\hw\ip\usbdev\rtl\usbdev.sv`
- `usbdev_reg_top` (L893) - `opentitan\hw\ip\usbdev\rtl\usbdev.sv`
- `usbdev_iomux` (L1193) - `opentitan\hw\ip\usbdev\rtl\usbdev.sv`
- `usbdev_counter` (L1333) - `opentitan\hw\ip\usbdev\rtl\usbdev.sv`
- `usbdev_aon_wake.sv` (L1) - `opentitan\hw\ip\usbdev\rtl\usbdev_aon_wake.sv`
- `usbdev_aon_wake` (L10) - `opentitan\hw\ip\usbdev\rtl\usbdev_aon_wake.sv`
- `usbdev_counter.sv` (L1) - `opentitan\hw\ip\usbdev\rtl\usbdev_counter.sv`
- `usbdev_counter` (L16) - `opentitan\hw\ip\usbdev\rtl\usbdev_counter.sv`
- `usbdev_iomux.sv` (L1) - `opentitan\hw\ip\usbdev\rtl\usbdev_iomux.sv`
- `usbdev_iomux` (L10) - `opentitan\hw\ip\usbdev\rtl\usbdev_iomux.sv`
- `usbdev_linkstate.sv` (L1) - `opentitan\hw\ip\usbdev\rtl\usbdev_linkstate.sv`
- `usbdev_linkstate` (L10) - `opentitan\hw\ip\usbdev\rtl\usbdev_linkstate.sv`
- `usbdev_pkg.sv` (L1) - `opentitan\hw\ip\usbdev\rtl\usbdev_pkg.sv`
- `usbdev_reg_pkg.sv` (L1) - `opentitan\hw\ip\usbdev\rtl\usbdev_reg_pkg.sv`
- `usbdev_reg_top.sv` (L1) - `opentitan\hw\ip\usbdev\rtl\usbdev_reg_top.sv`
- `usbdev_reg_top` (L9) - `opentitan\hw\ip\usbdev\rtl\usbdev_reg_top.sv`
- `usbdev_usbif.sv` (L1) - `opentitan\hw\ip\usbdev\rtl\usbdev_usbif.sv`
- `usbdev_usbif` (L12) - `opentitan\hw\ip\usbdev\rtl\usbdev_usbif.sv`
- `usb_fs_nb_pe` (L311) - `opentitan\hw\ip\usbdev\rtl\usbdev_usbif.sv`
- `usbdev_linkstate` (L425) - `opentitan\hw\ip\usbdev\rtl\usbdev_usbif.sv`
- `usb_consts_pkg.sv` (L1) - `opentitan\hw\ip\usbdev\rtl\usb_consts_pkg.sv`
- `usb_fs_nb_in_pe.sv` (L1) - `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_in_pe.sv`
- `usb_fs_nb_in_pe` (L15) - `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_in_pe.sv`
- `usb_consts_pkg` (L62) - `opentitan\hw\ip\usbdev\rtl\usb_fs_rx.sv`
- `usb_fs_nb_out_pe.sv` (L1) - `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_out_pe.sv`
- `usb_fs_nb_out_pe` (L16) - `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_out_pe.sv`
- `usb_fs_nb_pe.sv` (L1) - `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_pe.sv`
- `usb_fs_nb_pe` (L19) - `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_pe.sv`
- `usb_fs_nb_in_pe` (L178) - `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_pe.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:usbdev` | `usbdev` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_base_test.sv` | `opentitan\hw\ip\usbdev\dv\tests\usbdev_base_test.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_env_pkg` | `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_test_pkg.sv` | `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_linkstate.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_linkstate.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_linkstate` | `opentitan\hw\ip\usbdev\rtl\usbdev_linkstate.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_pkg` | `opentitan\hw\ip\usbdev\rtl\usbdev_aon_wake.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_aon_wake.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_aon_wake.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_aon_wake` | `opentitan\hw\ip\usbdev\rtl\usbdev_aon_wake.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_bind.sv` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_bind` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_reg_pkg` | `opentitan\hw\ip\usbdev\rtl\usbdev_reg_top.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_counter.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_counter.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_counter` | `opentitan\hw\ip\usbdev\rtl\usbdev_counter.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_reg_pkg.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_reg_pkg.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_reg_top.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_reg_top.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_reg_top` | `opentitan\hw\ip\usbdev\rtl\usbdev_reg_top.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_iomux.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_iomux.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_iomux` | `opentitan\hw\ip\usbdev\rtl\usbdev_iomux.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_usbif.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_usbif.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_usbif` | `opentitan\hw\ip\usbdev\rtl\usbdev_usbif.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_linkstate` | `opentitan\hw\ip\usbdev\rtl\usbdev_usbif.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_pkg.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev_pkg.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev.sv` | `opentitan\hw\ip\usbdev\rtl\usbdev.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev` | `opentitan\hw\ip\usbdev\rtl\usbdev.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_usbif` | `opentitan\hw\ip\usbdev\rtl\usbdev.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_reg_top` | `opentitan\hw\ip\usbdev\rtl\usbdev.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_iomux` | `opentitan\hw\ip\usbdev\rtl\usbdev.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_counter` | `opentitan\hw\ip\usbdev\rtl\usbdev.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_test_pkg` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usbdev_osc_tuning_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_nb_out_pe.sv` | `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_out_pe.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_nb_out_pe` | `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_out_pe.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_nb_in_pe.sv` | `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_in_pe.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_nb_in_pe` | `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_in_pe.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_consts_pkg.sv` | `opentitan\hw\ip\usbdev\rtl\usb_consts_pkg.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_tx_mux.sv` | `opentitan\hw\ip\usbdev\rtl\usb_fs_tx_mux.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_tx_mux` | `opentitan\hw\ip\usbdev\rtl\usb_fs_tx_mux.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_nb_pe` | `opentitan\hw\ip\usbdev\rtl\usbdev_usbif.sv` |
| `spec_component_matches_code` | `component:usbdev` | `usb_fs_nb_pe.sv` | `opentitan\hw\ip\usbdev\rtl\usb_fs_nb_pe.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `usbdev_bind.sv` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `usbdev_bind` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `tb.sv` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `tb` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `usbdev_env_pkg` | `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `usbdev_test_pkg` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `usb20_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev.hjson` | `usb20_block_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `usbdev_bind.sv` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `usbdev_bind` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `usbdev_env_pkg` | `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `usbdev_test_pkg` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `usb20_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_sec_cm_testplan.hjson` | `usb20_block_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_testplan.hjson` | `usbdev_bind.sv` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `usbdev_testplan.hjson` | `usbdev_bind` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `usbdev_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_testplan.hjson` | `tb` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_testplan.hjson` | `usbdev_env_pkg` | `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv` |
| `spec_path_matches_code_path` | `usbdev_testplan.hjson` | `usbdev_test_pkg` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_testplan.hjson` | `usb20_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `usbdev_testplan.hjson` | `usb20_block_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `usbdev_bind.sv` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `usbdev_bind` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `usbdev_env_pkg` | `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `usbdev_test_pkg` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `usb20_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `usb20_block_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `usbdev_bind.sv` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `usbdev_bind` | `opentitan\hw\ip\usbdev\dv\sva\usbdev_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `usbdev_env_pkg` | `opentitan\hw\ip\usbdev\dv\tests\usbdev_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `usbdev_test_pkg` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `usb20_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `usb20_block_if` | `opentitan\hw\ip\usbdev\dv\tb\tb.sv` |

## Retrieval Guidance

- When a code-only query mentions `usbdev`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
