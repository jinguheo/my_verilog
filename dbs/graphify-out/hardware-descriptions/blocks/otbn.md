# Hardware Description: otbn

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **OpenTitan Big Number Accelerator OTBN**: This directory contains the implementation of the OpenTitan Big Number
- **Develop OTBN**: See [here](../README.md) for documentation on
- **Build OTBN software**: the current version of OTBN; documentation matching the code in this directory

## Identity

- `ip_block`: `otbn`
- `bridge_edge_count`: 160
- Spec categories: document: 181, component: 41, testplan: 27, theory: 19, interface: 18
- Code categories: dv: 1608, other_code: 491, rtl: 122
- Bridge relations: spec_path_matches_code_path: 120, spec_component_matches_code: 40

## Spec Excerpts

### OpenTitan Big Number Accelerator OTBN
_Source: `opentitan/hw/ip/otbn/doc/developing_otbn.md`_

```
# OpenTitan Big Number Accelerator (OTBN)

This directory contains the implementation of the OpenTitan Big Number
Accelerator (OTBN). OTBN is a coprocessor for asymmetric cryptographic
operations like RSA or Elliptic Curve Cryptography (ECC).

See [here](../README.md) for documentation on
the current version of OTBN; documentation matching the code in this directory
```

### Develop OTBN
_Source: `opentitan/hw/ip/otbn/doc/developing_otbn.md`_

```
See [here](../README.md) for documentation on
the current version of OTBN; documentation matching the code in this directory
can be found in the `doc` directory.

OTBN is under active development. Please ask questions and report issues
through the [GitHub issue tracker](https://github.com/lowRISC/opentitan/issues).

## Develop OTBN

### Build OTBN software

An assembler, linker and disassembler fo
…
```

### Build OTBN software
_Source: `opentitan/hw/ip/otbn/doc/developing_otbn.md`_

```
the current version of OTBN; documentation matching the code in this directory
can be found in the `doc` directory.

OTBN is under active development. Please ask questions and report issues
through the [GitHub issue tracker](https://github.com/lowRISC/opentitan/issues).

## Develop OTBN

### Build OTBN software

An assembler, linker and disassembler for OTBN can be found in `hw/ip/otbn/util`
(For
…
```

### Hardware Interfaces
_Source: `opentitan/hw/ip/otbn/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/otbn/data/otbn.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`otbn`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_edn_i`**, **`clk_otp_i`**
- Bus Devi
…
```

### Inter-Module Signals
_Source: `opentitan/hw/ip/otbn/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/otbn/data/otbn.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`otbn`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_edn_i`**, **`clk_otp_i`**
- Bus Device Interfaces (TL-UL):
…
```

### Interrupts
_Source: `opentitan/hw/ip/otbn/doc/interfaces.md`_

```
| ram_cfg_rsp_imem | prim_ram_1p_pkg::ram_1p_cfg_rsp | uni     | req   |       1 |               |
| ram_cfg_rsp_dmem | prim_ram_1p_pkg::ram_1p_cfg_rsp | uni     | req   |       1 |               |
| lc_escalate_en   | lc_ctrl_pkg::lc_tx              | uni     | rcv   |       1 |               |
| lc_rma_req       | lc_ctrl_pkg::lc_tx              | uni     | rcv   |       1 |               |
| lc
…
```

### OpenTitan Big Number Accelerator OTBN Instruction Set Architecture
_Source: `opentitan/hw/ip/otbn/doc/isa.md`_

```
# OpenTitan Big Number Accelerator (OTBN) Instruction Set Architecture

This document describes the instruction set for OTBN.
For more details about the processor itself, see the [OTBN Technical Specification](../README.md).
In particular, this document assumes knowledge of the *Processor State* section from that guide.

The instruction set is split into *base* and *big number* subsets.
The base s
…
```

### Pseudo-code for operation descriptions
_Source: `opentitan/hw/ip/otbn/doc/isa.md`_

```
These operands are further documented in a table.
Immediate operands like `offset` show their valid range of values.

Below the table of operands is an encoding table.
This shows how the 32 bits of the instruction word are filled in.
Ranges of bits that map to an operand are named (in capitals) and those names are used in the operand table.
For example, the `SW` instruction's `offset` operand is s
…
```

## Spec Anchors

- `component:otbn` (L1) — `__graphify_spec_only__/components.md`
- `otbn.hjson` (L1) — `opentitan/hw/ip/otbn/data/otbn.hjson`
- `human name` (L6) — `opentitan/hw/ip/otbn/data/otbn.hjson`
- `one line desc` (L7) — `opentitan/hw/ip/otbn/data/otbn.hjson`
- `one paragraph desc` (L8) — `opentitan/hw/ip/otbn/data/otbn.hjson`
- `cip id` (L19) — `opentitan/hw/ip/otbn/data/otbn.hjson`
- `design spec` (L20) — `opentitan/hw/ip/otbn/data/otbn.hjson`
- `dv doc` (L21) — `opentitan/hw/ip/otbn/data/otbn.hjson`
- `hw checklist` (L22) — `opentitan/hw/ip/otbn/data/otbn.hjson`
- `sw checklist` (L23) — `opentitan/hw/ip/otbn/data/otbn.hjson`
- `revisions` (L24) — `opentitan/hw/ip/otbn/data/otbn.hjson`
- `version` (L26) — `opentitan/hw/ip/otbn/data/otbn.hjson`
- `otbn_sec_cm_testplan.hjson` (L1) — `opentitan/hw/ip/otbn/data/otbn_sec_cm_testplan.hjson`
- `testpoints` (L25) — `opentitan/hw/ip/otbn/data/otbn_sec_cm_testplan.hjson`
- `desc` (L28) — `opentitan/hw/ip/otbn/data/otbn_sec_cm_testplan.hjson`
- `stage` (L33) — `opentitan/hw/ip/otbn/data/otbn_sec_cm_testplan.hjson`
- `tests` (L34) — `opentitan/hw/ip/otbn/data/otbn_sec_cm_testplan.hjson`
- `otbn_testplan.hjson` (L1) — `opentitan/hw/ip/otbn/data/otbn_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/ip/otbn/data/otbn_testplan.hjson`
- `testpoints` (L16) — `opentitan/hw/ip/otbn/data/otbn_testplan.hjson`
- `desc` (L19) — `opentitan/hw/ip/otbn/data/otbn_testplan.hjson`
- `stage` (L28) — `opentitan/hw/ip/otbn/data/otbn_testplan.hjson`
- `tests` (L29) — `opentitan/hw/ip/otbn/data/otbn_testplan.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip/otbn/doc/checklist.md`
- `OTBN Checklist` (L1) — `opentitan/hw/ip/otbn/doc/checklist.md`
- `Design Checklist` (L6) — `opentitan/hw/ip/otbn/doc/checklist.md`
- `D1` (L8) — `opentitan/hw/ip/otbn/doc/checklist.md`
- `D2` (L32) — `opentitan/hw/ip/otbn/doc/checklist.md`
- `D2S` (L74) — `opentitan/hw/ip/otbn/doc/checklist.md`
- `D3` (L94) — `opentitan/hw/ip/otbn/doc/checklist.md`
- `Verification Checklist` (L120) — `opentitan/hw/ip/otbn/doc/checklist.md`
- `V1` (L122) — `opentitan/hw/ip/otbn/doc/checklist.md`
- `V2` (L172) — `opentitan/hw/ip/otbn/doc/checklist.md`
- `V2S` (L218) — `opentitan/hw/ip/otbn/doc/checklist.md`
- `developing_otbn.md` (L1) — `opentitan/hw/ip/otbn/doc/developing_otbn.md`

## Code Evidence

**DV** (50)
  - `keymgr_pkg`:L11 — `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv`
  - `key_sideload_if`:L36 — `opentitan\hw\ip\otbn\dv\uvm\tb.sv`
  - `edn_pkg`:L10 — `opentitan\hw\ip\otbn\dv\verilator\otbn_top_sim.sv`
  - `otbn_memutil.cc`:L1 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `OtbnMemUtil()`:L14 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.h`
  - `LoadElf()`:L29 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `GetLoopWarp()`:L37 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `OnElfLoaded()`:L43 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `OnSymbol()`:L76 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `AddLoopWarp()`:L114 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `OtbnMemUtilMake()`:L130 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `OtbnMemUtilFree()`:L139 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `OtbnMemUtilLoadElf()`:L141 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `OtbnMemUtilStageElf()`:L155 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `OtbnMemUtilGetSegCount()`:L169 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `OtbnMemUtilGetSegInfo()`:L184 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `OtbnMemUtilGetSegData()`:L231 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `OtbnMemUtilGetExpEndAddr()`:L276 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `OtbnMemUtilGetLoopWarp()`:L281 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`
  - `OtbnMemUtilGetNumLoopWarps()`:L293 — `opentitan\hw\ip\otbn\dv\memutil\otbn_memutil.cc`

## Neighbor Components

- `lowrisc_ibex` (221 refs; calls×207, instantiates×11, imports_from×3)
- `riscv-tests` (107 refs; calls×107)
- `otp_ctrl_descrambling_test.c` (23 refs; calls×23)
- `rv_core_ibex` (10 refs; imports_from×5, instantiates×5)
- `keymgr` (10 refs; imports_from×10)
- `i2c.rs` (7 refs; calls×7)
- `rv_plic` (6 refs; instantiates×6)
- `gpiodpi` (6 refs; calls×6)
- `tlul` (5 refs; instantiates×5)
- `prim` (5 refs; calls×3, instantiates×2)
- `riscv-test-env` (5 refs; calls×5)
- `ac_range_check` (5 refs; instantiates×5)

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

## Retrieval Guidance

- For code-only queries mentioning `otbn`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `otbn`.
