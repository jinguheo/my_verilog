---
sources: [summaries/instruction_fetch.md]
brief: The Instruction Fetch (IF) stage manages instruction flow, buffering, and prediction to supply instructions to the ID stage efficiently.
---

# Instruction Fetch Pipeline

The Instruction Fetch (IF) stage is responsible for retrieving instructions from memory and supplying them to the Instruction-Decode (ID) stage, optimizing performance through buffering and prediction.

## Instruction Flow and Buffering

Instructions are fetched into a prefetch buffer (``ibex_prefetch_buffer.sv``) for optimal timing and performance. This data is then stored along with the Program Counter (PC) in the fetch FIFO (``ibex_fetch_fifo.sv``).

The fetch FIFO includes a feedthrough path, ensuring that instructions are immediately available upon the FIFO becoming empty.

## Instruction Handling

The IF stage handles the expansion of compressed instructions, ensuring the decoder receives uncompressed instructions. 

## Instruction Caching

If the system uses an instruction cache (ICache), the prefetch buffer is replaced by the [[icache]] module. The cache interface includes signals to enable the cache and flush it upon execution of a ``fence.i`` instruction.

## Branch Prediction

Ibex supports static branch prediction to improve performance by predicting branch outcomes based on offset signs. While this feature avoids stall cycles for correctly predicted branches, it introduces a mis-predict penalty, which must be accounted for.

## Instruction-Side Memory Interface

The instruction interface defines how the IF stage communicates with the instruction memory or cache. This interface handles requests, data retrieval, and error reporting. 

*   **Alignment:** Externally, the interface performs word-aligned instruction fetches. Internally, the core manages both word- and half-word-aligned addresses to support compressed instructions, ignoring the LSB of the instruction address.
*   **Protocol:** The communication protocol is similar to the protocol used by the Load-Store Unit (LSU) on the data interface.

This pipeline architecture ensures a smooth, high-throughput flow of instructions necessary for efficient execution.

## Related Documents
- [[summaries/instruction_fetch]]
