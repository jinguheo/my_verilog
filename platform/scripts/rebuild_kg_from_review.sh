#!/usr/bin/env bash
# Lightweight alias — delegates to apply_review_and_update_kg.sh
exec "$(dirname "${BASH_SOURCE[0]}")/apply_review_and_update_kg.sh" "$@"
