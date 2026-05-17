# Graphify to OpenKB Bridge

This folder contains a compact Graphify-derived spec wiki prepared as lower-token OpenKB input.

## What Was Built

- Source graph: `dbs/graphify-out/spec-only-graphify/graph.json`
- OpenKB-ready KB: `dbs/graphify-out/kb-variants/spec-graphify-wiki/kb`
- Raw Markdown input: `dbs/graphify-out/kb-variants/spec-graphify-wiki/kb/raw`
- HTML preview: `dbs/graphify-out/graphify-openkb-bridge/graphify_derived_spec_wiki.html`

## Exported Pages

- Total Markdown pages: 107
- Component pages: 60
- Topic pages: 16
- Document map pages: 30
- Index page: 1

The exported Markdown pages preserve Graphify node ids, component names, topic names, source files, source locations, and community ids so OpenKB can curate already-structured knowledge instead of reading the full raw spec corpus.

## OpenKB Trial Status

A three-page OpenKB indexing trial was attempted with:

- `00_graphify_spec_wiki_index.md`
- `rv_core_ibex.md`
- `testplan.md`

The trial hit the current OpenAI account rate limit for `gpt-5.4-mini`:

- RPM limit observed: 3 requests per minute
- TPM limit previously observed: 10000 tokens per minute

OpenKB copied the three pages into its `sources` area, but summary/concept generation did not complete. Current status for the new KB is:

- sources: 3
- summaries: 0
- concepts: 0

## Recommended Next Step

Do not run the full 107-page OpenKB import until rate limits are raised or a slower throttled ingestion wrapper is added. The compact wiki itself is ready and can be inspected through the HTML preview without additional token cost.
