# Hardware Description: otp_macro

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **OTP MACRO HWIP Technical Specification**: This document specifies the OTP MACRO hardware IP functionality.
- **Overview**: This document specifies the OTP MACRO hardware IP functionality.
- **cip id**: one_line_desc: "OTP macro simulation model and CSR block",

## Identity

- `ip_block`: `otp_macro`
- `bridge_edge_count`: 33
- Spec categories: document: 31, testplan: 13, component: 10
- Code categories: rtl: 41
- Bridge relations: spec_path_matches_code_path: 24, spec_component_matches_code: 9

## Spec Excerpts

### OTP MACRO HWIP Technical Specification
_Source: `opentitan/hw/ip/otp_macro/README.md`_

```
# OTP MACRO HWIP Technical Specification

# Overview

This document specifies the OTP MACRO hardware IP functionality.
The OTP MACRO is a comportable IP that wraps an OTP macro.
This block is expected to be used in conjunction with an OTP Controller, and most of the features of the macro correspond to features of the controller.
```

### Overview
_Source: `opentitan/hw/ip/otp_macro/README.md`_

```
# OTP MACRO HWIP Technical Specification

# Overview

This document specifies the OTP MACRO hardware IP functionality.
The OTP MACRO is a comportable IP that wraps an OTP macro.
This block is expected to be used in conjunction with an OTP Controller, and most of the features of the macro correspond to features of the controller.

## Features
```

### cip id
_Source: `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`_

```
one_line_desc:      "OTP macro simulation model and CSR block",
  one_paragraph_desc: '''
  OTP macro has one-time programmable fuses that configure this top.
  It is tightly coupled to the OTP controller, but placed at the top for
  ease of integration. It contains a CSR block for testing and macro specific
  functionality.
  '''
  // Unique comportable IP identifier defined under KNOWN_CIP_IDS i
…
```

### design spec
_Source: `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`_

```
one_paragraph_desc: '''
  OTP macro has one-time programmable fuses that configure this top.
  It is tightly coupled to the OTP controller, but placed at the top for
  ease of integration. It contains a CSR block for testing and macro specific
  functionality.
  '''
  // Unique comportable IP identifier defined under KNOWN_CIP_IDS in the regtool.
  cip_id:             "44",
  design_spec:        "
…
```

### revisions
_Source: `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`_

```
functionality.
  '''
  // Unique comportable IP identifier defined under KNOWN_CIP_IDS in the regtool.
  cip_id:             "44",
  design_spec:        "../doc",
#  dv_doc:             "../doc/dv",
#  hw_checklist:       "../doc/checklist",
#  sw_checklist:       "/sw/device/lib/dif/dif_pwm",
  revisions: [
    {
      version:            "1.0.0",
      life_stage:         "L1",
      design_stag
…
```

### testpoints
_Source: `opentitan/hw/ip/otp_macro/data/otp_macro_sec_cm_testplan.hjson`_

```
// It is possible that the testing of some of these countermeasures may already
// be covered as a testpoint in a different testplan. This duplication is ok -
// the test would have likely already been developed. We simply map those tests
// to the testpoints below using the `tests` key.
//
// Please ensure that this testplan is imported in:
// .../otp_macro/data/otp_macro_testplan.hjson
{
  testp
…
```

### desc
_Source: `opentitan/hw/ip/otp_macro/data/otp_macro_sec_cm_testplan.hjson`_

```
// to the testpoints below using the `tests` key.
//
// Please ensure that this testplan is imported in:
// .../otp_macro/data/otp_macro_testplan.hjson
{
  testpoints: [
    {
      name: sec_cm_lc_ctrl_intersig_mubi
      desc: "Verify the countermeasure(s) LC_CTRL.INTERSIG.MUBI."
      stage: V2S
      tests: ["otp_ctrl_dai_lock"]
    }
    {
      name: sec_cm_test_bus_lc_gated
      desc: "Ver
…
```

### stage
_Source: `opentitan/hw/ip/otp_macro/data/otp_macro_sec_cm_testplan.hjson`_

```
//
// Please ensure that this testplan is imported in:
// .../otp_macro/data/otp_macro_testplan.hjson
{
  testpoints: [
    {
      name: sec_cm_lc_ctrl_intersig_mubi
      desc: "Verify the countermeasure(s) LC_CTRL.INTERSIG.MUBI."
      stage: V2S
      tests: ["otp_ctrl_dai_lock"]
    }
    {
      name: sec_cm_test_bus_lc_gated
      desc: "Verify the countermeasure(s) TEST.BUS.LC_GATED."
…
```

## Spec Anchors

- `component:otp_macro` (L1) — `__graphify_spec_only__/components.md`
- `otp_macro.hjson` (L1) — `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `human name` (L6) — `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `one line desc` (L7) — `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `one paragraph desc` (L8) — `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `cip id` (L15) — `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `design spec` (L16) — `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `revisions` (L20) — `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `version` (L22) — `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `life stage` (L23) — `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `design stage` (L24) — `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `verification stage` (L25) — `opentitan/hw/ip/otp_macro/data/otp_macro.hjson`
- `otp_macro_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/otp_macro/data/otp_macro_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/otp_macro/data/otp_macro_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/otp_macro/data/otp_macro_sec_cm_testplan.hjson`
- `stage` (L29) — `opentitan/hw/ip/otp_macro/data/otp_macro_sec_cm_testplan.hjson`
- `tests` (L30) — `opentitan/hw/ip/otp_macro/data/otp_macro_sec_cm_testplan.hjson`
- `README.md` (L1) — `opentitan/hw/ip/otp_macro/README.md`
- `OTP MACRO HWIP Technical Specification` (L1) — `opentitan/hw/ip/otp_macro/README.md`
- `Overview` (L3) — `opentitan/hw/ip/otp_macro/README.md`
- `Features` (L9) — `opentitan/hw/ip/otp_macro/README.md`

## Code Evidence

**RTL** (9)
  - `otp_macro.sv`:L1 — `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv`
  - `otp_macro`:L7 — `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv`
  - `otp_macro_reg_pkg`:L32 — `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv`
  - `otp_macro_prim_reg_top`:L160 — `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv`
  - `otp_macro_pkg.sv`:L1 — `opentitan\hw\ip\otp_macro\rtl\otp_macro_pkg.sv`
  - `otp_macro_prim_reg_top.sv`:L1 — `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv`
  - `otp_macro_prim_reg_top`:L9 — `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv`
  - `otp_macro_reg_pkg.sv`:L1 — `opentitan\hw\ip\otp_macro\rtl\otp_macro_reg_pkg.sv`
  - `otp_macro`:L1559 — `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv`

## Neighbor Components

- `rv_plic` (5 refs; instantiates×5)
- `rv_core_ibex` (3 refs; instantiates×2, imports_from×1)
- `otp_ctrl` (2 refs; imports_from×2)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro_reg_pkg` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro_prim_reg_top.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro_reg_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_reg_pkg.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_pkg.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_component_matches_code` | `component:otp_macro` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro_reg_pkg` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_pkg.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro_prim_reg_top.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `otp_macro.hjson` | `otp_macro_reg_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_reg_pkg.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro_reg_pkg` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_pkg.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro_prim_reg_top.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `otp_macro_sec_cm_testplan.hjson` | `otp_macro_reg_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_reg_pkg.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro_reg_pkg` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_pkg.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro_prim_reg_top.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro_prim_reg_top` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_prim_reg_top.sv` |
| `spec_path_matches_code_path` | `README.md` | `otp_macro_reg_pkg.sv` | `opentitan\hw\ip\otp_macro\rtl\otp_macro_reg_pkg.sv` |

## Retrieval Guidance

- For code-only queries mentioning `otp_macro`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `otp_macro`.
