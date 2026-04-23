#!/usr/bin/env python3
import argparse, json
def read_jsonl(path):
    with open(path, "r", encoding="utf-8") as fp:
        for line in fp:
            line=line.strip()
            if line: yield json.loads(line)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--seed", required=True); ap.add_argument("--outfile", required=True); args=ap.parse_args()
    rows=[]
    for row in read_jsonl(args.seed):
        if row.get("entity_type")!="module": continue
        text=" ".join([row.get("name",""), row.get("summary",""), " ".join(row.get("labels",[]))]).strip()
        rows.append({"entity_key":f'{row.get("project","")}::{row.get("path","")}::{row.get("name","")}',"text":text,"labels":row.get("labels",[])})
    with open(args.outfile, "w", encoding="utf-8") as fp: json.dump(rows, fp, ensure_ascii=False, indent=2)
    print(json.dumps({"status":"ok","rows":len(rows),"outfile":args.outfile}, ensure_ascii=False))
if __name__=="__main__": main()
