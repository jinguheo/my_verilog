# Hardware Description: uart

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `uart`
- `approved_label`: `pending:uart`
- `doc_anchor`: `uart`
- `module_name_prefix`: `uart`
- `bridge_edge_count`: 112

## Inferred Hardware Role

`uart` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 84, component: 41, testplan: 28, theory: 19, interface: 16
- Code categories: other_code: 110, dv: 68, rtl: 33, sva: 22
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Anchors

- `component:uart` (L1) - `__graphify_spec_only__/components.md`
- `uart.hjson` (L1) - `opentitan/hw/ip/uart/data/uart.hjson`
- `human name` (L6) - `opentitan/hw/ip/uart/data/uart.hjson`
- `one line desc` (L7) - `opentitan/hw/ip/uart/data/uart.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/ip/uart/data/uart.hjson`
- `cip id` (L16) - `opentitan/hw/ip/uart/data/uart.hjson`
- `design spec` (L17) - `opentitan/hw/ip/uart/data/uart.hjson`
- `dv doc` (L18) - `opentitan/hw/ip/uart/data/uart.hjson`
- `hw checklist` (L19) - `opentitan/hw/ip/uart/data/uart.hjson`
- `sw checklist` (L20) - `opentitan/hw/ip/uart/data/uart.hjson`
- `revisions` (L21) - `opentitan/hw/ip/uart/data/uart.hjson`
- `version` (L23) - `opentitan/hw/ip/uart/data/uart.hjson`
- `uart_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/uart/data/uart_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/uart/data/uart_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/uart/data/uart_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/uart/data/uart_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/uart/data/uart_sec_cm_testplan.hjson`
- `uart_testplan.hjson` (L1) - `opentitan/hw/ip/uart/data/uart_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/uart/data/uart_testplan.hjson`
- `testpoints` (L12) - `opentitan/hw/ip/uart/data/uart_testplan.hjson`
- `desc` (L15) - `opentitan/hw/ip/uart/data/uart_testplan.hjson`
- `stage` (L22) - `opentitan/hw/ip/uart/data/uart_testplan.hjson`
- `tests` (L23) - `opentitan/hw/ip/uart/data/uart_testplan.hjson`
- `covergroups` (L202) - `opentitan/hw/ip/uart/data/uart_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/uart/doc/checklist.md`
- `UART Checklist` (L1) - `opentitan/hw/ip/uart/doc/checklist.md`
- `Design Checklist` (L9) - `opentitan/hw/ip/uart/doc/checklist.md`
- `D1` (L11) - `opentitan/hw/ip/uart/doc/checklist.md`
- `D1 Exceptions` (L36) - `opentitan/hw/ip/uart/doc/checklist.md`
- `D2` (L40) - `opentitan/hw/ip/uart/doc/checklist.md`
- `D2S` (L82) - `opentitan/hw/ip/uart/doc/checklist.md`
- `D3` (L102) - `opentitan/hw/ip/uart/doc/checklist.md`
- `Verification Checklist` (L130) - `opentitan/hw/ip/uart/doc/checklist.md`
- `V1` (L132) - `opentitan/hw/ip/uart/doc/checklist.md`
- `V2` (L182) - `opentitan/hw/ip/uart/doc/checklist.md`

## Code Evidence

- `uart_bind.sv` (L1) - `opentitan\hw\ip\uart\dv\sva\uart_bind.sv`
- `uart_bind` (L5) - `opentitan\hw\ip\uart\dv\sva\uart_bind.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\uart\dv\tb\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\uart\dv\tb\tb.sv`
- `uart_env_pkg` (L9) - `opentitan\hw\ip\uart\dv\tests\uart_test_pkg.sv`
- `uart_test_pkg` (L11) - `opentitan\hw\ip\uart\dv\tb\tb.sv`
- `uart_nf_if` (L35) - `opentitan\hw\ip\uart\dv\tb\tb.sv`
- `uart_base_test.sv` (L1) - `opentitan\hw\ip\uart\dv\tests\uart_base_test.sv`
- `uart_test_pkg.sv` (L1) - `opentitan\hw\ip\uart\dv\tests\uart_test_pkg.sv`
- `uart.sv` (L1) - `opentitan\hw\ip\uart\rtl\uart.sv`
- `uart` (L9) - `opentitan\hw\ip\uart\rtl\uart.sv`
- `uart_reg_pkg` (L32) - `opentitan\hw\ip\uart\rtl\uart_reg_top.sv`
- `uart_reg_top` (L57) - `opentitan\hw\ip\uart\rtl\uart.sv`
- `uart_core` (L74) - `opentitan\hw\ip\uart\rtl\uart.sv`
- `uart_core.sv` (L1) - `opentitan\hw\ip\uart\rtl\uart_core.sv`
- `uart_core` (L10) - `opentitan\hw\ip\uart\rtl\uart_core.sv`
- `uart_tx` (L204) - `opentitan\hw\ip\uart\rtl\uart_core.sv`
- `uart_rx` (L268) - `opentitan\hw\ip\uart\rtl\uart_core.sv`
- `uart_reg_pkg.sv` (L1) - `opentitan\hw\ip\uart\rtl\uart_reg_pkg.sv`
- `uart_reg_top.sv` (L1) - `opentitan\hw\ip\uart\rtl\uart_reg_top.sv`
- `uart_reg_top` (L9) - `opentitan\hw\ip\uart\rtl\uart_reg_top.sv`
- `uart_rx.sv` (L1) - `opentitan\hw\ip\uart\rtl\uart_rx.sv`
- `uart_rx` (L8) - `opentitan\hw\ip\uart\rtl\uart_rx.sv`
- `uart_tx.sv` (L1) - `opentitan\hw\ip\uart\rtl\uart_tx.sv`
- `uart_tx` (L8) - `opentitan\hw\ip\uart\rtl\uart_tx.sv`
- `flow.rs` (L1) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `SoftwareFlowControl` (L19) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `SoftwareFlowControl<T>` (L25) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `.new()` (L27) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `.poll_read_to_buffer()` (L38) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `.poll_read()` (L61) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `.write()` (L85) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `.get_baudrate()` (L124) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `.set_baudrate()` (L129) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `.get_flow_control()` (L133) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `.set_flow_control()` (L137) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `.get_device_path()` (L147) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `.set_parity()` (L151) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `.clear_rx_buffer()` (L156) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `.set_break()` (L163) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `.borrow_fd()` (L167) - `opentitan\sw\host\opentitanlib\src\io\uart\flow.rs`
- `mod.rs` (L1) - `opentitan\sw\host\opentitanlib\src\io\uart\mod.rs`
- `UartParams` (L25) - `opentitan\sw\host\opentitanlib\src\io\uart\mod.rs`
- `.create()` (L40) - `opentitan\sw\host\opentitanlib\src\io\uart\mod.rs`
- `FlowControl` (L53) - `opentitan\sw\host\opentitanlib\src\io\uart\mod.rs`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:uart` | `uart` | `opentitan\hw\top_englishbreakfast\rtl\autogen\top_englishbreakfast.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_base_test.sv` | `opentitan\hw\ip\uart\dv\tests\uart_base_test.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_env_pkg` | `opentitan\hw\ip\uart\dv\tests\uart_test_pkg.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_test_pkg.sv` | `opentitan\hw\ip\uart\dv\tests\uart_test_pkg.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_bind.sv` | `opentitan\hw\ip\uart\dv\sva\uart_bind.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_bind` | `opentitan\hw\ip\uart\dv\sva\uart_bind.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_reg_pkg` | `opentitan\hw\ip\uart\rtl\uart_reg_top.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_reg_pkg.sv` | `opentitan\hw\ip\uart\rtl\uart_reg_pkg.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_reg_top.sv` | `opentitan\hw\ip\uart\rtl\uart_reg_top.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_reg_top` | `opentitan\hw\ip\uart\rtl\uart_reg_top.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_core.sv` | `opentitan\hw\ip\uart\rtl\uart_core.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_core` | `opentitan\hw\ip\uart\rtl\uart_core.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_tx` | `opentitan\hw\ip\uart\rtl\uart_core.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_rx` | `opentitan\hw\ip\uart\rtl\uart_core.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_rx.sv` | `opentitan\hw\ip\uart\rtl\uart_rx.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_rx` | `opentitan\hw\ip\uart\rtl\uart_rx.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_tx.sv` | `opentitan\hw\ip\uart\rtl\uart_tx.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_tx` | `opentitan\hw\ip\uart\rtl\uart_tx.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_test_pkg` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_nf_if` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:uart` | `uart.sv` | `opentitan\hw\ip\uart\rtl\uart.sv` |
| `spec_component_matches_code` | `component:uart` | `uart` | `opentitan\hw\ip\uart\rtl\uart.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_reg_top` | `opentitan\hw\ip\uart\rtl\uart.sv` |
| `spec_component_matches_code` | `component:uart` | `uart_core` | `opentitan\hw\ip\uart\rtl\uart.sv` |
| `spec_component_matches_code` | `component:uart` | `tb.sv` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:uart` | `tb` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:uart` | `uart.rs` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:uart` | `UartStopBits` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:uart` | `UartBitbangConfig` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:uart` | `UartTransfer` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:uart` | `UartBitbangEncoder` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:uart` | `UartTransferDecodeError` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:uart` | `UartBitbangDecoder` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:uart` | `uart_encode_decode()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:uart` | `uart_parity_break.rs` | `opentitan\sw\host\tests\chip\uart\src\uart_parity_break.rs` |
| `spec_component_matches_code` | `component:uart` | `uart_parity_break()` | `opentitan\sw\host\tests\chip\uart\src\uart_parity_break.rs` |
| `spec_component_matches_code` | `component:uart` | `.uart()` | `opentitan\sw\host\ot_transports\verilator\src\transport.rs` |
| `spec_component_matches_code` | `component:uart` | `uart.rs` | `opentitan\sw\host\ot_transports\ti50emulator\src\uart.rs` |
| `spec_component_matches_code` | `component:uart` | `Ti50Uart` | `opentitan\sw\host\ot_transports\ti50emulator\src\uart.rs` |
| `spec_component_matches_code` | `component:uart` | `.uart()` | `opentitan\sw\host\ot_transports\chipwhisperer\src\lib.rs` |
| `spec_path_matches_code_path` | `uart.hjson` | `uart_bind.sv` | `opentitan\hw\ip\uart\dv\sva\uart_bind.sv` |
| `spec_path_matches_code_path` | `uart.hjson` | `uart_bind` | `opentitan\hw\ip\uart\dv\sva\uart_bind.sv` |
| `spec_path_matches_code_path` | `uart.hjson` | `tb.sv` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `uart.hjson` | `tb` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `uart.hjson` | `uart_env_pkg` | `opentitan\hw\ip\uart\dv\tests\uart_test_pkg.sv` |
| `spec_path_matches_code_path` | `uart.hjson` | `uart_test_pkg` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `uart.hjson` | `uart_nf_if` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `uart.hjson` | `uart_base_test.sv` | `opentitan\hw\ip\uart\dv\tests\uart_base_test.sv` |
| `spec_path_matches_code_path` | `uart_sec_cm_testplan.hjson` | `uart_bind.sv` | `opentitan\hw\ip\uart\dv\sva\uart_bind.sv` |
| `spec_path_matches_code_path` | `uart_sec_cm_testplan.hjson` | `uart_bind` | `opentitan\hw\ip\uart\dv\sva\uart_bind.sv` |
| `spec_path_matches_code_path` | `uart_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `uart_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `uart_sec_cm_testplan.hjson` | `uart_env_pkg` | `opentitan\hw\ip\uart\dv\tests\uart_test_pkg.sv` |
| `spec_path_matches_code_path` | `uart_sec_cm_testplan.hjson` | `uart_test_pkg` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `uart_sec_cm_testplan.hjson` | `uart_nf_if` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `uart_sec_cm_testplan.hjson` | `uart_base_test.sv` | `opentitan\hw\ip\uart\dv\tests\uart_base_test.sv` |
| `spec_path_matches_code_path` | `uart_testplan.hjson` | `uart_bind.sv` | `opentitan\hw\ip\uart\dv\sva\uart_bind.sv` |
| `spec_path_matches_code_path` | `uart_testplan.hjson` | `uart_bind` | `opentitan\hw\ip\uart\dv\sva\uart_bind.sv` |
| `spec_path_matches_code_path` | `uart_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `uart_testplan.hjson` | `tb` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `uart_testplan.hjson` | `uart_env_pkg` | `opentitan\hw\ip\uart\dv\tests\uart_test_pkg.sv` |
| `spec_path_matches_code_path` | `uart_testplan.hjson` | `uart_test_pkg` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `uart_testplan.hjson` | `uart_nf_if` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `uart_testplan.hjson` | `uart_base_test.sv` | `opentitan\hw\ip\uart\dv\tests\uart_base_test.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `uart_bind.sv` | `opentitan\hw\ip\uart\dv\sva\uart_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `uart_bind` | `opentitan\hw\ip\uart\dv\sva\uart_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `uart_env_pkg` | `opentitan\hw\ip\uart\dv\tests\uart_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `uart_test_pkg` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `uart_nf_if` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `uart_base_test.sv` | `opentitan\hw\ip\uart\dv\tests\uart_base_test.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `uart_bind.sv` | `opentitan\hw\ip\uart\dv\sva\uart_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `uart_bind` | `opentitan\hw\ip\uart\dv\sva\uart_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `uart_env_pkg` | `opentitan\hw\ip\uart\dv\tests\uart_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `uart_test_pkg` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `uart_nf_if` | `opentitan\hw\ip\uart\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `uart_base_test.sv` | `opentitan\hw\ip\uart\dv\tests\uart_base_test.sv` |

## Retrieval Guidance

- When a code-only query mentions `uart`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
