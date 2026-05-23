# Spec Document: opentitan/hw/top_earlgrey/ip/sensor_ctrl/doc/programmers_guide.md

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_earlgrey\ip\sensor_ctrl\doc\programmers_guide.md`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\hw\top_earlgrey\ip\sensor_ctrl\doc\programmers_guide.md`
- Original extension: `.md`
- Original bytes: 499

## Content

# Programmer's Guide

Each available alert has a corresponding fatality configuration.
If an alert event is set to 1 in [`FATAL_ALERT_EN`](registers.md#fatal_alert_en), `sensor control` treats it as a fatal event instead of a recoverable event.
Fatal events are not acknowledged, and continuously send alert events in the system until some kind of escalation is seen.

## Device Interface Functions (DIFs)

- [Device Interface Functions](../../../../../sw/device/lib/dif/dif_sensor_ctrl.h)
