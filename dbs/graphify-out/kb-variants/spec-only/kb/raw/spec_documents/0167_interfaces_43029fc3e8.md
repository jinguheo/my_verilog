# Spec Document: opentitan/hw/ip/adc_ctrl/doc/interfaces.md

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\ip\adc_ctrl\doc\interfaces.md`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\ip\adc_ctrl\doc\interfaces.md`
- Original extension: `.md`
- Original bytes: 1871

## Content

# Hardware Interfaces

<!-- BEGIN CMDGEN util/regtool.py --interfaces ./hw/ip/adc_ctrl/data/adc_ctrl.hjson -->
Referring to the [Comportable guideline for peripheral device functionality](https://opentitan.org/book/doc/contributing/hw/comportability), the module **`adc_ctrl`** has the following hardware interfaces defined
- Primary Clock: **`clk_i`**
- Other Clocks: **`clk_aon_i`**
- Bus Device Interfaces (TL-UL): **`tl`**
- Bus Host Interfaces (TL-UL): *none*
- Peripheral Pins for Chip IO: *none*

## [Inter-Module Signals](https://opentitan.org/book/doc/contributing/hw/comportability/index.html#inter-signal-handling)

| Port Name   | Package::Struct   | Type    | Act   |   Width | Description   |
|:------------|:------------------|:--------|:------|--------:|:--------------|
| adc         | ast_pkg::adc_ast  | req_rsp | req   |       1 |               |
| wkup_req    | logic             | uni     | req   |       1 |               |
| tl          | tlul_pkg::tl      | req_rsp | rsp   |       1 |               |

## Interrupts

| Interrupt Name   | Type   | Description                                 |
|:-----------------|:-------|:--------------------------------------------|
| match_pending    | Status | ADC match or measurement event has occurred |

## Security Alerts

| Alert Name   | Description                                                                       |
|:-------------|:----------------------------------------------------------------------------------|
| fatal_fault  | This fatal alert is triggered when a fatal TL-UL bus integrity fault is detected. |

## Security Countermeasures

| Countermeasure ID      | Description                      |
|:-----------------------|:---------------------------------|
| ADC_CTRL.BUS.INTEGRITY | End-to-end bus integrity scheme. |


<!-- END CMDGEN -->
