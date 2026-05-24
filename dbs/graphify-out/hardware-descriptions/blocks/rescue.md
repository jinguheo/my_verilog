# Hardware Description: rescue

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `rescue`
- `bridge_edge_count`: 40
- Spec categories: component: 41
- Code categories: other_code: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:rescue` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**OTHER_CODE** (40)
  - `rescue_xmodem.c`:L1 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue_xmodem.c`
  - `rescue_protocol()`:L153 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue_xmodem.c`
  - `xmodem_rescue_error_handling.rs`:L1 — `opentitan\sw\host\tests\rescue\xmodem_rescue_error_handling.rs`
  - `rescue_null.c`:L1 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue_null.c`
  - `rescue_spi.c`:L1 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue_spi.c`
  - `rescue_protocol()`:L79 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue_spi.c`
  - `rescue_usb.c`:L1 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue_usb.c`
  - `rescue_protocol()`:L164 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue_usb.c`
  - `dfu_rescue_error_handling.rs`:L1 — `opentitan\sw\host\tests\rescue\dfu_rescue_error_handling.rs`
  - `RescueCommand`:L34 — `opentitan\sw\host\tests\rescue\dfu_rescue_error_handling.rs`
  - `DfuRescueTestActions`:L48 — `opentitan\sw\host\tests\rescue\dfu_rescue_error_handling.rs`
  - `rescue.c`:L1 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
  - `rescue_validate_mode()`:L153 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
  - `rescue_send_handler()`:L230 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
  - `rescue_recv_handler()`:L289 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
  - `rescue_state_init()`:L339 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
  - `rescue_enter_handler()`:L373 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
  - `rescue_inactivity()`:L381 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
  - `rescue_enter_on_fail()`:L389 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`
  - `rescue_skip_next_boot()`:L398 — `opentitan\sw\device\silicon_creator\lib\rescue\rescue.c`

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

- For code-only queries mentioning `rescue`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `rescue`.
