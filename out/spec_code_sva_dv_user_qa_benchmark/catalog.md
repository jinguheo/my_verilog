# SVA/DV User QA Benchmark

- Questions: 47
- Purpose: evaluate spec-to-verification traceability, including SVA bind/assertion and DV/testbench artifacts.

| Artifact kind | Count |
|---|---:|
| dv_testbench | 29 |
| sva | 18 |

## Sample

### svadv_001 - user_verification_dv_testbench

**Question**: `chip_rstmgr_testplan` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `chip_rstmgr_testplan` 검증에서는 spec `rstmgr_cnsty_chk_testplan.hjson`와 DV/testbench artifact `prim_rst_sync`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

### svadv_002 - user_verification_dv_testbench

**Question**: `chip_rstmgr_testplan` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `chip_rstmgr_testplan` 검증에서는 spec `rstmgr_cnsty_chk_testplan.hjson`와 DV/testbench artifact `rstmgr_cnsty_chk_if`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

### svadv_003 - user_verification_dv_testbench

**Question**: `chip_rstmgr_testplan` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `chip_rstmgr_testplan` 검증에서는 spec `rstmgr_cnsty_chk_testplan.hjson`와 DV/testbench artifact `rstmgr_cnsty_chk`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

### svadv_004 - user_verification_sva

**Question**: `ac_range_check` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `ac_range_check_testplan.hjson`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `ac_range_check_testplan.hjson`와 SVA artifact `ac_range_check_bind.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

### svadv_005 - user_verification_sva

**Question**: `ac_range_check` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `ac_range_check_testplan.hjson`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `ac_range_check_testplan.hjson`와 SVA artifact `ac_range_check_bind`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

### svadv_006 - user_verification_dv_testbench

**Question**: `ac_range_check` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `ac_range_check_testplan.hjson`와 DV/testbench artifact `tb.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

### svadv_007 - user_verification_dv_testbench

**Question**: `ac_range_check` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `ac_range_check_testplan.hjson`와 DV/testbench artifact `ac_range_check_env_pkg`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tests/ac_range_check_test_pkg.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

### svadv_008 - user_verification_dv_testbench

**Question**: `ac_range_check` 검증 testbench에서 어떤 spec 요구사항을 확인하는지 설명해줘. 관련 spec 문서와 DV/testbench code artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `ac_range_check_testplan.hjson`와 DV/testbench artifact `ac_range_check_test_pkg`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고 testbench/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/tb/tb.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 답변에는 spec 근거와 검증 코드 근거가 모두 포함되어야 합니다.

### svadv_009 - user_verification_sva

**Question**: `ac_range_check` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `interfaces.md`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `interfaces.md`와 SVA artifact `ac_range_check_bind.sv`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

### svadv_010 - user_verification_sva

**Question**: `ac_range_check` 검증에서 SVA/assertion 쪽으로 확인해야 할 항목이 뭐야? spec 문서 `interfaces.md`와 연결되는 SVA bind/assertion artifact를 같이 알려줘.

**Expected answer**: `ac_range_check` 검증에서는 spec `interfaces.md`와 SVA artifact `ac_range_check_bind`를 같이 봐야 합니다. Spec anchor는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`이고 SVA/code evidence는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG 연결 근거는 `spec_path_matches_code_path`이며, 이 답변은 요구사항이 assertion/bind 검증으로 어떻게 추적되는지 보여줘야 합니다.

