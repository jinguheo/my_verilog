# Code-Only vs Spec-Code Graphify Re-evaluation

- Questions: 150
- Benchmark: `D:\MyWork\verilog\out\spec_code_retrieval_benchmark\questions_all.jsonl`
- Ranking modes: current propagation, base lexical, degree-normalized propagation

## Overall

| Variant | Mode | spec hit@5 | code hit@5 | joint hit@5 | joint hit@10 | joint MRR |
|---|---|---:|---:|---:|---:|---:|
| code-only | current | 0.0 | 0.1267 | 0.0 | 0.0 | 0.0 |
| code-only | base | 0.0 | 0.5533 | 0.0 | 0.0 | 0.0 |
| code-only | degree_norm | 0.0 | 0.22 | 0.0 | 0.0 | 0.0 |
| spec-code | current | 0.8933 | 0.3 | 0.2533 | 0.3867 | 0.1132 |
| spec-code | base | 0.7467 | 0.2467 | 0.0533 | 0.1267 | 0.0383 |
| spec-code | degree_norm | 1.0 | 0.0 | 0.0 | 0.04 | 0.0314 |

## Code Gold Coverage

| Variant | gold code nodes | missing paths | missing exact nodes |
|---|---:|---:|---:|
| code-only | 150 | 0 | 0 |
| spec-code | 150 | 0 | 0 |

## Top Code-Only Hubs

| Label | File type | Degree | Source file |
|---|---|---:|---|
| `.ok()` | code | 1852 | `opentitan\sw\host\opentitanlib\src\transport\mod.rs` |
| `.exit()` | code | 963 | `opentitan\util\dvsim\StatusPrinter.py` |
| `.len()` | code | 915 | `opentitan\sw\host\ot_certs\src\asn1\codegen.rs` |
| `tohost_exit()` | code | 748 | `ibex\vendor\riscv-tests\benchmarks\common\syscalls.c` |
| `Format` | code | 737 | `opentitan\sw\host\opentitantool\src\command\ownership.rs` |
| `.append()` | code | 619 | `opentitan\hw\vendor\lowrisc_ibex\dv\formal\conductor.py` |
| `.write()` | code | 593 | `opentitan\sw\host\penetrationtests\python\util\targets.py` |
| `.range()` | code | 542 | `opentitan\sw\host\ot_certs\src\template\mod.rs` |
| `.check()` | code | 510 | `opentitan\util\validate_testplans.py` |
| `.new()` | code | 495 | `opentitan\sw\host\tests\xmodem\xmodem.rs` |
