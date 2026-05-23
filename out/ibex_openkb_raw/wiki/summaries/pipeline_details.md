---
doc_type: short
full_text: sources/pipeline_details.md
---

# Ibex Pipeline Details

Ibex utilizes a two-stage pipeline: Instruction Fetch (IF) and Instruction Decode and Execute (ID/EX).

## Pipeline Stages

1. **Instruction Fetch (IF):** Fetches instructions from memory via a prefetch buffer, aiming to fetch one instruction per cycle if the memory system allows. 
2. **Instruction Decode and Execute (ID/EX):** Decodes the instruction and immediately executes it, including register reads and writes. Multi-cycle instructions may stall this stage until completion.

All instructions require a minimum of two cycles to pass through the pipeline (one in IF and one in ID/EX).

## Performance and Stalls

Without stalls, the maximum Instructions per Cycle (IPC) Ibex can achieve is 1. Stalls occur when instructions require variable time for memory access or complex operations, leading to delays in the ID/EX stage.

### Instruction Stall Characteristics

The duration an instruction stalls for is defined by its type and behavior, detailed in the table below:

| Instruction Type | Stall Cycles | Description |
| :--- | :--- | :--- |
| **Integer Computational** | 0 | Instructions defined in the RISCV-V RV32I Base Integer Instruction Set. |
| **CSR Access** | 0 | Instructions defined in the 'Zicsr' of the RISC-V specification. |
| **Load/Store** | 1 - N | Stalls to await memory response. The duration depends on how long the data side memory interface takes to receive a response. |
| **Multiplication** | 0/1 or 2/3 | Stalls depend on whether a single-cycle or fast multi-cycle multiplier is used (e.g., MUL vs. MULH).
| **Division** | 1 or 37 | 1 stall cycle if dividing by zero, otherwise full long division latency. |
| **Jump** | 1 - N | Stalls to flush the prefetch counter and begin fetching from the new Program Counter (PC). The stall length depends on memory interface latency. |
| **Branch (Not-Taken)** | 0 | No stall for branches where the condition is not met. |
| **Branch (Taken)** | 2 - N | Stalls for 2 cycles in the ID/EX stage, plus additional cycles based on the time needed to calculate the branch target using the ALU. |
| **Instruction Fence** | 1 - N | Stall determined by the instruction as defined in 'Zifencei' of the RISC-V specification.
| **Zcmp Push/Pop** | 2 - N | Stalls correspond to the total number of register load/store operations and stack pointer adjustments.
| **Zcmp Move** | 2 | Fixed stall of 2 cycles for the `cm.mvsa01` and `cm.mva01s` instructions.

These stall characteristics are directly influenced by the latency of the instruction-side memory interface and the complexity of the operation, referencing details in [[mult-div]] and [[mult-div]].