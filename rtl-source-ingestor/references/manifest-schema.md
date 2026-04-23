# Manifest Schema

## Top-level fields
- `repo`: name, url, ref, commit, license
- `snapshot_root`: absolute or workspace-local root
- `files`: list of rtl source files with path and language
- `compile_context`: filelists, include_dirs, defines, top_candidates
- `warnings`: unresolved or repo-specific caveats

## Notes
Keep all paths relative to repo root where possible. Preserve unresolved macros and missing tops in warnings.
