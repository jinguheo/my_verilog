# Hardware Description: rom

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `rom`
- `bridge_edge_count`: 40
- Spec categories: component: 41
- Code categories: other_code: 35, rtl: 5
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:rom` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**RTL** (5)
  - `verified_ROM.v`:L1 — `RTLLM\Miscellaneous\RISC-V\ROM\verified_ROM.v`
  - `ROM`:L1 — `RTLLM\Miscellaneous\RISC-V\ROM\verified_ROM.v`
  - `rom_tb`:L1 — `RTLLM\Miscellaneous\RISC-V\ROM\testbench.v`
  - `ROM`:L6 — `RTLLM\Miscellaneous\RISC-V\ROM\testbench.v`
  - `testbench.v`:L1 — `RTLLM\Miscellaneous\RISC-V\ROM\testbench.v`
**OTHER_CODE** (35)
  - `immutable_rom_ext_section_test.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\immutable_rom_ext_section\immutable_rom_ext_section_test.c`
  - `rom_ext_non_mutable()`:L32 — `opentitan\sw\device\silicon_creator\rom\e2e\immutable_rom_ext_section\immutable_rom_ext_section_test.c`
  - `rom_ext_upgrade_interrupt.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\rom_ext_upgrade_interrupt\rom_ext_upgrade_interrupt.c`
  - `rom_e2e_shutdown_alert_config_test.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\shutdown_alert\rom_e2e_shutdown_alert_config_test.c`
  - `corrupt_rom_ext_word()`:L230 — `opentitan\sw\device\silicon_creator\rom\e2e\boot_policy_flash_ecc_error\flash_ecc_error_test.c`
  - `rom_e2e_alert_config_test.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\shutdown_alert\rom_e2e_alert_config_test.c`
  - `rom_e2e_ret_ram_init_test.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\retention_ram\rom_e2e_ret_ram_init_test.c`
  - `rom_e2e_ret_ram_keep_test.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\retention_ram\rom_e2e_ret_ram_keep_test.c`
  - `rom_e2e_bootstrap_rma_test.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\bootstrap\rom_e2e_bootstrap_rma_test.c`
  - `rom_e2e_shutdown_exception_c_test.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\rom_e2e_shutdown_exception_c_test.c`
  - `rom_e2e_keymgr_init_test.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\keymgr\rom_e2e_keymgr_init_test.c`
  - `rom_e2e_self_hash_test.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\release\rom_e2e_self_hash_test.c`
  - `hash_rom()`:L58 — `opentitan\sw\device\silicon_creator\rom\e2e\release\rom_e2e_self_hash_test.c`
  - `rom_e2e_flash_ctrl_init_test.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\rom_e2e_flash_ctrl_init_test.c`
  - `rom_e2e_static_critical_test.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\rom_e2e_static_critical_test.c`
  - `rom_ext_upgrade_test.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\rom_ext_upgrade_test.c`
  - `rom_e2e_c_init_test.c`:L1 — `opentitan\sw\device\silicon_creator\rom\e2e\rom_e2e_c_init_test.c`
  - `default_rom_hooks.c`:L1 — `opentitan\sw\device\silicon_creator\rom\hooks\default_rom_hooks.c`
  - `rom_test()`:L12 — `opentitan\sw\device\silicon_creator\rom\mock_boot_policy_ptrs.h`
  - `dummy_rom_hooks.c`:L1 — `opentitan\sw\device\silicon_creator\rom\hooks\dummy_rom_hooks.c`

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

- For code-only queries mentioning `rom`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `rom`.
