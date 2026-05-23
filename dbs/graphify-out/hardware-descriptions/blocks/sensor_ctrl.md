# Hardware Description: sensor_ctrl

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `sensor_ctrl`
- `approved_label`: `pending:sensor_ctrl`
- `doc_anchor`: `sensor_ctrl`
- `module_name_prefix`: `sensor_ctrl`
- `bridge_edge_count`: 113

## Inferred Hardware Role

`sensor_ctrl` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 99, interface: 22, theory: 20, component: 15, testplan: 2
- Code categories: rtl: 120, other_code: 3
- Bridge relations: spec_path_matches_code_path: 99, spec_component_matches_code: 14

## Spec Anchors

- `component:sensor_ctrl` (L1) - `__graphify_spec_only__/components.md`
- `sensor_ctrl.hjson` (L1) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `cip id` (L10) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `design spec` (L11) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `dv doc` (L12) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `hw checklist` (L13) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `sw checklist` (L14) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `revisions` (L15) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `version` (L17) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `life stage` (L18) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `design stage` (L19) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `verification stage` (L21) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/data/sensor_ctrl.hjson`
- `checklist.md` (L1) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `SENSOR CTRL Checklist` (L1) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `D2` (L32) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `D2S` (L74) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `D3` (L94) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `Verification Checklist` (L120) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/checklist.md`
- `interfaces.md` (L1) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`
- `Hardware Interfaces` (L1) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`
- `Peripheral Pins for Chip IO` (L11) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`
- `Inter-Module Signals` (L17) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`
- `Interrupts` (L29) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`
- `Security Alerts` (L36) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/interfaces.md`
- `programmers_guide.md` (L1) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/programmers_guide.md`
- `Programmer's Guide` (L1) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/programmers_guide.md`
- `Device Interface Functions DIFs` (L7) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/programmers_guide.md`
- `registers.md` (L1) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`
- `Registers` (L1) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`
- `Summary` (L4) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`
- `INTR STATE` (L38) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`
- `Fields` (L44) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`
- `INTR ENABLE` (L56) - `opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/registers.md`

## Code Evidence

- `prim_alert_sender` (L268) - `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
- `sensor_ctrl.sv` (L1) - `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
- `sensor_ctrl` (L9) - `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
- `sensor_ctrl_pkg` (L10) - `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
- `sensor_ctrl_reg_pkg` (L22) - `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv`
- `sensor_ctrl_reg_top` (L105) - `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
- `sensor_ctrl_pkg.sv` (L1) - `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_pkg.sv`
- `sensor_ctrl_reg_pkg.sv` (L1) - `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_pkg.sv`
- `sensor_ctrl_reg_top.sv` (L1) - `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv`
- `sensor_ctrl_reg_top` (L9) - `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv`
- `sensor_ctrl` (L2194) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
- `sensor_ctrl.c` (L1) - `opentitan\sw\device\silicon_creator\lib\drivers\sensor_ctrl.c`
- `sensor_ctrl_configure()` (L27) - `opentitan\sw\device\silicon_creator\lib\drivers\sensor_ctrl.c`
- `sensor_ctrl.h` (L1) - `opentitan\sw\device\silicon_creator\lib\drivers\sensor_ctrl.h`
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
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_reg_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_reg_top.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_reg_top` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_reg_top` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl.c` | `opentitan\sw\device\silicon_creator\lib\drivers\sensor_ctrl.c` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl_configure()` | `opentitan\sw\device\silicon_creator\lib\drivers\sensor_ctrl.c` |
| `spec_component_matches_code` | `component:sensor_ctrl` | `sensor_ctrl.h` | `opentitan\sw\device\silicon_creator\lib\drivers\sensor_ctrl.h` |
| `spec_path_matches_code_path` | `top_earlgrey.gen.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `top_earlgrey.secrets.testing.gen.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `chip_conn_testplan.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `chip_testplan.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `top_earlgrey.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `top_earlgrey_seed.testing.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `datasheet.md` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `README.md` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `memory_map.md` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `sensor_ctrl.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `sensor_ctrl` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `sensor_ctrl_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `sensor_ctrl_reg_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `sensor_ctrl_reg_top` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `sensor_ctrl_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_pkg.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `sensor_ctrl_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_pkg.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `sensor_ctrl.hjson` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sensor_ctrl.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sensor_ctrl` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sensor_ctrl_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sensor_ctrl_reg_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sensor_ctrl_reg_top` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sensor_ctrl_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sensor_ctrl_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sensor_ctrl.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sensor_ctrl` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sensor_ctrl_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sensor_ctrl_reg_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sensor_ctrl_reg_top` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sensor_ctrl_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sensor_ctrl_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `sensor_ctrl.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `sensor_ctrl` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `sensor_ctrl_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `sensor_ctrl_reg_pkg` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_top.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `sensor_ctrl_reg_top` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `sensor_ctrl_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_pkg.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `sensor_ctrl_reg_pkg.sv` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl_reg_pkg.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `programmers_guide.md` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |

## Retrieval Guidance

- When a code-only query mentions `sensor_ctrl`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
