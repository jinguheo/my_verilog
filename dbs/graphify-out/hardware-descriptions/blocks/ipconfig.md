# Hardware Description: ipconfig

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `ipconfig`
- `bridge_edge_count`: 10
- Spec categories: component: 11
- Code categories: other_code: 10
- Bridge relations: spec_component_matches_code: 10

## Spec Anchors

- `component:ipconfig` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**OTHER_CODE** (10)
  - `ipconfig.py`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\otp_ctrl\util\ipconfig.py`
  - `OtpCtrlIpConfig`:L13 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`
  - `Initialize an `IpConfig` from an already loaded and parsed `ipconfig.hjson``:L15 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`
  - `ipconfig.py`:L1 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`
  - `ipconfig.py`:L1 — `opentitan\hw\ip_templates\otp_ctrl\util\ipconfig.py`
  - `IpConfig`:L11 — `opentitan\hw\top\dt\rstmgr_ipconfig.py`
  - `IpConfig`:L205 — `opentitan\util\ipgen\lib.py`
  - `.__init__()`:L14 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`
  - `.sw_readable_partitions()`:L23 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`
  - `Return the list of OTP partitions whose fields are readable after being locked,`:L24 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\util\ipconfig.py`

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

- For code-only queries mentioning `ipconfig`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `ipconfig`.
