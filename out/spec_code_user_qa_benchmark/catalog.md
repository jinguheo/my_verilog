# Spec-Code User QA Benchmark

- Questions: 150
- Language: Korean user-style questions
- Purpose: evaluate whether answers can combine spec evidence and code evidence.

## Distribution

| Type | Count |
|---|---:|
| user_change_impact | 25 |
| user_code_to_spec_why | 25 |
| user_disambiguation | 25 |
| user_review_trace | 25 |
| user_spec_to_code_explain | 25 |
| user_verification_coverage | 25 |

## Sample

### userqa_001 - user_spec_to_code_explain

**Question**: `otp_ctrl` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `otp_ctrl_sec_cm_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `otp_ctrl`는 spec 문서 `otp_ctrl_sec_cm_testplan.hjson`와 code artifact `prim_sec_anchor_flop`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_earlgrey/ip_autogen/otp_ctrl/rtl/otp_ctrl_kdi.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

### userqa_002 - user_code_to_spec_why

**Question**: `prim_sync_reqack`가 왜 필요한지 spec 기준으로 설명해줘. `top_englishbreakfast/ip_autogen/rstmgr/rtl/rstmgr_cnsty_chk.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `chip_rstmgr_testplan`는 spec 문서 `rstmgr_cnsty_chk_testplan.hjson`와 code artifact `prim_sync_reqack`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/rtl/rstmgr_cnsty_chk.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

### userqa_003 - user_review_trace

**Question**: 리뷰할 때 `chip_rstmgr_testplan`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `chip_rstmgr_testplan`는 spec 문서 `rstmgr_cnsty_chk_testplan.hjson`와 code artifact `prim_rst_sync`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

### userqa_004 - user_verification_coverage

**Question**: `chip_rstmgr_testplan` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`와 연결된 code 쪽도 알려줘.

**Expected answer**: `chip_rstmgr_testplan`는 spec 문서 `rstmgr_cnsty_chk_testplan.hjson`와 code artifact `rstmgr_cnsty_chk_if`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

### userqa_005 - user_change_impact

**Question**: `chip_rstmgr_testplan` spec가 바뀌면 어떤 RTL/code artifact를 영향 분석해야 해? 관련 spec 문서와 code node를 같이 답해줘.

**Expected answer**: `chip_rstmgr_testplan`는 spec 문서 `rstmgr_cnsty_chk_testplan.hjson`와 code artifact `rstmgr_cnsty_chk`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/data/rstmgr_cnsty_chk_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rstmgr/dv/rstmgr_cnsty_chk/tb.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

### userqa_006 - user_disambiguation

**Question**: 이름만 보면 헷갈리는데 `rv_core_ibex`는 `top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson` 기준으로 어떤 code artifact와 연결돼? 단순 파일명 말고 spec-code 연결 근거로 답해줘.

**Expected answer**: `rv_core_ibex`는 spec 문서 `rv_core_ibex_sec_cm_testplan.hjson`와 code artifact `prim_sec_anchor_buf`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/data/rv_core_ibex_sec_cm_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_englishbreakfast/ip_autogen/rv_core_ibex/rtl/rv_core_ibex.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

### userqa_007 - user_spec_to_code_explain

**Question**: `ac_range_check` 관련 spec가 실제 RTL/코드 어디와 연결되는지 설명해줘. spec 문서는 `ac_range_check_testplan.hjson` 쪽이고, 구현 근거 파일도 같이 알려줘.

**Expected answer**: `ac_range_check`는 spec 문서 `ac_range_check_testplan.hjson`와 code artifact `prim_flop_en`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

### userqa_008 - user_code_to_spec_why

**Question**: `prim_onehot_enc`가 왜 필요한지 spec 기준으로 설명해줘. `top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`에 있는 코드와 연결되는 spec 문서/요구사항을 같이 찾아줘.

**Expected answer**: `ac_range_check`는 spec 문서 `ac_range_check_testplan.hjson`와 code artifact `prim_onehot_enc`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/rtl/ac_range_check.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

### userqa_009 - user_review_trace

**Question**: 리뷰할 때 `ac_range_check`는 어떤 spec와 어떤 코드 파일을 같이 봐야 해? spec 근거와 RTL/code 근거를 한 번에 정리해줘.

**Expected answer**: `ac_range_check`는 spec 문서 `ac_range_check_testplan.hjson`와 code artifact `ac_range_check_bind.sv`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

### userqa_010 - user_verification_coverage

**Question**: `ac_range_check` 검증 관점에서 빠뜨리면 안 되는 spec anchor와 testbench/RTL artifact가 뭐야? `top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`와 연결된 code 쪽도 알려줘.

**Expected answer**: `ac_range_check`는 spec 문서 `ac_range_check_testplan.hjson`와 code artifact `ac_range_check_bind`를 같이 봐야 합니다. Spec 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`이고, 구현/검증 쪽 근거는 `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/dv/sva/ac_range_check_bind.sv`입니다. KG에서는 `spec_path_matches_code_path` 관계로 연결되어 있으므로, 답변에는 spec anchor와 RTL/code node를 모두 포함해야 합니다.

