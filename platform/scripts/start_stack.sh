#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/_common.sh"
assert_command docker "Install Docker Engine: https://docs.docker.com/engine/install/ubuntu/"

load_env
pushd "$RUNTIME_ROOT" > /dev/null
docker compose --env-file "$PLATFORM_DIR/.env" up -d
popd > /dev/null
ok "Stack started (postgres, neo4j, adminer)"
echo "  Adminer : http://localhost:8081"
echo "  Neo4j   : http://localhost:7474"
