# Hardware Description: bitbanging

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `bitbanging`
- `bridge_edge_count`: 40
- Spec categories: component: 41
- Code categories: other_code: 40
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:bitbanging` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**OTHER_CODE** (40)
  - `.bitbanging()`:L33 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\i2c.rs`
  - `.bitbanging_byte()`:L64 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\i2c.rs`
  - `.bitbanging_bits()`:L78 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\i2c.rs`
  - `.bitbanging()`:L106 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\i2c.rs`
  - `uart_rx_sampling.rs`:L1 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `UartBitbangError`:L18 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `UartRxMonitoringDecoder`:L34 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `.new()`:L43 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `.timestamp_to_nanos()`:L62 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `.samples_since()`:L70 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `.sample_until_stable_state()`:L79 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `.get_last_state()`:L112 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `.decode_sample()`:L155 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `.decode_edge()`:L182 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `.decode_waveform()`:L229 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `.decode_response()`:L286 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `edge()`:L346 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `sample_and_decode()`:L354 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `smoke()`:L386 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`
  - `baud_rates()`:L402 — `opentitan\sw\host\opentitanlib\src\test_utils\bitbanging\uart_rx_sampling.rs`

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

- For code-only queries mentioning `bitbanging`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `bitbanging`.
