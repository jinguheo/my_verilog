---
name: rtl-source-ingestor
description: ingest public or internal verilog and systemverilog repositories into a reproducible source snapshot and compile-context manifest. use when chatgpt needs to collect rtl sources, normalize repo state, resolve filelists, include paths, macros, and produce machine-readable ingestion outputs for downstream parsing and indexing.
---

# Overview
Create a reproducible source snapshot for downstream rtl analysis.

## Use this skill to
- clone or refresh public verilog or systemverilog repositories
- capture repo metadata, commit, tag, license, and file manifest
- discover filelists, include directories, package/import hints, and macro definitions
- emit a normalized ingest manifest for parser and indexer skills

## Inputs
Accept either natural language or structured input. Normalize into this shape before proceeding.

```json
{
  "repo_url": "https://github.com/example/project",
  "ref": "main or tag or commit",
  "allow_extensions": [".v", ".sv", ".vh", ".svh"],
  "top_hints": ["top", "soc_top"],
  "notes": "optional repo-specific hints"
}
```

## Outputs
Always return both:
1. a short markdown summary for humans
2. a machine-readable manifest json

Required manifest fields:

```json
{
  "repo": {
    "name": "project",
    "url": "...",
    "ref": "...",
    "commit": "...",
    "license": "..."
  },
  "snapshot_root": "...",
  "files": [{"path": "rtl/top.sv", "language": "systemverilog"}],
  "compile_context": {
    "filelists": [],
    "include_dirs": [],
    "defines": {},
    "top_candidates": []
  },
  "warnings": []
}
```

## Workflow
1. Resolve the exact repo ref and record commit hash.
2. Enumerate candidate rtl files and exclude obvious generated or vendored noise when possible.
3. Search for filelists, scripts, readmes, fuse/flow configs, and macro definitions.
4. Extract a compile-context manifest even if incomplete.
5. Mark uncertain items in `warnings` instead of guessing.
6. Hand off the manifest to the parser skill.

## Heuristics
- prefer explicit filelists over recursive guesses
- keep multiple compile contexts if the repo has multiple tops
- preserve unresolved macros instead of deleting affected files
- store relative paths exactly as they appear in repo metadata

## Go implementation notes
Use the reference files to scaffold a Go ingestion service. Favor a small CLI plus a reusable package.
- CLI command: `ingest-repo`
- packages: `internal/gitx`, `internal/manifest`, `internal/filelist`, `internal/license`
- emit json to stdout and optionally to disk

## Resources
- read `references/manifest-schema.md` for the canonical manifest shape
- read `references/workflow.md` for the ingest decision tree
- read `assets/go_scaffold.txt` for the suggested Go package layout
