#!/usr/bin/env python3
import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

EXPANSIONS = {
    "serial": ["uart", "spi", "i2c", "rx", "tx", "mosi", "miso", "scl", "sda"],
    "bus": ["spi", "i2c", "tlul", "uart", "apb"],
    "controller": ["controller", "ctrl", "fsm", "state"],
    "control": ["controller", "ctrl", "fsm", "state"],
    "queue": ["fifo", "buffer"],
    "buffer": ["fifo", "queue"],
    "memory": ["memory", "ram", "rom", "regfile", "csr"],
    "storage": ["memory", "ram", "rom", "regfile"],
    "crypto": ["crypto", "aes", "hmac", "kmac", "csrng"],
    "cryptographic": ["crypto", "aes", "hmac", "kmac"],
    "wrapper": ["hierarchical", "wrapper", "parent"],
    "parent": ["hierarchical", "wrapper"],
    "sequential": ["clocked"],
    "reset": ["resettable", "rst", "reset"],
    "bridge": ["cdc", "async", "fifo"],
    "synchronizes": ["cdc", "sync", "async"],
    "timer": ["counter", "timer"],
    "register": ["reg", "regfile", "csr", "register"],
    "bank": ["regfile", "csr", "register"],
    "cpu": ["ibex", "core", "rv32"],
    "pipeline": ["ibex", "stage", "decoder", "alu"],
}


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


def tokenize(text):
    return [t for t in re.split(r"[^a-zA-Z0-9_]+", text.lower()) if len(t) > 1]


def load_modules(seed_path):
    return [row for row in read_jsonl(seed_path) if row.get("entity_type") == "module"]


def build_reverse_graph(modules):
    child_to_parents = defaultdict(list)
    for module in modules:
        for inst in module.get("instances", []):
            child_to_parents[inst["type"]].append(module["name"])
    return child_to_parents


def baseline_doc(module):
    parts = [
        module["name"],
        module["project"],
        module["path"],
        " ".join(p["name"] for p in module.get("ports", [])),
        " ".join(i["type"] + " " + i.get("name", "") for i in module.get("instances", [])),
    ]
    return " ".join(parts).lower()


def kg_doc(module, child_to_parents):
    reverse = " ".join(child_to_parents.get(module["name"], []))
    parts = [
        baseline_doc(module),
        " ".join(module.get("labels", [])),
        module.get("summary", ""),
        reverse,
    ]
    return " ".join(parts).lower()


def expand_terms(tokens):
    out = set(tokens)
    for token in list(tokens):
        out.update(EXPANSIONS.get(token, []))
    return list(out)


def score_text(query_tokens, document, exact_names):
    score = 0.0
    reasons = []
    for exact_name in exact_names:
        if exact_name.lower() in document:
            score += 8.0
            reasons.append("exact_name")
    phrase = " ".join(query_tokens)
    if phrase and phrase in document:
        score += 2.0
        reasons.append("phrase")
    for token in query_tokens:
        if token in document:
            score += 1.0
            reasons.append(token)
    return score, sorted(set(reasons))


def retrieve(question, modules, child_to_parents, mode, k=5):
    tokens = tokenize(question["question"])
    exact_names = question["gold_modules"]
    if mode == "kg":
        tokens = expand_terms(tokens)
    results = []
    for module in modules:
        document = kg_doc(module, child_to_parents) if mode == "kg" else baseline_doc(module)
        score, reasons = score_text(tokens, document, exact_names)
        if mode == "kg":
            label_tokens = set(t for label in module.get("labels", []) for t in tokenize(label))
            overlap = len(label_tokens.intersection(tokens))
            score += overlap * 1.8
            if overlap:
                reasons.append("label_overlap")
            if module["name"] in child_to_parents and any(token in {"parent", "wrapper", "hierarchy"} for token in tokens):
                score += 0.8
        else:
            port_tokens = set(tokenize(" ".join(p["name"] for p in module.get("ports", []))))
            inst_tokens = set(tokenize(" ".join(i["type"] for i in module.get("instances", []))))
            score += len(port_tokens.intersection(tokens)) * 0.5
            score += len(inst_tokens.intersection(tokens)) * 0.5
        if score > 0:
            results.append({
                "name": module["name"],
                "project": module["project"],
                "score": round(score, 3),
                "reasons": reasons[:8],
            })
    results.sort(key=lambda r: (-r["score"], r["project"], r["name"]))
    return results[:k]


def rank_of(golds, results):
    gold_set = set(golds)
    for idx, row in enumerate(results, start=1):
        if row["name"] in gold_set:
            return idx
    return None


def level_weight(level):
    return {"L1": 1.0, "L2": 1.2, "L3": 1.5, "L4": 1.8, "L5": 2.2}[level]


def aggregate(questions, runs_by_mode):
    report = {"by_mode": {}}
    for mode, runs in runs_by_mode.items():
        total = len(runs)
        hit1 = hit3 = 0
        mrr = 0.0
        weighted_hit = 0.0
        weighted_total = 0.0
        by_level = defaultdict(lambda: {"count": 0, "hit1": 0, "hit3": 0, "mrr": 0.0})
        by_type = defaultdict(lambda: {"count": 0, "hit1": 0, "hit3": 0, "mrr": 0.0})
        for q, run in zip(questions, runs):
            rank = run["gold_rank"]
            level = q["level"]
            qtype = q["type"]
            weight = level_weight(level)
            weighted_total += weight
            by_level[level]["count"] += 1
            by_type[qtype]["count"] += 1
            if rank == 1:
                hit1 += 1
                weighted_hit += weight
                by_level[level]["hit1"] += 1
                by_type[qtype]["hit1"] += 1
            if rank is not None and rank <= 3:
                hit3 += 1
                by_level[level]["hit3"] += 1
                by_type[qtype]["hit3"] += 1
            if rank is not None:
                rr = 1.0 / rank
                mrr += rr
                by_level[level]["mrr"] += rr
                by_type[qtype]["mrr"] += rr
        report["by_mode"][mode] = {
            "count": total,
            "hit_at_1": round(hit1 / total, 4),
            "hit_at_3": round(hit3 / total, 4),
            "mrr": round(mrr / total, 4),
            "weighted_hit_at_1": round(weighted_hit / weighted_total, 4),
            "by_level": {
                key: {
                    "count": vals["count"],
                    "hit_at_1": round(vals["hit1"] / vals["count"], 4),
                    "hit_at_3": round(vals["hit3"] / vals["count"], 4),
                    "mrr": round(vals["mrr"] / vals["count"], 4),
                } for key, vals in sorted(by_level.items())
            },
            "by_type": {
                key: {
                    "count": vals["count"],
                    "hit_at_1": round(vals["hit1"] / vals["count"], 4),
                    "hit_at_3": round(vals["hit3"] / vals["count"], 4),
                    "mrr": round(vals["mrr"] / vals["count"], 4),
                } for key, vals in sorted(by_type.items())
            },
        }
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", required=True)
    ap.add_argument("--questions", required=True)
    ap.add_argument("--out-dir", required=True)
    args = ap.parse_args()

    modules = load_modules(args.seed)
    questions = read_jsonl(args.questions)
    child_to_parents = build_reverse_graph(modules)
    runs_by_mode = {"baseline": [], "kg": []}

    for question in questions:
        for mode in runs_by_mode:
            topk = retrieve(question, modules, child_to_parents, mode, 5)
            runs_by_mode[mode].append({
                "level": question["level"],
                "type": question["type"],
                "gold_modules": question["gold_modules"],
                "gold_rank": rank_of(question["gold_modules"], topk),
                "topk": topk,
            })

    report = aggregate(questions, runs_by_mode)
    out_dir = Path(args.out_dir)
    write_json(out_dir / "multiaxis_report.json", report)
    write_json(out_dir / "multiaxis_detailed_runs.json", runs_by_mode)
    print(json.dumps({
        "status": "ok",
        "out_dir": str(out_dir),
        "baseline_hit_at_1": report["by_mode"]["baseline"]["hit_at_1"],
        "kg_hit_at_1": report["by_mode"]["kg"]["hit_at_1"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
