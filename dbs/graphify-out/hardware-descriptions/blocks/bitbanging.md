# Hardware Description: bitbanging

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `bitbanging`
- `approved_label`: `pending:bitbanging`
- `doc_anchor`: `bitbanging`
- `module_name_prefix`: `bitbanging`
- `bridge_edge_count`: 40

## Inferred Hardware Role

`bitbanging` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 41
- Code categories: other_code: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:bitbanging` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `.bitbanging()` (L33) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\i2c.rs`
- `.bitbanging_byte()` (L64) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\i2c.rs`
- `.bitbanging_bits()` (L78) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\i2c.rs`
- `.bitbanging()` (L106) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\i2c.rs`
- `uart_rx_sampling.rs` (L1) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `UartBitbangError` (L18) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `UartRxMonitoringDecoder` (L34) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `.new()` (L43) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `.timestamp_to_nanos()` (L62) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `.samples_since()` (L70) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `.sample_until_stable_state()` (L79) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `.get_last_state()` (L112) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `.decode_sample()` (L155) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `.decode_edge()` (L182) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `.decode_waveform()` (L229) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `.decode_response()` (L286) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `edge()` (L346) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `sample_and_decode()` (L354) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `smoke()` (L386) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `baud_rates()` (L402) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `clock_jitter_and_skew()` (L435) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `start_during_break()` (L516) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `start_mid_transmission()` (L538) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `partial_responses()` (L594) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
- `uart.rs` (L1) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `UartStopBits` (L12) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `UartBitbangConfig` (L20) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `.new()` (L30) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `.stop_bit_time()` (L51) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `.bit_time_per_frame()` (L59) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `.break_bit_time()` (L67) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `compute_parity()` (L75) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `UartTransfer` (L85) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `UartBitbangEncoder` (L100) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `.new()` (L105) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `.encode_break()` (L111) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `.encode_character()` (L121) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `.encode_characters()` (L145) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `.encode_transfer()` (L153) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`
- `.encode_transfers()` (L164) - `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:bitbanging` | `.bitbanging()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\i2c.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.bitbanging_byte()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\i2c.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.bitbanging_bits()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\i2c.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.bitbanging()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\i2c.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `uart_rx_sampling.rs` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `UartBitbangError` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `UartRxMonitoringDecoder` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.new()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.timestamp_to_nanos()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.samples_since()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.sample_until_stable_state()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.get_last_state()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.decode_sample()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.decode_edge()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.decode_waveform()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.decode_response()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `edge()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `sample_and_decode()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `smoke()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `baud_rates()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `clock_jitter_and_skew()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `start_during_break()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `start_mid_transmission()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `partial_responses()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `uart.rs` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `UartStopBits` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `UartBitbangConfig` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.new()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.stop_bit_time()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.bit_time_per_frame()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.break_bit_time()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `compute_parity()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `UartTransfer` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `UartBitbangEncoder` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.new()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.encode_break()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.encode_character()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.encode_characters()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.encode_transfer()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |
| `spec_component_matches_code` | `component:bitbanging` | `.encode_transfers()` | `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart.rs` |

## Retrieval Guidance

- When a code-only query mentions `bitbanging`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
