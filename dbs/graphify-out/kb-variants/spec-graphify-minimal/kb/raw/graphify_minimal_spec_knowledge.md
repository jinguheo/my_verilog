# Graphify Minimal Spec Knowledge

This is a single-file, low-token OpenKB input generated from the spec-only Graphify graph.
It is intentionally compact: use it as a curated bridge, not as a replacement for raw source truth.

## Source Graph
- Source graph: `D:\MyWork\verilog\dbs\graphify-out\spec-only-graphify\graph.json`
- Nodes: 8196
- Links: 30054
- Export strategy: top graph entities only, preserving source anchors and Graphify ids.

## Top Components
### Component: checklist
- Graphify id: `component_checklist`
- Community: 0
- Evidence sections: ADC CTRL Checklist [opentitan/hw/ip/adc_ctrl/doc/checklist.md:L1]; Design Checklist [opentitan/hw/ip/adc_ctrl/doc/checklist.md:L11]; D1 [opentitan/hw/ip/adc_ctrl/doc/checklist.md:L13]; D2 [opentitan/hw/ip/adc_ctrl/doc/checklist.md:L37]; ... 713 more
- Evidence documents: verification_stages.rst [ibex/doc/03_reference/verification_stages.rst:L1]; README.md [opentitan/doc/contributing/dv/methodology/README.md:L1]; setup_dv.md [opentitan/doc/getting_started/setup_dv.md:L1]; ... 136 more

### Component: readme
- Graphify id: `component_readme`
- Community: 1
- Evidence sections: OpenTitan Continuous Integration [opentitan/doc/contributing/ci/README.md:L1]; How to report CI problems [opentitan/doc/contributing/ci/README.md:L9]; Overview [opentitan/doc/contributing/ci/README.md:L15]; Test descriptions [opentitan/doc/contributing/ci/README.md:L37]; ... 482 more
- Evidence documents: examples.rst [ibex/doc/02_user/examples.rst:L1]; prim_keccak.md [ibex/vendor/lowrisc_ip/ip/prim/doc/prim_keccak.md:L1]; design_doc.md [ibex/vendor/lowrisc_ip/util/dvsim/doc/design_doc.md:L1]; ... 265 more

### Component: theory_of_operation
- Graphify id: `component_theory_of_operation`
- Community: 15
- Evidence sections: Theory of Operation [opentitan/hw/ip/adc_ctrl/doc/theory_of_operation.md:L1]; Block Diagram [opentitan/hw/ip/adc_ctrl/doc/theory_of_operation.md:L5]; Signals [opentitan/hw/ip/adc_ctrl/doc/theory_of_operation.md:L9]; Design Details [opentitan/hw/ip/adc_ctrl/doc/theory_of_operation.md:L19]; ... 567 more
- Evidence documents: example_ip_block.md [opentitan/doc/contributing/doc/example_ip_block.md:L1]; theory_of_operation.md [opentitan/hw/ip/adc_ctrl/doc/theory_of_operation.md:L1]; theory_of_operation.md [opentitan/hw/ip/aes/doc/theory_of_operation.md:L1]; ... 91 more

### Component: opentitan
- Graphify id: `component_opentitan`
- Community: 1
- Evidence sections: ! OpenTitan logo ../images/otlogo.png About OpenTitan [opentitan/doc/sections/opentitan.md:L2]
- Evidence documents: verification_overview.rst [ibex/doc/01_overview/verification_overview.rst:L1]; configuration.rst [ibex/doc/02_user/configuration.rst:L1]; getting_started.rst [ibex/doc/02_user/getting_started.rst:L1]; ... 649 more

### Component: lowrisc
- Graphify id: `component_lowrisc`
- Community: 3
- Evidence sections: lowRISC CIC [opentitan/doc/project_governance/lowRISC.md:L1]
- Evidence documents: licensing.rst [ibex/doc/01_overview/licensing.rst:L1]; verification_overview.rst [ibex/doc/01_overview/verification_overview.rst:L1]; examples.rst [ibex/doc/02_user/examples.rst:L1]; ... 504 more

### Component: programmers_guide
- Graphify id: `component_programmers_guide`
- Community: 7
- Evidence sections: Programmer's Guide [opentitan/hw/ip/adc_ctrl/doc/programmers_guide.md:L1]; Initialization [opentitan/hw/ip/adc_ctrl/doc/programmers_guide.md:L3]; Running in normal mode [opentitan/hw/ip/adc_ctrl/doc/programmers_guide.md:L16]; Running with the rest of the chip in sleep [opentitan/hw/ip/adc_ctrl/doc/programmers_guide.md:L25]; ... 407 more
- Evidence documents: example_ip_block.md [opentitan/doc/contributing/doc/example_ip_block.md:L1]; programmers_guide.md [opentitan/hw/ip/adc_ctrl/doc/programmers_guide.md:L1]; programmers_guide.md [opentitan/hw/ip/aes/doc/programmers_guide.md:L1]; ... 82 more

### Component: interfaces
- Graphify id: `component_interfaces`
- Community: 2
- Evidence sections: Hardware Interfaces [opentitan/hw/ip/adc_ctrl/doc/interfaces.md:L1]; Inter-Module Signals [opentitan/hw/ip/adc_ctrl/doc/interfaces.md:L11]; Interrupts [opentitan/hw/ip/adc_ctrl/doc/interfaces.md:L19]; Security Alerts [opentitan/hw/ip/adc_ctrl/doc/interfaces.md:L25]; ... 298 more
- Evidence documents: integration.rst [ibex/doc/02_user/integration.rst:L1]; instruction_decode_execute.rst [ibex/doc/03_reference/instruction_decode_execute.rst:L1]; instruction_fetch.rst [ibex/doc/03_reference/instruction_fetch.rst:L1]; ... 187 more

### Component: security
- Graphify id: `component_security`
- Community: 2
- Evidence sections: Security Features [ibex/doc/03_reference/security.rst:L3]; Outputs [ibex/doc/03_reference/security.rst:L9]; Data Independent Timing [ibex/doc/03_reference/security.rst:L17]; Dummy Instruction Insertion [ibex/doc/03_reference/security.rst:L41]; ... 26 more
- Evidence documents: integration.rst [ibex/doc/02_user/integration.rst:L1]; coverage_plan.rst [ibex/doc/03_reference/coverage_plan.rst:L1]; cs_registers.rst [ibex/doc/03_reference/cs_registers.rst:L1]; ... 359 more

### Component: software
- Graphify id: `component_software`
- Community: 8
- Evidence sections: ! OpenTitan logo ../images/otlogo.png OpenTitan Software [opentitan/doc/sections/software.md:L2]
- Evidence documents: index.rst [ibex/doc/02_user/index.rst:L1]; cs_registers.rst [ibex/doc/03_reference/cs_registers.rst:L1]; debug.rst [ibex/doc/03_reference/debug.rst:L1]; ... 362 more

### Component: pwrmgr
- Graphify id: `component_pwrmgr`
- Community: 7
- Evidence sections: template param list [opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson:L5]; desc [opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson:L8]; width [opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson:L31]; peripheral [opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson:L43]; ... 255 more
- Evidence documents: lc_ctrl_testplan.hjson [opentitan/hw/ip/lc_ctrl/data/lc_ctrl_testplan.hjson:L1]; interfaces.md [opentitan/hw/ip/lc_ctrl/doc/interfaces.md:L1]; rom_ctrl.hjson [opentitan/hw/ip/rom_ctrl/data/rom_ctrl.hjson:L1]; ... 93 more

### Component: rstmgr
- Graphify id: `component_rstmgr`
- Community: 4
- Evidence sections: resets [opentitan/hw/ip_templates/rstmgr/data/rstmgr.cfg.example.hjson:L32]; template param list [opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson:L5]; desc [opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson:L8]; peripheral [opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson:L33]; ... 246 more
- Evidence documents: README.md [opentitan/doc/project_governance/checklist/README.md:L1]; sysrst_ctrl.hjson [opentitan/hw/ip/sysrst_ctrl/data/sysrst_ctrl.hjson:L1]; programmers_guide.md [opentitan/hw/ip_templates/alert_handler/doc/programmers_guide.md:L1]; ... 93 more

### Component: pinmux
- Graphify id: `component_pinmux`
- Community: 10
- Evidence sections: template param list [opentitan/hw/ip_templates/pinmux/data/pinmux.tpldesc.hjson:L5]; desc [opentitan/hw/ip_templates/pinmux/data/pinmux.tpldesc.hjson:L8]; import testplans [opentitan/hw/ip_templates/pinmux/data/pinmux_fpv_testplan.hjson:L6]; testpoints [opentitan/hw/ip_templates/pinmux/data/pinmux_fpv_testplan.hjson:L7]; ... 257 more
- Evidence documents: README.md [opentitan/doc/contributing/hw/comportability/README.md:L1]; design.md [opentitan/doc/contributing/hw/design.md:L1]; device_interface_functions.md [opentitan/doc/contributing/sw/device_interface_functions.md:L1]; ... 80 more

### Component: ipconfig
- Graphify id: `component_ipconfig`
- Community: 4
- Evidence sections: instance name [opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson:L5]; param values [opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson:L6]; num ranges [opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson:L8]; nr role bits [opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson:L9]; ... 277 more
- Evidence documents: create_top.md [opentitan/hw/top/doc/create_top.md:L1]; top_desc.md [opentitan/hw/top/doc/top_desc.md:L1]; top_darjeeling_ac_range_check.ipconfig.hjson [opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson:L1]; ... 29 more

### Component: rv_core_ibex
- Graphify id: `component_rv_core_ibex`
- Community: 5
- Evidence sections: template param list [opentitan/hw/ip_templates/rv_core_ibex/data/rv_core_ibex.tpldesc.hjson:L5]; desc [opentitan/hw/ip_templates/rv_core_ibex/data/rv_core_ibex.tpldesc.hjson:L8]; dtgen [opentitan/hw/ip_templates/rv_core_ibex/data/rv_core_ibex.tpldesc.hjson:L17]; Boot, ROM execution and Patching [opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md:L1]; ... 246 more
- Evidence documents: verification_stages.rst [ibex/doc/03_reference/verification_stages.rst:L1]; cores.md [opentitan/hw/doc/cores.md:L1]; README.md [opentitan/hw/ip/aes/README.md:L1]; ... 58 more

### Component: clkmgr
- Graphify id: `component_clkmgr`
- Community: 12
- Evidence sections: template param list [opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson:L5]; desc [opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson:L8]; aon [opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson:L25]; freq [opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson:L26]; ... 224 more
- Evidence documents: README.md [opentitan/doc/contributing/dv/methodology/README.md:L1]; theory_of_operation.md [opentitan/hw/ip/lc_ctrl/doc/theory_of_operation.md:L1]; ac_range_check.tpldesc.hjson [opentitan/hw/ip_templates/ac_range_check/data/ac_range_check.tpldesc.hjson:L1]; ... 72 more

### Component: system
- Graphify id: `component_system`
- Community: 11
- Evidence sections: Overview [opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md:L1]; Features [opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md:L5]; Description [opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md:L15]; Compatibility [opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md:L19]; ... 6 more
- Evidence documents: examples.rst [ibex/doc/02_user/examples.rst:L1]; getting_started.rst [ibex/doc/02_user/getting_started.rst:L1]; integration.rst [ibex/doc/02_user/integration.rst:L1]; ... 271 more

### Component: gpio
- Graphify id: `component_gpio`
- Community: 15
- Evidence sections: template param list [opentitan/hw/ip_templates/gpio/data/gpio.tpldesc.hjson:L5]; desc [opentitan/hw/ip_templates/gpio/data/gpio.tpldesc.hjson:L8]; dtgen [opentitan/hw/ip_templates/gpio/data/gpio.tpldesc.hjson:L29]; testpoints [opentitan/hw/ip_templates/gpio/data/gpio_sec_cm_testplan.hjson:L25]; ... 207 more
- Evidence documents: README.md [opentitan/doc/contributing/hw/comportability/README.md:L1]; setup_fpga.md [opentitan/doc/getting_started/setup_fpga.md:L1]; setup_verilator.md [opentitan/doc/getting_started/setup_verilator.md:L1]; ... 67 more

### Component: rv_plic
- Graphify id: `component_rv_plic`
- Community: 9
- Evidence sections: template param list [opentitan/hw/ip_templates/rv_plic/data/rv_plic.tpldesc.hjson:L5]; desc [opentitan/hw/ip_templates/rv_plic/data/rv_plic.tpldesc.hjson:L8]; dtgen [opentitan/hw/ip_templates/rv_plic/data/rv_plic.tpldesc.hjson:L23]; testpoints [opentitan/hw/ip_templates/rv_plic/data/rv_plic_sec_cm_testplan.hjson:L25]; ... 233 more
- Evidence documents: README.md [opentitan/doc/contributing/hw/comportability/README.md:L1]; rv_plic.tpldesc.hjson [opentitan/hw/ip_templates/rv_plic/data/rv_plic.tpldesc.hjson:L1]; rv_plic_sec_cm_testplan.hjson [opentitan/hw/ip_templates/rv_plic/data/rv_plic_sec_cm_testplan.hjson:L1]; ... 38 more

### Component: otp_ctrl
- Graphify id: `component_otp_ctrl`
- Community: 8
- Evidence sections: template param list [opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl.tpldesc.hjson:L5]; desc [opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl.tpldesc.hjson:L8]; testpoints [opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson:L25]; desc [opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl_sec_cm_testplan.hjson:L28]; ... 196 more
- Evidence documents: lc_ctrl_testplan.hjson [opentitan/hw/ip/lc_ctrl/data/lc_ctrl_testplan.hjson:L1]; interfaces.md [opentitan/hw/ip/lc_ctrl/doc/interfaces.md:L1]; theory_of_operation.md [opentitan/hw/ip/lc_ctrl/doc/theory_of_operation.md:L1]; ... 61 more

### Component: flash_ctrl
- Graphify id: `component_flash_ctrl`
- Community: 16
- Evidence sections: template param list [opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl.tpldesc.hjson:L5]; desc [opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl.tpldesc.hjson:L8]; testpoints [opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson:L25]; desc [opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl_sec_cm_testplan.hjson:L28]; ... 192 more
- Evidence documents: testplanner.md [ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md:L1]; directory_structure.md [opentitan/doc/contributing/directory_structure.md:L1]; README.md [opentitan/doc/contributing/hw/comportability/README.md:L1]; ... 62 more

### Component: debug
- Graphify id: `component_debug`
- Community: 11
- Evidence sections: Debug Support [ibex/doc/03_reference/debug.rst:L3]; Interface [ibex/doc/03_reference/debug.rst:L18]; Parameters [ibex/doc/03_reference/debug.rst:L29]; Core Debug Registers [ibex/doc/03_reference/debug.rst:L48]; ... 14 more
- Evidence documents: compliance.rst [ibex/doc/01_overview/compliance.rst:L1]; verification_overview.rst [ibex/doc/01_overview/verification_overview.rst:L1]; examples.rst [ibex/doc/02_user/examples.rst:L1]; ... 223 more

### Component: verification
- Graphify id: `component_verification`
- Community: 0
- Evidence sections: Verification [ibex/doc/03_reference/verification.rst:L3]; Ibex Core [ibex/doc/03_reference/verification.rst:L10]; Overview [ibex/doc/03_reference/verification.rst:L13]; Testbench Architecture [ibex/doc/03_reference/verification.rst:L30]; ... 16 more
- Evidence documents: verification_overview.rst [ibex/doc/01_overview/verification_overview.rst:L1]; configuration.rst [ibex/doc/02_user/configuration.rst:L1]; getting_started.rst [ibex/doc/02_user/getting_started.rst:L1]; ... 207 more

### Component: alert_handler
- Graphify id: `component_alert_handler`
- Community: 4
- Evidence sections: template param list [opentitan/hw/ip_templates/alert_handler/data/alert_handler.tpldesc.hjson:L5]; desc [opentitan/hw/ip_templates/alert_handler/data/alert_handler.tpldesc.hjson:L8]; testpoints [opentitan/hw/ip_templates/alert_handler/data/alert_handler_sec_cm_testplan.hjson:L25]; desc [opentitan/hw/ip_templates/alert_handler/data/alert_handler_sec_cm_testplan.hjson:L28]; ... 143 more
- Evidence documents: README.md [opentitan/doc/contributing/hw/comportability/README.md:L1]; README.md [opentitan/doc/security/README.md:L1]; alert_handler.tpldesc.hjson [opentitan/hw/ip_templates/alert_handler/data/alert_handler.tpldesc.hjson:L1]; ... 66 more

### Component: lc_ctrl
- Graphify id: `component_lc_ctrl`
- Community: 8
- Evidence sections: human name [opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson:L6]; one line desc [opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson:L7]; one paragraph desc [opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson:L8]; cip id [opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson:L13]; ... 80 more
- Evidence documents: README.md [opentitan/doc/security/specs/device_life_cycle/README.md:L1]; interfaces.md [opentitan/hw/ip/aes/doc/interfaces.md:L1]; keymgr.hjson [opentitan/hw/ip/keymgr/data/keymgr.hjson:L1]; ... 125 more

### Component: testing
- Graphify id: `component_testing`
- Community: 3
- Evidence sections: seed [opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.secrets.testing.gen.hjson:L10]; topgen seed [opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.secrets.testing.gen.hjson:L12]; seed mode [opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.secrets.testing.gen.hjson:L14]; otp img seed [opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.secrets.testing.gen.hjson:L17]; ... 33 more
- Evidence documents: system_requirements.rst [ibex/doc/02_user/system_requirements.rst:L1]; verification.rst [ibex/doc/03_reference/verification.rst:L1]; verification_stages.rst [ibex/doc/03_reference/verification_stages.rst:L1]; ... 170 more

### Component: gen
- Graphify id: `component_gen`
- Community: 3
- Evidence sections: datawidth [opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.gen.hjson:L12]; racl config [opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.gen.hjson:L13]; power [opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.gen.hjson:L14]; domains [opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.gen.hjson:L16]; ... 136 more
- Evidence documents: verification.rst [ibex/doc/03_reference/verification.rst:L1]; adding_python_depedencies.md [opentitan/doc/contributing/sw/adding_python_depedencies.md:L1]; README.md [opentitan/doc/project_governance/checklist/README.md:L1]; ... 66 more

### Component: rom
- Graphify id: `component_rom`
- Community: 5
- Evidence sections: Boot, ROM execution and Patching [opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md:L1]; Glossary [opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md:L3]; Scope [opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md:L11]; Overview [opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md:L16]; ... 36 more
- Evidence documents: verification.rst [ibex/doc/03_reference/verification.rst:L1]; verification_stages.rst [ibex/doc/03_reference/verification_stages.rst:L1]; testplanner.md [ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md:L1]; ... 152 more

### Component: prim
- Graphify id: `component_prim`
- Community: 13
- Evidence sections: Primitive Component: Flash Wrapper [ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md:L1]; Overview [ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md:L3]; Parameters [ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md:L9]; Signal Interfaces [ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md:L24]; ... 122 more
- Evidence documents: icache.rst [ibex/doc/03_reference/icache.rst:L1]; load_store_unit.rst [ibex/doc/03_reference/load_store_unit.rst:L1]; prim_flash.md [ibex/vendor/lowrisc_ip/ip/prim/doc/prim_flash.md:L1]; ... 61 more

### Component: otbn
- Graphify id: `component_otbn`
- Community: 17
- Evidence sections: human name [opentitan/hw/ip/otbn/data/otbn.hjson:L6]; one line desc [opentitan/hw/ip/otbn/data/otbn.hjson:L7]; one paragraph desc [opentitan/hw/ip/otbn/data/otbn.hjson:L8]; cip id [opentitan/hw/ip/otbn/data/otbn.hjson:L19]; ... 108 more
- Evidence documents: otbn_style_guide.md [opentitan/doc/contributing/style_guides/otbn_style_guide.md:L1]; README.md [opentitan/doc/contributing/style_guides/README.md:L1]; otbn_sw.md [opentitan/doc/contributing/sw/otbn_sw.md:L1]; ... 72 more

### Component: specification
- Graphify id: `component_specification`
- Community: 9
- Evidence sections: ! OpenTitan logo ../images/otlogo.png OpenTitan Specification [opentitan/doc/sections/specification.md:L2]
- Evidence documents: compliance.rst [ibex/doc/01_overview/compliance.rst:L1]; integration.rst [ibex/doc/02_user/integration.rst:L1]; coverage_plan.rst [ibex/doc/03_reference/coverage_plan.rst:L1]; ... 181 more

## Topics
### Topic: memory
- Graphify id: `topic_memory`
- Community: 5
- Mentioning sections: Memory Access Checking and Bus Errors [ibex/doc/03_reference/cosim.rst:L145]; icache.rst [ibex/doc/03_reference/icache.rst:L1]; RAM Arrangement [ibex/doc/03_reference/icache.rst:L76]; instruction_fetch.rst [ibex/doc/03_reference/instruction_fetch.rst:L1]; Instruction-Side Memory Interface [ibex/doc/03_reference/instruction_fetch.rst:L41]; load_store_unit.rst [ibex/doc/03_reference/load_store_unit.rst:L1]; ... 260 more

### Topic: alert
- Graphify id: `topic_alert`
- Community: 2
- Mentioning sections: Recommendation 5 : Alerts [opentitan/doc/security/implementation_guidelines/hardware/README.md:L246]; interfaces.md [opentitan/hw/ip/adc_ctrl/doc/interfaces.md:L1]; Security Alerts [opentitan/hw/ip/adc_ctrl/doc/interfaces.md:L25]; registers.md [opentitan/hw/ip/adc_ctrl/doc/registers.md:L1]; ALERT TEST [opentitan/hw/ip/adc_ctrl/doc/registers.md:L92]; interfaces.md [opentitan/hw/ip/aes/doc/interfaces.md:L1]; ... 256 more

### Topic: security
- Graphify id: `topic_security`
- Community: 2
- Mentioning sections: Security Features [ibex/doc/03_reference/security.rst:L3]; README.md [opentitan/doc/contributing/dv/sec_cm_dv_framework/README.md:L1]; Security Countermeasure Verification Framework [opentitan/doc/contributing/dv/sec_cm_dv_framework/README.md:L1]; Standardized Design Countermeasure Primitive [opentitan/doc/contributing/dv/sec_cm_dv_framework/README.md:L11]; Verification Framework For The Standardized Design Countermeasures [opentitan/doc/contributing/dv/sec_cm_dv_framework/README.md:L98]; README.md [opentitan/doc/contributing/README.md:L1]; ... 240 more

### Topic: testplan
- Graphify id: `topic_testplan`
- Community: 0
- Mentioning sections: Verification Overview [ibex/doc/01_overview/verification_overview.rst:L1]; Verification Status [ibex/doc/01_overview/verification_overview.rst:L9]; rvfi.rst [ibex/doc/03_reference/rvfi.rst:L1]; Formal Verification [ibex/doc/03_reference/rvfi.rst:L11]; verification.rst [ibex/doc/03_reference/verification.rst:L1]; Verification [ibex/doc/03_reference/verification.rst:L3]; ... 207 more

### Topic: clock
- Graphify id: `topic_clock`
- Community: 3
- Mentioning sections: clocking [opentitan/hw/ip/dma/data/dma.hjson:L21]; mbx.hjson [opentitan/hw/ip/mbx/data/mbx.hjson:L1]; clocking [opentitan/hw/ip/mbx/data/mbx.hjson:L20]; README.md [opentitan/hw/ip/spi_device/README.md:L1]; Clocking Requirements [opentitan/hw/ip/spi_device/README.md:L89]; theory_of_operation.md [opentitan/hw/ip/spi_host/doc/theory_of_operation.md:L1]; ... 198 more

### Topic: interrupt
- Graphify id: `topic_interrupt`
- Community: 2
- Mentioning sections: Interrupts and Debug Requests [ibex/doc/03_reference/cosim.rst:L126]; cs_registers.rst [ibex/doc/03_reference/cs_registers.rst:L1]; Machine Interrupt Enable Register mie [ibex/doc/03_reference/cs_registers.rst:L149]; Machine Interrupt Pending Register mip [ibex/doc/03_reference/cs_registers.rst:L238]; exception_interrupts.rst [ibex/doc/03_reference/exception_interrupts.rst:L1]; Exceptions and Interrupts [ibex/doc/03_reference/exception_interrupts.rst:L3]; ... 162 more

### Topic: power
- Graphify id: `topic_power`
- Community: 7
- Mentioning sections: Running with the rest of the chip in sleep [opentitan/hw/ip/adc_ctrl/doc/programmers_guide.md:L25]; programmers_guide.md [opentitan/hw/ip/aon_timer/doc/programmers_guide.md:L1]; Wakeup count and threshold access [opentitan/hw/ip/aon_timer/doc/programmers_guide.md:L15]; README.md [opentitan/hw/ip/aon_timer/README.md:L1]; Wakeup timer [opentitan/hw/ip/aon_timer/README.md:L27]; interfaces.md [opentitan/hw/ip/lc_ctrl/doc/interfaces.md:L1]; ... 110 more

### Topic: crypto
- Graphify id: `topic_crypto`
- Community: 6
- Mentioning sections: AES [opentitan/doc/glossary.md:L7]; cryptolib_api.md [opentitan/doc/security/cryptolib/cryptolib_api.md:L1]; AES data structures [opentitan/doc/security/cryptolib/cryptolib_api.md:L126]; security.md [opentitan/doc/security/cryptolib/security.md:L1]; AES [opentitan/doc/security/cryptolib/security.md:L35]; HMAC [opentitan/doc/security/cryptolib/security.md:L61]; ... 65 more

### Topic: debug
- Graphify id: `topic_debug`
- Community: 11
- Mentioning sections: Interrupts and Debug Requests [ibex/doc/03_reference/cosim.rst:L126]; debug.rst [ibex/doc/03_reference/debug.rst:L1]; Debug Support [ibex/doc/03_reference/debug.rst:L3]; Core Debug Registers [ibex/doc/03_reference/debug.rst:L48]; pmp.rst [ibex/doc/03_reference/pmp.rst:L1]; Debug Mode [ibex/doc/03_reference/pmp.rst:L62]; ... 58 more

### Topic: entropy
- Graphify id: `topic_entropy`
- Community: 14
- Mentioning sections: Entropy source entropy source [opentitan/doc/security/README.md:L65]; CSRNG csrng [opentitan/doc/security/README.md:L71]; csrng.hjson [opentitan/hw/ip/csrng/data/csrng.hjson:L1]; csrng_sec_cm_testplan.hjson [opentitan/hw/ip/csrng/data/csrng_sec_cm_testplan.hjson:L1]; csrng_testplan.hjson [opentitan/hw/ip/csrng/data/csrng_testplan.hjson:L1]; checklist.md [opentitan/hw/ip/csrng/doc/checklist.md:L1]; ... 50 more

### Topic: reset
- Graphify id: `topic_reset`
- Community: 3
- Mentioning sections: CTRL . CMD FIFO RST [opentitan/hw/ip/edn/doc/registers.md:L137]; registers.md [opentitan/hw/ip/spi_host/doc/registers.md:L1]; CONTROL . SW RST [opentitan/hw/ip/spi_host/doc/registers.md:L119]; registers.md [opentitan/hw/ip/sysrst_ctrl/doc/registers.md:L1]; EC RST CTL [opentitan/hw/ip/sysrst_ctrl/doc/registers.md:L137]; rstmgr.cfg.example.hjson [opentitan/hw/ip_templates/rstmgr/data/rstmgr.cfg.example.hjson:L1]; ... 43 more

### Topic: fifo
- Graphify id: `topic_fifo`
- Community: 3
- Mentioning sections: Primitive Component: Packer FIFO [ibex/vendor/lowrisc_ip/ip/prim/doc/prim_packer_fifo.md:L1]; registers.md [opentitan/hw/ip/edn/doc/registers.md:L1]; CTRL . CMD FIFO RST [opentitan/hw/ip/edn/doc/registers.md:L137]; programmers_guide.md [opentitan/hw/ip/hmac/doc/programmers_guide.md:L1]; FIFO Depth and Empty status [opentitan/hw/ip/hmac/doc/programmers_guide.md:L130]; registers.md [opentitan/hw/ip/hmac/doc/registers.md:L1]; ... 25 more

### Topic: registers
- Graphify id: `topic_registers`
- Community: 17
- Mentioning sections: Identification CSRs [ibex/doc/02_user/integration.rst:L17]; instruction_decode_execute.rst [ibex/doc/03_reference/instruction_decode_execute.rst:L1]; Control and Status Register Block CSR [ibex/doc/03_reference/instruction_decode_execute.rst:L156]; security.rst [ibex/doc/03_reference/security.rst:L1]; Shadow CSRs [ibex/doc/03_reference/security.rst:L128]; asm_coding_style.md [opentitan/doc/contributing/style_guides/asm_coding_style.md:L1]; ... 21 more

### Topic: lifecycle
- Graphify id: `topic_lifecycle`
- Community: 8
- Mentioning sections: Device Lifecycle and Personalization Stages [opentitan/doc/security/specs/device_provisioning/README.md:L49]; lc_ctrl.hjson [opentitan/hw/ip/lc_ctrl/data/lc_ctrl.hjson:L1]; lc_ctrl_sec_cm_testplan.hjson [opentitan/hw/ip/lc_ctrl/data/lc_ctrl_sec_cm_testplan.hjson:L1]; lc_ctrl_state.hjson [opentitan/hw/ip/lc_ctrl/data/lc_ctrl_state.hjson:L1]; lc_ctrl_testplan.hjson [opentitan/hw/ip/lc_ctrl/data/lc_ctrl_testplan.hjson:L1]; checklist.md [opentitan/hw/ip/lc_ctrl/doc/checklist.md:L1]; ... 14 more

### Topic: bus
- Graphify id: `topic_bus`
- Community: 9
- Mentioning sections: tlul_testplan.hjson [opentitan/hw/ip/tlul/data/tlul_testplan.hjson:L1]; README.md [opentitan/hw/ip/tlul/doc/dv/README.md:L1]; TLUL XBAR DV document [opentitan/hw/ip/tlul/doc/dv/README.md:L1]; TlulProtocolChecker.md [opentitan/hw/ip/tlul/doc/TlulProtocolChecker.md:L1]; README.md [opentitan/hw/ip/tlul/README.md:L1]; README.md [opentitan/hw/ip_templates/rv_plic/doc/dv/README.md:L1]; ... 7 more

### Topic: coverage
- Graphify id: `topic_coverage`
- Community: 17
- Mentioning sections: Coverage Plan [ibex/doc/03_reference/coverage_plan.rst:L3]; Coverage Implementation [ibex/doc/03_reference/coverage_plan.rst:L21]; device_interface_functions.md [opentitan/doc/contributing/sw/device_interface_functions.md:L1]; Coverage Requirements [opentitan/doc/contributing/sw/device_interface_functions.md:L49]; fcov.md [opentitan/hw/ip/otbn/dv/doc/fcov.md:L1]; OTBN functional coverage [opentitan/hw/ip/otbn/dv/doc/fcov.md:L1]; ... 4 more

## High-Value Source Documents
### Document: theory_of_operation.md
- Graphify id: `doc_opentitan_hw_ip_lc_ctrl_doc_theory_of_operation_md`
- Source file: `opentitan/hw/ip/lc_ctrl/doc/theory_of_operation.md`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\ip\lc_ctrl\doc\theory_of_operation.md`
- Community: 8
- Sections: Theory of Operation; Power Up Sequence; Normal Operation; Unconditional Transitions; Conditional Transitions; Transition Counter Limits; Token Hashing Mechanism; Post Transition Handling; ... 2 more

### Document: top_darjeeling.gen.hjson
- Graphify id: `doc_opentitan_hw_top_darjeeling_data_autogen_top_darjeeling_gen_hjson`
- Source file: `opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.gen.hjson`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_darjeeling\data\autogen\top_darjeeling.gen.hjson`
- Community: 3
- Sections: datawidth; racl config; power; domains; wait for external reset; halt ibex via rom ctrl; unmanaged clocks; clocks; ... 2 more

### Document: top_darjeeling.hjson
- Graphify id: `doc_opentitan_hw_top_darjeeling_data_top_darjeeling_hjson`
- Source file: `opentitan/hw/top_darjeeling/data/top_darjeeling.hjson`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_darjeeling\data\top_darjeeling.hjson`
- Community: 3
- Sections: datawidth; racl config; power; domains; wait for external reset; halt ibex via rom ctrl; unmanaged clocks; clocks; ... 2 more

### Document: README.md
- Graphify id: `doc_opentitan_hw_top_earlgrey_doc_design_readme_md`
- Source file: `opentitan/hw/top_earlgrey/doc/design/README.md`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_earlgrey\doc\design\README.md`
- Community: 1
- Sections: OpenTitan Earl Grey Chip Specification; Theory of Operations; Design Details; Clocking and Reset; AST Clocking and Reset Relationship; System Reset Handling and Flash; Reset due to External Supply; Reset due to Internal Request; ... 2 more

### Document: chip_testplan.hjson
- Graphify id: `doc_opentitan_hw_top_darjeeling_data_chip_testplan_hjson`
- Source file: `opentitan/hw/top_darjeeling/data/chip_testplan.hjson`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_darjeeling\data\chip_testplan.hjson`
- Community: 6
- Sections: import testplans; testpoints; desc; stage; tests; tags; parameters; alert handler reg pkg; ... 2 more

### Document: xbar_main.gen.hjson
- Graphify id: `doc_opentitan_hw_top_darjeeling_ip_xbar_main_data_autogen_xbar_main_gen_hjson`
- Source file: `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_darjeeling\ip\xbar_main\data\autogen\xbar_main.gen.hjson`
- Community: 3
- Sections: clock srcs; clk main i; clk fixed i; clock group; reset connections; rst main ni; domain; rst fixed ni; ... 2 more

### Document: xbar_peri.gen.hjson
- Graphify id: `doc_opentitan_hw_top_darjeeling_ip_xbar_peri_data_autogen_xbar_peri_gen_hjson`
- Source file: `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_darjeeling\ip\xbar_peri\data\autogen\xbar_peri.gen.hjson`
- Community: 3
- Sections: clock srcs; clk peri i; clock group; reset connections; rst peri ni; domain; clock connections; connections; ... 2 more

### Document: top_earlgrey.gen.hjson
- Graphify id: `doc_opentitan_hw_top_earlgrey_data_autogen_top_earlgrey_gen_hjson`
- Source file: `opentitan/hw/top_earlgrey/data/autogen/top_earlgrey.gen.hjson`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_earlgrey\data\autogen\top_earlgrey.gen.hjson`
- Community: 3
- Sections: datawidth; power; domains; wait for external reset; unmanaged clocks; clocks; hier paths; ext; ... 2 more

### Document: top_earlgrey.hjson
- Graphify id: `doc_opentitan_hw_top_earlgrey_data_top_earlgrey_hjson`
- Source file: `opentitan/hw/top_earlgrey/data/top_earlgrey.hjson`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_earlgrey\data\top_earlgrey.hjson`
- Community: 3
- Sections: datawidth; power; domains; wait for external reset; unmanaged clocks; clocks; hier paths; ext; ... 2 more

### Document: xbar_main.gen.hjson
- Graphify id: `doc_opentitan_hw_top_earlgrey_ip_xbar_main_data_autogen_xbar_main_gen_hjson`
- Source file: `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_earlgrey\ip\xbar_main\data\autogen\xbar_main.gen.hjson`
- Community: 3
- Sections: clock srcs; clk main i; clk fixed i; clk usb i; clk spi host0 i; clk spi host1 i; clock group; reset connections; ... 2 more

### Document: xbar_peri.gen.hjson
- Graphify id: `doc_opentitan_hw_top_earlgrey_ip_xbar_peri_data_autogen_xbar_peri_gen_hjson`
- Source file: `opentitan/hw/top_earlgrey/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_earlgrey\ip\xbar_peri\data\autogen\xbar_peri.gen.hjson`
- Community: 3
- Sections: clock srcs; clk peri i; clock group; reset connections; rst peri ni; domain; clock connections; connections; ... 2 more

### Document: top_englishbreakfast.gen.hjson
- Graphify id: `doc_opentitan_hw_top_englishbreakfast_data_autogen_top_englishbreakfast_gen_hjson`
- Source file: `opentitan/hw/top_englishbreakfast/data/autogen/top_englishbreakfast.gen.hjson`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_englishbreakfast\data\autogen\top_englishbreakfast.gen.hjson`
- Community: 3
- Sections: datawidth; power; domains; wait for external reset; unmanaged clocks; clocks; hier paths; ext; ... 2 more

### Document: top_englishbreakfast.hjson
- Graphify id: `doc_opentitan_hw_top_englishbreakfast_data_top_englishbreakfast_hjson`
- Source file: `opentitan/hw/top_englishbreakfast/data/top_englishbreakfast.hjson`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\top_englishbreakfast\data\top_englishbreakfast.hjson`
- Community: 3
- Sections: datawidth; power; domains; wait for external reset; unmanaged clocks; clocks; hier paths; ext; ... 2 more

### Document: README.md
- Graphify id: `doc_opentitan_doc_contributing_dv_methodology_readme_md`
- Source file: `opentitan/doc/contributing/dv/methodology/README.md`
- Original source: `D:\MyWork\verilog\dbs\opentitan\doc\contributing\dv\methodology\README.md`
- Community: 1
- Sections: Design Verification Methodology within OpenTitan; Language and Tool Selection; Defining Verification Complete: Stages and Checklists; Documentation; Testplan; DV document; Regression Dashboard; Automation; ... 2 more

### Document: setup_fpga.md
- Graphify id: `doc_opentitan_doc_getting_started_setup_fpga_md`
- Source file: `opentitan/doc/getting_started/setup_fpga.md`
- Original source: `D:\MyWork\verilog\dbs\opentitan\doc\getting_started\setup_fpga.md`
- Community: 1
- Sections: FPGA Setup; Prerequisites; Obtain an FPGA bitstream; Download a Pre-built Bitstream; Using the @bitstreams repository; Build an FPGA bitstream; Splicing a different ROM or OTP into a Cached Bitstream; From Scratch; ... 2 more

### Document: glossary.md
- Graphify id: `doc_opentitan_doc_glossary_md`
- Source file: `opentitan/doc/glossary.md`
- Original source: `D:\MyWork\verilog\dbs\opentitan\doc\glossary.md`
- Community: 26
- Sections: Glossary; ADC; AES; Airgapped; AON; ASM; Attestation; Baud; ... 2 more

### Document: README.md
- Graphify id: `doc_opentitan_doc_project_governance_checklist_readme_md`
- Source file: `opentitan/doc/project_governance/checklist/README.md`
- Original source: `D:\MyWork\verilog\dbs\opentitan\doc\project_governance\checklist\README.md`
- Community: 1
- Sections: Signoff Checklist; D1; SPEC COMPLETE; CSR DEFINED; CLKRST CONNECTED; IP TOP; IP INSTANTIABLE; PHYSICAL MACROS DEFINED 80; ... 2 more

### Document: README.md
- Graphify id: `doc_opentitan_doc_security_readme_md`
- Source file: `opentitan/doc/security/README.md`
- Original source: `D:\MyWork\verilog\dbs\opentitan\doc\security\README.md`
- Community: 1
- Sections: Security; Overview; OpenTitan Security Model Specification security model; Logical Security Model logical security model; Secure Hardware Design Guidelines implementation guidelines; Functional Guarantees; Use Cases; Security Hardware Primitives; ... 2 more

### Document: otbn_intro.md
- Graphify id: `doc_opentitan_hw_ip_otbn_doc_otbn_intro_md`
- Source file: `opentitan/hw/ip/otbn/doc/otbn_intro.md`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\ip\otbn\doc\otbn_intro.md`
- Community: 17
- Sections: Introduction to OTBN; How OTBN executes programs; Security features; Instruction set highlights; Multiplying big numbers; Add/subtract modulo; Hardware loops; Concatenate-and-shift; ... 2 more

### Document: boot-rom-patching.md
- Graphify id: `doc_opentitan_hw_ip_templates_rv_core_ibex_doc_boot_rom_patching_md`
- Source file: `opentitan/hw/ip_templates/rv_core_ibex/doc/boot-rom-patching.md`
- Original source: `D:\MyWork\verilog\dbs\opentitan\hw\ip_templates\rv_core_ibex\doc\boot-rom-patching.md`
- Community: 5
- Sections: Boot, ROM execution and Patching; Glossary; Scope; Overview; Programming method; ROM Boot & Patching Building Blocks; OpenTitan base ROM first ROM partition; Second ROM partition; ... 2 more

## OpenKB Instructions
- Build concept pages from this compact graph-derived input.
- Preserve Graphify ids, exact component names, source paths, and source locations.
- If a question needs detailed wording, route back to the original source file rather than inventing details.
- Prefer component/topic/source anchors as late-binding keys for code KG integration.
