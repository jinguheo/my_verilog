-- KG version tracking table (append to existing Postgres schema)

CREATE TABLE IF NOT EXISTS kg_versions (
  version_id    BIGSERIAL PRIMARY KEY,
  version_tag   TEXT NOT NULL UNIQUE,          -- e.g. "v001"
  created_at    TIMESTAMP DEFAULT now(),
  modules_total INT,
  labels_total  INT,
  edges_total   INT,
  approved_added   INT DEFAULT 0,
  rejected_added   INT DEFAULT 0,
  decisions_file   TEXT,
  notes            TEXT,
  status           TEXT NOT NULL DEFAULT 'active'  -- active | archived
);

-- track which label assertions belong to which KG version
ALTER TABLE ontology_assertions
  ADD COLUMN IF NOT EXISTS kg_version_tag TEXT;

CREATE INDEX IF NOT EXISTS idx_kg_versions_tag ON kg_versions(version_tag);
CREATE INDEX IF NOT EXISTS idx_assertions_version ON ontology_assertions(kg_version_tag);
