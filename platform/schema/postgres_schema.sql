CREATE TABLE IF NOT EXISTS ingest_runs (
  ingest_run_id BIGSERIAL PRIMARY KEY,
  source_name TEXT NOT NULL,
  source_root TEXT NOT NULL,
  started_at TIMESTAMP DEFAULT now(),
  finished_at TIMESTAMP,
  status TEXT NOT NULL DEFAULT 'started',
  notes TEXT
);

CREATE TABLE IF NOT EXISTS repos (
  repo_id BIGSERIAL PRIMARY KEY,
  repo_name TEXT NOT NULL UNIQUE,
  repo_url TEXT,
  license TEXT,
  category TEXT[]
);

CREATE TABLE IF NOT EXISTS repo_versions (
  repo_version_id BIGSERIAL PRIMARY KEY,
  repo_id BIGINT REFERENCES repos(repo_id),
  version_ref TEXT NOT NULL,
  commit_hash TEXT,
  created_at TIMESTAMP DEFAULT now(),
  UNIQUE(repo_id, version_ref)
);

CREATE TABLE IF NOT EXISTS files (
  file_id BIGSERIAL PRIMARY KEY,
  repo_version_id BIGINT REFERENCES repo_versions(repo_version_id),
  file_path TEXT NOT NULL,
  language TEXT NOT NULL,
  checksum TEXT,
  UNIQUE(repo_version_id, file_path)
);

CREATE TABLE IF NOT EXISTS modules (
  module_id BIGSERIAL PRIMARY KEY,
  file_id BIGINT REFERENCES files(file_id),
  module_name TEXT NOT NULL,
  summary_short TEXT,
  summary_long TEXT,
  synthesizable BOOLEAN,
  testbench_only BOOLEAN DEFAULT FALSE,
  parameterized BOOLEAN DEFAULT FALSE,
  source_project TEXT,
  UNIQUE(file_id, module_name)
);

CREATE TABLE IF NOT EXISTS ports (
  port_id BIGSERIAL PRIMARY KEY,
  module_id BIGINT REFERENCES modules(module_id),
  direction TEXT NOT NULL,
  port_name TEXT NOT NULL,
  width_expr TEXT,
  UNIQUE(module_id, port_name)
);

CREATE TABLE IF NOT EXISTS instances (
  instance_id BIGSERIAL PRIMARY KEY,
  module_id BIGINT REFERENCES modules(module_id),
  child_module_type TEXT NOT NULL,
  instance_name TEXT NOT NULL,
  UNIQUE(module_id, instance_name)
);

CREATE TABLE IF NOT EXISTS semantic_labels (
  label_id BIGSERIAL PRIMARY KEY,
  label_key TEXT NOT NULL UNIQUE,
  label_group TEXT NOT NULL,
  description TEXT
);

CREATE TABLE IF NOT EXISTS module_labels (
  module_id BIGINT REFERENCES modules(module_id),
  label_id BIGINT REFERENCES semantic_labels(label_id),
  source TEXT NOT NULL,
  confidence NUMERIC(4,3),
  evidence JSONB,
  review_status TEXT DEFAULT 'proposed',
  PRIMARY KEY(module_id, label_id, source)
);

CREATE INDEX IF NOT EXISTS idx_modules_name ON modules(module_name);
CREATE INDEX IF NOT EXISTS idx_ports_name ON ports(port_name);
CREATE INDEX IF NOT EXISTS idx_instances_child_type ON instances(child_module_type);
