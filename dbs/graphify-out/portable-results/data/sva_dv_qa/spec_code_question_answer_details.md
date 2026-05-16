# Spec-Code KG Evaluation Details

- Questions: 47
- Variants: spec-only, code-only, spec-code
- Each item includes the benchmark question, gold answers, and the actual top retrieved nodes.

## Summary Table

| Task | Type | Best@10 | Gold Bridge |
|---|---|---|---|
| svadv_001 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_002 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_003 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_004 | user_verification_sva | code-only | spec_path_matches_code_path |
| svadv_005 | user_verification_sva | code-only | spec_path_matches_code_path |
| svadv_006 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_007 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_008 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_009 | user_verification_sva | code-only | spec_path_matches_code_path |
| svadv_010 | user_verification_sva | code-only | spec_path_matches_code_path |
| svadv_011 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_012 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_013 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_014 | user_verification_sva | code-only | spec_path_matches_code_path |
| svadv_015 | user_verification_sva | code-only | spec_path_matches_code_path |
| svadv_016 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_017 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_018 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_019 | user_verification_sva | spec-code | spec_path_matches_code_path |
| svadv_020 | user_verification_sva | spec-code | spec_path_matches_code_path |
| svadv_021 | user_verification_sva | spec-code | spec_path_matches_code_path |
| svadv_022 | user_verification_sva | spec-code | spec_path_matches_code_path |
| svadv_023 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_024 | user_verification_sva | spec-code | spec_path_matches_code_path |
| svadv_025 | user_verification_sva | spec-code | spec_path_matches_code_path |
| svadv_026 | user_verification_sva | spec-code | spec_path_matches_code_path |
| svadv_027 | user_verification_sva | spec-code | spec_path_matches_code_path |
| svadv_028 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_029 | user_verification_sva | spec-code | spec_path_matches_code_path |
| svadv_030 | user_verification_sva | spec-code | spec_path_matches_code_path |
| svadv_031 | user_verification_sva | spec-code | spec_path_matches_code_path |
| svadv_032 | user_verification_sva | spec-code | spec_path_matches_code_path |
| svadv_033 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_034 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_035 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_036 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_037 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_038 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_039 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_040 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_041 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_042 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_043 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_044 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_045 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_046 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |
| svadv_047 | user_verification_dv_testbench | spec-code | spec_path_matches_code_path |

## Detailed Questions

### svadv_001 (user_verification_dv_testbench, L5)

**Question**: `chip_rstmgr_testplan` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `chip_rstmgr_testplan` 검증에서는 spec `rstmgr_cnsty_chk_testplan.hjson`와 DV/testbench artifact `prim_rst_sync`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: rstmgr_cnsty_chk_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson | component:chip_rstmgr_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rstmgr_testplan_hjson [component] @ __graphify_spec_only__/components.md | component:rstmgr [component] @ __graphify_spec_only__/components.md

**Gold code answer**: prim_rst_sync [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv:L451

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rstmgr, rstmgr_cnsty_chk_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=171.0 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=110.25 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=105.4375 \| 5. component:testplan [component] @ __graphify_spec_only__/components.md, score=43.8625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .ok() [code] @ opentitan\sw\host\opentitanlib\src\transport\mod.rs, score=78.4375 \| 2. .uart() [code] @ opentitan\sw\host\ot_transports\verilator\src\transport.rs, score=26.25 \| 3. .wait_for() [code] @ opentitan\sw\host\opentitanlib\src\uart\console.rs, score=19.375 \| 4. .new() [code] @ opentitan\sw\host\tests\xmodem\xmodem.rs, score=15.9375 \| 5. .parse() [code] @ opentitan\util\py\scripts\mapfile_to_json.py, score=15.625 |
| spec-code | 1 | 15 | 15 | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=216.0 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=122.625 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=122.625 \| 4. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=118.125 \| 5. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=118.125 |

### svadv_002 (user_verification_dv_testbench, L4)

**Question**: `chip_rstmgr_testplan` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `chip_rstmgr_testplan` 검증에서는 spec `rstmgr_cnsty_chk_testplan.hjson`와 DV/testbench artifact `rstmgr_cnsty_chk_if`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: rstmgr_cnsty_chk_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson | component:chip_rstmgr_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rstmgr_testplan_hjson [component] @ __graphify_spec_only__/components.md | component:rstmgr [component] @ __graphify_spec_only__/components.md

**Gold code answer**: rstmgr_cnsty_chk_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv:L436

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rstmgr_cnsty_chk_testplan.hjson, rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson, ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=171.0 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=110.25 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=105.4375 \| 5. component:testplan [component] @ __graphify_spec_only__/components.md, score=43.8625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .ok() [code] @ opentitan\sw\host\opentitanlib\src\transport\mod.rs, score=78.4375 \| 2. .uart() [code] @ opentitan\sw\host\ot_transports\verilator\src\transport.rs, score=26.25 \| 3. .wait_for() [code] @ opentitan\sw\host\opentitanlib\src\uart\console.rs, score=19.375 \| 4. .new() [code] @ opentitan\sw\host\tests\xmodem\xmodem.rs, score=15.9375 \| 5. .parse() [code] @ opentitan\util\py\scripts\mapfile_to_json.py, score=15.625 |
| spec-code | 1 | 15 | 15 | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=216.0 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=122.625 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=122.625 \| 4. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=118.125 \| 5. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=118.125 |

### svadv_003 (user_verification_dv_testbench, L5)

**Question**: `chip_rstmgr_testplan` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `chip_rstmgr_testplan` 검증에서는 spec `rstmgr_cnsty_chk_testplan.hjson`와 DV/testbench artifact `rstmgr_cnsty_chk`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: rstmgr_cnsty_chk_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson | component:chip_rstmgr_testplan [component] @ __graphify_spec_only__/components.md | component:chip_rstmgr_testplan_hjson [component] @ __graphify_spec_only__/components.md | component:rstmgr [component] @ __graphify_spec_only__/components.md

**Gold code answer**: rstmgr_cnsty_chk [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\rstmgr\dv\rstmgr_cnsty_chk\tb.sv:L458

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rstmgr_cnsty_chk_testplan.hjson, rstmgr, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=171.0 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=110.25 \| 3. component:opentitan [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=105.4375 \| 5. component:testplan [component] @ __graphify_spec_only__/components.md, score=43.8625 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .ok() [code] @ opentitan\sw\host\opentitanlib\src\transport\mod.rs, score=78.4375 \| 2. .uart() [code] @ opentitan\sw\host\ot_transports\verilator\src\transport.rs, score=26.25 \| 3. .wait_for() [code] @ opentitan\sw\host\opentitanlib\src\uart\console.rs, score=19.375 \| 4. .new() [code] @ opentitan\sw\host\tests\xmodem\xmodem.rs, score=15.9375 \| 5. .parse() [code] @ opentitan\util\py\scripts\mapfile_to_json.py, score=15.625 |
| spec-code | 1 | 15 | 15 | spec=Y, code=N, joint=N | 1. component:rstmgr [component] @ __graphify_spec_only__/components.md, score=216.0 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=122.625 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=122.625 \| 4. prim_sec_anchor_flop [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_kdi.sv, score=118.125 \| 5. prim_secded_inv_72_64_enc [code] @ opentitan\hw\top_earlgrey\ip_autogen\otp_ctrl\rtl\otp_ctrl_ecc_reg.sv, score=118.125 |

### svadv_004 (user_verification_sva, L5)

**Question**: `ac_range_check` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `ac_range_check_testplan.hjson`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `ac_range_check_testplan.hjson`와 SVA artifact `ac_range_check_bind.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_testplan.hjson, top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson, ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=281.1375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=279.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=277.1125 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=178.15 \| 5. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=167.2 |
| code-only | - | 6 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.625 \| 2. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=17.4375 \| 3. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=12.5 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=11.2625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=281.1375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=279.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=277.1125 \| 4. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=247.75 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=227.475 |

### svadv_005 (user_verification_sva, L4)

**Question**: `ac_range_check` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `ac_range_check_testplan.hjson`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `ac_range_check_testplan.hjson`와 SVA artifact `ac_range_check_bind`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_testplan.hjson, ac_range_check, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=281.1375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=279.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=277.1125 \| 4. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=178.15 \| 5. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=167.2 |
| code-only | - | 6 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.625 \| 2. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=17.4375 \| 3. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=12.5 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=11.2625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=281.1375 \| 2. component:opentitan [component] @ __graphify_spec_only__/components.md, score=279.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=277.1125 \| 4. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=247.75 \| 5. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=227.475 |

### svadv_006 (user_verification_dv_testbench, L5)

**Question**: `ac_range_check` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `ac_range_check_testplan.hjson`와 DV/testbench artifact `tb.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_testplan.hjson, top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.375 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.0 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=186.75 \| 2. tb [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv, score=47.25 \| 3. ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv, score=45.375 \| 4. ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 \| 5. ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 |

### svadv_007 (user_verification_dv_testbench, L5)

**Question**: `ac_range_check` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `ac_range_check_testplan.hjson`와 DV/testbench artifact `ac_range_check_env_pkg`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv:L9

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_env_pkg, ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | 23 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.375 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.0 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=186.75 \| 2. tb [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv, score=47.25 \| 3. ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv, score=45.375 \| 4. ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 \| 5. ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 |

### svadv_008 (user_verification_dv_testbench, L4)

**Question**: `ac_range_check` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `ac_range_check_testplan.hjson`와 DV/testbench artifact `ac_range_check_test_pkg`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: ac_range_check_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_test_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv:L10

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check, ac_range_check_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.375 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.0 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=186.75 \| 2. tb [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv, score=47.25 \| 3. ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv, score=45.375 \| 4. ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 \| 5. ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 |

### svadv_009 (user_verification_sva, L4)

**Question**: `ac_range_check` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `interfaces.md`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `interfaces.md`와 SVA artifact `ac_range_check_bind.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=196.275 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=122.925 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=42.7875 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=38.85 \| 5. topic:security [topic] @ __graphify_spec_only__/topics.md, score=37.0125 |
| code-only | - | 6 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.6875 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.3125 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=196.275 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=195.825 \| 3. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=64.5375 \| 4. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=63.6 \| 5. ac_range_check_testplan.hjson [document] @ opentitan/hw/ip_templates/ac_range_check/data/ac_range_check_testplan.hjson, score=62.7875 |

### svadv_010 (user_verification_sva, L5)

**Question**: `ac_range_check` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `interfaces.md`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `interfaces.md`와 SVA artifact `ac_range_check_bind`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_bind, ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=196.275 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=122.925 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=42.7875 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=38.85 \| 5. topic:security [topic] @ __graphify_spec_only__/topics.md, score=37.0125 |
| code-only | - | 6 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.6875 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.3125 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 14 | 14 | spec=Y, code=N, joint=N | 1. component:interfaces [component] @ __graphify_spec_only__/components.md, score=196.275 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=195.825 \| 3. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=64.5375 \| 4. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=63.6 \| 5. ac_range_check_testplan.hjson [document] @ opentitan/hw/ip_templates/ac_range_check/data/ac_range_check_testplan.hjson, score=62.7875 |

### svadv_011 (user_verification_dv_testbench, L5)

**Question**: `ac_range_check` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `interfaces.md`와 DV/testbench artifact `tb.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check, interfaces.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.375 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.0 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=186.75 \| 2. tb [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv, score=47.25 \| 3. ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv, score=45.375 \| 4. ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 \| 5. ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 |

### svadv_012 (user_verification_dv_testbench, L4)

**Question**: `ac_range_check` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `interfaces.md`와 DV/testbench artifact `ac_range_check_env_pkg`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv:L9

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md, ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | 23 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.375 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.0 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=186.75 \| 2. tb [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv, score=47.25 \| 3. ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv, score=45.375 \| 4. ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 \| 5. ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 |

### svadv_013 (user_verification_dv_testbench, L5)

**Question**: `ac_range_check` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `interfaces.md`와 DV/testbench artifact `ac_range_check_test_pkg`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_test_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv:L10

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, ac_range_check, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.375 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.0 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=186.75 \| 2. tb [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv, score=47.25 \| 3. ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv, score=45.375 \| 4. ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 \| 5. ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 |

### svadv_014 (user_verification_sva, L5)

**Question**: `ac_range_check` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `theory_of_operation.md`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `theory_of_operation.md`와 SVA artifact `ac_range_check_bind.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=845.9375 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=127.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=99.75 \| 4. component:system [component] @ __graphify_spec_only__/components.md, score=77.875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=69.5625 |
| code-only | - | 6 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.375 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.0 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 26 | 26 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=845.9375 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=200.025 \| 3. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=116.3625 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=99.75 \| 5. component:clkmgr [component] @ __graphify_spec_only__/components.md, score=98.9625 |

### svadv_015 (user_verification_sva, L5)

**Question**: `ac_range_check` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `theory_of_operation.md`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `theory_of_operation.md`와 SVA artifact `ac_range_check_bind`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md, ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=845.9375 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=127.125 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=99.75 \| 4. component:system [component] @ __graphify_spec_only__/components.md, score=77.875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=69.5625 |
| code-only | - | 6 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.375 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.0 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 26 | 26 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=845.9375 \| 2. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=200.025 \| 3. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=116.3625 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=99.75 \| 5. component:clkmgr [component] @ __graphify_spec_only__/components.md, score=98.9625 |

### svadv_016 (user_verification_dv_testbench, L4)

**Question**: `ac_range_check` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `theory_of_operation.md`와 DV/testbench artifact `tb.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, ac_range_check, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.375 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.0 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=186.75 \| 2. tb [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv, score=47.25 \| 3. ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv, score=45.375 \| 4. ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 \| 5. ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 |

### svadv_017 (user_verification_dv_testbench, L5)

**Question**: `ac_range_check` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `theory_of_operation.md`와 DV/testbench artifact `ac_range_check_env_pkg`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv:L9

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | 23 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.375 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.0 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 3 | 3 | spec=Y, code=Y, joint=Y | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=186.75 \| 2. tb [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv, score=47.25 \| 3. ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv, score=45.375 \| 4. ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 \| 5. ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 |

### svadv_018 (user_verification_dv_testbench, L5)

**Question**: `ac_range_check` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `theory_of_operation.md`와 DV/testbench artifact `ac_range_check_test_pkg`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md | component:ac_range_check [component] @ __graphify_spec_only__/components.md | component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md | component:top_darjeeling_ac_range_check [component] @ __graphify_spec_only__/components.md

**Gold code answer**: ac_range_check_test_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv:L10

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: ac_range_check_test_pkg, ip_autogen/ac_range_check/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=119.25 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=28.875 \| 3. component:ac_range_check_testplan [component] @ __graphify_spec_only__/components.md, score=26.125 \| 4. checklist.md [document] @ opentitan/hw/ip_templates/ac_range_check/doc/checklist.md, score=18.1875 \| 5. ac_range_check.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson, score=18.1875 |
| code-only | - | 9 | - | spec=N, code=N, joint=N | 1. .check() [code] @ opentitan\util\validate_testplans.py, score=19.375 \| 2. launder32() [code] @ opentitan\sw\device\lib\base\hardened.h, score=16.25 \| 3. Format [code] @ opentitan\sw\host\opentitantool\src\command\ownership.rs, score=14.375 \| 4. .len() [code] @ opentitan\sw\host\ot_certs\src\asn1\codegen.rs, score=10.0 \| 5. ac_range_check [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv, score=9.9375 |
| spec-code | 1 | 2 | 2 | spec=Y, code=Y, joint=Y | 1. component:ac_range_check [component] @ __graphify_spec_only__/components.md, score=186.75 \| 2. tb [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv, score=47.25 \| 3. ac_range_check_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv, score=45.375 \| 4. ac_range_check_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 \| 5. ac_range_check_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv, score=45.1875 |

### svadv_019 (user_verification_sva, L4)

**Question**: `alert_handler` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `alert_handler_sec_cm_testplan.hjson`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `alert_handler_sec_cm_testplan.hjson`와 SVA artifact `alert_handler_cov_bind.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler, alert_handler_sec_cm_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=329.425 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=317.7125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=65.0 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 3. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=33.1 \| 4. .check() [code] @ opentitan\util\validate_testplans.py, score=25.5 \| 5. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.9375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=498.625 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=324.3125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=321.425 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 |

### svadv_020 (user_verification_sva, L5)

**Question**: `alert_handler` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `alert_handler_sec_cm_testplan.hjson`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `alert_handler_sec_cm_testplan.hjson`와 SVA artifact `alert_handler_cov_bind`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_sec_cm_testplan.hjson, top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson, ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=329.425 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=317.7125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=65.0 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 3. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=33.1 \| 4. .check() [code] @ opentitan\util\validate_testplans.py, score=25.5 \| 5. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.9375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=498.625 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=324.3125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=321.425 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 |

### svadv_021 (user_verification_sva, L5)

**Question**: `alert_handler` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `alert_handler_sec_cm_testplan.hjson`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `alert_handler_sec_cm_testplan.hjson`와 SVA artifact `alert_handler_bind.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/sva/alert_handler_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_sec_cm_testplan.hjson, alert_handler, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=329.425 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=317.7125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=65.0 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 3. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=33.1 \| 4. .check() [code] @ opentitan\util\validate_testplans.py, score=25.5 \| 5. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.9375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=498.625 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=324.3125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=321.425 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 |

### svadv_022 (user_verification_sva, L4)

**Question**: `alert_handler` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `alert_handler_sec_cm_testplan.hjson`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `alert_handler_sec_cm_testplan.hjson`와 SVA artifact `alert_handler_bind`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/sva/alert_handler_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_sec_cm_testplan.hjson, top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=329.425 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=317.7125 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. .exit() [code] @ opentitan\util\dvsim\StatusPrinter.py, score=65.0 \| 2. tohost_exit() [code] @ ibex\vendor\riscv-tests\benchmarks\common\syscalls.c, score=60.0 \| 3. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=33.1 \| 4. .check() [code] @ opentitan\util\validate_testplans.py, score=25.5 \| 5. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.9375 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=498.625 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=324.3125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=321.425 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=318.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=318.4125 |

### svadv_023 (user_verification_dv_testbench, L5)

**Question**: `alert_handler` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `alert_handler_sec_cm_testplan.hjson`와 DV/testbench artifact `tb.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: alert_handler_sec_cm_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_sec_cm_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, ip_autogen/alert_handler/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=221.1875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=45.9375 \| 3. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=39.375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=31.0625 \| 5. component:alert_handler_testplan [component] @ __graphify_spec_only__/components.md, score=30.0625 |
| code-only | - | 26 | - | spec=N, code=N, joint=N | 1. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=27.875 \| 2. .check() [code] @ opentitan\util\validate_testplans.py, score=24.0625 \| 3. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.4375 \| 4. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=18.375 \| 5. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_alert_handler_unittest.cc, score=17.75 |
| spec-code | 1 | 10 | 10 | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=356.1875 \| 2. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=79.125 \| 3. component:top_earlgrey [component] @ __graphify_spec_only__/components.md, score=71.75 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=70.3125 \| 5. alert_handler_cov_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv, score=69.375 |

### svadv_024 (user_verification_sva, L5)

**Question**: `alert_handler` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `alert_handler_testplan.hjson`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `alert_handler_testplan.hjson`와 SVA artifact `alert_handler_cov_bind.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler, alert_handler_testplan.hjson, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=324.175 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=290.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=289.975 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=289.275 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=33.1 \| 2. .check() [code] @ opentitan\util\validate_testplans.py, score=24.875 \| 3. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.9375 \| 4. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=21.125 \| 5. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_alert_handler_unittest.cc, score=20.8 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=493.375 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=306.125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=303.425 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=290.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=289.975 |

### svadv_025 (user_verification_sva, L4)

**Question**: `alert_handler` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `alert_handler_testplan.hjson`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `alert_handler_testplan.hjson`와 SVA artifact `alert_handler_cov_bind`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_testplan.hjson, top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson, ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=324.175 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=290.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=289.975 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=289.275 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=33.1 \| 2. .check() [code] @ opentitan\util\validate_testplans.py, score=24.875 \| 3. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.9375 \| 4. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=21.125 \| 5. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_alert_handler_unittest.cc, score=20.8 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=493.375 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=306.125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=303.425 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=290.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=289.975 |

### svadv_026 (user_verification_sva, L5)

**Question**: `alert_handler` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `alert_handler_testplan.hjson`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `alert_handler_testplan.hjson`와 SVA artifact `alert_handler_bind.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/sva/alert_handler_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_testplan.hjson, alert_handler, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=324.175 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=290.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=289.975 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=289.275 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | 28 | - | spec=N, code=N, joint=N | 1. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=33.1 \| 2. .check() [code] @ opentitan\util\validate_testplans.py, score=24.875 \| 3. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.9375 \| 4. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=21.125 \| 5. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_alert_handler_unittest.cc, score=20.8 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=493.375 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=306.125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=303.425 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=290.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=289.975 |

### svadv_027 (user_verification_sva, L5)

**Question**: `alert_handler` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `alert_handler_testplan.hjson`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `alert_handler_testplan.hjson`와 SVA artifact `alert_handler_bind`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/sva/alert_handler_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler_testplan.hjson, top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=324.175 \| 2. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=290.675 \| 3. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=289.975 \| 4. component:opentitan [component] @ __graphify_spec_only__/components.md, score=289.275 \| 5. component:ipconfig [component] @ __graphify_spec_only__/components.md, score=196.0 |
| code-only | - | 28 | - | spec=N, code=N, joint=N | 1. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=33.1 \| 2. .check() [code] @ opentitan\util\validate_testplans.py, score=24.875 \| 3. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.9375 \| 4. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=21.125 \| 5. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_alert_handler_unittest.cc, score=20.8 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=493.375 \| 2. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=306.125 \| 3. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=303.425 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=290.675 \| 5. component:lowrisc [component] @ __graphify_spec_only__/components.md, score=289.975 |

### svadv_028 (user_verification_dv_testbench, L4)

**Question**: `alert_handler` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `alert_handler_testplan.hjson`와 DV/testbench artifact `tb.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: alert_handler_testplan.hjson [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/data/alert_handler_testplan.hjson | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, ip_autogen/alert_handler/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=221.1875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=45.9375 \| 3. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=39.375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=31.0625 \| 5. component:alert_handler_testplan [component] @ __graphify_spec_only__/components.md, score=30.0625 |
| code-only | - | 26 | - | spec=N, code=N, joint=N | 1. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=27.875 \| 2. .check() [code] @ opentitan\util\validate_testplans.py, score=24.0625 \| 3. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.4375 \| 4. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=18.375 \| 5. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_alert_handler_unittest.cc, score=17.75 |
| spec-code | 1 | 10 | 10 | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=356.1875 \| 2. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=79.125 \| 3. component:top_earlgrey [component] @ __graphify_spec_only__/components.md, score=71.75 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=70.3125 \| 5. alert_handler_cov_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv, score=69.375 |

### svadv_029 (user_verification_sva, L5)

**Question**: `alert_handler` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `theory_of_operation.md`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `theory_of_operation.md`와 SVA artifact `alert_handler_cov_bind.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: alert_handler, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.25 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=256.625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=112.0 \| 4. component:system [component] @ __graphify_spec_only__/components.md, score=82.6875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=71.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=27.875 \| 2. .check() [code] @ opentitan\util\validate_testplans.py, score=24.0625 \| 3. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.4375 \| 4. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=18.825 \| 5. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_alert_handler_unittest.cc, score=17.75 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.25 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=407.825 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=120.9375 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=118.6875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=118.55 |

### svadv_030 (user_verification_sva, L5)

**Question**: `alert_handler` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `theory_of_operation.md`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `theory_of_operation.md`와 SVA artifact `alert_handler_cov_bind`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_cov_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv:L7

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md, ip_autogen/alert_handler/dv/cov/alert_handler_cov_bind.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.25 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=256.625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=112.0 \| 4. component:system [component] @ __graphify_spec_only__/components.md, score=82.6875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=71.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=27.875 \| 2. .check() [code] @ opentitan\util\validate_testplans.py, score=24.0625 \| 3. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.4375 \| 4. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=18.825 \| 5. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_alert_handler_unittest.cc, score=17.75 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.25 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=407.825 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=120.9375 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=118.6875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=118.55 |

### svadv_031 (user_verification_sva, L4)

**Question**: `alert_handler` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `theory_of_operation.md`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `theory_of_operation.md`와 SVA artifact `alert_handler_bind.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/sva/alert_handler_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, alert_handler, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.25 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=256.625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=112.0 \| 4. component:system [component] @ __graphify_spec_only__/components.md, score=82.6875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=71.75 |
| code-only | - | 28 | - | spec=N, code=N, joint=N | 1. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=27.875 \| 2. .check() [code] @ opentitan\util\validate_testplans.py, score=24.0625 \| 3. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.4375 \| 4. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=18.825 \| 5. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_alert_handler_unittest.cc, score=17.75 |
| spec-code | 1 | 15 | 15 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.25 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=407.825 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=120.9375 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=118.6875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=118.55 |

### svadv_032 (user_verification_sva, L5)

**Question**: `alert_handler` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `theory_of_operation.md`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `theory_of_operation.md`와 SVA artifact `alert_handler_bind`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/sva/alert_handler_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: alert_handler_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\sva\alert_handler_bind.sv:L5

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.25 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=256.625 \| 3. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=112.0 \| 4. component:system [component] @ __graphify_spec_only__/components.md, score=82.6875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=71.75 |
| code-only | - | 28 | - | spec=N, code=N, joint=N | 1. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=27.875 \| 2. .check() [code] @ opentitan\util\validate_testplans.py, score=24.0625 \| 3. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.4375 \| 4. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=18.825 \| 5. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_alert_handler_unittest.cc, score=17.75 |
| spec-code | 1 | 15 | 15 | spec=Y, code=N, joint=N | 1. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=868.25 \| 2. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=407.825 \| 3. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=120.9375 \| 4. prim_esc_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=118.6875 \| 5. component:pwrmgr [component] @ __graphify_spec_only__/components.md, score=118.55 |

### svadv_033 (user_verification_dv_testbench, L5)

**Question**: `alert_handler` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `alert_handler` 검증에서는 spec `theory_of_operation.md`와 DV/testbench artifact `tb.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/alert_handler/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/alert_handler/doc/theory_of_operation.md | component:alert_handler [component] @ __graphify_spec_only__/components.md | component:alert_agent_additional_testplan [component] @ __graphify_spec_only__/components.md | component:alert_agent_basic_testplan [component] @ __graphify_spec_only__/components.md | ... +2 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\tb\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, ip_autogen/alert_handler/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=221.1875 \| 2. component:checklist [component] @ __graphify_spec_only__/components.md, score=45.9375 \| 3. component:programmers_guide [component] @ __graphify_spec_only__/components.md, score=39.375 \| 4. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=31.0625 \| 5. component:alert_handler_testplan [component] @ __graphify_spec_only__/components.md, score=30.0625 |
| code-only | - | 26 | - | spec=N, code=N, joint=N | 1. dif_alert_handler.c [code] @ opentitan\sw\device\lib\dif\dif_alert_handler.c, score=27.875 \| 2. .check() [code] @ opentitan\util\validate_testplans.py, score=24.0625 \| 3. alert_handler.rs [code] @ opentitan\sw\host\opentitanlib\src\otp\alert_handler.rs, score=23.4375 \| 4. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=18.375 \| 5. TEST_F() [code] @ opentitan\sw\device\lib\dif\dif_alert_handler_unittest.cc, score=17.75 |
| spec-code | 1 | 10 | 10 | spec=Y, code=N, joint=N | 1. component:alert_handler [component] @ __graphify_spec_only__/components.md, score=356.1875 \| 2. alert_handler_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler_reg_wrap.sv, score=79.125 \| 3. component:top_earlgrey [component] @ __graphify_spec_only__/components.md, score=71.75 \| 4. prim_alert_pkg [code] @ opentitan\hw\top_earlgrey\ip_autogen\alert_handler\rtl\alert_handler.sv, score=70.3125 \| 5. alert_handler_cov_bind [code] @ opentitan\hw\top_darjeeling\ip_autogen\alert_handler\dv\cov\alert_handler_cov_bind.sv, score=69.375 |

### svadv_034 (user_verification_dv_testbench, L4)

**Question**: `racl_ctrl` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `racl_ctrl` 검증에서는 spec `interfaces.md`와 DV/testbench artifact `racl_ctrl_base_env_pkg`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_base_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv:L65

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: racl_ctrl, interfaces.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=140.25 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=106.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=101.0 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=85.75 |
| code-only | - | 25 | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=27.8125 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=26.5625 \| 4. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 \| 5. bitfield_bit32_write() [code] @ opentitan\sw\device\lib\base\bitfield.h, score=16.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=214.5 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=151.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=146.0 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=105.75 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 |

### svadv_035 (user_verification_dv_testbench, L5)

**Question**: `racl_ctrl` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `racl_ctrl` 검증에서는 spec `interfaces.md`와 DV/testbench artifact `racl_ctrl_env_cfg.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_cfg.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_env_cfg.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md, top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_cfg.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=140.25 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=106.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=101.0 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=85.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=27.8125 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=26.5625 \| 4. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 \| 5. bitfield_bit32_write() [code] @ opentitan\sw\device\lib\base\bitfield.h, score=16.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=214.5 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=151.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=146.0 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=105.75 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 |

### svadv_036 (user_verification_dv_testbench, L5)

**Question**: `racl_ctrl` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `racl_ctrl` 검증에서는 spec `interfaces.md`와 DV/testbench artifact `racl_ctrl_env_pkg.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_pkg.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_env_pkg.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, racl_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=140.25 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=106.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=101.0 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=85.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=27.8125 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=26.5625 \| 4. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 \| 5. bitfield_bit32_write() [code] @ opentitan\sw\device\lib\base\bitfield.h, score=16.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=214.5 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=151.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=146.0 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=105.75 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 |

### svadv_037 (user_verification_dv_testbench, L4)

**Question**: `racl_ctrl` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `racl_ctrl` 검증에서는 spec `interfaces.md`와 DV/testbench artifact `racl_ctrl_ral_pkg`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_pkg.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_ral_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv:L11

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: interfaces.md, top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=140.25 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=106.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=101.0 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=85.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=27.8125 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=26.5625 \| 4. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 \| 5. bitfield_bit32_write() [code] @ opentitan\sw\device\lib\base\bitfield.h, score=16.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=214.5 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=151.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=146.0 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=105.75 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 |

### svadv_038 (user_verification_dv_testbench, L5)

**Question**: `racl_ctrl` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `racl_ctrl` 검증에서는 spec `interfaces.md`와 DV/testbench artifact `tb.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=140.25 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=106.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=101.0 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=85.75 |
| code-only | - | 25 | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=27.8125 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=26.5625 \| 4. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 \| 5. bitfield_bit32_write() [code] @ opentitan\sw\device\lib\base\bitfield.h, score=16.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=214.5 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=151.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=146.0 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=105.75 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 |

### svadv_039 (user_verification_dv_testbench, L5)

**Question**: `racl_ctrl` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `racl_ctrl` 검증에서는 spec `theory_of_operation.md`와 DV/testbench artifact `racl_ctrl_base_env_pkg`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_base_env_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv:L65

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: racl_ctrl, theory_of_operation.md, requirement, RTL

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=140.25 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=106.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=101.0 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=85.75 |
| code-only | - | 25 | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=27.8125 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=26.5625 \| 4. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 \| 5. bitfield_bit32_write() [code] @ opentitan\sw\device\lib\base\bitfield.h, score=16.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=214.5 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=151.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=146.0 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=105.75 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 |

### svadv_040 (user_verification_dv_testbench, L4)

**Question**: `racl_ctrl` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `racl_ctrl` 검증에서는 spec `theory_of_operation.md`와 DV/testbench artifact `racl_ctrl_env_cfg.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_cfg.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_env_cfg.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md, top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_cfg.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=140.25 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=106.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=101.0 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=85.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=27.8125 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=26.5625 \| 4. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 \| 5. bitfield_bit32_write() [code] @ opentitan\sw\device\lib\base\bitfield.h, score=16.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=214.5 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=151.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=146.0 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=105.75 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 |

### svadv_041 (user_verification_dv_testbench, L5)

**Question**: `racl_ctrl` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `racl_ctrl` 검증에서는 spec `theory_of_operation.md`와 DV/testbench artifact `racl_ctrl_env_pkg.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_pkg.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_env_pkg.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, racl_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=140.25 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=106.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=101.0 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=85.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=27.8125 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=26.5625 \| 4. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 \| 5. bitfield_bit32_write() [code] @ opentitan\sw\device\lib\base\bitfield.h, score=16.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=214.5 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=151.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=146.0 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=105.75 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 |

### svadv_042 (user_verification_dv_testbench, L5)

**Question**: `racl_ctrl` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `racl_ctrl` 검증에서는 spec `theory_of_operation.md`와 DV/testbench artifact `racl_ctrl_ral_pkg`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/racl_ctrl_env_pkg.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: racl_ctrl_ral_pkg [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv:L11

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=140.25 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=106.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=101.0 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=85.75 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=27.8125 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=26.5625 \| 4. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 \| 5. bitfield_bit32_write() [code] @ opentitan\sw\device\lib\base\bitfield.h, score=16.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=214.5 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=151.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=146.0 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=105.75 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 |

### svadv_043 (user_verification_dv_testbench, L4)

**Question**: `racl_ctrl` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `racl_ctrl` 검증에서는 spec `theory_of_operation.md`와 DV/testbench artifact `tb.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/theory_of_operation.md | component:racl_ctrl [component] @ __graphify_spec_only__/components.md | component:racl [component] @ __graphify_spec_only__/components.md | component:racl_configuration [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: tb.sv [code] @ opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: tb.sv, top_darjeeling/ip_autogen/racl_ctrl/dv/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=140.25 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=106.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=101.0 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 \| 5. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=85.75 |
| code-only | - | 25 | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 \| 2. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=27.8125 \| 3. .check() [code] @ opentitan\util\validate_testplans.py, score=26.5625 \| 4. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=24.875 \| 5. bitfield_bit32_write() [code] @ opentitan\sw\device\lib\base\bitfield.h, score=16.5625 |
| spec-code | 1 | - | - | spec=Y, code=N, joint=N | 1. component:racl_ctrl [component] @ __graphify_spec_only__/components.md, score=214.5 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=151.6875 \| 3. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=146.0 \| 4. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=105.75 \| 5. component:checklist [component] @ __graphify_spec_only__/components.md, score=96.25 |

### svadv_044 (user_verification_dv_testbench, L5)

**Question**: `flash_ctrl` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `flash_ctrl` 검증에서는 spec `flash_ctrl_sec_cm_testplan.hjson`와 DV/testbench artifact `rst_shadowed_if`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: flash_ctrl_sec_cm_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: rst_shadowed_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv:L50

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_sec_cm_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson, implementation, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 2. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 3. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.625 \| 4. .check() [code] @ opentitan\util\validate_testplans.py, score=37.1875 \| 5. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=431.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=154.75 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=115.8125 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 5. flash_ctrl_top_specific_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv, score=105.75 |

### svadv_045 (user_verification_dv_testbench, L5)

**Question**: `flash_ctrl` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `flash_ctrl` 검증에서는 spec `flash_ctrl_testplan.hjson`와 DV/testbench artifact `rst_shadowed_if`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: flash_ctrl_testplan.hjson [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: rst_shadowed_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv:L50

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: flash_ctrl_testplan.hjson, top_englishbreakfast/ip_autogen/flash_ctrl/data/flash_ctrl_testplan.hjson, ip_autogen/flash_ctrl/dv/tb/tb.sv, bridge

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 2. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 3. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.625 \| 4. .check() [code] @ opentitan\util\validate_testplans.py, score=37.1875 \| 5. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=431.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=154.75 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=115.8125 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 5. flash_ctrl_top_specific_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv, score=105.75 |

### svadv_046 (user_verification_dv_testbench, L4)

**Question**: `flash_ctrl` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `flash_ctrl` 검증에서는 spec `interfaces.md`와 DV/testbench artifact `rst_shadowed_if`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md`이고 testbench/code evidence는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: interfaces.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/interfaces.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: rst_shadowed_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv:L50

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: rst_shadowed_if, ip_autogen/flash_ctrl/dv/tb/tb.sv, spec evidence, spec_path_matches_code_path

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 2. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 3. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.625 \| 4. .check() [code] @ opentitan\util\validate_testplans.py, score=37.1875 \| 5. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=431.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=154.75 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=115.8125 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 5. flash_ctrl_top_specific_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv, score=105.75 |

### svadv_047 (user_verification_dv_testbench, L5)

**Question**: `flash_ctrl` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `flash_ctrl` 검증에서는 spec `theory_of_operation.md`와 DV/testbench artifact `rst_shadowed_if`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md`이고 testbench/code evidence는 `opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

**Gold spec answer**: theory_of_operation.md [document] @ opentitan/hw/top_englishbreakfast/ip_autogen/flash_ctrl/doc/theory_of_operation.md | component:flash_ctrl [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan [component] @ __graphify_spec_only__/components.md | component:chip_flash_ctrl_testplan_hjson [component] @ __graphify_spec_only__/components.md | ... +3 more

**Gold code answer**: rst_shadowed_if [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\dv\tb\tb.sv:L50

**Gold bridge**: spec_path_matches_code_path

**Gold evidence terms**: theory_of_operation.md, flash_ctrl, verification, review

| Variant | Spec Rank | Code Rank | Joint Rank | Hit@5 | Actual retrieved answer, top 5 |
|---|---:|---:|---:|---|---|
| spec-only | 1 | - | - | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=296.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=109.75 \| 3. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 4. opentitan/hw [category] @ __graphify_spec_only__/categories.md, score=97.125 \| 5. component:theory_of_operation [component] @ __graphify_spec_only__/components.md, score=87.9375 |
| code-only | - | - | - | spec=N, code=N, joint=N | 1. mmio_region_read32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=52.1875 \| 2. dif_flash_ctrl.c [code] @ opentitan\sw\device\lib\dif\dif_flash_ctrl.c, score=49.75 \| 3. flash_ctrl.c [code] @ opentitan\sw\device\silicon_creator\lib\drivers\flash_ctrl.c, score=47.625 \| 4. .check() [code] @ opentitan\util\validate_testplans.py, score=37.1875 \| 5. mmio_region_write32() [code] @ opentitan\sw\device\lib\base\mock_mmio.cc, score=36.5625 |
| spec-code | 1 | 13 | 13 | spec=Y, code=N, joint=N | 1. component:flash_ctrl [component] @ __graphify_spec_only__/components.md, score=431.4375 \| 2. component:otp_ctrl [component] @ __graphify_spec_only__/components.md, score=154.75 \| 3. component:lc_ctrl [component] @ __graphify_spec_only__/components.md, score=115.8125 \| 4. component:checklist [component] @ __graphify_spec_only__/components.md, score=106.75 \| 5. flash_ctrl_top_specific_pkg [code] @ opentitan\hw\top_englishbreakfast\ip_autogen\flash_ctrl\rtl\flash_phy.sv, score=105.75 |

