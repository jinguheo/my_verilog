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
def infer(name, body, ports, insts):
    hay=" ".join([name, body[:4000]]+[p["name"] for p in ports]+[i["type"] for i in insts]).lower()
    labels=set()
    for label,hints in ROLE_HINTS.items():
        if any(h in hay for h in hints): labels.add(label)
    if any("clk" in p["name"].lower() for p in ports): labels.add("clocked")
    if any("rst" in p["name"].lower() or "reset" in p["name"].lower() for p in ports): labels.add("resettable")
    if insts: labels.add("hierarchical")
    return sorted(labels)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--root", required=True); ap.add_argument("--out", required=True); args=ap.parse_args()
    root=Path(args.root); out=Path(args.out); out.parent.mkdir(parents=True, exist_ok=True)
    count=0
    with out.open("w", encoding="utf-8") as fp:
        for path in root.rglob("*"):
            if path.suffix.lower() not in {".v",".sv"}: continue
            text=strip_comments(path.read_text(encoding="utf-8", errors="ignore"))
            for module_name, body in find_modules(text):
                ports=[{"dir":d,"name":n} for d,n in PORT_RE.findall(body)]
                insts=[{"type":t,"name":n} for t,n in INSTANCE_RE.findall(body) if t!="module"]
                labels=infer(module_name, body, ports, insts)
                row={"project":root.name,"entity_type":"module","name":module_name,"path":str(path),"summary":f"{module_name}: {', '.join(labels) if labels else 'unlabeled rtl block'}","labels":labels,"ports":ports,"instances":insts,"metadata":{"source_kind":"ontology_seed"}}
                fp.write(json.dumps(row, ensure_ascii=False)+"\n"); count += 1
    print(json.dumps({"status":"ok","modules":count,"out":str(out)}))
if __name__=="__main__": main()
