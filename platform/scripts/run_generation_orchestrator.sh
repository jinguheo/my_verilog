#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/_common.sh"
assert_command go "Install Go: https://go.dev/doc/install"

SERVICE_ROOT="$PLATFORM_DIR/services/generation-orchestrator"
pushd "$SERVICE_ROOT" > /dev/null
go mod tidy
go run ./cmd/generation-orchestrator
popd > /dev/null
