---
sources: [summaries/0003_compliance_32f20a4d58.md, summaries/0002_requirements_e3923399fe.md, summaries/0001_index_bd80d85a59.md]
brief: RISC-V is the open ISA foundation for Ibex and its configurable compliance
---

# RISC-V

RISC-V is an open instruction set architecture (ISA) for building processors and CPU cores. It defines the machine-level instructions, programmer-visible behavior, and architectural conventions that software and hardware must follow to be compatible.

## Why it matters in Ibex

The Ibex documentation identifies the core as an **embedded 32-bit RISC-V CPU core** [[summaries/0001_index_bd80d85a59]]. That means Ibex implements the RISC-V ISA as its architectural contract with software, while remaining configurable and suitable for embedded control applications.

The compliance documentation makes this relationship more concrete: Ibex is a standards-compliant 32-bit RISC-V processor that tracks specific versions of the user-level ISA, privileged architecture, debug support, bit-manipulation, and machine-mode memory protection extensions [[summaries/0003_compliance_32f20a4d58]]. In other words, RISC-V is not just the general foundation for Ibex — it is the formal compatibility target that shapes what the core can run and which features it exposes.

## Key characteristics

- **Open ISA**: RISC-V is publicly specified and widely adopted in open and commercial hardware.
- **Modular**: The architecture supports a base instruction set with optional extensions.
- **32-bit support**: Ibex is documented as a 32-bit implementation, targeting embedded-class systems.
- **Configurable compliance**: Ibex can be configured for either [[RV32I]] or [[RV32E]], and several extensions are optional while others are always enabled [[summaries/0003_compliance_32f20a4d58]].
- **Software compatibility**: Programs, compilers, and operating systems can target RISC-V-compliant cores.

## Ibex’s RISC-V compliance profile

The compliance document shows that Ibex follows several RISC-V specifications and related standards:

- RISC-V User-Level ISA, Volume I, version 20190608
- RISC-V Privileged Architecture, Volume II, version 20211203
- RISC-V External Debug Support, version 0.13.2
- RISC-V Bit-Manipulation Extension, versions 1.0.0 and draft 0.93
- [[Smepmp]] for enhanced machine-mode PMP behavior

Ibex also supports privileged features including:

- M-mode and U-mode
- all documented CSRs
- performance counters
- vectorized trap handling

This makes RISC-V in Ibex more than a baseline instruction set: it includes the privileged execution model and selected extension behavior needed for real embedded software stacks.

## Base ISA and extensions in Ibex

Ibex can be configured to support either of the following base instruction sets:

- [[RV32I]] Base Integer Instruction Set, version 2.1
- [[RV32E]] Base Integer Instruction Set, version 1.9

It also supports a set of standard extensions with different configurability:

- **C** — Compressed Instructions: always enabled
- **M** — Integer Multiplication and Division: optional
- **B** — Bit-Manipulation: optional
- **Zicsr** — CSR instructions: always enabled
- **Zifencei** — Instruction-Fetch Fence: always enabled
- **Zcb** — Simple code-size saving instructions: optional
- **Zcmp** — Push/Pop/Move code-size saving instructions: optional
- **Smepmp** — machine-mode PMP enhancements: always enabled in PMP-enabled configurations

The B extension is especially notable because Ibex fully implements the ratified 1.0.0 version while also supporting additional draft sub-extensions from version 0.93, such as Zbe, Zbf, Zbp, Zbr, and Zbt [[summaries/0003_compliance_32f20a4d58]].

## In the context of the source document

The document does not explain the RISC-V ISA in general terms; instead, it establishes Ibex’s standards position by listing the exact architectural specifications it follows. That makes RISC-V the compliance framework for the rest of the Ibex documentation.

The larger documentation set uses this foundation to organize material about:

- the high-level properties of the core,
- how to use it in designs,
- how the implementation works in detail,
- and how to contribute to the core itself.

## Related concepts

- [[concepts/embedded-processors]] — RISC-V cores like Ibex are commonly used in embedded systems.
- [[concepts/open-source-hardware]] — Ibex is open source, aligning with the openness of the ISA.
- [[concepts/systemverilog]] — the implementation language used for the core.
- [[concepts/parameterized-design]] — Ibex is heavily configurable while remaining RISC-V compatible.
- [[concepts/hardware-verification]] — verifying compliance and correctness is essential for ISA implementations.
- [[concepts/privileged-architecture]] — Ibex implements the RISC-V privileged execution model.
- [[concepts/bit-manipulation-extension]] — Ibex supports both ratified and draft B-extension features.
- [[concepts/machine-mode]] — Machine mode support is part of the compliance profile.

## See also

- [[summaries/0001_index_bd80d85a59]] — top-level Ibex documentation index that introduces the core as a RISC-V CPU.
- [[summaries/0002_requirements_e3923399fe]]
- [[summaries/0003_compliance_32f20a4d58]] — standards compliance details for Ibex.
