# Integration plan

Deploy order:
1. runtime
2. ingest
3. schema
4. OpenTitan review queue
5. Ibex review queue
6. merged ontology review
7. module-qa-api
8. vector-search-api
9. generation-orchestrator
10. web-console

Short-term milestone:
- merged approved label set across OpenTitan and Ibex
- stable entity_key convention
- vector fallback restricted to approved labels only
