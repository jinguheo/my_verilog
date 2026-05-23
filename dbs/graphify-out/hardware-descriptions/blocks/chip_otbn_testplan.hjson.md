# Hardware Description: chip_otbn_testplan.hjson

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `chip_otbn_testplan.hjson`
- `approved_label`: `pending:chip_otbn_testplan.hjson`
- `doc_anchor`: `chip_otbn_testplan.hjson`
- `module_name_prefix`: `chip_otbn_testplan.hjson`
- `bridge_edge_count`: 8

## Inferred Hardware Role

`chip_otbn_testplan.hjson` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: testplan: 17
- Code categories: rtl: 8
- Bridge relations: spec_path_matches_code_path: 8

## Spec Anchors

- `chip_otbn_testplan.hjson` (L1) - `opentitan/hw/top_earlgrey/data/ip/chip_otbn_testplan.hjson`
- `testpoints` (L6) - `opentitan/hw/top_earlgrey/data/ip/chip_otbn_testplan.hjson`
- `desc` (L9) - `opentitan/hw/top_earlgrey/data/ip/chip_otbn_testplan.hjson`
- `stage` (L21) - `opentitan/hw/top_earlgrey/data/ip/chip_otbn_testplan.hjson`
- `si stage` (L22) - `opentitan/hw/top_earlgrey/data/ip/chip_otbn_testplan.hjson`
- `tests` (L23) - `opentitan/hw/top_earlgrey/data/ip/chip_otbn_testplan.hjson`
- `bazel` (L24) - `opentitan/hw/top_earlgrey/data/ip/chip_otbn_testplan.hjson`
- `lc states` (L25) - `opentitan/hw/top_earlgrey/data/ip/chip_otbn_testplan.hjson`
- `features` (L26) - `opentitan/hw/top_earlgrey/data/ip/chip_otbn_testplan.hjson`

## Code Evidence

- `prim_alert_sender` (L268) - `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
- `prim_alert_pkg` (L11) - `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
- `prim_esc_pkg` (L12) - `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
- `prim_secded_inv_72_64_enc` (L39) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv`
- `prim_sec_anchor_flop` (L275) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv`
- `prim_packer_fifo` (L233) - `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv`
- `adc_ctrl` (L2047) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
- `csrng` (L2617) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `chip_otbn_testplan.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `chip_otbn_testplan.hjson` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `chip_otbn_testplan.hjson` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `chip_otbn_testplan.hjson` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `chip_otbn_testplan.hjson` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `chip_otbn_testplan.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `chip_otbn_testplan.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `chip_otbn_testplan.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |

## Retrieval Guidance

- When a code-only query mentions `chip_otbn_testplan.hjson`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
