# Hardware Description: rom

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `rom`
- `approved_label`: `pending:rom`
- `doc_anchor`: `rom`
- `module_name_prefix`: `rom`
- `bridge_edge_count`: 40

## Inferred Hardware Role

`rom` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 41
- Code categories: other_code: 35, rtl: 5
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:rom` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `verified_ROM.v` (L1) - `RTLLM\Miscellaneous\RISC-V\ROM\verified_ROM.v`
- `ROM` (L1) - `RTLLM\Miscellaneous\RISC-V\ROM\verified_ROM.v`
- `rom_tb` (L1) - `RTLLM\Miscellaneous\RISC-V\ROM\testbench.v`
- `ROM` (L6) - `RTLLM\Miscellaneous\RISC-V\ROM\testbench.v`
- `testbench.v` (L1) - `RTLLM\Miscellaneous\RISC-V\ROM\testbench.v`
- `immutable_rom_ext_section_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\immutable_rom_ext_section\immutable_rom_ext_section_test.c`
- `rom_ext_non_mutable()` (L32) - `opentitan\sw\device\silicon_creator\rom\e2e\immutable_rom_ext_section\immutable_rom_ext_section_test.c`
- `rom_ext_upgrade_interrupt.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\rom_ext_upgrade_interrupt\rom_ext_upgrade_interrupt.c`
- `rom_e2e_shutdown_alert_config_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\shutdown_alert\rom_e2e_shutdown_alert_config_test.c`
- `corrupt_rom_ext_word()` (L230) - `opentitan\sw\device\silicon_creator\rom\e2e\boot_policy_flash_ecc_error\flash_ecc_error_test.c`
- `rom_e2e_alert_config_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\shutdown_alert\rom_e2e_alert_config_test.c`
- `rom_e2e_ret_ram_init_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\retention_ram\rom_e2e_ret_ram_init_test.c`
- `rom_e2e_ret_ram_keep_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\retention_ram\rom_e2e_ret_ram_keep_test.c`
- `rom_e2e_bootstrap_rma_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\bootstrap\rom_e2e_bootstrap_rma_test.c`
- `rom_e2e_shutdown_exception_c_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\rom_e2e_shutdown_exception_c_test.c`
- `rom_e2e_keymgr_init_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\keymgr\rom_e2e_keymgr_init_test.c`
- `rom_e2e_self_hash_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\release\rom_e2e_self_hash_test.c`
- `hash_rom()` (L58) - `opentitan\sw\device\silicon_creator\rom\e2e\release\rom_e2e_self_hash_test.c`
- `rom_e2e_flash_ctrl_init_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\rom_e2e_flash_ctrl_init_test.c`
- `rom_e2e_static_critical_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\rom_e2e_static_critical_test.c`
- `rom_ext_upgrade_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\rom_ext_upgrade_test.c`
- `rom_e2e_c_init_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\e2e\rom_e2e_c_init_test.c`
- `default_rom_hooks.c` (L1) - `opentitan\sw\device\silicon_creator\rom\hooks\default_rom_hooks.c`
- `rom_test()` (L12) - `opentitan\sw\device\silicon_creator\rom\mock_boot_policy_ptrs.h`
- `dummy_rom_hooks.c` (L1) - `opentitan\sw\device\silicon_creator\rom\hooks\dummy_rom_hooks.c`
- `dummy_rom_init_pre_hook()` (L12) - `opentitan\sw\device\silicon_creator\rom\hooks\dummy_rom_hooks.c`
- `RomMockGroup` (L22) - `opentitan\sw\device\silicon_creator\rom\bootstrap_fuzz_test.cc`
- `.RomMockGroup()` (L24) - `opentitan\sw\device\silicon_creator\rom\bootstrap_fuzz_test.cc`
- `rom_epmp_test.c` (L1) - `opentitan\sw\device\silicon_creator\rom\rom_epmp_test.c`
- `rom_nmi_handler()` (L80) - `opentitan\sw\device\silicon_creator\rom\rom_epmp_test.c`
- `rom_interrupt_handler()` (L81) - `opentitan\sw\device\silicon_creator\rom\rom_epmp_test.c`
- `rom_exception_handler()` (L111) - `opentitan\sw\device\silicon_creator\rom\rom_epmp_test.c`
- `rom_main()` (L353) - `opentitan\sw\device\silicon_creator\rom\rom_epmp_test.c`
- `gen-otp-immutable-rom-ext-json.py` (L1) - `opentitan\util\design\gen-otp-immutable-rom-ext-json.py`
- `RomExtImmutableSectionOtpFields` (L25) - `opentitan\util\design\gen-otp-immutable-rom-ext-json.py`
- `.update_json_with_immutable_rom_ext_section_data()` (L59) - `opentitan\util\design\gen-otp-immutable-rom-ext-json.py`
- `.immutable_rom_ext_enable()` (L71) - `opentitan\util\design\gen-otp-immutable-rom-ext-json.py`
- `Update the JSON with the ROM_EXT immutable section data.         Args:` (L60) - `opentitan\util\design\gen-otp-immutable-rom-ext-json.py`
- `Checks if immutable ROM extension is enabled.          This method retrieves t` (L72) - `opentitan\util\design\gen-otp-immutable-rom-ext-json.py`
- `rom_state.c` (L1) - `opentitan\sw\device\silicon_creator\rom\rom_state.c`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:rom` | `verified_ROM.v` | `RTLLM\Miscellaneous\RISC-V\ROM\verified_ROM.v` |
| `spec_component_matches_code` | `component:rom` | `ROM` | `RTLLM\Miscellaneous\RISC-V\ROM\verified_ROM.v` |
| `spec_component_matches_code` | `component:rom` | `rom_tb` | `RTLLM\Miscellaneous\RISC-V\ROM\testbench.v` |
| `spec_component_matches_code` | `component:rom` | `ROM` | `RTLLM\Miscellaneous\RISC-V\ROM\testbench.v` |
| `spec_component_matches_code` | `component:rom` | `testbench.v` | `RTLLM\Miscellaneous\RISC-V\ROM\testbench.v` |
| `spec_component_matches_code` | `component:rom` | `immutable_rom_ext_section_test.c` | `opentitan\sw\device\silicon_creator\rom\e2e\immutable_rom_ext_section\immutable_rom_ext_section_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_ext_non_mutable()` | `opentitan\sw\device\silicon_creator\rom\e2e\immutable_rom_ext_section\immutable_rom_ext_section_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_ext_upgrade_interrupt.c` | `opentitan\sw\device\silicon_creator\rom\e2e\rom_ext_upgrade_interrupt\rom_ext_upgrade_interrupt.c` |
| `spec_component_matches_code` | `component:rom` | `rom_e2e_shutdown_alert_config_test.c` | `opentitan\sw\device\silicon_creator\rom\e2e\shutdown_alert\rom_e2e_shutdown_alert_config_test.c` |
| `spec_component_matches_code` | `component:rom` | `corrupt_rom_ext_word()` | `opentitan\sw\device\silicon_creator\rom\e2e\boot_policy_flash_ecc_error\flash_ecc_error_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_e2e_alert_config_test.c` | `opentitan\sw\device\silicon_creator\rom\e2e\shutdown_alert\rom_e2e_alert_config_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_e2e_ret_ram_init_test.c` | `opentitan\sw\device\silicon_creator\rom\e2e\retention_ram\rom_e2e_ret_ram_init_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_e2e_ret_ram_keep_test.c` | `opentitan\sw\device\silicon_creator\rom\e2e\retention_ram\rom_e2e_ret_ram_keep_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_e2e_bootstrap_rma_test.c` | `opentitan\sw\device\silicon_creator\rom\e2e\bootstrap\rom_e2e_bootstrap_rma_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_e2e_shutdown_exception_c_test.c` | `opentitan\sw\device\silicon_creator\rom\e2e\rom_e2e_shutdown_exception_c_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_e2e_keymgr_init_test.c` | `opentitan\sw\device\silicon_creator\rom\e2e\keymgr\rom_e2e_keymgr_init_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_e2e_self_hash_test.c` | `opentitan\sw\device\silicon_creator\rom\e2e\release\rom_e2e_self_hash_test.c` |
| `spec_component_matches_code` | `component:rom` | `hash_rom()` | `opentitan\sw\device\silicon_creator\rom\e2e\release\rom_e2e_self_hash_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_e2e_flash_ctrl_init_test.c` | `opentitan\sw\device\silicon_creator\rom\e2e\rom_e2e_flash_ctrl_init_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_e2e_static_critical_test.c` | `opentitan\sw\device\silicon_creator\rom\e2e\rom_e2e_static_critical_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_ext_upgrade_test.c` | `opentitan\sw\device\silicon_creator\rom\e2e\rom_ext_upgrade_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_e2e_c_init_test.c` | `opentitan\sw\device\silicon_creator\rom\e2e\rom_e2e_c_init_test.c` |
| `spec_component_matches_code` | `component:rom` | `default_rom_hooks.c` | `opentitan\sw\device\silicon_creator\rom\hooks\default_rom_hooks.c` |
| `spec_component_matches_code` | `component:rom` | `rom_test()` | `opentitan\sw\device\silicon_creator\rom\mock_boot_policy_ptrs.h` |
| `spec_component_matches_code` | `component:rom` | `dummy_rom_hooks.c` | `opentitan\sw\device\silicon_creator\rom\hooks\dummy_rom_hooks.c` |
| `spec_component_matches_code` | `component:rom` | `dummy_rom_init_pre_hook()` | `opentitan\sw\device\silicon_creator\rom\hooks\dummy_rom_hooks.c` |
| `spec_component_matches_code` | `component:rom` | `RomMockGroup` | `opentitan\sw\device\silicon_creator\rom\bootstrap_fuzz_test.cc` |
| `spec_component_matches_code` | `component:rom` | `.RomMockGroup()` | `opentitan\sw\device\silicon_creator\rom\bootstrap_fuzz_test.cc` |
| `spec_component_matches_code` | `component:rom` | `rom_epmp_test.c` | `opentitan\sw\device\silicon_creator\rom\rom_epmp_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_nmi_handler()` | `opentitan\sw\device\silicon_creator\rom\rom_epmp_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_interrupt_handler()` | `opentitan\sw\device\silicon_creator\rom\rom_epmp_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_exception_handler()` | `opentitan\sw\device\silicon_creator\rom\rom_epmp_test.c` |
| `spec_component_matches_code` | `component:rom` | `rom_main()` | `opentitan\sw\device\silicon_creator\rom\rom_epmp_test.c` |
| `spec_component_matches_code` | `component:rom` | `gen-otp-immutable-rom-ext-json.py` | `opentitan\util\design\gen-otp-immutable-rom-ext-json.py` |
| `spec_component_matches_code` | `component:rom` | `RomExtImmutableSectionOtpFields` | `opentitan\util\design\gen-otp-immutable-rom-ext-json.py` |
| `spec_component_matches_code` | `component:rom` | `.update_json_with_immutable_rom_ext_section_data()` | `opentitan\util\design\gen-otp-immutable-rom-ext-json.py` |
| `spec_component_matches_code` | `component:rom` | `.immutable_rom_ext_enable()` | `opentitan\util\design\gen-otp-immutable-rom-ext-json.py` |
| `spec_component_matches_code` | `component:rom` | `Update the JSON with the ROM_EXT immutable section data.         Args:` | `opentitan\util\design\gen-otp-immutable-rom-ext-json.py` |
| `spec_component_matches_code` | `component:rom` | `Checks if immutable ROM extension is enabled.          This method retrieves t` | `opentitan\util\design\gen-otp-immutable-rom-ext-json.py` |
| `spec_component_matches_code` | `component:rom` | `rom_state.c` | `opentitan\sw\device\silicon_creator\rom\rom_state.c` |

## Retrieval Guidance

- When a code-only query mentions `rom`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
