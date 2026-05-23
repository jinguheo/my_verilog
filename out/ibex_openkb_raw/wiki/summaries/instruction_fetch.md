---
doc_type: short
full_text: sources/instruction_fetch.md
---

The Instruction Fetch (IF) stage supplies instructions to the Instruction-Decode (ID) stage, optimizing performance by fetching instructions into a prefetch buffer and managing instruction flow.

Instructions are stored in a prefetch buffer (``ibex_prefetch_buffer.sv``) and tracked along with their Program Counter (PC) in the fetch FIFO (``ibex_fetch_fifo.sv``). The fetch FIFO includes a feedthrough path to ensure immediate availability of new instructions.

The IF stage handles instruction expansion for compressed instructions, ensuring the decoder always receives uncompressed instructions.

If the Ibex is configured with an instruction cache (ICache), the prefetch buffer is replaced by the icache module, which includes signals for cache enabling and flushing upon executing a ``fence.i`` instruction.

Branch Prediction is an experimental feature that uses static prediction to improve performance by predicting branch outcomes based on offset signs, potentially avoiding stall cycles, although mis-predict penalties exist.

An Instruction-Side Memory Interface is defined by signals for requesting instructions, providing data, and reporting errors. These interfaces handle word-aligned fetches externally, but the core internally manages both word- and half-word-aligned addresses to support compressed instructions, ignoring the LSB of the instruction address.

The protocol used for communicating with the instruction cache or instruction memory is similar to the protocol used by the Load-Store Unit (LSU) on the data interface.

## Related Concepts
- [[concepts/instruction-fetch-pipeline]]
- [[concepts/branch-prediction]]
- [[concepts/memory-interface-protocol]]
