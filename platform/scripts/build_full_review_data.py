"""
Build review_console_data_full.json from all available data sources.
Output: out/review_full/review_console_data.json
"""
import json
import os
from collections import Counter, defaultdict

BASE = r"D:\MyWork\verilog"
OUT_DIR = os.path.join(BASE, "out", "review_full")
os.makedirs(OUT_DIR, exist_ok=True)

def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

# ── 1. Modules from merged_ontology_seed ─────────────────────────────────────
print("Loading modules...")
seed = load_jsonl(os.path.join(BASE, "out", "merged_ontology_seed.jsonl"))
modules = []
for i, row in enumerate(seed):
    ports = row.get("ports", [])
    instances = row.get("instances", [])
    modules.append({
        "id": f"{row['project']}:{row['name']}:{i}",
        "project": row.get("project", ""),
        "entity_type": row.get("entity_type", "module"),
        "name": row.get("name", ""),
        "path": row.get("path", ""),
        "summary": row.get("summary", ""),
        "labels": row.get("labels", []),
        "ports": ports if isinstance(ports, list) else [],
        "instances": instances if isinstance(instances, list) else [],
        "metadata": row.get("metadata", {"source_kind": "merged_ontology_seed"}),
    })
print(f"  {len(modules)} modules")

# ── 2. Labels from review_queue + auto_approved ───────────────────────────────
print("Loading labels...")
review_queue = load_jsonl(os.path.join(BASE, "out", "label_approval", "review_queue.jsonl"))
auto_approved = load_jsonl(os.path.join(BASE, "out", "label_approval", "auto_approved_labels.jsonl"))
auto_rejected = load_jsonl(os.path.join(BASE, "out", "label_approval", "auto_rejected_labels.jsonl"))

labels = []
def map_state(decision, review_state):
    if review_state in ("approved", "auto_approved"):
        return "auto_accept_candidate"
    if review_state in ("rejected", "auto_rejected"):
        return "rejected"
    return "needs_review"

for row in review_queue + auto_approved + auto_rejected:
    ev = row.get("evidence", {})
    evidence_list = [{"kind": k, "value": v} for k, v in ev.items()] if isinstance(ev, dict) else []
    labels.append({
        "project": row.get("project", ""),
        "entity_type": row.get("entity_type", "label_proposal"),
        "module": row.get("target_name", ""),
        "path": row.get("path", ""),
        "label": row.get("label", ""),
        "group": row.get("group", ""),
        "confidence": row.get("auto_confidence", row.get("source_confidence", 0.0)),
        "review_state": map_state(row.get("decision", ""), row.get("review_state", "")),
        "evidence": evidence_list,
    })
print(f"  {len(labels)} label proposals")

# ── 3. Graph: sample from kg_full ─────────────────────────────────────────────
print("Loading KG graph...")
kg = load_json(os.path.join(BASE, "out", "kg_full", "kg_full_nodes_edges.json"))
all_nodes = kg["nodes"]
all_edges = kg["edges"]

# Separate module vs label nodes
module_nodes = [n for n in all_nodes if n.get("kind") == "module"]
label_nodes  = [n for n in all_nodes if n.get("kind") == "label"]
port_nodes   = [n for n in all_nodes if n.get("kind") not in ("module", "label")]

# For graph viz: take up to 600 module nodes (port-rich first) + all label nodes
module_nodes_sorted = sorted(module_nodes, key=lambda n: n.get("port_count", 0) + n.get("instance_count", 0) * 2, reverse=True)
selected_modules = module_nodes_sorted[:600]
selected_ids = {n["id"] for n in selected_modules} | {n["id"] for n in label_nodes}

# Remap to UI format
graph_nodes = []
for n in selected_modules:
    graph_nodes.append({
        "id": n["id"],
        "type": "module",
        "label": n.get("name", ""),
        "project": n.get("project", ""),
        "path": n.get("path", ""),
        "ports": n.get("port_count", 0),
        "instances": n.get("instance_count", 0),
    })
for n in label_nodes:
    graph_nodes.append({
        "id": n["id"],
        "type": "label",
        "label": n.get("name", n["id"].replace("label:", "")),
        "project": "",
        "path": "",
        "ports": 0,
        "instances": 0,
    })

graph_edges = [
    {"source": e["source"], "target": e["target"], "type": e.get("type", "HAS_LABEL")}
    for e in all_edges
    if e["source"] in selected_ids and e["target"] in selected_ids
]
print(f"  graph: {len(graph_nodes)} nodes, {len(graph_edges)} edges")

# ── 4. Summary ────────────────────────────────────────────────────────────────
label_counter = Counter()
for m in seed:
    for lbl in m.get("labels", []):
        label_counter[lbl] += 1

projects = Counter(m["project"] for m in seed)

kg_summary = load_json(os.path.join(BASE, "out", "kg_full", "kg_full_summary.json"))

summary = {
    "sample_files": kg_summary.get("modules", len(seed)),
    "modules": kg_summary.get("modules", len(seed)),
    "ip_blocks": kg_summary.get("ip_blocks", 0),
    "ports": kg_summary.get("ports", sum(len(m.get("ports", [])) for m in seed)),
    "instances": kg_summary.get("instance_edges", 0),
    "label_proposals": len(labels),
    "graph_nodes": len(graph_nodes),
    "graph_edges": len(graph_edges),
    "projects": dict(projects),
    "top_labels": label_counter.most_common(15),
    "approval": {
        "auto_approved": len(auto_approved),
        "needs_review": len(review_queue),
        "auto_rejected": len(auto_rejected),
    },
}

# ── 5. Search comparison (reuse existing 4 examples) ─────────────────────────
search_comparison = load_json(os.path.join(BASE, "out", "review_demo_100", "search_comparison_100.json"))

# ── 6. Write output ───────────────────────────────────────────────────────────
out = {
    "summary": summary,
    "modules": modules,
    "labels": labels,
    "graph": {"nodes": graph_nodes, "edges": graph_edges},
    "searchComparison": search_comparison,
}

out_path = os.path.join(OUT_DIR, "review_console_data.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, separators=(",", ":"))

size_mb = os.path.getsize(out_path) / 1024 / 1024
print(f"\nWrote: {out_path}")
print(f"Size: {size_mb:.1f} MB")
print(f"Summary: {json.dumps(summary, indent=2, ensure_ascii=False)}")
