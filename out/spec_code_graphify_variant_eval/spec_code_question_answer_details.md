# Spec-Code KG Evaluation Details

- Questions: 150
- Variants: spec-only, code-only, spec-code
- Each item includes the benchmark question, gold answers, and the actual top retrieved nodes.

## Summary Table

| Task | Type | Best@10 | Gold Bridge |
|---|---|---|---|
| speccode_001 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_002 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_003 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_004 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_005 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_006 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_007 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_008 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_009 | bridge_disambiguation | spec-only | spec_path_matches_code_path |
| speccode_010 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_011 | spec_to_code_trace | spec-only | spec_path_matches_code_path |
| speccode_012 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_013 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_014 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_015 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_016 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_017 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_018 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_019 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_020 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_021 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_022 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_023 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_024 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_025 | verification_trace | code-only | spec_path_matches_code_path |
| speccode_026 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_027 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_028 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_029 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_030 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_031 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_032 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_033 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_034 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_035 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_036 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_037 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_038 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_039 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_040 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_041 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_042 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_043 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_044 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_045 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_046 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_047 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_048 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_049 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_050 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_051 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_052 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_053 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_054 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_055 | verification_trace | code-only | spec_path_matches_code_path |
| speccode_056 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_057 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_058 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_059 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_060 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_061 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_062 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_063 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_064 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_065 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_066 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_067 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_068 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_069 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_070 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_071 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_072 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_073 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_074 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_075 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_076 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_077 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_078 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_079 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_080 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_081 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_082 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_083 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_084 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_085 | verification_trace | code-only | spec_path_matches_code_path |
| speccode_086 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_087 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_088 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_089 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_090 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_091 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_092 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_093 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_094 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_095 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_096 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_097 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_098 | requirement_to_rtl | code-only | spec_path_matches_code_path |
| speccode_099 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_100 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_101 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_102 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_103 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_104 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_105 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_106 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_107 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_108 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_109 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_110 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_111 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_112 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_113 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_114 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_115 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_116 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_117 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_118 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_119 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_120 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_121 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_122 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_123 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_124 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_125 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_126 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_127 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_128 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_129 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_130 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_131 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_132 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_133 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_134 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_135 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_136 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_137 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_138 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_139 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_140 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_141 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_142 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_143 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_144 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_145 | verification_trace | spec-code | spec_path_matches_code_path |
| speccode_146 | spec_to_code_trace | spec-code | spec_path_matches_code_path |
| speccode_147 | code_to_spec_trace | spec-code | spec_path_matches_code_path |
| speccode_148 | requirement_to_rtl | spec-code | spec_path_matches_code_path |
| speccode_149 | bridge_disambiguation | spec-code | spec_path_matches_code_path |
| speccode_150 | verification_trace | spec-code | spec_path_matches_code_path |

## Detailed Questions

### speccode_001 (spec_to_code_trace, L4)

**Question**: Find the implementation-side code evidence for the spec concept `otp_ctrl_sec_cm_testplan.hjson`. The spec-side clue is `top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: otp_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv:L275

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_sec_cm_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1289.3125 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=1064.4375 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=975.8 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=890.75 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=838.2375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=113.6875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.7 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.875 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=94.3125 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=92.5625 |
| spec-code | 10 | 1 | 10 | spec=N, code=Y, joint=N | 1. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1529.975 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1528.0375 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1514.95 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1514.05 \| 5. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1463.4125 |

### speccode_002 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `prim_sync_reqack` under `top_englishbreakfast/ip_autogen/rstmgr/rtl/rstmgr_cnsty_chk.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: rstmgr_cnsty_chk_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson | component:chip_rstmgr_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rstmgr_testplan_hjson [component] @ __graphify_spec_only__/components.md | component:rstmgr [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_sync_reqack [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_cnsty_chk.sv:L274

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_sync_reqack, top_englishbreakfast/ip_autogen/rstmgr/rtl/rstmgr_cnsty_chk.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=651.0125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=589.6625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=552.9125 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=509.5125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=501.9 |
| code-only | - | 21 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=122.0 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=107.4375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.3125 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=85.3125 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=84.25 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=934.0625 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=730.0125 \| 3. component:pinmux [component] @ __graphify_spec_only__/components.md, score=679.0875 \| 4. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=667.925 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=650.075 |

### speccode_003 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `rstmgr` requirement described around `rstmgr_cnsty_chk_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: rstmgr_cnsty_chk_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson | component:chip_rstmgr_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rstmgr_testplan_hjson [component] @ __graphify_spec_only__/components.md | component:rstmgr [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_rst_sync [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv:L451

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rstmgr, rstmgr_cnsty_chk_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=329.0125 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=290.4125 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=290.0625 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=289.7125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=183.4875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=48.875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=41.4375 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=35.875 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.0625 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=418.5625 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=290.4125 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=290.0625 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=289.7125 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=251.925 |

### speccode_004 (bridge_disambiguation, L4)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `rstmgr_cnsty_chk_testplan.hjson` from `rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson` to the most relevant code artifact in `ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv`.

**Gold spec answer**: rstmgr_cnsty_chk_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson | component:chip_rstmgr_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rstmgr_testplan_hjson [component] @ __graphify_spec_only__/components.md | component:rstmgr [component] @ __graphify_spec_only__/components.md

**Gold code answer**: rstmgr_cnsty_chk_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv:L436

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rstmgr_cnsty_chk_testplan.hjson, rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson, ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=820.6625 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=732.1125 \| 3. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=707.3625 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=691.8625 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=624.4 |
| code-only | - | 20 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=42.8125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=29.5 \| 3. prim_mubi4_sync [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_leaf_rst.sv, score=28.375 \| 4. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=25.25 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=24.0 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=885.3375 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=820.6625 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=778.6 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=778.6 \| 5. csrng [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=736.05 |

### speccode_005 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `rstmgr_cnsty_chk_testplan.hjson` in the `rstmgr` area.

**Gold spec answer**: rstmgr_cnsty_chk_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson | component:chip_rstmgr_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rstmgr_testplan_hjson [component] @ __graphify_spec_only__/components.md | component:rstmgr [component] @ __graphify_spec_only__/components.md

**Gold code answer**: rstmgr_cnsty_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv:L458

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rstmgr_cnsty_chk_testplan.hjson, rstmgr, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=331.1125 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=293.5625 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=292.1625 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=291.2875 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=183.4875 |
| code-only | - | 11 | - | spec=N, code=N, joint=N | 1. dif_rstmgr.c [code] @ opentitan\sw\device\lib\dif\dif_rstmgr.c, score=13.4 \| 2. prim_sync_reqack [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_cnsty_chk.sv, score=9.75 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=9.5 \| 4. dif_rstmgr_unittest.cc [code] @ opentitan\sw\device\lib\dif\dif_rstmgr_unittest.cc, score=9.375 \| 5. rstmgr_reg_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_reg_top.sv, score=9.025 |
| spec-code | 1 | 30 | 30 | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=403.1125 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=293.5625 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=292.1625 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=291.2875 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=248.4 |

### speccode_006 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `rv_core_ibex_sec_cm_testplan.hjson`. The spec-side clue is `top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sec_anchor_buf [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L359

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1144.5875 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=968.875 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=960.6625 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=889.9625 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=854.175 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=368.0 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=108.0 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.2875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.25 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1361.275 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1144.5875 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=1086.4125 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1061.175 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1059.375 |

### speccode_007 (code_to_spec_trace, L4)

**Question**: Find the spec-side evidence that explains the code node `prim_flop_en` under `top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv:L269

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_flop_en, top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=624.75 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=585.9875 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=524.5625 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=521.2375 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=462.4375 |
| code-only | - | 19 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=113.4375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=97.85 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.0625 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=84.75 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=84.625 |
| spec-code | 9 | 1 | 9 | spec=N, code=Y, joint=N | 1. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=791.7625 \| 2. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=785.0125 \| 3. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=783.8875 \| 4. tlul_jtag_dtm [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=756.8875 \| 5. tlul_cmd_intg_gen [code] @ opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv, score=755.8875 |

### speccode_008 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `ac_range_check` requirement described around `ac_range_check_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv:L128

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check, ac_range_check_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=281.1375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=279.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=277.1125 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=178.15 \| 5. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=167.2 |
| code-only | - | 19 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.8125 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.3125 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=281.1375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=279.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=277.1125 \| 4. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=258.55 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=231.0 |

### speccode_009 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `ac_range_check_testplan.hjson` from `top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson` to the most relevant code artifact in `ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_testplan.hjson, top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson, ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1107.225 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=927.9375 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=856.5375 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=852.8625 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=702.8875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.5 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=56.5 \| 3. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.5625 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=54.3125 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=54.3125 |
| spec-code | 16 | - | - | spec=N, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1107.225 \| 2. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1103.475 \| 3. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=1075.5625 \| 4. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=1075.5625 \| 5. tlul_jtag_dtm [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1041.6 |

### speccode_010 (verification_trace, L4)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `ac_range_check_testplan.hjson` in the `ac_range_check` area.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_testplan.hjson, ac_range_check, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=283.2375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=282.275 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=278.6875 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=178.15 \| 5. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=168.25 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.625 \| 2. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=17.4375 \| 3. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=12.5 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=11.2625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=283.2375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=282.275 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=278.6875 \| 4. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=243.4 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=227.475 |

### speccode_011 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `ac_range_check_testplan.hjson`. The spec-side clue is `top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_testplan.hjson, top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1105.0375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=924.175 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=856.5375 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=850.325 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=702.625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.6875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.25 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=84.0 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.5625 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.0625 |
| spec-code | 16 | - | - | spec=N, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1105.0375 \| 2. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1101.9625 \| 3. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=1080.425 \| 4. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=1076.3 \| 5. tlul_jtag_dtm [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1041.0625 |

### speccode_012 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `ac_range_check_env_pkg` under `ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv:L9

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_env_pkg, ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=343.0 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=289.8875 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=287.175 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=282.625 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=256.1125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=526.4375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=514.425 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=299.5625 \| 4. .ok() [code] @ opentitan\sw\host\opentitanlib\src\transport\mod.rs, score=285.6875 \| 5. mmio_region_from_addr() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=141.3125 |
| spec-code | 3 | - | - | spec=Y, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=526.4375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=514.425 \| 3. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=370.25 \| 4. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=362.5375 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=349.7125 |

### speccode_013 (requirement_to_rtl, L4)

**Question**: A reviewer asks where the `ac_range_check` requirement described around `ac_range_check_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_test_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv:L10

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check, ac_range_check_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=281.1375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=279.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=277.1125 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=178.15 \| 5. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=167.2 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.8125 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.3125 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=281.1375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=279.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=277.1125 \| 4. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=258.55 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=231.0 |

### speccode_014 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `interfaces.md` from `top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md` to the most relevant code artifact in `top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv:L269

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md, top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=874.2125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=844.375 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=770.45 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=596.925 |
| code-only | - | 20 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=105.0625 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.0625 \| 3. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.0625 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=86.5625 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=85.8125 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 2. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=901.925 \| 3. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=898.35 \| 4. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=897.8 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=874.2125 |

### speccode_015 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `interfaces.md` in the `ac_range_check` area.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv:L128

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, ac_range_check, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=196.275 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=123.975 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=67.725 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=44.3625 \| 5. component:opentitan [component] @ __graphify_spec_only__/components.md, score=42.0 |
| code-only | - | 5 | - | spec=N, code=Y, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.6875 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.3125 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=196.275 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=191.475 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=67.725 \| 4. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=57.3375 \| 5. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=57.3375 |

### speccode_016 (spec_to_code_trace, L4)

**Question**: Find the implementation-side code evidence for the spec concept `interfaces.md`. The spec-side clue is `top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=873.5125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=834.8375 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=769.225 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=592.4625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.6875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.0 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=83.1 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.3125 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=81.8125 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 2. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=885.725 \| 3. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=881.6 \| 4. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=881.4625 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=873.5125 |

### speccode_017 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `ac_range_check_bind` under `ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_bind, ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=343.0 \| 2. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=287.175 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=285.425 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=278.25 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=250.25 |
| code-only | - | 23 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=30.3125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=27.4 \| 3. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=24.9375 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=23.6875 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=23.6875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=377.7625 \| 2. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=363.3125 \| 3. component:pinmux [component] @ __graphify_spec_only__/components.md, score=348.35 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=343.0 \| 5. component:clkmgr [component] @ __graphify_spec_only__/components.md, score=338.5375 |

### speccode_018 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `ac_range_check` requirement described around `interfaces.md` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check, interfaces.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=196.275 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=122.925 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=42.7875 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=38.85 \| 5. topic:security [topic] @ __graphify_spec_only__/topics.md, score=37.0125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.6875 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.1875 |
| spec-code | 1 | 17 | 17 | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=206.625 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=196.275 \| 3. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=65.2125 \| 4. component:tlul [component] @ __graphify_spec_only__/components.md, score=61.6125 \| 5. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=61.0875 |

### speccode_019 (bridge_disambiguation, L4)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `interfaces.md` from `top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md` to the most relevant code artifact in `ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv`.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv:L9

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md, ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=878.675 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=843.15 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=771.2375 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=598.675 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=526.75 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=514.425 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=301.0 \| 4. .ok() [code] @ opentitan\sw\host\opentitanlib\src\transport\mod.rs, score=300.9375 \| 5. mmio_region_from_addr() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=142.0625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 2. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=891.7375 \| 3. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=891.7375 \| 4. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=891.3 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=878.675 |

### speccode_020 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `interfaces.md` in the `ac_range_check` area.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_test_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv:L10

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, ac_range_check, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=196.275 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=123.975 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=67.725 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=44.3625 \| 5. component:opentitan [component] @ __graphify_spec_only__/components.md, score=42.0 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.6875 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.3125 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 6 | 6 | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=196.275 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=191.475 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=67.725 \| 4. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=57.3375 \| 5. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=57.3375 |

### speccode_021 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `theory_of_operation.md`. The spec-side clue is `top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv:L269

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1733.0125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=899.4125 \| 4. component:pinmux [component] @ __graphify_spec_only__/components.md, score=644.0875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=635.5125 |
| code-only | - | 22 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.6875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.0 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=83.1 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.3125 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=81.8125 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1733.0125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 3. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=918.125 \| 4. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=914.0 \| 5. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=909.8125 |

### speccode_022 (code_to_spec_trace, L4)

**Question**: Find the spec-side evidence that explains the code node `prim_onehot_enc` under `top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv:L128

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_onehot_enc, top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=624.75 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=585.9875 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=524.5625 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=521.2375 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=462.4375 |
| code-only | - | 18 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=111.5625 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=97.85 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.0625 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=84.625 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=83.8125 |
| spec-code | 9 | 1 | 9 | spec=N, code=Y, joint=N | 1. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=789.2625 \| 2. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=787.6375 \| 3. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=785.0125 \| 4. tlul_jtag_dtm [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=756.8875 \| 5. tlul_cmd_intg_gen [code] @ opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv, score=755.8875 |

### speccode_023 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `ac_range_check` requirement described around `theory_of_operation.md` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=846.4625 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=127.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=99.75 \| 4. component:system [component] @ __graphify_spec_only__/components.md, score=77.875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=69.5625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.6875 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.1875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=846.4625 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=210.825 \| 3. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=102.3375 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=99.75 \| 5. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=93.5625 |

### speccode_024 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `theory_of_operation.md` from `top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md` to the most relevant code artifact in `ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md, ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1733.7125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=903.35 \| 4. component:pinmux [component] @ __graphify_spec_only__/components.md, score=644.4375 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=635.775 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.5 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=56.5 \| 3. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.5625 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=54.3125 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=54.3125 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1733.7125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 3. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=918.5125 \| 4. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=918.5125 \| 5. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=914.025 |

### speccode_025 (verification_trace, L4)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `theory_of_operation.md` in the `ac_range_check` area.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, ac_range_check, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=845.9375 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=128.175 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=101.325 \| 4. component:system [component] @ __graphify_spec_only__/components.md, score=78.925 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=71.6625 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.375 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.0 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 22 | 22 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=845.9375 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=195.675 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=101.325 \| 4. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=85.6875 \| 5. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=85.6875 |

### speccode_026 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `theory_of_operation.md`. The spec-side clue is `top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv:L9

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1733.0125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=899.4125 \| 4. component:pinmux [component] @ __graphify_spec_only__/components.md, score=644.0875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=635.5125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.6875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.0 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=83.1 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.3125 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=81.8125 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1733.0125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 3. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=918.125 \| 4. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=914.0 \| 5. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=909.8125 |

### speccode_027 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `ac_range_check_test_pkg` under `ip_autogen/ac_range_check/dv/tb/tb.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_test_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv:L10

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_test_pkg, ip_autogen/ac_range_check/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=343.0 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=289.3625 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=287.0 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=281.75 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=252.4375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=243.125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=232.5 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=149.625 \| 4. .ok() [code] @ opentitan\sw\host\opentitanlib\src\transport\mod.rs, score=143.9375 \| 5. assertEqual() [code] @ ibex\vendor\riscv-tests\debug\testlib.py, score=59.0625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=352.25 \| 2. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=349.5625 \| 3. component:pinmux [component] @ __graphify_spec_only__/components.md, score=345.8125 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=343.0 \| 5. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=319.6875 |

### speccode_028 (requirement_to_rtl, L4)

**Question**: A reviewer asks where the `alert_handler` requirement described around `alert_handler_sec_cm_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler, alert_handler_sec_cm_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=329.425 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=317.7125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=65.0 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=43.275 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 5. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=491.875 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=327.8375 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=324.275 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 |

### speccode_029 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `alert_handler_sec_cm_testplan.hjson` from `top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson` to the most relevant code artifact in `ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_sec_cm_testplan.hjson, top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson, ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1155.6125 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=973.4375 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=897.05 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=874.5625 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=725.375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=69.125 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.5 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=57.6875 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.5 |
| spec-code | 5 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1155.6125 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1118.0875 \| 3. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1116.525 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1114.9125 \| 5. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=1083.525 |

### speccode_030 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `alert_handler_sec_cm_testplan.hjson` in the `alert_handler` area.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_sec_cm_testplan.hjson, alert_handler, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=332.05 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=320.8625 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=320.5125 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=320.25 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=65.0 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 3. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=33.1 \| 4. .check() [code] @ opentitan\util\validate_testplans.py, score=25.5 \| 5. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.9375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=485.05 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=324.3125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=321.425 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=320.8625 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=320.5125 |

### speccode_031 (spec_to_code_trace, L4)

**Question**: Find the implementation-side code evidence for the spec concept `alert_handler_sec_cm_testplan.hjson`. The spec-side clue is `top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_sec_cm_testplan.hjson, top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1153.3375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=969.5875 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=894.425 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=874.5625 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=725.1125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.6875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=88.575 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.4375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=83.25 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.5 |
| spec-code | 6 | - | - | spec=N, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1153.3375 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1119.7125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1115.8625 \| 4. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1115.0125 \| 5. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=1068.0125 |

### speccode_032 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `tb.sv` under `ip_autogen/alert_handler/dv/tb/tb.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, ip_autogen/alert_handler/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=362.5 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=360.0625 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=307.5625 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=301.0 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=288.75 |
| code-only | - | 22 | - | spec=N, code=N, joint=N | 1. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=30.625 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=30.3125 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=29.125 \| 4. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=28.3125 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=26.875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=587.5 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=372.8125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=370.5625 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=360.0625 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=346.8125 |

### speccode_033 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `alert_handler` requirement described around `alert_handler_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler, alert_handler_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=324.175 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=290.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=289.975 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=289.275 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=43.275 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.25 \| 4. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=33.1 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=486.625 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=309.65 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=306.275 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=290.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=289.975 |

### speccode_034 (bridge_disambiguation, L4)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `alert_handler_testplan.hjson` from `top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson` to the most relevant code artifact in `ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_testplan.hjson, top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson, ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1122.0125 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=939.4 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=874.5625 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=863.0125 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=714.7875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.5 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=57.6875 \| 3. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.5 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.5 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.5 |
| spec-code | 5 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1122.0125 \| 2. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1104.375 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1096.2625 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1093.3125 \| 5. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=1077.925 |

### speccode_035 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `alert_handler_testplan.hjson` in the `alert_handler` area.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_testplan.hjson, alert_handler, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=326.8 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=292.425 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=292.25 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=292.075 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=33.1 \| 2. .check() [code] @ opentitan\util\validate_testplans.py, score=24.875 \| 3. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.9375 \| 4. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_alert_handler_unittest.cc, score=20.8 \| 5. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=20.675 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=479.8 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=306.125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=303.425 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=292.425 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=292.25 |

### speccode_036 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `alert_handler_testplan.hjson`. The spec-side clue is `top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_testplan.hjson, top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1119.7375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=935.55 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=874.5625 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=860.3875 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=714.6125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.6875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=88.575 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.4375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=83.25 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.5 |
| spec-code | 5 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1119.7375 \| 2. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1102.8625 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1097.8875 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1094.2625 \| 5. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=1060.275 |

### speccode_037 (code_to_spec_trace, L4)

**Question**: Find the spec-side evidence that explains the code node `tb.sv` under `ip_autogen/alert_handler/dv/tb/tb.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, ip_autogen/alert_handler/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=362.5 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=360.0625 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=307.5625 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=301.0 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=288.75 |
| code-only | - | 22 | - | spec=N, code=N, joint=N | 1. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=30.625 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=30.3125 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=29.125 \| 4. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=28.3125 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=26.875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=587.5 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=372.8125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=370.5625 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=360.0625 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=346.8125 |

### speccode_038 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `alert_handler` requirement described around `theory_of_operation.md` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.775 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=256.625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=112.0 \| 4. component:system [component] @ __graphify_spec_only__/components.md, score=82.6875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=71.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=42.6 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.0 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=29.625 |
| spec-code | 1 | 23 | 23 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.775 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=401.075 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=124.4625 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=121.5375 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=112.0 |

### speccode_039 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `theory_of_operation.md` from `top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md` to the most relevant code artifact in `ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md, ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1756.6375 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1062.6875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=918.1375 \| 4. component:pinmux [component] @ __graphify_spec_only__/components.md, score=646.0125 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=639.3625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.5 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=57.6875 \| 3. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.5 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.5 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.5 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1756.6375 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1062.6875 \| 3. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=1009.325 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=918.1375 \| 5. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=914.925 |

### speccode_040 (verification_trace, L4)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `theory_of_operation.md` in the `alert_handler` area.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, alert_handler, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.25 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=259.25 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=113.575 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=84.7875 \| 5. component:system [component] @ __graphify_spec_only__/components.md, score=83.7375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=27.875 \| 2. .check() [code] @ opentitan\util\validate_testplans.py, score=24.0625 \| 3. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.4375 \| 4. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=18.375 \| 5. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_alert_handler_unittest.cc, score=17.75 |
| spec-code | 1 | 16 | 16 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.25 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=394.25 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=120.9375 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=118.6875 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=113.575 |

### speccode_041 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `theory_of_operation.md`. The spec-side clue is `top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1755.325 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1060.7625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=911.6625 \| 4. component:pinmux [component] @ __graphify_spec_only__/components.md, score=645.4 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=639.3625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.6875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.9375 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=86.85 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.75 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.0 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1755.325 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1060.7625 \| 3. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=938.35 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=911.6625 \| 5. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=909.8125 |

### speccode_042 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `tb.sv` under `ip_autogen/alert_handler/dv/tb/tb.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, ip_autogen/alert_handler/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=362.5 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=360.0625 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=307.5625 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=301.0 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=288.75 |
| code-only | - | 22 | - | spec=N, code=N, joint=N | 1. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=30.625 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=30.3125 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=29.125 \| 4. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=28.3125 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=26.875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=587.5 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=372.8125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=370.5625 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=360.0625 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=346.8125 |

### speccode_043 (requirement_to_rtl, L4)

**Question**: A reviewer asks where the `racl_ctrl` requirement described around `interfaces.md` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_base_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv:L65

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: racl_ctrl, interfaces.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=247.4625 \| 2. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=151.275 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=120.3375 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=114.1 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=109.4 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=48.7875 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=43.125 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=40.0625 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=37.0 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=247.4625 \| 2. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=237.675 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=201.7875 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=190.85 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=159.6 |

### speccode_044 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `interfaces.md` from `top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md` to the most relevant code artifact in `top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_cfg.sv`.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_env_cfg.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md, top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_cfg.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1115.3625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=933.975 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=928.9 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=825.225 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=644.4375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=70.6875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=69.6875 \| 3. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=66.25 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=65.875 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=65.875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1115.3625 \| 2. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=942.975 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=933.975 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=928.9 \| 5. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=917.925 |

### speccode_045 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `interfaces.md` in the `racl_ctrl` area.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_env_pkg.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, racl_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=247.4625 \| 2. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=152.325 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=135.1 \| 4. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=121.9125 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=115.675 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=27.8125 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=26.5625 \| 4. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 \| 5. bitfield_bit32_write() [code] @ opentitan\sw\device\lib\base\bitfield.h, score=16.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=247.4625 \| 2. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=226.575 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=166.9125 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=155.975 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=135.1 |

### speccode_046 (spec_to_code_trace, L4)

**Question**: Find the implementation-side code evidence for the spec concept `interfaces.md`. The spec-side clue is `top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_ral_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv:L11

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1111.075 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=928.2 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=906.15 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=820.4125 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=643.7375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=108.4375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=93.0375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.3125 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=86.5 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=85.4375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1111.075 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=928.2 \| 3. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=917.4625 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=906.15 \| 5. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=900.475 |

### speccode_047 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `tb.sv` under `top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=692.125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=651.0 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=575.75 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=546.0 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=467.6875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=69.0625 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=61.5625 \| 3. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=58.75 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=58.4375 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=58.4375 |
| spec-code | 9 | - | - | spec=N, code=N, joint=N | 1. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=813.8125 \| 2. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=790.0 \| 3. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=789.6875 \| 4. tlul_jtag_dtm [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=789.375 \| 5. dma [code] @ opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv, score=788.125 |

### speccode_048 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `racl_ctrl` requirement described around `theory_of_operation.md` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_base_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv:L65

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: racl_ctrl, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=901.15 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=171.0625 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=159.1875 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=149.5625 \| 5. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=148.125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=48.7875 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=43.125 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=40.0625 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=37.0 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=901.15 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=240.6375 \| 3. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=234.525 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=231.0125 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=186.9 |

### speccode_049 (bridge_disambiguation, L4)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `theory_of_operation.md` from `top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md` to the most relevant code artifact in `top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_cfg.sv`.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_env_cfg.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md, top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_cfg.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1788.4 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1115.3625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=998.55 \| 4. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=663.6875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=654.7625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=70.6875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=69.6875 \| 3. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=66.25 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=65.875 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=65.875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1788.4 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1115.3625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=998.55 \| 4. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=971.325 \| 5. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=950.325 |

### speccode_050 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `theory_of_operation.md` in the `racl_ctrl` area.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_env_pkg.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, racl_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=900.625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=172.6375 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=160.7625 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=151.1375 \| 5. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=149.175 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=28.125 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=26.5625 \| 4. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 \| 5. bitfield_bit32_write() [code] @ opentitan\sw\device\lib\base\bitfield.h, score=16.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=900.625 \| 2. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=223.425 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=205.7625 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=196.1375 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=172.6375 |

### speccode_051 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `theory_of_operation.md`. The spec-side clue is `top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_ral_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv:L11

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1787.7 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1111.075 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=970.725 \| 4. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=662.9875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=646.8875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=108.4375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=93.0375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.3125 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=86.5 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=85.4375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1787.7 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1111.075 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=970.725 \| 4. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=945.8125 \| 5. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=932.875 |

### speccode_052 (code_to_spec_trace, L4)

**Question**: Find the spec-side evidence that explains the code node `tb.sv` under `top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=692.125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=651.0 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=575.75 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=546.0 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=467.6875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=69.0625 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=61.5625 \| 3. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=58.75 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=58.4375 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=58.4375 |
| spec-code | 9 | - | - | spec=N, code=N, joint=N | 1. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=813.8125 \| 2. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=790.0 \| 3. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=789.6875 \| 4. tlul_jtag_dtm [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=789.375 \| 5. dma [code] @ opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv, score=788.125 |

### speccode_053 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `alert_handler` requirement described around `alert_handler_sec_cm_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv:L11

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler, alert_handler_sec_cm_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=329.425 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=317.7125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | 22 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=65.0 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=43.275 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 5. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.875 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=491.875 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=327.8375 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=324.275 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 |

### speccode_054 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `alert_handler_sec_cm_testplan.hjson` from `top_earlgrey/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson` to the most relevant code artifact in `top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv`.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_sec_cm_testplan.hjson, top_earlgrey/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson, top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1191.05 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=1004.85 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=927.85 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=910.0875 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=740.1625 |
| code-only | - | 20 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=107.6875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=93.25 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=92.4 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.375 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.0 |
| spec-code | 10 | 1 | 10 | spec=N, code=Y, joint=N | 1. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1490.7125 \| 2. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1486.8625 \| 3. csrng [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1386.825 \| 4. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1385.7 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1372.3 |

### speccode_055 (verification_trace, L4)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `alert_handler_sec_cm_testplan.hjson` in the `alert_handler` area.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_sec_cm_testplan.hjson, alert_handler, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=332.05 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=320.8625 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=320.5125 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=320.25 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | 7 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=65.0 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 3. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=33.1 \| 4. .check() [code] @ opentitan\util\validate_testplans.py, score=25.5 \| 5. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.9375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=485.05 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=324.3125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=321.425 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=320.8625 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=320.5125 |

### speccode_056 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `alert_handler_testplan.hjson`. The spec-side clue is `top_earlgrey/ip_autogen/alert_handler/data/alert_handler_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv:L11

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_testplan.hjson, top_earlgrey/ip_autogen/alert_handler/data/alert_handler_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1149.4875 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=961.8 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=885.7625 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=872.8125 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=732.1125 |
| code-only | - | 20 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=107.1875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=92.325 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.4375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=83.875 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=83.5625 |
| spec-code | 10 | 1 | 10 | spec=N, code=Y, joint=N | 1. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1458.1375 \| 2. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1454.5125 \| 3. csrng [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1357.55 \| 4. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1356.55 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1344.5 |

### speccode_057 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `prim_esc_pkg` under `top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_esc_pkg, top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=660.3625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=631.575 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=558.8625 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=542.4125 \| 5. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=542.3125 |
| code-only | - | 21 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.0625 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=108.025 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=89.125 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=86.125 \| 5. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=85.625 |
| spec-code | 7 | 1 | 7 | spec=N, code=Y, joint=N | 1. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1006.7375 \| 2. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1005.3 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=925.475 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=920.225 \| 5. csrng [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=910.475 |

### speccode_058 (requirement_to_rtl, L4)

**Question**: A reviewer asks where the `alert_handler` requirement described around `alert_handler_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler, alert_handler_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=324.175 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=290.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=289.975 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=289.275 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | 13 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=43.275 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.25 \| 4. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=33.1 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=486.625 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=309.65 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=306.275 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=290.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=289.975 |

### speccode_059 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `theory_of_operation.md` from `top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md` to the most relevant code artifact in `top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv`.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv:L11

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md, top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1771.5125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1080.3625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=953.575 \| 4. component:pinmux [component] @ __graphify_spec_only__/components.md, score=662.375 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=654.5875 |
| code-only | - | 17 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=107.6875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=93.25 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=91.5 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.375 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.0 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1771.5125 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1191.2375 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1187.6125 \| 4. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1102.4 \| 5. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1099.025 |

### speccode_060 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `theory_of_operation.md` in the `alert_handler` area.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, alert_handler, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.25 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=259.25 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=113.575 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=84.7875 \| 5. component:system [component] @ __graphify_spec_only__/components.md, score=83.7375 |
| code-only | - | 13 | - | spec=N, code=N, joint=N | 1. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=27.875 \| 2. .check() [code] @ opentitan\util\validate_testplans.py, score=24.0625 \| 3. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.4375 \| 4. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=18.375 \| 5. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_alert_handler_unittest.cc, score=17.75 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.25 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=394.25 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=120.9375 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=118.6875 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=113.575 |

### speccode_061 (spec_to_code_trace, L4)

**Question**: Find the implementation-side code evidence for the spec concept `theory_of_operation.md`. The spec-side clue is `top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1770.2 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1078.2625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=941.4125 \| 4. component:pinmux [component] @ __graphify_spec_only__/components.md, score=657.65 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=649.95 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=107.1875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=90.6 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.9375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=83.375 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=83.0625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1770.2 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1169.4625 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1166.5375 \| 4. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1089.1 \| 5. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1085.975 |

### speccode_062 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `prim_secded_inv_72_64_enc` under `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_ecc_reg.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: otp_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv:L39

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_secded_inv_72_64_enc, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_ecc_reg.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=727.9125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=723.1 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=691.7625 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=619.15 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=557.9875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=120.875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=119.875 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=117.8 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=113.5625 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=112.8125 |
| spec-code | 3 | 1 | 3 | spec=Y, code=Y, joint=Y | 1. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1088.75 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1078.0 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=1073.5875 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1038.9 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1036.725 |

### speccode_063 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `otp_ctrl` requirement described around `otp_ctrl_sec_cm_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: otp_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sum_tree [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_dai.sv:L944

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl, otp_ctrl_sec_cm_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=417.4625 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=412.1125 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=380.975 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=369.25 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=64.875 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=54.3 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=49.125 \| 5. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=48.6875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=601.5625 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=418.925 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=417.4625 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=416.8625 \| 5. component:opentitan [component] @ __graphify_spec_only__/components.md, score=380.975 |

### speccode_064 (bridge_disambiguation, L4)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `otp_ctrl_sec_cm_testplan.hjson` from `top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson` to the most relevant code artifact in `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`.

**Gold spec answer**: otp_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L13

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_sec_cm_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1303.1375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=1078.9625 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=989.45 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=931.175 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=845.325 |
| code-only | - | 19 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.5 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=107.3 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=103.0625 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=96.8125 \| 5. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=96.5625 |
| spec-code | 10 | - | - | spec=N, code=N, joint=N | 1. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1545.725 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1543.7875 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1532.775 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1531.6875 \| 5. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1484.75 |

### speccode_065 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `otp_ctrl_sec_cm_testplan.hjson` in the `otp_ctrl` area.

**Gold spec answer**: otp_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_util_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_sec_cm_testplan.hjson, otp_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=419.0375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=413.6875 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=384.125 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=371.35 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | 11 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=64.875 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 3. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=46.5625 \| 4. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=37.0625 \| 5. .check() [code] @ opentitan\util\validate_testplans.py, score=32.875 |
| spec-code | 1 | 28 | 28 | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=566.6875 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=419.0375 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=415.675 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=414.2375 \| 5. component:opentitan [component] @ __graphify_spec_only__/components.md, score=384.125 |

### speccode_066 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `otp_ctrl_sec_cm_testplan.hjson`. The spec-side clue is `top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: otp_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L15

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_sec_cm_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1289.3125 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=1064.4375 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=975.8 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=890.75 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=838.2375 |
| code-only | - | 19 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=113.6875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.7 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.875 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=94.3125 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=92.5625 |
| spec-code | 10 | - | - | spec=N, code=N, joint=N | 1. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1529.975 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1528.0375 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1514.95 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1514.05 \| 5. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1463.4125 |

### speccode_067 (code_to_spec_trace, L4)

**Question**: Find the spec-side evidence that explains the code node `otp_macro_pkg` under `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: otp_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl.sv:L21

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_macro_pkg, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=728.2625 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=724.2375 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=696.6625 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=618.7125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=558.5125 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=113.3125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=105.0125 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.0625 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=92.625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=90.8125 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=1087.4875 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1082.65 \| 3. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1081.9 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1041.6 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1040.7375 |

### speccode_068 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `otp_ctrl` requirement described around `otp_ctrl_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: otp_ctrl_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv:L39

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl, otp_ctrl_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=406.8625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=389.4625 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=352.5375 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=340.8125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=54.3 \| 2. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=49.125 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=48.0625 \| 4. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=46.5625 \| 5. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=45.25 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=596.3125 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=401.925 \| 3. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=401.1125 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=389.4625 \| 5. component:opentitan [component] @ __graphify_spec_only__/components.md, score=352.5375 |

### speccode_069 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `otp_ctrl_testplan.hjson` from `top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson` to the most relevant code artifact in `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_kdi.sv`.

**Gold spec answer**: otp_ctrl_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv:L275

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_kdi.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1265.6875 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=1041.425 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=951.825 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=928.375 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=839.1125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.3125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.85 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=100.6875 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=95.1875 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.5 |
| spec-code | 10 | 1 | 10 | spec=N, code=Y, joint=N | 1. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1525.725 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1521.2875 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1506.625 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1505.95 \| 5. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1465.5625 |

### speccode_070 (verification_trace, L4)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `otp_ctrl_testplan.hjson` in the `otp_ctrl` area.

**Gold spec answer**: otp_ctrl_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sum_tree [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_dai.sv:L944

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_testplan.hjson, otp_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=408.4375 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=391.0375 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=355.6875 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=342.9125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=46.5625 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=37.0625 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=32.25 \| 4. dif_otp_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_otp_ctrl.c, score=29.6 \| 5. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=29.325 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=561.4375 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=398.675 \| 3. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=398.4875 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=391.0375 \| 5. component:opentitan [component] @ __graphify_spec_only__/components.md, score=355.6875 |

### speccode_071 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `otp_ctrl_testplan.hjson`. The spec-side clue is `top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: otp_ctrl_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L13

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1255.7125 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=1030.4 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=941.7625 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=890.75 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=832.6375 |
| code-only | - | 17 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=113.6875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.7 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.875 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=93.5625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=92.5625 |
| spec-code | 10 | - | - | spec=N, code=N, joint=N | 1. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1509.825 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1509.1375 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1494.475 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1493.8 \| 5. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1448.5625 |

### speccode_072 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `prim_util_pkg` under `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: otp_ctrl_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_util_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_util_pkg, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=731.7625 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=723.1 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=694.125 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=618.7125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=585.375 |
| code-only | - | 24 | - | spec=N, code=N, joint=N | 1. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=151.6875 \| 2. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=136.1875 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=120.125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=119.65 \| 5. .append() [code] @ opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py, score=115.25 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=1088.55 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1081.6 \| 3. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1079.5375 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1044.65 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1042.25 |

### speccode_073 (requirement_to_rtl, L4)

**Question**: A reviewer asks where the `otp_ctrl` requirement described around `otp_ctrl_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: otp_ctrl_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L15

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl, otp_ctrl_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=406.8625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=389.4625 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=352.5375 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=340.8125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=54.3 \| 2. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=49.125 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=48.0625 \| 4. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=46.5625 \| 5. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=45.25 |
| spec-code | 1 | 26 | 26 | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=596.3125 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=401.925 \| 3. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=401.1125 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=389.4625 \| 5. component:opentitan [component] @ __graphify_spec_only__/components.md, score=352.5375 |

### speccode_074 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `otp_ctrl_testplan.hjson` from `top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson` to the most relevant code artifact in `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl.sv`.

**Gold spec answer**: otp_ctrl_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl.sv:L21

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1265.95 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=1041.6875 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=952.0875 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=928.375 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=839.375 |
| code-only | - | 15 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.4375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.925 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=100.6875 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=95.3125 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.5 |
| spec-code | 10 | - | - | spec=N, code=N, joint=N | 1. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1522.65 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1521.9625 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1506.85 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1506.175 \| 5. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1465.7875 |

### speccode_075 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `interfaces.md` in the `otp_ctrl` area.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv:L39

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, otp_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=327.4125 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=268.9 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=146.0375 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=144.9875 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=114.9125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=31.5625 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=31.5625 \| 4. dif_otp_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_otp_ctrl.c, score=25.25 \| 5. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=462.4125 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=268.9 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=182.825 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=182.5125 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=159.9125 |

### speccode_076 (spec_to_code_trace, L4)

**Question**: Find the implementation-side code evidence for the spec concept `interfaces.md`. The spec-side clue is `top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv:L275

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1139.5125 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=971.075 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=965.2125 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=857.6 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=778.3875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=112.1875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=100.5375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=93.25 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=90.0625 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.75 |
| spec-code | 5 | 1 | 5 | spec=Y, code=Y, joint=Y | 1. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1192.25 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1191.3125 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1157.2 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1156.525 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=1139.5125 |

### speccode_077 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `prim_sum_tree` under `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_dai.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sum_tree [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_dai.sv:L944

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_sum_tree, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_dai.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=727.9125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=723.1 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=691.7625 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=622.65 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=557.9875 |
| code-only | - | 30 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=119.9375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=118.175 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=99.3125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.5 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=94.75 |
| spec-code | 3 | - | - | spec=Y, code=N, joint=N | 1. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1078.0 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1075.9375 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=1056.7125 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1038.9 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1036.725 |

### speccode_078 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `otp_ctrl` requirement described around `interfaces.md` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L13

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl, interfaces.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=325.8375 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=268.9 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=143.4125 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=113.3375 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=107.1875 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=52.5375 \| 2. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=46.3125 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=46.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=44.375 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 |
| spec-code | 1 | 8 | 8 | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=497.2875 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=268.9 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=194.7875 \| 4. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=186.075 \| 5. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=185.1375 |

### speccode_079 (bridge_disambiguation, L4)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `interfaces.md` from `top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md` to the most relevant code artifact in `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_util_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1144.7625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=998.8125 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=971.775 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=862.9375 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=805.775 |
| code-only | - | 17 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.5 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=106.4 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=103.0625 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=96.8125 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=96.375 |
| spec-code | 3 | - | - | spec=Y, code=N, joint=N | 1. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1235.1 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1234.4125 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=1216.85 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1192.125 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1191.2625 |

### speccode_080 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `interfaces.md` in the `otp_ctrl` area.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L15

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, otp_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=327.4125 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=268.9 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=146.0375 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=144.9875 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=114.9125 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=31.5625 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=31.5625 \| 4. dif_otp_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_otp_ctrl.c, score=25.25 \| 5. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 |
| spec-code | 1 | 9 | 9 | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=462.4125 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=268.9 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=182.825 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=182.5125 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=159.9125 |

### speccode_081 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `interfaces.md`. The spec-side clue is `top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl.sv:L21

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1139.5125 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=971.075 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=965.2125 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=857.6 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=778.3875 |
| code-only | - | 13 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=112.1875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=100.5375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=93.25 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=90.0625 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.75 |
| spec-code | 5 | - | - | spec=Y, code=N, joint=N | 1. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1192.25 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1191.3125 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1157.2 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1156.525 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=1139.5125 |

### speccode_082 (code_to_spec_trace, L4)

**Question**: Find the spec-side evidence that explains the code node `prim_secded_inv_72_64_enc` under `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_ecc_reg.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv:L39

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_secded_inv_72_64_enc, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_ecc_reg.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=727.9125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=723.1 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=691.7625 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=619.15 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=557.9875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=120.875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=119.875 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=117.8 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=113.5625 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=112.8125 |
| spec-code | 3 | 1 | 3 | spec=Y, code=Y, joint=Y | 1. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1088.75 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1078.0 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=1073.5875 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1038.9 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1036.725 |

### speccode_083 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `otp_ctrl` requirement described around `theory_of_operation.md` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv:L275

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=929.15 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=364.6875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=200.375 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=153.5 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=121.5625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=52.5375 \| 2. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=46.3125 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=46.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=44.375 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=929.15 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=536.1375 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=234.95 \| 4. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=217.125 \| 5. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=216.1875 |

### speccode_084 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `theory_of_operation.md` from `top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md` to the most relevant code artifact in `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_dai.sv`.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sum_tree [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_dai.sv:L944

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_dai.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1831.275 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1144.7625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1059.5375 \| 4. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=845.4125 \| 5. component:opentitan [component] @ __graphify_spec_only__/components.md, score=687.575 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.3125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=105.075 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=100.6875 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=97.0625 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.5 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1831.275 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1266.6 \| 3. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1265.9125 \| 4. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=1230.3875 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1227.4 |

### speccode_085 (verification_trace, L4)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `theory_of_operation.md` in the `otp_ctrl` area.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L13

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, otp_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=928.625 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=366.2625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=201.95 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=155.075 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=146.0375 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=31.875 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=31.5625 \| 4. dif_otp_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_otp_ctrl.c, score=25.25 \| 5. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 |
| spec-code | 1 | 15 | 15 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=928.625 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=501.2625 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=213.875 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=213.5625 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=201.95 |

### speccode_086 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `theory_of_operation.md`. The spec-side clue is `top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_util_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1830.575 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1139.5125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1029.7875 \| 4. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=818.6375 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=686.6125 |
| code-only | - | 16 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=112.1875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=100.5375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=93.25 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=90.0625 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.75 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1830.575 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1227.35 \| 3. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1226.4125 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1198.15 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1197.475 |

### speccode_087 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `otp_ctrl_macro_pkg` under `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L15

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_macro_pkg, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=737.275 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=726.075 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=698.7625 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=618.8 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=586.3375 |
| code-only | - | 16 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=113.875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=106.5875 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=101.0 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=95.0625 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.8125 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=1117.9375 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1090.875 \| 3. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1090.1875 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1048.425 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1047.525 |

### speccode_088 (requirement_to_rtl, L4)

**Question**: A reviewer asks where the `otp_ctrl` requirement described around `theory_of_operation.md` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl.sv:L21

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=929.15 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=364.6875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=200.375 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=153.5 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=121.5625 |
| code-only | - | 20 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=52.5375 \| 2. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=46.3125 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=46.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=44.375 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 |
| spec-code | 1 | 24 | 24 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=929.15 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=536.1375 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=234.95 \| 4. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=217.125 \| 5. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=216.1875 |

### speccode_089 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `flash_ctrl_sec_cm_testplan.hjson` from `top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson` to the most relevant code artifact in `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_arbiter_tree [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L163

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1196.825 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=996.5375 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=916.5625 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=898.8 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=812.425 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=112.9375 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=105.75 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=101.75 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.5625 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.1875 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1222.6 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1196.825 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1112.7 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1111.8 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1056.85 |

### speccode_090 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `flash_ctrl_sec_cm_testplan.hjson` in the `flash_ctrl` area.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv:L240

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_sec_cm_testplan.hjson, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=404.2375 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=398.2125 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=369.425 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=360.2375 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | 15 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=63.75 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=60.4375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 4. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=58.65 \| 5. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=52.85 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=557.2375 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=398.2125 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=369.425 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=360.2375 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=339.1 |

### speccode_091 (spec_to_code_trace, L4)

**Question**: Find the implementation-side code evidence for the spec concept `flash_ctrl_sec_cm_testplan.hjson`. The spec-side clue is `top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_72_64_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L775

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1189.3 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=987.7875 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=908.95 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=864.15 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=805.1625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=110.5375 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=105.3125 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=96.9375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.0625 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=90.75 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1210.6125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1189.3 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1107.3 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1106.4 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1052.125 |

### speccode_092 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `prim_secded_hamming_76_68_enc` under `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_prog.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv:L334

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_secded_hamming_76_68_enc, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_prog.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=671.5625 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=637.6875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=622.65 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=580.5625 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=526.925 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=122.8125 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=110.9375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.375 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.4375 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=90.375 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1025.1375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=757.0875 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=739.6625 \| 4. prim_secded_hamming_72_64_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv, score=686.225 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=680.1375 |

### speccode_093 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `flash_ctrl` requirement described around `flash_ctrl_sec_cm_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_dec [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L435

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl, flash_ctrl_sec_cm_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=402.6625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=396.6375 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=366.275 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=358.1375 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=63.75 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=60.4375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=59.4375 \| 5. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=58.65 |
| spec-code | 1 | 16 | 16 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=592.1125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=396.6375 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=366.275 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=358.1375 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=342.35 |

### speccode_094 (bridge_disambiguation, L4)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `flash_ctrl_sec_cm_testplan.hjson` from `top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson` to the most relevant code artifact in `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy.sv`.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_ctrl_top_specific_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv:L14

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1196.825 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=996.5375 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=916.5625 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=898.8 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=812.425 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=112.9375 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=105.75 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=101.75 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.5625 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.1875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1222.6 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1196.825 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1112.7 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1111.8 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1056.85 |

### speccode_095 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `flash_ctrl_sec_cm_testplan.hjson` in the `flash_ctrl` area.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_phy_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_scramble.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_sec_cm_testplan.hjson, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=404.2375 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=398.2125 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=369.425 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=360.2375 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | 24 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=63.75 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=60.4375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 4. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=58.65 \| 5. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=52.85 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=557.2375 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=398.2125 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=369.425 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=360.2375 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=339.1 |

### speccode_096 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `flash_ctrl_sec_cm_testplan.hjson`. The spec-side clue is `top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: rst_shadowed_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv:L50

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1189.3 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=987.7875 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=908.95 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=864.15 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=805.1625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=110.5375 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=105.3125 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=96.9375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.0625 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=90.75 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1210.6125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1189.3 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1107.3 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1106.4 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1052.125 |

### speccode_097 (code_to_spec_trace, L4)

**Question**: Find the spec-side evidence that explains the code node `prim_arbiter_tree` under `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_arbiter_tree [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L163

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_arbiter_tree, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=671.5625 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=637.6875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=622.65 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=584.5 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=526.925 |
| code-only | - | 28 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=123.375 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=110.9375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.375 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.4375 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=90.375 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1022.8875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=757.65 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=738.725 \| 4. prim_arbiter_tree [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv, score=685.85 \| 5. prim_secded_hamming_72_64_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv, score=681.5375 |

### speccode_098 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `flash_ctrl` requirement described around `flash_ctrl_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv:L240

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl, flash_ctrl_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=398.725 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=369.075 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=338.275 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=330.1375 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | 5 | - | spec=N, code=Y, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=60.4375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=59.4375 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=58.65 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=53.075 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=48.4375 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=588.175 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=369.075 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=338.275 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=330.1375 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=326.475 |

### speccode_099 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `flash_ctrl_testplan.hjson` from `top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson` to the most relevant code artifact in `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_72_64_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L775

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1163.75 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=963.025 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=898.8 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=883.05 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=808.225 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=112.9375 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=105.75 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=101.75 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.5625 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.1875 |
| spec-code | 1 | 15 | 15 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1218.4 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1163.75 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1092.225 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1091.55 \| 5. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1040.1625 |

### speccode_100 (verification_trace, L4)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `flash_ctrl_testplan.hjson` in the `flash_ctrl` area.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv:L334

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_testplan.hjson, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=400.3 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=370.65 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=341.425 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=332.2375 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=60.4375 \| 2. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=58.65 \| 3. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=52.85 \| 4. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=42.6875 \| 5. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl_unittest.cc, score=38.05 |
| spec-code | 1 | 20 | 20 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=553.3 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=370.65 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=341.425 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=332.2375 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=323.225 |

### speccode_101 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `flash_ctrl_testplan.hjson`. The spec-side clue is `top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_dec [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L435

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1156.225 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=954.275 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=875.4375 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=864.15 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=800.9625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=110.5375 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=105.3125 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=96.9375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.0625 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=90.75 |
| spec-code | 1 | 15 | 15 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1206.4125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1156.225 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1086.825 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1086.15 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1033.325 |

### speccode_102 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `flash_ctrl_top_specific_pkg` under `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_ctrl_top_specific_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv:L14

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_top_specific_pkg, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=674.0125 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=650.2 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=630.525 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=580.9125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=559.3 |
| code-only | - | 12 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=113.6625 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=105.0 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=100.625 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.625 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.25 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1066.0 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=753.3375 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=746.55 \| 4. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=689.9125 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=687.2 |

### speccode_103 (requirement_to_rtl, L4)

**Question**: A reviewer asks where the `flash_ctrl` requirement described around `flash_ctrl_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_phy_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_scramble.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl, flash_ctrl_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=398.725 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=369.075 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=338.275 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=330.1375 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | 28 | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=60.4375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=59.4375 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=58.65 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=53.075 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=48.4375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=588.175 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=369.075 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=338.275 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=330.1375 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=326.475 |

### speccode_104 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `flash_ctrl_testplan.hjson` from `top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson` to the most relevant code artifact in `ip_autogen/flash_ctrl/dv/tb/tb.sv`.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: rst_shadowed_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv:L50

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson, ip_autogen/flash_ctrl/dv/tb/tb.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1158.5 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=958.125 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=878.0625 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=864.15 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=803.7625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=71.7625 \| 2. .ok() [code] @ opentitan\sw\host\opentitanlib\src\transport\mod.rs, score=67.875 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=66.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=66.125 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=64.625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1172.7625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1158.5 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1084.425 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1084.425 \| 5. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1032.575 |

### speccode_105 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `interfaces.md` in the `flash_ctrl` area.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_arbiter_tree [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L163

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=306.4125 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=263.65 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=145.6 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=127.05 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=124.975 |
| code-only | - | 30 | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 2. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 3. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.625 \| 4. .check() [code] @ opentitan\util\validate_testplans.py, score=37.1875 \| 5. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 |
| spec-code | 1 | 11 | 11 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=441.4125 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=263.65 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=169.975 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=145.6 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=131.0375 |

### speccode_106 (spec_to_code_trace, L4)

**Question**: Find the implementation-side code evidence for the spec concept `interfaces.md`. The spec-side clue is `top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv:L240

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1090.075 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=932.575 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=871.15 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=818.225 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=719.2375 |
| code-only | - | 8 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=105.475 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.0625 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.1875 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.6875 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.375 |
| spec-code | 1 | 6 | 6 | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1090.075 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1088.6875 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=932.575 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=871.15 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=846.85 |

### speccode_107 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `prim_secded_hamming_72_64_enc` under `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_72_64_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L775

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_secded_hamming_72_64_enc, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=671.5625 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=637.6875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=622.65 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=580.5625 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=526.925 |
| code-only | - | 27 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=123.375 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=110.9375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.375 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.4375 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=90.375 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1022.8875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=757.65 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=738.725 \| 4. prim_secded_hamming_72_64_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv, score=687.7875 \| 5. prim_arbiter_tree [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv, score=680.85 |

### speccode_108 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `flash_ctrl` requirement described around `interfaces.md` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv:L334

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl, interfaces.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=304.8375 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=263.65 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=125.475 \| 4. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=123.4 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 16 | 16 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=476.2875 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=263.65 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=204.85 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=169.6625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=137.3625 |

### speccode_109 (bridge_disambiguation, L4)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `interfaces.md` from `top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md` to the most relevant code artifact in `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_dec [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L435

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1093.1375 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=933.8875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=889.35 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=821.8125 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=744.0875 |
| code-only | - | 30 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=110.9875 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=105.25 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=100.625 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.625 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.25 |
| spec-code | 1 | 10 | 10 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1145.2625 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1093.1375 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=933.8875 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=889.35 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=864.0625 |

### speccode_110 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `interfaces.md` in the `flash_ctrl` area.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_ctrl_top_specific_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv:L14

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=306.4125 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=263.65 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=145.6 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=127.05 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=124.975 |
| code-only | - | 8 | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 2. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 3. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.625 \| 4. .check() [code] @ opentitan\util\validate_testplans.py, score=37.1875 \| 5. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 |
| spec-code | 1 | 10 | 10 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=441.4125 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=263.65 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=169.975 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=145.6 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=131.0375 |

### speccode_111 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `interfaces.md`. The spec-side clue is `top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_phy_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_scramble.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1090.075 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=932.575 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=871.15 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=818.225 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=719.2375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=105.475 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.0625 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.1875 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.6875 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1090.075 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1088.6875 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=932.575 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=871.15 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=846.85 |

### speccode_112 (code_to_spec_trace, L4)

**Question**: Find the spec-side evidence that explains the code node `rst_shadowed_if` under `ip_autogen/flash_ctrl/dv/tb/tb.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: rst_shadowed_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv:L50

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rst_shadowed_if, ip_autogen/flash_ctrl/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=457.0 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=421.75 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=374.5 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=364.4375 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=316.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.8125 \| 2. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 3. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.8125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=44.5 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=42.8125 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=682.0 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=421.75 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=418.875 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=378.3125 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=378.0 |

### speccode_113 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `flash_ctrl` requirement described around `theory_of_operation.md` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_arbiter_tree [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L163

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=925.65 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=345.0 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=182.4375 \| 4. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=162.25 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=112.8125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 10 | 10 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=925.65 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=516.45 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=243.7 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=196.9625 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=182.4375 |

### speccode_114 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `theory_of_operation.md` from `top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md` to the most relevant code artifact in `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_core.sv`.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv:L240

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_core.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1810.8875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1113.7 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=969.675 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=786.7875 \| 5. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=710.9625 |
| code-only | - | 8 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=114.1125 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=106.8125 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=103.75 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=97.75 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=97.0625 |
| spec-code | 1 | 7 | 7 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1810.8875 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1192.4625 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=1113.7 \| 4. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=979.3875 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=969.675 |

### speccode_115 (verification_trace, L4)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `theory_of_operation.md` in the `flash_ctrl` area.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_72_64_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L775

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=925.125 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=346.575 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=184.0125 \| 4. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=163.825 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=145.6 |
| code-only | - | 30 | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 2. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 3. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.625 \| 4. .check() [code] @ opentitan\util\validate_testplans.py, score=37.1875 \| 5. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.875 |
| spec-code | 1 | 10 | 10 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=925.125 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=481.575 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=208.825 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=184.0125 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=158.3375 |

### speccode_116 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `theory_of_operation.md`. The spec-side clue is `top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv:L334

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1792.075 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1090.075 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=935.725 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=761.0625 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=660.8 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=105.475 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.0625 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.1875 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.6875 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.375 |
| spec-code | 1 | 21 | 21 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1792.075 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1130.5125 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=1090.075 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=935.725 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=883.3 |

### speccode_117 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `prim_secded_hamming_76_68_dec` under `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_dec [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L435

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_secded_hamming_76_68_dec, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=671.5625 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=637.6875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=622.65 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=580.5625 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=526.925 |
| code-only | - | 28 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=126.375 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=110.9375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.375 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.4375 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=90.375 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1022.8875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=760.65 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=738.725 \| 4. prim_secded_hamming_72_64_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv, score=685.2875 \| 5. prim_arbiter_tree [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv, score=680.85 |

### speccode_118 (requirement_to_rtl, L4)

**Question**: A reviewer asks where the `flash_ctrl` requirement described around `theory_of_operation.md` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_ctrl_top_specific_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv:L14

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=925.65 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=345.0 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=182.4375 \| 4. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=162.25 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=112.8125 |
| code-only | - | 15 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 16 | 16 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=925.65 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=516.45 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=243.7 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=196.9625 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=182.4375 |

### speccode_119 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `theory_of_operation.md` from `top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md` to the most relevant code artifact in `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_scramble.sv`.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_phy_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_scramble.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_scramble.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1793.3875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1093.1375 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=953.925 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=785.9125 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=661.0625 |
| code-only | - | 24 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=110.425 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=105.25 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=100.625 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.625 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.25 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1793.3875 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1187.0875 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=1093.1375 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=953.925 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=899.95 |

### speccode_120 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `theory_of_operation.md` in the `flash_ctrl` area.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: rst_shadowed_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv:L50

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=925.125 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=346.575 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=184.0125 \| 4. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=163.825 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=145.6 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 2. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 3. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.625 \| 4. .check() [code] @ opentitan\util\validate_testplans.py, score=37.1875 \| 5. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.875 |
| spec-code | 1 | 24 | 24 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=925.125 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=481.575 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=208.825 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=184.0125 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=158.3375 |

### speccode_121 (spec_to_code_trace, L4)

**Question**: Find the implementation-side code evidence for the spec concept `rv_core_ibex_sec_cm_testplan.hjson`. The spec-side clue is `top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L905

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1144.5875 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=968.875 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=960.6625 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=889.9625 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=854.175 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=368.0 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=108.0 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.2875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.25 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1361.275 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1144.5875 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=1086.4125 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1061.175 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1059.375 |

### speccode_122 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `prim_esc_receiver` under `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L283

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_esc_receiver, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=815.925 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=628.5125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=592.725 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=544.6875 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=523.6 |
| code-only | - | 3 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.8125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=118.65 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.6875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.8125 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1192.125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=846.525 \| 3. prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=761.25 \| 4. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=761.0 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=678.2625 |

### speccode_123 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `rv_core_ibex` requirement described around `rv_core_ibex_sec_cm_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv:L58

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex, rv_core_ibex_sec_cm_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=485.6125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=355.8625 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=341.6875 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=341.425 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=203.4375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=365.3125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=69.0625 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=684.5125 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=365.3125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=355.8625 \| 4. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 5. component:opentitan [component] @ __graphify_spec_only__/components.md, score=341.6875 |

### speccode_124 (bridge_disambiguation, L4)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `rv_core_ibex_sec_cm_testplan.hjson` from `top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson` to the most relevant code artifact in `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sync_reqack_data [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L376

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1152.55 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=976.8375 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=969.9375 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=898.1875 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=888.825 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=367.75 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=108.8125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.8375 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=97.0625 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1374.4125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1152.55 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=1097.5375 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1066.8 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1065.0 |

### speccode_125 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `rv_core_ibex_sec_cm_testplan.hjson` in the `rv_core_ibex` area.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sync [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L325

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_sec_cm_testplan.hjson, rv_core_ibex, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=488.7625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=357.4375 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=344.8375 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=343.525 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=203.4375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=365.3125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=67.1875 |
| spec-code | 1 | 12 | 12 | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=641.7625 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=365.3125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=357.4375 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=344.8375 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=343.525 |

### speccode_126 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `rv_core_ibex_sec_cm_testplan.hjson`. The spec-side clue is `top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sender [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L406

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1144.5875 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=968.875 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=960.6625 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=889.9625 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=854.175 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=368.0 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=108.0 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.2875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.25 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1361.275 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1144.5875 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=1086.4125 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1061.175 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1059.375 |

### speccode_127 (code_to_spec_trace, L4)

**Question**: Find the spec-side evidence that explains the code node `tlul_adapter_host` under `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: tlul_adapter_host [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L668

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tlul_adapter_host, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=815.925 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=634.2 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=591.85 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=549.5 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=521.85 |
| code-only | - | 11 | - | spec=N, code=N, joint=N | 1. .ok() [code] @ opentitan\sw\host\opentitanlib\src\transport\mod.rs, score=591.3125 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=310.0 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 4. .write() [code] @ opentitan\sw\host\penetrationtests\python\util\targets.py, score=167.875 \| 5. .new() [code] @ opentitan\sw\host\tests\xmodem\xmodem.rs, score=149.625 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1192.125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=834.775 \| 3. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=758.5 \| 4. prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=753.75 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=678.2625 |

### speccode_128 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `rv_core_ibex` requirement described around `rv_core_ibex_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L905

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex, rv_core_ibex_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=480.3625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=328.3 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=313.6875 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=313.425 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=203.4375 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=305.3125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=68.75 |
| spec-code | 1 | 6 | 6 | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=679.2625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=328.3 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=313.6875 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=313.425 \| 5. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=305.3125 |

### speccode_129 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `rv_core_ibex_testplan.hjson` from `top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson` to the most relevant code artifact in `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L283

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1119.475 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=971.325 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=936.425 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=888.825 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=864.675 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=307.75 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=108.8125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.8375 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=97.0625 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1368.9 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1119.475 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=1081.3375 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1046.325 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1044.75 |

### speccode_130 (verification_trace, L4)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `rv_core_ibex_testplan.hjson` in the `rv_core_ibex` area.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv:L58

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_testplan.hjson, rv_core_ibex, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=483.5125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=329.875 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=316.8375 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=315.525 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=203.4375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=305.3125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=66.875 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=636.5125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=329.875 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=316.8375 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=315.525 \| 5. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=305.3125 |

### speccode_131 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `rv_core_ibex_testplan.hjson`. The spec-side clue is `top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sync_reqack_data [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L376

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1111.5125 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=963.3625 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=927.15 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=856.45 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=854.175 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=308.0 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=108.0 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.2875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.25 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1355.7625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1111.5125 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=1070.2125 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1040.7 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1039.125 |

### speccode_132 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `prim_sec_anchor_buf` under `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sec_anchor_buf [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L359

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_sec_anchor_buf, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=822.4875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=628.5125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=618.1 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=544.6875 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=521.85 |
| code-only | - | 3 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=362.8125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=118.8375 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.6875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.8125 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1198.6875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=860.2125 \| 3. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=774.5 \| 4. prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=769.75 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=688.7625 |

### speccode_133 (requirement_to_rtl, L4)

**Question**: A reviewer asks where the `rv_core_ibex` requirement described around `rv_core_ibex_testplan.hjson` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sync [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L325

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex, rv_core_ibex_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=480.3625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=328.3 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=313.6875 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=313.425 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=203.4375 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=305.3125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=68.75 |
| spec-code | 1 | 6 | 6 | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=679.2625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=328.3 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=313.6875 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=313.425 \| 5. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=305.3125 |

### speccode_134 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `rv_core_ibex_testplan.hjson` from `top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson` to the most relevant code artifact in `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sender [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L406

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1119.475 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=971.325 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=936.425 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=888.825 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=864.675 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=307.75 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=108.8125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.8375 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=97.0625 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1368.9 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1119.475 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=1081.3375 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1046.325 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1044.75 |

### speccode_135 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `rv_core_ibex_testplan.hjson` in the `rv_core_ibex` area.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: tlul_adapter_host [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L668

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_testplan.hjson, rv_core_ibex, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=483.5125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=329.875 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=316.8375 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=315.525 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=203.4375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=305.3125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=66.875 |
| spec-code | 1 | 11 | 11 | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=636.5125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=329.875 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=316.8375 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=315.525 \| 5. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=305.3125 |

### speccode_136 (spec_to_code_trace, L4)

**Question**: Find the implementation-side code evidence for the spec concept `interfaces.md`. The spec-side clue is `top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L905

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1045.8875 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=909.2 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=897.1375 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=837.4625 \| 5. component:interfaces [component] @ __graphify_spec_only__/components.md, score=781.0375 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=255.625 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=106.5625 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=100.7875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.0625 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1265.6 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1045.8875 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=929.9125 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=897.1375 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=858.75 |

### speccode_137 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `prim_esc_receiver` under `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L283

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_esc_receiver, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=815.925 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=628.5125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=592.725 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=544.6875 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=523.6 |
| code-only | - | 3 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.8125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=118.65 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.6875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.8125 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1192.125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=846.525 \| 3. prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=761.25 \| 4. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=761.0 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=678.2625 |

### speccode_138 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `rv_core_ibex` requirement described around `interfaces.md` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv:L58

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex, interfaces.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=387.4375 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=226.4625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=91.7875 \| 4. component:security [component] @ __graphify_spec_only__/components.md, score=72.1 \| 5. component:boot [component] @ __graphify_spec_only__/components.md, score=70.525 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.625 |
| spec-code | 1 | 6 | 6 | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=568.3375 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=226.4625 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=182.8125 |

### speccode_139 (bridge_disambiguation, L4)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `interfaces.md` from `top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md` to the most relevant code artifact in `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sync_reqack_data [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L376

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1048.95 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=938.075 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=897.6625 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=850.5 \| 5. component:interfaces [component] @ __graphify_spec_only__/components.md, score=785.15 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.5625 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=108.8125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=103.9375 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=97.0625 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1335.65 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1048.95 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=955.3375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=897.6625 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=882.4 |

### speccode_140 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `interfaces.md` in the `rv_core_ibex` area.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sec_anchor_buf [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L359

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, rv_core_ibex, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=390.5875 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=226.4625 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=101.4125 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=93.3625 \| 5. component:security [component] @ __graphify_spec_only__/components.md, score=73.15 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=63.75 |
| spec-code | 1 | 5 | 5 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=525.5875 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=226.4625 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=143.9625 |

### speccode_141 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `interfaces.md`. The spec-side clue is `top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sync [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L325

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1045.8875 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=909.2 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=897.1375 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=837.4625 \| 5. component:interfaces [component] @ __graphify_spec_only__/components.md, score=781.0375 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=255.625 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=106.5625 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=100.7875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.0625 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1265.6 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1045.8875 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=929.9125 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=897.1375 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=858.75 |

### speccode_142 (code_to_spec_trace, L4)

**Question**: Find the spec-side evidence that explains the code node `prim_lc_sender` under `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sender [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L406

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_lc_sender, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=815.925 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=628.5125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=590.5375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=544.6875 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=521.85 |
| code-only | - | 3 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.8125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=121.275 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.6875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.8125 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1192.125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=849.15 \| 3. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=761.0 \| 4. prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=756.25 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=678.2625 |

### speccode_143 (requirement_to_rtl, L5)

**Question**: A reviewer asks where the `rv_core_ibex` requirement described around `interfaces.md` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: tlul_adapter_host [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L668

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex, interfaces.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=387.4375 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=226.4625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=91.7875 \| 4. component:security [component] @ __graphify_spec_only__/components.md, score=72.1 \| 5. component:boot [component] @ __graphify_spec_only__/components.md, score=70.525 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.625 |
| spec-code | 1 | 5 | 5 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=568.3375 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=226.4625 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=182.8125 |

### speccode_144 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `theory_of_operation.md` from `top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md` to the most relevant code artifact in `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L905

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1757.1625 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1048.95 \| 3. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=988.125 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=915.075 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=649.775 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.5625 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=108.8125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=103.9375 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=97.0625 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1757.1625 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1385.7 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=1048.95 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=991.7875 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=918.85 |

### speccode_145 (verification_trace, L4)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `theory_of_operation.md` in the `rv_core_ibex` area.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L283

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, rv_core_ibex, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=889.6875 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=439.15 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=150.325 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=101.4125 \| 5. component:system [component] @ __graphify_spec_only__/components.md, score=98.6125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=63.4375 |
| spec-code | 1 | 5 | 5 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=889.6875 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=574.15 \| 3. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 4. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=175.6875 |

### speccode_146 (spec_to_code_trace, L5)

**Question**: Find the implementation-side code evidence for the spec concept `theory_of_operation.md`. The spec-side clue is `top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md` and the expected answer should include the connected RTL/code node, not just the document node.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv:L58

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1756.6375 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1045.8875 \| 3. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=959.25 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=902.0375 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=644.9625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=255.625 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=106.5625 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=100.7875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.0625 |
| spec-code | 1 | 6 | 6 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1756.6375 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1315.65 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=1045.8875 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=966.3625 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=902.0375 |

### speccode_147 (code_to_spec_trace, L5)

**Question**: Find the spec-side evidence that explains the code node `prim_sync_reqack_data` under `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`. Return the relevant spec/document node as well as the code node so traceability can be checked.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sync_reqack_data [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L376

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_sync_reqack_data, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=864.925 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=744.5375 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=657.9125 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=653.8875 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=552.65 |
| code-only | - | 3 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=303.75 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=122.025 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=118.75 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.8125 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1241.125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=919.65 \| 3. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=830.75 \| 4. prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=826.0 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=759.2 |

### speccode_148 (requirement_to_rtl, L4)

**Question**: A reviewer asks where the `rv_core_ibex` requirement described around `theory_of_operation.md` is implemented. Retrieve both the spec node and the RTL/code node connected by the spec-code graph.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sec_anchor_buf [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L359

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=890.2125 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=436.0 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=148.75 \| 4. component:boot [component] @ __graphify_spec_only__/components.md, score=97.5625 \| 5. component:system [component] @ __graphify_spec_only__/components.md, score=97.5625 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.3125 |
| spec-code | 1 | 5 | 5 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=890.2125 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=616.9 \| 3. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 4. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=214.5375 |

### speccode_149 (bridge_disambiguation, L5)

**Question**: Use the graph bridge, not only lexical filename matching: connect spec clue `theory_of_operation.md` from `top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md` to the most relevant code artifact in `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sync [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L325

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1757.1625 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1048.95 \| 3. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=988.125 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=915.075 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=649.775 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.5625 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=108.8125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=103.9375 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=97.0625 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1757.1625 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1385.7 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=1048.95 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=991.7875 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=918.85 |

### speccode_150 (verification_trace, L5)

**Question**: For verification or review, identify the spec/document anchor and code artifact that should be inspected together for `theory_of_operation.md` in the `rv_core_ibex` area.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sender [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L406

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, rv_core_ibex, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=889.6875 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=439.15 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=150.325 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=101.4125 \| 5. component:system [component] @ __graphify_spec_only__/components.md, score=98.6125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=63.4375 |
| spec-code | 1 | 5 | 5 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=889.6875 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=574.15 \| 3. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 4. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=175.6875 |

