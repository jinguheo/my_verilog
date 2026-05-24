# Hardware Description: ibex

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

- **Standards Compliance**: Ibex is a standards-compliant 32 bit RISC-V processor.
- **Licensing**: Ibex is released under the Apache license, version 2.0.
- **Synthesis Targets**: ASIC Synthesis

## Identity

- `ip_block`: `ibex`
- `bridge_edge_count`: 370
- Spec categories: document: 537, testplan: 36, interface: 7
- Code categories: dv: 534, rtl: 100, other_code: 64
- Bridge relations: spec_path_matches_code_path: 370

## Spec Excerpts

### Standards Compliance
_Source: `ibex/doc/01_overview/compliance.rst`_

```
Standards Compliance
====================

Ibex is a standards-compliant 32 bit RISC-V processor.
It follows these specifications:

* `RISC-V Instruction Set Manual, Volume I: User-Level ISA, document version 20190608-Base-Ratified (June 8, 2019) <https://github.com/riscv/riscv-isa-manual/releases/download/Ratified-IMFDQC-and-Priv-v1.11/riscv-spec-20190608.pdf>`_
* `RISC-V Instruction Set Manual,
…
```

### Licensing
_Source: `ibex/doc/01_overview/licensing.rst`_

```
Licensing
=========

Ibex is released under the Apache license, version 2.0.

Ibex can be used, modified, and distributed for any purpose (including commercial) and without any royalties.
There are some requirements on including copyright notices and the original license.
```

### Synthesis Targets
_Source: `ibex/doc/01_overview/targets.rst`_

```
Synthesis Targets
=================

ASIC Synthesis
--------------

ASIC synthesis is supported for Ibex.
The whole design is completely synchronous and uses positive-edge triggered flip-flops, except for the register file, which can be implemented either with latches or with flip-flops.
```

### ASIC Synthesis
_Source: `ibex/doc/01_overview/targets.rst`_

```
Synthesis Targets
=================

ASIC Synthesis
--------------

ASIC synthesis is supported for Ibex.
The whole design is completely synchronous and uses positive-edge triggered flip-flops, except for the register file, which can be implemented either with latches or with flip-flops.
See :ref:`register-file` for more details.

FPGA Synthesis
```

### FPGA Synthesis
_Source: `ibex/doc/01_overview/targets.rst`_

```
ASIC Synthesis
--------------

ASIC synthesis is supported for Ibex.
The whole design is completely synchronous and uses positive-edge triggered flip-flops, except for the register file, which can be implemented either with latches or with flip-flops.
See :ref:`register-file` for more details.

FPGA Synthesis
--------------

FPGA Synthesis is supported for Ibex.
The FPGA-optimized register file im
…
```

### Verification Overview
_Source: `ibex/doc/01_overview/verification_overview.rst`_

```
Verification Overview
=====================

Ibex is verified using a :ref:`UVM based testbench<verification>` that employs a :ref:`co-simulation methodology<cosim>` to cross-check Ibex execution against an ISS reference model (`Spike <https://github.com/lowRISC/riscv-isa-sim>`_).
The testbench runs binaries built from source produced by the `RISC-DV <https://github.com/chipsalliance/riscv-dv>`_ r
…
```

### Verification Status
_Source: `ibex/doc/01_overview/verification_overview.rst`_

```
Verification Overview
=====================

Ibex is verified using a :ref:`UVM based testbench<verification>` that employs a :ref:`co-simulation methodology<cosim>` to cross-check Ibex execution against an ISS reference model (`Spike <https://github.com/lowRISC/riscv-isa-sim>`_).
The testbench runs binaries built from source produced by the `RISC-DV <https://github.com/chipsalliance/riscv-dv>`_ r
…
```

### Examples
_Source: `ibex/doc/02_user/examples.rst`_

```
.. _examples:

Examples
========

There are two examples that demonstrate Ibex usage.

The first is 'Simple System' and is part of the Ibex repository.
It demonstrates a minimal system connecting Ibex to some memory with a timer peripheral and is targeted at simulation.
```

## Spec Anchors

- `compliance.rst` (L1) — `ibex/doc/01_overview/compliance.rst`
- `Standards Compliance` (L1) — `ibex/doc/01_overview/compliance.rst`
- `index.rst` (L1) — `ibex/doc/01_overview/index.rst`
- `Introduction to Ibex` (L1) — `ibex/doc/01_overview/index.rst`
- `licensing.rst` (L1) — `ibex/doc/01_overview/licensing.rst`
- `Licensing` (L1) — `ibex/doc/01_overview/licensing.rst`
- `targets.rst` (L1) — `ibex/doc/01_overview/targets.rst`
- `Synthesis Targets` (L1) — `ibex/doc/01_overview/targets.rst`
- `ASIC Synthesis` (L4) — `ibex/doc/01_overview/targets.rst`
- `FPGA Synthesis` (L11) — `ibex/doc/01_overview/targets.rst`
- `verification_overview.rst` (L1) — `ibex/doc/01_overview/verification_overview.rst`
- `Verification Overview` (L1) — `ibex/doc/01_overview/verification_overview.rst`
- `Verification Status` (L9) — `ibex/doc/01_overview/verification_overview.rst`
- `configuration.rst` (L1) — `ibex/doc/02_user/configuration.rst`
- `Ibex Configurations` (L3) — `ibex/doc/02_user/configuration.rst`
- `Configuration Tool` (L11) — `ibex/doc/02_user/configuration.rst`
- `Supported Configurations` (L35) — `ibex/doc/02_user/configuration.rst`
- `examples.rst` (L1) — `ibex/doc/02_user/examples.rst`
- `Examples` (L3) — `ibex/doc/02_user/examples.rst`
- `Simple System` (L14) — `ibex/doc/02_user/examples.rst`
- `getting_started.rst` (L1) — `ibex/doc/02_user/getting_started.rst`
- `Getting Started with Ibex` (L3) — `ibex/doc/02_user/getting_started.rst`
- `index.rst` (L1) — `ibex/doc/02_user/index.rst`
- `Ibex User Guide` (L1) — `ibex/doc/02_user/index.rst`
- `integration.rst` (L1) — `ibex/doc/02_user/integration.rst`
- `Core Integration` (L3) — `ibex/doc/02_user/integration.rst`
- `Register File` (L10) — `ibex/doc/02_user/integration.rst`
- `Identification CSRs` (L17) — `ibex/doc/02_user/integration.rst`
- `Primitives` (L33) — `ibex/doc/02_user/integration.rst`
- `RTL File List` (L65) — `ibex/doc/02_user/integration.rst`
- `Instantiation Template` (L86) — `ibex/doc/02_user/integration.rst`
- `Parameters` (L183) — `ibex/doc/02_user/integration.rst`
- `Interfaces` (L271) — `ibex/doc/02_user/integration.rst`
- `system_requirements.rst` (L1) — `ibex/doc/02_user/system_requirements.rst`
- `System and Tool Requirements` (L1) — `ibex/doc/02_user/system_requirements.rst`

## Code Evidence

**DV** (48)
  - `cosim.h`:L1 — `ibex\dv\cosim\cosim.h`
  - `cosim_dpi.cc`:L1 — `ibex\dv\cosim\cosim_dpi.cc`
  - `cosim_dpi.h`:L1 — `ibex\dv\cosim\cosim_dpi.h`
  - `spike_cosim.cc`:L1 — `ibex\dv\cosim\spike_cosim.cc`
  - `spike_cosim.h`:L1 — `ibex\dv\cosim\spike_cosim.h`
  - `base_register.cc`:L1 — `ibex\dv\cs_registers\model\base_register.cc`
  - `base_register.h`:L1 — `ibex\dv\cs_registers\model\base_register.h`
  - `register_model.cc`:L1 — `ibex\dv\cs_registers\model\register_model.cc`
  - `register_model.h`:L1 — `ibex\dv\cs_registers\model\register_model.h`
  - `register_driver.cc`:L1 — `ibex\dv\cs_registers\reg_driver\register_driver.cc`
  - `register_driver.h`:L1 — `ibex\dv\cs_registers\reg_driver\register_driver.h`
  - `register_transaction.cc`:L1 — `ibex\dv\cs_registers\reg_driver\register_transaction.cc`
  - `register_transaction.h`:L1 — `ibex\dv\cs_registers\reg_driver\register_transaction.h`
  - `reg_dpi.cc`:L1 — `ibex\dv\cs_registers\reg_driver\reg_dpi.cc`
  - `reg_dpi.sv`:L1 — `ibex\dv\cs_registers\reg_driver\reg_dpi.sv`
  - `reset_driver.cc`:L1 — `ibex\dv\cs_registers\rst_driver\reset_driver.cc`
  - `reset_driver.h`:L1 — `ibex\dv\cs_registers\rst_driver\reset_driver.h`
  - `rst_dpi.cc`:L1 — `ibex\dv\cs_registers\rst_driver\rst_dpi.cc`
  - `rst_dpi.sv`:L1 — `ibex\dv\cs_registers\rst_driver\rst_dpi.sv`
  - `tb_cs_registers.cc`:L1 — `ibex\dv\cs_registers\tb\tb_cs_registers.cc`
**OTHER_CODE** (2)
  - `__init__.py`:L1 — `ibex\__init__.py`
  - `conf.py`:L1 — `ibex\doc\conf.py`

## Neighbor Components

- `lowrisc_ibex` (402 refs; contains×310, imports_from×52, instantiates×39)
- `verilator_sim_ctrl.cc` (4 refs; calls×4)
- `riscv-tests` (2 refs; calls×2)
- `lowrisc_ip` (2 refs; imports_from×2)
- `pulp_riscv_dbg` (1 refs; instantiates×1)
- `prim_generic` (1 refs; instantiates×1)
- `prim` (1 refs; instantiates×1)

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_path_matches_code_path` | `compliance.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `compliance.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `index.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `index.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `index.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `index.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `index.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `index.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `index.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `index.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `licensing.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `targets.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `verification_overview.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `configuration.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `encodings.sv` | `ibex\dv\formal\check\encodings.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `spec_instance.sv` | `ibex\dv\formal\check\spec_instance.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `top.sv` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `examples.rst` | `top` | `ibex\dv\formal\check\top.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `reg_dpi.sv` | `ibex\dv\cs_registers\reg_driver\reg_dpi.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `rst_dpi.sv` | `ibex\dv\cs_registers\rst_driver\rst_dpi.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `tb_cs_registers.sv` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |
| `spec_path_matches_code_path` | `getting_started.rst` | `tb_cs_registers` | `ibex\dv\cs_registers\tb\tb_cs_registers.sv` |

## Retrieval Guidance

- For code-only queries mentioning `ibex`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `ibex`.
