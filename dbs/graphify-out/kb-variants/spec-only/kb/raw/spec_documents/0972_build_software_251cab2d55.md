# Spec Document: opentitan/sw/doc/build_software.md

- Project: `opentitan`
- Original source: `D:\MyWork\verilog\dbs\opentitan\sw\doc\build_software.md`
- Exported path: `D:\MyWork\verilog\out\spec_documents_20260514_204108\opentitan\sw\doc\build_software.md`
- Original extension: `.md`
- Original bytes: 505

## Content

# OpenTitan Software Build Instructions

All OpenTitan software is built with [Bazel](https://bazel.build/).

For example, to build and run the OpenTitan UART smoke test located in `sw/device/tests/` for Verilator, run

```console
cd "$REPO_TOP"
bazel test --test_output=streamed //sw/device/tests:uart_smoketest_sim_verilator
```

The resulting binaries will be located under `bazel-out/`. For more information, check out [the Building Software guide](../../doc/getting_started/build_sw.md).
