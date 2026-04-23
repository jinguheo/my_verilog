CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS ontology_entities (
  entity_id BIGSERIAL PRIMARY KEY,
  entity_key TEXT NOT NULL UNIQUE,
  project TEXT NOT NULL,
  entity_type TEXT NOT NULL,
  name TEXT NOT NULL,
  file_path TEXT,
  version_ref TEXT,
  summary TEXT,
  canonical_status TEXT DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS ontology_labels (
  ontology_label_id BIGSERIAL PRIMARY KEY,
  label_key TEXT NOT NULL UNIQUE,
  label_group TEXT NOT NULL,
  canonical_label_key TEXT,
  description TEXT,
  state TEXT NOT NULL DEFAULT 'approved'
);

CREATE TABLE IF NOT EXISTS ontology_assertions (
  assertion_id BIGSERIAL PRIMARY KEY,
  entity_id BIGINT REFERENCES ontology_entities(entity_id),
  ontology_label_id BIGINT REFERENCES ontology_labels(ontology_label_id),
  source_kind TEXT NOT NULL,
  confidence NUMERIC(4,3),
  review_state TEXT NOT NULL DEFAULT 'proposed',
  created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE IF NOT EXISTS ontology_evidence (
  evidence_id BIGSERIAL PRIMARY KEY,
  assertion_id BIGINT REFERENCES ontology_assertions(assertion_id),
  source_path TEXT NOT NULL,
  line_start INT,
  line_end INT,
  extract_text TEXT,
  created_by TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ontology_review_queue (
  review_item_id BIGSERIAL PRIMARY KEY,
  entity_key TEXT NOT NULL,
  proposed_label TEXT NOT NULL,
  reason TEXT,
  confidence NUMERIC(4,3),
  state TEXT NOT NULL DEFAULT 'proposed',
  assignee TEXT,
  created_at TIMESTAMP DEFAULT now(),
  resolved_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS module_embeddings (
  embedding_id BIGSERIAL PRIMARY KEY,
  entity_key TEXT NOT NULL,
  embedding_source TEXT NOT NULL,
  embedding vector(1536),
  summary TEXT,
  created_at TIMESTAMP DEFAULT now()
);
