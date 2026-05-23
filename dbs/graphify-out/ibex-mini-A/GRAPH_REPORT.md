# Graph Report - D:\MyWork\verilog\out\ibex_mini_docs  (2026-05-23)

## Corpus Check
- Spec-only graph built deterministically from exported spec documents; no LLM/OpenKB ingest was run.

## Summary
- 18 nodes · 26 edges · 3 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_componentinstruction_fetch, topicmemory, instruction_fetch.rst|component:instruction_fetch, topic:memory, instruction_fetch.rst]]
- [[_COMMUNITY_instruction_fetch_rstroot, pipeline_details_rstroot, projectinstruction_fetch_rst|instruction_fetch_rst/root, pipeline_details_rst/root, project:instruction_fetch_rst]]
- [[_COMMUNITY_componentpipeline_details, pipeline_details.rst, Third Pipeline Stage|component:pipeline_details, pipeline_details.rst, Third Pipeline Stage]]

## God Nodes (most connected - your core abstractions)
1. `component:instruction_fetch` - 6 edges
2. `component:pipeline_details` - 4 edges
3. `Instruction-Side Memory Interface` - 3 edges
4. `Spec Documents Corpus` - 2 edges
5. `project:instruction_fetch_rst` - 2 edges
6. `instruction_fetch_rst/root` - 2 edges
7. `topic:memory` - 2 edges
8. `Instruction Fetch` - 2 edges
9. `Branch Prediction` - 2 edges
10. `Misaligned Accesses` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Instruction Fetch` --references_component--> `component:instruction_fetch`  [EXTRACTED]
  instruction_fetch.rst → __graphify_spec_only__/components.md
- `Branch Prediction` --references_component--> `component:instruction_fetch`  [EXTRACTED]
  instruction_fetch.rst → __graphify_spec_only__/components.md
- `Misaligned Accesses` --references_component--> `component:instruction_fetch`  [EXTRACTED]
  instruction_fetch.rst → __graphify_spec_only__/components.md
- `Protocol` --references_component--> `component:instruction_fetch`  [EXTRACTED]
  instruction_fetch.rst → __graphify_spec_only__/components.md
- `Instruction-Side Memory Interface` --references_component--> `component:instruction_fetch`  [EXTRACTED]
  instruction_fetch.rst → __graphify_spec_only__/components.md

## Communities

### Community 0 - "component:instruction_fetch, topic:memory, instruction_fetch.rst"
Cohesion: 0.46
Nodes (7): component:instruction_fetch, Branch Prediction, Instruction Fetch, Instruction-Side Memory Interface, Misaligned Accesses, Protocol, topic:memory

### Community 1 - "instruction_fetch_rst/root, pipeline_details_rst/root, project:instruction_fetch_rst"
Cohesion: 0.4
Nodes (5): instruction_fetch_rst/root, pipeline_details_rst/root, project:instruction_fetch_rst, project:pipeline_details_rst, Spec Documents Corpus

### Community 2 - "component:pipeline_details, pipeline_details.rst, Third Pipeline Stage"
Cohesion: 0.7
Nodes (4): component:pipeline_details, Third Pipeline Stage, Multi- and Single-Cycle Instructions, Pipeline Details

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `instruction_fetch_rst/root` connect `instruction_fetch_rst/root, pipeline_details_rst/root, project:instruction_fetch_rst` to `component:instruction_fetch, topic:memory, instruction_fetch.rst`?**
  _High betweenness centrality (0.529) - this node is a cross-community bridge._