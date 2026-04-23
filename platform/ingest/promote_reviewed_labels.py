#!/usr/bin/env python3
import argparse, json
def read_jsonl(path):
    with open(path, "r", encoding="utf-8") as fp:
        for line in fp:
            line=line.strip()
            if line: yield json.loads(line)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--infile", required=True); ap.add_argument("--outfile", required=True); args=ap.parse_args()
    out=[]
    for row in read_jsonl(args.infile):
        if row.get("review_state") in {"reviewed","approved"} and row.get("confidence",0)>=0.75:
            row["promotion_candidate"]=True; out.append(row)
    with open(args.outfile, "w", encoding="utf-8") as fp:
        for row in out: fp.write(json.dumps(row, ensure_ascii=False)+"\n")
    print(json.dumps({"status":"ok","count":len(out),"outfile":args.outfile}, ensure_ascii=False))
if __name__=="__main__": main()
