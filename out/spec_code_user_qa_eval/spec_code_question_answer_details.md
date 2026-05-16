# Spec-Code KG Evaluation Details

- Questions: 150
- Variants: spec-only, code-only, spec-code
- Each item includes the benchmark question, gold answers, and the actual top retrieved nodes.

## Summary Table

| Task | Type | Best@10 | Gold Bridge |
|---|---|---|---|
| userqa_001 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_002 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_003 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_004 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_005 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_006 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_007 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_008 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_009 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_010 | user_verification_coverage | spec-only | spec_path_matches_code_path |
| userqa_011 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_012 | user_disambiguation | spec-only | spec_path_matches_code_path |
| userqa_013 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_014 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_015 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_016 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_017 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_018 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_019 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_020 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_021 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_022 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_023 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_024 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_025 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_026 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_027 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_028 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_029 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_030 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_031 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_032 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_033 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_034 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_035 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_036 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_037 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_038 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_039 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_040 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_041 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_042 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_043 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_044 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_045 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_046 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_047 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_048 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_049 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_050 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_051 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_052 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_053 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_054 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_055 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_056 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_057 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_058 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_059 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_060 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_061 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_062 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_063 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_064 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_065 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_066 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_067 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_068 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_069 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_070 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_071 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_072 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_073 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_074 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_075 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_076 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_077 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_078 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_079 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_080 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_081 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_082 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_083 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_084 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_085 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_086 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_087 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_088 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_089 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_090 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_091 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_092 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_093 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_094 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_095 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_096 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_097 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_098 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_099 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_100 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_101 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_102 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_103 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_104 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_105 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_106 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_107 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_108 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_109 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_110 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_111 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_112 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_113 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_114 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_115 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_116 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_117 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_118 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_119 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_120 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_121 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_122 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_123 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_124 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_125 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_126 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_127 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_128 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_129 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_130 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_131 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_132 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_133 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_134 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_135 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_136 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_137 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_138 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_139 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_140 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_141 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_142 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_143 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_144 | user_disambiguation | spec-code | spec_path_matches_code_path |
| userqa_145 | user_spec_to_code_explain | spec-code | spec_path_matches_code_path |
| userqa_146 | user_code_to_spec_why | spec-code | spec_path_matches_code_path |
| userqa_147 | user_review_trace | spec-code | spec_path_matches_code_path |
| userqa_148 | user_verification_coverage | spec-code | spec_path_matches_code_path |
| userqa_149 | user_change_impact | spec-code | spec_path_matches_code_path |
| userqa_150 | user_disambiguation | spec-code | spec_path_matches_code_path |

## Detailed Questions

### userqa_001 (user_spec_to_code_explain, L4)

**Question**: `otp_ctrl` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `otp_ctrl_sec_cm_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_sec_cm_testplan.hjson`와 code artifact `prim_sec_anchor_flop`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_kdi.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: otp_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv:L275

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_sec_cm_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=417.4625 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=412.1125 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=380.975 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=369.25 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=64.875 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=54.3 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=49.125 \| 5. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=48.6875 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=601.5625 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=418.925 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=417.4625 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=416.8625 \| 5. component:opentitan [component] @ __graphify_spec_only__/components.md, score=380.975 |

### userqa_002 (user_code_to_spec_why, L5)

**Question**: `prim_sync_reqack`가 왜 필요한지 spec 기준으로 설명해줘. `top_englishbreakfast/ip_autogen/rstmgr/rtl/rstmgr_cnsty_chk.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `chip_rstmgr_testplan`는 spec 문서 `rstmgr_cnsty_chk_testplan.hjson`와 code artifact `prim_sync_reqack`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/rtl/rstmgr_cnsty_chk.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rstmgr_cnsty_chk_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson | component:chip_rstmgr_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rstmgr_testplan_hjson [component] @ __graphify_spec_only__/components.md | component:rstmgr [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_sync_reqack [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\rtl\rstmgr_cnsty_chk.sv:L274

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_sync_reqack, top_englishbreakfast/ip_autogen/rstmgr/rtl/rstmgr_cnsty_chk.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=651.0125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=589.6625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=552.9125 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=509.5125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=501.9 |
| code-only | - | 21 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=122.0 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=107.4375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.3125 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=85.3125 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=84.25 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=934.0625 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=730.0125 \| 3. component:pinmux [component] @ __graphify_spec_only__/components.md, score=679.0875 \| 4. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=667.925 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=650.075 |

### userqa_003 (user_review_trace, L5)

**Question**: 리뷰할 때 `chip_rstmgr_testplan`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `chip_rstmgr_testplan`는 spec 문서 `rstmgr_cnsty_chk_testplan.hjson`와 code artifact `prim_rst_sync`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rstmgr_cnsty_chk_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson | component:chip_rstmgr_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rstmgr_testplan_hjson [component] @ __graphify_spec_only__/components.md | component:rstmgr [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_rst_sync [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv:L451

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rstmgr, rstmgr_cnsty_chk_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=171.0 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=110.25 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=105.4375 \| 5. component:testplan [component] @ __graphify_spec_only__/components.md, score=42.8125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .ok() [code] @ opentitan\sw\host\opentitanlib\src\transport\mod.rs, score=78.4375 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=45.3125 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=40.1625 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=35.375 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.6875 |
| spec-code | 1 | 25 | 25 | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=233.55 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=126.15 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=125.475 \| 4. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=122.625 \| 5. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=120.75 |

### userqa_004 (user_verification_coverage, L4)

**Question**: `chip_rstmgr_testplan` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`와 연결된 code 쪽도 알려줘.

**Expected answer**: `chip_rstmgr_testplan`는 spec 문서 `rstmgr_cnsty_chk_testplan.hjson`와 code artifact `rstmgr_cnsty_chk_if`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rstmgr_cnsty_chk_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson | component:chip_rstmgr_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rstmgr_testplan_hjson [component] @ __graphify_spec_only__/components.md | component:rstmgr [component] @ __graphify_spec_only__/components.md

**Gold code answer**: rstmgr_cnsty_chk_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv:L436

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rstmgr_cnsty_chk_testplan.hjson, rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson, ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=516.8625 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=515.2875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=511.4375 \| 4. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=454.4875 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=347.025 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .ok() [code] @ opentitan\sw\host\opentitanlib\src\transport\mod.rs, score=89.3125 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=52.5625 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=42.8625 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.25 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=559.3375 \| 2. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=516.8625 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=515.2875 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=511.4375 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=464.55 |

### userqa_005 (user_change_impact, L5)

**Question**: `chip_rstmgr_testplan` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `chip_rstmgr_testplan`는 spec 문서 `rstmgr_cnsty_chk_testplan.hjson`와 code artifact `rstmgr_cnsty_chk`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rstmgr_cnsty_chk_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson | component:chip_rstmgr_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rstmgr_testplan_hjson [component] @ __graphify_spec_only__/components.md | component:rstmgr [component] @ __graphify_spec_only__/components.md

**Gold code answer**: rstmgr_cnsty_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv:L458

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rstmgr_cnsty_chk_testplan.hjson, rstmgr, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=171.0 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=110.25 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=105.4375 \| 5. component:testplan [component] @ __graphify_spec_only__/components.md, score=42.8125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .ok() [code] @ opentitan\sw\host\opentitanlib\src\transport\mod.rs, score=78.4375 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=45.3125 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=40.1625 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=35.375 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.6875 |
| spec-code | 1 | 25 | 25 | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=233.55 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=126.15 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=125.475 \| 4. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=122.625 \| 5. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=120.75 |

### userqa_006 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `rv_core_ibex`는 `top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_sec_cm_testplan.hjson`와 code artifact `prim_sec_anchor_buf`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sec_anchor_buf [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L359

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1062.3375 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=965.8125 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=876.8375 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=848.925 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=805.2625 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=367.25 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=72.875 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1314.1125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1062.3375 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=1011.925 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=987.8625 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=986.775 |

### userqa_007 (user_spec_to_code_explain, L4)

**Question**: `ac_range_check` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `ac_range_check_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `ac_range_check`는 spec 문서 `ac_range_check_testplan.hjson`와 code artifact `prim_flop_en`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv:L269

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_flop_en, top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=281.1375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=279.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=277.1125 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=178.15 \| 5. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=167.2 |
| code-only | - | 19 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.8125 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.3125 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=281.1375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=279.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=277.1125 \| 4. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=258.55 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=231.0 |

### userqa_008 (user_code_to_spec_why, L5)

**Question**: `prim_onehot_enc`가 왜 필요한지 spec 기준으로 설명해줘. `top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `ac_range_check`는 spec 문서 `ac_range_check_testplan.hjson`와 code artifact `prim_onehot_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv:L128

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check, ac_range_check_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=624.75 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=585.9875 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=524.5625 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=521.2375 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=462.4375 |
| code-only | - | 18 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=111.5625 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=97.85 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.0625 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=84.625 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=83.8125 |
| spec-code | 9 | 1 | 9 | spec=N, code=Y, joint=N | 1. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=789.2625 \| 2. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=787.6375 \| 3. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=785.0125 \| 4. tlul_jtag_dtm [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=756.8875 \| 5. tlul_cmd_intg_gen [code] @ opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv, score=755.8875 |

### userqa_009 (user_review_trace, L5)

**Question**: 리뷰할 때 `ac_range_check`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `ac_range_check`는 spec 문서 `ac_range_check_testplan.hjson`와 code artifact `ac_range_check_bind.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_testplan.hjson, top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson, ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.6875 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.1875 |
| spec-code | 1 | 18 | 18 | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=202.95 \| 2. component:tlul [component] @ __graphify_spec_only__/components.md, score=57.9375 \| 3. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=55.9875 \| 4. checklist.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md, score=55.9875 \| 5. registers.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/registers.md, score=55.9875 |

### userqa_010 (user_verification_coverage, L4)

**Question**: `ac_range_check` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`와 연결된 code 쪽도 알려줘.

**Expected answer**: `ac_range_check`는 spec 문서 `ac_range_check_testplan.hjson`와 code artifact `ac_range_check_bind`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_testplan.hjson, ac_range_check, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1028.2125 \| 2. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=851.2875 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=845.775 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=771.05 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=690.375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.6875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.25 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=84.0 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.5625 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.0625 |
| spec-code | 15 | - | - | spec=N, code=N, joint=N | 1. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1056.0625 \| 2. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=1038.6625 \| 3. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=1034.5375 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1028.2125 \| 5. tlul_jtag_dtm [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1000.1125 |

### userqa_011 (user_change_impact, L5)

**Question**: `ac_range_check` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `ac_range_check`는 spec 문서 `ac_range_check_testplan.hjson`와 code artifact `tb.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tb/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_testplan.hjson, top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.6875 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.1875 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=202.95 \| 2. component:tlul [component] @ __graphify_spec_only__/components.md, score=57.9375 \| 3. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=55.9875 \| 4. checklist.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md, score=55.9875 \| 5. registers.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/registers.md, score=55.9875 |

### userqa_012 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `ac_range_check`는 `top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `ac_range_check`는 spec 문서 `ac_range_check_testplan.hjson`와 code artifact `ac_range_check_env_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv:L9

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_env_pkg, ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1028.2125 \| 2. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=851.2875 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=845.775 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=771.05 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=690.375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.3125 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=56.5 \| 3. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.5625 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=54.3125 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=54.3125 |
| spec-code | 14 | - | - | spec=N, code=N, joint=N | 1. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1052.3125 \| 2. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=1030.7875 \| 3. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=1030.7875 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1028.2125 \| 5. tlul_jtag_dtm [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=997.8625 |

### userqa_013 (user_spec_to_code_explain, L4)

**Question**: `ac_range_check` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `ac_range_check_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `ac_range_check`는 spec 문서 `ac_range_check_testplan.hjson`와 code artifact `ac_range_check_test_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tb/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_test_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv:L10

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check, ac_range_check_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=281.1375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=279.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=277.1125 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=178.15 \| 5. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=167.2 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.8125 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.3125 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=281.1375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=279.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=277.1125 \| 4. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=258.55 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=231.0 |

### userqa_014 (user_code_to_spec_why, L5)

**Question**: `prim_flop_en`가 왜 필요한지 spec 기준으로 설명해줘. `top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `ac_range_check`는 spec 문서 `interfaces.md`와 code artifact `prim_flop_en`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv:L269

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md, top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=624.75 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=585.9875 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=524.5625 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=521.2375 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=462.4375 |
| code-only | - | 19 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=113.4375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=97.85 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.0625 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=84.75 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=84.625 |
| spec-code | 9 | 1 | 9 | spec=N, code=Y, joint=N | 1. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=791.7625 \| 2. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=785.0125 \| 3. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=783.8875 \| 4. tlul_jtag_dtm [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=756.8875 \| 5. tlul_cmd_intg_gen [code] @ opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv, score=755.8875 |

### userqa_015 (user_review_trace, L5)

**Question**: 리뷰할 때 `ac_range_check`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `ac_range_check`는 spec 문서 `interfaces.md`와 code artifact `prim_onehot_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv:L128

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, ac_range_check, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | 19 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.6875 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.1875 |
| spec-code | 1 | 9 | 9 | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=202.95 \| 2. component:tlul [component] @ __graphify_spec_only__/components.md, score=57.9375 \| 3. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=55.9875 \| 4. checklist.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md, score=55.9875 \| 5. registers.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/registers.md, score=55.9875 |

### userqa_016 (user_verification_coverage, L4)

**Question**: `ac_range_check` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`와 연결된 code 쪽도 알려줘.

**Expected answer**: `ac_range_check`는 spec 문서 `interfaces.md`와 code artifact `ac_range_check_bind.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=872.9875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=826.4375 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=749.975 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=591.0625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.6875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.125 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=83.1 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.4375 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=81.9375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 2. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=885.3125 \| 3. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=881.1875 \| 4. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=878.9875 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=872.9875 |

### userqa_017 (user_change_impact, L5)

**Question**: `ac_range_check` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `ac_range_check`는 spec 문서 `interfaces.md`와 code artifact `ac_range_check_bind`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_bind, ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.6875 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.1875 |
| spec-code | 1 | 18 | 18 | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=202.95 \| 2. component:tlul [component] @ __graphify_spec_only__/components.md, score=57.9375 \| 3. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=55.9875 \| 4. checklist.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md, score=55.9875 \| 5. registers.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/registers.md, score=55.9875 |

### userqa_018 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `ac_range_check`는 `top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `ac_range_check`는 spec 문서 `interfaces.md`와 code artifact `tb.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tb/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check, interfaces.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=872.9875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=826.4375 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=749.975 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=591.0625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.3125 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=56.375 \| 3. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.4375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=54.1875 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=54.1875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 2. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=877.4375 \| 3. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=877.4375 \| 4. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=875.2375 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=872.9875 |

### userqa_019 (user_spec_to_code_explain, L4)

**Question**: `ac_range_check` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `interfaces.md` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `ac_range_check`는 spec 문서 `interfaces.md`와 code artifact `ac_range_check_env_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv:L9

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md, ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=196.275 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=122.925 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=42.7875 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=38.85 \| 5. topic:security [topic] @ __graphify_spec_only__/topics.md, score=37.0125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.6875 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.1875 |
| spec-code | 1 | 23 | 23 | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=206.625 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=196.275 \| 3. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=65.2125 \| 4. component:tlul [component] @ __graphify_spec_only__/components.md, score=61.6125 \| 5. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=61.0875 |

### userqa_020 (user_code_to_spec_why, L5)

**Question**: `ac_range_check_test_pkg`가 왜 필요한지 spec 기준으로 설명해줘. `ip_autogen/ac_range_check/dv/tb/tb.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `ac_range_check`는 spec 문서 `interfaces.md`와 code artifact `ac_range_check_test_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tb/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_test_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv:L10

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, ac_range_check, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=343.0 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=289.3625 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=287.0 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=281.75 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=252.4375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=242.8125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=232.5 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=149.625 \| 4. .ok() [code] @ opentitan\sw\host\opentitanlib\src\transport\mod.rs, score=140.6875 \| 5. assertEqual() [code] @ ibex\vendor\riscv-tests\debug\testlib.py, score=58.4375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=352.25 \| 2. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=349.5625 \| 3. component:pinmux [component] @ __graphify_spec_only__/components.md, score=345.8125 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=343.0 \| 5. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=319.6875 |

### userqa_021 (user_review_trace, L5)

**Question**: 리뷰할 때 `ac_range_check`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `ac_range_check`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_flop_en`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv:L269

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | 19 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.6875 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.1875 |
| spec-code | 1 | 9 | 9 | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=202.95 \| 2. component:tlul [component] @ __graphify_spec_only__/components.md, score=57.9375 \| 3. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=55.9875 \| 4. checklist.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md, score=55.9875 \| 5. registers.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/registers.md, score=55.9875 |

### userqa_022 (user_verification_coverage, L4)

**Question**: `ac_range_check` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`와 연결된 code 쪽도 알려줘.

**Expected answer**: `ac_range_check`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_onehot_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv:L128

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_onehot_enc, top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1704.4 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=883.4 \| 4. component:pinmux [component] @ __graphify_spec_only__/components.md, score=639.3625 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=631.4 |
| code-only | - | 19 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.6875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.125 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=83.1 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.4375 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=81.9375 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1704.4 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 3. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=913.6625 \| 4. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=909.5375 \| 5. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=903.9625 |

### userqa_023 (user_change_impact, L5)

**Question**: `ac_range_check` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `ac_range_check`는 spec 문서 `theory_of_operation.md`와 code artifact `ac_range_check_bind.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.6875 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.1875 |
| spec-code | 1 | 18 | 18 | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=202.95 \| 2. component:tlul [component] @ __graphify_spec_only__/components.md, score=57.9375 \| 3. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=55.9875 \| 4. checklist.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md, score=55.9875 \| 5. registers.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/registers.md, score=55.9875 |

### userqa_024 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `ac_range_check`는 `top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `ac_range_check`는 spec 문서 `theory_of_operation.md`와 code artifact `ac_range_check_bind`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md, ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1704.4 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=883.4 \| 4. component:pinmux [component] @ __graphify_spec_only__/components.md, score=639.3625 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=631.4 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.3125 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=56.375 \| 3. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.4375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=54.1875 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=54.1875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1704.4 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1043.7 \| 3. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=905.7875 \| 4. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=905.7875 \| 5. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=900.2125 |

### userqa_025 (user_spec_to_code_explain, L4)

**Question**: `ac_range_check` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `theory_of_operation.md` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `ac_range_check`는 spec 문서 `theory_of_operation.md`와 code artifact `tb.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tb/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, ac_range_check, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=845.9375 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=127.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=99.75 \| 4. component:system [component] @ __graphify_spec_only__/components.md, score=77.875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=69.5625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.6875 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.1875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=845.9375 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=210.825 \| 3. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=102.3375 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=99.75 \| 5. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=93.5625 |

### userqa_026 (user_code_to_spec_why, L5)

**Question**: `ac_range_check_env_pkg`가 왜 필요한지 spec 기준으로 설명해줘. `ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `ac_range_check`는 spec 문서 `theory_of_operation.md`와 code artifact `ac_range_check_env_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv:L9

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=343.0 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=289.8875 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=287.175 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=282.625 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=256.1125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=526.125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=514.425 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=299.5625 \| 4. .ok() [code] @ opentitan\sw\host\opentitanlib\src\transport\mod.rs, score=282.4375 \| 5. mmio_region_from_addr() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=141.3125 |
| spec-code | 3 | - | - | spec=Y, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=526.125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=514.425 \| 3. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=370.25 \| 4. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=362.5375 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=349.7125 |

### userqa_027 (user_review_trace, L5)

**Question**: 리뷰할 때 `ac_range_check`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `ac_range_check`는 spec 문서 `theory_of_operation.md`와 code artifact `ac_range_check_test_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tb/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_test_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv:L10

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_test_pkg, ip_autogen/ac_range_check/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=38.85 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=34.125 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=31.6875 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=29.1875 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=202.95 \| 2. component:tlul [component] @ __graphify_spec_only__/components.md, score=57.9375 \| 3. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=55.9875 \| 4. checklist.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md, score=55.9875 \| 5. registers.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/registers.md, score=55.9875 |

### userqa_028 (user_verification_coverage, L4)

**Question**: `alert_handler` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson`와 연결된 code 쪽도 알려줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_sec_cm_testplan.hjson`와 code artifact `alert_handler_cov_bind.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler, alert_handler_sec_cm_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1071.0 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=885.675 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=869.3125 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=809.6375 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=712.1625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.6875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=88.575 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.4375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=83.25 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.5 |
| spec-code | 3 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1071.0 \| 2. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1067.0875 \| 3. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=1058.0 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1050.25 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1046.4375 |

### userqa_029 (user_change_impact, L5)

**Question**: `alert_handler` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_sec_cm_testplan.hjson`와 code artifact `alert_handler_cov_bind`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_sec_cm_testplan.hjson, top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson, ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=221.1875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=45.9375 \| 3. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=39.375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=31.0625 \| 5. component:alert_handler_testplan [component] @ __graphify_spec_only__/components.md, score=30.0625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=42.6 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.0 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=29.625 |
| spec-code | 1 | 7 | 7 | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=365.6375 \| 2. component:top_earlgrey [component] @ __graphify_spec_only__/components.md, score=90.65 \| 3. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=83.775 \| 4. component:top_darjeeling [component] @ __graphify_spec_only__/components.md, score=78.3 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=73.8375 |

### userqa_030 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `alert_handler`는 `top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_sec_cm_testplan.hjson`와 code artifact `alert_handler_bind.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/sva/alert_handler_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_sec_cm_testplan.hjson, alert_handler, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1071.0 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=885.675 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=869.3125 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=809.6375 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=712.1625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=66.9375 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.3125 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=57.6875 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.5 |
| spec-code | 3 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1071.0 \| 2. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1063.3375 \| 3. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=1048.55 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1046.725 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1043.5875 |

### userqa_031 (user_spec_to_code_explain, L4)

**Question**: `alert_handler` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `alert_handler_sec_cm_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_sec_cm_testplan.hjson`와 code artifact `alert_handler_bind`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/sva/alert_handler_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_sec_cm_testplan.hjson, top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=329.425 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=317.7125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=65.0 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=43.275 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 5. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=491.875 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=327.8375 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=324.275 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 |

### userqa_032 (user_code_to_spec_why, L5)

**Question**: `tb.sv`가 왜 필요한지 spec 기준으로 설명해줘. `ip_autogen/alert_handler/dv/tb/tb.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_sec_cm_testplan.hjson`와 code artifact `tb.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/tb/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, ip_autogen/alert_handler/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=362.5 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=360.0625 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=307.5625 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=301.0 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=288.75 |
| code-only | - | 21 | - | spec=N, code=N, joint=N | 1. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=30.625 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=30.3125 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=29.125 \| 4. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=27.875 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=26.875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=587.5 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=372.8125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=370.5625 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=360.0625 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=346.8125 |

### userqa_033 (user_review_trace, L5)

**Question**: 리뷰할 때 `alert_handler`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_testplan.hjson`와 code artifact `alert_handler_cov_bind.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler, alert_handler_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=221.1875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=45.9375 \| 3. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=39.375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=31.0625 \| 5. component:alert_handler_testplan [component] @ __graphify_spec_only__/components.md, score=30.0625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=42.6 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.0 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=29.625 |
| spec-code | 1 | 7 | 7 | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=365.6375 \| 2. component:top_earlgrey [component] @ __graphify_spec_only__/components.md, score=90.65 \| 3. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=83.775 \| 4. component:top_darjeeling [component] @ __graphify_spec_only__/components.md, score=78.3 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=73.8375 |

### userqa_034 (user_verification_coverage, L4)

**Question**: `alert_handler` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`와 연결된 code 쪽도 알려줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_testplan.hjson`와 code artifact `alert_handler_cov_bind`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_testplan.hjson, top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson, ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1043.0 \| 2. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=869.3125 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=857.2375 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=781.2 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=704.6375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.6875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=88.575 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.4375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=83.25 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.5 |
| spec-code | 2 | - | - | spec=Y, code=N, joint=N | 1. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1056.9625 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=1052.75 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1043.0 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1032.0625 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1028.4375 |

### userqa_035 (user_change_impact, L5)

**Question**: `alert_handler` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_testplan.hjson`와 code artifact `alert_handler_bind.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/sva/alert_handler_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_testplan.hjson, alert_handler, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=221.1875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=45.9375 \| 3. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=39.375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=31.0625 \| 5. component:alert_handler_testplan [component] @ __graphify_spec_only__/components.md, score=30.0625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=42.6 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.0 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=29.625 |
| spec-code | 1 | 9 | 9 | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=365.6375 \| 2. component:top_earlgrey [component] @ __graphify_spec_only__/components.md, score=90.65 \| 3. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=83.775 \| 4. component:top_darjeeling [component] @ __graphify_spec_only__/components.md, score=78.3 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=73.8375 |

### userqa_036 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `alert_handler`는 `top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_testplan.hjson`와 code artifact `alert_handler_bind`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/sva/alert_handler_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_testplan.hjson, top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1043.0 \| 2. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=869.3125 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=857.2375 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=781.2 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=704.6375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.3125 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=57.6875 \| 3. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.5 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.5 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.5 |
| spec-code | 2 | - | - | spec=Y, code=N, joint=N | 1. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=1053.2125 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=1043.3 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1043.0 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1028.5375 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1025.5875 |

### userqa_037 (user_spec_to_code_explain, L4)

**Question**: `alert_handler` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `alert_handler_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_testplan.hjson`와 code artifact `tb.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/tb/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, ip_autogen/alert_handler/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=324.175 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=290.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=289.975 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=289.275 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=43.275 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.25 \| 4. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=33.1 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=486.625 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=309.65 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=306.275 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=290.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=289.975 |

### userqa_038 (user_code_to_spec_why, L5)

**Question**: `alert_handler_cov_bind.sv`가 왜 필요한지 spec 기준으로 설명해줘. `ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `alert_handler`는 spec 문서 `theory_of_operation.md`와 code artifact `alert_handler_cov_bind.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=379.825 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=361.8125 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=308.35 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=305.2 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=292.95 |
| code-only | - | 26 | - | spec=N, code=N, joint=N | 1. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=36.725 \| 2. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=34.15 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=31.15 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=30.3125 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=28.375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=669.625 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=383.8375 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=380.8875 \| 4. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=362.9 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=361.8125 |

### userqa_039 (user_review_trace, L5)

**Question**: 리뷰할 때 `alert_handler`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `alert_handler`는 spec 문서 `theory_of_operation.md`와 code artifact `alert_handler_cov_bind`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md, ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=221.1875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=45.9375 \| 3. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=39.375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=31.0625 \| 5. component:alert_handler_testplan [component] @ __graphify_spec_only__/components.md, score=30.0625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=42.6 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.0 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=29.625 |
| spec-code | 1 | 7 | 7 | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=365.6375 \| 2. component:top_earlgrey [component] @ __graphify_spec_only__/components.md, score=90.65 \| 3. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=83.775 \| 4. component:top_darjeeling [component] @ __graphify_spec_only__/components.md, score=78.3 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=73.8375 |

### userqa_040 (user_verification_coverage, L4)

**Question**: `alert_handler` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md`와 연결된 code 쪽도 알려줘.

**Expected answer**: `alert_handler`는 spec 문서 `theory_of_operation.md`와 code artifact `alert_handler_bind.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/sva/alert_handler_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, alert_handler, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1727.15 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1061.8125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=897.05 \| 4. component:pinmux [component] @ __graphify_spec_only__/components.md, score=640.9375 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=635.5125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.6875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.1875 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=87.525 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=83.0 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=82.25 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1727.15 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1061.8125 \| 3. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=971.225 \| 4. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=904.4125 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=897.05 |

### userqa_041 (user_change_impact, L5)

**Question**: `alert_handler` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `alert_handler`는 spec 문서 `theory_of_operation.md`와 code artifact `alert_handler_bind`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/sva/alert_handler_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=221.1875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=45.9375 \| 3. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=39.375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=31.0625 \| 5. component:alert_handler_testplan [component] @ __graphify_spec_only__/components.md, score=30.0625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=42.6 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.0 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=29.625 |
| spec-code | 1 | 9 | 9 | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=365.6375 \| 2. component:top_earlgrey [component] @ __graphify_spec_only__/components.md, score=90.65 \| 3. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=83.775 \| 4. component:top_darjeeling [component] @ __graphify_spec_only__/components.md, score=78.3 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=73.8375 |

### userqa_042 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `alert_handler`는 `top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `alert_handler`는 spec 문서 `theory_of_operation.md`와 code artifact `tb.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/tb/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, ip_autogen/alert_handler/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1727.15 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1061.8125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=897.05 \| 4. component:pinmux [component] @ __graphify_spec_only__/components.md, score=640.9375 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=635.5125 |
| code-only | - | 28 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.3125 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=57.4375 \| 3. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.25 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.25 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.25 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1727.15 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1061.8125 \| 3. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=961.775 \| 4. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=900.6625 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=897.05 |

### userqa_043 (user_spec_to_code_explain, L4)

**Question**: `racl_ctrl` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `interfaces.md` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `racl_ctrl`는 spec 문서 `interfaces.md`와 code artifact `racl_ctrl_base_env_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_base_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv:L65

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: racl_ctrl, interfaces.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=247.4625 \| 2. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=151.275 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=120.3375 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=114.1 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=109.4 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=48.7875 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=43.125 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=40.0625 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=37.0 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=247.4625 \| 2. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=237.675 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=201.7875 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=190.85 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=159.6 |

### userqa_044 (user_code_to_spec_why, L5)

**Question**: `racl_ctrl_env_cfg.sv`가 왜 필요한지 spec 기준으로 설명해줘. `top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_cfg.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `racl_ctrl`는 spec 문서 `interfaces.md`와 code artifact `racl_ctrl_env_cfg.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_cfg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_env_cfg.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md, top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_cfg.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=696.325 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=672.2625 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=575.925 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=552.9125 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=473.925 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=70.3125 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=65.0625 \| 3. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=61.9375 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=61.5625 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=61.5625 |
| spec-code | 9 | - | - | spec=N, code=N, joint=N | 1. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=830.2375 \| 2. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=806.55 \| 3. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=806.1125 \| 4. tlul_jtag_dtm [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=805.8 \| 5. dma [code] @ opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv, score=804.55 |

### userqa_045 (user_review_trace, L5)

**Question**: 리뷰할 때 `racl_ctrl`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `racl_ctrl`는 spec 문서 `interfaces.md`와 code artifact `racl_ctrl_env_pkg.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_env_pkg.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, racl_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=140.25 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=106.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=101.0 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=85.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=48.7875 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=43.125 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=40.0625 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=37.0 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=226.65 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=188.1375 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=182.45 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=144.9 \| 5. component:sysrst_ctrl [component] @ __graphify_spec_only__/components.md, score=120.075 |

### userqa_046 (user_verification_coverage, L4)

**Question**: `racl_ctrl` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md`와 연결된 code 쪽도 알려줘.

**Expected answer**: `racl_ctrl`는 spec 문서 `interfaces.md`와 code artifact `racl_ctrl_ral_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_ral_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv:L11

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1113.2625 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=927.5875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=905.8875 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=802.7375 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=643.3875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=109.1875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=94.4625 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=93.5 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.5625 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=86.4375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1113.2625 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=927.5875 \| 3. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=920.1625 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=905.8875 \| 5. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=903.2375 |

### userqa_047 (user_change_impact, L5)

**Question**: `racl_ctrl` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `racl_ctrl`는 spec 문서 `interfaces.md`와 code artifact `tb.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=140.25 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=106.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=101.0 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=85.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=48.7875 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=43.125 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=40.0625 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=37.0 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=226.65 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=188.1375 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=182.45 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=144.9 \| 5. component:sysrst_ctrl [component] @ __graphify_spec_only__/components.md, score=120.075 |

### userqa_048 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `racl_ctrl`는 `top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `racl_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `racl_ctrl_base_env_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_base_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv:L65

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: racl_ctrl, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1759.0 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1113.2625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=962.85 \| 4. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=659.4875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=644.35 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=69.8125 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=62.75 \| 3. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=59.8125 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=59.4375 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=59.4375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1759.0 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1113.2625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=962.85 \| 4. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=941.3875 \| 5. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=923.7125 |

### userqa_049 (user_spec_to_code_explain, L4)

**Question**: `racl_ctrl` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `theory_of_operation.md` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `racl_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `racl_ctrl_env_cfg.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_cfg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_env_cfg.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md, top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_cfg.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=900.625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=171.0625 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=159.1875 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=149.5625 \| 5. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=148.125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=48.7875 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=43.125 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=40.0625 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=37.0 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=900.625 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=240.6375 \| 3. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=234.525 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=231.0125 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=186.9 |

### userqa_050 (user_code_to_spec_why, L5)

**Question**: `racl_ctrl_env_pkg.sv`가 왜 필요한지 spec 기준으로 설명해줘. `top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_pkg.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `racl_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `racl_ctrl_env_pkg.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_env_pkg.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, racl_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=696.325 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=665.9625 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=575.925 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=552.9125 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=473.925 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. uvm_pkg [code] @ sv-tests\tests\testbenches\uvm_test_run_test.sv, score=74.0 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=70.3125 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=63.9375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=60.8125 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=60.4375 |
| spec-code | 9 | - | - | spec=N, code=N, joint=N | 1. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=823.4875 \| 2. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=799.8 \| 3. prim_onehot_enc [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=799.3625 \| 4. tlul_jtag_dtm [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=799.05 \| 5. dma [code] @ opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv, score=797.8 |

### userqa_051 (user_review_trace, L5)

**Question**: 리뷰할 때 `racl_ctrl`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `racl_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `racl_ctrl_ral_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_ral_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv:L11

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=140.25 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=106.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=101.0 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=85.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=48.7875 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=43.125 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=40.0625 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=37.0 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=226.65 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=188.1375 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=182.45 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=144.9 \| 5. component:sysrst_ctrl [component] @ __graphify_spec_only__/components.md, score=120.075 |

### userqa_052 (user_verification_coverage, L4)

**Question**: `racl_ctrl` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md`와 연결된 code 쪽도 알려줘.

**Expected answer**: `racl_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `tb.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1759.0 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1113.2625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=962.85 \| 4. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=659.4875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=644.35 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=109.1875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=94.4625 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=93.5 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=87.5625 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=86.4375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1759.0 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1113.2625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=962.85 \| 4. prim_ram_1p_adv [code] @ opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv, score=945.1375 \| 5. prim_flop_en [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=931.5875 |

### userqa_053 (user_change_impact, L5)

**Question**: `alert_handler` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_sec_cm_testplan.hjson`와 code artifact `prim_alert_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv:L11

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler, alert_handler_sec_cm_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=221.1875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=45.9375 \| 3. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=39.375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=31.0625 \| 5. component:alert_handler_testplan [component] @ __graphify_spec_only__/components.md, score=30.0625 |
| code-only | - | 22 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=42.6 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.0 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=29.625 |
| spec-code | 1 | 5 | 5 | spec=Y, code=Y, joint=Y | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=365.6375 \| 2. component:top_earlgrey [component] @ __graphify_spec_only__/components.md, score=90.65 \| 3. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=83.775 \| 4. component:top_darjeeling [component] @ __graphify_spec_only__/components.md, score=78.3 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=73.8375 |

### userqa_054 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `alert_handler`는 `top_earlgrey/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_sec_cm_testplan.hjson`와 code artifact `prim_esc_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_sec_cm_testplan.hjson, top_earlgrey/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson, top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1100.75 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=911.925 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=867.5625 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=835.0125 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=722.6625 |
| code-only | - | 19 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=67.8125 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=66.9375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=57.6875 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=56.125 |
| spec-code | 10 | 1 | 10 | spec=N, code=Y, joint=N | 1. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1406.975 \| 2. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1403.8375 \| 3. csrng [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1302.425 \| 4. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1301.8 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1294.0 |

### userqa_055 (user_spec_to_code_explain, L4)

**Question**: `alert_handler` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `alert_handler_sec_cm_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_sec_cm_testplan.hjson`와 code artifact `alert_handler_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler_reg_wrap.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_sec_cm_testplan.hjson, alert_handler, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=329.425 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=317.7125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | 16 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=65.0 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=43.275 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 5. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=491.875 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=327.8375 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=324.275 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 |

### userqa_056 (user_code_to_spec_why, L5)

**Question**: `prim_alert_pkg`가 왜 필요한지 spec 기준으로 설명해줘. `top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_testplan.hjson`와 code artifact `prim_alert_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv:L11

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_testplan.hjson, top_earlgrey/ip_autogen/alert_handler/data/alert_handler_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=660.8 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=630.525 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=559.0375 \| 4. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=541.875 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=540.8375 |
| code-only | - | 21 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.0625 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=108.1 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=89.25 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=86.25 \| 5. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=85.75 |
| spec-code | 7 | 1 | 7 | spec=N, code=Y, joint=N | 1. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1010.4125 \| 2. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1003.85 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=925.75 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=921.125 \| 5. csrng [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=911.375 |

### userqa_057 (user_review_trace, L5)

**Question**: 리뷰할 때 `alert_handler`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_testplan.hjson`와 code artifact `prim_esc_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_esc_pkg, top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=221.1875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=45.9375 \| 3. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=39.375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=31.0625 \| 5. component:alert_handler_testplan [component] @ __graphify_spec_only__/components.md, score=30.0625 |
| code-only | - | 22 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=42.6 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.0 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=29.625 |
| spec-code | 1 | 5 | 5 | spec=Y, code=Y, joint=Y | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=365.6375 \| 2. component:top_earlgrey [component] @ __graphify_spec_only__/components.md, score=90.65 \| 3. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=83.775 \| 4. component:top_darjeeling [component] @ __graphify_spec_only__/components.md, score=78.3 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=73.8375 |

### userqa_058 (user_verification_coverage, L4)

**Question**: `alert_handler` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_earlgrey/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`와 연결된 code 쪽도 알려줘.

**Expected answer**: `alert_handler`는 spec 문서 `alert_handler_testplan.hjson`와 code artifact `alert_handler_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler_reg_wrap.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler, alert_handler_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1072.75 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=883.4875 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=867.5625 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=806.575 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=722.1375 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=107.1875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=92.325 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=88.4375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=83.875 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=83.5625 |
| spec-code | 10 | - | - | spec=N, code=N, joint=N | 1. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1392.3125 \| 2. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1388.6875 \| 3. csrng [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1292.3 \| 4. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1291.3 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1283.875 |

### userqa_059 (user_change_impact, L5)

**Question**: `alert_handler` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `alert_handler`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_alert_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv:L11

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md, top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=221.1875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=45.9375 \| 3. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=39.375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=31.0625 \| 5. component:alert_handler_testplan [component] @ __graphify_spec_only__/components.md, score=30.0625 |
| code-only | - | 22 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=42.6 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.0 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=29.625 |
| spec-code | 1 | 5 | 5 | spec=Y, code=Y, joint=Y | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=365.6375 \| 2. component:top_earlgrey [component] @ __graphify_spec_only__/components.md, score=90.65 \| 3. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=83.775 \| 4. component:top_darjeeling [component] @ __graphify_spec_only__/components.md, score=78.3 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=73.8375 |

### userqa_060 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `alert_handler`는 `top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `alert_handler`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_esc_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, alert_handler, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1742.025 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1079.3125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=926.8 \| 4. component:pinmux [component] @ __graphify_spec_only__/components.md, score=653.1875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=646.275 |
| code-only | - | 16 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=67.8125 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=57.4375 \| 3. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.875 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.875 \| 5. tlul_cmd_intg_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=55.875 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1742.025 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1162.9 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1160.2 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=1079.3125 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1077.875 |

### userqa_061 (user_spec_to_code_explain, L4)

**Question**: `alert_handler` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `theory_of_operation.md` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `alert_handler`는 spec 문서 `theory_of_operation.md`와 code artifact `alert_handler_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/alert_handler/rtl/alert_handler_reg_wrap.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_earlgrey/ip_autogen/alert_handler/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.25 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=256.625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=112.0 \| 4. component:system [component] @ __graphify_spec_only__/components.md, score=82.6875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=71.75 |
| code-only | - | 15 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=42.6 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=39.375 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=36.0 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=32.625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=29.625 |
| spec-code | 1 | 10 | 10 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.25 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=401.075 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=124.4625 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=121.5375 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=112.0 |

### userqa_062 (user_code_to_spec_why, L5)

**Question**: `prim_secded_inv_72_64_enc`가 왜 필요한지 spec 기준으로 설명해줘. `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_ecc_reg.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_sec_cm_testplan.hjson`와 code artifact `prim_secded_inv_72_64_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_ecc_reg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: otp_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv:L39

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_secded_inv_72_64_enc, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_ecc_reg.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=727.9125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=723.1 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=691.7625 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=619.15 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=557.9875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=120.875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=119.875 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=117.8 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=113.5625 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=112.8125 |
| spec-code | 3 | 1 | 3 | spec=Y, code=Y, joint=Y | 1. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1088.75 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1078.0 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=1073.5875 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1038.9 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1036.725 |

### userqa_063 (user_review_trace, L5)

**Question**: 리뷰할 때 `otp_ctrl`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_sec_cm_testplan.hjson`와 code artifact `prim_sum_tree`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_dai.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: otp_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sum_tree [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_dai.sv:L944

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl, otp_ctrl_sec_cm_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=312.1875 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=115.0625 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=107.1875 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=104.9375 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=91.4375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=52.5375 \| 2. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=46.3125 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=46.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=44.375 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 |
| spec-code | 1 | 11 | 11 | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=483.6375 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=186.3875 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=169.875 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=168.9375 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=163.7125 |

### userqa_064 (user_verification_coverage, L4)

**Question**: `otp_ctrl` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`와 연결된 code 쪽도 알려줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_sec_cm_testplan.hjson`와 code artifact `otp_ctrl_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: otp_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L13

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_sec_cm_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1206.975 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=980.525 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=891.0125 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=885.5 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=833.6 |
| code-only | - | 19 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=113.8125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.775 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.875 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=95.0625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=92.5625 |
| spec-code | 9 | - | - | spec=N, code=N, joint=N | 1. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1466.425 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1463.2375 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1445.1625 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1444.3 \| 5. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1395.6875 |

### userqa_065 (user_change_impact, L5)

**Question**: `otp_ctrl` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_sec_cm_testplan.hjson`와 code artifact `prim_util_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: otp_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_util_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_sec_cm_testplan.hjson, otp_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=312.1875 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=115.0625 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=107.1875 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=104.9375 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=91.4375 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=52.5375 \| 2. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=46.3125 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=46.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=44.375 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 |
| spec-code | 1 | 6 | 6 | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=483.6375 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=186.3875 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=169.875 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=168.9375 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=163.7125 |

### userqa_066 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `otp_ctrl`는 `top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_sec_cm_testplan.hjson`와 code artifact `otp_ctrl_macro_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: otp_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L15

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_sec_cm_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1206.975 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=980.525 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=891.0125 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=885.5 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=833.6 |
| code-only | - | 17 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=74.4375 \| 2. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=68.5625 \| 3. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=66.8125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=65.925 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=65.125 |
| spec-code | 10 | - | - | spec=N, code=N, joint=N | 1. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1460.675 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1460.6125 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1441.6375 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1441.45 \| 5. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1393.8125 |

### userqa_067 (user_spec_to_code_explain, L4)

**Question**: `otp_ctrl` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `otp_ctrl_sec_cm_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_sec_cm_testplan.hjson`와 code artifact `otp_macro_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: otp_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl.sv:L21

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_macro_pkg, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=417.4625 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=412.1125 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=380.975 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=369.25 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | 23 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=64.875 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=54.3 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=49.125 \| 5. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=48.6875 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=601.5625 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=418.925 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=417.4625 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=416.8625 \| 5. component:opentitan [component] @ __graphify_spec_only__/components.md, score=380.975 |

### userqa_068 (user_code_to_spec_why, L5)

**Question**: `prim_secded_inv_72_64_enc`가 왜 필요한지 spec 기준으로 설명해줘. `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_ecc_reg.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_testplan.hjson`와 code artifact `prim_secded_inv_72_64_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_ecc_reg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: otp_ctrl_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv:L39

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl, otp_ctrl_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=727.9125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=723.1 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=691.7625 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=619.15 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=557.9875 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=120.875 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=119.875 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=117.8 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=113.5625 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=112.8125 |
| spec-code | 3 | 1 | 3 | spec=Y, code=Y, joint=Y | 1. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1088.75 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1078.0 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=1073.5875 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1038.9 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1036.725 |

### userqa_069 (user_review_trace, L5)

**Question**: 리뷰할 때 `otp_ctrl`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_testplan.hjson`와 code artifact `prim_sec_anchor_flop`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_kdi.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: otp_ctrl_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv:L275

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_kdi.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=312.1875 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=115.0625 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=107.1875 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=104.9375 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=91.4375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=52.5375 \| 2. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=46.3125 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=46.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=44.375 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=483.6375 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=186.3875 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=169.875 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=168.9375 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=163.7125 |

### userqa_070 (user_verification_coverage, L4)

**Question**: `otp_ctrl` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson`와 연결된 code 쪽도 알려줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_testplan.hjson`와 code artifact `prim_sum_tree`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_dai.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: otp_ctrl_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sum_tree [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_dai.sv:L944

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_testplan.hjson, otp_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1178.975 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=952.0875 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=885.5 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=862.575 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=828.35 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=113.8125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.775 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.875 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=94.4375 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=92.5625 |
| spec-code | 9 | - | - | spec=N, code=N, joint=N | 1. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1449.425 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1447.4875 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1428.1 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1427.425 \| 5. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1383.3125 |

### userqa_071 (user_change_impact, L5)

**Question**: `otp_ctrl` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_testplan.hjson`와 code artifact `otp_ctrl_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: otp_ctrl_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L13

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=312.1875 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=115.0625 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=107.1875 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=104.9375 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=91.4375 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=52.5375 \| 2. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=46.3125 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=46.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=44.375 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 |
| spec-code | 1 | 6 | 6 | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=483.6375 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=186.3875 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=169.875 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=168.9375 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=163.7125 |

### userqa_072 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `otp_ctrl`는 `top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_testplan.hjson`와 code artifact `prim_util_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: otp_ctrl_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_util_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_util_pkg, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1178.975 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=952.0875 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=885.5 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=862.575 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=828.35 |
| code-only | - | 15 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=74.4375 \| 2. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=68.5625 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=65.925 \| 4. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=65.125 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=62.25 |
| spec-code | 10 | - | - | spec=N, code=N, joint=N | 1. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1444.8625 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1443.675 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1424.575 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1424.575 \| 5. adc_ctrl [code] @ opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv, score=1381.4375 |

### userqa_073 (user_spec_to_code_explain, L4)

**Question**: `otp_ctrl` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `otp_ctrl_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_testplan.hjson`와 code artifact `otp_ctrl_macro_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: otp_ctrl_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L15

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl, otp_ctrl_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=406.8625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=389.4625 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=352.5375 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=340.8125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=54.3 \| 2. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=49.125 \| 3. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=48.0625 \| 4. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=46.5625 \| 5. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=45.25 |
| spec-code | 1 | 26 | 26 | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=596.3125 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=401.925 \| 3. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=401.1125 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=389.4625 \| 5. component:opentitan [component] @ __graphify_spec_only__/components.md, score=352.5375 |

### userqa_074 (user_code_to_spec_why, L5)

**Question**: `otp_macro_pkg`가 왜 필요한지 spec 기준으로 설명해줘. `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_testplan.hjson`와 code artifact `otp_macro_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: otp_ctrl_testplan.hjson [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl.sv:L21

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_testplan.hjson, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=728.2625 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=724.2375 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=696.6625 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=618.7125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=558.5125 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=113.3125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=105.0125 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.0625 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=92.625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=90.8125 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=1087.4875 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1082.65 \| 3. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1081.9 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1041.6 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1040.7375 |

### userqa_075 (user_review_trace, L5)

**Question**: 리뷰할 때 `otp_ctrl`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `interfaces.md`와 code artifact `prim_secded_inv_72_64_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_ecc_reg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv:L39

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, otp_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=312.1875 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=115.0625 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=107.1875 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=104.9375 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=91.4375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=52.5375 \| 2. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=46.3125 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=46.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=44.375 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=483.6375 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=186.3875 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=169.875 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=168.9375 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=163.7125 |

### userqa_076 (user_verification_coverage, L4)

**Question**: `otp_ctrl` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md`와 연결된 code 쪽도 알려줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `interfaces.md`와 code artifact `prim_sec_anchor_flop`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_kdi.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv:L275

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1142.225 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=970.4625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=968.625 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=840.7125 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=795.275 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=113.1875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=102.375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.5625 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=92.6875 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=89.75 |
| spec-code | 5 | 1 | 5 | spec=Y, code=Y, joint=Y | 1. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1206.4 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1204.3375 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1164.85 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1164.175 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=1160.225 |

### userqa_077 (user_change_impact, L5)

**Question**: `otp_ctrl` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `interfaces.md`와 code artifact `prim_sum_tree`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_dai.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sum_tree [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_dai.sv:L944

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_sum_tree, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_dai.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=312.1875 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=115.0625 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=107.1875 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=104.9375 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=91.4375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=52.5375 \| 2. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=46.3125 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=46.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=44.375 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 |
| spec-code | 1 | 11 | 11 | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=483.6375 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=186.3875 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=169.875 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=168.9375 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=163.7125 |

### userqa_078 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `otp_ctrl`는 `top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `interfaces.md`와 code artifact `otp_ctrl_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L13

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl, interfaces.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1142.225 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=970.4625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=968.625 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=840.7125 \| 5. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=795.275 |
| code-only | - | 15 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=73.8125 \| 2. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=65.75 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=63.8125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=63.525 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=61.125 |
| spec-code | 5 | - | - | spec=Y, code=N, joint=N | 1. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1201.7125 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1200.65 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1161.325 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1161.325 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=1142.225 |

### userqa_079 (user_spec_to_code_explain, L4)

**Question**: `otp_ctrl` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `interfaces.md` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `interfaces.md`와 code artifact `prim_util_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_util_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=325.8375 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=268.9 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=143.4125 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=113.3375 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=107.1875 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=52.5375 \| 2. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=46.3125 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=46.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=44.375 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 |
| spec-code | 1 | 8 | 8 | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=497.2875 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=268.9 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=194.7875 \| 4. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=186.075 \| 5. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=185.1375 |

### userqa_080 (user_code_to_spec_why, L5)

**Question**: `otp_ctrl_macro_pkg`가 왜 필요한지 spec 기준으로 설명해줘. `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `interfaces.md`와 code artifact `otp_ctrl_macro_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L15

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, otp_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=737.275 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=726.075 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=698.7625 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=618.8 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=586.3375 |
| code-only | - | 16 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=113.875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=106.5875 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=101.0 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=95.0625 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.8125 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=1117.9375 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1090.875 \| 3. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1090.1875 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1048.425 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1047.525 |

### userqa_081 (user_review_trace, L5)

**Question**: 리뷰할 때 `otp_ctrl`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `interfaces.md`와 code artifact `otp_macro_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl.sv:L21

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_earlgrey/ip_autogen/otp_ctrl/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=312.1875 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=115.0625 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=107.1875 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=104.9375 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=91.4375 |
| code-only | - | 20 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=52.5375 \| 2. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=46.3125 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=46.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=44.375 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=483.6375 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=186.3875 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=169.875 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=168.9375 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=163.7125 |

### userqa_082 (user_verification_coverage, L4)

**Question**: `otp_ctrl` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md`와 연결된 code 쪽도 알려줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_secded_inv_72_64_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_ecc_reg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv:L39

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_secded_inv_72_64_enc, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_ecc_reg.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1801.875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1142.225 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1025.5875 \| 4. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=834.125 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=682.7625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=113.1875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=102.375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.5625 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=92.6875 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=89.75 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1801.875 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1237.45 \| 3. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1235.3875 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1200.625 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1199.95 |

### userqa_083 (user_change_impact, L5)

**Question**: `otp_ctrl` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_sec_anchor_flop`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_kdi.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv:L275

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=312.1875 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=115.0625 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=107.1875 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=104.9375 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=91.4375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=52.5375 \| 2. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=46.3125 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=46.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=44.375 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=483.6375 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=186.3875 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=169.875 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=168.9375 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=163.7125 |

### userqa_084 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `otp_ctrl`는 `top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_sum_tree`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_dai.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_sum_tree [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_dai.sv:L944

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_dai.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1801.875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1142.225 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1025.5875 \| 4. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=834.125 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=682.7625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=73.8125 \| 2. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=65.75 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=63.8125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=63.525 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=61.125 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1801.875 \| 2. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1232.7625 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1231.7 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1197.1 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1197.1 |

### userqa_085 (user_spec_to_code_explain, L4)

**Question**: `otp_ctrl` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `theory_of_operation.md` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `otp_ctrl_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L13

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, otp_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=928.625 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=364.6875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=200.375 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=153.5 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=121.5625 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=52.5375 \| 2. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=46.3125 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=46.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=44.375 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=928.625 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=536.1375 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=234.95 \| 4. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=217.125 \| 5. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=216.1875 |

### userqa_086 (user_code_to_spec_why, L5)

**Question**: `prim_util_pkg`가 왜 필요한지 spec 기준으로 설명해줘. `top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_util_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: prim_util_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=731.7625 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=723.1 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=694.125 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=618.7125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=585.375 |
| code-only | - | 24 | - | spec=N, code=N, joint=N | 1. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=149.8125 \| 2. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=132.6875 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=120.125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=119.65 \| 5. .append() [code] @ opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py, score=113.0625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=1088.55 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1081.6 \| 3. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1079.5375 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1044.65 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1042.25 |

### userqa_087 (user_review_trace, L5)

**Question**: 리뷰할 때 `otp_ctrl`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `otp_ctrl_macro_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_ctrl_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_top_specific_pkg.sv:L15

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl_macro_pkg, top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_top_specific_pkg.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=312.1875 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=115.0625 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=107.1875 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=104.9375 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=91.4375 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=52.5375 \| 2. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=46.3125 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=46.1875 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=44.375 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=40.0 |
| spec-code | 1 | 6 | 6 | spec=Y, code=N, joint=N | 1. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=483.6375 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=186.3875 \| 3. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=169.875 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=168.9375 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=163.7125 |

### userqa_088 (user_verification_coverage, L4)

**Question**: `otp_ctrl` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md`와 연결된 code 쪽도 알려줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `otp_macro_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/doc/theory_of_operation.md | component:otp_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_otp_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +4 more

**Gold code answer**: otp_macro_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl.sv:L21

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: otp_ctrl, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1801.875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1142.225 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1025.5875 \| 4. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=834.125 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=682.7625 |
| code-only | - | 13 | - | spec=N, code=N, joint=N | 1. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=113.1875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=102.375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.5625 \| 4. prim_flop [code] @ opentitan\hw\vendor\lowrisc_ibex\rtl\ibex_lockstep.sv, score=92.6875 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=89.75 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1801.875 \| 2. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=1237.45 \| 3. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=1235.3875 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1200.625 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1199.95 |

### userqa_089 (user_change_impact, L5)

**Question**: `flash_ctrl` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_sec_cm_testplan.hjson`와 code artifact `prim_arbiter_tree`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_arbiter_tree [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L163

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=467.8875 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=191.2 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=154.9625 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=126.5625 \| 5. component:sysrst_ctrl [component] @ __graphify_spec_only__/components.md, score=120.075 |

### userqa_090 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `flash_ctrl`는 `top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_sec_cm_testplan.hjson`와 code artifact `prim_count`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_core.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv:L240

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_sec_cm_testplan.hjson, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1106.9625 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=903.875 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=858.9 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=824.1625 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=798.95 |
| code-only | - | 6 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=71.7625 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=66.1875 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.9375 \| 4. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=65.6875 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=64.625 |
| spec-code | 1 | 9 | 9 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1167.95 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1106.9625 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1033.9875 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1033.8 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=982.825 |

### userqa_091 (user_spec_to_code_explain, L4)

**Question**: `flash_ctrl` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `flash_ctrl_sec_cm_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_sec_cm_testplan.hjson`와 code artifact `prim_secded_hamming_72_64_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_72_64_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L775

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=402.6625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=396.6375 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=366.275 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=358.1375 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=63.75 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=60.4375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=59.4375 \| 5. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=58.65 |
| spec-code | 1 | 16 | 16 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=592.1125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=396.6375 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=366.275 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=358.1375 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=342.35 |

### userqa_092 (user_code_to_spec_why, L5)

**Question**: `prim_secded_hamming_76_68_enc`가 왜 필요한지 spec 기준으로 설명해줘. `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_prog.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_sec_cm_testplan.hjson`와 code artifact `prim_secded_hamming_76_68_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_prog.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv:L334

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_secded_hamming_76_68_enc, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_prog.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=671.5625 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=637.6875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=622.65 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=580.5625 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=526.925 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=122.8125 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=110.9375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.375 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.4375 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=90.375 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1025.1375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=757.0875 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=739.6625 \| 4. prim_secded_hamming_72_64_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv, score=686.225 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=680.1375 |

### userqa_093 (user_review_trace, L5)

**Question**: 리뷰할 때 `flash_ctrl`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_sec_cm_testplan.hjson`와 code artifact `prim_secded_hamming_76_68_dec`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_dec [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L435

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl, flash_ctrl_sec_cm_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=467.8875 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=191.2 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=154.9625 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=126.5625 \| 5. component:sysrst_ctrl [component] @ __graphify_spec_only__/components.md, score=120.075 |

### userqa_094 (user_verification_coverage, L4)

**Question**: `flash_ctrl` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`와 연결된 code 쪽도 알려줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_sec_cm_testplan.hjson`와 code artifact `flash_ctrl_top_specific_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_ctrl_top_specific_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv:L14

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1106.9625 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=903.875 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=858.9 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=824.1625 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=798.95 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=110.6125 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=105.3125 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=96.9375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.0625 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=90.75 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1204.4 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1106.9625 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1037.5125 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1036.65 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=988.575 |

### userqa_095 (user_change_impact, L5)

**Question**: `flash_ctrl` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_sec_cm_testplan.hjson`와 code artifact `flash_phy_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_scramble.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_phy_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_scramble.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_sec_cm_testplan.hjson, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | 26 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 9 | 9 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=467.8875 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=191.2 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=154.9625 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=126.5625 \| 5. component:sysrst_ctrl [component] @ __graphify_spec_only__/components.md, score=120.075 |

### userqa_096 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `flash_ctrl`는 `top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_sec_cm_testplan.hjson`와 code artifact `rst_shadowed_if`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/dv/tb/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: rst_shadowed_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv:L50

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1106.9625 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=903.875 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=858.9 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=824.1625 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=798.95 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=71.7625 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=66.1875 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.9375 \| 4. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=65.6875 \| 5. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=64.625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1167.95 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1106.9625 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1033.9875 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1033.8 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=982.825 |

### userqa_097 (user_spec_to_code_explain, L4)

**Question**: `flash_ctrl` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `flash_ctrl_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_testplan.hjson`와 code artifact `prim_arbiter_tree`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_arbiter_tree [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L163

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_arbiter_tree, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=398.725 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=369.075 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=338.275 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=330.1375 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=60.4375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=59.4375 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=58.65 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=53.075 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=48.4375 |
| spec-code | 1 | 17 | 17 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=588.175 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=369.075 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=338.275 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=330.1375 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=326.475 |

### userqa_098 (user_code_to_spec_why, L5)

**Question**: `prim_count`가 왜 필요한지 spec 기준으로 설명해줘. `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_core.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_testplan.hjson`와 code artifact `prim_count`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_core.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv:L240

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl, flash_ctrl_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=692.125 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=638.5625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=638.4 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=598.0625 \| 5. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=542.0 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=126.5 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=112.5 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=98.5 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=97.8125 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.25 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1028.2625 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=808.4 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=800.15 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=758.4125 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=702.3375 |

### userqa_099 (user_review_trace, L5)

**Question**: 리뷰할 때 `flash_ctrl`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_testplan.hjson`와 code artifact `prim_secded_hamming_72_64_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_72_64_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L775

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=467.8875 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=191.2 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=154.9625 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=126.5625 \| 5. component:sysrst_ctrl [component] @ __graphify_spec_only__/components.md, score=120.075 |

### userqa_100 (user_verification_coverage, L4)

**Question**: `flash_ctrl` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson`와 연결된 code 쪽도 알려줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_testplan.hjson`와 code artifact `prim_secded_hamming_76_68_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_prog.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv:L334

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_testplan.hjson, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1079.4 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=875.875 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=858.9 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=796.1625 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=795.0125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=110.6125 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=105.3125 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=96.9375 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.0625 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=90.75 |
| spec-code | 1 | 23 | 23 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1200.4625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1079.4 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1020.45 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1019.775 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=972.7 |

### userqa_101 (user_change_impact, L5)

**Question**: `flash_ctrl` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_testplan.hjson`와 code artifact `prim_secded_hamming_76_68_dec`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_dec [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L435

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=467.8875 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=191.2 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=154.9625 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=126.5625 \| 5. component:sysrst_ctrl [component] @ __graphify_spec_only__/components.md, score=120.075 |

### userqa_102 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `flash_ctrl`는 `top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_testplan.hjson`와 code artifact `flash_ctrl_top_specific_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_ctrl_top_specific_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv:L14

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_top_specific_pkg, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1079.4 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=875.875 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=858.9 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=796.1625 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=795.0125 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=71.7625 \| 2. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=66.1875 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.9375 \| 4. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=64.625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=64.4375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1164.0125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1079.4 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1016.925 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=1016.925 \| 5. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=967.3875 |

### userqa_103 (user_spec_to_code_explain, L4)

**Question**: `flash_ctrl` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `flash_ctrl_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_testplan.hjson`와 code artifact `flash_phy_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_scramble.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_phy_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_scramble.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl, flash_ctrl_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=398.725 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=369.075 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=338.275 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=330.1375 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=213.325 |
| code-only | - | 28 | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=60.4375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=59.4375 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=58.65 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=53.075 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=48.4375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=588.175 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=369.075 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=338.275 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=330.1375 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=326.475 |

### userqa_104 (user_code_to_spec_why, L5)

**Question**: `rst_shadowed_if`가 왜 필요한지 spec 기준으로 설명해줘. `ip_autogen/flash_ctrl/dv/tb/tb.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `flash_ctrl_testplan.hjson`와 code artifact `rst_shadowed_if`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/dv/tb/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: rst_shadowed_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv:L50

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson, ip_autogen/flash_ctrl/dv/tb/tb.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=457.0 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=421.75 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=374.5 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=364.4375 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=316.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.5 \| 2. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 3. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.8125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=44.5 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=42.8125 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=682.0 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=421.75 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=418.875 \| 4. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=378.3125 \| 5. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=378.0 |

### userqa_105 (user_review_trace, L5)

**Question**: 리뷰할 때 `flash_ctrl`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `interfaces.md`와 code artifact `prim_arbiter_tree`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_arbiter_tree [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L163

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=467.8875 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=191.2 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=154.9625 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=126.5625 \| 5. component:sysrst_ctrl [component] @ __graphify_spec_only__/components.md, score=120.075 |

### userqa_106 (user_verification_coverage, L4)

**Question**: `flash_ctrl` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md`와 연결된 code 쪽도 알려줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `interfaces.md`와 code artifact `prim_count`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_core.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv:L240

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1092.7 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=932.4 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=871.675 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=801.25 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=736.825 |
| code-only | - | 8 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=107.7625 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.8125 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.5625 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=89.875 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=89.5625 |
| spec-code | 1 | 6 | 6 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1124.275 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1092.7 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=932.4 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=871.675 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=847.1125 |

### userqa_107 (user_change_impact, L5)

**Question**: `flash_ctrl` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `interfaces.md`와 code artifact `prim_secded_hamming_72_64_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_72_64_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L775

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_secded_hamming_72_64_enc, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=467.8875 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=191.2 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=154.9625 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=126.5625 \| 5. component:sysrst_ctrl [component] @ __graphify_spec_only__/components.md, score=120.075 |

### userqa_108 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `flash_ctrl`는 `top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `interfaces.md`와 code artifact `prim_secded_hamming_76_68_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_prog.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv:L334

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl, interfaces.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1092.7 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=932.4 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=871.675 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=801.25 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=736.825 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=68.9125 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.4375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=64.8125 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=62.125 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=62.125 |
| spec-code | 1 | 20 | 20 | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1092.7 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1087.825 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=932.4 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=871.675 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=808.2625 |

### userqa_109 (user_spec_to_code_explain, L4)

**Question**: `flash_ctrl` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `interfaces.md` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `interfaces.md`와 code artifact `prim_secded_hamming_76_68_dec`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_dec [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L435

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=304.8375 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=263.65 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=125.475 \| 4. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=123.4 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=476.2875 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=263.65 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=204.85 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=169.6625 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=137.3625 |

### userqa_110 (user_code_to_spec_why, L5)

**Question**: `flash_ctrl_top_specific_pkg`가 왜 필요한지 spec 기준으로 설명해줘. `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `interfaces.md`와 code artifact `flash_ctrl_top_specific_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_ctrl_top_specific_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv:L14

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=674.0125 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=650.2 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=630.525 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=580.9125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=559.3 |
| code-only | - | 12 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=113.6625 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=105.0 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=100.625 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.625 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=94.25 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1066.0 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=753.3375 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=746.55 \| 4. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=689.9125 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=687.2 |

### userqa_111 (user_review_trace, L5)

**Question**: 리뷰할 때 `flash_ctrl`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `interfaces.md`와 code artifact `flash_phy_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_scramble.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_phy_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_scramble.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | 26 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 9 | 9 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=467.8875 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=191.2 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=154.9625 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=126.5625 \| 5. component:sysrst_ctrl [component] @ __graphify_spec_only__/components.md, score=120.075 |

### userqa_112 (user_verification_coverage, L4)

**Question**: `flash_ctrl` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md`와 연결된 code 쪽도 알려줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `interfaces.md`와 code artifact `rst_shadowed_if`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/dv/tb/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: rst_shadowed_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv:L50

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rst_shadowed_if, ip_autogen/flash_ctrl/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1092.7 \| 2. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=932.4 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=871.675 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=801.25 \| 5. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=736.825 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=107.7625 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.8125 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.5625 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=89.875 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=89.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1124.275 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1092.7 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=932.4 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=871.675 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=847.1125 |

### userqa_113 (user_change_impact, L5)

**Question**: `flash_ctrl` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_arbiter_tree`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_arbiter_tree [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L163

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=467.8875 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=191.2 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=154.9625 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=126.5625 \| 5. component:sysrst_ctrl [component] @ __graphify_spec_only__/components.md, score=120.075 |

### userqa_114 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `flash_ctrl`는 `top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_count`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_core.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv:L240

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_core.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1763.8125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1092.7 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=928.6375 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=776.9875 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=657.2125 |
| code-only | - | 7 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=68.9125 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.4375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=64.8125 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=62.125 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=62.125 |
| spec-code | 1 | 7 | 7 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1763.8125 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1127.9875 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=1092.7 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=928.6375 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=839.9875 |

### userqa_115 (user_spec_to_code_explain, L4)

**Question**: `flash_ctrl` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `theory_of_operation.md` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_secded_hamming_72_64_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_72_64_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L775

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=925.125 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=345.0 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=182.4375 \| 4. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=162.25 \| 5. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=112.8125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 10 | 10 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=925.125 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=516.45 \| 3. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=243.7 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=196.9625 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=182.4375 |

### userqa_116 (user_code_to_spec_why, L5)

**Question**: `prim_secded_hamming_76_68_enc`가 왜 필요한지 spec 기준으로 설명해줘. `top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_prog.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_secded_hamming_76_68_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_prog.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_prog.sv:L334

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=671.5625 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=637.6875 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=622.65 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=580.5625 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=526.925 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=122.8125 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=110.9375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.375 \| 4. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.4375 \| 5. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=90.375 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1025.1375 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=757.0875 \| 3. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=739.6625 \| 4. prim_secded_hamming_72_64_enc [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv, score=686.225 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=680.1375 |

### userqa_117 (user_review_trace, L5)

**Question**: 리뷰할 때 `flash_ctrl`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_secded_hamming_76_68_dec`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: prim_secded_hamming_76_68_dec [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_rd.sv:L435

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_secded_hamming_76_68_dec, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_rd.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=467.8875 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=191.2 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=154.9625 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=126.5625 \| 5. component:sysrst_ctrl [component] @ __graphify_spec_only__/components.md, score=120.075 |

### userqa_118 (user_verification_coverage, L4)

**Question**: `flash_ctrl` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md`와 연결된 code 쪽도 알려줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `flash_ctrl_top_specific_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_ctrl_top_specific_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv:L14

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1763.8125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1092.7 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=928.6375 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=776.9875 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=657.2125 |
| code-only | - | 14 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=107.7625 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=104.8125 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=95.5625 \| 4. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=89.875 \| 5. prim_subreg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=89.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1763.8125 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1164.4375 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=1092.7 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=928.6375 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=878.8375 |

### userqa_119 (user_change_impact, L5)

**Question**: `flash_ctrl` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `flash_phy_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_scramble.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: flash_phy_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_scramble.sv:L12

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md, top_englishbreakfast/ip_autogen/flash_ctrl/rtl/flash_phy_scramble.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | 26 | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=57.225 \| 2. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 3. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 4. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.85 \| 5. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=45.5625 |
| spec-code | 1 | 9 | 9 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=467.8875 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=191.2 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=154.9625 \| 4. prim_count [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy_core.sv, score=126.5625 \| 5. component:sysrst_ctrl [component] @ __graphify_spec_only__/components.md, score=120.075 |

### userqa_120 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `flash_ctrl`는 `top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `flash_ctrl`는 spec 문서 `theory_of_operation.md`와 code artifact `rst_shadowed_if`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/dv/tb/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: rst_shadowed_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv:L50

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1763.8125 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1092.7 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=928.6375 \| 4. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=776.9875 \| 5. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=657.2125 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=68.9125 \| 2. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=65.4375 \| 3. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=64.8125 \| 4. prim_reg_we_check [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=62.125 \| 5. tlul_adapter_reg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=62.125 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1763.8125 \| 2. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=1127.9875 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=1092.7 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=928.6375 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=839.9875 |

### userqa_121 (user_spec_to_code_explain, L4)

**Question**: `rv_core_ibex` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `rv_core_ibex_sec_cm_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_sec_cm_testplan.hjson`와 code artifact `prim_mubi_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L905

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=485.6125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=355.8625 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=341.6875 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=341.425 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=203.4375 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=365.3125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=69.0625 |
| spec-code | 1 | 7 | 7 | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=684.5125 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=365.3125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=355.8625 \| 4. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 5. component:opentitan [component] @ __graphify_spec_only__/components.md, score=341.6875 |

### userqa_122 (user_code_to_spec_why, L5)

**Question**: `prim_esc_receiver`가 왜 필요한지 spec 기준으로 설명해줘. `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_sec_cm_testplan.hjson`와 code artifact `prim_esc_receiver`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L283

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_esc_receiver, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=815.925 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=628.5125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=592.725 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=544.6875 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=523.6 |
| code-only | - | 3 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.5 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=118.65 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.6875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.8125 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1192.125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=846.525 \| 3. prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=761.25 \| 4. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=761.0 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=678.2625 |

### userqa_123 (user_review_trace, L5)

**Question**: 리뷰할 때 `rv_core_ibex`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_sec_cm_testplan.hjson`와 code artifact `prim_arbiter_fixed`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex_addr_trans.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv:L58

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex, rv_core_ibex_sec_cm_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=379.5625 \| 2. component:boot [component] @ __graphify_spec_only__/components.md, score=67.375 \| 3. component:rom [component] @ __graphify_spec_only__/components.md, score=64.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=63.4375 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=62.5625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.3125 |
| spec-code | 1 | 5 | 5 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=560.4625 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=170.6625 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=130.9375 |

### userqa_124 (user_verification_coverage, L4)

**Question**: `rv_core_ibex` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson`와 연결된 code 쪽도 알려줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_sec_cm_testplan.hjson`와 code artifact `prim_sync_reqack_data`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sync_reqack_data [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L376

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1062.3375 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=965.8125 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=876.8375 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=848.925 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=805.2625 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=367.25 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=108.1875 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.65 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.25 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1360.0125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1062.3375 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=1050.775 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=991.3875 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=989.625 |

### userqa_125 (user_change_impact, L5)

**Question**: `rv_core_ibex` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_sec_cm_testplan.hjson`와 code artifact `prim_lc_sync`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sync [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L325

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_sec_cm_testplan.hjson, rv_core_ibex, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=379.5625 \| 2. component:boot [component] @ __graphify_spec_only__/components.md, score=67.375 \| 3. component:rom [component] @ __graphify_spec_only__/components.md, score=64.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=63.4375 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=62.5625 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.3125 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=560.4625 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=170.6625 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=130.9375 |

### userqa_126 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `rv_core_ibex`는 `top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_sec_cm_testplan.hjson`와 code artifact `prim_lc_sender`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sender [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L406

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1062.3375 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=965.8125 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=876.8375 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=848.925 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=805.2625 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=367.25 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=72.875 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1314.1125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1062.3375 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=1011.925 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=987.8625 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=986.775 |

### userqa_127 (user_spec_to_code_explain, L4)

**Question**: `rv_core_ibex` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `rv_core_ibex_sec_cm_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_sec_cm_testplan.hjson`와 code artifact `tlul_adapter_host`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: tlul_adapter_host [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L668

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tlul_adapter_host, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=485.6125 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=355.8625 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=341.6875 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=341.425 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=203.4375 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=365.3125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=69.0625 |
| spec-code | 1 | 7 | 7 | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=684.5125 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=365.3125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=355.8625 \| 4. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 5. component:opentitan [component] @ __graphify_spec_only__/components.md, score=341.6875 |

### userqa_128 (user_code_to_spec_why, L5)

**Question**: `prim_mubi_pkg`가 왜 필요한지 spec 기준으로 설명해줘. `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_testplan.hjson`와 code artifact `prim_mubi_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L905

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex, rv_core_ibex_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=815.925 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=628.5125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=590.5375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=544.6875 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=521.85 |
| code-only | - | 3 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.5 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=122.775 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.6875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.8125 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1200.0 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=850.65 \| 3. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=761.0 \| 4. prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=756.25 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=685.0125 |

### userqa_129 (user_review_trace, L5)

**Question**: 리뷰할 때 `rv_core_ibex`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_testplan.hjson`와 code artifact `prim_esc_receiver`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L283

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=379.5625 \| 2. component:boot [component] @ __graphify_spec_only__/components.md, score=67.375 \| 3. component:rom [component] @ __graphify_spec_only__/components.md, score=64.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=63.4375 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=62.5625 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.3125 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=560.4625 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=170.6625 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=130.9375 |

### userqa_130 (user_verification_coverage, L4)

**Question**: `rv_core_ibex` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson`와 연결된 code 쪽도 알려줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_testplan.hjson`와 code artifact `prim_arbiter_fixed`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex_addr_trans.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv:L58

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_testplan.hjson, rv_core_ibex, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1034.775 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=960.5625 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=848.925 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=848.8375 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=777.2625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=307.25 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=108.1875 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=104.65 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.25 |
| spec-code | 1 | 6 | 6 | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1354.7625 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=1037.275 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1034.775 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=974.325 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=972.75 |

### userqa_131 (user_change_impact, L5)

**Question**: `rv_core_ibex` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_testplan.hjson`와 code artifact `prim_sync_reqack_data`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sync_reqack_data [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L376

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=379.5625 \| 2. component:boot [component] @ __graphify_spec_only__/components.md, score=67.375 \| 3. component:rom [component] @ __graphify_spec_only__/components.md, score=64.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=63.4375 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=62.5625 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.3125 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=560.4625 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=170.6625 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=130.9375 |

### userqa_132 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `rv_core_ibex`는 `top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_testplan.hjson`와 code artifact `prim_sec_anchor_buf`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sec_anchor_buf [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L359

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_sec_anchor_buf, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 2 | - | - | spec=Y, code=N, joint=N | 1. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1034.775 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=960.5625 \| 3. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=848.925 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=848.8375 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=777.2625 |
| code-only | - | 8 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=307.25 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=72.5625 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1308.8625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=1034.775 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=998.425 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=970.8 \| 5. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=969.9 |

### userqa_133 (user_spec_to_code_explain, L4)

**Question**: `rv_core_ibex` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `rv_core_ibex_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_testplan.hjson`와 code artifact `prim_lc_sync`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sync [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L325

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex, rv_core_ibex_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=480.3625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=328.3 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=313.6875 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=313.425 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=203.4375 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=305.3125 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=68.75 |
| spec-code | 1 | 6 | 6 | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=679.2625 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=328.3 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=313.6875 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=313.425 \| 5. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=305.3125 |

### userqa_134 (user_code_to_spec_why, L5)

**Question**: `prim_lc_sender`가 왜 필요한지 spec 기준으로 설명해줘. `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_testplan.hjson`와 code artifact `prim_lc_sender`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sender [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L406

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=815.925 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=628.5125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=590.5375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=544.6875 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=521.85 |
| code-only | - | 3 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.5 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=121.275 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.6875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.8125 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1192.125 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=849.15 \| 3. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=761.0 \| 4. prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=756.25 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=678.2625 |

### userqa_135 (user_review_trace, L5)

**Question**: 리뷰할 때 `rv_core_ibex`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_testplan.hjson`와 code artifact `tlul_adapter_host`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: rv_core_ibex_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_testplan.hjson | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: tlul_adapter_host [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L668

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex_testplan.hjson, rv_core_ibex, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=379.5625 \| 2. component:boot [component] @ __graphify_spec_only__/components.md, score=67.375 \| 3. component:rom [component] @ __graphify_spec_only__/components.md, score=64.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=63.4375 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=62.5625 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.3125 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=560.4625 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=170.6625 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=130.9375 |

### userqa_136 (user_verification_coverage, L4)

**Question**: `rv_core_ibex` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md`와 연결된 code 쪽도 알려줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `interfaces.md`와 code artifact `prim_mubi_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L905

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1047.4625 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=929.325 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=896.4375 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=830.9875 \| 5. component:interfaces [component] @ __graphify_spec_only__/components.md, score=764.0625 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.5 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=107.8125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=103.525 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.875 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1305.525 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1047.4625 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=935.35 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=896.4375 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=862.45 |

### userqa_137 (user_change_impact, L5)

**Question**: `rv_core_ibex` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `interfaces.md`와 code artifact `prim_esc_receiver`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L283

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_esc_receiver, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=379.5625 \| 2. component:boot [component] @ __graphify_spec_only__/components.md, score=67.375 \| 3. component:rom [component] @ __graphify_spec_only__/components.md, score=64.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=63.4375 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=62.5625 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.3125 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=560.4625 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=170.6625 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=130.9375 |

### userqa_138 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `rv_core_ibex`는 `top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `interfaces.md`와 code artifact `prim_arbiter_fixed`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex_addr_trans.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv:L58

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex, interfaces.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1047.4625 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=929.325 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=896.4375 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=830.9875 \| 5. component:interfaces [component] @ __graphify_spec_only__/components.md, score=764.0625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.5 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=71.0 |
| spec-code | 1 | 5 | 5 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1259.625 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1047.4625 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=896.5 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=896.4375 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=856.825 |

### userqa_139 (user_spec_to_code_explain, L4)

**Question**: `rv_core_ibex` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `interfaces.md` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `interfaces.md`와 code artifact `prim_sync_reqack_data`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sync_reqack_data [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L376

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=387.4375 \| 2. component:interfaces [component] @ __graphify_spec_only__/components.md, score=226.4625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=91.7875 \| 4. component:security [component] @ __graphify_spec_only__/components.md, score=72.1 \| 5. component:boot [component] @ __graphify_spec_only__/components.md, score=70.525 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.625 |
| spec-code | 1 | 5 | 5 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=568.3375 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 4. component:interfaces [component] @ __graphify_spec_only__/components.md, score=226.4625 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=182.8125 |

### userqa_140 (user_code_to_spec_why, L5)

**Question**: `prim_sec_anchor_buf`가 왜 필요한지 spec 기준으로 설명해줘. `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `interfaces.md`와 code artifact `prim_sec_anchor_buf`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sec_anchor_buf [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L359

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, rv_core_ibex, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=822.4875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=628.5125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=618.1 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=544.6875 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=521.85 |
| code-only | - | 3 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=362.5 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=341.925 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=118.8375 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=114.6875 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.8125 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1198.6875 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=860.2125 \| 3. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=774.5 \| 4. prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=769.75 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=688.7625 |

### userqa_141 (user_review_trace, L5)

**Question**: 리뷰할 때 `rv_core_ibex`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `interfaces.md`와 code artifact `prim_lc_sync`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sync [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L325

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=379.5625 \| 2. component:boot [component] @ __graphify_spec_only__/components.md, score=67.375 \| 3. component:rom [component] @ __graphify_spec_only__/components.md, score=64.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=63.4375 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=62.5625 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.3125 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=560.4625 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=170.6625 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=130.9375 |

### userqa_142 (user_verification_coverage, L4)

**Question**: `rv_core_ibex` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md`와 연결된 code 쪽도 알려줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `interfaces.md`와 code artifact `prim_lc_sender`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sender [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L406

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_lc_sender, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:checklist [component] @ __graphify_spec_only__/components.md, score=1047.4625 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=929.325 \| 3. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=896.4375 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=830.9875 \| 5. component:interfaces [component] @ __graphify_spec_only__/components.md, score=764.0625 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.5 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=107.8125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=103.525 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.875 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1305.525 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1047.4625 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=935.35 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=896.4375 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=862.45 |

### userqa_143 (user_change_impact, L5)

**Question**: `rv_core_ibex` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `interfaces.md`와 code artifact `tlul_adapter_host`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/interfaces.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: tlul_adapter_host [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L668

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex, interfaces.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=379.5625 \| 2. component:boot [component] @ __graphify_spec_only__/components.md, score=67.375 \| 3. component:rom [component] @ __graphify_spec_only__/components.md, score=64.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=63.4375 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=62.5625 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.3125 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=560.4625 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=170.6625 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=130.9375 |

### userqa_144 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `rv_core_ibex`는 `top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_mubi_pkg`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L905

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1727.85 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1047.4625 \| 3. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=977.8875 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=887.95 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=640.2375 |
| code-only | - | 7 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.5 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=70.6875 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1727.85 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1308.1875 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=1047.4625 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=928.225 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=888.55 |

### userqa_145 (user_spec_to_code_explain, L4)

**Question**: `rv_core_ibex` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `theory_of_operation.md` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_esc_receiver`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L283

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, rv_core_ibex, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=889.6875 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=436.0 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=148.75 \| 4. component:boot [component] @ __graphify_spec_only__/components.md, score=97.5625 \| 5. component:system [component] @ __graphify_spec_only__/components.md, score=97.5625 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.3125 |
| spec-code | 1 | 5 | 5 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=889.6875 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=616.9 \| 3. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 4. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 5. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=214.5375 |

### userqa_146 (user_code_to_spec_why, L5)

**Question**: `prim_arbiter_fixed`가 왜 필요한지 spec 기준으로 설명해줘. `top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex_addr_trans.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_arbiter_fixed`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex_addr_trans.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv:L58

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=814.0 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=628.25 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=590.1875 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=544.6875 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=523.6 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.5 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=118.6625 \| 4. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=116.0625 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=92.8125 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1215.4 \| 2. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=845.6375 \| 3. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=771.6625 \| 4. prim_esc_receiver [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=754.9125 \| 5. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=678.0 |

### userqa_147 (user_review_trace, L5)

**Question**: 리뷰할 때 `rv_core_ibex`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_sync_reqack_data`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sync_reqack_data [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L376

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: prim_sync_reqack_data, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=379.5625 \| 2. component:boot [component] @ __graphify_spec_only__/components.md, score=67.375 \| 3. component:rom [component] @ __graphify_spec_only__/components.md, score=64.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=63.4375 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=62.5625 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.3125 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=560.4625 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=170.6625 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=130.9375 |

### userqa_148 (user_verification_coverage, L4)

**Question**: `rv_core_ibex` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md`와 연결된 code 쪽도 알려줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_sec_anchor_buf`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_sec_anchor_buf [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L359

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rv_core_ibex, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1727.85 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1047.4625 \| 3. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=977.8875 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=887.95 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=640.2375 |
| code-only | - | 4 | - | spec=N, code=Y, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.5 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. prim_flop_2sync [code] @ opentitan\hw\vendor\pulp_riscv_dbg\src\dmi_cdc.sv, score=107.8125 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=103.525 \| 5. tlul_rsp_intg_gen [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_plic\rtl\rv_plic_reg_top.sv, score=91.875 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1727.85 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1354.0875 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=1047.4625 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=967.075 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=894.175 |

### userqa_149 (user_change_impact, L5)

**Question**: `rv_core_ibex` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_lc_sync`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sync [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L325

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md, top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=379.5625 \| 2. component:boot [component] @ __graphify_spec_only__/components.md, score=67.375 \| 3. component:rom [component] @ __graphify_spec_only__/components.md, score=64.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=63.4375 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=62.5625 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=65.3125 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=560.4625 \| 2. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=254.375 \| 3. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=234.9375 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=170.6625 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=130.9375 |

### userqa_150 (user_disambiguation, L5)

**Question**: 이름만 보면 헷갈리는데 `rv_core_ibex`는 `top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `theory_of_operation.md`와 code artifact `prim_lc_sender`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/doc/theory_of_operation.md | component:rv_core_ibex [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rv_core_ibex_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +1 more

**Gold code answer**: prim_lc_sender [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv:L406

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, rv_core_ibex, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1727.85 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=1047.4625 \| 3. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=977.8875 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=887.95 \| 5. component:pinmux [component] @ __graphify_spec_only__/components.md, score=640.2375 |
| code-only | - | 7 | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=302.5 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=281.925 \| 3. riscv_instr_cover_group.py [code] @ ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.625 \| 4. riscv_instr_cover_group.py [code] @ opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\pygen\pygen_src\riscv_instr_cover_group.py, score=78.375 \| 5. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=70.6875 |
| spec-code | 1 | 4 | 4 | spec=Y, code=Y, joint=Y | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=1727.85 \| 2. component:rv_core_ibex [component] @ __graphify_spec_only__/components.md, score=1308.1875 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=1047.4625 \| 4. prim_mubi_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex.sv, score=928.225 \| 5. prim_arbiter_fixed [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rv_core_ibex\rtl\rv_core_ibex_addr_trans.sv, score=888.55 |

