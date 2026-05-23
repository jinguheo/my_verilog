# Hardware Description: ipconfig

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `ipconfig`
- `approved_label`: `pending:ipconfig`
- `doc_anchor`: `ipconfig`
- `module_name_prefix`: `ipconfig`
- `bridge_edge_count`: 10

## Inferred Hardware Role

`ipconfig` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: component: 11
- Code categories: other_code: 10
- Bridge relations: spec_component_matches_code: 10

## Spec Anchors

- `component:ipconfig` (L1) - `__graphify_spec_only__/components.md`

## Code Evidence

- `ipconfig.py` (L1) - `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\util\ipconfig.py`
- `OtpCtrlIpConfig` (L13) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`
- `Initialize an `IpConfig` from an already loaded and parsed `ipconfig.hjson`` (L15) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`
- `ipconfig.py` (L1) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`
- `ipconfig.py` (L1) - `opentitan\hw\ip_templates\otp_ctrl\util\ipconfig.py`
- `IpConfig` (L11) - `opentitan\hw\top\dt\rstmgr_ipconfig.py`
- `IpConfig` (L205) - `opentitan\util\ipgen\lib.py`
- `.__init__()` (L14) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`
- `.sw_readable_partitions()` (L23) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`
- `Return the list of OTP partitions whose fields are readable after being locked,` (L24) - `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:ipconfig` | `ipconfig.py` | `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\util\ipconfig.py` |
| `spec_component_matches_code` | `component:ipconfig` | `OtpCtrlIpConfig` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py` |
| `spec_component_matches_code` | `component:ipconfig` | `Initialize an `IpConfig` from an already loaded and parsed `ipconfig.hjson`` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py` |
| `spec_component_matches_code` | `component:ipconfig` | `ipconfig.py` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py` |
| `spec_component_matches_code` | `component:ipconfig` | `ipconfig.py` | `opentitan\hw\ip_templates\otp_ctrl\util\ipconfig.py` |
| `spec_component_matches_code` | `component:ipconfig` | `IpConfig` | `opentitan\hw\top\dt\rstmgr_ipconfig.py` |
| `spec_component_matches_code` | `component:ipconfig` | `IpConfig` | `opentitan\util\ipgen\lib.py` |
| `spec_component_matches_code` | `component:ipconfig` | `.__init__()` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py` |
| `spec_component_matches_code` | `component:ipconfig` | `.sw_readable_partitions()` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py` |
| `spec_component_matches_code` | `component:ipconfig` | `Return the list of OTP partitions whose fields are readable after being locked,` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py` |

## Retrieval Guidance

- When a code-only query mentions `ipconfig`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
