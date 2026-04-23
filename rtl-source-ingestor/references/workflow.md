# Ingest Workflow

1. Resolve repository ref to an immutable commit.
2. Enumerate source files and detect language extensions.
3. Search filelists and build scripts before guessing compile context.
4. Collect include directories and macro definitions.
5. Emit a manifest even when context is partial.
