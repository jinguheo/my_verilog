# Hardware Description: hmac

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `hmac`
- `approved_label`: `pending:hmac`
- `doc_anchor`: `hmac`
- `module_name_prefix`: `hmac`
- `bridge_edge_count`: 112

## Inferred Hardware Role

`hmac` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 87, component: 41, testplan: 28, theory: 17, interface: 15
- Code categories: dv: 95, rtl: 32, other_code: 24, sva: 22
- Bridge relations: spec_path_matches_code_path: 72, spec_component_matches_code: 40

## Spec Anchors

- `component:hmac` (L1) - `__graphify_spec_only__/components.md`
- `hmac.hjson` (L1) - `opentitan/hw/ip/hmac/data/hmac.hjson`
- `human name` (L6) - `opentitan/hw/ip/hmac/data/hmac.hjson`
- `one line desc` (L7) - `opentitan/hw/ip/hmac/data/hmac.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/ip/hmac/data/hmac.hjson`
- `cip id` (L16) - `opentitan/hw/ip/hmac/data/hmac.hjson`
- `design spec` (L17) - `opentitan/hw/ip/hmac/data/hmac.hjson`
- `dv doc` (L18) - `opentitan/hw/ip/hmac/data/hmac.hjson`
- `hw checklist` (L19) - `opentitan/hw/ip/hmac/data/hmac.hjson`
- `sw checklist` (L20) - `opentitan/hw/ip/hmac/data/hmac.hjson`
- `revisions` (L21) - `opentitan/hw/ip/hmac/data/hmac.hjson`
- `version` (L23) - `opentitan/hw/ip/hmac/data/hmac.hjson`
- `hmac_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/hmac/data/hmac_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/hmac/data/hmac_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/hmac/data/hmac_sec_cm_testplan.hjson`
- `stage` (L29) - `opentitan/hw/ip/hmac/data/hmac_sec_cm_testplan.hjson`
- `tests` (L30) - `opentitan/hw/ip/hmac/data/hmac_sec_cm_testplan.hjson`
- `hmac_testplan.hjson` (L1) - `opentitan/hw/ip/hmac/data/hmac_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/hmac/data/hmac_testplan.hjson`
- `testpoints` (L12) - `opentitan/hw/ip/hmac/data/hmac_testplan.hjson`
- `desc` (L15) - `opentitan/hw/ip/hmac/data/hmac_testplan.hjson`
- `stage` (L27) - `opentitan/hw/ip/hmac/data/hmac_testplan.hjson`
- `tests` (L28) - `opentitan/hw/ip/hmac/data/hmac_testplan.hjson`
- `covergroups` (L163) - `opentitan/hw/ip/hmac/data/hmac_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/hmac/doc/checklist.md`
- `HMAC Checklist` (L1) - `opentitan/hw/ip/hmac/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/hmac/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/hmac/doc/checklist.md`
- `D2` (L34) - `opentitan/hw/ip/hmac/doc/checklist.md`
- `D2S` (L77) - `opentitan/hw/ip/hmac/doc/checklist.md`
- `D3` (L97) - `opentitan/hw/ip/hmac/doc/checklist.md`
- `Verification Checklist` (L125) - `opentitan/hw/ip/hmac/doc/checklist.md`
- `V1` (L127) - `opentitan/hw/ip/hmac/doc/checklist.md`
- `V2` (L177) - `opentitan/hw/ip/hmac/doc/checklist.md`
- `V2S` (L223) - `opentitan/hw/ip/hmac/doc/checklist.md`

## Code Evidence

- `prim_sha2_32` (L725) - `opentitan\hw\ip\hmac\rtl\hmac.sv`
- `cryptoc_dpi.c` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
- `collect_bytes()` (L22) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
- `c_dpi_SHA_hash()` (L58) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
- `c_dpi_SHA256_hash()` (L71) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
- `c_dpi_SHA384_hash()` (L87) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
- `c_dpi_SHA512_hash()` (L103) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
- `c_dpi_HMAC_SHA()` (L119) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
- `c_dpi_HMAC_SHA256()` (L137) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
- `c_dpi_HMAC_SHA384()` (L158) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
- `c_dpi_HMAC_SHA512()` (L180) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi.c`
- `cryptoc_dpi_pkg.sv` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi_pkg.sv`
- `hash-internal.h` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hash-internal.h`
- `hmac.c` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac.c`
- `HMAC_init_LITE()` (L48) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac.c`
- `HMAC_SHA384_init()` (L83) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac.c`
- `HMAC_SHA512_init()` (L88) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac.c`
- `HMAC_final_LITE()` (L93) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac.c`
- `hmac.h` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac.h`
- `hmac_wrap.c` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac_wrap.c`
- `HMAC_SHA()` (L14) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac_wrap.c`
- `HMAC_SHA256()` (L24) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac_wrap.c`
- `HMAC_SHA384()` (L34) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac_wrap.c`
- `HMAC_SHA512()` (L44) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac_wrap.c`
- `hmac_wrap.h` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\hmac_wrap.h`
- `main.c` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\main.c`
- `sha.c` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\sha.c`
- `sha.h` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\sha.h`
- `sha256.c` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\sha256.c`
- `sha256.h` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\sha256.h`
- `sha384.c` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\sha384.c`
- `sha384.h` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\sha384.h`
- `sha512.c` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\sha512.c`
- `sha512.h` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\sha512.h`
- `util.c` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\util.c`
- `util.h` (L1) - `opentitan\hw\ip\hmac\dv\cryptoc_dpi\util.h`
- `hmac_bind.sv` (L1) - `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv`
- `hmac_bind` (L5) - `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv`
- `tb.sv` (L1) - `opentitan\hw\ip\hmac\dv\tb\tb.sv`
- `tb` (L5) - `opentitan\hw\ip\hmac\dv\tb\tb.sv`
- `hmac_env_pkg` (L9) - `opentitan\hw\ip\hmac\dv\tests\hmac_test_pkg.sv`
- `hmac_test_pkg` (L11) - `opentitan\hw\ip\hmac\dv\tb\tb.sv`
- `hmac_if` (L28) - `opentitan\hw\ip\hmac\dv\tb\tb.sv`
- `hmac_base_test.sv` (L1) - `opentitan\hw\ip\hmac\dv\tests\hmac_base_test.sv`
- `hmac_test_pkg.sv` (L1) - `opentitan\hw\ip\hmac\dv\tests\hmac_test_pkg.sv`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:hmac` | `hmac` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_base_test.sv` | `opentitan\hw\ip\hmac\dv\tests\hmac_base_test.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_env_pkg` | `opentitan\hw\ip\hmac\dv\tests\hmac_test_pkg.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_test_pkg.sv` | `opentitan\hw\ip\hmac\dv\tests\hmac_test_pkg.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_bind.sv` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_bind` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_reg_pkg` | `opentitan\hw\ip\hmac\rtl\hmac_reg_top.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_reg_pkg.sv` | `opentitan\hw\ip\hmac\rtl\hmac_reg_pkg.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_reg_top.sv` | `opentitan\hw\ip\hmac\rtl\hmac_reg_top.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_reg_top` | `opentitan\hw\ip\hmac\rtl\hmac_reg_top.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_core.sv` | `opentitan\hw\ip\hmac\rtl\hmac_core.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_core` | `opentitan\hw\ip\hmac\rtl\hmac_core.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_test_pkg` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_if` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac.sv` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_core` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac_reg_top` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_component_matches_code` | `component:hmac` | `cryptoc_dpi_pkg.sv` | `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi_pkg.sv` |
| `spec_component_matches_code` | `component:hmac` | `prim_sha2_32` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_component_matches_code` | `component:hmac` | `tb.sv` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:hmac` | `tb` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:hmac` | `hmac.c` | `opentitan\sw\device\tests\crypto\cryptotest\firmware\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `handle_hmac()` | `opentitan\sw\device\tests\crypto\cryptotest\firmware\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac.h` | `opentitan\sw\device\tests\crypto\cryptotest\firmware\hmac.h` |
| `spec_component_matches_code` | `component:hmac` | `hmac_base()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac.c` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_configure()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `sc_hmac_hmac_sha256_configure()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_configure()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_start()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_update()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_update_words()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_process()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_final_truncated()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `sc_hmac_hmac_sha256()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_save()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac_sha256_restore()` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.c` |
| `spec_component_matches_code` | `component:hmac` | `hmac.h` | `opentitan\sw\device\silicon_creator\lib\drivers\hmac.h` |
| `spec_path_matches_code_path` | `hmac.hjson` | `prim_sha2_32` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_path_matches_code_path` | `hmac.hjson` | `cryptoc_dpi_pkg.sv` | `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `hmac.hjson` | `hmac_bind.sv` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `hmac.hjson` | `hmac_bind` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `hmac.hjson` | `tb.sv` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `hmac.hjson` | `tb` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `hmac.hjson` | `hmac_env_pkg` | `opentitan\hw\ip\hmac\dv\tests\hmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `hmac.hjson` | `hmac_test_pkg` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `prim_sha2_32` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `cryptoc_dpi_pkg.sv` | `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `hmac_bind.sv` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `hmac_bind` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `tb` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `hmac_env_pkg` | `opentitan\hw\ip\hmac\dv\tests\hmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `hmac_sec_cm_testplan.hjson` | `hmac_test_pkg` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `hmac_testplan.hjson` | `prim_sha2_32` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_path_matches_code_path` | `hmac_testplan.hjson` | `cryptoc_dpi_pkg.sv` | `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `hmac_testplan.hjson` | `hmac_bind.sv` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `hmac_testplan.hjson` | `hmac_bind` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `hmac_testplan.hjson` | `tb.sv` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `hmac_testplan.hjson` | `tb` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `hmac_testplan.hjson` | `hmac_env_pkg` | `opentitan\hw\ip\hmac\dv\tests\hmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `hmac_testplan.hjson` | `hmac_test_pkg` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_sha2_32` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `cryptoc_dpi_pkg.sv` | `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `hmac_bind.sv` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `hmac_bind` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `hmac_env_pkg` | `opentitan\hw\ip\hmac\dv\tests\hmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `hmac_test_pkg` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `prim_sha2_32` | `opentitan\hw\ip\hmac\rtl\hmac.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `cryptoc_dpi_pkg.sv` | `opentitan\hw\ip\hmac\dv\cryptoc_dpi\cryptoc_dpi_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `hmac_bind.sv` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `hmac_bind` | `opentitan\hw\ip\hmac\dv\sva\hmac_bind.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb.sv` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `tb` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `hmac_env_pkg` | `opentitan\hw\ip\hmac\dv\tests\hmac_test_pkg.sv` |
| `spec_path_matches_code_path` | `interfaces.md` | `hmac_test_pkg` | `opentitan\hw\ip\hmac\dv\tb\tb.sv` |

## Retrieval Guidance

- When a code-only query mentions `hmac`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
