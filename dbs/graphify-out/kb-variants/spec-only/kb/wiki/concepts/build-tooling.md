---
sources: [summaries/0002_requirements_e3923399fe.md]
brief: Dependencies and tools used to build project documentation and assets.
---

# Build Tooling

Build tooling is the collection of dependencies and utilities used to generate, render, and package project artifacts rather than to run the project itself. In this wiki, it covers the documentation build environment and its supporting libraries.

## What it includes

From [[summaries/0002_requirements_e3923399fe]], the `ibex` documentation build setup depends on:

- `setuptools_scm` — versioning support from source control metadata
- `sphinx>=7.0` — the documentation generator
- `sphinx_rtd_theme` — the Read the Docs HTML theme
- `sphinxcontrib-wavedrom` — Sphinx integration for WaveDrom diagrams
- `wavedrom>=1.9.0rc1` — waveform/timing diagram rendering
- `jinja2 == 3.0.3` — template rendering used by the docs toolchain

## Why build tooling matters

Build tooling defines the reproducible environment needed to turn source material into published outputs. For documentation, this typically means:

- converting source text into rendered pages
- applying a consistent visual theme
- generating diagrams or other embedded assets
- handling templates and build-time metadata
- ensuring compatible tool versions are used together

## Key characteristics seen in the source

The requirements file suggests a documentation-focused toolchain with a few important traits:

- **Modern Sphinx baseline**: `sphinx>=7.0` indicates the project targets current Sphinx behavior.
- **Themed output**: `sphinx_rtd_theme` standardizes the visual presentation of the docs.
- **Diagram support**: `sphinxcontrib-wavedrom` and `wavedrom` imply the docs include waveform-style diagrams.
- **Version pinning for stability**: `jinja2 == 3.0.3` is pinned exactly, likely to avoid template compatibility issues.
- **Source-controlled versioning**: `setuptools_scm` indicates the build may derive version information automatically.

## Relationship to other concepts

Build tooling often connects to:

- [[concepts/sphinx-documentation]] — the broader Sphinx-based docs workflow
- [[concepts/documentation-workflow]] — how source docs become published output
- [[concepts/dependency-management]] — controlling versions and compatibility across tools

## Source-specific takeaway

The `ibex` requirements file is a concise example of documentation build tooling: it assembles the minimum set of packages needed to build styled, diagram-enabled documentation reliably.

See also: [[summaries/0002_requirements_e3923399fe]]