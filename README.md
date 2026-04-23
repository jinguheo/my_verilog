# Verilog RTL Ontology Workspace

This workspace builds a small ontology-first knowledge layer from public RTL repositories.

Primary entry point:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step status
```

## Main Workflows

Quick review demo:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step demo
```

Generate full OpenTitan + Ibex ontology artifacts:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step seed
```

Run Docker runtime, schema load, seed generation, and Neo4j load:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\workflow.ps1 -Step full
```

## Important Paths

```text
dbs/        public RTL source repositories
platform/   executable pipeline, schema, services, and UI
out/        generated artifacts
docs/       operator-facing workflow documentation
workflow.ps1 root workflow launcher
```

## Operator Docs

- [Workflow Guide](docs/README.md)
- [Operator Checklist](docs/OPERATOR_CHECKLIST.md)
- [Workflow Map](docs/WORKFLOW_MAP.md)

## Review Console

After running `workflow.ps1 -Step demo`, open:

```text
http://localhost:8765/platform/ui/review-console/index.html
```

The console shows ontology summary, label review queue, parser/LSP vs knowledge DB search contrast, graph visualization, and module cards.
