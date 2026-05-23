# Hardware Description: aes

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `aes`
- `approved_label`: `pending:aes`
- `doc_anchor`: `aes`
- `module_name_prefix`: `aes`
- `bridge_edge_count`: 112

## Inferred Hardware Role

`aes` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 89, component: 41, testplan: 28, theory: 19, interface: 14
- Code categories: rtl: 188, dv: 131, other_code: 73, sva: 7
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Anchors

- `component:aes` (L1) - `__graphify_spec_only__/components.md`
- `aes.hjson` (L1) - `opentitan/hw/ip/aes/data/aes.hjson`
- `human name` (L8) - `opentitan/hw/ip/aes/data/aes.hjson`
- `one line desc` (L9) - `opentitan/hw/ip/aes/data/aes.hjson`
- `one paragraph desc` (L10) - `opentitan/hw/ip/aes/data/aes.hjson`
- `cip id` (L20) - `opentitan/hw/ip/aes/data/aes.hjson`
- `design spec` (L21) - `opentitan/hw/ip/aes/data/aes.hjson`
- `dv doc` (L22) - `opentitan/hw/ip/aes/data/aes.hjson`
- `hw checklist` (L23) - `opentitan/hw/ip/aes/data/aes.hjson`
- `sw checklist` (L24) - `opentitan/hw/ip/aes/data/aes.hjson`
- `version` (L25) - `opentitan/hw/ip/aes/data/aes.hjson`
- `life stage` (L26) - `opentitan/hw/ip/aes/data/aes.hjson`
- `aes_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/aes/data/aes_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/aes/data/aes_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/aes/data/aes_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/aes/data/aes_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/aes/data/aes_sec_cm_testplan.hjson`
- `aes_testplan.hjson` (L1) - `opentitan/hw/ip/aes/data/aes_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/aes/data/aes_testplan.hjson`
- `testpoints` (L12) - `opentitan/hw/ip/aes/data/aes_testplan.hjson`
- `desc` (L22) - `opentitan/hw/ip/aes/data/aes_testplan.hjson`
- `stage` (L24) - `opentitan/hw/ip/aes/data/aes_testplan.hjson`
- `tests` (L25) - `opentitan/hw/ip/aes/data/aes_testplan.hjson`
- `covergroups` (L174) - `opentitan/hw/ip/aes/data/aes_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/aes/doc/checklist.md`
- `AES Checklist` (L1) - `opentitan/hw/ip/aes/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/aes/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/aes/doc/checklist.md`
- `D2` (L32) - `opentitan/hw/ip/aes/doc/checklist.md`
- `D2S` (L74) - `opentitan/hw/ip/aes/doc/checklist.md`
- `D3` (L94) - `opentitan/hw/ip/aes/doc/checklist.md`
- `Verification Checklist` (L120) - `opentitan/hw/ip/aes/doc/checklist.md`
- `V1` (L122) - `opentitan/hw/ip/aes/doc/checklist.md`
- `V2` (L172) - `opentitan/hw/ip/aes/doc/checklist.md`
- `V2S` (L218) - `opentitan/hw/ip/aes/doc/checklist.md`

## Code Evidence

- `aes_model_dpi.c` (L1) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
- `c_dpi_aes_crypt_block()` (L16) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
- `c_dpi_aes_crypt_message()` (L123) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
- `c_dpi_aes_sub_bytes()` (L259) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
- `c_dpi_aes_shift_rows()` (L277) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
- `c_dpi_aes_mix_columns()` (L295) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
- `c_dpi_aes_key_expand()` (L313) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
- `aes_data_get()` (L352) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
- `aes_data_put()` (L371) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
- `aes_data_unpacked_get()` (L389) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
- `aes_data_unpacked_put()` (L408) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
- `aes_key_get()` (L428) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
- `aes_key_put()` (L448) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.c`
- `aes_model_dpi.h` (L1) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi.h`
- `aes_model_dpi_pkg.sv` (L1) - `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi_pkg.sv`
- `aes_pkg` (L8) - `opentitan\hw\ip\aes\rtl\aes_wrap.sv`
- `aes_cov_bind.sv` (L1) - `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv`
- `aes_cov_bind` (L6) - `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv`
- `aes_cov_if.sv` (L1) - `opentitan\hw\ip\aes\dv\cov\aes_cov_if.sv`
- `aes_err_injection_bind.sv` (L1) - `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv`
- `aes_err_injection_bind` (L4) - `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv`
- `fi_cipher_fsm_wrapper.sv` (L1) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_cipher_fsm_wrapper.sv`
- `fi_cipher_fsm_wrapper` (L9) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_cipher_fsm_wrapper.sv`
- `aes_env_pkg` (L9) - `opentitan\hw\ip\aes\dv\tests\aes_test_pkg.sv`
- `fi_cipher_if.sv` (L1) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_cipher_if.sv`
- `fi_control_fsm_wrapper.sv` (L1) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_control_fsm_wrapper.sv`
- `fi_control_fsm_wrapper` (L9) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_control_fsm_wrapper.sv`
- `fi_control_if.sv` (L1) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_control_if.sv`
- `fi_core_if.sv` (L1) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_core_if.sv`
- `fi_core_wrapper.sv` (L1) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_core_wrapper.sv`
- `fi_core_wrapper` (L9) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_core_wrapper.sv`
- `fi_ctr_fsm_if.sv` (L1) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_ctr_fsm_if.sv`
- `fi_ctr_fsm_wrapper.sv` (L1) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_ctr_fsm_wrapper.sv`
- `fi_ctr_fsm_wrapper` (L9) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_ctr_fsm_wrapper.sv`
- `fi_ghash_if.sv` (L1) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_ghash_if.sv`
- `fi_ghash_wrapper.sv` (L1) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_ghash_wrapper.sv`
- `fi_ghash_wrapper` (L9) - `opentitan\hw\ip\aes\dv\err_injection_if\fi_ghash_wrapper.sv`
- `force_if.sv` (L1) - `opentitan\hw\ip\aes\dv\err_injection_if\force_if.sv`
- `signal_force.sv` (L1) - `opentitan\hw\ip\aes\dv\err_injection_if\signal_force.sv`
- `signal_force` (L9) - `opentitan\hw\ip\aes\dv\err_injection_if\signal_force.sv`
- `force_if` (L20) - `opentitan\hw\ip\aes\dv\err_injection_if\signal_force.sv`
- `aes_bind.sv` (L1) - `opentitan\hw\ip\aes\dv\sva\aes_bind.sv`
- `aes_bind` (L5) - `opentitan\hw\ip\aes\dv\sva\aes_bind.sv`
- `aes_idle_check.sv` (L1) - `opentitan\hw\ip\aes\dv\sva\aes_idle_check.sv`
- `aes_idle_check` (L7) - `opentitan\hw\ip\aes\dv\sva\aes_idle_check.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:aes` | `aes_cipher_core_tb.sv` | `opentitan\hw\ip\aes\pre_dv\aes_cipher_core_tb\rtl\aes_cipher_core_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_cipher_core_tb` | `opentitan\hw\ip\aes\pre_dv\aes_cipher_core_tb\rtl\aes_cipher_core_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_masked_wrapper.sv` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_lec\aes_sbox_masked_wrapper.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_masked_wrapper` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_lec\aes_sbox_masked_wrapper.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_masked` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_lec\aes_sbox_masked_wrapper.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_err_injection_bind.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_err_injection_bind` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_canright_masked_noreuse.sv` | `opentitan\hw\ip\aes\rtl\aes_sbox_canright_masked_noreuse.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_masked_inverse_gf2p4_noreuse` | `opentitan\hw\ip\aes\rtl\aes_sbox_canright_masked_noreuse.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_masked_inverse_gf2p8_noreuse` | `opentitan\hw\ip\aes\rtl\aes_sbox_canright_masked_noreuse.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_masked_inverse_gf2p4_noreuse` | `opentitan\hw\ip\aes\rtl\aes_sbox_canright_masked_noreuse.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_canright_masked_noreuse` | `opentitan\hw\ip\aes\rtl\aes_sbox_canright_masked_noreuse.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_masked_inverse_gf2p8_noreuse` | `opentitan\hw\ip\aes\rtl\aes_sbox_canright_masked_noreuse.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_manual_config_err_test.sv` | `opentitan\hw\ip\aes\dv\tests\aes_manual_config_err_test.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_model_dpi_pkg.sv` | `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi_pkg.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_gcm_save_restore_test.sv` | `opentitan\hw\ip\aes\dv\tests\aes_gcm_save_restore_test.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_tb.sv` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_tb\rtl\aes_sbox_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_tb` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_tb\rtl\aes_sbox_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_lut` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_tb\rtl\aes_sbox_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_canright` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_tb\rtl\aes_sbox_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_canright_masked_noreuse` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_tb\rtl\aes_sbox_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_canright_masked` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_tb\rtl\aes_sbox_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_sbox_dom` | `opentitan\hw\ip\aes\pre_dv\aes_sbox_tb\rtl\aes_sbox_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_wrap_tb.sv` | `opentitan\hw\ip\aes\pre_dv\aes_wrap_tb\rtl\aes_wrap_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_wrap_tb` | `opentitan\hw\ip\aes\pre_dv\aes_wrap_tb\rtl\aes_wrap_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_wrap` | `opentitan\hw\ip\aes\pre_dv\aes_wrap_tb\rtl\aes_wrap_tb.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_config_error_test.sv` | `opentitan\hw\ip\aes\dv\tests\aes_config_error_test.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_tb_c_dpi.sv` | `opentitan\hw\ip\aes\pre_dv\aes_tb\rtl\aes_tb_c_dpi.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_tb_c_dpi` | `opentitan\hw\ip\aes\pre_dv\aes_tb\rtl\aes_tb_c_dpi.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_model_dpi_pkg` | `opentitan\hw\ip\aes\pre_dv\aes_tb\rtl\aes_tb_c_dpi.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_alert_reset_test.sv` | `opentitan\hw\ip\aes\dv\tests\aes_alert_reset_test.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_tb_pkg` | `opentitan\hw\ip\aes\pre_dv\aes_tb\rtl\aes_tb_reqs.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_tb_reqs.sv` | `opentitan\hw\ip\aes\pre_dv\aes_tb\rtl\aes_tb_reqs.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_tb_reqs` | `opentitan\hw\ip\aes\pre_dv\aes_tb\rtl\aes_tb_reqs.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_ctrl_gcm_reg_shadowed.sv` | `opentitan\hw\ip\aes\rtl\aes_ctrl_gcm_reg_shadowed.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_ctrl_gcm_reg_shadowed` | `opentitan\hw\ip\aes\rtl\aes_ctrl_gcm_reg_shadowed.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_masking_reseed_if.sv` | `opentitan\hw\ip\aes\dv\sva\aes_masking_reseed_if.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_tb_pkg.sv` | `opentitan\hw\ip\aes\pre_dv\aes_tb\rtl\aes_tb_pkg.sv` |
| `spec_component_matches_code` | `component:aes` | `aes_cipher_control_fsm_n.sv` | `opentitan\hw\ip\aes\rtl\aes_cipher_control_fsm_n.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `aes_model_dpi_pkg.sv` | `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `aes_pkg` | `opentitan\hw\ip\aes\rtl\aes_wrap.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `aes_cov_bind.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `aes_cov_bind` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `aes_cov_if.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_if.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `aes_err_injection_bind.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `aes_err_injection_bind` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_path_matches_code_path` | `aes.hjson` | `fi_cipher_fsm_wrapper.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\fi_cipher_fsm_wrapper.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `aes_model_dpi_pkg.sv` | `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `aes_pkg` | `opentitan\hw\ip\aes\rtl\aes_wrap.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `aes_cov_bind.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `aes_cov_bind` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `aes_cov_if.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_if.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `aes_err_injection_bind.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `aes_err_injection_bind` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_path_matches_code_path` | `aes_sec_cm_testplan.hjson` | `fi_cipher_fsm_wrapper.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\fi_cipher_fsm_wrapper.sv` |
| `spec_path_matches_code_path` | `aes_testplan.hjson` | `aes_model_dpi_pkg.sv` | `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `aes_testplan.hjson` | `aes_pkg` | `opentitan\hw\ip\aes\rtl\aes_wrap.sv` |
| `spec_path_matches_code_path` | `aes_testplan.hjson` | `aes_cov_bind.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `aes_testplan.hjson` | `aes_cov_bind` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `aes_testplan.hjson` | `aes_cov_if.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_if.sv` |
| `spec_path_matches_code_path` | `aes_testplan.hjson` | `aes_err_injection_bind.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_path_matches_code_path` | `aes_testplan.hjson` | `aes_err_injection_bind` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_path_matches_code_path` | `aes_testplan.hjson` | `fi_cipher_fsm_wrapper.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\fi_cipher_fsm_wrapper.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aes_model_dpi_pkg.sv` | `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aes_pkg` | `opentitan\hw\ip\aes\rtl\aes_wrap.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aes_cov_bind.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aes_cov_bind` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aes_cov_if.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aes_err_injection_bind.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aes_err_injection_bind` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `fi_cipher_fsm_wrapper.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\fi_cipher_fsm_wrapper.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aes_model_dpi_pkg.sv` | `opentitan\hw\ip\aes\dv\aes_model_dpi\aes_model_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aes_pkg` | `opentitan\hw\ip\aes\rtl\aes_wrap.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aes_cov_bind.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aes_cov_bind` | `opentitan\hw\ip\aes\dv\cov\aes_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aes_cov_if.sv` | `opentitan\hw\ip\aes\dv\cov\aes_cov_if.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aes_err_injection_bind.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aes_err_injection_bind` | `opentitan\hw\ip\aes\dv\err_injection_if\aes_err_injection_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `fi_cipher_fsm_wrapper.sv` | `opentitan\hw\ip\aes\dv\err_injection_if\fi_cipher_fsm_wrapper.sv` |

## Retrieval Guidance

- When a code-only query mentions `aes`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
