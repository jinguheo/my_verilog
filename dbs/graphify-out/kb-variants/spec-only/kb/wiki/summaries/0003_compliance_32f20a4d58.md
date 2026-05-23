---
doc_type: short
full_text: sources/0003_compliance_32f20a4d58.md
---

# Summary: Standards Compliance for Ibex

This document summarizes the RISC-V standards compliance profile of the [[ibex]] processor. It lists the specification versions Ibex targets, the ISA base profiles it can be configured for, and the instruction set extensions and privileged features it supports.

## Core compliance targets

Ibex is described as a standards-compliant 32-bit RISC-V processor. It aligns with these major specifications:

- [[RISC-V]] User-Level ISA, Volume I, version 20190608
- [[RISC-V]] Privileged Architecture, Volume II, version 20211203, with Ibex implementing Machine ISA version 1.12
- RISC-V External Debug Support, version 0.13.2
- [[RISC-V Bit-Manipulation Extension]] versions 1.0.0 and draft 0.93
- [[Smepmp]] version 1.0 for enhanced PMP-based memory protection

## Configurable base ISA support

Ibex can be configured to implement either of the following base instruction sets:

- [[RV32I]] Base Integer Instruction Set, version 2.1
- [[RV32E]] Base Integer Instruction Set, version 1.9

This emphasizes that Ibex is parameterized rather than fixed to a single base profile.

## Supported instruction set extensions

The document lists the main extensions available in Ibex and whether they are always enabled or optional:

- **C** — Compressed Instructions: always enabled
- **M** — Integer Multiplication and Division: optional
- **B** — Bit-Manipulation: optional
- **Zicsr** — CSR instructions: always enabled
- **Zifencei** — Instruction-fetch fence: always enabled
- **Zcb** — Code-size saving instructions: optional
- **Zcmp** — Push/pop/move code-size saving instructions: optional
- **Smepmp** — PMP enhancements for machine-mode memory access and execution prevention: always enabled when PMP is configured

These extensions show that Ibex balances baseline compatibility with area- and feature-dependent configurability.

## Privileged architecture features

According to the RISC-V Privileged Specification, Ibex supports:

- [[Machine Mode]] and [[User Mode]]
- All CSRs referenced by the privileged architecture documentation
- Performance counters
- Vectorized trap handling for exceptions and interrupts

This indicates support for core operating-system and runtime features needed by software stacks targeting RISC-V.

## Bit-manipulation note

The footnote clarifies an important compatibility detail: Ibex fully implements the ratified B-extension 1.0.0, including sub-extensions Zba, Zbb, Zbc, and Zbs. It also supports additional draft sub-extensions (Zbe, Zbf, Zbp, Zbr, Zbt) from version 0.93, with the caveat that draft features may change and may not be supported consistently by toolchains such as GCC or Clang.

## Takeaway

The document positions Ibex as a configurable, standards-oriented [[RISC-V]] core with strong compliance across base ISA, privileged architecture, debug, and selected optional extensions. Its main theme is that compliance depends on configuration, especially for features like [[RV32I]], [[RV32E]], [[M extension]], [[B extension]], and [[Smepmp]].

## Related Concepts
- [[concepts/risc-v]]
- [[concepts/embedded-processors]]
- [[concepts/open-source-hardware]]
- [[concepts/sphinx-documentation]]
