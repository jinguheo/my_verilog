// Bind module: attaches gpio_assert to the gpio DUT without modifying RTL.
// Include this file in the simulation filelist or formal setup.
//
// Assumes OpenTitan GPIO interface with reg2hw struct from gpio_reg_top.

module gpio_bind;
  bind gpio gpio_assert #(.N(32)) u_gpio_assert (
    .clk_i               (clk_i),
    .rst_ni              (rst_ni),
    .cio_gpio_i          (cio_gpio_i),
    .cio_gpio_o          (cio_gpio_o),
    .cio_gpio_en_o       (cio_gpio_en_o),
    .reg_direct_out      (reg2hw.direct_out.q),
    .reg_direct_oe       (reg2hw.direct_oe.q),
    .reg_masked_out_lower(reg2hw.masked_out_lower.data.q),
    .reg_masked_oe_lower (reg2hw.masked_oe_lower.data.q),
    .reg_intr_enable     (reg2hw.intr_enable.q),
    .intr_gpio_o         (intr_gpio_o)
  );
endmodule : gpio_bind
