# Graph Report - D:\MyWork\verilog\out\ibex_openkb_raw\wiki  (2026-05-23)

## Corpus Check
- Spec-only graph built deterministically from exported spec documents; no LLM/OpenKB ingest was run.

## Summary
- 77 nodes · 187 edges · 7 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_componentagents, componentlog, AGENTS|component:agents, component:log, AGENTS.md]]
- [[_COMMUNITY_projectconcepts, projectsources, agents_mdroot|project:concepts, project:sources, agents_md/root]]
- [[_COMMUNITY_componentfetch, componentinstruction, componentpipeline|component:fetch, component:instruction, component:pipeline]]
- [[_COMMUNITY_componentmemory, componentprotocol, topicmemory|component:memory, component:protocol, topic:memory]]
- [[_COMMUNITY_componentbranch, componentprediction, componentinstruction_fetch|component:branch, component:prediction, component:instruction_fetch]]
- [[_COMMUNITY_componentpipeline_details, projectsummaries, summariesinstruction_fetch|component:pipeline_details, project:summaries, summaries/instruction_fetch.md]]
- [[_COMMUNITY_index_mdroot, projectindex_md, index|index_md/root, project:index_md, index.md]]

## God Nodes (most connected - your core abstractions)
1. `component:fetch` - 15 edges
2. `component:instruction` - 15 edges
3. `component:memory` - 15 edges
4. `component:protocol` - 13 edges
5. `component:pipeline` - 12 edges
6. `component:branch` - 11 edges
7. `component:prediction` - 9 edges
8. `component:agents` - 8 edges
9. `component:instruction_fetch` - 8 edges
10. `component:pipeline_details` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Wiki Schema` --references_component--> `component:agents`  [EXTRACTED]
  AGENTS.md → __graphify_spec_only__/components.md
- `Directory Structure` --references_component--> `component:agents`  [EXTRACTED]
  AGENTS.md → __graphify_spec_only__/components.md
- `Special Files` --references_component--> `component:agents`  [EXTRACTED]
  AGENTS.md → __graphify_spec_only__/components.md
- `Page Types` --references_component--> `component:agents`  [EXTRACTED]
  AGENTS.md → __graphify_spec_only__/components.md
- `Index Page Format` --references_component--> `component:agents`  [EXTRACTED]
  AGENTS.md → __graphify_spec_only__/components.md

## Communities

### Community 0 - "component:agents, component:log, AGENTS.md"
Cohesion: 0.25
Nodes (12): component:agents, component:log, Special Files, Page Types, Wiki Schema, Index Page Format, Log Format, Format (+4 more)

### Community 1 - "project:concepts, project:sources, agents_md/root"
Cohesion: 0.17
Nodes (12): agents_md/root, concepts/branch-prediction.md, concepts/instruction-fetch-pipeline.md, concepts/memory-interface-protocol.md, log_md/root, sources/instruction_fetch.md, sources/pipeline_details.md, project:agents_md (+4 more)

### Community 2 - "component:fetch, component:instruction, component:pipeline"
Cohesion: 0.52
Nodes (10): component:fetch, component:instruction, component:pipeline, Instruction Flow and Buffering, Instruction Handling, Instruction Caching, Branch Prediction, Instruction-Side Memory Interface (+2 more)

### Community 3 - "component:memory, component:protocol, topic:memory"
Cohesion: 0.42
Nodes (11): component:memory, component:protocol, Interface Overview, Protocol Similarity, Instruction Fetch Interface, Key Signals, Alignment Handling, External Alignment (+3 more)

### Community 4 - "component:branch, component:prediction, component:instruction_fetch"
Cohesion: 0.42
Nodes (8): component:branch, component:instruction_fetch, component:prediction, Mechanism and Goal, Mis-prediction Penalty, Status, Branch Prediction, Related Concepts

### Community 5 - "component:pipeline_details, project:summaries, summaries/instruction_fetch.md"
Cohesion: 0.33
Nodes (8): summaries/instruction_fetch.md, summaries/pipeline_details.md, component:pipeline_details, project:summaries, Pipeline Stages, Performance and Stalls, Instruction Stall Characteristics, Ibex Pipeline Details

### Community 6 - "index_md/root, project:index_md, index.md"
Cohesion: 0.29
Nodes (6): index_md/root, project:index_md, Explorations, Knowledge Base Index, Documents, Concepts

## Knowledge Gaps
- **4 isolated node(s):** `Knowledge Base Index`, `Documents`, `Concepts`, `Explorations`
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `component:instruction_fetch` connect `component:branch, component:prediction, component:instruction_fetch` to `component:agents, component:log, AGENTS.md`, `component:fetch, component:instruction, component:pipeline`, `component:memory, component:protocol, topic:memory`, `index_md/root, project:index_md, index.md`?**
  _High betweenness centrality (0.231) - this node is a cross-community bridge._
- **Why does `component:pipeline_details` connect `component:pipeline_details, project:summaries, summaries/instruction_fetch.md` to `component:agents, component:log, AGENTS.md`, `component:fetch, component:instruction, component:pipeline`, `index_md/root, project:index_md, index.md`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **What connects `Knowledge Base Index`, `Documents`, `Concepts` to the rest of the system?**
  _4 weakly-connected nodes found - possible documentation gaps or missing edges._