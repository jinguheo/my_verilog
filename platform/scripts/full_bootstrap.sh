#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/_common.sh"

SCRIPTS_DIR="$PLATFORM_DIR/scripts"

bash "$SCRIPTS_DIR/init_folders.sh"
load_env
bash "$SCRIPTS_DIR/start_stack.sh"

echo "Docker 스택 기동 대기 (8초)..."
sleep 8

bash "$SCRIPTS_DIR/load_postgres_schema.sh"
bash "$SCRIPTS_DIR/generate_seed_and_labels.sh"
bash "$SCRIPTS_DIR/load_neo4j.sh"

ok "Bootstrap 완료 (OpenTitan + Ibex)"
