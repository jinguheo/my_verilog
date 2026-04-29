# Generation Verification

Use this flow when you need to check whether generated Verilog is actually correct, not just whether retrieval found useful context.

## What It Measures

The retrieval benchmarks answer: did KG/Graphify find the right module context?

Generation verification answers:

- Does the generated RTL parse?
- Does it compile with Icarus Verilog?
- Does the generated module pass the supplied functional testbench?
- If it fails, did it fail at candidate lookup, compile, simulation, or functional mismatch?

## Inputs

Problems are JSONL rows compatible with VerilogEval-style fields:

- `task_id` or `problem_id`
- `prompt` or `ifc`
- `canonical_solution` or `ref`
- `test` or `testbench`

Generated candidates are JSONL rows with:

- `task_id` or `problem_id`
- `completion`, `generated_code`, `code`, `rtl`, or `answer`

The candidate `task_id` must match the problem `task_id`.

The bundled L1-L5 fixture separates generation checks into smoke-level examples:

| Level | Focus |
|---|---|
| `L1` | Basic combinational generation |
| `L2` | Conditional/select logic generation |
| `L3` | Arithmetic expression generation |
| `L4` | Sequential logic with reset generation |
| `L5` | Stateful behavior generation |

## Commands

Smoke check using reference solutions:

```powershell
.\.venv-graphify\Scripts\python.exe platform\eval\run_generation_verification.py --candidate-mode reference
```

Run the L1-L5 generation benchmark with externally supplied candidates:

```powershell
.\.venv-graphify\Scripts\python.exe platform\eval\run_generation_verification.py `
  --problems platform\eval\fixtures\generation_l1_l5.jsonl `
  --candidates platform\eval\fixtures\generation_l1_l5_candidates.jsonl `
  --candidate-mode external `
  --out out\generation_eval_l1_l5
```

Build and run the 150-task realistic RTL generation benchmark:

```powershell
.\.venv-graphify\Scripts\python.exe platform\eval\build_generation_benchmark.py `
  --out-dir out\generation_benchmark

.\.venv-graphify\Scripts\python.exe platform\eval\run_generation_verification.py `
  --problems out\generation_benchmark\problems_all.jsonl `
  --candidates out\generation_benchmark\candidates_all.jsonl `
  --candidate-mode external `
  --out out\generation_eval_150
```

The 150-task benchmark covers realistic RTL patterns such as address decoders,
byte masks, priority grants, ready/valid stages, timers, sequence detectors,
packet FSMs, credit control, round-robin arbiters, skid buffers, small register
files, tiny FIFOs, APB-like CSR blocks, DMA burst controllers, PWM controllers,
watchdogs, and LFSR scramblers.

Prepare and run actual NVlabs VerilogEval generation problems by context mode:

```powershell
git clone --depth 1 https://github.com/NVlabs/verilog-eval.git tools\verilog-eval

.\.venv-graphify\Scripts\python.exe platform\eval\prepare_verilogeval_generation.py `
  --repo tools\verilog-eval `
  --task all `
  --out-dir out\verilogeval_generation

.\.venv-graphify\Scripts\python.exe platform\eval\run_verilogeval_generation_modes.py `
  --base-dir out\verilogeval_generation\code-complete-iccad2023 `
  --out-dir out\verilogeval_generation_eval\code-complete-iccad2023

.\.venv-graphify\Scripts\python.exe platform\eval\run_verilogeval_generation_modes.py `
  --base-dir out\verilogeval_generation\spec-to-rtl `
  --out-dir out\verilogeval_generation_eval\spec-to-rtl
```

The mode runner expects `candidates_parser_lsp.jsonl`, `candidates_kg.jsonl`,
and `candidates_graphify.jsonl`. The prepared files are oracle references for
harness sanity checks; replace them with real generated RTL to compare mode
quality.

The VerilogEval normalizer embeds the official `RefModule` in each testbench so
the generated `TopModule` is checked by functional comparison. It also applies a
small Icarus compatibility pass for oracle sanity checks: enum typedefs in a few
official references are lowered to localparams, and one spec-to-RTL reference
with mismatched ports is repaired from the paired code-complete reference.

The script first checks `PATH`, then falls back to `tools\iverilog\bin\iverilog.exe` and `tools\iverilog\bin\vvp.exe` when the portable simulator is present.

Evaluate generated candidates:

```powershell
.\.venv-graphify\Scripts\python.exe platform\eval\run_generation_verification.py `
  --problems path\to\verilogeval.jsonl `
  --candidates path\to\generated_candidates.jsonl `
  --candidate-mode external
```

Outputs are written under `out\generation_eval\`:

- `generation_eval_report.json`
- `generation_eval_results.csv`
- `generation_eval_summary.md`
- `work\<task_id>\combined.sv`

## Required Simulator

Functional verification requires Icarus Verilog:

- `iverilog`
- `vvp`

If they are not on `PATH`, the script still writes combined source files and runs optional tree-sitter syntax parsing when available, but each result is marked `TOOL_MISSING`.

## Status Meaning

| Status | Meaning |
|---|---|
| `PASS` | Compiled and simulated without failure markers |
| `NO_CANDIDATE` | No generated answer was provided for the problem |
| `TOOL_MISSING` | `iverilog` or `vvp` is missing |
| `COMPILE_FAIL` | Icarus Verilog rejected the design/testbench |
| `SIM_FAIL` | `vvp` exited with an error |
| `FUNCTION_FAIL` | Simulation ran, but output showed mismatches or failure markers |
| `COMPILE_TIMEOUT` / `SIM_TIMEOUT` | Tool exceeded the configured timeout |

## How This Fits the KG Work

Use the existing KG/Graphify comparison to choose retrieval context. Then feed generated RTL into this verification script. The real generation score should be reported as compile pass rate and simulation pass rate, not the current proxy retrieval score.
