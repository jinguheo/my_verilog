#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/_common.sh"

echo "=== ontology-first multi-project pipeline ==="
bash "$(dirname "${BASH_SOURCE[0]}")/generate_seed_and_labels.sh"
ok "완료. 다음: merged labels 리뷰 후 임베딩 생성."
