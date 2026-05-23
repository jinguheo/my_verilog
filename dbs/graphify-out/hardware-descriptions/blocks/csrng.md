# Hardware Description: csrng

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `csrng`
- `approved_label`: `pending:csrng`
- `doc_anchor`: `csrng`
- `module_name_prefix`: `csrng`
- `bridge_edge_count`: 112

## Inferred Hardware Role

`csrng` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 88, component: 41, testplan: 30, theory: 19, interface: 16
- Code categories: dv: 83, rtl: 69, sva: 6
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Anchors

- `component:csrng` (L1) - `__graphify_spec_only__/components.md`
- `csrng.hjson` (L1) - `opentitan/hw/ip/csrng/data/csrng.hjson`
- `human name` (L5) - `opentitan/hw/ip/csrng/data/csrng.hjson`
- `one line desc` (L6) - `opentitan/hw/ip/csrng/data/csrng.hjson`
- `one paragraph desc` (L7) - `opentitan/hw/ip/csrng/data/csrng.hjson`
- `cip id` (L18) - `opentitan/hw/ip/csrng/data/csrng.hjson`
- `design spec` (L19) - `opentitan/hw/ip/csrng/data/csrng.hjson`
- `dv doc` (L20) - `opentitan/hw/ip/csrng/data/csrng.hjson`
- `hw checklist` (L21) - `opentitan/hw/ip/csrng/data/csrng.hjson`
- `sw checklist` (L22) - `opentitan/hw/ip/csrng/data/csrng.hjson`
- `version` (L23) - `opentitan/hw/ip/csrng/data/csrng.hjson`
- `life stage` (L24) - `opentitan/hw/ip/csrng/data/csrng.hjson`
- `csrng_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/csrng/data/csrng_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/csrng/data/csrng_sec_cm_testplan.hjson`
- `desc` (L29) - `opentitan/hw/ip/csrng/data/csrng_sec_cm_testplan.hjson`
- `stage` (L35) - `opentitan/hw/ip/csrng/data/csrng_sec_cm_testplan.hjson`
- `tests` (L36) - `opentitan/hw/ip/csrng/data/csrng_sec_cm_testplan.hjson`
- `csrng_testplan.hjson` (L1) - `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `testpoints` (L12) - `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `desc` (L15) - `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `stage` (L20) - `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `tests` (L21) - `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `covergroups` (L103) - `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `Cross` (L115) - `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `genbits fips cp` (L192) - `opentitan/hw/ip/csrng/data/csrng_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/csrng/doc/checklist.md`
- `CSRNG Checklist` (L1) - `opentitan/hw/ip/csrng/doc/checklist.md`
- `Design Checklist` (L11) - `opentitan/hw/ip/csrng/doc/checklist.md`
- `D1` (L13) - `opentitan/hw/ip/csrng/doc/checklist.md`
- `D2` (L37) - `opentitan/hw/ip/csrng/doc/checklist.md`
- `D2S` (L79) - `opentitan/hw/ip/csrng/doc/checklist.md`
- `D3` (L99) - `opentitan/hw/ip/csrng/doc/checklist.md`
- `Verification Checklist` (L125) - `opentitan/hw/ip/csrng/doc/checklist.md`
- `V1` (L127) - `opentitan/hw/ip/csrng/doc/checklist.md`

## Code Evidence

- `csrng_pkg` (L13) - `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv`
- `aes_cipher_core` (L64) - `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\csrng\dv\tb.sv`
- `csrng_env_pkg` (L9) - `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv`
- `csrng_test_pkg` (L10) - `opentitan\hw\ip\csrng\dv\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\csrng\dv\tb.sv`
- `csrng_agents_if` (L36) - `opentitan\hw\ip\csrng\dv\tb.sv`
- `csrng_path_if` (L39) - `opentitan\hw\ip\csrng\dv\tb.sv`
- `csrng_cov_bind.sv` (L1) - `opentitan\hw\ip\csrng\dv\cov\csrng_cov_bind.sv`
- `csrng_cov_bind` (L6) - `opentitan\hw\ip\csrng\dv\cov\csrng_cov_bind.sv`
- `csrng_cov_if.sv` (L1) - `opentitan\hw\ip\csrng\dv\cov\csrng_cov_if.sv`
- `csrng_assert_if.sv` (L1) - `opentitan\hw\ip\csrng\dv\sva\csrng_assert_if.sv`
- `csrng_bind.sv` (L1) - `opentitan\hw\ip\csrng\dv\sva\csrng_bind.sv`
- `csrng_bind` (L5) - `opentitan\hw\ip\csrng\dv\sva\csrng_bind.sv`
- `csrng_alert_test.sv` (L1) - `opentitan\hw\ip\csrng\dv\tests\csrng_alert_test.sv`
- `csrng_base_test.sv` (L1) - `opentitan\hw\ip\csrng\dv\tests\csrng_base_test.sv`
- `csrng_cmds_test.sv` (L1) - `opentitan\hw\ip\csrng\dv\tests\csrng_cmds_test.sv`
- `csrng_intr_test.sv` (L1) - `opentitan\hw\ip\csrng\dv\tests\csrng_intr_test.sv`
- `csrng_regwen_test.sv` (L1) - `opentitan\hw\ip\csrng\dv\tests\csrng_regwen_test.sv`
- `csrng_smoke_test.sv` (L1) - `opentitan\hw\ip\csrng\dv\tests\csrng_smoke_test.sv`
- `csrng_stress_all_test.sv` (L1) - `opentitan\hw\ip\csrng\dv\tests\csrng_stress_all_test.sv`
- `csrng_test_pkg.sv` (L1) - `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv`
- `csrng.sv` (L1) - `opentitan\hw\ip\csrng\rtl\csrng.sv`
- `csrng` (L9) - `opentitan\hw\ip\csrng\rtl\csrng.sv`
- `csrng_reg_pkg` (L14) - `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv`
- `csrng_core` (L77) - `opentitan\hw\ip\csrng\rtl\csrng.sv`
- `csrng_block_encrypt.sv` (L1) - `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv`
- `csrng_block_encrypt` (L8) - `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv`
- `csrng_cmd_stage.sv` (L1) - `opentitan\hw\ip\csrng\rtl\csrng_cmd_stage.sv`
- `csrng_cmd_stage` (L9) - `opentitan\hw\ip\csrng\rtl\csrng_cmd_stage.sv`
- `csrng_core.sv` (L1) - `opentitan\hw\ip\csrng\rtl\csrng_core.sv`
- `csrng_core` (L9) - `opentitan\hw\ip\csrng\rtl\csrng_core.sv`
- `csrng_main_sm` (L778) - `opentitan\hw\ip\csrng\rtl\csrng_core.sv`
- `csrng_state_db` (L840) - `opentitan\hw\ip\csrng\rtl\csrng_core.sv`
- `csrng_ctr_drbg` (L912) - `opentitan\hw\ip\csrng\rtl\csrng_core.sv`
- `csrng_block_encrypt` (L950) - `opentitan\hw\ip\csrng\rtl\csrng_core.sv`
- `csrng_ctr_drbg.sv` (L1) - `opentitan\hw\ip\csrng\rtl\csrng_ctr_drbg.sv`
- `csrng_ctr_drbg` (L9) - `opentitan\hw\ip\csrng\rtl\csrng_ctr_drbg.sv`
- `csrng_main_sm.sv` (L1) - `opentitan\hw\ip\csrng\rtl\csrng_main_sm.sv`
- `csrng_main_sm` (L11) - `opentitan\hw\ip\csrng\rtl\csrng_main_sm.sv`
- `csrng_pkg.sv` (L1) - `opentitan\hw\ip\csrng\rtl\csrng_pkg.sv`
- `csrng_reg_pkg.sv` (L1) - `opentitan\hw\ip\csrng\rtl\csrng_reg_pkg.sv`
- `csrng_reg_top.sv` (L1) - `opentitan\hw\ip\csrng\rtl\csrng_reg_top.sv`
- `csrng_reg_top` (L9) - `opentitan\hw\ip\csrng\rtl\csrng_reg_top.sv`
- `csrng_state_db.sv` (L1) - `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:csrng` | `csrng_stress_all_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_stress_all_test.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_regwen_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_regwen_test.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_alert_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_alert_test.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_smoke_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_smoke_test.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_base_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_base_test.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_cmds_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_cmds_test.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_intr_test.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_intr_test.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_env_pkg` | `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_test_pkg.sv` | `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_block_encrypt.sv` | `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_block_encrypt` | `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_assert_if.sv` | `opentitan\hw\ip\csrng\dv\sva\csrng_assert_if.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_cov_bind.sv` | `opentitan\hw\ip\csrng\dv\cov\csrng_cov_bind.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_cov_bind` | `opentitan\hw\ip\csrng\dv\cov\csrng_cov_bind.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_cov_if.sv` | `opentitan\hw\ip\csrng\dv\cov\csrng_cov_if.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_cmd_stage.sv` | `opentitan\hw\ip\csrng\rtl\csrng_cmd_stage.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_cmd_stage` | `opentitan\hw\ip\csrng\rtl\csrng_cmd_stage.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_pkg` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_reg_pkg` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_ctr_drbg.sv` | `opentitan\hw\ip\csrng\rtl\csrng_ctr_drbg.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_ctr_drbg` | `opentitan\hw\ip\csrng\rtl\csrng_ctr_drbg.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_state_db.sv` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_state_db` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_bind.sv` | `opentitan\hw\ip\csrng\dv\sva\csrng_bind.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_bind` | `opentitan\hw\ip\csrng\dv\sva\csrng_bind.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_main_sm.sv` | `opentitan\hw\ip\csrng\rtl\csrng_main_sm.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_main_sm` | `opentitan\hw\ip\csrng\rtl\csrng_main_sm.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_reg_pkg.sv` | `opentitan\hw\ip\csrng\rtl\csrng_reg_pkg.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_reg_top.sv` | `opentitan\hw\ip\csrng\rtl\csrng_reg_top.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_reg_top` | `opentitan\hw\ip\csrng\rtl\csrng_reg_top.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_core.sv` | `opentitan\hw\ip\csrng\rtl\csrng_core.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_core` | `opentitan\hw\ip\csrng\rtl\csrng_core.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_main_sm` | `opentitan\hw\ip\csrng\rtl\csrng_core.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_state_db` | `opentitan\hw\ip\csrng\rtl\csrng_core.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_ctr_drbg` | `opentitan\hw\ip\csrng\rtl\csrng_core.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_block_encrypt` | `opentitan\hw\ip\csrng\rtl\csrng_core.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng_pkg.sv` | `opentitan\hw\ip\csrng\rtl\csrng_pkg.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng.sv` | `opentitan\hw\ip\csrng\rtl\csrng.sv` |
| `spec_component_matches_code` | `component:csrng` | `csrng` | `opentitan\hw\ip\csrng\rtl\csrng.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `csrng_pkg` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `aes_cipher_core` | `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `tb.sv` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `csrng_env_pkg` | `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `csrng_test_pkg` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `tb` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `csrng_agents_if` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng.hjson` | `csrng_path_if` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `csrng_pkg` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `aes_cipher_core` | `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `csrng_env_pkg` | `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `csrng_test_pkg` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `csrng_agents_if` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_sec_cm_testplan.hjson` | `csrng_path_if` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_testplan.hjson` | `csrng_pkg` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_path_matches_code_path` | `csrng_testplan.hjson` | `aes_cipher_core` | `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv` |
| `spec_path_matches_code_path` | `csrng_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_testplan.hjson` | `csrng_env_pkg` | `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv` |
| `spec_path_matches_code_path` | `csrng_testplan.hjson` | `csrng_test_pkg` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_testplan.hjson` | `tb` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_testplan.hjson` | `csrng_agents_if` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `csrng_testplan.hjson` | `csrng_path_if` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `csrng_pkg` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `aes_cipher_core` | `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `csrng_env_pkg` | `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `csrng_test_pkg` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `csrng_agents_if` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `csrng_path_if` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `csrng_pkg` | `opentitan\hw\ip\csrng\rtl\csrng_state_db.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `aes_cipher_core` | `opentitan\hw\ip\csrng\rtl\csrng_block_encrypt.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `csrng_env_pkg` | `opentitan\hw\ip\csrng\dv\tests\csrng_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `csrng_test_pkg` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `csrng_agents_if` | `opentitan\hw\ip\csrng\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `csrng_path_if` | `opentitan\hw\ip\csrng\dv\tb.sv` |

## Retrieval Guidance

- When a code-only query mentions `csrng`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
