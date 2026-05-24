# Hardware Description: ac_range_check

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Hardware Interfaces**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`ac_range_check`** has the following hardware interfaces defined
- **Inter-Module Signals**: Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`ac_range_check`** has the following hardware interfaces defined

## Identity

- `ip_block`: `ac_range_check`
- `bridge_edge_count`: 174
- Spec categories: document: 134, testplan: 35, theory: 25, component: 21, interface: 21
- Code categories: rtl: 111, dv: 56, sva: 26
- Bridge relations: spec_path_matches_code_path: 154, spec_component_matches_code: 20

## Spec Excerpts

### Hardware Interfaces
_Source: `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`_

```
# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`ac_range_check`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Othe
…
```

### Inter-Module Signals
_Source: `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`_

```
<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`ac_range_check`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: *none*
- Bus
…
```

### Interrupts
_Source: `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/interfaces.md`_

```
| ctn_tl_h2d            | tlul_pkg::tl_h2d              | uni     | rcv   |       1 | TL-UL input port (request part), synchronous                                                                                         |
| ctn_tl_d2h            | tlul_pkg::tl_d2h              | uni     | req   |       1 | TL-UL input port (response part), synchronous
…
```

### Summary
_Source: `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/registers.md`_

```
# Registers

<!-- BEGIN CMDGEN util/regtool.py -d ./hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson -->
## Summary

| Name                                                                          | Offset   |   Length | Description                                                                                                                                               |
|:
…
```

### INTR STATE
_Source: `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/registers.md`_

```
| ac_range_check.[`RANGE_RACL_POLICY_SHADOWED_25`](#range_racl_policy_shadowed) | 0x284    |        4 | The RACL policy register allows the system to further restrict the access to specific source roles.                                                       |
| ac_range_check.[`RANGE_RACL_POLICY_SHADOWED_26`](#range_racl_policy_shadowed) | 0x288    |        4 | The RACL policy register allows the
…
```

### Fields
_Source: `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/registers.md`_

```
| ac_range_check.[`RANGE_RACL_POLICY_SHADOWED_31`](#range_racl_policy_shadowed) | 0x29c    |        4 | The RACL policy register allows the system to further restrict the access to specific source roles.                                                       |

## INTR_STATE
Interrupt State Register
- Offset: `0x0`
- Reset default: `0x0`
- Reset mask: `0x1`

### Fields

```wavejson
{"reg": [{"name"
…
```

### Theory of Operation
_Source: `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`_

```
# Theory of Operation

The following pseudo-code illustrates the range check logic, incorporating range priorities and access control rules.
The default system behavior is to deny access unless explicitly allowed by the range configuration.
The incoming address is compared against each enabled range register, and access control decisions are made based on matching and permissions.
The priority ord
…
```

### Return the final access decision
_Source: `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/theory_of_operation.md`_

```
access_granted = True
        else if access_type == WRITE and range[i].write and access_role in range[i].write_perm:
          access_granted = True
        else:
          access_granted = False   # No matching permissions
        # Stop after the first match (highest-priority range matched)
        break

  # Return the final access decision
  if access_granted:
    return ACCESS_GRANTED
  else
…
```

## Spec Anchors

- `component:ac_range_check` (L1) — `__graphify_spec_only__/components.md`
- `ac_range_check.hjson` (L1) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `human name` (L8) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `one line desc` (L9) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `one paragraph desc` (L10) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `cip id` (L12) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `design spec` (L13) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `dv doc` (L14) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `version` (L15) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `clocking` (L17) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `bus interfaces` (L18) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `param list` (L21) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check.hjson`
- `ac_range_check_testplan.hjson` (L1) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `import testplans` (L6) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `testpoints` (L12) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `desc` (L15) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `Stimulus` (L19) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `Checking` (L29) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `stage` (L46) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `tests` (L47) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `covergroups` (L105) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/ac_range_check_testplan.hjson`
- `top_darjeeling_ac_range_check.ipconfig.hjson` (L1) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `instance name` (L5) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `param values` (L6) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `num ranges` (L8) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `nr role bits` (L9) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `nr ctn uid bits` (L10) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `module instance name` (L11) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `topname` (L12) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `uniquified modules` (L13) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `dtgen` (L15) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson`
- `checklist.md` (L1) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md`
- `Design Checklist` (L13) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md`
- `D1` (L15) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md`
- `D2` (L41) — `opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/doc/checklist.md`

## Code Evidence

**RTL** (18)
  - `prim_flop_en`:L269 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
  - `prim_onehot_enc`:L128 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
  - `ac_range_check.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
  - `ac_range_check`:L7 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
  - `ac_range_check_reg_pkg`:L36 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_top.sv`
  - `ac_range_check_reg_top`:L53 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
  - `prim_leading_one_ppc`:L217 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
  - `tlul_request_loopback`:L245 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv`
  - `ac_range_check_reg_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_pkg.sv`
  - `ac_range_check_reg_top.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_top.sv`
  - `ac_range_check_reg_top`:L9 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_top.sv`
  - `ac_range_check`:L2684 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `prim_ram_1p_adv`:L1487 — `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
  - `tlul_cmd_intg_gen`:L46 — `opentitan\hw\top_darjeeling\ip\soc_proxy\rtl\bat.sv`
  - `dma`:L2221 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `keymgr_dpe`:L1905 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
  - `tlul_jtag_dtm`:L1340 — `opentitan\hw\top_darjeeling\rtl\autogen\chip_darjeeling_asic.sv`
  - `mbx`:L2257 — `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv`
**DV** (6)
  - `tb.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv`
  - `tb`:L5 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv`
  - `ac_range_check_env_pkg`:L9 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv`
  - `ac_range_check_test_pkg`:L10 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv`
  - `ac_range_check_base_test.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_base_test.sv`
  - `ac_range_check_test_pkg.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv`
**SVA** (2)
  - `ac_range_check_bind.sv`:L1 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv`
  - `ac_range_check_bind`:L5 — `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv`

## Neighbor Components

- `rv_plic` (6 refs; instantiates×6)
- `aes` (5 refs; instantiates×5)
- `otbn` (5 refs; instantiates×5)
- `prim` (4 refs; instantiates×4)
- `flash_ctrl` (3 refs; instantiates×3)
- `mbx` (3 refs; instantiates×3)
- `pwrmgr` (3 refs; instantiates×3)
- `lowrisc_ibex` (2 refs; instantiates×1, imports_from×1)
- `dma` (1 refs; instantiates×1)
- `soc_dbg_ctrl` (1 refs; instantiates×1)
- `spi_device` (1 refs; instantiates×1)
- `spi_host` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_base_test.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_base_test.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_test_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_bind` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_reg_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_top.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_reg_pkg.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_pkg.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_reg_top.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_top.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_reg_top` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check_reg_top.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_reg_top` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check_test_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `ac_range_check` | `opentitan\hw\top_darjeeling\rtl\autogen\top_darjeeling.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `prim_leading_one_ppc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `tlul_request_loopback` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_component_matches_code` | `component:ac_range_check` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `ac_range_check_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `ac_range_check_bind` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `ac_range_check_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv` |
| `spec_path_matches_code_path` | `ac_range_check.tpldesc.hjson` | `ac_range_check_test_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `ac_range_check_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `ac_range_check_bind` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `ac_range_check_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv` |
| `spec_path_matches_code_path` | `ac_range_check_testplan.hjson` | `ac_range_check_test_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ac_range_check_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ac_range_check_bind` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ac_range_check_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv` |
| `spec_path_matches_code_path` | `checklist.md` | `ac_range_check_test_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `ac_range_check_bind.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `ac_range_check_bind` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\sva\ac_range_check_bind.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `tb.sv` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `tb` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `ac_range_check_env_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tests\ac_range_check_test_pkg.sv` |
| `spec_path_matches_code_path` | `theory_of_operation.md` | `ac_range_check_test_pkg` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\dv\tb\tb.sv` |
| `spec_path_matches_code_path` | `top_darjeeling.gen.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `top_darjeeling.gen.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `top_darjeeling.secrets.testing.gen.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `top_darjeeling.secrets.testing.gen.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `chip_cfg.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `chip_cfg.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `chip_conn_testplan.hjson` | `prim_flop_en` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |
| `spec_path_matches_code_path` | `chip_conn_testplan.hjson` | `prim_onehot_enc` | `opentitan\hw\top_darjeeling\ip_autogen\ac_range_check\rtl\ac_range_check.sv` |

## Retrieval Guidance

- For code-only queries mentioning `ac_range_check`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `ac_range_check`.
