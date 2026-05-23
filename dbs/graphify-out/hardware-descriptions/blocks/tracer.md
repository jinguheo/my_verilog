# Hardware Description: tracer

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `tracer`
- `approved_label`: `pending:tracer`
- `doc_anchor`: `tracer`
- `module_name_prefix`: `tracer`
- `bridge_edge_count`: 17

## Inferred Hardware Role

`tracer` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 18
- Code categories: dv: 17
- Bridge relations: spec_component_matches_code: 17

## Spec Anchors

- `component:tracer` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `otbn_tracer.sv` (L1) - `opentitan\hw\ip\otbn\dv\tracer\rtl\otbn_tracer.sv`
- `otbn_tracer` (L12) - `opentitan\hw\ip\otbn\dv\tracer\rtl\otbn_tracer.sv`
- `otbn_trace_if.sv` (L1) - `opentitan\hw\ip\otbn\dv\tracer\rtl\otbn_trace_if.sv`
- `log_trace_listener.cc` (L1) - `opentitan\hw\ip\otbn\dv\tracer\cpp\log_trace_listener.cc`
- `LogTraceListener()` (L14) - `opentitan\hw\ip\otbn\dv\tracer\cpp\log_trace_listener.cc`
- `AcceptTraceString()` (L23) - `opentitan\hw\ip\otbn\dv\tracer\cpp\log_trace_listener.cc`
- `otbn_trace_listener.h` (L1) - `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_listener.h`
- `OtbnTraceListener()` (L17) - `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_listener.h`
- `log_trace_listener.h` (L1) - `opentitan\hw\ip\otbn\dv\tracer\cpp\log_trace_listener.h`
- `OtbnTraceListener()` (L26) - `opentitan\hw\ip\otbn\dv\tracer\cpp\log_trace_listener.h`
- `otbn_trace_source.cc` (L1) - `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_source.cc`
- `AddListener()` (L20) - `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_source.cc`
- `RemoveListener()` (L24) - `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_source.cc`
- `Broadcast()` (L30) - `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_source.cc`
- `accept_otbn_trace_string()` (L37) - `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_source.cc`
- `otbn_trace_source.h` (L1) - `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_source.h`
- `OtbnTraceSource()` (L20) - `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_source.h`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:tracer` | `otbn_tracer.sv` | `opentitan\hw\ip\otbn\dv\tracer\rtl\otbn_tracer.sv` |
| `spec_component_matches_code` | `component:tracer` | `otbn_tracer` | `opentitan\hw\ip\otbn\dv\tracer\rtl\otbn_tracer.sv` |
| `spec_component_matches_code` | `component:tracer` | `otbn_trace_if.sv` | `opentitan\hw\ip\otbn\dv\tracer\rtl\otbn_trace_if.sv` |
| `spec_component_matches_code` | `component:tracer` | `log_trace_listener.cc` | `opentitan\hw\ip\otbn\dv\tracer\cpp\log_trace_listener.cc` |
| `spec_component_matches_code` | `component:tracer` | `LogTraceListener()` | `opentitan\hw\ip\otbn\dv\tracer\cpp\log_trace_listener.cc` |
| `spec_component_matches_code` | `component:tracer` | `AcceptTraceString()` | `opentitan\hw\ip\otbn\dv\tracer\cpp\log_trace_listener.cc` |
| `spec_component_matches_code` | `component:tracer` | `otbn_trace_listener.h` | `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_listener.h` |
| `spec_component_matches_code` | `component:tracer` | `OtbnTraceListener()` | `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_listener.h` |
| `spec_component_matches_code` | `component:tracer` | `log_trace_listener.h` | `opentitan\hw\ip\otbn\dv\tracer\cpp\log_trace_listener.h` |
| `spec_component_matches_code` | `component:tracer` | `OtbnTraceListener()` | `opentitan\hw\ip\otbn\dv\tracer\cpp\log_trace_listener.h` |
| `spec_component_matches_code` | `component:tracer` | `otbn_trace_source.cc` | `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_source.cc` |
| `spec_component_matches_code` | `component:tracer` | `AddListener()` | `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_source.cc` |
| `spec_component_matches_code` | `component:tracer` | `RemoveListener()` | `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_source.cc` |
| `spec_component_matches_code` | `component:tracer` | `Broadcast()` | `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_source.cc` |
| `spec_component_matches_code` | `component:tracer` | `accept_otbn_trace_string()` | `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_source.cc` |
| `spec_component_matches_code` | `component:tracer` | `otbn_trace_source.h` | `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_source.h` |
| `spec_component_matches_code` | `component:tracer` | `OtbnTraceSource()` | `opentitan\hw\ip\otbn\dv\tracer\cpp\otbn_trace_source.h` |

## Retrieval Guidance

- When a code-only query mentions `tracer`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
