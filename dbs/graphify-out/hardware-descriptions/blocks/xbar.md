# Hardware Description: xbar

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **TL-UL Checklist**: This checklist is for [Hardware Stage](../../../../../doc/project_governance/development_stages.md) transitions for the [TL-UL component.](../../../../ip/tlul/README.md)
- **D2S**: [CDC_SYNCMACRO]: ../../../../../doc/project_governance/checklist/README.md#cdc_syncmacro
- **Verification Checklist**: [LINT_COMPLETE]: ../../../../../doc/project_governance/checklist/README.md#lint_complete

## Identity

- `ip_block`: `xbar`
- `bridge_edge_count`: 31
- Spec categories: component: 24, document: 19
- Code categories: other_code: 23, rtl: 8
- Bridge relations: spec_component_matches_code: 23, spec_path_matches_code_path: 8

## Spec Excerpts

### TL-UL Checklist
_Source: `opentitan/hw/top_earlgrey/ip/xbar/doc/checklist.md`_

```
# TL-UL Checklist

This checklist is for [Hardware Stage](../../../../../doc/project_governance/development_stages.md) transitions for the [TL-UL component.](../../../../ip/tlul/README.md)
All checklist items refer to the content in the [Checklist](../../../../../doc/project_governance/checklist/README.md).

## Design Checklist

### D1
```

### D2S
_Source: `opentitan/hw/top_earlgrey/ip/xbar/doc/checklist.md`_

```
[CDC_SYNCMACRO]:         ../../../../../doc/project_governance/checklist/README.md#cdc_syncmacro
[LINT_PASS]:             ../../../../../doc/project_governance/checklist/README.md#lint_pass
[CDC_SETUP]:             ../../../../../doc/project_governance/checklist/README.md#cdc_setup
[RDC_SETUP]:             ../../../../../doc/project_governance/checklist/README.md#rdc_setup
[AREA_CHECK]:
…
```

### Verification Checklist
_Source: `opentitan/hw/top_earlgrey/ip/xbar/doc/checklist.md`_

```
[LINT_COMPLETE]:        ../../../../../doc/project_governance/checklist/README.md#lint_complete
[CDC_COMPLETE]:         ../../../../../doc/project_governance/checklist/README.md#cdc_complete
[RDC_COMPLETE]:         ../../../../../doc/project_governance/checklist/README.md#rdc_complete
[REVIEW_RTL]:           ../../../../../doc/project_governance/checklist/README.md#review_rtl
[REVIEW_DELETED_FF]:
…
```

## Spec Anchors

- `component:xbar` (L1) — `__graphify_spec_only__/components.md`
- `checklist.md` (L1) — `opentitan/hw/top_earlgrey/ip/xbar/doc/checklist.md`
- `TL-UL Checklist` (L1) — `opentitan/hw/top_earlgrey/ip/xbar/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/top_earlgrey/ip/xbar/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/top_earlgrey/ip/xbar/doc/checklist.md`
- `D2` (L35) — `opentitan/hw/top_earlgrey/ip/xbar/doc/checklist.md`
- `D2S` (L79) — `opentitan/hw/top_earlgrey/ip/xbar/doc/checklist.md`
- `D3` (L99) — `opentitan/hw/top_earlgrey/ip/xbar/doc/checklist.md`
- `Verification Checklist` (L125) — `opentitan/hw/top_earlgrey/ip/xbar/doc/checklist.md`
- `V1` (L127) — `opentitan/hw/top_earlgrey/ip/xbar/doc/checklist.md`
- `V2` (L174) — `opentitan/hw/top_earlgrey/ip/xbar/doc/checklist.md`
- `V2S` (L220) — `opentitan/hw/top_earlgrey/ip/xbar/doc/checklist.md`

## Code Evidence

**RTL** (8)
  - `prim_alert_sender`:L268 — `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv`
  - `prim_alert_pkg`:L11 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `prim_esc_pkg`:L12 — `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv`
  - `prim_secded_inv_72_64_enc`:L39 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv`
  - `prim_sec_anchor_flop`:L275 — `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv`
  - `prim_packer_fifo`:L233 — `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv`
  - `adc_ctrl`:L2047 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
  - `csrng`:L2617 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`
**OTHER_CODE** (23)
  - `xbar.py`:L1 — `opentitan\util\tlgen\xbar.py`
  - `Xbar`:L11 — `opentitan\util\tlgen\xbar.py`
  - `Xbar contains configurations to generate TL-UL crossbar.`:L12 — `opentitan\util\tlgen\xbar.py`
  - `.__init__()`:L14 — `opentitan\util\tlgen\xbar.py`
  - `.get_node()`:L25 — `opentitan\util\tlgen\xbar.py`
  - `hosts()`:L33 — `opentitan\util\tlgen\xbar.py`
  - `devices()`:L37 — `opentitan\util\tlgen\xbar.py`
  - `socket_1ns()`:L41 — `opentitan\util\tlgen\xbar.py`
  - `.get_downstream_device()`:L44 — `opentitan\util\tlgen\xbar.py`
  - `.get_downstream_device_from_edge()`:L55 — `opentitan\util\tlgen\xbar.py`
  - `.get_leaf_from_s1n()`:L58 — `opentitan\util\tlgen\xbar.py`
  - `.get_socket_if_exist()`:L66 — `opentitan\util\tlgen\xbar.py`
  - `.get_leaf_from_node()`:L79 — `opentitan\util\tlgen\xbar.py`
  - `.get_devices_from_host()`:L89 — `opentitan\util\tlgen\xbar.py`
  - `.get_addr()`:L96 — `opentitan\util\tlgen\xbar.py`
  - `.connect_nodes()`:L102 — `opentitan\util\tlgen\xbar.py`
  - `.insert_node()`:L125 — `opentitan\util\tlgen\xbar.py`
  - `.repr_tree()`:L182 — `opentitan\util\tlgen\xbar.py`
  - `get end-device node from Socket_1n's Downstream port          Current implemen`:L59 — `opentitan\util\tlgen\xbar.py`
  - `return SOCKET_1N or SOCKET_M1 if exists down from the node, else             re`:L67 — `opentitan\util\tlgen\xbar.py`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:xbar` | `xbar.py` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `Xbar` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `Xbar contains configurations to generate TL-UL crossbar.` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `.__init__()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `.get_node()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `hosts()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `devices()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `socket_1ns()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `.get_downstream_device()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `.get_downstream_device_from_edge()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `.get_leaf_from_s1n()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `.get_socket_if_exist()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `.get_leaf_from_node()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `.get_devices_from_host()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `.get_addr()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `.connect_nodes()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `.insert_node()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `.repr_tree()` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `get end-device node from Socket_1n's Downstream port          Current implemen` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `return SOCKET_1N or SOCKET_M1 if exists down from the node, else             re` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `get end device node from any node, idx is given to look down.` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `string format of tree connection from node to devices          Desired output:` | `opentitan\util\tlgen\xbar.py` |
| `spec_component_matches_code` | `component:xbar` | `# TODO: add new_node.us logic` | `opentitan\util\tlgen\xbar.py` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_alert_sender` | `opentitan\hw\top_earlgrey\ip\sensor_ctrl\rtl\sensor_ctrl.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_alert_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_esc_pkg` | `opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_secded_inv_72_64_enc` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_sec_anchor_flop` | `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_packer_fifo` | `opentitan\hw\top_earlgrey\ip\ast\rtl\dev_entropy.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `adc_ctrl` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |

## Retrieval Guidance

- For code-only queries mentioning `xbar`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `xbar`.
