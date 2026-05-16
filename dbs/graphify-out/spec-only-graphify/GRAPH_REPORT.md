# Graph Report - D:\MyWork\verilog\out\spec_documents_20260514_204108  (2026-05-16)

## Corpus Check
- Spec-only graph built deterministically from exported spec documents; no LLM/OpenKB ingest was run.

## Summary
- 8196 nodes · 30054 edges · 33 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_componentchecklist, componentverification, topictestplan|component:checklist, component:verification, topic:testplan]]
- [[_COMMUNITY_componentreadme, componentopentitan, componentrequirements|component:readme, component:opentitan, component:requirements]]
- [[_COMMUNITY_componentinterfaces, componentsecurity, topicalert|component:interfaces, component:security, topic:alert]]
- [[_COMMUNITY_componentlowrisc, componenttesting, componentgen|component:lowrisc, component:testing, component:gen]]
- [[_COMMUNITY_componentrstmgr, componentipconfig, componentalert_handler|component:rstmgr, component:ipconfig, component:alert_handler]]
- [[_COMMUNITY_componentrv_core_ibex, topicmemory, componentrom|component:rv_core_ibex, topic:memory, component:rom]]
- [[_COMMUNITY_componentaes, componentkmac, componentkeymgr|component:aes, component:kmac, component:keymgr]]
- [[_COMMUNITY_opentitanhw, componentprogrammers_guide, componentpwrmgr|opentitan/hw, component:programmers_guide, component:pwrmgr]]
- [[_COMMUNITY_componentsoftware, componentotp_ctrl, componentlc_ctrl|component:software, component:otp_ctrl, component:lc_ctrl]]
- [[_COMMUNITY_componentrv_plic, componentspecification, componenttlul|component:rv_plic, component:specification, component:tlul]]
- [[_COMMUNITY_componentpinmux, componentusbdev, componentpinmux_fpv_testplan|component:pinmux, component:usbdev, component:pinmux_fpv_testplan]]
- [[_COMMUNITY_componentsystem, componentdebug, componentrv_dm|component:system, component:debug, component:rv_dm]]
- [[_COMMUNITY_componentclkmgr, componentast, componenttpldesc|component:clkmgr, component:ast, component:tpldesc]]
- [[_COMMUNITY_componentprim, componentsram_ctrl, componentprim_flash|component:prim, component:sram_ctrl, component:prim_flash]]
- [[_COMMUNITY_componentedn, componentcsrng, componententropy_src|component:edn, component:csrng, component:entropy_src]]
- [[_COMMUNITY_componenttheory_of_operation, componentgpio, componentascon|component:theory_of_operation, component:gpio, component:ascon]]
- [[_COMMUNITY_componentflash_ctrl, componentflash_ctrl_testplan, componenthistory|component:flash_ctrl, component:flash_ctrl_testplan, component:history]]
- [[_COMMUNITY_componentotbn, componentisa, topicregisters|component:otbn, component:isa, topic:registers]]
- [[_COMMUNITY_componentspi_device, componentspi_host, componentspi_host_testplan|component:spi_device, component:spi_host, component:spi_host_testplan]]
- [[_COMMUNITY_componentsysrst_ctrl, componentsensor_ctrl, componentchip_pwrmgr_testplan|component:sysrst_ctrl, component:sensor_ctrl, component:chip_pwrmgr_testplan]]
- [[_COMMUNITY_componentpwm, componentpwm_testplan, componentpwm_sec_cm_testplan|component:pwm, component:pwm_testplan, component:pwm_sec_cm_testplan]]
- [[_COMMUNITY_componentuart, componentexample_ip_block, componentchip_uart_testplan|component:uart, component:example_ip_block, component:chip_uart_testplan]]
- [[_COMMUNITY_componentadc_ctrl, componentadc_ctrl_testplan, componentchip_adc_ctrl_testplan|component:adc_ctrl, component:adc_ctrl_testplan, component:chip_adc_ctrl_testplan]]
- [[_COMMUNITY_componenti2c, componenti2c_testplan, componentchip_i2c_testplan|component:i2c, component:i2c_testplan, component:chip_i2c_testplan]]
- [[_COMMUNITY_componentrv_timer, componentchip_rv_timer_testplan, componentchip_rv_timer_testplan_hjson|component:rv_timer, component:chip_rv_timer_testplan, component:chip_rv_timer_testplan_hjson]]
- [[_COMMUNITY_componentaon_timer, componentchip_aon_timer_testplan, componentchip_rstmgr_testplan|component:aon_timer, component:chip_aon_timer_testplan, component:chip_rstmgr_testplan]]
- [[_COMMUNITY_componentglossary, componentproducts, componenthjson_usage_style|component:glossary, component:products, component:hjson_usage_style]]
- [[_COMMUNITY_componentac_range_check, componentac_range_check_testplan, componenttop_darjeeling_ac_range_check|component:ac_range_check, component:ac_range_check_testplan, component:top_darjeeling_ac_range_check]]
- [[_COMMUNITY_componentpattgen, componentpattgen_testplan, componentpattgen_sec_cm_testplan|component:pattgen, component:pattgen_testplan, component:pattgen_sec_cm_testplan]]
- [[_COMMUNITY_componentibex_icache_dv_plan, componentibex_icache_testplan, ibexdv|component:ibex_icache_dv_plan, component:ibex_icache_testplan, ibex/dv]]
- [[_COMMUNITY_componentcommon_project_cfg, common_project_cfg.hjson, scratch base path|component:common_project_cfg, common_project_cfg.hjson, scratch base path]]
- [[_COMMUNITY_componentottf_testplan, ottf_testplan.hjson, stage|component:ottf_testplan, ottf_testplan.hjson, stage]]
- [[_COMMUNITY_componentcshake_nist_example_values, cshake_nist_example_values.hjson, security str|component:cshake_nist_example_values, cshake_nist_example_values.hjson, security str]]

## God Nodes (most connected - your core abstractions)
1. `component:checklist` - 856 edges
2. `opentitan/hw` - 797 edges
3. `component:readme` - 754 edges
4. `component:theory_of_operation` - 665 edges
5. `component:opentitan` - 653 edges
6. `component:lowrisc` - 508 edges
7. `component:programmers_guide` - 496 edges
8. `component:interfaces` - 492 edges
9. `component:security` - 392 edges
10. `component:software` - 366 edges

## Surprising Connections (you probably didn't know these)
- `Registers` --references_component--> `component:clkmgr`  [EXTRACTED]
  opentitan/hw/top_earlgrey/ip_autogen/clkmgr/doc/registers.md → __graphify_spec_only__/components.md
- `Summary` --references_component--> `component:clkmgr`  [EXTRACTED]
  opentitan/hw/top_earlgrey/ip_autogen/clkmgr/doc/registers.md → __graphify_spec_only__/components.md
- `Fields` --references_component--> `component:clkmgr`  [EXTRACTED]
  opentitan/hw/top_earlgrey/ip_autogen/clkmgr/doc/registers.md → __graphify_spec_only__/components.md
- `EXTCLK CTRL REGWEN` --references_component--> `component:clkmgr`  [EXTRACTED]
  opentitan/hw/top_earlgrey/ip_autogen/clkmgr/doc/registers.md → __graphify_spec_only__/components.md
- `EXTCLK CTRL` --references_component--> `component:clkmgr`  [EXTRACTED]
  opentitan/hw/top_earlgrey/ip_autogen/clkmgr/doc/registers.md → __graphify_spec_only__/components.md

## Communities

### Community 0 - "component:checklist, component:verification, topic:testplan"
Cohesion: 0.01
Nodes (765): component:checklist, component:development_stages, component:integration, component:setup, component:setup_verilator, component:testplan, component:verification, component:verification_overview (+757 more)

### Community 1 - "component:readme, component:opentitan, component:requirements"
Cohesion: 0.01
Nodes (716): opentitan/doc, opentitan/util, component:adding_python_depedencies, component:asm_coding_style, component:bazel_notes, component:bitbanging, component:build_docs, component:build_sw (+708 more)

### Community 2 - "component:interfaces, component:security, topic:alert"
Cohesion: 0.01
Nodes (553): component:contributing, component:dma, component:dma_sec_cm_testplan, component:dma_testplan, component:doe, component:exception_interrupts, component:interfaces, component:mbx (+545 more)

### Community 3 - "component:lowrisc, component:testing, component:gen"
Cohesion: 0.01
Nodes (464): component:all_rd_wr_mapping, component:cfg, component:create_top, component:edit, component:gen, component:lowrisc, component:news, component:opensource (+456 more)

### Community 4 - "component:rstmgr, component:ipconfig, component:alert_handler"
Cohesion: 0.01
Nodes (465): component:alert_agent_additional_testplan, component:alert_agent_basic_testplan, component:alert_handler, component:alert_handler_sec_cm_testplan, component:alert_handler_testplan, component:esc_agent_additional_testplan, component:esc_agent_basic_testplan, component:ipconfig (+457 more)

### Community 5 - "component:rv_core_ibex, topic:memory, component:rom"
Cohesion: 0.01
Nodes (424): opentitan/sw, component:boot, component:boot_log, component:bootstrap, component:build_software, component:chip_rv_core_ibex_testplan, component:chip_rv_core_ibex_testplan_hjson, component:cs_registers (+416 more)

### Community 6 - "component:aes, component:kmac, component:keymgr"
Cohesion: 0.01
Nodes (383): component:aes, component:aes_sec_cm_testplan, component:aes_testplan, component:chip_aes_testplan, component:chip_aes_testplan_hjson, component:chip_conn_testplan, component:chip_flash_ctrl_testplan, component:chip_flash_ctrl_testplan_hjson (+375 more)

### Community 7 - "opentitan/hw, component:programmers_guide, component:pwrmgr"
Cohesion: 0.01
Nodes (307): opentitan/hw, component:chip_rom_ctrl_testplan, component:chip_rom_ctrl_testplan_hjson, component:programmers_guide, component:pwrmgr, component:pwrmgr_sec_cm_testplan, component:pwrmgr_testplan, component:rom_ctrl (+299 more)

### Community 8 - "component:software, component:otp_ctrl, component:lc_ctrl"
Cohesion: 0.01
Nodes (279): component:background, component:chip_otp_ctrl_testplan, component:chip_otp_ctrl_testplan_hjson, component:lc_ctrl, component:lc_ctrl_access_signals_table, component:lc_ctrl_counter_table, component:lc_ctrl_encoding_table, component:lc_ctrl_flash_accessibility (+271 more)

### Community 9 - "component:rv_plic, component:specification, component:tlul"
Cohesion: 0.01
Nodes (275): component:chip_rv_plic_testplan, component:chip_rv_plic_testplan_hjson, component:compliance, component:dv_doc_template, component:performance_counters, component:prj, component:project_milestone_definitions, component:rv_plic (+267 more)

### Community 10 - "component:pinmux, component:usbdev, component:pinmux_fpv_testplan"
Cohesion: 0.02
Nodes (254): component:chip_usbdev_testplan, component:chip_usbdev_testplan_hjson, component:communications, component:pinmux, component:pinmux_fpv_testplan, component:pinmux_sec_cm_testplan, component:pinout_asic, component:pinout_cw305 (+246 more)

### Community 11 - "component:system, component:debug, component:rv_dm"
Cohesion: 0.02
Nodes (241): ibex/doc, component:chip_cfg, component:chip_csrng_testplan, component:chip_csrng_testplan_hjson, component:chip_lc_ctrl_testplan, component:chip_lc_ctrl_testplan_hjson, component:chip_rv_dm_testplan, component:chip_rv_dm_testplan_hjson (+233 more)

### Community 12 - "component:clkmgr, component:ast, component:tpldesc"
Cohesion: 0.02
Nodes (238): component:ast, component:chip_clkmgr_testplan, component:chip_clkmgr_testplan_hjson, component:chip_entropy_src_testplan, component:chip_entropy_src_testplan_hjson, component:clkmgr, component:clkmgr_sec_cm_testplan, component:clkmgr_testplan (+230 more)

### Community 13 - "component:prim, component:sram_ctrl, component:prim_flash"
Cohesion: 0.02
Nodes (216): ibex/vendor, component:chip_alert_handler_testplan, component:chip_alert_handler_testplan_hjson, component:mem_access_testplan, component:prim, component:prim_alert_testplan, component:prim_esc_testplan, component:prim_flash (+208 more)

### Community 14 - "component:edn, component:csrng, component:entropy_src"
Cohesion: 0.02
Nodes (217): component:chip_edn_testplan, component:chip_edn_testplan_hjson, component:csrng, component:csrng_sec_cm_testplan, component:csrng_testplan, component:edn, component:edn_sec_cm_testplan, component:edn_testplan (+209 more)

### Community 15 - "component:theory_of_operation, component:gpio, component:ascon"
Cohesion: 0.02
Nodes (210): component:ascon, component:gpio, component:gpio_sec_cm_testplan, component:gpio_testplan, component:theory_of_operation, one paragraph desc, regwidth, cip id (+202 more)

### Community 16 - "component:flash_ctrl, component:flash_ctrl_testplan, component:history"
Cohesion: 0.02
Nodes (164): component:flash_ctrl, component:flash_ctrl_sec_cm_testplan, component:flash_ctrl_testplan, component:history, component:top_earlgrey_flash_ctrl, component:top_englishbreakfast_flash_ctrl, References, History (+156 more)

### Community 17 - "component:otbn, component:isa, topic:registers"
Cohesion: 0.03
Nodes (155): component:chip_otbn_testplan, component:chip_otbn_testplan_hjson, component:coverage_plan, component:developing_otbn, component:fcov, component:instruction_decode_execute, component:isa, component:otbn (+147 more)

### Community 18 - "component:spi_device, component:spi_host, component:spi_host_testplan"
Cohesion: 0.03
Nodes (146): component:chip_spi_device_testplan, component:chip_spi_device_testplan_hjson, component:chip_spi_host_testplan, component:chip_spi_host_testplan_hjson, component:spi_device, component:spi_device_sec_cm_testplan, component:spi_device_testplan, component:spi_host (+138 more)

### Community 19 - "component:sysrst_ctrl, component:sensor_ctrl, component:chip_pwrmgr_testplan"
Cohesion: 0.04
Nodes (94): component:chip_pwrmgr_testplan, component:chip_pwrmgr_testplan_hjson, component:chip_sysrst_ctrl_testplan, component:chip_sysrst_ctrl_testplan_hjson, component:sensor_ctrl, component:sysrst_ctrl, component:sysrst_ctrl_sec_cm_testplan, component:sysrst_ctrl_testplan (+86 more)

### Community 20 - "component:pwm, component:pwm_testplan, component:pwm_sec_cm_testplan"
Cohesion: 0.05
Nodes (87): component:chip_pwm_testplan, component:chip_pwm_testplan_hjson, component:pwm, component:pwm_sec_cm_testplan, component:pwm_testplan, component:top_earlgrey_pwm, testpoints, desc (+79 more)

### Community 21 - "component:uart, component:example_ip_block, component:chip_uart_testplan"
Cohesion: 0.05
Nodes (75): component:chip_uart_testplan, component:chip_uart_testplan_hjson, component:example_ip_block, component:uart, component:uart_sec_cm_testplan, component:uart_testplan, Example IP Block, Overview (+67 more)

### Community 22 - "component:adc_ctrl, component:adc_ctrl_testplan, component:chip_adc_ctrl_testplan"
Cohesion: 0.06
Nodes (68): component:adc_ctrl, component:adc_ctrl_sec_cm_testplan, component:adc_ctrl_testplan, component:chip_adc_ctrl_testplan, component:chip_adc_ctrl_testplan_hjson, cip id, design spec, dv doc (+60 more)

### Community 23 - "component:i2c, component:i2c_testplan, component:chip_i2c_testplan"
Cohesion: 0.06
Nodes (68): component:chip_i2c_testplan, component:chip_i2c_testplan_hjson, component:i2c, component:i2c_sec_cm_testplan, component:i2c_testplan, cip id, design spec, dv doc (+60 more)

### Community 24 - "component:rv_timer, component:chip_rv_timer_testplan, component:chip_rv_timer_testplan_hjson"
Cohesion: 0.06
Nodes (66): component:chip_rv_timer_testplan, component:chip_rv_timer_testplan_hjson, component:outgoing_alerts_englishbreakfast, component:rv_timer, component:rv_timer_sec_cm_testplan, component:rv_timer_testplan, cip id, design spec (+58 more)

### Community 25 - "component:aon_timer, component:chip_aon_timer_testplan, component:chip_rstmgr_testplan"
Cohesion: 0.06
Nodes (63): component:aon_timer, component:aon_timer_sec_cm_testplan, component:aon_timer_testplan, component:chip_aon_timer_testplan, component:chip_aon_timer_testplan_hjson, component:chip_rstmgr_testplan, component:chip_rstmgr_testplan_hjson, cip id (+55 more)

### Community 26 - "component:glossary, component:products, component:hjson_usage_style"
Cohesion: 0.05
Nodes (61): component:earlgrey_a1, component:earlgrey_a2, component:glossary, component:hjson_usage_style, component:products, Build configuration, Build modes, Glossary of Terms (+53 more)

### Community 27 - "component:ac_range_check, component:ac_range_check_testplan, component:top_darjeeling_ac_range_check"
Cohesion: 0.08
Nodes (52): component:ac_range_check, component:ac_range_check_testplan, component:top_darjeeling_ac_range_check, covergroups, testpoints, desc, Stimulus, Checking (+44 more)

### Community 28 - "component:pattgen, component:pattgen_testplan, component:pattgen_sec_cm_testplan"
Cohesion: 0.08
Nodes (48): component:pattgen, component:pattgen_sec_cm_testplan, component:pattgen_testplan, cip id, design spec, dv doc, hw checklist, sw checklist (+40 more)

### Community 29 - "component:ibex_icache_dv_plan, component:ibex_icache_testplan, ibex/dv"
Cohesion: 0.11
Nodes (31): ibex/dv, component:ibex_icache_dv_plan, component:ibex_icache_testplan, desc, stage, tests, testpoints, Current status (+23 more)

### Community 30 - "component:common_project_cfg, common_project_cfg.hjson, scratch base path"
Cohesion: 0.32
Nodes (11): component:common_project_cfg, scratch base path, scratch path, build pass patterns, build fail patterns, exports, project, repo server (+3 more)

### Community 31 - "component:ottf_testplan, ottf_testplan.hjson, stage"
Cohesion: 0.42
Nodes (8): component:ottf_testplan, stage, tests, si stage, bazel, lc states, testpoints, desc

### Community 32 - "component:cshake_nist_example_values, cshake_nist_example_values.hjson, security str"
Cohesion: 0.46
Nodes (7): component:cshake_nist_example_values, vector identifier, operation, security str, input msg, cust str, digest

## Knowledge Gaps
- **25 isolated node(s):** `Introduction to Ibex`, `Ibex Configurations`, `Configuration Tool`, `Supported Configurations`, `Ibex User Guide` (+20 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `opentitan/hw` connect `opentitan/hw, component:programmers_guide, component:pwrmgr` to `component:checklist, component:verification, topic:testplan`, `component:readme, component:opentitan, component:requirements`, `component:interfaces, component:security, topic:alert`, `component:lowrisc, component:testing, component:gen`, `component:rstmgr, component:ipconfig, component:alert_handler`, `component:rv_core_ibex, topic:memory, component:rom`, `component:aes, component:kmac, component:keymgr`, `component:software, component:otp_ctrl, component:lc_ctrl`, `component:rv_plic, component:specification, component:tlul`, `component:pinmux, component:usbdev, component:pinmux_fpv_testplan`, `component:system, component:debug, component:rv_dm`, `component:clkmgr, component:ast, component:tpldesc`, `component:prim, component:sram_ctrl, component:prim_flash`, `component:edn, component:csrng, component:entropy_src`, `component:theory_of_operation, component:gpio, component:ascon`, `component:flash_ctrl, component:flash_ctrl_testplan, component:history`, `component:otbn, component:isa, topic:registers`, `component:spi_device, component:spi_host, component:spi_host_testplan`, `component:sysrst_ctrl, component:sensor_ctrl, component:chip_pwrmgr_testplan`, `component:pwm, component:pwm_testplan, component:pwm_sec_cm_testplan`, `component:uart, component:example_ip_block, component:chip_uart_testplan`, `component:adc_ctrl, component:adc_ctrl_testplan, component:chip_adc_ctrl_testplan`, `component:i2c, component:i2c_testplan, component:chip_i2c_testplan`, `component:rv_timer, component:chip_rv_timer_testplan, component:chip_rv_timer_testplan_hjson`, `component:aon_timer, component:chip_aon_timer_testplan, component:chip_rstmgr_testplan`, `component:ac_range_check, component:ac_range_check_testplan, component:top_darjeeling_ac_range_check`, `component:pattgen, component:pattgen_testplan, component:pattgen_sec_cm_testplan`, `component:ibex_icache_dv_plan, component:ibex_icache_testplan, ibex/dv`, `component:common_project_cfg, common_project_cfg.hjson, scratch base path`?**
  _High betweenness centrality (0.168) - this node is a cross-community bridge._
- **Why does `component:opentitan` connect `component:readme, component:opentitan, component:requirements` to `component:checklist, component:verification, topic:testplan`, `component:interfaces, component:security, topic:alert`, `component:lowrisc, component:testing, component:gen`, `component:rstmgr, component:ipconfig, component:alert_handler`, `component:rv_core_ibex, topic:memory, component:rom`, `component:aes, component:kmac, component:keymgr`, `opentitan/hw, component:programmers_guide, component:pwrmgr`, `component:software, component:otp_ctrl, component:lc_ctrl`, `component:rv_plic, component:specification, component:tlul`, `component:pinmux, component:usbdev, component:pinmux_fpv_testplan`, `component:system, component:debug, component:rv_dm`, `component:clkmgr, component:ast, component:tpldesc`, `component:prim, component:sram_ctrl, component:prim_flash`, `component:edn, component:csrng, component:entropy_src`, `component:theory_of_operation, component:gpio, component:ascon`, `component:flash_ctrl, component:flash_ctrl_testplan, component:history`, `component:otbn, component:isa, topic:registers`, `component:spi_device, component:spi_host, component:spi_host_testplan`, `component:sysrst_ctrl, component:sensor_ctrl, component:chip_pwrmgr_testplan`, `component:pwm, component:pwm_testplan, component:pwm_sec_cm_testplan`, `component:uart, component:example_ip_block, component:chip_uart_testplan`, `component:adc_ctrl, component:adc_ctrl_testplan, component:chip_adc_ctrl_testplan`, `component:i2c, component:i2c_testplan, component:chip_i2c_testplan`, `component:rv_timer, component:chip_rv_timer_testplan, component:chip_rv_timer_testplan_hjson`, `component:aon_timer, component:chip_aon_timer_testplan, component:chip_rstmgr_testplan`, `component:glossary, component:products, component:hjson_usage_style`, `component:ac_range_check, component:ac_range_check_testplan, component:top_darjeeling_ac_range_check`, `component:pattgen, component:pattgen_testplan, component:pattgen_sec_cm_testplan`, `component:ibex_icache_dv_plan, component:ibex_icache_testplan, ibex/dv`, `component:common_project_cfg, common_project_cfg.hjson, scratch base path`, `component:ottf_testplan, ottf_testplan.hjson, stage`, `component:cshake_nist_example_values, cshake_nist_example_values.hjson, security str`?**
  _High betweenness centrality (0.110) - this node is a cross-community bridge._
- **Why does `component:readme` connect `component:readme, component:opentitan, component:requirements` to `component:checklist, component:verification, topic:testplan`, `component:interfaces, component:security, topic:alert`, `component:lowrisc, component:testing, component:gen`, `component:rstmgr, component:ipconfig, component:alert_handler`, `component:rv_core_ibex, topic:memory, component:rom`, `component:aes, component:kmac, component:keymgr`, `opentitan/hw, component:programmers_guide, component:pwrmgr`, `component:software, component:otp_ctrl, component:lc_ctrl`, `component:rv_plic, component:specification, component:tlul`, `component:pinmux, component:usbdev, component:pinmux_fpv_testplan`, `component:system, component:debug, component:rv_dm`, `component:clkmgr, component:ast, component:tpldesc`, `component:prim, component:sram_ctrl, component:prim_flash`, `component:edn, component:csrng, component:entropy_src`, `component:theory_of_operation, component:gpio, component:ascon`, `component:flash_ctrl, component:flash_ctrl_testplan, component:history`, `component:otbn, component:isa, topic:registers`, `component:spi_device, component:spi_host, component:spi_host_testplan`, `component:sysrst_ctrl, component:sensor_ctrl, component:chip_pwrmgr_testplan`, `component:uart, component:example_ip_block, component:chip_uart_testplan`, `component:adc_ctrl, component:adc_ctrl_testplan, component:chip_adc_ctrl_testplan`, `component:i2c, component:i2c_testplan, component:chip_i2c_testplan`, `component:rv_timer, component:chip_rv_timer_testplan, component:chip_rv_timer_testplan_hjson`, `component:aon_timer, component:chip_aon_timer_testplan, component:chip_rstmgr_testplan`, `component:glossary, component:products, component:hjson_usage_style`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._
- **What connects `Introduction to Ibex`, `Ibex Configurations`, `Configuration Tool` to the rest of the system?**
  _25 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `component:checklist, component:verification, topic:testplan` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._
- **Should `component:readme, component:opentitan, component:requirements` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._
- **Should `component:interfaces, component:security, topic:alert` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._