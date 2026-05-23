# Adversarial Retrieval Benchmark

- Total tasks: 117
- Target names are hidden.
- Questions are built from ambiguous child, sibling, and label neighborhoods.

| Type | Count |
|---|---:|
| adversarial_label_ambiguity | 22 |
| adversarial_parent_from_shared_child | 50 |
| adversarial_sibling_disambiguation | 45 |

## Samples

- `advret_001` gold=`dmi_cdc`
  - Adversarial parent retrieval. A query is centered on a reused child dependency `prim_flop_2sync`, but the answer must be the owning parent module. Pick the parent whose coarse area is vendor / pulp_riscv_dbg / src, whose common interface clues are clk_i, rst_ni, testmode_i, test_rst_ni, and whose semantic role hints are fifo. Do not return the child itself or another parent that only shares the same child.
- `advret_002` gold=`chip_englishbreakfast_cw305`
  - Adversarial parent retrieval. A query is centered on a reused child dependency `prim_flop_2sync`, but the answer must be the owning parent module. Pick the parent whose coarse area is D: / opentitan, whose common interface clues are POR_N, USB_P, USB_N, SPI_DEV_D0, and whose semantic role hints are spi. Do not return the child itself or another parent that only shares the same child.
- `advret_003` gold=`rv_plic`
  - Adversarial parent retrieval. A query is centered on a reused child dependency `prim_flop_2sync`, but the answer must be the owning parent module. Pick the parent whose coarse area is opentitan / top_darjeeling / ip_autogen, whose common interface clues are clk_i, rst_ni, tlul_pkg, tlul_pkg, and whose semantic role hints are fifo, uart. Do not return the child itself or another parent that only shares the same child.
- `advret_004` gold=`rv_core_ibex`
  - Adversarial parent retrieval. A query is centered on a reused child dependency `prim_flop_2sync`, but the answer must be the owning parent module. Pick the parent whose coarse area is opentitan / top_darjeeling / ip_autogen, whose common interface clues are clk_i, rst_ni, tlul_pkg, tlul_pkg, and whose semantic role hints are apb, fifo. Do not return the child itself or another parent that only shares the same child.
- `advret_005` gold=`ibex_lockstep`
  - Adversarial parent retrieval. A query is centered on a reused child dependency `prim_flop`, but the answer must be the owning parent module. Pick the parent whose coarse area is D:, whose common interface clues are clk_i, rst_ni, hart_id_i, boot_addr_i, and whose semantic role hints are apb. Do not return the child itself or another parent that only shares the same child.
- `advret_006` gold=`rv_core_ibex_cfg_reg_top`
  - Adversarial parent retrieval. A query is centered on a reused child dependency `prim_flop`, but the answer must be the owning parent module. Pick the parent whose coarse area is D: / opentitan / ip_autogen, whose common interface clues are clk_i, rst_ni, tlul_pkg, tlul_pkg, and whose semantic role hints are spi. Do not return the child itself or another parent that only shares the same child.
- `advret_007` gold=`rstmgr_por`
  - Adversarial parent retrieval. A query is centered on a reused child dependency `prim_flop`, but the answer must be the owning parent module. Pick the parent whose coarse area is D: / opentitan / ip_templates, whose common interface clues are clk_i, rst_ni, scan_rst_ni, scanmode_i, and whose semantic role hints are clocked, hierarchical, resettable. Do not return the child itself or another parent that only shares the same child.
- `advret_008` gold=`pwrmgr_fsm`
  - Adversarial parent retrieval. A query is centered on a reused child dependency `prim_flop`, but the answer must be the owning parent module. Pick the parent whose coarse area is opentitan / top_darjeeling / ip_autogen, whose common interface clues are clk_i, rst_ni, clk_slow_i, rst_slow_ni, and whose semantic role hints are uart. Do not return the child itself or another parent that only shares the same child.
- `advret_009` gold=`rv_plic_reg_top`
  - Adversarial parent retrieval. A query is centered on a reused child dependency `tlul_rsp_intg_gen`, but the answer must be the owning parent module. Pick the parent whose coarse area is D: / opentitan / ip_autogen, whose common interface clues are clk_i, rst_ni, tlul_pkg, tlul_pkg, and whose semantic role hints are spi. Do not return the child itself or another parent that only shares the same child.
- `advret_010` gold=`rstmgr_reg_top`
  - Adversarial parent retrieval. A query is centered on a reused child dependency `tlul_rsp_intg_gen`, but the answer must be the owning parent module. Pick the parent whose coarse area is D: / opentitan / ip_autogen, whose common interface clues are clk_i, rst_ni, tlul_pkg, tlul_pkg, and whose semantic role hints are spi. Do not return the child itself or another parent that only shares the same child.
- `advret_011` gold=`pwrmgr_reg_top`
  - Adversarial parent retrieval. A query is centered on a reused child dependency `tlul_rsp_intg_gen`, but the answer must be the owning parent module. Pick the parent whose coarse area is D: / opentitan / ip_autogen, whose common interface clues are clk_i, rst_ni, tlul_pkg, tlul_pkg, and whose semantic role hints are spi. Do not return the child itself or another parent that only shares the same child.
- `advret_012` gold=`ibex_top`
  - Adversarial parent retrieval. A query is centered on a reused child dependency `prim_buf`, but the answer must be the owning parent module. Pick the parent whose coarse area is D:, whose common interface clues are clk_i, rst_ni, test_en_i, prim_ram_1p_pkg, and whose semantic role hints are apb. Do not return the child itself or another parent that only shares the same child.
