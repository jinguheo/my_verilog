#!/usr/bin/env python3
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

from retrieval_common import apply_approved_labels, resolve_approved_labels_path


def read_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fp:
        json.dump(payload, fp, ensure_ascii=False, indent=2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", required=True)
    ap.add_argument("--labels", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--approved-labels")
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    seed_rows = read_jsonl(args.seed)
    label_rows = read_jsonl(args.labels)

    modules = [row for row in seed_rows if row.get("entity_type") == "module"]
    approved_path = resolve_approved_labels_path(args.seed, args.approved_labels)
    approved_summary = apply_approved_labels(modules, approved_path)
    ip_blocks = [row for row in label_rows if row.get("entity_type") == "ip_block"]
    module_names = {m["name"] for m in modules}

    nodes = []
    edges = []
    label_counter = Counter()
    reverse_edges = defaultdict(list)

    for module in modules:
        module_id = f"module:{module['project']}:{module['name']}:{module['path']}"
        nodes.append({
            "id": module_id,
            "kind": "module",
            "name": module["name"],
            "project": module["project"],
            "path": module["path"],
            "summary": module.get("summary", ""),
            "port_count": len(module.get("ports", [])),
            "instance_count": len(module.get("instances", [])),
        })
        for label in module.get("labels", []):
            label_id = f"label:{label}"
            label_counter[label] += 1
            edges.append({"source": module_id, "target": label_id, "type": "HAS_LABEL"})
        for port in module.get("ports", []):
            port_id = f"port:{module['project']}:{module['name']}:{port['name']}"
            nodes.append({
                "id": port_id,
                "kind": "port",
                "name": port["name"],
                "direction": port.get("dir", ""),
                "module": module["name"],
                "project": module["project"],
            })
            edges.append({"source": module_id, "target": port_id, "type": "HAS_PORT"})
        for inst in module.get("instances", []):
            child_name = inst.get("type")
            if not child_name:
                continue
            reverse_edges[child_name].append(module["name"])
            if child_name in module_names:
                child_candidates = [m for m in modules if m["name"] == child_name]
                child = child_candidates[0]
                child_id = f"module:{child['project']}:{child['name']}:{child['path']}"
                edges.append({
                    "source": module_id,
                    "target": child_id,
                    "type": "INSTANTIATES",
                    "instance_name": inst.get("name", ""),
                })

    for label, count in sorted(label_counter.items()):
        nodes.append({
            "id": f"label:{label}",
            "kind": "label",
            "name": label,
            "module_count": count,
        })

    for ip in ip_blocks:
        ip_id = f"ip:{ip['project']}:{ip['name']}"
        nodes.append({
            "id": ip_id,
            "kind": "ip_block",
            "name": ip["name"],
            "project": ip["project"],
            "path": ip["path"],
            "labels": ip.get("labels", []),
        })
        for label in ip.get("labels", []):
            edges.append({"source": ip_id, "target": f"label:{label}", "type": "HAS_LABEL"})

    summary = {
        "modules": len(modules),
        "ip_blocks": len(ip_blocks),
        "labels": len(label_counter),
        "ports": sum(len(m.get("ports", [])) for m in modules),
        "instance_edges": sum(1 for e in edges if e["type"] == "INSTANTIATES"),
        "total_nodes": len(nodes),
        "total_edges": len(edges),
        "projects": dict(Counter(m["project"] for m in modules)),
        "top_labels": label_counter.most_common(20),
        "approved_labels": approved_summary,
    }

    write_json(out_dir / "kg_full_nodes_edges.json", {"nodes": nodes, "edges": edges})
    write_json(out_dir / "kg_full_summary.json", summary)
    print(json.dumps({"status": "ok", "out_dir": str(out_dir), **summary}, ensure_ascii=False))


if __name__ == "__main__":
    main()
