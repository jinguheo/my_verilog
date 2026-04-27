#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/_common.sh"
assert_command docker "Install Docker Engine"

assert_path "$SCHEMA_ROOT/postgres_schema.sql"            "Postgres base schema"
assert_path "$SCHEMA_ROOT/postgres_ontology_extension.sql" "Postgres ontology extension"

docker exec -i verilog-postgres psql -U postgres -d verilog \
    < "$SCHEMA_ROOT/postgres_schema.sql"
docker exec -i verilog-postgres psql -U postgres -d verilog \
    < "$SCHEMA_ROOT/postgres_ontology_extension.sql"
docker exec -i verilog-postgres psql -U postgres -d verilog \
    < "$SCHEMA_ROOT/kg_version_schema.sql"

ok "Postgres 스키마 로드 완료 (base + ontology + kg_version)"
