# Hardware Description: kmac

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `kmac`
- `approved_label`: `pending:kmac`
- `doc_anchor`: `kmac`
- `module_name_prefix`: `kmac`
- `bridge_edge_count`: 112

## Inferred Hardware Role

`kmac` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 89, component: 41, testplan: 28, theory: 19, interface: 14
- Code categories: dv: 260, rtl: 96, other_code: 7, sva: 5
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Anchors

- `component:kmac` (L1) - `__graphify_spec_only__/components.md`
- `kmac.hjson` (L1) - `opentitan/hw/ip/kmac/data/kmac.hjson`
- `human name` (L7) - `opentitan/hw/ip/kmac/data/kmac.hjson`
- `one line desc` (L8) - `opentitan/hw/ip/kmac/data/kmac.hjson`
- `one paragraph desc` (L9) - `opentitan/hw/ip/kmac/data/kmac.hjson`
- `cip id` (L20) - `opentitan/hw/ip/kmac/data/kmac.hjson`
- `design spec` (L21) - `opentitan/hw/ip/kmac/data/kmac.hjson`
- `dv doc` (L22) - `opentitan/hw/ip/kmac/data/kmac.hjson`
- `hw checklist` (L23) - `opentitan/hw/ip/kmac/data/kmac.hjson`
- `sw checklist` (L24) - `opentitan/hw/ip/kmac/data/kmac.hjson`
- `revisions` (L25) - `opentitan/hw/ip/kmac/data/kmac.hjson`
- `version` (L27) - `opentitan/hw/ip/kmac/data/kmac.hjson`
- `kmac_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/kmac/data/kmac_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/kmac/data/kmac_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/kmac/data/kmac_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/kmac/data/kmac_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/kmac/data/kmac_sec_cm_testplan.hjson`
- `kmac_testplan.hjson` (L1) - `opentitan/hw/ip/kmac/data/kmac_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/kmac/data/kmac_testplan.hjson`
- `testpoints` (L14) - `opentitan/hw/ip/kmac/data/kmac_testplan.hjson`
- `desc` (L17) - `opentitan/hw/ip/kmac/data/kmac_testplan.hjson`
- `stage` (L46) - `opentitan/hw/ip/kmac/data/kmac_testplan.hjson`
- `tests` (L47) - `opentitan/hw/ip/kmac/data/kmac_testplan.hjson`
- `covergroups` (L285) - `opentitan/hw/ip/kmac/data/kmac_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/kmac/doc/checklist.md`
- `KMAC Checklist` (L1) - `opentitan/hw/ip/kmac/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/kmac/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/kmac/doc/checklist.md`
- `D2` (L32) - `opentitan/hw/ip/kmac/doc/checklist.md`
- `D2S` (L74) - `opentitan/hw/ip/kmac/doc/checklist.md`
- `D3` (L94) - `opentitan/hw/ip/kmac/doc/checklist.md`
- `Verification Checklist` (L120) - `opentitan/hw/ip/kmac/doc/checklist.md`
- `V1` (L122) - `opentitan/hw/ip/kmac/doc/checklist.md`
- `V2` (L173) - `opentitan/hw/ip/kmac/doc/checklist.md`
- `V2S` (L219) - `opentitan/hw/ip/kmac/doc/checklist.md`

## Code Evidence

- `sha3` (L199) - `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\kmac\dv\tb.sv`
- `kmac_env_pkg` (L9) - `opentitan\hw\ip\kmac\dv\tests\kmac_test_pkg.sv`
- `kmac_test_pkg` (L10) - `opentitan\hw\ip\kmac\dv\tb.sv`
- `kmac_reg_pkg` (L31) - `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv`
- `tb` (L5) - `opentitan\hw\ip\kmac\dv\tb.sv`
- `kmac_if` (L28) - `opentitan\hw\ip\kmac\dv\tb.sv`
- `kmac_cov_bind.sv` (L1) - `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv`
- `kmac_cov_bind` (L5) - `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv`
- `kmac_cov_if.sv` (L1) - `opentitan\hw\ip\kmac\dv\cov\kmac_cov_if.sv`
- `sha3_pkg` (L10) - `opentitan\hw\ip\kmac\rtl\sha3pad.sv`
- `sha3pad_assert_if.sv` (L1) - `opentitan\hw\ip\kmac\dv\cov\sha3pad_assert_if.sv`
- `digestpp_dpi.cc` (L1) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `load_arr_from_simulator()` (L25) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `write_array_to_simulator()` (L37) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `get_sha3_digest()` (L54) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `c_dpi_sha3_224()` (L81) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `c_dpi_sha3_256()` (L89) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `c_dpi_sha3_384()` (L97) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `c_dpi_sha3_512()` (L105) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `c_dpi_shake128()` (L113) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `c_dpi_shake256()` (L137) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `c_dpi_cshake128()` (L161) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `c_dpi_cshake256()` (L189) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `c_dpi_kmac128()` (L217) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `c_dpi_kmac128_xof()` (L255) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `c_dpi_kmac256()` (L291) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `c_dpi_kmac256_xof()` (L329) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi.cc`
- `digestpp_dpi_pkg.sv` (L1) - `opentitan\hw\ip\kmac\dv\dpi\digestpp_dpi_pkg.sv`
- `digestpp.hpp` (L1) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\digestpp.hpp`
- `hasher.hpp` (L1) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\hasher.hpp`
- `hasher` (L36) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\hasher.hpp`
- `squeeze()` (L189) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\hasher.hpp`
- `hexsqueeze()` (L243) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\hasher.hpp`
- `digest()` (L271) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\hasher.hpp`
- `hexdigest()` (L319) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\hasher.hpp`
- `blake.hpp` (L1) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\algorithm\blake.hpp`
- `blake2.hpp` (L1) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\algorithm\blake2.hpp`
- `groestl.hpp` (L1) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\algorithm\groestl.hpp`
- `jh.hpp` (L1) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\algorithm\jh.hpp`
- `k12m14.hpp` (L1) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\algorithm\k12m14.hpp`
- `kmac.hpp` (L1) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\algorithm\kmac.hpp`
- `kupyna.hpp` (L1) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\algorithm\kupyna.hpp`
- `md5.hpp` (L1) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\algorithm\md5.hpp`
- `sha1.hpp` (L1) - `opentitan\hw\ip\kmac\dv\dpi\vendor\kerukuro_digestpp\algorithm\sha1.hpp`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:kmac` | `kmac_reduced_tb.sv` | `opentitan\hw\ip\kmac\pre_dv\kmac_reduced_tb\rtl\kmac_reduced_tb.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reduced_tb` | `opentitan\hw\ip\kmac\pre_dv\kmac_reduced_tb\rtl\kmac_reduced_tb.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_base_test.sv` | `opentitan\hw\ip\kmac\dv\tests\kmac_base_test.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_env_pkg` | `opentitan\hw\ip\kmac\dv\tests\kmac_test_pkg.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_test_pkg.sv` | `opentitan\hw\ip\kmac\dv\tests\kmac_test_pkg.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_cov_bind.sv` | `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_cov_bind` | `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_cov_if.sv` | `opentitan\hw\ip\kmac\dv\cov\kmac_cov_if.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reg_pkg` | `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_bind.sv` | `opentitan\hw\ip\kmac\dv\sva\kmac_bind.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_bind` | `opentitan\hw\ip\kmac\dv\sva\kmac_bind.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_pkg` | `opentitan\hw\ip\kmac\rtl\kmac_staterd.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_entropy.sv` | `opentitan\hw\ip\kmac\rtl\kmac_entropy.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_entropy` | `opentitan\hw\ip\kmac\rtl\kmac_entropy.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_msgfifo.sv` | `opentitan\hw\ip\kmac\rtl\kmac_msgfifo.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_msgfifo` | `opentitan\hw\ip\kmac\rtl\kmac_msgfifo.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reduced.sv` | `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reduced` | `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_entropy` | `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reg_pkg.sv` | `opentitan\hw\ip\kmac\rtl\kmac_reg_pkg.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reg_top.sv` | `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reg_top` | `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_staterd.sv` | `opentitan\hw\ip\kmac\rtl\kmac_staterd.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_staterd` | `opentitan\hw\ip\kmac\rtl\kmac_staterd.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_errchk.sv` | `opentitan\hw\ip\kmac\rtl\kmac_errchk.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_errchk` | `opentitan\hw\ip\kmac\rtl\kmac_errchk.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_core.sv` | `opentitan\hw\ip\kmac\rtl\kmac_core.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_core` | `opentitan\hw\ip\kmac\rtl\kmac_core.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_app.sv` | `opentitan\hw\ip\kmac\rtl\kmac_app.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_app` | `opentitan\hw\ip\kmac\rtl\kmac_app.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_pkg.sv` | `opentitan\hw\ip\kmac\rtl\kmac_pkg.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac.sv` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_core` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_app` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_msgfifo` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_staterd` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_errchk` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_component_matches_code` | `component:kmac` | `kmac_reg_top` | `opentitan\hw\ip\kmac\rtl\kmac.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `sha3` | `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `tb.sv` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `kmac_env_pkg` | `opentitan\hw\ip\kmac\dv\tests\kmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `kmac_test_pkg` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `kmac_reg_pkg` | `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `tb` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `kmac_if` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac.hjson` | `kmac_cov_bind.sv` | `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `sha3` | `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `kmac_env_pkg` | `opentitan\hw\ip\kmac\dv\tests\kmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `kmac_test_pkg` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `kmac_reg_pkg` | `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `kmac_if` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac_sec_cm_testplan.hjson` | `kmac_cov_bind.sv` | `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv` |
| `spec_path_matches_code_path` | `kmac_testplan.hjson` | `sha3` | `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv` |
| `spec_path_matches_code_path` | `kmac_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac_testplan.hjson` | `kmac_env_pkg` | `opentitan\hw\ip\kmac\dv\tests\kmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `kmac_testplan.hjson` | `kmac_test_pkg` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac_testplan.hjson` | `kmac_reg_pkg` | `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv` |
| `spec_path_matches_code_path` | `kmac_testplan.hjson` | `tb` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac_testplan.hjson` | `kmac_if` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `kmac_testplan.hjson` | `kmac_cov_bind.sv` | `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `sha3` | `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `kmac_env_pkg` | `opentitan\hw\ip\kmac\dv\tests\kmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `kmac_test_pkg` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `kmac_reg_pkg` | `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `kmac_if` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `kmac_cov_bind.sv` | `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `sha3` | `opentitan\hw\ip\kmac\rtl\kmac_reduced.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `kmac_env_pkg` | `opentitan\hw\ip\kmac\dv\tests\kmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `kmac_test_pkg` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `kmac_reg_pkg` | `opentitan\hw\ip\kmac\rtl\kmac_reg_top.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `kmac_if` | `opentitan\hw\ip\kmac\dv\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `kmac_cov_bind.sv` | `opentitan\hw\ip\kmac\dv\cov\kmac_cov_bind.sv` |

## Retrieval Guidance

- When a code-only query mentions `kmac`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
