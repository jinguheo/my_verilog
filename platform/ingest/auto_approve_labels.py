#!/usr/bin/env python3
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

LABEL_HINTS = {
    "uart": ["uart", "tx", "rx", "baud", "serial"],
    "i2c": ["i2c", "scl", "sda", "serial_bus"],
    "spi": ["spi", "mosi", "miso", "sclk", "csb", "serial_bus"],
    "gpio": ["gpio", "io"],
    "fifo": ["fifo", "queue", "full", "empty", "wr_ptr", "rd_ptr", "buffer"],
    "arbiter": ["arb", "grant", "gnt", "req", "request"],
    "controller": ["ctrl", "controller", "fsm", "state", "next_state"],
    "memory": ["mem", "ram", "rom", "flash", "storage", "regfile"],
    "counter": ["counter", "timer", "tick"],
    "decoder": ["decoder", "decode"],
    "encoder": ["encoder", "encode"],
    "register_file": ["register_file", "regfile", "register bank"],
    "adapter": ["adapter", "shim"],
    "bridge": ["bridge", "cdc", "async", "crossing"],
    "core": ["core", "engine"],
    "pipeline": ["pipeline", "stage"],
    "alu": ["alu", "adder", "logic unit"],
    "decoder_stage": ["decoder", "stage"],
    "csr": ["csr", "control status register"],
    "crypto": ["crypto", "aes", "hmac", "kmac", "cipher", "hash"],
    "flash": ["flash"],
    "timer": ["timer"],
    "opentitan_ip": ["opentitan", "hw\\ip", "/hw/ip/"],
    "ibex_core": ["ibex", "rv32", "core"],
}
GENERIC_LABELS = {"opentitan_ip", "ibex_core", "serial", "serial_bus", "device", "io"}
REVIEWABLE_GROUPS = {
    "protocol": {"uart", "i2c", "spi", "apb", "axi_lite", "gpio"},
    "role": {"fifo", "arbiter", "controller", "memory", "counter", "decoder", "encoder", "register_file", "adapter", "bridge", "core", "pipeline", "alu", "decoder_stage", "csr", "crypto", "flash", "timer"},
    "project": {"opentitan_ip", "ibex_core"},
}


def read_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fp:
        for row in rows:
            fp.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fp:
        json.dump(payload, fp, ensure_ascii=False, indent=2)


def tokenize(text):
    return [t for t in re.split(r"[^a-zA-Z0-9_]+", str(text).lower()) if t]


def label_group(label):
    for group, labels in REVIEWABLE_GROUPS.items():
        if label in labels:
            return group
    return "other"


def build_module_index(seed_rows):
    by_name = defaultdict(list)
    for row in seed_rows:
        if row.get("entity_type") != "module":
            continue
        by_name[row["name"]].append(row)
    return by_name


def find_matching_seed_rows(proposal, module_index):
    if proposal.get("entity_type") == "label_proposal":
        return module_index.get(proposal.get("name", ""), [])
    return []


def evidence_score(label, proposal, seed_matches, project_label_freq):
    name = proposal.get("name", "").lower()
    path = proposal.get("path", "").lower()
    summary = proposal.get("summary", "").lower()
    ports = []
    instances = []
    existing_seed_labels = set()
    for match in seed_matches:
        ports.extend(p.get("name", "").lower() for p in match.get("ports", []))
        instances.extend(i.get("type", "").lower() for i in match.get("instances", []))
        existing_seed_labels.update(l.lower() for l in match.get("labels", []))

    hints = LABEL_HINTS.get(label, [label])
    name_match = any(h in name for h in hints) or label in tokenize(name)
    path_match = any(h in path for h in hints) or label in tokenize(path)
    port_match = any(any(h in p for h in hints) for p in ports)
    inst_match = any(any(h in i for h in hints) for i in instances)
    summary_match = any(h in summary for h in hints)
    seed_label_match = label in existing_seed_labels
    project_support = min(project_label_freq[(proposal.get("project", ""), label)] / 10.0, 1.0)

    group = label_group(label)
    score = 0.0
    if name_match:
        score += 0.35
    if path_match:
        score += 0.30 if group == "project" else 0.20
    if port_match:
        score += 0.15
    if inst_match:
        score += 0.10
    if summary_match:
        score += 0.10 if group == "project" else 0.05
    if seed_label_match:
        score += 0.10
    score += 0.05 * project_support

    if group == "project" and proposal.get("entity_type") == "ip_block" and path_match:
        score += 0.10

    penalties = 0.0
    if label in GENERIC_LABELS and not (name_match or path_match):
        penalties += 0.10
    if group == "role" and not (name_match or port_match or inst_match or seed_label_match):
        penalties += 0.20
    if group == "protocol" and not (name_match or port_match or path_match):
        penalties += 0.25

    score = max(0.0, min(1.0, score - penalties))
    evidence = {
        "name_match": name_match,
        "path_match": path_match,
        "port_match": port_match,
        "instance_match": inst_match,
        "summary_match": summary_match,
        "seed_label_match": seed_label_match,
        "project_support": round(project_support, 3),
    }
    return score, evidence


def decide(score, evidence, label, proposal, base_conf):
    positive_hits = sum(
        1 for key in ["name_match", "path_match", "port_match", "instance_match", "summary_match", "seed_label_match"]
        if evidence.get(key)
    )
    group = label_group(label)
    entity_type = proposal.get("entity_type")
    source_kind = (proposal.get("metadata") or {}).get("source_kind", "")
    target_name = proposal.get("name", "").lower()
    target_tokens = set(tokenize(target_name))

    if group == "other":
        if (
            source_kind == "label_proposal"
            and label in target_tokens
            and not evidence.get("seed_label_match")
            and evidence.get("project_support", 0.0) <= 0.2
        ):
            return "auto_rejected"
        if score >= 0.7 and positive_hits >= 3:
            return "auto_approved"
        if score >= 0.5:
            return "needs_review"
        return "auto_rejected"

    if score >= 0.85 and positive_hits >= 2:
        return "auto_approved"

    if group == "project":
        if entity_type == "ip_block" and evidence.get("path_match") and evidence.get("summary_match") and base_conf >= 0.75:
            return "auto_approved"
        if score >= 0.65 and positive_hits >= 2:
            return "auto_approved"

    if group == "protocol":
        if (
            entity_type == "ip_block"
            and base_conf >= 0.75
            and evidence.get("name_match")
            and evidence.get("path_match")
            and evidence.get("summary_match")
        ):
            return "auto_approved"
        if score >= 0.72 and positive_hits >= 2 and (
            evidence.get("name_match") or evidence.get("port_match") or evidence.get("path_match")
        ):
            return "auto_approved"

    if group == "role":
        if (
            entity_type == "ip_block"
            and base_conf >= 0.75
            and evidence.get("name_match")
            and evidence.get("path_match")
            and evidence.get("summary_match")
        ):
            return "auto_approved"
        if score >= 0.78 and positive_hits >= 3:
            return "auto_approved"
        if (
            base_conf >= 0.8
            and score >= 0.68
            and evidence.get("name_match")
            and (
                evidence.get("path_match")
                or evidence.get("seed_label_match")
                or evidence.get("instance_match")
                or evidence.get("port_match")
            )
        ):
            return "auto_approved"

    if score >= 0.70 and group == "project" and positive_hits >= 1:
        return "auto_approved"
    if score >= 0.5:
        return "needs_review"
    return "auto_rejected"


def normalize_entries(label_rows, seed_rows):
    module_index = build_module_index(seed_rows)
    project_label_freq = Counter()
    for row in seed_rows:
        if row.get("entity_type") != "module":
            continue
        for label in row.get("labels", []):
            project_label_freq[(row.get("project", ""), label.lower())] += 1
    for row in label_rows:
        for label in row.get("labels", []):
            project_label_freq[(row.get("project", ""), label.lower())] += 1

    entries = []
    for row in label_rows:
        base_conf = float(row.get("confidence", 0.5))
        seed_matches = find_matching_seed_rows(row, module_index)
        for label in row.get("labels", []):
            label_l = label.lower()
            score, evidence = evidence_score(label_l, row, seed_matches, project_label_freq)
            floor = base_conf * (0.75 if label_group(label_l) == "project" else 0.65)
            final_score = round(min(1.0, max(score, floor)), 4)
            decision = decide(final_score, evidence, label_l, row, base_conf)
            entry = {
                "project": row.get("project"),
                "entity_type": row.get("entity_type"),
                "target_name": row.get("name"),
                "path": row.get("path"),
                "label": label_l,
                "group": label_group(label_l),
                "source_confidence": base_conf,
                "auto_confidence": final_score,
                "decision": decision,
                "review_state": "approved" if decision == "auto_approved" else ("needs_review" if decision == "needs_review" else "rejected"),
                "evidence": evidence,
                "source_summary": row.get("summary", ""),
                "source_metadata": row.get("metadata", {}),
            }
            entries.append(entry)
    return entries


def summarize(entries):
    by_decision = Counter(e["decision"] for e in entries)
    by_group_and_decision = defaultdict(Counter)
    for e in entries:
        by_group_and_decision[e["group"]][e["decision"]] += 1
    return {
        "total_entries": len(entries),
        "by_decision": dict(by_decision),
        "by_group": {g: dict(c) for g, c in sorted(by_group_and_decision.items())},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", required=True)
    ap.add_argument("--labels", required=True)
    ap.add_argument("--out-dir", required=True)
    args = ap.parse_args()

    seed_rows = read_jsonl(args.seed)
    label_rows = read_jsonl(args.labels)
    entries = normalize_entries(label_rows, seed_rows)
    summary = summarize(entries)

    out_dir = Path(args.out_dir)
    approved = [e for e in entries if e["decision"] == "auto_approved"]
    review = [e for e in entries if e["decision"] == "needs_review"]
    rejected = [e for e in entries if e["decision"] == "auto_rejected"]

    write_jsonl(out_dir / "auto_approved_labels.jsonl", approved)
    write_jsonl(out_dir / "review_queue.jsonl", review)
    write_jsonl(out_dir / "auto_rejected_labels.jsonl", rejected)
    write_jsonl(out_dir / "all_label_decisions.jsonl", entries)
    write_json(out_dir / "summary.json", summary)
    print(json.dumps({"status": "ok", "out_dir": str(out_dir), **summary}, ensure_ascii=False))


if __name__ == "__main__":
    main()
