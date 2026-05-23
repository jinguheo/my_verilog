# Hardware Description: outgoing_alerts_englishbreakfast.hjson

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `outgoing_alerts_englishbreakfast.hjson`
- `approved_label`: `pending:outgoing_alerts_englishbreakfast.hjson`
- `doc_anchor`: `outgoing_alerts_englishbreakfast.hjson`
- `module_name_prefix`: `outgoing_alerts_englishbreakfast.hjson`
- `bridge_edge_count`: 16

## Inferred Hardware Role

`outgoing_alerts_englishbreakfast.hjson` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 22
- Code categories: rtl: 16
- Bridge relations: spec_path_matches_code_path: 16

## Spec Anchors

- `outgoing_alerts_englishbreakfast.hjson` (L1) - `opentitan/hw/top_englishbreakfast/data/autogen/outgoing_alerts_englishbreakfast.hjson`
- `englishbreakfast` (L8) - `opentitan/hw/top_englishbreakfast/data/autogen/outgoing_alerts_englishbreakfast.hjson`
- `module name` (L11) - `opentitan/hw/top_englishbreakfast/data/autogen/outgoing_alerts_englishbreakfast.hjson`
- `async` (L14) - `opentitan/hw/top_englishbreakfast/data/autogen/outgoing_alerts_englishbreakfast.hjson`
- `width` (L15) - `opentitan/hw/top_englishbreakfast/data/autogen/outgoing_alerts_englishbreakfast.hjson`
- `lpg idx` (L16) - `opentitan/hw/top_englishbreakfast/data/autogen/outgoing_alerts_englishbreakfast.hjson`

## Code Evidence

- `BUFG` (L92) - `opentitan\hw\top_englishbreakfast\rtl\clkgen_xil7series.sv`
- `prim_mubi_pkg` (L905) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `prim_esc_receiver` (L283) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`
- `prim_arbiter_fixed` (L58) - `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv`
- `prim_arbiter_tree` (L163) - `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv`
- `prim_count` (L240) - `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv`
- `prim_secded_hamming_72_64_enc` (L775) - `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv`
- `prim_secded_hamming_76_68_enc` (L334) - `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv`
- `top_racl_pkg` (L13) - `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv`
- `prim_ram_1p_adv` (L1487) - `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
- `prim_pad_wrapper_pkg` (L61) - `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv`
- `tlul_pkg` (L165) - `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
- `adc_ctrl` (L2047) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
- `aes` (L1174) - `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
- `aon_timer` (L1049) - `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv`
- `csrng` (L2617) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `BUFG` | `opentitan\hw\top_englishbreakfast\rtl\clkgen_xil7series.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `prim_mubi_pkg` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `prim_esc_receiver` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `prim_arbiter_fixed` | `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `prim_arbiter_tree` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `prim_count` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `prim_secded_hamming_72_64_enc` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `prim_secded_hamming_76_68_enc` | `opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `top_racl_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast_racl_pkg.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `prim_ram_1p_adv` | `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `prim_pad_wrapper_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\chip_englishbreakfast_cw305.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `tlul_pkg` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `aes` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `aon_timer` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_path_matches_code_path` | `outgoing_alerts_englishbreakfast.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |

## Retrieval Guidance

- When a code-only query mentions `outgoing_alerts_englishbreakfast.hjson`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
