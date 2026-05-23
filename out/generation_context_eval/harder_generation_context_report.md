# Harder Generation Context Benchmark

- Total tasks: 77
- Style: blind-anchor retrieval
- Gold module names are removed from question text.
- Questions emphasize interfaces, child dependencies, coarse location, role, and negative constraints.

## Level Counts

| Level | Count |
|---|---:|
| L4 | 26 |
| L5 | 51 |

## Sample Questions

- `hardblind_001` gold=`top_darjeeling`
  - Blind anchor retrieval task: identify the existing RTL module that should be used as the primary source for a generation brief. The target module name is intentionally hidden. Use the following clues: role=top-level SoC integration wrapper; coarse location=D: / MyWork / opentitan; key interface signals/types=mio_in_i, mio_out_o, mio_oe_o, dio_in_i, dio_out_o; local child/dependency clues=uart, gpio, spi_device, i2c; semantic labels=i2c, spi, uart. Return the primary owner module, not a primitive, package, register helper, child dependency, or similarly named neighbor.
- `hardblind_002` gold=`top_earlgrey`
  - Blind anchor retrieval task: identify the existing RTL module that should be used as the primary source for a generation brief. The target module name is intentionally hidden. Use the following clues: role=top-level SoC integration wrapper; coarse location=D: / MyWork / opentitan; key interface signals/types=mio_in_i, mio_out_o, mio_oe_o, dio_in_i, dio_out_o; local child/dependency clues=pinmux_jtag_breakout, uart, gpio, spi_device; semantic labels=fifo, i2c, spi, uart. Return the primary owner module, not a primitive, package, register helper, child dependency, or similarly named neighbor.
- `hardblind_003` gold=`chip_darjeeling_asic`
  - Blind anchor retrieval task: identify the existing RTL module that should be used as the primary source for a generation brief. The target module name is intentionally hidden. Use the following clues: role=board/chip integration wrapper; coarse location=D: / MyWork / opentitan; key interface signals/types=POR_N, JTAG_TCK, JTAG_TMS, JTAG_TDI, JTAG_TDO; local child/dependency clues=ast, tlul_jtag_dtm, tlul_socket_m1, tlul_socket_1n; semantic labels=i2c, spi, uart. Return the primary owner module, not a primitive, package, register helper, child dependency, or similarly named neighbor.
- `hardblind_004` gold=`top_englishbreakfast`
  - Blind anchor retrieval task: identify the existing RTL module that should be used as the primary source for a generation brief. The target module name is intentionally hidden. Use the following clues: role=top-level SoC integration wrapper; coarse location=D: / MyWork / opentitan; key interface signals/types=mio_in_i, mio_out_o, mio_oe_o, dio_in_i, dio_out_o; local child/dependency clues=pinmux_jtag_breakout, uart, gpio, spi_device; semantic labels=apb, fifo, spi, uart. Return the primary owner module, not a primitive, package, register helper, child dependency, or similarly named neighbor.
- `hardblind_005` gold=`spi_device`
  - Blind anchor retrieval task: identify the existing RTL module that should be used as the primary source for a generation brief. The target module name is intentionally hidden. Use the following clues: role=hierarchical controller or subsystem wrapper; coarse location=D: / MyWork / opentitan; key interface signals/types=clk_i, rst_ni, tlul_pkg, prim_alert_pkg, top_racl_pkg; local child/dependency clues=prim_buf, prim_edge_detector, prim_intr_hw, prim_pulse_sync; semantic labels=fifo, spi, uart. Return the primary owner module, not a primitive, package, register helper, child dependency, or similarly named neighbor.
- `hardblind_006` gold=`ast`
  - Blind anchor retrieval task: identify the existing RTL module that should be used as the primary source for a generation brief. The target module name is intentionally hidden. Use the following clues: role=top-level SoC integration wrapper; coarse location=D: / MyWork / opentitan / top_earlgrey; key interface signals/types=tlul_pkg, prim_mubi_pkg, clk_[hidden-target]_adc_i, rst_[hidden-target]_adc_ni, clk_[hidden-target]_alert_i; local child/dependency clues=prim_clock_buf, prim_flop_2sync, prim_clock_inv, prim_flop; semantic labels=spi. Return the primary owner module, not a primitive, package, register helper, child dependency, or similarly named neighbor.
- `hardblind_007` gold=`flash_ctrl`
  - Blind anchor retrieval task: identify the existing RTL module that should be used as the primary source for a generation brief. The target module name is intentionally hidden. Use the following clues: role=top-level SoC integration wrapper; coarse location=MyWork / opentitan / top_englishbreakfast / ip_autogen; key interface signals/types=clk_i, rst_ni, rst_shadowed_ni, clk_otp_i, rst_otp_ni; local child/dependency clues=[hidden-target]_core_reg_top, [hidden-target]_region_cfg, prim_lc_sync, prim_lfsr; semantic labels=fifo, uart. Return the primary owner module, not a primitive, package, register helper, child dependency, or similarly named neighbor.
- `hardblind_008` gold=`flash_ctrl`
  - Blind anchor retrieval task: identify the existing RTL module that should be used as the primary source for a generation brief. The target module name is intentionally hidden. Use the following clues: role=top-level SoC integration wrapper; coarse location=MyWork / opentitan / top_earlgrey / ip_autogen; key interface signals/types=clk_i, rst_ni, rst_shadowed_ni, clk_otp_i, rst_otp_ni; local child/dependency clues=[hidden-target]_core_reg_top, [hidden-target]_region_cfg, prim_lc_sync, prim_lfsr; semantic labels=fifo, uart. Return the primary owner module, not a primitive, package, register helper, child dependency, or similarly named neighbor.
- `hardblind_009` gold=`chip_earlgrey_cw310`
  - Blind anchor retrieval task: identify the existing RTL module that should be used as the primary source for a generation brief. The target module name is intentionally hidden. Use the following clues: role=board/chip integration wrapper; coarse location=D: / MyWork / opentitan; key interface signals/types=POR_N, SPI_HOST_D0, SPI_HOST_D1, SPI_HOST_D2, SPI_HOST_D3; local child/dependency clues=clkgen_xil7series, ast, top_earlgrey, prim_flop_2sync; semantic labels=spi, uart. Return the primary owner module, not a primitive, package, register helper, child dependency, or similarly named neighbor.
- `hardblind_010` gold=`chip_earlgrey_cw340`
  - Blind anchor retrieval task: identify the existing RTL module that should be used as the primary source for a generation brief. The target module name is intentionally hidden. Use the following clues: role=board/chip integration wrapper; coarse location=D: / MyWork / opentitan; key interface signals/types=POR_N, SPI_HOST_D0, SPI_HOST_D1, SPI_HOST_D2, SPI_HOST_D3; local child/dependency clues=clkgen_xil_ultrascale, ast, top_earlgrey, prim_flop_2sync; semantic labels=spi, uart. Return the primary owner module, not a primitive, package, register helper, child dependency, or similarly named neighbor.
