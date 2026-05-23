# Graph Report - D:\MyWork\verilog\out\ibex_graphify_openkb\kb\wiki  (2026-05-23)

## Corpus Check
- Spec-only graph built deterministically from exported spec documents; no LLM/OpenKB ingest was run.

## Summary
- 191 nodes · 524 edges · 10 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_componentinstruction, componentfetch, componentprotocol|component:instruction, component:fetch, component:protocol]]
- [[_COMMUNITY_componentmemory, topicmemory, componentside|component:memory, topic:memory, component:side]]
- [[_COMMUNITY_componentpipeline_details_rst, componentpipeline, componentstages|component:pipeline_details_rst, component:pipeline, component:stages]]
- [[_COMMUNITY_componentinstruction_fetch, componentanchors, componentknowledge|component:instruction_fetch, component:anchors, component:knowledge]]
- [[_COMMUNITY_projectconcepts, projectsources, conceptsbranch-prediction|project:concepts, project:sources, concepts/branch-prediction.md]]
- [[_COMMUNITY_component00_graphify_spec_wiki_index, projectsummaries, summaries00_graphify_spec_wiki_index|component:00_graphify_spec_wiki_index, project:summaries, summaries/00_graphify_spec_wiki_index.md]]
- [[_COMMUNITY_componentbranch, componentprediction, branch-prediction|component:branch, component:prediction, branch-prediction.md]]
- [[_COMMUNITY_componentpipeline_details, summariespipeline_details.md, pipeline_details|component:pipeline_details, summaries/pipeline_details.md, pipeline_details.md]]
- [[_COMMUNITY_componentinstruction_fetch_rst, instruction_fetch_rst.md, Instruction-Side Memory Interface|component:instruction_fetch_rst, instruction_fetch_rst.md, Instruction-Side Memory Interface]]
- [[_COMMUNITY_componentlog, log_mdroot, projectlog_md|component:log, log_md/root, project:log_md]]

## God Nodes (most connected - your core abstractions)
1. `component:instruction` - 38 edges
2. `component:memory` - 32 edges
3. `component:fetch` - 31 edges
4. `component:instruction_fetch_rst` - 24 edges
5. `component:instruction_fetch` - 19 edges
6. `component:protocol` - 19 edges
7. `component:branch` - 18 edges
8. `component:prediction` - 18 edges
9. `topic:memory` - 18 edges
10. `component:pipeline_details_rst` - 17 edges

## Surprising Connections (you probably didn't know these)
- `Document: instruction fetch.rst` --references_component--> `component:instruction_fetch_rst`  [EXTRACTED]
  sources/instruction_fetch_rst.md → __graphify_spec_only__/components.md
- `Source` --references_component--> `component:instruction_fetch_rst`  [EXTRACTED]
  sources/instruction_fetch_rst.md → __graphify_spec_only__/components.md
- `Sections` --references_component--> `component:instruction_fetch_rst`  [EXTRACTED]
  sources/instruction_fetch_rst.md → __graphify_spec_only__/components.md
- `OpenKB Curation Hints` --references_component--> `component:instruction_fetch_rst`  [EXTRACTED]
  sources/instruction_fetch_rst.md → __graphify_spec_only__/components.md
- `Graphify-derived Spec Wiki` --references_component--> `component:00_graphify_spec_wiki_index`  [EXTRACTED]
  sources/00_graphify_spec_wiki_index.md → __graphify_spec_only__/components.md

## Communities

### Community 0 - "component:instruction, component:fetch, component:protocol"
Cohesion: 0.16
Nodes (33): component:accesses, component:fetch, component:instruction, component:misaligned, component:protocol, Overview, Pipeline Context, Pipeline Details (+25 more)

### Community 1 - "component:memory, topic:memory, component:side"
Cohesion: 0.18
Nodes (23): component:memory, component:side, component:topic, Role in Instruction Fetching, Context, Related Concepts, Instruction-Side Memory Interface, Definition (+15 more)

### Community 2 - "component:pipeline_details_rst, component:pipeline, component:stages"
Cohesion: 0.16
Nodes (20): component:pipeline, component:pipeline_details_rst, component:stages, Overview, Specific Stages, Instruction Handling, Pipeline Stages, Concepts (+12 more)

### Community 3 - "component:instruction_fetch, component:anchors, component:knowledge"
Cohesion: 0.21
Nodes (17): component:anchors, component:instruction_fetch, component:knowledge, Purpose, Application in Curation, Related Documents, Knowledge Anchors and Entities, Referencing Documents (+9 more)

### Community 4 - "project:concepts, project:sources, concepts/branch-prediction.md"
Cohesion: 0.11
Nodes (19): concepts/branch-prediction.md, concepts/instruction-fetch.md, concepts/instruction-side-memory-interface.md, concepts/knowledge-anchors.md, concepts/misaligned-accesses.md, concepts/pipeline-stages----Pipeline-Stages.md, concepts/protocol-instruction-fetch.md, concepts/topic-memory.md (+11 more)

### Community 5 - "component:00_graphify_spec_wiki_index, project:summaries, summaries/00_graphify_spec_wiki_index.md"
Cohesion: 0.19
Nodes (13): summaries/00_graphify_spec_wiki_index.md, summaries/instruction_fetch.md, summaries/instruction_fetch_rst.md, summaries/memory.md, summaries/pipeline_details_rst.md, component:00_graphify_spec_wiki_index, project:summaries, Strategy (+5 more)

### Community 6 - "component:branch, component:prediction, branch-prediction.md"
Cohesion: 0.41
Nodes (12): component:branch, component:prediction, Overview, Key Topics, Instruction Fetch, Branch Prediction, Instruction-Side Memory Interface, Misaligned Accesses (+4 more)

### Community 7 - "component:pipeline_details, summaries/pipeline_details.md, pipeline_details.md"
Cohesion: 0.27
Nodes (11): summaries/pipeline_details.md, component:pipeline_details, Referencing Documents, Referencing Sections, OpenKB Curation Hints, Component: pipeline details, OpenKB Purpose, Graphify Identity (+3 more)

### Community 8 - "component:instruction_fetch_rst, instruction_fetch_rst.md, Instruction-Side Memory Interface"
Cohesion: 0.32
Nodes (11): component:instruction_fetch_rst, Overview, Key Topics, Instruction Fetch, Branch Prediction, Instruction-Side Memory Interface, Misaligned Accesses, Protocol (+3 more)

### Community 9 - "component:log, log_md/root, project:log_md"
Cohesion: 0.31
Nodes (10): log_md/root, component:log, project:log_md, 2026-05-23 16:38:41 ingest | pipeline details rst.md, 2026-05-23 16:39:12 ingest | memory.md, Operations Log, 2026-05-23 16:36:00 ingest | 00 graphify spec wiki index.md, 2026-05-23 16:36:28 ingest | instruction fetch.md (+2 more)

## Knowledge Gaps
- **4 isolated node(s):** `Knowledge Base Index`, `Documents`, `Concepts`, `Explorations`
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `component:memory` connect `component:memory, topic:memory, component:side` to `component:instruction, component:fetch, component:protocol`, `component:pipeline_details_rst, component:pipeline, component:stages`, `component:branch, component:prediction, branch-prediction.md`, `component:instruction_fetch_rst, instruction_fetch_rst.md, Instruction-Side Memory Interface`, `component:log, log_md/root, project:log_md`?**
  _High betweenness centrality (0.144) - this node is a cross-community bridge._
- **Why does `component:instruction` connect `component:instruction, component:fetch, component:protocol` to `component:memory, topic:memory, component:side`, `component:pipeline_details_rst, component:pipeline, component:stages`, `component:instruction_fetch, component:anchors, component:knowledge`, `component:branch, component:prediction, branch-prediction.md`, `component:instruction_fetch_rst, instruction_fetch_rst.md, Instruction-Side Memory Interface`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._
- **Why does `component:instruction_fetch_rst` connect `component:instruction_fetch_rst, instruction_fetch_rst.md, Instruction-Side Memory Interface` to `component:instruction, component:fetch, component:protocol`, `component:memory, topic:memory, component:side`, `component:pipeline_details_rst, component:pipeline, component:stages`, `component:instruction_fetch, component:anchors, component:knowledge`, `component:branch, component:prediction, branch-prediction.md`, `component:log, log_md/root, project:log_md`?**
  _High betweenness centrality (0.094) - this node is a cross-community bridge._
- **What connects `Knowledge Base Index`, `Documents`, `Concepts` to the rest of the system?**
  _4 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `project:concepts, project:sources, concepts/branch-prediction.md` be split into smaller, more focused modules?**
  _Cohesion score 0.11 - nodes in this community are weakly interconnected._