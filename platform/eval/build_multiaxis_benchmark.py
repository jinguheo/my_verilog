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
GENERIC_LABELS = {"clocked", "resettable", "hierarchical", "opentitan_ip", "ibex_core"}
LEVELS = ["L1", "L2", "L3", "L4", "L5"]
TYPES = [
    "structure_understanding",
    "search_navigation",
    "comparison_similarity",
    "function_similarity",
    "generation_design",
    "code_explanation",
    "documentation_summary",
]


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


def pick_label(module, default="hierarchical"):
    labels = [l for l in module.get("labels", []) if l not in GENERIC_LABELS]
    return random.choice(labels) if labels else default


def module_snapshot(module):
    return {
        "name": module["name"],
        "project": module["project"],
        "path": module["path"],
        "labels": module.get("labels", []),
        "ports": [p["name"] for p in module.get("ports", [])[:12]],
        "instances": [i["type"] for i in module.get("instances", [])[:12]],
    }


def add_question(bucket, used, level, qtype, prompt, gold_modules, evidence, notes):
    key = (level, qtype, tuple(sorted(m["name"] for m in gold_modules)), prompt)
    if key in used:
        return False
    used.add(key)
    bucket.append({
        "level": level,
        "type": qtype,
        "question": prompt,
        "gold_modules": [m["name"] for m in gold_modules],
        "gold_projects": sorted({m["project"] for m in gold_modules}),
        "gold_paths": [m["path"] for m in gold_modules],
        "gold_evidence": evidence,
        "notes": notes,
        "module_snapshots": [module_snapshot(m) for m in gold_modules],
    })
    return True


def build_indexes(modules):
    by_project = defaultdict(list)
    by_label = defaultdict(list)
    by_port = defaultdict(list)
    by_name = {}
    child_to_parents = defaultdict(list)
    for m in modules:
        by_project[m["project"]].append(m)
        by_name[m["name"]] = m
        for label in m.get("labels", []):
            by_label[label].append(m)
        for p in m.get("ports", []):
            by_port[p["name"]].append(m)
        for inst in m.get("instances", []):
            child_to_parents[inst["type"]].append(m)
    return by_project, by_label, by_port, by_name, child_to_parents


def trustworthy_modules(modules):
    out = []
    for m in modules:
        stem = Path(m["path"]).stem.lower()
        name = m["name"].lower()
        if name in stem or stem in name:
            out.append(m)
    return out


def choose_pairs(modules):
    pairs = []
    for i in range(len(modules)):
        for j in range(i + 1, len(modules)):
            a, b = modules[i], modules[j]
            if a["project"] == b["project"]:
                pairs.append((a, b))
    return pairs


def module_label_support(module, label, include_instances=True):
    label_tokens = set(re.split(r"[_$]+", label.lower()))
    name = module["name"].lower()
    path_file = Path(module["path"]).name.lower()
    ports = " ".join(p["name"].lower() for p in module.get("ports", []))
    instances = " ".join(i["type"].lower() for i in module.get("instances", []))
    if label in name or label in path_file or label_tokens.intersection(set(re.split(r"[^a-zA-Z0-9_]+", name + " " + path_file))):
        return "name_or_file"
    if label in ports or label_tokens.intersection(set(re.split(r"[^a-zA-Z0-9_]+", ports))):
        return "interface"
    if include_instances and (label in instances or label_tokens.intersection(set(re.split(r"[^a-zA-Z0-9_]+", instances)))):
        return "child_graph"
    return None


def canonical_label_key(row, parent_counts=None):
    label, module, support = row
    support_rank = {"name_or_file": 0, "interface": 1, "child_graph": 2}
    name = module["name"].lower()
    path_file = Path(module["path"]).name.lower()
    ports = " ".join(p["name"].lower() for p in module.get("ports", []))
    instances = " ".join(i["type"].lower() for i in module.get("instances", []))
    parent_count = (parent_counts or {}).get(module["name"], 0)
    representativeness = 0.0
    if name == label:
        representativeness += 20.0
    if label in name:
        representativeness += 10.0
    if label in path_file:
        representativeness += 8.0
    if label in ports:
        representativeness += 6.0
    if label in instances:
        representativeness += 6.0
    if label in module.get("labels", []):
        representativeness += 5.0
    representativeness += min(parent_count, 12) * 0.8
    exact = 0 if name == label else 1
    core_name = 0 if name.endswith(f"_{label}") or name.startswith(f"{label}_") else 1
    return (
        support_rank[support],
        -representativeness,
        exact,
        core_name,
        len(name),
        module["project"],
        module["name"],
    )


def strong_label_examples(modules, direct_only=False, parent_counts=None):
    examples = []
    for module in modules:
        for label in module.get("labels", []):
            if label in GENERIC_LABELS:
                continue
            support = module_label_support(module, label, include_instances=not direct_only)
            if not support:
                continue
            examples.append((label, module, support))
    examples.sort(key=lambda row: (row[0], canonical_label_key(row, parent_counts)))
    return examples


def strong_label_owners(modules, parent_counts=None):
    by_label = defaultdict(list)
    seen = defaultdict(set)
    for label, module, _support in strong_label_examples(modules, parent_counts=parent_counts):
        key = module["name"]
        if key not in seen[label]:
            by_label[label].append(module)
            seen[label].add(key)
    return by_label


def representative_label_examples(modules, parent_counts=None):
    by_label = defaultdict(list)
    for row in strong_label_examples(modules, direct_only=True, parent_counts=parent_counts):
        by_label[row[0]].append(row)
    reps = [rows[0] for _label, rows in sorted(by_label.items())]
    reps.sort(key=lambda row: (-len(by_label[row[0]]), row[0], canonical_label_key(row, parent_counts)))
    return reps


def shared_label_pairs(by_label, same_project=None):
    rows = []
    for label, owners in sorted(by_label.items()):
        for i in range(len(owners)):
            for j in range(i + 1, len(owners)):
                a, b = owners[i], owners[j]
                if same_project is True and a["project"] != b["project"]:
                    continue
                if same_project is False and a["project"] == b["project"]:
                    continue
                rows.append((label, a, b))
    rows.sort(key=lambda row: (row[0], row[1]["project"], row[1]["name"], row[2]["project"], row[2]["name"]))
    return rows


def unique_by_name(rows):
    out = []
    seen = set()
    for row in rows:
        if row["name"] in seen:
            continue
        seen.add(row["name"])
        out.append(row)
    return out


def graph_parent_priority(parent, child):
    child_l = child.lower()
    child_tokens = set(re.split(r"[_$]+", child_l))
    inst_types = [i.get("type", "").lower() for i in parent.get("instances", [])]
    inst_names = [i.get("name", "").lower() for i in parent.get("instances", [])]
    ports = [p.get("name", "").lower() for p in parent.get("ports", [])]
    hay_tokens = set(re.split(r"[^a-zA-Z0-9_]+", " ".join(inst_types + inst_names + ports + [parent["name"].lower(), parent["path"].lower()])))
    exact_child_count = sum(1 for inst in inst_types if inst == child_l)
    token_hits = len(child_tokens.intersection(hay_tokens))
    return (
        -exact_child_count,
        -token_hits,
        -len(parent.get("instances", [])),
        -len(parent.get("ports", [])),
        parent["project"],
        parent["name"],
    )


def prioritized_parents(parents, child, limit):
    return sorted(unique_by_name(parents), key=lambda parent: graph_parent_priority(parent, child))[:limit]


def generate_questions(modules, per_cell):
    by_project, by_label, by_port, by_name, child_to_parents = build_indexes(modules)
    used = set()
    rows = []

    trusted = trustworthy_modules(sorted(modules, key=lambda m: (m["project"], m["name"])))
    complex_modules = sorted(modules, key=lambda m: (-len(m["instances"]), -len(m["ports"]), m["name"]))
    pairs = choose_pairs(complex_modules[:120])
    parent_counts = {child: len(unique_by_name(parents)) for child, parents in child_to_parents.items()}
    direct_label_examples = representative_label_examples(modules, parent_counts)
    by_strong_label = strong_label_owners(modules, parent_counts)
    same_project_label_pairs = shared_label_pairs(by_strong_label, same_project=True)
    cross_project_label_pairs = shared_label_pairs(by_strong_label, same_project=False)

    # L1
    for m in trusted[:per_cell]:
        add_question(rows, used, "L1", "search_navigation",
            f"Find the module named `{m['name']}` in the current RTL knowledge DB.",
            [m], [f"module.name={m['name']}"], "Direct lookup.")
    for m in complex_modules[:per_cell]:
        add_question(rows, used, "L1", "structure_understanding",
            f"What are the top-level ports and child instances of module `{m['name']}`?",
            [m], ["top-level ports", "direct instances"], "Single-module structure read.")
    for m in complex_modules[per_cell:2*per_cell]:
        add_question(rows, used, "L1", "code_explanation",
            f"Explain in simple terms what module `{m['name']}` appears to do from its ports, labels, and file path.",
            [m], ["ports", "labels", "path"], "Simple code understanding.")
    for m in complex_modules[2*per_cell:3*per_cell]:
        add_question(rows, used, "L1", "documentation_summary",
            f"Write a short design-note summary for module `{m['name']}` using only the current knowledge DB facts.",
            [m], ["summary", "labels", "ports"], "Single-module summary.")
    for label, m, support in direct_label_examples[:per_cell]:
        add_question(rows, used, "L1", "function_similarity",
            f"Which module is tagged as `{label}` and would be the most direct example of that function?",
            [m], [f"label={label}", f"support={support}"], "Single-label function lookup with direct evidence.")
    for m in complex_modules[4*per_cell:5*per_cell]:
        add_question(rows, used, "L1", "generation_design",
            f"If you needed a very small wrapper around `{m['name']}`, which existing module should you inspect first as the reference block?",
            [m], ["reference module"], "Low-complexity design reference lookup.")
    for a, b in pairs[:per_cell]:
        add_question(rows, used, "L1", "comparison_similarity",
            f"Compare `{a['name']}` and `{b['name']}` at a high level using only project, labels, ports, and instance counts.",
            [a, b], ["project", "labels", "counts"], "High-level similarity question.")

    # L2
    idx = 0
    for m in complex_modules:
        if Counter(r["type"] for r in rows if r["level"] == "L2")["structure_understanding"] >= per_cell:
            break
        if len(m["ports"]) >= 2 and m["instances"]:
            add_question(rows, used, "L2", "structure_understanding",
                f"Describe how `{m['name']}` is structured by relating ports `{m['ports'][0]['name']}`, `{m['ports'][1]['name']}` and child `{m['instances'][0]['type']}`.",
                [m], ["two ports", "one child instance"], "Multi-clue structure read.")
    for m in complex_modules:
        if Counter(r["type"] for r in rows if r["level"] == "L2")["search_navigation"] >= per_cell:
            break
        if m["ports"]:
            port = m["ports"][-1]["name"]
            add_question(rows, used, "L2", "search_navigation",
                f"Find the `{m['project']}` module that combines port `{port}` with the path `{Path(m['path']).name}`.",
                [m], [f"path={Path(m['path']).name}", f"port={port}"], "Path + port lookup.")
    for a, b in pairs[per_cell:per_cell*2]:
        if Counter(r["type"] for r in rows if r["level"] == "L2")["comparison_similarity"] >= per_cell:
            break
        add_question(rows, used, "L2", "comparison_similarity",
            f"Which of `{a['name']}` and `{b['name']}` are structurally closer based on shared labels and interface shape?",
            [a, b], ["shared labels", "interface shape"], "Pairwise structural comparison.")
    for label, owners in sorted(by_strong_label.items(), key=lambda item: (-len(item[1]), item[0])):
        if Counter(r["type"] for r in rows if r["level"] == "L2")["function_similarity"] >= per_cell:
            break
        if len(owners) >= 2:
            chosen = owners[:2]
            add_question(rows, used, "L2", "function_similarity",
                f"Find two modules that both behave like `{label}` blocks and explain the common function.",
                chosen, [f"label={label}", "strong label evidence"], "Shared function via grounded label.")
    for m in complex_modules[20:]:
        if Counter(r["type"] for r in rows if r["level"] == "L2")["generation_design"] >= per_cell:
            break
        if m["instances"]:
            add_question(rows, used, "L2", "generation_design",
                f"If you were generating a thin wrapper around `{m['name']}`, which child block and interface signals must be preserved first?",
                [m], [f"child={m['instances'][0]['type']}"], "Wrapper-oriented prompt.")
    for m in complex_modules[30:]:
        if Counter(r["type"] for r in rows if r["level"] == "L2")["code_explanation"] >= per_cell:
            break
        if m["ports"]:
            add_question(rows, used, "L2", "code_explanation",
                f"Explain the likely role of `{m['name']}` from labels `{', '.join(m.get('labels', [])[:3])}` and ports like `{m['ports'][0]['name']}`.",
                [m], ["labels", "representative port"], "Clue-based explanation.")
    for m in complex_modules[40:]:
        if Counter(r["type"] for r in rows if r["level"] == "L2")["documentation_summary"] >= per_cell:
            break
        add_question(rows, used, "L2", "documentation_summary",
            f"Summarize `{m['name']}` for an engineer who only needs interface, role, and integration context.",
            [m], ["interface", "role", "integration"], "Engineer-facing summary.")

    # L3
    for m in complex_modules:
        if Counter(r["type"] for r in rows if r["level"] == "L3")["structure_understanding"] >= per_cell:
            break
        if len(m["instances"]) >= 2:
            add_question(rows, used, "L3", "structure_understanding",
                f"Reconstruct the local hierarchy under `{m['name']}` and explain what each major child likely contributes.",
                [m], ["multiple child instances", "local hierarchy"], "Hierarchy interpretation.")
    for child, parents in child_to_parents.items():
        if Counter(r["type"] for r in rows if r["level"] == "L3")["search_navigation"] >= per_cell:
            break
        uniq = {p['name']: p for p in parents}
        if len(uniq) == 1:
            parent = next(iter(uniq.values()))
            add_question(rows, used, "L3", "search_navigation",
                f"Which parent module should be retrieved if the query is centered on child `{child}` rather than the parent name itself?",
                [parent], [f"reverse edge from child {child}"], "Reverse navigation.")
    for a, b in pairs[25:]:
        if Counter(r["type"] for r in rows if r["level"] == "L3")["comparison_similarity"] >= per_cell:
            break
        if set(a.get("labels", [])).intersection(set(b.get("labels", []))):
            add_question(rows, used, "L3", "comparison_similarity",
                f"Compare `{a['name']}` and `{b['name']}` as candidate alternatives for the same subsystem role.",
                [a, b], ["shared labels", "subsystem role"], "Alternative design comparison.")
    for label, a, b in cross_project_label_pairs:
        if Counter(r["type"] for r in rows if r["level"] == "L3")["function_similarity"] >= per_cell:
            break
        add_question(rows, used, "L3", "function_similarity",
            f"Find cross-project modules that both implement a `{label}`-like function and explain the commonality.",
            [a, b], [f"shared cross-project label {label}"], "Cross-project function similarity.")
    for m in complex_modules[60:]:
        if Counter(r["type"] for r in rows if r["level"] == "L3")["generation_design"] >= per_cell:
            break
        if len(m["ports"]) >= 2 and m["instances"]:
            add_question(rows, used, "L3", "generation_design",
                f"Create a design brief for generating a compatible block around `{m['name']}` without breaking ports `{m['ports'][0]['name']}` and `{m['ports'][1]['name']}`.",
                [m], ["compatibility brief", "interface constraints"], "Mid-level design planning.")
    for m in complex_modules[70:]:
        if Counter(r["type"] for r in rows if r["level"] == "L3")["code_explanation"] >= per_cell:
            break
        if len(m.get("labels", [])) >= 2:
            add_question(rows, used, "L3", "code_explanation",
                f"Explain why `{m['name']}` probably exists in the design, using both its semantic labels and its child-instance graph.",
                [m], ["semantic labels", "child graph"], "Purpose explanation with graph evidence.")
    for m in complex_modules[80:]:
        if Counter(r["type"] for r in rows if r["level"] == "L3")["documentation_summary"] >= per_cell:
            break
        add_question(rows, used, "L3", "documentation_summary",
            f"Write a module reference summary for `{m['name']}` including role, interface shape, and where it sits in the hierarchy.",
            [m], ["role", "interface", "hierarchy"], "Reference-style summary.")

    # L4
    for m in complex_modules[90:]:
        if Counter(r["type"] for r in rows if r["level"] == "L4")["structure_understanding"] >= per_cell:
            break
        if len(m["instances"]) >= 3:
            add_question(rows, used, "L4", "structure_understanding",
                f"Explain the structural decomposition of `{m['name']}` and how its major children likely partition responsibilities.",
                [m], ["multi-child decomposition"], "Deeper structural reasoning.")
    for child, parents in sorted(child_to_parents.items(), key=lambda item: -len(item[1])):
        if Counter(r["type"] for r in rows if r["level"] == "L4")["search_navigation"] >= per_cell:
            break
        if len(parents) >= 2:
            chosen = prioritized_parents(parents, child, 2)
            if len(chosen) < 2:
                continue
            add_question(rows, used, "L4", "search_navigation",
                f"If the query starts from reused child `{child}`, which parent contexts should a graph-aware search inspect first?",
                chosen, [f"shared child {child}"], "Graph-aware ambiguous navigation.")
    for a, b in pairs[100:]:
        if Counter(r["type"] for r in rows if r["level"] == "L4")["comparison_similarity"] >= per_cell:
            break
        if len(a["instances"]) >= 2 and len(b["instances"]) >= 2:
            add_question(rows, used, "L4", "comparison_similarity",
                f"Compare `{a['name']}` and `{b['name']}` as architectural wrappers, focusing on hierarchy, integration points, and likely subsystem boundaries.",
                [a, b], ["wrapper architecture", "integration points"], "Architectural comparison.")
    for label, a, b in same_project_label_pairs:
        if Counter(r["type"] for r in rows if r["level"] == "L4")["function_similarity"] >= per_cell:
            break
        add_question(rows, used, "L4", "function_similarity",
            f"Which two modules would you shortlist as functionally similar candidates for `{label}` behavior, and why?",
            [a, b], [f"shared grounded label {label}"], "Higher-level shortlist reasoning.")
    for m in complex_modules[130:]:
        if Counter(r["type"] for r in rows if r["level"] == "L4")["generation_design"] >= per_cell:
            break
        if len(m["instances"]) >= 2 and len(m["ports"]) >= 2:
            add_question(rows, used, "L4", "generation_design",
                f"Prepare a generation plan for a replacement or extension of `{m['name']}` that preserves hierarchy, interface intent, and likely child dependencies.",
                [m], ["generation plan", "hierarchy", "interface intent"], "Complex design planning.")
    for m in complex_modules[140:]:
        if Counter(r["type"] for r in rows if r["level"] == "L4")["code_explanation"] >= per_cell:
            break
        if len(m["instances"]) >= 2 and len(m.get("labels", [])) >= 2:
            add_question(rows, used, "L4", "code_explanation",
                f"Explain the design intent of `{m['name']}` as if onboarding another RTL engineer who needs both behavior and integration context.",
                [m], ["intent", "integration context"], "Engineer-to-engineer explanation.")
    for m in complex_modules[150:]:
        if Counter(r["type"] for r in rows if r["level"] == "L4")["documentation_summary"] >= per_cell:
            break
        add_question(rows, used, "L4", "documentation_summary",
            f"Draft documentation for `{m['name']}` that includes role, dependencies, exposed interface, and likely upstream/downstream context.",
            [m], ["dependencies", "interface", "context"], "Documentation with context.")

    # L5
    for m in complex_modules[160:]:
        if Counter(r["type"] for r in rows if r["level"] == "L5")["structure_understanding"] >= per_cell:
            break
        if len(m["instances"]) >= 4:
            add_question(rows, used, "L5", "structure_understanding",
                f"Reconstruct the likely subsystem architecture around `{m['name']}` and identify which child blocks are control, buffering, or transport oriented.",
                [m], ["subsystem architecture", "role partitioning"], "Deep structural inference.")
    for child, parents in sorted(child_to_parents.items(), key=lambda item: -len(item[1])):
        if Counter(r["type"] for r in rows if r["level"] == "L5")["search_navigation"] >= per_cell:
            break
        if len(parents) >= 3:
            chosen = prioritized_parents(parents, child, 3)
            if len(chosen) < 3:
                continue
            add_question(rows, used, "L5", "search_navigation",
                f"For a graph query starting from shared child `{child}`, how should retrieval disambiguate among multiple parent contexts?",
                chosen, [f"high fan-out child {child}"], "Requires graph disambiguation strategy.")
    for a, b in pairs[160:]:
        if Counter(r["type"] for r in rows if r["level"] == "L5")["comparison_similarity"] >= per_cell:
            break
        labels = sorted(set(a.get("labels", [])).intersection(set(b.get("labels", []))))
        if len(labels) >= 1 and len(a["instances"]) >= 2 and len(b["instances"]) >= 2:
            add_question(rows, used, "L5", "comparison_similarity",
                f"Make an architecture-level comparison between `{a['name']}` and `{b['name']}` to decide which is the better template for a new subsystem.",
                [a, b], ["template selection", "architecture-level comparison"], "Template choice reasoning.")
    for label, a, b in cross_project_label_pairs[per_cell:]:
        if Counter(r["type"] for r in rows if r["level"] == "L5")["function_similarity"] >= per_cell:
            break
        add_question(rows, used, "L5", "function_similarity",
            f"Across projects, which modules are the best semantic analogs for `{label}` behavior between `{a['name']}` and `{b['name']}`, and where do they diverge functionally?",
            [a, b], [f"cross-project analog label {label}"], "Cross-project analog reasoning.")
    for m in complex_modules[200:]:
        if Counter(r["type"] for r in rows if r["level"] == "L5")["generation_design"] >= per_cell:
            break
        if len(m["instances"]) >= 3 and len(m["ports"]) >= 3:
            add_question(rows, used, "L5", "generation_design",
                f"Write a design-generation brief for building a new module inspired by `{m['name']}`, including preserved interfaces, child-role decomposition, and likely review risks.",
                [m], ["design-generation brief", "review risks"], "Most demanding design prompt.")
    for m in complex_modules[220:]:
        if Counter(r["type"] for r in rows if r["level"] == "L5")["code_explanation"] >= per_cell:
            break
        if len(m["instances"]) >= 3:
            add_question(rows, used, "L5", "code_explanation",
                f"Explain `{m['name']}` deeply enough that another engineer could answer follow-up questions about hierarchy, behavior, and likely integration assumptions.",
                [m], ["deep explanation", "integration assumptions"], "Deep code understanding.")
    for m in complex_modules[240:]:
        if Counter(r["type"] for r in rows if r["level"] == "L5")["documentation_summary"] >= per_cell:
            break
        add_question(rows, used, "L5", "documentation_summary",
            f"Produce a high-value design document summary for `{m['name']}` that could seed internal docs or review notes for future maintainers.",
            [m], ["maintainer-facing summary"], "Highest-level documentation synthesis.")

    return rows


def ensure_matrix(rows, per_cell):
    counter = Counter((row["level"], row["type"]) for row in rows)
    missing = []
    for level in LEVELS:
        for qtype in TYPES:
            if counter[(level, qtype)] < per_cell:
                missing.append((level, qtype, counter[(level, qtype)]))
    if missing:
        raise RuntimeError(f"Missing required level/type cells: {missing}")


def fill_missing_cells(rows, modules, per_cell):
    used = {
        (row["level"], row["type"], tuple(sorted(row["gold_modules"])), row["question"])
        for row in rows
    }
    trusted = trustworthy_modules(sorted(modules, key=lambda m: (m["project"], m["name"])))
    complex_modules = sorted(modules, key=lambda m: (-len(m["instances"]), -len(m["ports"]), m["name"]))
    pairs = choose_pairs(complex_modules[:160])
    _by_project, _by_label, _by_port, _by_name, child_to_parents = build_indexes(modules)
    parent_counts = {child: len(unique_by_name(parents)) for child, parents in child_to_parents.items()}
    direct_label_examples = representative_label_examples(modules, parent_counts)

    for level in LEVELS:
        for qtype in TYPES:
            need = per_cell - sum(1 for r in rows if r["level"] == level and r["type"] == qtype)
            attempts = 0
            cursor = 0
            while need > 0 and attempts < 200:
                attempts += 1
                if qtype in {"structure_understanding", "search_navigation", "generation_design", "code_explanation", "documentation_summary", "function_similarity"}:
                    source = complex_modules[(cursor + len(level) + len(qtype)) % len(complex_modules)]
                    if qtype == "structure_understanding":
                        prompt = f"In {level}, explain the structure of `{source['name']}` using ports, labels, and child instances."
                        evidence = ["ports", "labels", "instances"]
                    elif qtype == "search_navigation":
                        anchor = source["ports"][0]["name"] if source["ports"] else Path(source["path"]).name
                        prompt = f"In {level}, locate the module that should be found starting from anchor `{anchor}` and file `{Path(source['path']).name}`."
                        evidence = [f"anchor={anchor}", f"path={Path(source['path']).name}"]
                    elif qtype == "function_similarity":
                        if direct_label_examples:
                            label, source, support = direct_label_examples[(cursor + len(level)) % len(direct_label_examples)]
                            evidence = [f"label={label}", f"support={support}"]
                        else:
                            label = pick_label(source)
                            evidence = [f"label={label}"]
                        prompt = f"In {level}, identify the module that best represents `{label}` behavior and justify it from the knowledge DB."
                    elif qtype == "generation_design":
                        prompt = f"In {level}, write a generation/design prompt for extending `{source['name']}` while preserving its interface intent."
                        evidence = ["generation prompt", "interface intent"]
                    elif qtype == "code_explanation":
                        prompt = f"In {level}, explain `{source['name']}` to another engineer using hierarchy, labels, and ports."
                        evidence = ["hierarchy", "labels", "ports"]
                    else:
                        prompt = f"In {level}, produce a concise documentation summary for `{source['name']}` from the current knowledge DB."
                        evidence = ["documentation summary"]
                    added = add_question(rows, used, level, qtype, prompt, [source], evidence, "Auto-filled level/type cell.")
                else:
                    a, b = pairs[(cursor + len(level)) % len(pairs)]
                    prompt = f"In {level}, compare `{a['name']}` and `{b['name']}` for similarity in role, structure, and reuse value."
                    added = add_question(rows, used, level, qtype, prompt, [a, b], ["pairwise comparison"], "Auto-filled comparison cell.")
                if added:
                    need -= 1
                cursor += 1


def write_catalog(path, rows):
    grouped = defaultdict(list)
    for row in rows:
        grouped[(row["level"], row["type"])].append(row)
    lines = ["# Multi-Axis RTL Question Set", ""]
    for level in LEVELS:
        lines.append(f"## {level}")
        lines.append("")
        for qtype in TYPES:
            lines.append(f"### {qtype}")
            lines.append("")
            for idx, row in enumerate(grouped[(level, qtype)], start=1):
                gold = ", ".join(row["gold_modules"])
                lines.append(f"{idx}. {row['question']}")
                lines.append(f"   - gold: `{gold}`")
            lines.append("")
    with open(path, "w", encoding="utf-8") as fp:
        fp.write("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", required=True)
    ap.add_argument("--labels", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--per-cell", type=int, default=5)
    ap.add_argument("--random-seed", type=int, default=11)
    args = ap.parse_args()

    random.seed(args.random_seed)
    modules = clean_modules(read_jsonl(args.seed))
    _labels = read_jsonl(args.labels)
    rows = generate_questions(modules, args.per_cell)
    fill_missing_cells(rows, modules, args.per_cell)
    ensure_matrix(rows, args.per_cell)

    summary = {
        "per_cell": args.per_cell,
        "total": len(rows),
        "levels": {level: sum(1 for r in rows if r["level"] == level) for level in LEVELS},
        "types": {qtype: sum(1 for r in rows if r["type"] == qtype) for qtype in TYPES},
        "matrix": {
            level: {qtype: sum(1 for r in rows if r["level"] == level and r["type"] == qtype) for qtype in TYPES}
            for level in LEVELS
        },
    }

    out_dir = Path(args.out_dir)
    write_jsonl(out_dir / "questions_all.jsonl", rows)
    write_json(out_dir / "summary.json", summary)
    write_catalog(out_dir / "questions_catalog.md", rows)
    for level in LEVELS:
        write_jsonl(out_dir / f"{level.lower()}.jsonl", [r for r in rows if r["level"] == level])
    for qtype in TYPES:
        write_jsonl(out_dir / f"type_{qtype}.jsonl", [r for r in rows if r["type"] == qtype])
    print(json.dumps({"status": "ok", "out_dir": str(out_dir), **summary}, ensure_ascii=False))


if __name__ == "__main__":
    main()
