#!/usr/bin/env python3
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

RESERVED = {
    "if", "for", "while", "case", "module", "interface", "end", "begin",
    "generate", "assign", "always", "function", "task", "unique", "auto",
    "is", "tb", "to", "can", "contains", "checks", "values",
}

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "current", "db",
    "do", "does", "each", "explain", "facts", "file", "find", "for",
    "from", "high", "how", "in", "into", "it", "its", "knowledge",
    "level", "like", "module", "modules", "of", "only", "or", "path",
    "ports", "project", "query", "return", "returned", "should", "short",
    "summary", "terms", "the", "this", "top", "using", "what", "which",
    "with", "write",
}

PATH_EXCLUDES = [
    "\\dv\\", "\\tb", "\\formal\\", "\\pre_sca\\", "\\lint\\",
    "\\fpv\\", "\\doc\\",
]

EXPANSIONS = {
    "serial": ["uart", "spi", "i2c", "rx", "tx", "mosi", "miso", "scl", "sda"],
    "bus": ["spi", "i2c", "tlul", "uart", "apb"],
    "controller": ["controller", "ctrl", "fsm", "state"],
    "control": ["controller", "ctrl", "fsm", "state"],
    "queue": ["fifo", "buffer"],
    "buffer": ["fifo", "queue"],
    "memory": ["memory", "ram", "rom", "regfile", "csr", "flash"],
    "storage": ["memory", "ram", "rom", "regfile", "flash"],
    "crypto": ["crypto", "aes", "hmac", "kmac", "csrng", "cipher", "hash"],
    "cryptographic": ["crypto", "aes", "hmac", "kmac", "cipher", "hash"],
    "wrapper": ["hierarchical", "wrapper", "parent"],
    "parent": ["hierarchical", "wrapper"],
    "sequential": ["clocked", "clk"],
    "reset": ["resettable", "rst", "reset"],
    "bridge": ["cdc", "async", "fifo", "adapter"],
    "synchronizes": ["cdc", "sync", "async"],
    "timer": ["counter", "timer"],
    "register": ["reg", "regfile", "csr", "register"],
    "bank": ["regfile", "csr", "register"],
    "cpu": ["ibex", "core", "rv32"],
    "pipeline": ["ibex", "stage", "decoder", "alu"],
}

GENERIC_LABELS = {"clocked", "resettable", "hierarchical", "opentitan_ip", "ibex_core"}

BASELINE_WEIGHTS = {
    "name": 6.0,
    "project": 0.8,
    "path": 1.0,
    "path_file": 3.5,
    "ports": 2.4,
    "instances": 3.0,
    "instance_names": 1.2,
}

KG_WEIGHTS = {
    **BASELINE_WEIGHTS,
    "labels": 1.7,
    "summary": 0.6,
    "parents": 1.1,
}

IDENT_RE = re.compile(r"[a-zA-Z0-9_$]+")
QUOTED_RE = re.compile(r"`([^`]+)`")


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


def normalized_path(path):
    return str(path).lower().replace("/", "\\")


def tokenize(text):
    out = []
    for raw in IDENT_RE.findall(str(text).lower()):
        if len(raw) <= 1 or raw in STOPWORDS:
            continue
        out.append(raw)
        for part in re.split(r"[_$]+", raw):
            if len(part) > 1 and part not in STOPWORDS and part != raw:
                out.append(part)
    return out


def token_set(text):
    return set(tokenize(text))


def clean_module(row):
    if row.get("entity_type") != "module":
        return None
    name = row.get("name", "")
    name_l = name.lower()
    path_l = normalized_path(row.get("path", ""))
    if any(token in path_l for token in PATH_EXCLUDES):
        return None
    if not name or name_l in RESERVED or name_l in STOPWORDS or len(name) < 3:
        return None
    if sum(ch.isalpha() for ch in name) < 3:
        return None
    if re.fullmatch(r"[a-z]+", name_l) and name_l not in path_l:
        return None

    module = dict(row)
    module["ports"] = [
        p for p in row.get("ports", [])
        if p.get("name") and p["name"].lower() not in RESERVED and p["name"].lower() not in STOPWORDS
    ]
    module["instances"] = [
        i for i in row.get("instances", [])
        if i.get("type") and i["type"].lower() not in RESERVED and i["type"].lower() not in STOPWORDS
    ]
    module["labels"] = sorted(set(row.get("labels", [])))
    return module


def load_modules(seed_path):
    modules = []
    for row in read_jsonl(seed_path):
        module = clean_module(row)
        if module is not None:
            modules.append(module)
    return modules


def resolve_approved_labels_path(seed_path, provided=None):
    if provided:
        path = Path(provided)
        return path if path.exists() else None
    candidate = Path(seed_path).parent / "label_approval" / "auto_approved_labels.jsonl"
    return candidate if candidate.exists() else None


def apply_approved_labels(modules, approved_path):
    if not approved_path:
        return {"path": None, "module_labels_added": 0, "ip_context_labels_added": 0}

    module_labels = defaultdict(set)
    ip_prefix_labels = []
    for row in read_jsonl(approved_path):
        decision = row.get("decision", "")
        review_state = row.get("review_state", "")
        if decision != "auto_approved" and review_state not in {"approved", "reviewed"}:
            continue
        label = str(row.get("label", "")).lower()
        if not label:
            continue
        entity_type = row.get("entity_type")
        project = row.get("project", "")
        target = row.get("target_name", "")
        if entity_type == "label_proposal" and target:
            module_labels[(project, target)].add(label)
        elif entity_type == "ip_block" and row.get("group") in {"protocol", "role"}:
            ip_prefix_labels.append((project, normalized_path(row.get("path", "")), label))

    module_added = 0
    ip_added = 0
    for module in modules:
        labels = set(module.get("labels", []))
        before = len(labels)
        labels.update(module_labels.get((module.get("project", ""), module.get("name", "")), set()))
        module_added += len(labels) - before

        path_l = normalized_path(module.get("path", ""))
        before = len(labels)
        for project, prefix, label in ip_prefix_labels:
            if project == module.get("project", "") and prefix and path_l.startswith(prefix):
                labels.add(label)
        ip_added += len(labels) - before
        module["labels"] = sorted(labels)

    return {
        "path": str(approved_path),
        "module_labels_added": module_added,
        "ip_context_labels_added": ip_added,
    }


def build_reverse_graph(modules):
    child_to_parents = defaultdict(list)
    for module in modules:
        for inst in module.get("instances", []):
            child_to_parents[inst["type"]].append(module["name"])
    return child_to_parents


def module_features(module, child_to_parents):
    path = Path(module.get("path", ""))
    ports = [p.get("name", "") for p in module.get("ports", [])]
    inst_types = [i.get("type", "") for i in module.get("instances", [])]
    inst_names = [i.get("name", "") for i in module.get("instances", [])]
    parents = child_to_parents.get(module.get("name", ""), [])
    labels = module.get("labels", [])
    fields = {
        "name": token_set(module.get("name", "")),
        "project": token_set(module.get("project", "")),
        "path": token_set(module.get("path", "")),
        "path_file": token_set(path.name),
        "ports": token_set(" ".join(ports)),
        "instances": token_set(" ".join(inst_types)),
        "instance_names": token_set(" ".join(inst_names)),
        "labels": token_set(" ".join(labels)),
        "summary": token_set(module.get("summary", "")),
        "parents": token_set(" ".join(parents)),
    }
    return {
        "fields": fields,
        "name_exact": module.get("name", "").lower(),
        "project_exact": module.get("project", "").lower(),
        "path_file_exact": path.name.lower(),
        "path_stem_exact": path.stem.lower(),
        "ports_exact": {p.lower() for p in ports},
        "instances_exact": {i.lower() for i in inst_types},
        "labels_exact": {l.lower() for l in labels},
        "parents_exact": {p.lower() for p in parents},
    }


def attach_features(modules, child_to_parents):
    for module in modules:
        module["_features"] = module_features(module, child_to_parents)


def build_idf(modules, mode):
    weights = KG_WEIGHTS if mode == "kg" else BASELINE_WEIGHTS
    df = Counter()
    for module in modules:
        tokens = set()
        for field in weights:
            tokens.update(module["_features"]["fields"].get(field, set()))
        for token in tokens:
            df[token] += 1
    total = max(1, len(modules))
    return {token: 1.0 + math.log((total + 1.0) / (count + 0.5)) for token, count in df.items()}


def expand_terms(tokens):
    expanded = set()
    for token in tokens:
        for item in EXPANSIONS.get(token, []):
            expanded.update(tokenize(item))
    return expanded.difference(tokens)


def extract_anchors(question):
    target_anchors = set()
    child_anchors = set()
    path_anchors = set()
    question_l = question.lower()
    for match in QUOTED_RE.finditer(question):
        value = match.group(1).strip().lower()
        before = question_l[max(0, match.start() - 55):match.start()]
        if value.endswith((".v", ".sv", ".vh", ".svh")):
            path_anchors.add(value)
        elif re.search(r"(child|children|instantiat|wraps|wrapped|reused child|shared child)", before):
            child_anchors.add(value)
        else:
            target_anchors.add(value)
    return target_anchors, child_anchors, path_anchors


def add(reason_rows, amount, reason):
    if amount:
        reason_rows.append((amount, reason))
    return amount


def field_overlap_score(fields, query_tokens, weights, idf, factor, reason_rows):
    score = 0.0
    for field, weight in weights.items():
        overlap = fields.get(field, set()).intersection(query_tokens)
        if not overlap:
            continue
        for token in overlap:
            token_factor = 0.35 if field == "labels" and token in GENERIC_LABELS else 1.0
            amount = weight * idf.get(token, 1.0) * factor * token_factor
            score += add(reason_rows, amount, f"{field}:{token}")
    return score


def score_module(module, question, mode, idf, known_projects):
    features = module["_features"]
    fields = features["fields"]
    query_tokens = set(tokenize(question))
    expanded_tokens = expand_terms(query_tokens) if mode == "kg" else set()
    target_anchors, child_anchors, path_anchors = extract_anchors(question)
    weights = KG_WEIGHTS if mode == "kg" else BASELINE_WEIGHTS
    reasons = []
    score = 0.0

    score += field_overlap_score(fields, query_tokens, weights, idf, 1.0, reasons)
    if expanded_tokens:
        score += field_overlap_score(fields, expanded_tokens, weights, idf, 0.28, reasons)

    name = features["name_exact"]
    if name in target_anchors or name in query_tokens:
        score += add(reasons, 16.0, "module_name")
    if features["path_stem_exact"] in target_anchors and features["path_stem_exact"] != name:
        score += add(reasons, 8.0, "path_stem")
    if features["path_file_exact"] in path_anchors:
        score += add(reasons, 8.0, "path_file")

    for anchor in target_anchors:
        if anchor in features["ports_exact"]:
            score += add(reasons, 4.5, f"port:{anchor}")
        if anchor in features["instances_exact"]:
            score += add(reasons, 5.5, f"instance:{anchor}")
        if anchor in features["labels_exact"] and mode == "kg":
            score += add(reasons, 2.5, f"label:{anchor}")

    for child in child_anchors:
        if child in features["instances_exact"]:
            score += add(reasons, 10.0, f"child_instance:{child}")
        if name == child:
            score -= add(reasons, 5.0, "child_anchor_penalty")

    projects_in_query = known_projects.intersection(query_tokens)
    if projects_in_query:
        if features["project_exact"] in projects_in_query:
            score += add(reasons, 2.0, "project_match")
        else:
            score -= add(reasons, 1.2, "project_mismatch")

    if mode == "kg" and {"parent", "wrapper", "hierarchy", "hierarchical"}.intersection(query_tokens):
        if module.get("instances"):
            score += add(reasons, 0.8, "hierarchy_context")
        if features["parents_exact"]:
            score += add(reasons, 0.5, "reverse_context")

    reasons = [reason for _, reason in sorted(reasons, key=lambda item: -abs(item[0]))[:8]]
    return score, reasons


def retrieve(question, modules, mode, k=5):
    idf = question["_idf"][mode]
    known_projects = question["_known_projects"]
    results = []
    for module in modules:
        score, reasons = score_module(module, question["question"], mode, idf, known_projects)
        if score > 0.1:
            results.append({
                "name": module["name"],
                "project": module["project"],
                "score": round(score, 3),
                "reasons": reasons,
            })
    results.sort(key=lambda row: (-row["score"], row["project"], row["name"]))
    return results[:k]


def prepare_retrieval(seed_path, approved_labels=None):
    modules = load_modules(seed_path)
    approved_path = resolve_approved_labels_path(seed_path, approved_labels)
    approved_summary = apply_approved_labels(modules, approved_path)
    child_to_parents = build_reverse_graph(modules)
    attach_features(modules, child_to_parents)
    idf_by_mode = {
        "baseline": build_idf(modules, "baseline"),
        "kg": build_idf(modules, "kg"),
    }
    known_projects = {m.get("project", "").lower() for m in modules}
    return modules, idf_by_mode, known_projects, approved_summary


def rank_of(golds, results):
    gold_set = set(golds if isinstance(golds, list) else [golds])
    for idx, row in enumerate(results, start=1):
        if row["name"] in gold_set:
            return idx
    return None
