---
sources: [summaries/0005_licensing_d3fe8b66d2.md, summaries/0004_index_3411d17b96.md]
brief: Ibex is a parametrizable open-source 32-bit RISC-V CPU core for embedded use.
---

# Ibex CPU Core

Ibex is a **production-quality open-source 32-bit RISC-V CPU core** written in **SystemVerilog**. It is designed to be **heavily parametrizable**, making it adaptable to a range of embedded designs and implementation goals.

The core is presented as a mature, real-world processor intended for **embedded control applications**, with evidence of strong engineering maturity through **extensive verification** and **multiple tape-outs**.

## Core characteristics

- **ISA / architecture**: 32-bit [[concepts/risc-v]] compatible CPU core
- **Language**: SystemVerilog
- **Licensing model**: Open source under the **Apache License 2.0**
- **Design style**: Highly parametrizable
- **Primary use case**: Embedded control systems
- **Maturity indicators**: Extensive verification and multiple tape-outs

## Licensing and use

Ibex is released under the Apache license, version 2.0. This means it can be **used, modified, and distributed** for any purpose, including commercial use, without royalties.

The main obligations are the usual Apache 2.0 requirements: users should preserve the **copyright notices** and include the **original license**. The repository’s `LICENSE` file contains the full and legally binding license text.

Even though the license does not require it, the project explicitly welcomes **feedback, bug reports, questions, suggested improvements, and code contributions**. Community involvement is encouraged through GitHub **issues** and **pull requests**, and commercial support is available from lowRISC.

Related licensing themes are captured in [[concepts/licensing-obligations]], [[concepts/open_source_licensing]], [[concepts/contributor_workflow]], and [[concepts/commercial_support]].

## Why Ibex matters

Ibex sits at the intersection of several important hardware design concerns:

- **Standards compliance**: It is part of the RISC-V ecosystem and is expected to align with relevant implementation and compliance requirements.
- **Adaptability**: Parameterization makes it useful for different silicon targets and product constraints.
- **Trustworthiness**: Verification and tape-out history suggest a design that has progressed beyond a prototype stage.
- **Practical deployment**: Its focus on embedded control makes it relevant for resource-constrained systems where a small, reliable CPU core is needed.
- **Adoption friendliness**: The permissive Apache 2.0 license lowers barriers to reuse in both open and commercial settings.

## Related themes

- [[concepts/risc-v-compliance]] — the standards and compliance context around Ibex
- [[concepts/synthesis-targets]] — the kinds of hardware targets Ibex may be synthesized for
- [[concepts/verification]] — the verification practices supporting confidence in the core
- [[concepts/licensing-obligations]] — legal and financial considerations when using Ibex
- [[concepts/open_source_licensing]] — open source licensing model and reuse rights
- [[concepts/contributor_workflow]] — issue reporting, pull requests, and contribution norms
- [[concepts/commercial_support]] — vendor-backed support options
- [[summaries/0004_index_3411d17b96]] — source summary for the introduction page

## Source context

The source document is the introduction to the Ibex documentation tree. It serves as an entry point to deeper topics such as compliance, supported targets, licensing, contribution practices, and verification overview.

## Related Documents
- [[summaries/0005_licensing_d3fe8b66d2]]
