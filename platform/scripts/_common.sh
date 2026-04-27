#!/usr/bin/env bash
# _common.sh — shared variables and helpers for all bash scripts
# source this file at the top of each script:
#   source "$(dirname "${BASH_SOURCE[0]}")/_common.sh"

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLATFORM_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
WORKSPACE_ROOT="$(cd "$PLATFORM_DIR/.." && pwd)"

DB_ROOT="${VERILOG_DB_ROOT:-$WORKSPACE_ROOT/dbs}"
OUT_ROOT="${VERILOG_OUT_ROOT:-$WORKSPACE_ROOT/out}"
RUNTIME_ROOT="$PLATFORM_DIR/runtime"
INGEST_ROOT="$PLATFORM_DIR/ingest"
EVAL_ROOT="$PLATFORM_DIR/eval"
SCHEMA_ROOT="$PLATFORM_DIR/schema"

POSTGRES_URL="${POSTGRES_URL:-postgresql://postgres:postgres@localhost:5432/verilog}"
NEO4J_URI="${NEO4J_URI:-neo4j://localhost:7687}"
NEO4J_USER="${NEO4J_USER:-neo4j}"
NEO4J_PASSWORD="${NEO4J_PASSWORD:-neo4jpassword}"

# Prefer python3, fall back to python
PYTHON="${PYTHON:-$(command -v python3 2>/dev/null || command -v python)}"

# ── helpers ──────────────────────────────────────────────────────────────────

step() { echo ""; echo -e "\033[36m[$1]\033[0m $2"; }
ok()   { echo -e "      \033[32mOK:\033[0m $1"; }
warn() { echo -e "      \033[33mWARN:\033[0m $1"; }
skip() { echo -e "      \033[33mSKIP:\033[0m $1"; }
err()  { echo -e "      \033[31mERROR:\033[0m $1" >&2; exit 1; }

assert_path() {
    [[ -e "$1" ]] || err "$2 not found: $1"
}

assert_command() {
    command -v "$1" &>/dev/null || err "$1 not found. $2"
}

run_python() {
    local script="$1"; shift
    assert_path "$script" "Python script"
    "$PYTHON" "$script" "$@" || err "Python script failed: $script"
}

docker_container_running() {
    docker ps --filter "name=$1" --filter "status=running" -q 2>/dev/null | grep -q .
}

ensure_out_root() {
    mkdir -p "$OUT_ROOT"
}

load_env() {
    local env_file="$PLATFORM_DIR/.env"
    local example="$PLATFORM_DIR/.env.example"
    if [[ ! -f "$env_file" ]]; then
        cp "$example" "$env_file"
        warn ".env not found — copied from .env.example"
    fi
    # Export vars from .env (skip comments and blanks)
    set -o allexport
    # shellcheck disable=SC1090
    source "$env_file"
    set +o allexport
}
