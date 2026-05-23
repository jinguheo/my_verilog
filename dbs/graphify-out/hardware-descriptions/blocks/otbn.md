# Hardware Description: otbn

This document is generated from the Graphify spec-code graph. It is an intermediate anchor that helps connect code-only evidence to spec documents.

## Bridge Keys

- `ip_block`: `otbn`
- `approved_label`: `pending:otbn`
- `doc_anchor`: `otbn`
- `module_name_prefix`: `otbn`
- `bridge_edge_count`: 160

## Inferred Hardware Role

`otbn` appears as a hardware/IP block with code evidence and spec/document anchors. Use this page as the linking surface between RTL/DV/SVA files and specification sections.

## Evidence Summary

- Spec categories: document: 181, component: 41, testplan: 27, theory: 19, interface: 18
- Code categories: dv: 1608, other_code: 491, rtl: 122
- Bridge relations: spec_path_matches_code_path: 120, spec_component_matches_code: 40

## Spec Anchors

- `component:otbn` (L1) - `__graphify_spec_only__/components.md`
- `otbn.hjson` (L1) - `opentitan/hw/ip/otbn/data/otbn.hjson`
- `human name` (L6) - `opentitan/hw/ip/otbn/data/otbn.hjson`
- `one line desc` (L7) - `opentitan/hw/ip/otbn/data/otbn.hjson`
- `one paragraph desc` (L8) - `opentitan/hw/ip/otbn/data/otbn.hjson`
- `cip id` (L19) - `opentitan/hw/ip/otbn/data/otbn.hjson`
- `design spec` (L20) - `opentitan/hw/ip/otbn/data/otbn.hjson`
- `dv doc` (L21) - `opentitan/hw/ip/otbn/data/otbn.hjson`
- `hw checklist` (L22) - `opentitan/hw/ip/otbn/data/otbn.hjson`
- `sw checklist` (L23) - `opentitan/hw/ip/otbn/data/otbn.hjson`
- `revisions` (L24) - `opentitan/hw/ip/otbn/data/otbn.hjson`
- `version` (L26) - `opentitan/hw/ip/otbn/data/otbn.hjson`
- `otbn_sec_cm_testplan.hjson` (L1) - `opentitan/hw/ip/otbn/data/otbn_sec_cm_testplan.hjson`
- `testpoints` (L25) - `opentitan/hw/ip/otbn/data/otbn_sec_cm_testplan.hjson`
- `desc` (L28) - `opentitan/hw/ip/otbn/data/otbn_sec_cm_testplan.hjson`
- `stage` (L33) - `opentitan/hw/ip/otbn/data/otbn_sec_cm_testplan.hjson`
- `tests` (L34) - `opentitan/hw/ip/otbn/data/otbn_sec_cm_testplan.hjson`
- `otbn_testplan.hjson` (L1) - `opentitan/hw/ip/otbn/data/otbn_testplan.hjson`
- `import testplans` (L6) - `opentitan/hw/ip/otbn/data/otbn_testplan.hjson`
- `testpoints` (L16) - `opentitan/hw/ip/otbn/data/otbn_testplan.hjson`
- `desc` (L19) - `opentitan/hw/ip/otbn/data/otbn_testplan.hjson`
- `stage` (L28) - `opentitan/hw/ip/otbn/data/otbn_testplan.hjson`
- `tests` (L29) - `opentitan/hw/ip/otbn/data/otbn_testplan.hjson`
- `checklist.md` (L1) - `opentitan/hw/ip/otbn/doc/checklist.md`
- `OTBN Checklist` (L1) - `opentitan/hw/ip/otbn/doc/checklist.md`
- `Design Checklist` (L6) - `opentitan/hw/ip/otbn/doc/checklist.md`
- `D1` (L8) - `opentitan/hw/ip/otbn/doc/checklist.md`
- `D2` (L32) - `opentitan/hw/ip/otbn/doc/checklist.md`
- `D2S` (L74) - `opentitan/hw/ip/otbn/doc/checklist.md`
- `D3` (L94) - `opentitan/hw/ip/otbn/doc/checklist.md`
- `Verification Checklist` (L120) - `opentitan/hw/ip/otbn/doc/checklist.md`
- `V1` (L122) - `opentitan/hw/ip/otbn/doc/checklist.md`
- `V2` (L172) - `opentitan/hw/ip/otbn/doc/checklist.md`
- `V2S` (L218) - `opentitan/hw/ip/otbn/doc/checklist.md`
- `developing_otbn.md` (L1) - `opentitan/hw/ip/otbn/doc/developing_otbn.md`

## Code Evidence

- `keymgr_pkg` (L11) - `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv`
- `key_sideload_if` (L36) - `opentitan\hw\ip\otbn\dv\uvm\tb.sv`
- `edn_pkg` (L10) - `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv`
- `otbn_memutil.cc` (L1) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `OtbnMemUtil()` (L14) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.h`
- `LoadElf()` (L29) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `GetLoopWarp()` (L37) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `OnElfLoaded()` (L43) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `OnSymbol()` (L76) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `AddLoopWarp()` (L114) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `OtbnMemUtilMake()` (L130) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `OtbnMemUtilFree()` (L139) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `OtbnMemUtilLoadElf()` (L141) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `OtbnMemUtilStageElf()` (L155) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `OtbnMemUtilGetSegCount()` (L169) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `OtbnMemUtilGetSegInfo()` (L184) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `OtbnMemUtilGetSegData()` (L231) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `OtbnMemUtilGetExpEndAddr()` (L276) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `OtbnMemUtilGetLoopWarp()` (L281) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `OtbnMemUtilGetNumLoopWarps()` (L293) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `OtbnMemUtilGetLoopWarpByIndex()` (L302) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
- `otbn_memutil.h` (L1) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.h`
- `otbn_memutil_pkg.sv` (L1) - `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil_pkg.sv`
- `sv_utils.h` (L1) - `opentitan\hw\ip\otbn\dv\memutil\sv_utils.h`
- `set_sv_u8()` (L11) - `opentitan\hw\ip\otbn\dv\memutil\sv_utils.h`
- `set_sv_u32()` (L20) - `opentitan\hw\ip\otbn\dv\memutil\sv_utils.h`
- `get_sv_u32()` (L29) - `opentitan\hw\ip\otbn\dv\memutil\sv_utils.h`
- `iss_wrapper.cc` (L1) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `TmpDir()` (L37) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `find_repo_top()` (L114) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `find_otbn_model()` (L193) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `read_hex_32()` (L206) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `read_ext_reg()` (L215) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `read_ext_flag()` (L242) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `reset()` (L260) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `ISSWrapper()` (L269) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `load_d()` (L354) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `load_i()` (L360) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `add_loop_warp()` (L366) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `clear_loop_warps()` (L374) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `dump_d()` (L378) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `start_operation()` (L384) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `otp_key_cdc_done()` (L408) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `edn_rnd_cdc_done()` (L412) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`
- `edn_urnd_cdc_done()` (L416) - `opentitan\hw\ip\otbn\dv\model\iss_wrapper.cc`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:otbn` | `otbn_model_agent_cfg.sv` | `opentitan\hw\ip\otbn\dv\uvm\otbn_model_agent\otbn_model_agent_cfg.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_model_agent_pkg.sv` | `opentitan\hw\ip\otbn\dv\uvm\otbn_model_agent\otbn_model_agent_pkg.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_model_monitor.sv` | `opentitan\hw\ip\otbn\dv\uvm\otbn_model_agent\otbn_model_monitor.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_model_agent.sv` | `opentitan\hw\ip\otbn\dv\uvm\otbn_model_agent\otbn_model_agent.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_model_item.sv` | `opentitan\hw\ip\otbn\dv\uvm\otbn_model_agent\otbn_model_item.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_model_if.sv` | `opentitan\hw\ip\otbn\dv\uvm\otbn_model_agent\otbn_model_if.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_mock_edn_bivium.sv` | `opentitan\hw\ip\otbn\dv\verilator\otbn_mock_edn_bivium.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_mock_edn_bivium` | `opentitan\hw\ip\otbn\dv\verilator\otbn_mock_edn_bivium.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_stack_snooper_if.sv` | `opentitan\hw\ip\otbn\dv\model\otbn_stack_snooper_if.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_top_coco.v` | `opentitan\hw\ip\otbn\pre_sca\alma\rtl\otbn_top_coco.v` |
| `spec_component_matches_code` | `component:otbn` | `otbn_top_coco` | `opentitan\hw\ip\otbn\pre_sca\alma\rtl\otbn_top_coco.v` |
| `spec_component_matches_code` | `component:otbn` | `otbn` | `opentitan\hw\top_earlgrey\rtl\autogen\top_earlgrey.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_idle_checker.sv` | `opentitan\hw\ip\otbn\dv\uvm\sva\otbn_idle_checker.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_idle_checker` | `opentitan\hw\ip\otbn\dv\uvm\sva\otbn_idle_checker.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_mod_result_selector.sv` | `opentitan\hw\ip\otbn\rtl\otbn_mod_result_selector.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_mod_result_selector` | `opentitan\hw\ip\otbn\rtl\otbn_mod_result_selector.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_memutil_pkg.sv` | `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil_pkg.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_rf_snooper_if.sv` | `opentitan\hw\ip\otbn\dv\model\otbn_rf_snooper_if.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_trace_if.sv` | `opentitan\hw\ip\otbn\dv\tracer\rtl\otbn_trace_if.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_base_test.sv` | `opentitan\hw\ip\otbn\dv\uvm\tests\otbn_base_test.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_start_stop_control.sv` | `opentitan\hw\ip\otbn\rtl\otbn_start_stop_control.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_start_stop_control` | `opentitan\hw\ip\otbn\rtl\otbn_start_stop_control.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_env_pkg` | `opentitan\hw\ip\otbn\dv\uvm\tests\otbn_test_pkg.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_test_pkg.sv` | `opentitan\hw\ip\otbn\dv\uvm\tests\otbn_test_pkg.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_memutil_pkg` | `opentitan\hw\ip\otbn\dv\uvm\tests\otbn_test_pkg.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_mock_edn.sv` | `opentitan\hw\ip\otbn\dv\verilator\otbn_mock_edn.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_mock_edn` | `opentitan\hw\ip\otbn\dv\verilator\otbn_mock_edn.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_instruction_fetch.sv` | `opentitan\hw\ip\otbn\rtl\otbn_instruction_fetch.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_instruction_fetch` | `opentitan\hw\ip\otbn\rtl\otbn_instruction_fetch.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_predecode` | `opentitan\hw\ip\otbn\rtl\otbn_instruction_fetch.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_tracer.sv` | `opentitan\hw\ip\otbn\dv\tracer\rtl\otbn_tracer.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_tracer` | `opentitan\hw\ip\otbn\dv\tracer\rtl\otbn_tracer.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_core_model` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_top_sim.sv` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_top_sim` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_mock_edn` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_mock_edn_bivium` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_core_model.sv` | `opentitan\hw\ip\otbn\dv\model\otbn_core_model.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_core_model` | `opentitan\hw\ip\otbn\dv\model\otbn_core_model.sv` |
| `spec_component_matches_code` | `component:otbn` | `otbn_loop_controller.sv` | `opentitan\hw\ip\otbn\rtl\otbn_loop_controller.sv` |
| `spec_path_matches_code_path` | `otbn.hjson` | `keymgr_pkg` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_path_matches_code_path` | `otbn.hjson` | `key_sideload_if` | `opentitan\hw\ip\otbn\dv\uvm\tb.sv` |
| `spec_path_matches_code_path` | `otbn.hjson` | `edn_pkg` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_path_matches_code_path` | `otbn.hjson` | `otbn_memutil_pkg.sv` | `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil_pkg.sv` |
| `spec_path_matches_code_path` | `otbn.hjson` | `otbn_core_model.sv` | `opentitan\hw\ip\otbn\dv\model\otbn_core_model.sv` |
| `spec_path_matches_code_path` | `otbn.hjson` | `otbn_core_model` | `opentitan\hw\ip\otbn\dv\model\otbn_core_model.sv` |
| `spec_path_matches_code_path` | `otbn.hjson` | `otbn_pkg` | `opentitan\hw\ip\otbn\rtl\otbn_vec_transposer.sv` |
| `spec_path_matches_code_path` | `otbn.hjson` | `otbn_rf_snooper_if.sv` | `opentitan\hw\ip\otbn\dv\model\otbn_rf_snooper_if.sv` |
| `spec_path_matches_code_path` | `otbn_sec_cm_testplan.hjson` | `keymgr_pkg` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_path_matches_code_path` | `otbn_sec_cm_testplan.hjson` | `key_sideload_if` | `opentitan\hw\ip\otbn\dv\uvm\tb.sv` |
| `spec_path_matches_code_path` | `otbn_sec_cm_testplan.hjson` | `edn_pkg` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_path_matches_code_path` | `otbn_sec_cm_testplan.hjson` | `otbn_memutil_pkg.sv` | `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil_pkg.sv` |
| `spec_path_matches_code_path` | `otbn_sec_cm_testplan.hjson` | `otbn_core_model.sv` | `opentitan\hw\ip\otbn\dv\model\otbn_core_model.sv` |
| `spec_path_matches_code_path` | `otbn_sec_cm_testplan.hjson` | `otbn_core_model` | `opentitan\hw\ip\otbn\dv\model\otbn_core_model.sv` |
| `spec_path_matches_code_path` | `otbn_sec_cm_testplan.hjson` | `otbn_pkg` | `opentitan\hw\ip\otbn\rtl\otbn_vec_transposer.sv` |
| `spec_path_matches_code_path` | `otbn_sec_cm_testplan.hjson` | `otbn_rf_snooper_if.sv` | `opentitan\hw\ip\otbn\dv\model\otbn_rf_snooper_if.sv` |
| `spec_path_matches_code_path` | `otbn_testplan.hjson` | `keymgr_pkg` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_path_matches_code_path` | `otbn_testplan.hjson` | `key_sideload_if` | `opentitan\hw\ip\otbn\dv\uvm\tb.sv` |
| `spec_path_matches_code_path` | `otbn_testplan.hjson` | `edn_pkg` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_path_matches_code_path` | `otbn_testplan.hjson` | `otbn_memutil_pkg.sv` | `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil_pkg.sv` |
| `spec_path_matches_code_path` | `otbn_testplan.hjson` | `otbn_core_model.sv` | `opentitan\hw\ip\otbn\dv\model\otbn_core_model.sv` |
| `spec_path_matches_code_path` | `otbn_testplan.hjson` | `otbn_core_model` | `opentitan\hw\ip\otbn\dv\model\otbn_core_model.sv` |
| `spec_path_matches_code_path` | `otbn_testplan.hjson` | `otbn_pkg` | `opentitan\hw\ip\otbn\rtl\otbn_vec_transposer.sv` |
| `spec_path_matches_code_path` | `otbn_testplan.hjson` | `otbn_rf_snooper_if.sv` | `opentitan\hw\ip\otbn\dv\model\otbn_rf_snooper_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `keymgr_pkg` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `key_sideload_if` | `opentitan\hw\ip\otbn\dv\uvm\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `edn_pkg` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `otbn_memutil_pkg.sv` | `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `otbn_core_model.sv` | `opentitan\hw\ip\otbn\dv\model\otbn_core_model.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `otbn_core_model` | `opentitan\hw\ip\otbn\dv\model\otbn_core_model.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `otbn_pkg` | `opentitan\hw\ip\otbn\rtl\otbn_vec_transposer.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `otbn_rf_snooper_if.sv` | `opentitan\hw\ip\otbn\dv\model\otbn_rf_snooper_if.sv` |
| `spec_path_matches_code_path` | `developing_otbn.md` | `keymgr_pkg` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_path_matches_code_path` | `developing_otbn.md` | `key_sideload_if` | `opentitan\hw\ip\otbn\dv\uvm\tb.sv` |
| `spec_path_matches_code_path` | `developing_otbn.md` | `edn_pkg` | `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv` |
| `spec_path_matches_code_path` | `developing_otbn.md` | `otbn_memutil_pkg.sv` | `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil_pkg.sv` |
| `spec_path_matches_code_path` | `developing_otbn.md` | `otbn_core_model.sv` | `opentitan\hw\ip\otbn\dv\model\otbn_core_model.sv` |
| `spec_path_matches_code_path` | `developing_otbn.md` | `otbn_core_model` | `opentitan\hw\ip\otbn\dv\model\otbn_core_model.sv` |
| `spec_path_matches_code_path` | `developing_otbn.md` | `otbn_pkg` | `opentitan\hw\ip\otbn\rtl\otbn_vec_transposer.sv` |
| `spec_path_matches_code_path` | `developing_otbn.md` | `otbn_rf_snooper_if.sv` | `opentitan\hw\ip\otbn\dv\model\otbn_rf_snooper_if.sv` |

## Retrieval Guidance

- When a code-only query mentions `otbn`, use this hardware description to expand toward spec anchors.
- Prefer exact module/file evidence first, then bridge to matching spec components, testplans, theory docs, and interface docs.
- Human review can replace `pending:*` with an approved label after validating the connection.
