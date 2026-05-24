# Hardware Description: racl_ctrl

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Programmer's Guide**: RACL Control can be configured through its [registers](./registers.md).
- **RACL Policies**: RACL Control can be configured through its [registers](./registers.md).
- **Interrupts**: RACL Control can be configured through its [registers](./registers.md).

## Identity

- `ip_block`: `racl_ctrl`
- `bridge_edge_count`: 206
- Spec categories: document: 222, interface: 29, component: 23, theory: 22, testplan: 14
- Code categories: dv: 118, rtl: 81, sva: 28
- Bridge relations: spec_path_matches_code_path: 184, spec_component_matches_code: 22

## Spec Excerpts

### Programmer's Guide
_Source: `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

RACL Control can be configured through its [registers](./registers.md).

## RACL Policies

Each RACL policy has a register named after the policy which contains a permission bitmap for read and write permissions for each of the roles defined in the top-level configuration.
The exact register layout is defined in [RACL: Register Access Control List](../../../../../doc/contribu
…
```

### RACL Policies
_Source: `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

RACL Control can be configured through its [registers](./registers.md).

## RACL Policies

Each RACL policy has a register named after the policy which contains a permission bitmap for read and write permissions for each of the roles defined in the top-level configuration.
The exact register layout is defined in [RACL: Register Access Control List](../../../../../doc/contribu
…
```

### Interrupts
_Source: `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`_

```
RACL Control can be configured through its [registers](./registers.md).

## RACL Policies

Each RACL policy has a register named after the policy which contains a permission bitmap for read and write permissions for each of the roles defined in the top-level configuration.
The exact register layout is defined in [RACL: Register Access Control List](../../../../../doc/contributing/hw/racl/README.md
…
```

### Hardware Interfaces
_Source: `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/top_darjeeling/ip_autogen/racl_ctrl/data/racl_ctrl.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`racl_ctrl`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none
…
```

### Inter-Module Signals
_Source: `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/top_darjeeling/ip_autogen/racl_ctrl/data/racl_ctrl.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`racl_ctrl`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus Device Interfac
…
```

### Interrupts
_Source: `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/interfaces.md`_

```
| Port Name           | Package::Struct               | Type    | Act   | Width                     | Description                                                                            |
|:--------------------|:------------------------------|:--------|:------|:--------------------------|:---------------------------------------------------------------------------------------|
| racl_policies
…
```

### Programmer's Guide
_Source: `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

RACL Control can be configured through its [registers](./registers.md).

## RACL Policies

Each RACL policy has a register named after the policy which contains a permission bitmap for read and write permissions for each of the roles defined in the top-level configuration.
The exact register layout is defined in [RACL: Register Access Control List](../../../../../doc/contribu
…
```

### RACL Policies
_Source: `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/doc/programmers_guide.md`_

```
# Programmer's Guide

RACL Control can be configured through its [registers](./registers.md).

## RACL Policies

Each RACL policy has a register named after the policy which contains a permission bitmap for read and write permissions for each of the roles defined in the top-level configuration.
The exact register layout is defined in [RACL: Register Access Control List](../../../../../doc/contribu
…
```

## Spec Anchors

- `component:racl_ctrl` (L1) — `__graphify_spec_only__/components.md`
- `racl_ctrl_testplan.hjson` (L1) — `opentitan/hw/ip/racl_ctrl/data/racl_ctrl_testplan.hjson`
- `import testplans` (L10) — `opentitan/hw/ip/racl_ctrl/data/racl_ctrl_testplan.hjson`
- `testpoints` (L28) — `opentitan/hw/ip/racl_ctrl/data/racl_ctrl_testplan.hjson`
- `desc` (L31) — `opentitan/hw/ip/racl_ctrl/data/racl_ctrl_testplan.hjson`
- `stage` (L38) — `opentitan/hw/ip/racl_ctrl/data/racl_ctrl_testplan.hjson`
- `tests` (L39) — `opentitan/hw/ip/racl_ctrl/data/racl_ctrl_testplan.hjson`
- `racl_ctrl.tpldesc.hjson` (L1) — `opentitan/hw/ip_templates/racl_ctrl/data/racl_ctrl.tpldesc.hjson`
- `template param list` (L5) — `opentitan/hw/ip_templates/racl_ctrl/data/racl_ctrl.tpldesc.hjson`
- `desc` (L8) — `opentitan/hw/ip_templates/racl_ctrl/data/racl_ctrl.tpldesc.hjson`
- `checklist.md` (L1) — `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `Design Checklist` (L13) — `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `D1` (L15) — `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `D2` (L41) — `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `D2S` (L83) — `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `D3` (L103) — `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `Verification Checklist` (L129) — `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `V1` (L131) — `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `V2` (L181) — `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `V2S` (L227) — `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `V3` (L243) — `opentitan/hw/ip_templates/racl_ctrl/doc/checklist.md`
- `programmers_guide.md` (L1) — `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `Programmer's Guide` (L1) — `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `RACL Policies` (L5) — `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `Interrupts` (L11) — `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `Error Logs` (L16) — `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `Programming Sequence` (L29) — `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `Initializing the IP` (L31) — `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `Checking for and handling RACL errors` (L40) — `opentitan/hw/ip_templates/racl_ctrl/doc/programmers_guide.md`
- `racl_ctrl.hjson` (L1) — `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/data/racl_ctrl.hjson`
- `human name` (L9) — `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/data/racl_ctrl.hjson`
- `one line desc` (L10) — `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/data/racl_ctrl.hjson`
- `one paragraph desc` (L11) — `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/data/racl_ctrl.hjson`
- `cip id` (L15) — `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/data/racl_ctrl.hjson`
- `design spec` (L16) — `opentitan/hw/top_darjeeling/ip_autogen/racl_ctrl/data/racl_ctrl.hjson`

## Code Evidence

**RTL** (17)
  - `racl_ctrl.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv`
  - `racl_ctrl`:L7 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv`
  - `racl_ctrl_reg_pkg`:L33 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_top.sv`
  - `racl_ctrl_reg_top`:L47 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv`
  - `prim_racl_error_arb`:L147 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv`
  - `racl_ctrl_reg_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_pkg.sv`
  - `racl_ctrl_reg_top.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_top.sv`
  - `racl_ctrl_reg_top`:L9 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_top.sv`
  - `racl_ctrl`:L2657 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `prim_flop_en`:L269 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
  - `prim_ram_1p_adv`:L1487 — `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
  - `tlul_cmd_intg_gen`:L46 — `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv`
  - `dma`:L2221 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `keymgr_dpe`:L1905 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `tlul_jtag_dtm`:L1340 — `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
  - `mbx`:L2257 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `prim_onehot_enc`:L128 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
**DV** (11)
  - `racl_ctrl_base_test.sv`:L1 — `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_base_test.sv`
  - `racl_ctrl_test_pkg.sv`:L1 — `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_test_pkg.sv`
  - `racl_ctrl_base_env_pkg`:L65 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv`
  - `racl_ctrl_env_cfg.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv`
  - `racl_ctrl_env_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv`
  - `racl_ctrl_ral_pkg`:L11 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv`
  - `tb.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv`
  - `tb`:L5 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv`
  - `racl_ctrl_test_pkg`:L13 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv`
  - `racl_error_log_if`:L30 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv`
  - `racl_ctrl_env_pkg`:L66 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv`
**SVA** (10)
  - `racl_ctrl_bind.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\sva\racl_ctrl_bind.sv`
  - `racl_ctrl_bind`:L5 — `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\sva\racl_ctrl_bind.sv`
  - `clkmgr_aon_cg_en_sva_if.sv`:L1 — `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv`
  - `clkmgr_cg_en_sva_if.sv`:L1 — `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv`
  - `clkmgr_div_sva_if.sv`:L1 — `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv`
  - `clkmgr_extclk_sva_if.sv`:L1 — `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv`
  - `clkmgr_gated_clock_sva_if.sv`:L1 — `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv`
  - `clkmgr_lost_calib_ctrl_en_sva_if.sv`:L1 — `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv`
  - `clkmgr_lost_calib_regwen_sva_if.sv`:L1 — `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv`
  - `clkmgr_sec_cm_checker_assert.sv`:L1 — `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv`

## Neighbor Components

- `rv_plic` (6 refs; instantiates×6)
- `lowrisc_ibex` (3 refs; instantiates×2, imports_from×1)
- `pwrmgr` (3 refs; instantiates×3)
- `flash_ctrl` (2 refs; instantiates×2)
- `rstmgr` (1 refs; imports_from×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\sva\racl_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_bind` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\sva\racl_ctrl_bind.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_reg_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_reg_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_pkg.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_reg_top.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_reg_top` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl_reg_top.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_env_cfg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_env_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_ral_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_reg_top` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_base_test.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_base_test.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_base_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_test_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_ctrl_test_pkg.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_test_pkg.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `prim_racl_error_arb` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\rtl\racl_ctrl.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_component_matches_code` | `component:racl_ctrl` | `racl_error_log_if` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `racl_ctrl_base_test.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_base_test.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `racl_ctrl_test_pkg.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `racl_ctrl_base_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `racl_ctrl_env_cfg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `racl_ctrl_env_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `racl_ctrl_ral_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `racl_ctrl_testplan.hjson` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `racl_ctrl_base_test.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_base_test.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `racl_ctrl_test_pkg.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `racl_ctrl_base_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `racl_ctrl_env_cfg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `racl_ctrl_env_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `racl_ctrl_ral_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_lost_calib_regwen_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_regwen_sva_if.sv` |
| `spec_path_matches_code_path` | `racl_ctrl.tpldesc.hjson` | `clkmgr_sec_cm_checker_assert.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_sec_cm_checker_assert.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `racl_ctrl_base_test.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_base_test.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `racl_ctrl_test_pkg.sv` | `opentitan\hw\ip\racl_ctrl\dv\tests\racl_ctrl_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `racl_ctrl_base_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `racl_ctrl_env_cfg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_cfg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `racl_ctrl_env_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `racl_ctrl_ral_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\racl_ctrl_env_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\racl_ctrl\dv\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_aon_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_aon_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_cg_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_cg_en_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_div_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_div_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_extclk_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_extclk_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_gated_clock_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_gated_clock_sva_if.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `clkmgr_lost_calib_ctrl_en_sva_if.sv` | `opentitan\hw\ip_templates\clkmgr\dv\sva\clkmgr_lost_calib_ctrl_en_sva_if.sv` |

## Retrieval Guidance

- For code-only queries mentioning `racl_ctrl`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `racl_ctrl`.
