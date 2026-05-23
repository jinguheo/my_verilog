# Hardware Description: rescue

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `rescue`
- `approved_label`: `pending:rescue`
- `doc_anchor`: `rescue`
- `module_name_prefix`: `rescue`
- `bridge_edge_count`: 40

## Inferred Hardware Role

`rescue` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 41
- Code categories: other_code: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:rescue` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `rescue_xmodem.c` (L1) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue_xmodem.c`
- `rescue_protocol()` (L153) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue_xmodem.c`
- `xmodem_rescue_error_handling.rs` (L1) - `opentitan\sw\host\tests\rescue\xmodem_rescue_error_handling.rs`
- `rescue_null.c` (L1) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue_null.c`
- `rescue_spi.c` (L1) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue_spi.c`
- `rescue_protocol()` (L79) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue_spi.c`
- `rescue_usb.c` (L1) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue_usb.c`
- `rescue_protocol()` (L164) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue_usb.c`
- `dfu_rescue_error_handling.rs` (L1) - `opentitan\sw\host\tests\rescue\dfu_rescue_error_handling.rs`
- `RescueCommand` (L34) - `opentitan\sw\host\tests\rescue\dfu_rescue_error_handling.rs`
- `DfuRescueTestActions` (L48) - `opentitan\sw\host\tests\rescue\dfu_rescue_error_handling.rs`
- `rescue.c` (L1) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
- `rescue_validate_mode()` (L153) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
- `rescue_send_handler()` (L230) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
- `rescue_recv_handler()` (L289) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
- `rescue_state_init()` (L339) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
- `rescue_enter_handler()` (L373) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
- `rescue_inactivity()` (L381) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
- `rescue_enter_on_fail()` (L389) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
- `rescue_skip_next_boot()` (L398) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
- `rescue_detect_entry()` (L403) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
- `rescue.h` (L1) - `opentitan\sw\device\silicon_creator\lib\rescue\rescue.h`
- `rescue.rs` (L1) - `opentitan\sw\host\opentitanlib\src\ownership\rescue.rs`
- `OwnerRescueConfig` (L57) - `opentitan\sw\host\opentitanlib\src\ownership\rescue.rs`
- `test_owner_rescue_config_write()` (L269) - `opentitan\sw\host\opentitanlib\src\ownership\rescue.rs`
- `test_owner_rescue_config_read()` (L305) - `opentitan\sw\host\opentitanlib\src\ownership\rescue.rs`
- `rescue.rs` (L1) - `opentitan\sw\host\opentitantool\src\command\rescue.rs`
- `InternalRescueCommand` (L564) - `opentitan\sw\host\opentitantool\src\command\rescue.rs`
- `RescueCommand` (L577) - `opentitan\sw\host\opentitantool\src\command\rescue.rs`
- `RescueSerial` (L20) - `opentitan\sw\host\opentitanlib\src\rescue\serial.rs`
- `UsbRescueParams` (L46) - `opentitan\sw\host\tests\rescue\usbdfu_protocol.rs`
- `RescueError` (L31) - `opentitan\sw\host\opentitanlib\src\rescue\mod.rs`
- `RescueProtocol` (L43) - `opentitan\sw\host\opentitanlib\src\rescue\mod.rs`
- `RescueTrigger` (L51) - `opentitan\sw\host\opentitanlib\src\rescue\mod.rs`
- `RescueParams` (L59) - `opentitan\sw\host\opentitanlib\src\rescue\mod.rs`
- `Rescue` (L211) - `opentitan\sw\host\opentitanlib\src\rescue\mod.rs`
- `rescue_test.rs` (L1) - `opentitan\sw\host\tests\rescue\rescue_test.rs`
- `RescueCommand` (L60) - `opentitan\sw\host\tests\rescue\rescue_test.rs`
- `RescueTestActions` (L74) - `opentitan\sw\host\tests\rescue\rescue_test.rs`
- `expect_err_from_rescue_result()` (L242) - `opentitan\sw\host\tests\rescue\rescue_test.rs`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:rescue` | `rescue_xmodem.c` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue_xmodem.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue_protocol()` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue_xmodem.c` |
| `spec_component_matches_code` | `component:rescue` | `xmodem_rescue_error_handling.rs` | `opentitan\sw\host\tests\rescue\xmodem_rescue_error_handling.rs` |
| `spec_component_matches_code` | `component:rescue` | `rescue_null.c` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue_null.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue_spi.c` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue_spi.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue_protocol()` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue_spi.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue_usb.c` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue_usb.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue_protocol()` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue_usb.c` |
| `spec_component_matches_code` | `component:rescue` | `dfu_rescue_error_handling.rs` | `opentitan\sw\host\tests\rescue\dfu_rescue_error_handling.rs` |
| `spec_component_matches_code` | `component:rescue` | `RescueCommand` | `opentitan\sw\host\tests\rescue\dfu_rescue_error_handling.rs` |
| `spec_component_matches_code` | `component:rescue` | `DfuRescueTestActions` | `opentitan\sw\host\tests\rescue\dfu_rescue_error_handling.rs` |
| `spec_component_matches_code` | `component:rescue` | `rescue.c` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue_validate_mode()` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue_send_handler()` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue_recv_handler()` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue_state_init()` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue_enter_handler()` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue_inactivity()` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue_enter_on_fail()` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue_skip_next_boot()` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue_detect_entry()` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c` |
| `spec_component_matches_code` | `component:rescue` | `rescue.h` | `opentitan\sw\device\silicon_creator\lib\rescue\rescue.h` |
| `spec_component_matches_code` | `component:rescue` | `rescue.rs` | `opentitan\sw\host\opentitanlib\src\ownership\rescue.rs` |
| `spec_component_matches_code` | `component:rescue` | `OwnerRescueConfig` | `opentitan\sw\host\opentitanlib\src\ownership\rescue.rs` |
| `spec_component_matches_code` | `component:rescue` | `test_owner_rescue_config_write()` | `opentitan\sw\host\opentitanlib\src\ownership\rescue.rs` |
| `spec_component_matches_code` | `component:rescue` | `test_owner_rescue_config_read()` | `opentitan\sw\host\opentitanlib\src\ownership\rescue.rs` |
| `spec_component_matches_code` | `component:rescue` | `rescue.rs` | `opentitan\sw\host\opentitantool\src\command\rescue.rs` |
| `spec_component_matches_code` | `component:rescue` | `InternalRescueCommand` | `opentitan\sw\host\opentitantool\src\command\rescue.rs` |
| `spec_component_matches_code` | `component:rescue` | `RescueCommand` | `opentitan\sw\host\opentitantool\src\command\rescue.rs` |
| `spec_component_matches_code` | `component:rescue` | `RescueSerial` | `opentitan\sw\host\opentitanlib\src\rescue\serial.rs` |
| `spec_component_matches_code` | `component:rescue` | `UsbRescueParams` | `opentitan\sw\host\tests\rescue\usbdfu_protocol.rs` |
| `spec_component_matches_code` | `component:rescue` | `RescueError` | `opentitan\sw\host\opentitanlib\src\rescue\mod.rs` |
| `spec_component_matches_code` | `component:rescue` | `RescueProtocol` | `opentitan\sw\host\opentitanlib\src\rescue\mod.rs` |
| `spec_component_matches_code` | `component:rescue` | `RescueTrigger` | `opentitan\sw\host\opentitanlib\src\rescue\mod.rs` |
| `spec_component_matches_code` | `component:rescue` | `RescueParams` | `opentitan\sw\host\opentitanlib\src\rescue\mod.rs` |
| `spec_component_matches_code` | `component:rescue` | `Rescue` | `opentitan\sw\host\opentitanlib\src\rescue\mod.rs` |
| `spec_component_matches_code` | `component:rescue` | `rescue_test.rs` | `opentitan\sw\host\tests\rescue\rescue_test.rs` |
| `spec_component_matches_code` | `component:rescue` | `RescueCommand` | `opentitan\sw\host\tests\rescue\rescue_test.rs` |
| `spec_component_matches_code` | `component:rescue` | `RescueTestActions` | `opentitan\sw\host\tests\rescue\rescue_test.rs` |
| `spec_component_matches_code` | `component:rescue` | `expect_err_from_rescue_result()` | `opentitan\sw\host\tests\rescue\rescue_test.rs` |

## Retrieval Guidance

- When a code-only query mentions `rescue`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
