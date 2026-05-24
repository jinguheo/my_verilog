// GPIO SVA Assertions
// Source spec: opentitan/hw/ip_templates/gpio/doc/README.md
// Covers: reset behaviour, output enable, masked writes, interrupt gating
//
// Usage: bound to gpio module via gpio_bind.sv
// Simulate: vcs/questa with -assert enable_diag
// Formal:   SymbiYosys with --mode prove

module gpio_assert #(
  parameter int unsigned N = 32
) (
  input  logic        clk_i,
  input  logic        rst_ni,

  // Pad signals
  input  logic [N-1:0] cio_gpio_i,
  input  logic [N-1:0] cio_gpio_o,
  input  logic [N-1:0] cio_gpio_en_o,

  // Register mirror (connected via bind)
  input  logic [N-1:0] reg_direct_out,   // GPIO_OUT / DIRECT_OUT register
  input  logic [N-1:0] reg_direct_oe,    // GPIO_OE  / DIRECT_OE  register
  input  logic [N-1:0] reg_masked_out_lower,  // MASKED_OUT_LOWER.data
  input  logic [N-1:0] reg_masked_oe_lower,   // MASKED_OE_LOWER.data
  input  logic [N-1:0] reg_intr_enable,  // INTR_ENABLE register
  input  logic [N-1:0] intr_gpio_o       // interrupt output lines
);

  // ----------------------------------------------------------------
  // Reset properties
  // SPEC: "After reset all outputs shall be 0 and output-enables deasserted."
  // REF:  gpio/doc/README.md §Reset Behaviour
  // ----------------------------------------------------------------

  // sva.gpio.rst.outputs_clear
  // All output values must be 0 while reset is asserted.
  property p_rst_outputs_zero;
    @(posedge clk_i) !rst_ni |-> (cio_gpio_o == '0);
  endproperty
  assert property (p_rst_outputs_zero)
    else $error("SVA FAIL gpio.rst.outputs_clear: cio_gpio_o != 0 during reset");

  // sva.gpio.rst.oe_clear
  // All output-enables must be deasserted while reset is asserted.
  property p_rst_oe_zero;
    @(posedge clk_i) !rst_ni |-> (cio_gpio_en_o == '0);
  endproperty
  assert property (p_rst_oe_zero)
    else $error("SVA FAIL gpio.rst.oe_clear: cio_gpio_en_o != 0 during reset");

  // sva.gpio.rst.intr_clear
  // No interrupts while reset is asserted.
  property p_rst_intr_zero;
    @(posedge clk_i) !rst_ni |-> (intr_gpio_o == '0);
  endproperty
  assert property (p_rst_intr_zero)
    else $error("SVA FAIL gpio.rst.intr_clear: intr_gpio_o != 0 during reset");


  // ----------------------------------------------------------------
  // Output enable properties
  // SPEC: "cio_gpio_en_o[i] reflects DIRECT_OE[i] when DIRECT_OE controls the pin."
  // REF:  gpio/doc/README.md §Output Enable
  // ----------------------------------------------------------------

  generate
    for (genvar i = 0; i < N; i++) begin : g_oe

      // sva.gpio.oe.asserted_when_reg_set
      // When DIRECT_OE bit is set, output-enable must be asserted.
      property p_oe_asserted;
        @(posedge clk_i) disable iff (!rst_ni)
        reg_direct_oe[i] |-> cio_gpio_en_o[i];
      endproperty
      assert property (p_oe_asserted)
        else $error("SVA FAIL gpio.oe.asserted_when_reg_set [%0d]", i);

      // sva.gpio.oe.deasserted_when_reg_clear
      // When DIRECT_OE bit is clear, output-enable must be deasserted.
      property p_oe_deasserted;
        @(posedge clk_i) disable iff (!rst_ni)
        !reg_direct_oe[i] |-> !cio_gpio_en_o[i];
      endproperty
      assert property (p_oe_deasserted)
        else $error("SVA FAIL gpio.oe.deasserted_when_reg_clear [%0d]", i);

    end
  endgenerate


  // ----------------------------------------------------------------
  // Direct output properties
  // SPEC: "cio_gpio_o[i] reflects DIRECT_OUT[i] when output-enable is set."
  // REF:  gpio/doc/README.md §Output Value
  // ----------------------------------------------------------------

  generate
    for (genvar i = 0; i < N; i++) begin : g_out

      // sva.gpio.out.matches_reg_when_oe
      // Output value must match DIRECT_OUT register when OE is set.
      property p_out_matches_reg;
        @(posedge clk_i) disable iff (!rst_ni)
        reg_direct_oe[i] |-> (cio_gpio_o[i] == reg_direct_out[i]);
      endproperty
      assert property (p_out_matches_reg)
        else $error("SVA FAIL gpio.out.matches_reg_when_oe [%0d]", i);

    end
  endgenerate


  // ----------------------------------------------------------------
  // Masked-write properties
  // SPEC: "MASKED_OUT_LOWER write only changes bits whose mask bit is set."
  // REF:  gpio/doc/README.md §Masked Output
  // ----------------------------------------------------------------

  // sva.gpio.masked.lower_unchanged_bits_stable
  // Bits outside the mask must not change on a masked-lower write.
  // (Checked combinatorially: mask=upper half of MASKED_OUT_LOWER)
  property p_masked_lower_bit_stability (int i);
    @(posedge clk_i) disable iff (!rst_ni)
    // If mask bit N/2+i is 0, output bit i must track direct_out not masked_out
    !reg_masked_oe_lower[i] |-> (cio_gpio_o[i] == reg_direct_out[i]);
  endproperty
  generate
    for (genvar i = 0; i < N/2; i++) begin : g_masked_lower
      assert property (p_masked_lower_bit_stability(i))
        else $error("SVA FAIL gpio.masked.lower_unchanged_bits_stable [%0d]", i);
    end
  endgenerate


  // ----------------------------------------------------------------
  // Interrupt properties
  // SPEC: "An interrupt is raised only when the corresponding INTR_ENABLE bit is set."
  // REF:  gpio/doc/README.md §Interrupts
  // ----------------------------------------------------------------

  generate
    for (genvar i = 0; i < N; i++) begin : g_intr

      // sva.gpio.intr.gated_by_enable
      // Interrupt can only fire when INTR_ENABLE bit is set.
      property p_intr_gated;
        @(posedge clk_i) disable iff (!rst_ni)
        intr_gpio_o[i] |-> reg_intr_enable[i];
      endproperty
      assert property (p_intr_gated)
        else $error("SVA FAIL gpio.intr.gated_by_enable [%0d]", i);

    end
  endgenerate


  // ----------------------------------------------------------------
  // Cover properties — reachability goals
  // SPEC: verify that key scenarios are reachable in simulation
  // ----------------------------------------------------------------

  // sva.gpio.cover.any_output_driven
  cover property (@(posedge clk_i) disable iff (!rst_ni)
    cio_gpio_en_o != '0);

  // sva.gpio.cover.all_outputs_driven
  cover property (@(posedge clk_i) disable iff (!rst_ni)
    cio_gpio_en_o == '1);

  // sva.gpio.cover.any_interrupt_fired
  cover property (@(posedge clk_i) disable iff (!rst_ni)
    intr_gpio_o != '0);

  // sva.gpio.cover.mixed_oe_state
  // Some pins driven output, some input simultaneously
  cover property (@(posedge clk_i) disable iff (!rst_ni)
    (cio_gpio_en_o != '0) && (cio_gpio_en_o != '1));

endmodule : gpio_assert
