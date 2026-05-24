# SVA Manifest

Generated from `D:\MyWork\verilog\platform\sva`.

- Components: 1
- Assert properties: 8
- Cover properties: 4

## gpio

**Bound to:** `gpio`

| Kind | ID | Spec reference | File:line |
|------|-----|----------------|-----------|
| `assert` | `sva.gpio.rst.outputs_clear` | "After reset all outputs shall be 0 and output-enables deasserted." | `gpio_assert.sv:40` |
| `assert` | `sva.gpio.rst.oe_clear` |  | `gpio_assert.sv:48` |
| `assert` | `sva.gpio.rst.intr_clear` |  | `gpio_assert.sv:56` |
| `assert` | `sva.gpio.oe.asserted_when_reg_set` |  | `gpio_assert.sv:75` |
| `assert` | `sva.gpio.oe.deasserted_when_reg_clear` |  | `gpio_assert.sv:84` |
| `assert` | `sva.gpio.out.matches_reg_when_oe` |  | `gpio_assert.sv:106` |
| `assert` | `sva.gpio.masked.lower_unchanged_bits_stable` | "MASKED_OUT_LOWER write only changes bits whose mask bit is set." | `gpio_assert.sv:129` |
| `assert` | `sva.gpio.intr.gated_by_enable` |  | `gpio_assert.sv:150` |
| `cover` | `sva.gpio.cover.any_output_driven` |  | `gpio_assert.sv:163` |
| `cover` | `sva.gpio.cover.all_outputs_driven` |  | `gpio_assert.sv:167` |
| `cover` | `sva.gpio.cover.any_interrupt_fired` |  | `gpio_assert.sv:171` |
| `cover` | `anon_ln176` |  | `gpio_assert.sv:176` |
