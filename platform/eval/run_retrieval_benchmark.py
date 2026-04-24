#!/usr/bin/env python3
import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

EXPANSIONS = {
    "serial": ["uart", "spi", "i2c", "rx", "tx", "mosi", "miso", "scl", "sda"],
    "bus": ["spi", "i2c", "tlul", "uart"],
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
    modules = []
    for row in read_jsonl(seed_path):
        if row.get("entity_type") != "module":
            continue
        modules.append(row)
    return modules


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


def score_text(query_tokens, document, exact_name):
    score = 0.0
    reasons = []
    joined = " ".join(query_tokens)
    if exact_name and exact_name.lower() in document:
        score += 10.0
        reasons.append("exact_name")
    for token in query_tokens:
        if token in document:
            score += 1.0
            reasons.append(token)
    if joined and joined in document:
        score += 2.0
        reasons.append("phrase")
    return score, sorted(set(reasons))


def retrieve(question, modules, child_to_parents, mode, k=5):
    q = question["question"]
    tokens = tokenize(q)
    if mode == "kg":
        tokens = expand_terms(tokens)
    results = []
    exact_name = None
    if question["type"] == "exact_name":
        exact_name = question["gold_modules"][0]
    for module in modules:
        document = kg_doc(module, child_to_parents) if mode == "kg" else baseline_doc(module)
        score, reasons = score_text(tokens, document, exact_name)
        if mode == "kg":
            label_tokens = set(t for label in module.get("labels", []) for t in tokenize(label))
            overlap = len(label_tokens.intersection(tokens))
            score += overlap * 1.8
            if overlap:
                reasons.append("label_overlap")
            if module["name"] in child_to_parents and any(token in {"parent", "wrapper"} for token in tokens):
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


def rank_of(gold, results):
    for idx, row in enumerate(results, start=1):
        if row["name"] == gold:
            return idx
    return None


def difficulty_weight(d):
    return {"easy": 1.0, "medium": 1.5, "hard": 2.0}[d]


def aggregate(question_rows, runs_by_mode):
    report = {"by_mode": {}, "proxy_verilogeval": {}}
    for mode, runs in runs_by_mode.items():
        hit1 = hit3 = 0
        mrr = 0.0
        weighted = 0.0
        weighted_total = 0.0
        by_diff = defaultdict(lambda: {"count": 0, "hit1": 0, "hit3": 0, "mrr": 0.0})
        for row, run in zip(question_rows, runs):
            rank = run["gold_rank"]
            diff = row["difficulty"]
            w = difficulty_weight(diff)
            weighted_total += w
            by_diff[diff]["count"] += 1
            if rank == 1:
                hit1 += 1
                by_diff[diff]["hit1"] += 1
                weighted += w
            if rank is not None and rank <= 3:
                hit3 += 1
                by_diff[diff]["hit3"] += 1
            if rank is not None:
                rr = 1.0 / rank
                mrr += rr
                by_diff[diff]["mrr"] += rr
        n = len(runs)
        report["by_mode"][mode] = {
            "count": n,
            "hit_at_1": round(hit1 / n, 4),
            "hit_at_3": round(hit3 / n, 4),
            "mrr": round(mrr / n, 4),
            "weighted_hit_at_1": round(weighted / weighted_total, 4) if weighted_total else 0.0,
            "by_difficulty": {
                diff: {
                    "count": vals["count"],
                    "hit_at_1": round(vals["hit1"] / vals["count"], 4),
                    "hit_at_3": round(vals["hit3"] / vals["count"], 4),
                    "mrr": round(vals["mrr"] / vals["count"], 4),
                }
                for diff, vals in sorted(by_diff.items())
            },
        }
        # This is a local proxy, not an official VerilogEval score.
        report["proxy_verilogeval"][mode] = {
            "status": "proxy_only",
            "score_100": round(
                100.0 * (
                    0.45 * report["by_mode"][mode]["weighted_hit_at_1"] +
                    0.35 * report["by_mode"][mode]["hit_at_3"] +
                    0.20 * report["by_mode"][mode]["mrr"]
                ),
                2,
            ),
        }
    return report


def build_markdown(report, adapter_status):
    lines = [
        "# Retrieval Benchmark Report",
        "",
        "This report compares two retrieval conditions:",
        "",
        "- `kg`: uses labels, summaries, reverse graph hints, and query expansion.",
        "- `baseline`: uses parser/LSP style file-local clues such as module name, path, ports, and instances.",
        "",
        "## Aggregate",
        "",
    ]
    for mode, metrics in report["by_mode"].items():
        lines.extend([
            f"### {mode}",
            "",
            f"- hit@1: {metrics['hit_at_1']}",
            f"- hit@3: {metrics['hit_at_3']}",
            f"- mrr: {metrics['mrr']}",
            f"- weighted hit@1: {metrics['weighted_hit_at_1']}",
            f"- proxy VerilogEval score (/100): {report['proxy_verilogeval'][mode]['score_100']}",
            "",
        ])
    lines.extend([
        "## VerilogEval Adapter",
        "",
        f"- status: {adapter_status['status']}",
        f"- detail: {adapter_status['detail']}",
        "",
        "The proxy score is not an official VerilogEval number. It is a local readiness score derived from weighted retrieval accuracy.",
        "",
    ])
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", required=True)
    ap.add_argument("--benchmark", required=True)
    ap.add_argument("--out-dir", required=True)
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    modules = load_modules(args.seed)
    questions = read_jsonl(args.benchmark)
    child_to_parents = build_reverse_graph(modules)

    runs_by_mode = {"baseline": [], "kg": []}
    for question in questions:
        gold = question["gold_modules"][0]
        for mode in runs_by_mode:
            topk = retrieve(question, modules, child_to_parents, mode, k=5)
            runs_by_mode[mode].append({
                "id": question["id"],
                "difficulty": question["difficulty"],
                "gold": gold,
                "gold_rank": rank_of(gold, topk),
                "topk": topk,
            })

    report = aggregate(questions, runs_by_mode)
    adapter_status = {
        "status": "unavailable",
        "detail": "verilogeval package or runner was not available in this workspace; generated proxy-only score and adapter metadata.",
    }
    adapter = {
        "status": adapter_status["status"],
        "detail": adapter_status["detail"],
        "expected_inputs": {
            "questions_jsonl": str(Path(args.benchmark)),
            "predictions_json": str(out_dir / "predictions_for_verilogeval.json"),
        },
        "note": "Map each question to a model answer, then hand it to an external VerilogEval runner when available.",
    }

    predictions = []
    for mode, runs in runs_by_mode.items():
        for run in runs:
            predictions.append({
                "mode": mode,
                "id": run["id"],
                "gold": run["gold"],
                "prediction_top1": run["topk"][0]["name"] if run["topk"] else None,
                "prediction_top5": [row["name"] for row in run["topk"]],
                "gold_rank": run["gold_rank"],
            })

    write_json(out_dir / "retrieval_report.json", report)
    write_json(out_dir / "verilogeval_adapter.json", adapter)
    write_json(out_dir / "predictions_for_verilogeval.json", predictions)
    write_json(out_dir / "detailed_runs.json", runs_by_mode)
    with open(out_dir / "retrieval_report.md", "w", encoding="utf-8") as fp:
        fp.write(build_markdown(report, adapter_status))
    print(json.dumps({
        "status": "ok",
        "out_dir": str(out_dir),
        "baseline_hit_at_1": report["by_mode"]["baseline"]["hit_at_1"],
        "kg_hit_at_1": report["by_mode"]["kg"]["hit_at_1"],
        "baseline_proxy_score": report["proxy_verilogeval"]["baseline"]["score_100"],
        "kg_proxy_score": report["proxy_verilogeval"]["kg"]["score_100"],
        "verilogeval_status": adapter_status["status"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
