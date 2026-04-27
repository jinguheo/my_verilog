#!/usr/bin/env bash
source "$(dirname "${BASH_SOURCE[0]}")/_common.sh"

check() {
    local name="$1" path="$2"
    if [[ -e "$path" ]]; then
        printf "  \033[32m✓\033[0m  %-30s  %s\n" "$name" "$path"
    else
        printf "  \033[31m✗\033[0m  %-30s  %s\n" "$name" "$path"
    fi
}

echo ""
echo "=== Workflow Status ==="
echo ""
check "OpenTitan DB"           "$DB_ROOT/opentitan"
check "Ibex DB"                "$DB_ROOT/ibex"
check "sv-tests DB"            "$DB_ROOT/sv-tests"
check "RTLLM DB"               "$DB_ROOT/RTLLM"
check "Merged ontology seed"   "$OUT_ROOT/merged_ontology_seed.jsonl"
check "Merged labels"          "$OUT_ROOT/merged_labels.jsonl"
check "Auto approved labels"   "$OUT_ROOT/label_approval/auto_approved_labels.jsonl"
check "Review queue"           "$OUT_ROOT/label_approval/review_queue.jsonl"
check "KG full nodes/edges"    "$OUT_ROOT/kg_full/kg_full_nodes_edges.json"
check "KG versions index"      "$OUT_ROOT/kg_versions/index.json"
check "Review console data"    "$OUT_ROOT/review_full/review_console_data.json"
check "Platform .env"          "$PLATFORM_DIR/.env"
echo ""

# KG version 현황
if [[ -f "$OUT_ROOT/kg_versions/index.json" ]]; then
    echo "KG 버전 히스토리:"
    "$PYTHON" - "$OUT_ROOT/kg_versions/index.json" <<'PYEOF'
import json, sys
index = json.load(open(sys.argv[1]))
cur = index.get("current","")
for v in index["versions"]:
    tag = v["version_tag"]
    marker = " ◄ current" if tag == cur else ""
    print(f"  {tag}  {v['created_at'][:19].replace('T',' ')}  "
          f"modules={v.get('modules_total',0)}  "
          f"approved_added={v.get('approved_added',0)}{marker}")
PYEOF
    echo ""
fi

# Docker 상태
echo "Docker 컨테이너:"
for c in verilog-postgres verilog-neo4j verilog-adminer; do
    if docker_container_running "$c"; then
        printf "  \033[32m✓ running\033[0m  %s\n" "$c"
    else
        printf "  \033[31m✗ stopped\033[0m  %s\n" "$c"
    fi
done
echo ""
echo "Quick start: bash $PLATFORM_DIR/scripts/full_bootstrap.sh"
