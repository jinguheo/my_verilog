# Graphify Ultra Minimal Spec Knowledge

Single-file OpenKB input compressed from Graphify spec-only graph. Use this as a low-cost curator seed.

## Graph
- Nodes: 8196
- Links: 30054
- Keep Graphify ids and source anchors as late-binding keys for code/spec integration.

## Components
### security
- id: `component_security`, community: 2
- evidence: Security Features <ibex/doc/03_reference/security.rst:L3>; Outputs <ibex/doc/03_reference/security.rst:L9>
- source: integration.rst <ibex/doc/02_user/integration.rst:L1>

### pwrmgr
- id: `component_pwrmgr`, community: 7
- evidence: template param list <opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson:L5>; desc <opentitan/hw/ip_templates/pwrmgr/data/pwrmgr.tpldesc.hjson:L8>
- source: lc_ctrl_testplan.hjson <opentitan/hw/ip/lc_ctrl/data/lc_ctrl_testplan.hjson:L1>

### rstmgr
- id: `component_rstmgr`, community: 4
- evidence: resets <opentitan/hw/ip_templates/rstmgr/data/rstmgr.cfg.example.hjson:L32>; template param list <opentitan/hw/ip_templates/rstmgr/data/rstmgr.tpldesc.hjson:L5>
- source: README.md <opentitan/doc/project_governance/checklist/README.md:L1>

### pinmux
- id: `component_pinmux`, community: 10
- evidence: template param list <opentitan/hw/ip_templates/pinmux/data/pinmux.tpldesc.hjson:L5>; desc <opentitan/hw/ip_templates/pinmux/data/pinmux.tpldesc.hjson:L8>
- source: README.md <opentitan/doc/contributing/hw/comportability/README.md:L1>

### ipconfig
- id: `component_ipconfig`, community: 4
- evidence: instance name <opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson:L5>; param values <opentitan/hw/top_darjeeling/ip_autogen/ac_range_check/data/top_darjeeling_ac_range_check.ipconfig.hjson:L6>
- source: create_top.md <opentitan/hw/top/doc/create_top.md:L1>

### rv_core_ibex
- id: `component_rv_core_ibex`, community: 5
- evidence: template param list <opentitan/hw/ip_templates/rv_core_ibex/data/rv_core_ibex.tpldesc.hjson:L5>; desc <opentitan/hw/ip_templates/rv_core_ibex/data/rv_core_ibex.tpldesc.hjson:L8>
- source: verification_stages.rst <ibex/doc/03_reference/verification_stages.rst:L1>

### clkmgr
- id: `component_clkmgr`, community: 12
- evidence: template param list <opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson:L5>; desc <opentitan/hw/ip_templates/clkmgr/data/clkmgr.tpldesc.hjson:L8>
- source: README.md <opentitan/doc/contributing/dv/methodology/README.md:L1>

### system
- id: `component_system`, community: 11
- evidence: Overview <opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md:L1>; Features <opentitan/hw/vendor/pulp_riscv_dbg/doc/debug-system.md:L5>
- source: examples.rst <ibex/doc/02_user/examples.rst:L1>

### gpio
- id: `component_gpio`, community: 15
- evidence: template param list <opentitan/hw/ip_templates/gpio/data/gpio.tpldesc.hjson:L5>; desc <opentitan/hw/ip_templates/gpio/data/gpio.tpldesc.hjson:L8>
- source: README.md <opentitan/doc/contributing/hw/comportability/README.md:L1>

### rv_plic
- id: `component_rv_plic`, community: 9
- evidence: template param list <opentitan/hw/ip_templates/rv_plic/data/rv_plic.tpldesc.hjson:L5>; desc <opentitan/hw/ip_templates/rv_plic/data/rv_plic.tpldesc.hjson:L8>
- source: README.md <opentitan/doc/contributing/hw/comportability/README.md:L1>

### otp_ctrl
- id: `component_otp_ctrl`, community: 8
- evidence: template param list <opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl.tpldesc.hjson:L5>; desc <opentitan/hw/ip_templates/otp_ctrl/data/otp_ctrl.tpldesc.hjson:L8>
- source: lc_ctrl_testplan.hjson <opentitan/hw/ip/lc_ctrl/data/lc_ctrl_testplan.hjson:L1>

### flash_ctrl
- id: `component_flash_ctrl`, community: 16
- evidence: template param list <opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl.tpldesc.hjson:L5>; desc <opentitan/hw/ip_templates/flash_ctrl/data/flash_ctrl.tpldesc.hjson:L8>
- source: testplanner.md <ibex/vendor/lowrisc_ip/util/dvsim/doc/testplanner.md:L1>

### debug
- id: `component_debug`, community: 11
- evidence: Debug Support <ibex/doc/03_reference/debug.rst:L3>; Interface <ibex/doc/03_reference/debug.rst:L18>
- source: compliance.rst <ibex/doc/01_overview/compliance.rst:L1>

### verification
- id: `component_verification`, community: 0
- evidence: Verification <ibex/doc/03_reference/verification.rst:L3>; Ibex Core <ibex/doc/03_reference/verification.rst:L10>
- source: verification_overview.rst <ibex/doc/01_overview/verification_overview.rst:L1>

### alert_handler
- id: `component_alert_handler`, community: 4
- evidence: template param list <opentitan/hw/ip_templates/alert_handler/data/alert_handler.tpldesc.hjson:L5>; desc <opentitan/hw/ip_templates/alert_handler/data/alert_handler.tpldesc.hjson:L8>
- source: README.md <opentitan/doc/contributing/hw/comportability/README.md:L1>

## Topics
### memory
- id: `topic_memory`, community: 5
- anchors: Memory Access Checking and Bus Errors <ibex/doc/03_reference/cosim.rst:L145>; icache.rst <ibex/doc/03_reference/icache.rst:L1>; RAM Arrangement <ibex/doc/03_reference/icache.rst:L76>

### alert
- id: `topic_alert`, community: 2
- anchors: Recommendation 5 : Alerts <opentitan/doc/security/implementation_guidelines/hardware/README.md:L246>; interfaces.md <opentitan/hw/ip/adc_ctrl/doc/interfaces.md:L1>; Security Alerts <opentitan/hw/ip/adc_ctrl/doc/interfaces.md:L25>

### security
- id: `topic_security`, community: 2
- anchors: Security Features <ibex/doc/03_reference/security.rst:L3>; README.md <opentitan/doc/contributing/dv/sec_cm_dv_framework/README.md:L1>; Standardized Design Countermeasure Primitive <opentitan/doc/contributing/dv/sec_cm_dv_framework/README.md:L11>

### testplan
- id: `topic_testplan`, community: 0
- anchors: Verification Overview <ibex/doc/01_overview/verification_overview.rst:L1>; Verification Status <ibex/doc/01_overview/verification_overview.rst:L9>; rvfi.rst <ibex/doc/03_reference/rvfi.rst:L1>

### clock
- id: `topic_clock`, community: 3
- anchors: clocking <opentitan/hw/ip/dma/data/dma.hjson:L21>; mbx.hjson <opentitan/hw/ip/mbx/data/mbx.hjson:L1>; clocking <opentitan/hw/ip/mbx/data/mbx.hjson:L20>

### interrupt
- id: `topic_interrupt`, community: 2
- anchors: Interrupts and Debug Requests <ibex/doc/03_reference/cosim.rst:L126>; cs_registers.rst <ibex/doc/03_reference/cs_registers.rst:L1>; Machine Interrupt Enable Register mie <ibex/doc/03_reference/cs_registers.rst:L149>

### power
- id: `topic_power`, community: 7
- anchors: Running with the rest of the chip in sleep <opentitan/hw/ip/adc_ctrl/doc/programmers_guide.md:L25>; programmers_guide.md <opentitan/hw/ip/aon_timer/doc/programmers_guide.md:L1>; Wakeup count and threshold access <opentitan/hw/ip/aon_timer/doc/programmers_guide.md:L15>

### crypto
- id: `topic_crypto`, community: 6
- anchors: AES <opentitan/doc/glossary.md:L7>; cryptolib_api.md <opentitan/doc/security/cryptolib/cryptolib_api.md:L1>; AES data structures <opentitan/doc/security/cryptolib/cryptolib_api.md:L126>

### debug
- id: `topic_debug`, community: 11
- anchors: Interrupts and Debug Requests <ibex/doc/03_reference/cosim.rst:L126>; debug.rst <ibex/doc/03_reference/debug.rst:L1>; Debug Support <ibex/doc/03_reference/debug.rst:L3>

### entropy
- id: `topic_entropy`, community: 14
- anchors: Entropy source entropy source <opentitan/doc/security/README.md:L65>; CSRNG csrng <opentitan/doc/security/README.md:L71>; csrng.hjson <opentitan/hw/ip/csrng/data/csrng.hjson:L1>

## Source Maps
### theory_of_operation.md
- id: `doc_opentitan_hw_ip_lc_ctrl_doc_theory_of_operation_md`
- file: `opentitan/hw/ip/lc_ctrl/doc/theory_of_operation.md`
- sections: Theory of Operation <opentitan/hw/ip/lc_ctrl/doc/theory_of_operation.md:L1>; Power Up Sequence <opentitan/hw/ip/lc_ctrl/doc/theory_of_operation.md:L6>; Normal Operation <opentitan/hw/ip/lc_ctrl/doc/theory_of_operation.md:L24>; Unconditional Transitions <opentitan/hw/ip/lc_ctrl/doc/theory_of_operation.md:L29>

### top_darjeeling.gen.hjson
- id: `doc_opentitan_hw_top_darjeeling_data_autogen_top_darjeeling_gen_hjson`
- file: `opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.gen.hjson`
- sections: datawidth <opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.gen.hjson:L12>; racl config <opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.gen.hjson:L13>; power <opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.gen.hjson:L14>; domains <opentitan/hw/top_darjeeling/data/autogen/top_darjeeling.gen.hjson:L16>

### top_darjeeling.hjson
- id: `doc_opentitan_hw_top_darjeeling_data_top_darjeeling_hjson`
- file: `opentitan/hw/top_darjeeling/data/top_darjeeling.hjson`
- sections: datawidth <opentitan/hw/top_darjeeling/data/top_darjeeling.hjson:L10>; racl config <opentitan/hw/top_darjeeling/data/top_darjeeling.hjson:L13>; power <opentitan/hw/top_darjeeling/data/top_darjeeling.hjson:L16>; domains <opentitan/hw/top_darjeeling/data/top_darjeeling.hjson:L20>

### README.md
- id: `doc_opentitan_hw_top_earlgrey_doc_design_readme_md`
- file: `opentitan/hw/top_earlgrey/doc/design/README.md`
- sections: OpenTitan Earl Grey Chip Specification <opentitan/hw/top_earlgrey/doc/design/README.md:L1>; Theory of Operations <opentitan/hw/top_earlgrey/doc/design/README.md:L6>; Design Details <opentitan/hw/top_earlgrey/doc/design/README.md:L14>; Clocking and Reset <opentitan/hw/top_earlgrey/doc/design/README.md:L20>

### chip_testplan.hjson
- id: `doc_opentitan_hw_top_darjeeling_data_chip_testplan_hjson`
- file: `opentitan/hw/top_darjeeling/data/chip_testplan.hjson`
- sections: import testplans <opentitan/hw/top_darjeeling/data/chip_testplan.hjson:L8>; testpoints <opentitan/hw/top_darjeeling/data/chip_testplan.hjson:L17>; desc <opentitan/hw/top_darjeeling/data/chip_testplan.hjson:L26>; stage <opentitan/hw/top_darjeeling/data/chip_testplan.hjson:L33>

### xbar_main.gen.hjson
- id: `doc_opentitan_hw_top_darjeeling_ip_xbar_main_data_autogen_xbar_main_gen_hjson`
- file: `opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- sections: clock srcs <opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson:L11>; clk main i <opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson:L13>; clk fixed i <opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson:L14>; clock group <opentitan/hw/top_darjeeling/ip/xbar_main/data/autogen/xbar_main.gen.hjson:L16>

### xbar_peri.gen.hjson
- id: `doc_opentitan_hw_top_darjeeling_ip_xbar_peri_data_autogen_xbar_peri_gen_hjson`
- file: `opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson`
- sections: clock srcs <opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson:L11>; clk peri i <opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson:L13>; clock group <opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson:L15>; reset connections <opentitan/hw/top_darjeeling/ip/xbar_peri/data/autogen/xbar_peri.gen.hjson:L17>

### top_earlgrey.gen.hjson
- id: `doc_opentitan_hw_top_earlgrey_data_autogen_top_earlgrey_gen_hjson`
- file: `opentitan/hw/top_earlgrey/data/autogen/top_earlgrey.gen.hjson`
- sections: datawidth <opentitan/hw/top_earlgrey/data/autogen/top_earlgrey.gen.hjson:L12>; power <opentitan/hw/top_earlgrey/data/autogen/top_earlgrey.gen.hjson:L13>; domains <opentitan/hw/top_earlgrey/data/autogen/top_earlgrey.gen.hjson:L15>; wait for external reset <opentitan/hw/top_earlgrey/data/autogen/top_earlgrey.gen.hjson:L21>

### top_earlgrey.hjson
- id: `doc_opentitan_hw_top_earlgrey_data_top_earlgrey_hjson`
- file: `opentitan/hw/top_earlgrey/data/top_earlgrey.hjson`
- sections: datawidth <opentitan/hw/top_earlgrey/data/top_earlgrey.hjson:L10>; power <opentitan/hw/top_earlgrey/data/top_earlgrey.hjson:L13>; domains <opentitan/hw/top_earlgrey/data/top_earlgrey.hjson:L17>; wait for external reset <opentitan/hw/top_earlgrey/data/top_earlgrey.hjson:L23>

### xbar_main.gen.hjson
- id: `doc_opentitan_hw_top_earlgrey_ip_xbar_main_data_autogen_xbar_main_gen_hjson`
- file: `opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson`
- sections: clock srcs <opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson:L11>; clk main i <opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson:L13>; clk fixed i <opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson:L14>; clk usb i <opentitan/hw/top_earlgrey/ip/xbar_main/data/autogen/xbar_main.gen.hjson:L15>

## OpenKB Rule
- Build compact concept pages only from the anchors above.
- Do not infer detailed requirements unless the referenced source file is consulted.
