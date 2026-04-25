#!/usr/bin/env python3
import argparse
import json
import random
import re
from collections import Counter, defaultdict
from pathlib import Path

RESERVED = {
    "if", "for", "while", "case", "module", "interface", "end", "begin",
    "generate", "assign", "always", "function", "task", "unique",
    "auto", "is", "tb", "to", "can", "contains", "checks", "values",
}
PATH_EXCLUDES = ["\\dv\\", "\\tb", "\\formal\\", "\\pre_sca\\", "\\lint\\", "\\fpv\\", "\\doc\\"]

LABEL_SYNONYMS = {
    "uart": ["serial", "rx", "tx", "uart"],
    "spi": ["serial bus", "spi", "mosi", "miso", "sclk"],
    "i2c": ["serial bus", "i2c", "scl", "sda"],
    "fifo": ["queue", "fifo", "buffer"],
    "arbiter": ["arbiter", "grant", "request scheduler"],
    "controller": ["controller", "fsm", "control block"],
    "memory": ["memory", "storage", "ram", "rom", "register bank"],
    "counter": ["counter", "timer"],
    "crypto": ["crypto", "cryptographic", "cipher", "hash"],
    "clocked": ["clocked", "sequential"],
    "resettable": ["resettable", "reset aware"],
    "hierarchical": ["hierarchical", "wrapper", "parent block"],
    "ibex_core": ["ibex core", "cpu pipeline", "rv32 core"],
    "csr": ["csr", "control status register", "register bank"],
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


def write_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fp:
        for row in rows:
            fp.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_markdown_catalog(path, sections):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# RTL QA Benchmark Catalog", ""]
    for title, rows in sections:
        lines.append(f"## {title}")
        lines.append("")
        for idx, row in enumerate(rows, start=1):
            lines.append(f"{idx}. {row['question']}")
            lines.append(f"   - gold: `{row['gold_modules'][0]}` ({row['gold_project']})")
            lines.append(f"   - type: `{row['type']}`")
        lines.append("")
    with open(path, "w", encoding="utf-8") as fp:
        fp.write("\n".join(lines))


def clean_modules(rows):
    cleaned = []
    for row in rows:
        if row.get("entity_type") != "module":
            continue
        name = row.get("name", "")
        path_lower = row.get("path", "").lower()
        if any(token in path_lower for token in PATH_EXCLUDES):
            continue
        if not name or name.lower() in RESERVED or len(name) < 3:
            continue
        if sum(ch.isalpha() for ch in name) < 3:
            continue
        if re.fullmatch(r"[a-z]+", name.lower()) and name.lower() not in path_lower:
            continue
        ports = [p for p in row.get("ports", []) if p.get("name") and p["name"].lower() not in RESERVED]
        instances = [
            i for i in row.get("instances", [])
            if i.get("type") and i["type"].lower() not in RESERVED and i.get("name", "").lower() not in RESERVED
        ]
        row = dict(row)
        row["ports"] = ports
        row["instances"] = instances
        cleaned.append(row)
    return cleaned


def build_indexes(modules):
    port_to_modules = defaultdict(list)
    label_to_modules = defaultdict(list)
    child_to_parents = defaultdict(list)
    path_token_to_modules = defaultdict(list)
    for module in modules:
        for port in module["ports"]:
            port_to_modules[port["name"].lower()].append(module)
        for label in module.get("labels", []):
            label_to_modules[label.lower()].append(module)
        for inst in module["instances"]:
            child_to_parents[inst["type"]].append(module)
        for token in re.split(r"[^a-zA-Z0-9_]+", module["path"].lower()):
            if len(token) > 2:
                path_token_to_modules[token].append(module)
    return port_to_modules, label_to_modules, child_to_parents, path_token_to_modules


def module_brief(module):
    return {
        "name": module["name"],
        "project": module["project"],
        "path": module["path"],
        "labels": module.get("labels", []),
        "ports": [p["name"] for p in module.get("ports", [])],
        "instances": [i["type"] for i in module.get("instances", [])],
    }


def trustworthy_name(module):
    name = module["name"].lower()
    stem = Path(module["path"]).stem.lower()
    if name in stem or stem in name:
        return True
    stem_tokens = set(re.split(r"[^a-zA-Z0-9_]+", stem))
    name_tokens = set(re.split(r"[^a-zA-Z0-9_]+", name))
    return bool(stem_tokens.intersection(name_tokens))


def unique_port_candidates(modules, port_to_modules):
    for port, owners in port_to_modules.items():
        if len(owners) == 1 and len(port) >= 4:
            yield port, owners[0]


def select_synonym(label):
    key = label.lower().split(":")[-1]
    options = LABEL_SYNONYMS.get(key, [label])
    return random.choice(options)


def add_question(bucket, used_ids, question_id, difficulty, qtype, question, gold_module, evidence, notes):
    if question_id in used_ids:
        return False
    used_ids.add(question_id)
    bucket.append({
        "id": question_id,
        "difficulty": difficulty,
        "type": qtype,
        "question": question,
        "gold_modules": [gold_module["name"]],
        "gold_project": gold_module["project"],
        "gold_path": gold_module["path"],
        "gold_evidence": evidence,
        "notes": notes,
        "module_snapshot": module_brief(gold_module),
    })
    return True


def build_easy(modules, port_to_modules, target=50):
    rows = []
    used = set()
    exact_candidates = [m for m in modules if trustworthy_name(m)]
    for module in sorted(exact_candidates, key=lambda m: (m["project"], m["name"])):
        if len(rows) >= target:
            break
        if add_question(
            rows, used, f"easy-name-{module['project']}-{module['name']}", "easy", "exact_name",
            f"Which module named `{module['name']}` should be returned from the current RTL knowledge DB?",
            module,
            [f"module.name={module['name']}"],
            "Exact entity lookup.",
        ) and len(rows) >= target:
            break
    for port, module in unique_port_candidates(modules, port_to_modules):
        if len(rows) >= target:
            break
        add_question(
            rows, used, f"easy-port-{module['project']}-{port}", "easy", "unique_port",
            f"Find the `{module['project']}` module that exposes the unique port `{port}`.",
            module,
            [f"unique port {port}"],
            "Single strong port clue.",
        )
    return rows[:target]


def build_medium(modules, port_to_modules, child_to_parents, path_token_to_modules, target=50):
    rows = []
    used = set()
    for module in sorted(modules, key=lambda m: (-len(m.get("labels", [])), -len(m["ports"]))):
        if len(rows) >= target:
            break
        labels = [l for l in module.get("labels", []) if l and l.lower() not in {"clocked", "resettable", "hierarchical"}]
        if len(labels) >= 1 and len(module["ports"]) >= 2:
            label_word = select_synonym(labels[0])
            p1 = module["ports"][0]["name"]
            p2 = module["ports"][1]["name"]
            add_question(
                rows, used, f"medium-label-port-{module['project']}-{module['name']}", "medium", "label_plus_ports",
                f"Which `{module['project']}` module behaves like a `{label_word}` block and includes ports `{p1}` and `{p2}`?",
                module,
                [f"label {labels[0]}", f"ports {p1},{p2}"],
                "Needs label + port matching.",
            )
        if len(rows) >= target:
            break
        if module["instances"]:
            child = module["instances"][0]["type"]
            if child.lower() not in RESERVED:
                add_question(
                    rows, used, f"medium-parent-child-{module['project']}-{module['name']}-{child}", "medium", "parent_child",
                    f"Find the module in `{module['project']}` that instantiates `{child}` and is implemented at `{Path(module['path']).name}`.",
                    module,
                    [f"instantiates {child}", f"path {Path(module['path']).name}"],
                    "Combines file-level and child-instance evidence.",
                )
        if len(rows) >= target:
            break
        path_tokens = [t for t in re.split(r"[^a-zA-Z0-9_]+", module["path"].lower()) if len(t) > 3]
        uncommon = next((t for t in path_tokens if len(path_token_to_modules[t]) == 1), None)
        if uncommon and module["ports"]:
            port = module["ports"][-1]["name"]
            add_question(
                rows, used, f"medium-path-port-{module['project']}-{module['name']}", "medium", "path_plus_port",
                f"Which module belongs to the `{uncommon}` path region and still exposes port `{port}`?",
                module,
                [f"path token {uncommon}", f"port {port}"],
                "Path-derived routing clue plus interface clue.",
            )
    return rows[:target]


def build_hard(modules, child_to_parents, target=50):
    rows = []
    used = set()
    type_caps = {"reverse_graph": 20, "multi_hop": 15, "semantic_bridge": 15}
    type_counts = Counter()
    for child, parents in sorted(child_to_parents.items(), key=lambda item: (-len(item[1]), item[0])):
        if len(rows) >= target:
            break
        if type_counts["reverse_graph"] >= type_caps["reverse_graph"]:
            break
        unique_parents = {p["name"]: p for p in parents}
        if len(unique_parents) != 1:
            continue
        parent = next(iter(unique_parents.values()))
        labels = [l for l in parent.get("labels", []) if l]
        if len(labels) < 2:
            continue
        phrase_a = select_synonym(labels[0])
        phrase_b = select_synonym(labels[1])
        if add_question(
            rows, used, f"hard-reverse-{parent['project']}-{parent['name']}-{child}", "hard", "reverse_graph",
            f"Which parent module in `{parent['project']}` wraps child `{child}` and also looks like a `{phrase_a}` / `{phrase_b}` block?",
            parent,
            [f"reverse edge from child {child}", f"labels {labels[0]},{labels[1]}"],
            "Requires reverse connectivity plus semantic label reasoning.",
        ):
            type_counts["reverse_graph"] += 1

    candidates = sorted(modules, key=lambda m: (-len(m["instances"]), -len(m.get("labels", [])), m["name"]))
    for module in candidates:
        if len(rows) >= target:
            break
        if type_counts["multi_hop"] >= type_caps["multi_hop"]:
            break
        if len(module["instances"]) < 2 or len(module["ports"]) < 2 or len(module.get("labels", [])) < 2:
            continue
        inst_a = module["instances"][0]["type"]
        inst_b = module["instances"][1]["type"]
        label_phrase = select_synonym(module["labels"][0])
        port_phrase = module["ports"][0]["name"]
        if add_question(
            rows, used, f"hard-multihop-{module['project']}-{module['name']}", "hard", "multi_hop",
            f"Find the `{module['project']}` wrapper that behaves like `{label_phrase}`, instantiates both `{inst_a}` and `{inst_b}`, and still exposes `{port_phrase}`.",
            module,
            [f"instances {inst_a},{inst_b}", f"label {module['labels'][0]}", f"port {port_phrase}"],
            "Multi-clue retrieval over interface, graph, and semantic abstraction.",
        ):
            type_counts["multi_hop"] += 1

    for module in candidates:
        if len(rows) >= target:
            break
        if type_counts["semantic_bridge"] >= type_caps["semantic_bridge"]:
            break
        labels = module.get("labels", [])
        if not {"clocked", "resettable"}.issubset(set(labels)) or not module["instances"]:
            continue
        child = module["instances"][-1]["type"]
        phrase = select_synonym(random.choice(labels))
        if add_question(
            rows, used, f"hard-semantic-{module['project']}-{module['name']}-{child}", "hard", "semantic_bridge",
            f"Which module would best answer a query for a `{phrase}` bridge that synchronizes around child `{child}` in `{module['project']}`?",
            module,
            [f"semantic phrase {phrase}", f"child {child}", "clocked/resettable"],
            "Semantic clue wording without direct module name.",
        ):
            type_counts["semantic_bridge"] += 1
    return rows[:target]


def ensure_count(rows, expected, label):
    if len(rows) < expected:
        raise RuntimeError(f"Could not build {expected} {label} questions; built {len(rows)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", required=True)
    ap.add_argument("--labels", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--count-per-level", type=int, default=50)
    ap.add_argument("--random-seed", type=int, default=7)
    args = ap.parse_args()

    random.seed(args.random_seed)
    out_dir = Path(args.out_dir)

    modules = clean_modules(read_jsonl(args.seed))
    _labels = read_jsonl(args.labels)
    port_to_modules, label_to_modules, child_to_parents, path_token_to_modules = build_indexes(modules)

    easy = build_easy(modules, port_to_modules, args.count_per_level)
    medium = build_medium(modules, port_to_modules, child_to_parents, path_token_to_modules, args.count_per_level)
    hard = build_hard(modules, child_to_parents, args.count_per_level)

    ensure_count(easy, args.count_per_level, "easy")
    ensure_count(medium, args.count_per_level, "medium")
    ensure_count(hard, args.count_per_level, "hard")

    all_rows = easy + medium + hard
    summary = {
        "easy": len(easy),
        "medium": len(medium),
        "hard": len(hard),
        "total": len(all_rows),
        "projects": dict(Counter(row["gold_project"] for row in all_rows)),
        "types": dict(Counter(row["type"] for row in all_rows)),
    }

    write_jsonl(out_dir / "benchmark_all.jsonl", all_rows)
    write_jsonl(out_dir / "benchmark_easy.jsonl", easy)
    write_jsonl(out_dir / "benchmark_medium.jsonl", medium)
    write_jsonl(out_dir / "benchmark_hard.jsonl", hard)
    write_json(out_dir / "benchmark_summary.json", summary)
    write_markdown_catalog(out_dir / "benchmark_catalog.md", [
        ("Easy (50)", easy),
        ("Medium (50)", medium),
        ("Hard (50)", hard),
    ])
    print(json.dumps({"status": "ok", "out_dir": str(out_dir), **summary}, ensure_ascii=False))


if __name__ == "__main__":
    main()
