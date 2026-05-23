---
doc_type: short
full_text: sources/0002_requirements_e3923399fe.md
---

# Summary: ibex/doc/requirements.txt

This document is a minimal dependency list for building the **ibex** documentation environment.

## Key contents

The requirements specify the following Python packages:

- `setuptools_scm`
- `sphinx>=7.0`
- `sphinx_rtd_theme`
- `sphinxcontrib-wavedrom`
- `wavedrom>=1.9.0rc1`
- `jinja2 == 3.0.3`

## Main purpose

The file appears to define the tooling needed for documentation generation, especially:

- **Sphinx-based documentation** via `sphinx`
- **Read the Docs styling** via `sphinx_rtd_theme`
- **WaveDrom rendering support** via `sphinxcontrib-wavedrom` and `wavedrom`
- **Build/version integration** via `setuptools_scm`
- **Template rendering support** via `jinja2`

## Notable observations

- The dependency set is compact and focused on docs generation rather than runtime software.
- `sphinx>=7.0` indicates a relatively modern Sphinx build target.
- `jinja2` is pinned exactly to `3.0.3`, suggesting compatibility sensitivity.
- `wavedrom>=1.9.0rc1` suggests the documentation includes timing diagrams or other waveform-style visuals.

## Related concepts

This document relates to broader topics such as [[concepts/sphinx-documentation]] and [[concepts/build-tooling]] if those concept pages are created later.

## Bottom line

`ibex/doc/requirements.txt` defines the exact Python dependencies needed to build and style the ibex documentation, including Sphinx and WaveDrom support.

## Related Concepts
- [[concepts/embedded-processors]]
- [[concepts/open-source-hardware]]
- [[concepts/risc-v]]
