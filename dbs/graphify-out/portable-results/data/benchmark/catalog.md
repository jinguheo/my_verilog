# Spec-Code Retrieval Benchmark

- Questions: 150
- Source graph: `D:\MyWork\verilog\dbs\graphify-out\spec-code-graphify\graph.json`
- Goal: compare code-only, spec-only, and spec-code Graphify variants.

## Distribution

| Type | Count |
|---|---:|
| bridge_disambiguation | 30 |
| code_to_spec_trace | 30 |
| requirement_to_rtl | 30 |
| spec_to_code_trace | 30 |
| verification_trace | 30 |

## First 10 Questions

### speccode_001 - spec_to_code_trace

Find the implementation-side code evidence for the spec concept `otp_ctrl_sec_cm_testplan.hjson`. The spec-side clue is `top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

- Spec gold: `otp_ctrl_sec_cm_testplan.hjson` from `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`
- Code gold: `prim_sec_anchor_flop` from `opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv`

### speccode_002 - code_to_spec_trace

Find the spec-side evidence that explains the code node `prim_sync_reqack` under `top_englishbreakfast/ip_autogen/rstmgr/rtl/rstmgr_cnsty_chk.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

- Spec gold: `rstmgr_cnsty_chk_testplan.hjson` from `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`
- Code gold: `prim_sync_reqack` from `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_cnsty_chk.sv`

### speccode_003 - requirement_to_rtl

A reviewer asks where the `rstmgr` requirement described around `rstmgr_cnsty_chk_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

- Spec gold: `rstmgr_cnsty_chk_testplan.hjson` from `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`
- Code gold: `prim_rst_sync` from `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv`

### speccode_004 - bridge_disambiguation

Use the graph bridge, not only lexical filename matching: connect spec clue `rstmgr_cnsty_chk_testplan.hjson` from `rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson` to the most relevant code artifact in `ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv`.

- Spec gold: `rstmgr_cnsty_chk_testplan.hjson` from `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`
- Code gold: `rstmgr_cnsty_chk_if` from `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv`

### speccode_005 - verification_trace

For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `rstmgr_cnsty_chk_testplan.hjson` in the `rstmgr` area.

- Spec gold: `rstmgr_cnsty_chk_testplan.hjson` from `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`
- Code gold: `rstmgr_cnsty_chk` from `opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv`

### speccode_006 - spec_to_code_trace

Find the implementation-side code evidence for the spec concept `rv_core_ibex_sec_cm_testplan.hjson`. The spec-side clue is `top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

- Spec gold: `rv_core_ibex_sec_cm_testplan.hjson` from `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson`
- Code gold: `prim_sec_anchor_buf` from `opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv`

### speccode_007 - code_to_spec_trace

Find the spec-side evidence that explains the code node `prim_flop_en` under `top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

- Spec gold: `ac_range_check_testplan.hjson` from `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- Code gold: `prim_flop_en` from `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`

### speccode_008 - requirement_to_rtl

A reviewer asks where the `ac_range_check` requirement described around `ac_range_check_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

- Spec gold: `ac_range_check_testplan.hjson` from `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- Code gold: `prim_onehot_enc` from `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`

### speccode_009 - bridge_disambiguation

Use the graph bridge, not only lexical filename matching: connect spec clue `ac_range_check_testplan.hjson` from `top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson` to the most relevant code artifact in `ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`.

- Spec gold: `ac_range_check_testplan.hjson` from `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- Code gold: `ac_range_check_bind.sv` from `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv`

### speccode_010 - verification_trace

For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `ac_range_check_testplan.hjson` in the `ac_range_check` area.

- Spec gold: `ac_range_check_testplan.hjson` from `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- Code gold: `ac_range_check_bind` from `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv`
