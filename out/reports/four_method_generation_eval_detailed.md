# Four-Method Verilog Generation Evaluation

Generated: 2026-05-09T20:55:03

## Scope

This report separates two different results:

1. Direct functional Verilog harness: existing candidates are canonical RTL, so the 150/150 PASS result validates the simulator/testbench path only.
2. Hard generation context readiness: 77 difficult generation prompts evaluate whether each method retrieves the correct source RTL context before generation.

## Direct Functional Harness

- Candidate source: canonical/oracle RTL
- Problems: 150
- PASS: 150
- Pass rate: 1.0000

## Hard Generation Context Readiness

Questions: 77

| Method | hit@1 | hit@3 | hit@5 | MRR | Status counts |
|---|---:|---:|---:|---:|---|
| 1. Parser + LSP | 0.9481 | 1.0000 | 1.0000 | 0.9675 | HIT@1=73, HIT@3=4 |
| 2. Parser + LSP + Manticore | 0.8312 | 0.8961 | 0.9481 | 0.8645 | HIT@1=64, HIT@3=5, HIT@5=4, MISS=4 |
| 3. KG | 0.9481 | 0.9870 | 1.0000 | 0.9658 | HIT@1=73, HIT@3=3, HIT@5=1 |
| 4. Graphify | 0.9740 | 0.9740 | 0.9740 | 0.9740 | HIT@1=75, MISS=2 |

## By Level

### 1. Parser + LSP

| Level | Count | hit@1 | hit@3 | MRR |
|---|---:|---:|---:|---:|
| L3 | 26 | 1.0000 | 1.0000 | 1.0000 |
| L4 | 26 | 0.8846 | 1.0000 | 0.9295 |
| L5 | 25 | 0.9600 | 1.0000 | 0.9733 |

### 2. Parser + LSP + Manticore

| Level | Count | hit@1 | hit@3 | MRR |
|---|---:|---:|---:|---:|
| L3 | 26 | 1.0000 | 1.0000 | 1.0000 |
| L4 | 26 | 0.6923 | 0.8077 | 0.7654 |
| L5 | 25 | 0.8000 | 0.8800 | 0.8267 |

### 3. KG

| Level | Count | hit@1 | hit@3 | MRR |
|---|---:|---:|---:|---:|
| L3 | 26 | 1.0000 | 1.0000 | 1.0000 |
| L4 | 26 | 0.8462 | 0.9615 | 0.8987 |
| L5 | 25 | 1.0000 | 1.0000 | 1.0000 |

### 4. Graphify

| Level | Count | hit@1 | hit@3 | MRR |
|---|---:|---:|---:|---:|
| L3 | 26 | 1.0000 | 1.0000 | 1.0000 |
| L4 | 26 | 0.9615 | 0.9615 | 0.9615 |
| L5 | 25 | 0.9600 | 0.9600 | 0.9600 |

## Representative Misses

### 1. Parser + LSP

No misses in top-5.

### 2. Parser + LSP + Manticore

- genctx_021_pwrmgr: gold=pwrmgr, top1=prim_esc_receiver
- genctx_023_clkmgr: gold=clkmgr, top1=prim_clock_div
- genctx_024_clkmgr: gold=clkmgr, top1=clkmgr_reg_top
- genctx_054_clkmgr: gold=clkmgr, top1=clkmgr_clk_status

### 3. KG

No misses in top-5.

### 4. Graphify

- existing_070: gold=aes_dom_inverse_gf2p8, top1=Extension
- existing_075: gold=aes_dom_inverse_gf2p4, top1=# NOTE: This list is likely to become out of date as the codebase evolves

## Interpretation

- Graphify has the best hit@1 on the hard context benchmark.
- Parser + LSP and KG are close and both reach 100% hit@5, which is strong for compact generation context packing.
- Manticore Parser/LSP is weaker on L4/L5 generation prompts and needs generation-specific field weighting.
- The direct Verilog pass rate is not a method comparison until real generated RTL candidates replace canonical candidates.
