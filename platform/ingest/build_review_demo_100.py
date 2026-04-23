#!/usr/bin/env python3
import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

MODULE_RE = re.compile(r"\bmodule\s+([A-Za-z_][A-Za-z0-9_$]*)")
ENDMODULE_RE = re.compile(r"\bendmodule\b")
PORT_RE = re.compile(
    r"\b(input|output|inout)\b(?:\s+(?:wire|reg|logic|signed|unsigned))*\s*(?:\[[^\]]+\]\s*)?([A-Za-z_][A-Za-z0-9_$]*)"
)
INSTANCE_RE = re.compile(
    r"^\s*([A-Za-z_][A-Za-z0-9_$]*)\s*(?:#\s*\([^;]*?\))?\s+([A-Za-z_][A-Za-z0-9_$]*)\s*\(",
    re.MULTILINE | re.DOTALL,
)

LABEL_HINTS = {
    "protocol:uart": ["uart", "baud", "tx", "rx"],
    "protocol:i2c": ["i2c", "scl", "sda"],
    "protocol:spi": ["spi", "mosi", "miso", "sclk", "csb"],
    "protocol:tlul": ["tl_", "tlul", "a_valid", "d_valid"],
    "role:fifo": ["fifo", "queue", "full", "empty", "wr_ptr", "rd_ptr"],
    "role:arbiter": ["arb", "grant", "gnt", "request", "req"],
    "role:controller": ["ctrl", "controller", "fsm", "state", "next_state"],
    "role:memory": ["mem", "ram", "rom", "sram", "regfile"],
    "role:crypto": ["aes", "hmac", "kmac", "sha", "entropy"],
    "cpu:ibex": ["ibex", "rv32", "csr", "decoder", "alu"],
}
RESERVED_NAMES = {
    "a", "an", "and", "are", "as", "auto", "be", "can", "case", "end", "for", "from",
    "if", "in", "is", "module", "of", "or", "that", "the", "this", "to", "with",
}


def read_jsonl(path):
    if not path.exists():
        return []
    rows = []
    with path.open("r", encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fp:
        json.dump(payload, fp, ensure_ascii=False, indent=2)


def write_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fp:
        for row in rows:
            fp.write(json.dumps(row, ensure_ascii=False) + "\n")


def find_modules(text):
    starts = [(m.start(), m.group(1)) for m in MODULE_RE.finditer(text)]
    ends = [m.start() for m in ENDMODULE_RE.finditer(text)]
    modules = []
    eidx = 0
    for start, name in starts:
        while eidx < len(ends) and ends[eidx] < start:
            eidx += 1
        if eidx >= len(ends):
            break
        if name.lower() not in RESERVED_NAMES:
            modules.append((name, text[start:ends[eidx]]))
        eidx += 1
    return modules


def infer_labels(project, module_name, body, ports, instances, path):
    haystack = " ".join(
        [project, module_name, str(path), body[:5000]]
        + [p["name"] for p in ports]
        + [i["type"] for i in instances]
    ).lower()
    labels = set()
    for label, hints in LABEL_HINTS.items():
        if any(hint in haystack for hint in hints):
            labels.add(label)
    if any("clk" in p["name"].lower() for p in ports):
        labels.add("runtime:clocked")
    if any("rst" in p["name"].lower() or "reset" in p["name"].lower() for p in ports):
        labels.add("runtime:resettable")
    if instances:
        labels.add("structure:hierarchical")
    if project == "opentitan":
        labels.add("project:opentitan")
    if project == "ibex":
        labels.add("project:ibex")
    return sorted(labels)


def module_bearing_files(base):
    files = []
    if not base.exists():
        return files
    for path in sorted(base.rglob("*")):
        if path.suffix.lower() not in {".v", ".sv"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if MODULE_RE.search(text):
            files.append(path)
    return files


def select_rtl_files(root, limit):
    buckets = [
        module_bearing_files(root / "opentitan" / "hw" / "ip"),
        module_bearing_files(root / "opentitan" / "hw" / "vendor" / "pulp_riscv_dbg"),
        module_bearing_files(root / "ibex" / "rtl"),
        module_bearing_files(root / "ibex" / "vendor"),
    ]
    seen = set()
    selected = []
    idx = 0
    while len(selected) < limit and any(idx < len(bucket) for bucket in buckets):
        for bucket in buckets:
            if idx >= len(bucket):
                continue
            path = bucket[idx]
            key = str(path).lower()
            if key not in seen:
                selected.append(path)
                seen.add(key)
            if len(selected) >= limit:
                break
        idx += 1
    return selected


def project_for(path):
    parts = {p.lower() for p in path.parts}
    if "opentitan" in parts:
        return "opentitan"
    if "ibex" in parts:
        return "ibex"
    return "unknown"


def build_records(files):
    modules = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        project = project_for(path)
        for module_name, body in find_modules(text):
            ports = [{"dir": d, "name": n} for d, n in PORT_RE.findall(body)]
            instances = [
                {"type": t, "name": n}
                for t, n in INSTANCE_RE.findall(body)
                if t not in {"module", "if", "for", "always", "assign"}
            ]
            labels = infer_labels(project, module_name, body, ports, instances, path)
            modules.append(
                {
                    "id": f"{project}:{module_name}:{len(modules)}",
                    "project": project,
                    "entity_type": "module",
                    "name": module_name,
                    "path": str(path),
                    "summary": f"{module_name}: {', '.join(labels) if labels else 'unlabeled rtl block'}",
                    "labels": labels,
                    "ports": ports,
                    "instances": instances[:80],
                    "evidence": [{"kind": "source_file", "path": str(path)}],
                    "metadata": {"source_kind": "review_demo_100"},
                }
            )
    return modules


def build_label_proposals(modules):
    proposals = []
    for module in modules:
        for label in module["labels"]:
            confidence = 0.86
            if label.startswith("project:") or label.startswith("runtime:"):
                confidence = 0.93
            elif label.startswith("role:") or label.startswith("protocol:"):
                confidence = 0.78
            proposals.append(
                {
                    "project": module["project"],
                    "entity_type": "label_proposal",
                    "module": module["name"],
                    "path": module["path"],
                    "label": label,
                    "confidence": confidence,
                    "review_state": "needs_review"
                    if confidence < 0.85
                    else "auto_accept_candidate",
                    "evidence": module["evidence"],
                }
            )
    return proposals


def build_graph(modules):
    nodes = []
    edges = []
    label_seen = set()
    module_names = {m["name"] for m in modules}
    for module in modules:
        nodes.append(
            {
                "id": module["id"],
                "type": "module",
                "label": module["name"],
                "project": module["project"],
                "path": module["path"],
                "ports": len(module["ports"]),
                "instances": len(module["instances"]),
            }
        )
        for label in module["labels"]:
            label_id = f"label:{label}"
            if label_id not in label_seen:
                nodes.append({"id": label_id, "type": "label", "label": label})
                label_seen.add(label_id)
            edges.append({"source": module["id"], "target": label_id, "type": "HAS_LABEL"})
        for inst in module["instances"]:
            if inst["type"] in module_names:
                edges.append(
                    {
                        "source": module["id"],
                        "target_name": inst["type"],
                        "type": "INSTANTIATES",
                        "instance": inst["name"],
                    }
                )
    name_to_id = {}
    for module in modules:
        name_to_id.setdefault(module["name"], module["id"])
    for edge in edges:
        if "target_name" in edge:
            edge["target"] = name_to_id.get(edge.pop("target_name"))
    edges = [e for e in edges if e.get("target")]
    return {"nodes": nodes, "edges": edges}


def tokenize(text):
    return [t for t in re.split(r"[^a-zA-Z0-9_]+", text.lower()) if len(t) > 1]


def parser_lsp_search(modules, query):
    terms = tokenize(query)
    results = []
    for module in modules:
        score = 0
        for term in terms:
            if term in module["name"].lower():
                score += 6
            if term in Path(module["path"]).name.lower():
                score += 3
            for port in module["ports"]:
                if term in port["name"].lower():
                    score += 2
            for inst in module["instances"]:
                if term in inst["type"].lower() or term in inst["name"].lower():
                    score += 1
        if score:
            results.append({"name": module["name"], "project": module["project"], "score": score, "why": "symbol/path/port string match"})
    return sorted(results, key=lambda r: (-r["score"], r["name"]))[:8]


def ontology_search(modules, query):
    terms = tokenize(query)
    results = []
    for module in modules:
        text = " ".join([module["name"], module["summary"], " ".join(module["labels"]), module["path"]]).lower()
        score = 0.0
        reasons = []
        for term in terms:
            if term in module["name"].lower():
                score += 6
                reasons.append("module name")
            if any(term in label.lower() for label in module["labels"]):
                score += 5
                reasons.append("ontology label")
            if term in text:
                score += 1.5
        if "protocol" in query.lower() and any(l.startswith("protocol:") for l in module["labels"]):
            score += 2
            reasons.append("protocol facet")
        if "hierarchical" in query.lower() and module["instances"]:
            score += 2
            reasons.append("graph connectivity")
        if score:
            results.append(
                {
                    "name": module["name"],
                    "project": module["project"],
                    "score": round(score, 2),
                    "labels": module["labels"],
                    "why": ", ".join(sorted(set(reasons))) or "ontology text",
                }
            )
    return sorted(results, key=lambda r: (-r["score"], r["name"]))[:8]


def build_search_comparison(modules):
    queries = ["spi controller", "fifo resettable", "ibex decoder", "crypto memory"]
    rows = []
    for query in queries:
        rows.append(
            {
                "query": query,
                "parser_lsp": parser_lsp_search(modules, query),
                "ontology_db": ontology_search(modules, query),
                "difference": {
                    "parser_lsp": "소스 심볼, 파일명, 포트명처럼 현재 열려 있거나 파싱 가능한 문자열 중심으로 찾음",
                    "ontology_db": "모듈, 포트, 인스턴스, 라벨, evidence, graph 관계를 함께 사용해 의도와 역할 중심으로 찾음",
                },
            }
        )
    return rows


def summarize(files, modules, labels, graph):
    label_counts = Counter(label for module in modules for label in module["labels"])
    project_counts = Counter(module["project"] for module in modules)
    ports = sum(len(m["ports"]) for m in modules)
    instances = sum(len(m["instances"]) for m in modules)
    return {
        "sample_files": len(files),
        "modules": len(modules),
        "ports": ports,
        "instances": instances,
        "label_proposals": len(labels),
        "graph_nodes": len(graph["nodes"]),
        "graph_edges": len(graph["edges"]),
        "projects": dict(project_counts),
        "top_labels": label_counts.most_common(12),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db-root", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--limit", type=int, default=100)
    args = ap.parse_args()

    db_root = Path(args.db_root)
    out_dir = Path(args.out_dir)
    files = select_rtl_files(db_root, args.limit)
    modules = build_records(files)
    labels = build_label_proposals(modules)
    graph = build_graph(modules)
    search = build_search_comparison(modules)
    summary = summarize(files, modules, labels, graph)

    write_json(out_dir / "sample_files.json", [str(p) for p in files])
    write_jsonl(out_dir / "ontology_seed_100.jsonl", modules)
    write_jsonl(out_dir / "review_candidates_100.jsonl", labels)
    write_json(out_dir / "ontology_graph_100.json", graph)
    write_json(out_dir / "search_comparison_100.json", search)
    write_json(out_dir / "summary_100.json", summary)
    write_json(
        out_dir / "review_console_data.json",
        {
            "summary": summary,
            "modules": modules,
            "labels": labels,
            "graph": graph,
            "searchComparison": search,
        },
    )
    print(json.dumps({"status": "ok", "out_dir": str(out_dir), **summary}, ensure_ascii=False))


if __name__ == "__main__":
    main()
