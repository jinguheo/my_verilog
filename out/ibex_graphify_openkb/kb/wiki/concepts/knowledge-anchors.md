---
sources: [summaries/instruction_fetch_rst.md, summaries/instruction_fetch.md]
brief: Knowledge anchors define curated views of information used as anchors for OpenKB processing and source curation.
---

# Knowledge Anchors and Entities

Knowledge Anchors and Entities are core mechanisms used to define specific, curated views of information candidates within the knowledge base, serving as anchors for OpenKB processing.

These anchors allow for the creation of compact, high-confidence views—often derived from graph structures—that serve as effective input for systems like OpenKB, rather than raw source material.

## Purpose

The primary goal of establishing knowledge anchors is to distill complex source documents into actionable, low-token representations that provide context for downstream knowledge graph or reasoning tasks.

## Application in Curation

When curating documents, anchors help define how a source entity should be treated:

*   **Entity Anchoring:** Treating a specific piece of data or code as a fixed point for reference.
*   **Curation Hints:** Using linked sections from the source as evidence for requirements, verification topics, and integration constraints.

For example, a specific entry like `component_instruction_fetch` acts as an anchor, providing identity (Node ID, Role, Confidence Score) and curation guidance.

This application is crucial when processing technical specifications. For instance, a document like [[summaries/instruction_fetch]] uses sections to map specific points within the original specification corpus, demonstrating how anchors are used to guide the ingestion and processing of source documents, ensuring the knowledge base utilizes high-quality, anchored information rather than relying solely on raw text.

[[summaries/instruction_fetch]]

## Related Documents
- [[summaries/instruction_fetch_rst]]
