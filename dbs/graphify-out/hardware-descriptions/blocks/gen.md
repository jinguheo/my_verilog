# Hardware Description: gen

_Generated from Graphify spec-code graph. Middle layer connecting RTL/DV code to specification sections._

## Functional Summary

_No spec snippet available. Derived from bridge evidence only._

## Identity

- `ip_block`: `gen`
- `bridge_edge_count`: 40
- Spec categories: component: 41
- Code categories: dv: 25, other_code: 15
- Bridge relations: spec_component_matches_code: 40

## Spec Anchors

- `component:gen` (L1) — `__graphify_spec_only__/components.md`

## Code Evidence

**DV** (25)
  - `.gen()`:L54 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\misaligned_load_store.py`
  - `.gen()`:L63 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\straight_line_insn.py`
  - `.gen()`:L43 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\edge_load_store.py`
  - `.gen()`:L34 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_giant_loop.py`
  - `.gen()`:L50 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_load_store.py`
  - `.gen()`:L19 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\untaken_branch.py`
  - `.gen()`:L199 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_deep_loop.py`
  - `.gen()`:L50 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_zero_loop.py`
  - `.gen()`:L117 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\call_stack_rw.py`
  - `.gen()`:L194 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\call_stack_rw.py`
  - `.gen()`:L126 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_at_end.py`
  - `.gen()`:L37 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_bnmovr.py`
  - `.gen()`:L47 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\branch_gen.py`
  - `.gen()`:L30 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\known_wdr.py`
  - `.gen()`:L49 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\small_val.py`
  - `.gen()`:L42 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_insn.py`
  - `.gen()`:L51 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_ispr.py`
  - `.gen()`:L122 — `opentitan\hw\ip\otbn\dv\rig\rig\snippet_gens.py`
  - `.gen()`:L54 — `opentitan\hw\ip\otbn\dv\rig\rig\snippet_gen.py`
  - `.gen()`:L103 — `opentitan\hw\ip\otbn\dv\rig\rig\gens\branch.py`
**OTHER_CODE** (15)
  - `gen()`:L356 — `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\run.py`
  - `gen-otp-immutable-rom-ext-json.py`:L1 — `opentitan\util\design\gen-otp-immutable-rom-ext-json.py`
  - `gen-rng-health-thresholds.py`:L1 — `opentitan\util\design\gen-rng-health-thresholds.py`
  - `gen.scala`:L1 — `ibex\vendor\riscv-tests\benchmarks\mm\gen.scala`
  - `MMGen`:L2 — `ibex\vendor\riscv-tests\benchmarks\mm\gen.scala`
  - `gen-otp-rot-auth-json.py`:L1 — `opentitan\util\design\gen-otp-rot-auth-json.py`
  - `gen-lc-state-enc.py`:L1 — `opentitan\util\design\gen-lc-state-enc.py`
  - `gen.py`:L1 — `opentitan\util\autogen_testutils\gen.py`
  - `gen_testutils()`:L18 — `opentitan\util\autogen_testutils\gen.py`
  - `Generate testutils libraries that are rendered from Mako templates.      Args:`:L21 — `opentitan\util\autogen_testutils\gen.py`
  - `gen()`:L61 — `opentitan\util\design\mubi\prim_mubi.py`
  - `gen-flash-img.py`:L1 — `opentitan\util\design\gen-flash-img.py`
  - `gen-lfsr-seed.py`:L1 — `opentitan\util\design\gen-lfsr-seed.py`
  - `gen-otp-mmap.py`:L1 — `opentitan\util\design\gen-otp-mmap.py`
  - `gen-top-docs.py`:L1 — `opentitan\util\design\gen-top-docs.py`

## Direct Spec-Code Bridges

| Relation | Spec anchor | Code artifact | Code file |
|---|---|---|---|
| `spec_component_matches_code` | `component:gen` | `gen()` | `opentitan\hw\vendor\lowrisc_ibex\vendor\google_riscv-dv\run.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\misaligned_load_store.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\straight_line_insn.py` |
| `spec_component_matches_code` | `component:gen` | `gen-otp-immutable-rom-ext-json.py` | `opentitan\util\design\gen-otp-immutable-rom-ext-json.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\edge_load_store.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_giant_loop.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_load_store.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\untaken_branch.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_deep_loop.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_zero_loop.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\call_stack_rw.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\call_stack_rw.py` |
| `spec_component_matches_code` | `component:gen` | `gen-rng-health-thresholds.py` | `opentitan\util\design\gen-rng-health-thresholds.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_at_end.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_bnmovr.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\branch_gen.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\known_wdr.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\small_val.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_insn.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\bad_ispr.py` |
| `spec_component_matches_code` | `component:gen` | `gen.scala` | `ibex\vendor\riscv-tests\benchmarks\mm\gen.scala` |
| `spec_component_matches_code` | `component:gen` | `MMGen` | `ibex\vendor\riscv-tests\benchmarks\mm\gen.scala` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\snippet_gens.py` |
| `spec_component_matches_code` | `component:gen` | `gen-otp-rot-auth-json.py` | `opentitan\util\design\gen-otp-rot-auth-json.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\snippet_gen.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\branch.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\ecall.py` |
| `spec_component_matches_code` | `component:gen` | `gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\init_data.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\jump.py` |
| `spec_component_matches_code` | `component:gen` | `.gen()` | `opentitan\hw\ip\otbn\dv\rig\rig\gens\loop.py` |
| `spec_component_matches_code` | `component:gen` | `gen-binaries.py` | `opentitan\hw\ip\otbn\dv\uvm\gen-binaries.py` |
| `spec_component_matches_code` | `component:gen` | `gen-lc-state-enc.py` | `opentitan\util\design\gen-lc-state-enc.py` |
| `spec_component_matches_code` | `component:gen` | `gen.py` | `opentitan\util\autogen_testutils\gen.py` |
| `spec_component_matches_code` | `component:gen` | `gen_testutils()` | `opentitan\util\autogen_testutils\gen.py` |
| `spec_component_matches_code` | `component:gen` | `Generate testutils libraries that are rendered from Mako templates.      Args:` | `opentitan\util\autogen_testutils\gen.py` |
| `spec_component_matches_code` | `component:gen` | `gen()` | `opentitan\util\design\mubi\prim_mubi.py` |
| `spec_component_matches_code` | `component:gen` | `gen-flash-img.py` | `opentitan\util\design\gen-flash-img.py` |
| `spec_component_matches_code` | `component:gen` | `gen-lfsr-seed.py` | `opentitan\util\design\gen-lfsr-seed.py` |
| `spec_component_matches_code` | `component:gen` | `gen-otp-mmap.py` | `opentitan\util\design\gen-otp-mmap.py` |
| `spec_component_matches_code` | `component:gen` | `gen-top-docs.py` | `opentitan\util\design\gen-top-docs.py` |

## Retrieval Guidance

- For code-only queries mentioning `gen`, expand toward spec anchors via this description.
- Spec Excerpts above show primary functional context — prefer these over raw file lists.
- Bridge table maps the exact spec ↔ code correspondences found by Graphify.
- Neighbor components listed above share code-level relationships with `gen`.
