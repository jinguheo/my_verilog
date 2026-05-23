---
sources: [summaries/instruction_fetch.md]
brief: The Instruction Memory Interface Protocol governs how the Instruction Fetch stage communicates with the instruction cache or memory.
---

# Instruction Memory Interface Protocol

This protocol defines the communication mechanism used by the Instruction Fetch (IF) stage to interact with the instruction cache or instruction memory.

## Interface Overview

The interface is designed to facilitate the efficient fetching of instructions, similar to the data interface used by the Load-Store Unit (LSU).

### Protocol Similarity

The protocol used for instruction fetches is highly similar to the protocol employed by the LSU on the data interface of the processor.

*   See [[summaries/instruction_fetch]] for details on how this protocol is implemented in the IF stage.
*   For specific details on the underlying mechanism, refer to the [[LSU Protocol|LSU Protocol]].

## Instruction Fetch Interface

The instruction interface is a simplified version of the interface used on the data interface, focusing only on instruction requests and data flow, which avoids the need for write transactions.

### Key Signals

The interface uses a set of signals to manage the request, grant, and data transfer for instructions:

| Signal | Direction | Description |
| :--- | :--- | :--- |
| `instr_req_o` | output | Request valid, must stay high until `instr_gnt_i` is high for one cycle. |
| `instr_addr_o[31:0]` | output | The memory address, word aligned. |
| `instr_gnt_i` | input | The other side accepted the request; `instr_req_o` may be deasserted in the next cycle. |
| `instr_rvalid_i` | input | `instr_rdata_i` holds valid data when this signal is high, indicating exactly one cycle of data transfer. |
| `instr_rdata_i[31:0]` | input | The instruction data read from memory. |
| `instr_rdata_intg_i[6:0]` | input | Data integrity bits returned from memory. |
| `instr_err_i` | input | Indicates a memory access error occurred. |

## Alignment Handling

### External Alignment

Externally, the IF interface performs word-aligned instruction fetches only.

### Internal Alignment

Internally, the core is able to handle both word-aligned and half-word-aligned instruction addresses to support compressed instructions. The Least Significant Bit (LSB) of the instruction address is ignored internally to manage these alignments.
