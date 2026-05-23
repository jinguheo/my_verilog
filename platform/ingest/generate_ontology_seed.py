#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path

COMMENT_RE = re.compile(r"//.*?$|/\*.*?\*/", re.MULTILINE | re.DOTALL)
MODULE_RE = re.compile(r"\bmodule\s+([A-Za-z_][A-Za-z0-9_$]*)")
ENDMODULE_RE = re.compile(r"\bendmodule\b")
PORT_RE = re.compile(r"\b(input|output|inout)\b(?:\s+(?:wire|reg|logic|signed|unsigned))*\s*(?:\[[^\]]+\]\s*)?([A-Za-z_][A-Za-z0-9_$]*)")
INSTANCE_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_$]*)\s*(?:#\s*\([^;]*?\))?\s+([A-Za-z_][A-Za-z0-9_$]*)\s*\(", re.MULTILINE | re.DOTALL)
ROLE_HINTS = {"fifo":["fifo","full","empty"],"uart":["uart","tx","rx"],"i2c":["i2c","scl","sda"],"spi":["spi","mosi","miso"],"apb":["paddr","psel","penable"]}


def strip_comments(text):
    return COMMENT_RE.sub("", text)


def find_modules(text):
    starts=[(m.start(),m.group(1)) for m in MODULE_RE.finditer(text)]
    ends=[m.start() for m in ENDMODULE_RE.finditer(text)]
    out=[]; eidx=0
    for s,name in starts:
        while eidx < len(ends) and ends[eidx] < s: eidx += 1
        if eidx >= len(ends): break
        out.append((name, text[s:ends[eidx]])); eidx += 1
    return out


def read_node_text(node, source):
    return source[node.start_byte:node.end_byte].decode("utf-8", errors="ignore")


def first_child_text(node, source, *types):
    for child in node.children:
        if child.type in types:
            return read_node_text(child, source).strip()
    return None


def module_name_from_declaration(node, source):
    name_node = node.child_by_field_name("name")
    if name_node:
        return read_node_text(name_node, source).strip()
    for child in node.children:
        if child.type == "module_header":
            name = first_child_text(child, source, "simple_identifier", "escaped_identifier")
            if name:
                return name
    return first_child_text(node, source, "simple_identifier", "escaped_identifier")


def instantiation_type_from_node(node, source):
    type_node = node.child_by_field_name("module_type")
    if type_node:
        return read_node_text(type_node, source).strip()
    return first_child_text(node, source, "simple_identifier", "escaped_identifier")


def walk_tree(node):
    yield node
    for child in node.children:
        yield from walk_tree(child)


def extract_ports_from_body(body):
    seen = set()
    ports = []
    for direction, name in PORT_RE.findall(body):
        key = (direction, name)
        if key in seen:
            continue
        seen.add(key)
        ports.append({"dir": direction, "name": name})
    return ports


def extract_instances_from_tree(module_node, source, module_name):
    insts = []
    seen = set()
    for node in walk_tree(module_node):
        if node.type != "module_instantiation":
            continue
        inst_type = instantiation_type_from_node(node, source)
        if not inst_type or inst_type in {"module", module_name}:
            continue
        text = read_node_text(node, source)
        # Keep instance names as best-effort. Ranking mainly needs child module type.
        names = re.findall(r"\b([A-Za-z_][A-Za-z0-9_$]*)\s*\(", text)
        inst_name = names[-1] if names else ""
        key = (inst_type, inst_name)
        if key in seen:
            continue
        seen.add(key)
        insts.append({"type": inst_type, "name": inst_name})
    return insts


def find_modules_tree_sitter(path):
    import tree_sitter_verilog as tsverilog
    from tree_sitter import Language, Parser

    source = path.read_bytes()
    parser = Parser(Language(tsverilog.language()))
    tree = parser.parse(source)
    modules = []
    for node in walk_tree(tree.root_node):
        if node.type != "module_declaration":
            continue
        name = module_name_from_declaration(node, source)
        if not name:
            continue
        body = read_node_text(node, source)
        ports = extract_ports_from_body(body)
        insts = extract_instances_from_tree(node, source, name)
        modules.append((name, body, ports, insts))
    return modules


def find_modules_regex(text):
    rows = []
    for module_name, body in find_modules(text):
        ports=[{"dir":d,"name":n} for d,n in PORT_RE.findall(body)]
        insts=[{"type":t,"name":n} for t,n in INSTANCE_RE.findall(body) if t!="module"]
        rows.append((module_name, body, ports, insts))
    return rows


def infer(name, body, ports, insts):
    hay=" ".join([name, body[:4000]]+[p["name"] for p in ports]+[i["type"] for i in insts]).lower()
    labels=set()
    for label,hints in ROLE_HINTS.items():
        if any(h in hay for h in hints): labels.add(label)
    if any("clk" in p["name"].lower() for p in ports): labels.add("clocked")
    if any("rst" in p["name"].lower() or "reset" in p["name"].lower() for p in ports): labels.add("resettable")
    if insts: labels.add("hierarchical")
    return sorted(labels)


def resolve_frontend(frontend):
    if frontend == "regex":
        return "regex"
    try:
        import tree_sitter_verilog  # noqa: F401
        import tree_sitter  # noqa: F401
        return "tree-sitter"
    except ImportError:
        if frontend == "tree-sitter":
            raise
        return "regex"


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--frontend", choices=["auto", "tree-sitter", "regex"], default="auto")
    args=ap.parse_args()
    root=Path(args.root); out=Path(args.out); out.parent.mkdir(parents=True, exist_ok=True)
    frontend = resolve_frontend(args.frontend)
    count=0
    with out.open("w", encoding="utf-8") as fp:
        for path in root.rglob("*"):
            if path.suffix.lower() not in {".v",".sv"}: continue
            if frontend == "tree-sitter":
                modules = find_modules_tree_sitter(path)
            else:
                text=strip_comments(path.read_text(encoding="utf-8", errors="ignore"))
                modules = find_modules_regex(text)
            for module_name, body, ports, insts in modules:
                labels=infer(module_name, body, ports, insts)
                row={"project":root.name,"entity_type":"module","name":module_name,"path":str(path),"summary":f"{module_name}: {', '.join(labels) if labels else 'unlabeled rtl block'}","labels":labels,"ports":ports,"instances":insts,"metadata":{"source_kind":"ontology_seed","frontend":frontend}}
                fp.write(json.dumps(row, ensure_ascii=False)+"\n"); count += 1
    print(json.dumps({"status":"ok","modules":count,"out":str(out),"frontend":frontend}))
if __name__=="__main__": main()
