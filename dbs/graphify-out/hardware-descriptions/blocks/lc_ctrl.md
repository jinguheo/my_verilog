# Hardware Description: lc_ctrl

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `lc_ctrl`
- `approved_label`: `pending:lc_ctrl`
- `doc_anchor`: `lc_ctrl`
- `module_name_prefix`: `lc_ctrl`
- `bridge_edge_count`: 192

## Inferred Hardware Role

`lc_ctrl` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 181, component: 41, testplan: 34, interface: 21, theory: 19
- Code categories: dv: 136, rtl: 95, sva: 4
- Bridge relations: spec_path_matches_code_path: 152, spec_component_matches_code: 40

## Spec Anchors

- `component:lc_ctrl` (L1) - `__graphify_spec_only__/components.md`
- `lc_ctrl.hjson` (L1) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `human name` (L6) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `one line desc` (L7) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `cip id` (L13) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `design spec` (L14) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `dv doc` (L15) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `hw checklist` (L16) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `sw checklist` (L17) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `version` (L18) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `life stage` (L19) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson`
- `lc_ctrl_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `stage` (L32) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `tests` (L33) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `TRANSITION.CONFIG.REGWEN` (L38) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `MANUF.STATE.SPARSE` (L51) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `TRANSITION.CTR.SPARSE` (L61) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `MANUF.STATE.BKGN CHK` (L71) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `TRANSITION.CTR.BKGN CHK` (L81) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `STATE.CONFIG.SPARSE` (L91) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson`
- `lc_ctrl_state.hjson` (L1) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `secded` (L12) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `data width` (L13) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `ecc width` (L14) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `ecc matrix` (L15) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `min hw` (L28) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `max hw` (L29) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `min hd` (L30) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `token size` (L33) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `tokens` (L34) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `lc state` (L47) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson`
- `lc_ctrl_testplan.hjson` (L1) - `opentitan/hw/ip/lc_ctrl/data/lc_ctrl_testplan.hjson`

## Code Evidence

- `lc_ctrl_state_pkg` (L10) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\lc_ctrl\dv\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\lc_ctrl\dv\tb.sv`
- `lc_ctrl_reg_pkg` (L22) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv`
- `lc_ctrl_env_pkg` (L10) - `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv`
- `lc_ctrl_test_pkg` (L13) - `opentitan\hw\ip\lc_ctrl\dv\tb.sv`
- `jtag_riscv_agent_pkg` (L15) - `opentitan\hw\ip\lc_ctrl\dv\tb.sv`
- `lc_ctrl_dv_utils_pkg` (L16) - `opentitan\hw\ip\lc_ctrl\dv\tb.sv`
- `lc_ctrl_if` (L64) - `opentitan\hw\ip\lc_ctrl\dv\tb.sv`
- `lc_ctrl_cov_bind.sv` (L1) - `opentitan\hw\ip\lc_ctrl\dv\cov\lc_ctrl_cov_bind.sv`
- `lc_ctrl_cov_bind` (L6) - `opentitan\hw\ip\lc_ctrl\dv\cov\lc_ctrl_cov_bind.sv`
- `lc_ctrl_fsm_cov_if.sv` (L1) - `opentitan\hw\ip\lc_ctrl\dv\cov\lc_ctrl_fsm_cov_if.sv`
- `lc_tx_cov_array_if.sv` (L1) - `opentitan\hw\ip\lc_ctrl\dv\cov\lc_tx_cov_array_if.sv`
- `lc_ctrl_bind.sv` (L1) - `opentitan\hw\ip\lc_ctrl\dv\sva\lc_ctrl_bind.sv`
- `lc_ctrl_bind` (L5) - `opentitan\hw\ip\lc_ctrl\dv\sva\lc_ctrl_bind.sv`
- `lc_ctrl_base_test.sv` (L1) - `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_base_test.sv`
- `lc_ctrl_test_pkg.sv` (L1) - `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv`
- `lc_ctrl.sv` (L1) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv`
- `lc_ctrl` (L10) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv`
- `lc_ctrl_regs_reg_top` (L153) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv`
- `lc_ctrl_kmac_if` (L748) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv`
- `lc_ctrl_fsm` (L770) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv`
- `lc_ctrl_dmi_reg_top.sv` (L1) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_dmi_reg_top.sv`
- `lc_ctrl_dmi_reg_top` (L9) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_dmi_reg_top.sv`
- `lc_ctrl_fsm.sv` (L1) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv`
- `lc_ctrl_fsm` (L9) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv`
- `lc_ctrl_token_pkg` (L113) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv`
- `lc_ctrl_state_decode` (L764) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv`
- `lc_ctrl_state_transition` (L777) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv`
- `lc_ctrl_signal_decode` (L794) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv`
- `lc_ctrl_kmac_if.sv` (L1) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_kmac_if.sv`
- `lc_ctrl_kmac_if` (L10) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_kmac_if.sv`
- `lc_ctrl_pkg.sv` (L1) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_pkg.sv`
- `lc_ctrl_regs_reg_top.sv` (L1) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv`
- `lc_ctrl_regs_reg_top` (L9) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv`
- `lc_ctrl_reg_pkg.sv` (L1) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_reg_pkg.sv`
- `lc_ctrl_signal_decode.sv` (L1) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_signal_decode.sv`
- `lc_ctrl_signal_decode` (L9) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_signal_decode.sv`
- `lc_ctrl_state_decode.sv` (L1) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_decode.sv`
- `lc_ctrl_state_decode` (L7) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_decode.sv`
- `lc_ctrl_state_pkg.sv` (L1) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_pkg.sv`
- `lc_ctrl_state_transition.sv` (L1) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv`
- `lc_ctrl_state_transition` (L8) - `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv`
- `lc_ctrl` (L1597) - `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_transition.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_transition` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_base_test.sv` | `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_env_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_fsm_cov_if.sv` | `opentitan\hw\ip\lc_ctrl\dv\cov\lc_ctrl_fsm_cov_if.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_test_pkg.sv` | `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_signal_decode.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_signal_decode.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_signal_decode` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_signal_decode.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_reg_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_regs_reg_top.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_regs_reg_top` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_decode.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_decode.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_decode` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_decode.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_cov_bind.sv` | `opentitan\hw\ip\lc_ctrl\dv\cov\lc_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_cov_bind` | `opentitan\hw\ip\lc_ctrl\dv\cov\lc_ctrl_cov_bind.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_dmi_reg_top.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_dmi_reg_top.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_dmi_reg_top` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_dmi_reg_top.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_pkg.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_pkg.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_bind.sv` | `opentitan\hw\ip\lc_ctrl\dv\sva\lc_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_bind` | `opentitan\hw\ip\lc_ctrl\dv\sva\lc_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_kmac_if.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_kmac_if.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_kmac_if` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_kmac_if.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_reg_pkg.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_fsm.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_fsm` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_token_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_decode` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_state_transition` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_signal_decode` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_fsm.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_pkg.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_pkg.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl.sv` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_regs_reg_top` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_kmac_if` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_fsm` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_test_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_dv_utils_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:lc_ctrl` | `lc_ctrl_if` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `lc_ctrl_state_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `tb.sv` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `tb` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `lc_ctrl_reg_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `lc_ctrl_env_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `lc_ctrl_test_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `jtag_riscv_agent_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl.hjson` | `lc_ctrl_dv_utils_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `lc_ctrl_state_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `lc_ctrl_reg_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `lc_ctrl_env_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `lc_ctrl_test_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `jtag_riscv_agent_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_sec_cm_testplan.hjson` | `lc_ctrl_dv_utils_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_state.hjson` | `lc_ctrl_state_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_state.hjson` | `tb.sv` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_state.hjson` | `tb` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_state.hjson` | `lc_ctrl_reg_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_state.hjson` | `lc_ctrl_env_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_state.hjson` | `lc_ctrl_test_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_state.hjson` | `jtag_riscv_agent_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_state.hjson` | `lc_ctrl_dv_utils_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_testplan.hjson` | `lc_ctrl_state_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_testplan.hjson` | `tb` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_testplan.hjson` | `lc_ctrl_reg_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_testplan.hjson` | `lc_ctrl_env_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_testplan.hjson` | `lc_ctrl_test_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_testplan.hjson` | `jtag_riscv_agent_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `lc_ctrl_testplan.hjson` | `lc_ctrl_dv_utils_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `lc_ctrl_state_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_state_transition.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `lc_ctrl_reg_pkg` | `opentitan\hw\ip\lc_ctrl\rtl\lc_ctrl_regs_reg_top.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `lc_ctrl_env_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tests\lc_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `lc_ctrl_test_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `jtag_riscv_agent_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `lc_ctrl_dv_utils_pkg` | `opentitan\hw\ip\lc_ctrl\dv\tb.sv` |

## Retrieval Guidance

- When a code-only query mentions `lc_ctrl`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
