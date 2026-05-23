# Hardware Description: ascon

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `ascon`
- `approved_label`: `pending:ascon`
- `doc_anchor`: `ascon`
- `module_name_prefix`: `ascon`
- `bridge_edge_count`: 92

## Inferred Hardware Role

`ascon` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 98, component: 29, theory: 19, interface: 11
- Code categories: rtl: 104, other_code: 8, dv: 4
- Bridge relations: spec_path_matches_code_path: 64, spec_component_matches_code: 28

## Spec Anchors

- `component:ascon` (L1) - `__graphify_spec_only__/components.md`
- `ascon.hjson` (L1) - `opentitan/hw/ip/ascon/data/ascon.hjson`
- `human name` (L8) - `opentitan/hw/ip/ascon/data/ascon.hjson`
- `one line desc` (L9) - `opentitan/hw/ip/ascon/data/ascon.hjson`
- `one paragraph desc` (L10) - `opentitan/hw/ip/ascon/data/ascon.hjson`
- `regwidth` (L17) - `opentitan/hw/ip/ascon/data/ascon.hjson`
- `cip id` (L18) - `opentitan/hw/ip/ascon/data/ascon.hjson`
- `design spec` (L19) - `opentitan/hw/ip/ascon/data/ascon.hjson`
- `hw checklist` (L20) - `opentitan/hw/ip/ascon/data/ascon.hjson`
- `version` (L21) - `opentitan/hw/ip/ascon/data/ascon.hjson`
- `life stage` (L22) - `opentitan/hw/ip/ascon/data/ascon.hjson`
- `design stage` (L23) - `opentitan/hw/ip/ascon/data/ascon.hjson`
- `background.md` (L1) - `opentitan/hw/ip/ascon/doc/background.md`
- `Background` (L1) - `opentitan/hw/ip/ascon/doc/background.md`
- `Duplex Sponge` (L8) - `opentitan/hw/ip/ascon/doc/background.md`
- `Ascon AEAD` (L30) - `opentitan/hw/ip/ascon/doc/background.md`
- `checklist.md` (L1) - `opentitan/hw/ip/ascon/doc/checklist.md`
- `Design Checklist` (L7) - `opentitan/hw/ip/ascon/doc/checklist.md`
- `D1` (L9) - `opentitan/hw/ip/ascon/doc/checklist.md`
- `D2` (L35) - `opentitan/hw/ip/ascon/doc/checklist.md`
- `D2S` (L77) - `opentitan/hw/ip/ascon/doc/checklist.md`
- `D3` (L97) - `opentitan/hw/ip/ascon/doc/checklist.md`
- `Verification Checklist` (L123) - `opentitan/hw/ip/ascon/doc/checklist.md`
- `V1` (L125) - `opentitan/hw/ip/ascon/doc/checklist.md`
- `V2` (L175) - `opentitan/hw/ip/ascon/doc/checklist.md`
- `V2S` (L221) - `opentitan/hw/ip/ascon/doc/checklist.md`
- `V3` (L237) - `opentitan/hw/ip/ascon/doc/checklist.md`
- `interfaces.md` (L1) - `opentitan/hw/ip/ascon/doc/interfaces.md`
- `Inter-Module Signals` (L10) - `opentitan/hw/ip/ascon/doc/interfaces.md`
- `Security Alerts` (L20) - `opentitan/hw/ip/ascon/doc/interfaces.md`
- `programmers_guide.md` (L1) - `opentitan/hw/ip/ascon/doc/programmers_guide.md`
- `Programmer’s Guide` (L1) - `opentitan/hw/ip/ascon/doc/programmers_guide.md`
- `Initializing the IP` (L3) - `opentitan/hw/ip/ascon/doc/programmers_guide.md`
- `Interrupt Configuration` (L12) - `opentitan/hw/ip/ascon/doc/programmers_guide.md`
- `Issuing Transactions` (L17) - `opentitan/hw/ip/ascon/doc/programmers_guide.md`

## Code Evidence

- `ascon_tb.cc` (L1) - `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc`
- `AsconSim` (L14) - `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc`
- `OnClock()` (L31) - `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc`
- `main()` (L37) - `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc`
- `ascon_sim.sv` (L1) - `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv`
- `ascon_sim` (L7) - `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv`
- `ascon_pkg` (L9) - `opentitan\hw\ip\ascon\rtl\ascon_core.sv`
- `ascon_reg_pkg` (L26) - `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv`
- `ascon_tl_ul_stim` (L56) - `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv`
- `ascon` (L145) - `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv`
- `ascon_tl_ul_stim.sv` (L1) - `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv`
- `ascon_tl_ul_stim` (L7) - `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv`
- `ascon_tl_ul_stim_pkg` (L11) - `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv`
- `ascon_tl_ul_stim_pkg.sv` (L1) - `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim_pkg.sv`
- `ascon.sv` (L1) - `opentitan\hw\ip\ascon\rtl\ascon.sv`
- `ascon` (L7) - `opentitan\hw\ip\ascon\rtl\ascon.sv`
- `ascon_reg_top` (L61) - `opentitan\hw\ip\ascon\rtl\ascon.sv`
- `ascon_core` (L74) - `opentitan\hw\ip\ascon\rtl\ascon.sv`
- `ascon_core.sv` (L1) - `opentitan\hw\ip\ascon\rtl\ascon_core.sv`
- `ascon_core` (L7) - `opentitan\hw\ip\ascon\rtl\ascon_core.sv`
- `ascon_pkg.sv` (L1) - `opentitan\hw\ip\ascon\rtl\ascon_pkg.sv`
- `ascon_reg_pkg.sv` (L1) - `opentitan\hw\ip\ascon\rtl\ascon_reg_pkg.sv`
- `ascon_reg_top.sv` (L1) - `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv`
- `ascon_reg_top` (L9) - `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv`
- `ascon.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\ascon.h`
- `ascon.h` (L1) - `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\ascon.h`
- `ascon.h` (L1) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\ascon.h`
- `ascon.h` (L1) - `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\ascon.h`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:ascon` | `ascon_tl_ul_stim_pkg.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim_pkg.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_tl_ul_stim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_tl_ul_stim_pkg` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_sim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_sim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_reg_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_reg_pkg.sv` | `opentitan\hw\ip\ascon\rtl\ascon_reg_pkg.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_reg_top.sv` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_reg_top` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_core.sv` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_core` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_pkg.sv` | `opentitan\hw\ip\ascon\rtl\ascon_pkg.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon.sv` | `opentitan\hw\ip\ascon\rtl\ascon.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon` | `opentitan\hw\ip\ascon\rtl\ascon.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_reg_top` | `opentitan\hw\ip\ascon\rtl\ascon.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon_core` | `opentitan\hw\ip\ascon\rtl\ascon.sv` |
| `spec_component_matches_code` | `component:ascon` | `ascon.h` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\ascon.h` |
| `spec_component_matches_code` | `component:ascon` | `ascon.h` | `ibex\vendor\lowrisc_ip\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\ascon.h` |
| `spec_component_matches_code` | `component:ascon` | `ascon.h` | `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128a\ascon.h` |
| `spec_component_matches_code` | `component:ascon` | `ascon.h` | `opentitan\hw\ip\prim\dv\prim_ascon\ascon_model_dpi\vendor\ascon_ascon-c\ascon128\ascon.h` |
| `spec_component_matches_code` | `component:ascon` | `ascon_tb.cc` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc` |
| `spec_component_matches_code` | `component:ascon` | `AsconSim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc` |
| `spec_component_matches_code` | `component:ascon` | `OnClock()` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc` |
| `spec_component_matches_code` | `component:ascon` | `main()` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\cpp\ascon_tb.cc` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon_sim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon_sim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon_reg_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon_tl_ul_stim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `ascon.hjson` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon_sim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon_sim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon_reg_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon_tl_ul_stim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `background.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon_sim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon_sim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon_reg_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon_tl_ul_stim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon_sim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon_sim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon_reg_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon_tl_ul_stim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `ascon_sim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `ascon_sim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `ascon_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `ascon_reg_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `ascon` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `ascon_tl_ul_stim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `registers.md` | `ascon_sim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `registers.md` | `ascon_sim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `registers.md` | `ascon_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_path_matches_code_path` | `registers.md` | `ascon_reg_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |
| `spec_path_matches_code_path` | `registers.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `registers.md` | `ascon` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `registers.md` | `ascon_tl_ul_stim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `registers.md` | `ascon_tl_ul_stim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_tl_ul_stim.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `ascon_sim.sv` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `ascon_sim` | `opentitan\hw\ip\ascon\pre_dv\ascon_tb\rtl\ascon_sim.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `ascon_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_core.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `ascon_reg_pkg` | `opentitan\hw\ip\ascon\rtl\ascon_reg_top.sv` |

## Retrieval Guidance

- When a code-only query mentions `ascon`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
