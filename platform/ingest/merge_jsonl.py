#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def read_jsonl(path):
    with open(path, "r", encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            if line:
                yield json.loads(line)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    count = 0
    with out.open("w", encoding="utf-8") as fp:
        for path in args.inputs:
            for row in read_jsonl(path):
                fp.write(json.dumps(row, ensure_ascii=False) + "\n")
                count += 1
    print(json.dumps({"status":"ok","rows":count,"out":str(out)}))

if __name__ == "__main__":
    main()
