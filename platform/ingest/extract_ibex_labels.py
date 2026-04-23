#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path

MODULE_RE = re.compile(r"\bmodule\s+([A-Za-z_][A-Za-z0-9_$]*)")
ENDMODULE_RE = re.compile(r"\bendmodule\b")

def find_modules(text):
    starts=[(m.start(),m.group(1)) for m in MODULE_RE.finditer(text)]
    ends=[m.start() for m in ENDMODULE_RE.finditer(text)]
    out=[]; eidx=0
    for s,name in starts:
        while eidx < len(ends) and ends[eidx] < s:
            eidx += 1
        if eidx >= len(ends):
            break
        out.append((name, text[s:ends[eidx]]))
        eidx += 1
    return out

def infer_ibex_labels(module_name, body):
    hay = (module_name + " " + body[:4000]).lower()
    labels = {"ibex_core"}
    if "ibex" in hay:
        labels.add("core")
    if "alu" in hay:
        labels.add("alu")
    if "decoder" in hay:
        labels.add("decoder_stage")
    if "controller" in hay or "ctrl" in hay:
        labels.add("controller")
    if "csr" in hay:
        labels.add("csr")
    if "register" in hay or "regfile" in hay:
        labels.add("register_file")
    if "pipeline" in hay or "stage" in hay:
        labels.add("pipeline")
    if "fifo" in hay:
        labels.add("fifo")
    return sorted(labels)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    args=ap.parse_args()

    root=Path(args.root)
    out=Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    rtl_roots = []
    for candidate in ["rtl", "vendor"]:
        p = root / candidate
        if p.exists():
            rtl_roots.append(p)
    if not rtl_roots:
        rtl_roots = [root]

    count=0
    with out.open("w", encoding="utf-8") as fp:
        for rtl_root in rtl_roots:
            for path in rtl_root.rglob("*"):
                if path.suffix.lower() not in {".v", ".sv"}:
                    continue
                text = path.read_text(encoding="utf-8", errors="ignore")
                for module_name, body in find_modules(text):
                    row = {
                        "project": "ibex",
                        "entity_type": "label_proposal",
                        "name": module_name,
                        "path": str(path),
                        "summary": f"{module_name}: Ibex module label proposal",
                        "labels": infer_ibex_labels(module_name, body),
                        "confidence": 0.72,
                        "evidence": [str(path)],
                        "metadata": {"source_kind": "label_proposal"}
                    }
                    fp.write(json.dumps(row, ensure_ascii=False) + "\n")
                    count += 1
    print(json.dumps({"status":"ok","count":count,"out":str(out)}))

if __name__=="__main__":
    main()
