#!/usr/bin/env python3
import argparse, json
from pathlib import Path
def label_for_ip(ip_name):
    name=ip_name.lower(); labels={name,"opentitan_ip"}
    if "uart" in name: labels.update(["uart","serial","device"])
    if "i2c" in name: labels.update(["i2c","serial_bus"])
    if "spi" in name: labels.update(["spi","serial_bus"])
    if "gpio" in name: labels.update(["gpio","io"])
    if "timer" in name: labels.update(["timer","counter"])
    if "flash" in name: labels.update(["flash","memory"])
    if "aes" in name or "hmac" in name or "kmac" in name: labels.update(["crypto"])
    if "ctrl" in name: labels.add("controller")
    return sorted(labels)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--root", required=True); ap.add_argument("--out", required=True); args=ap.parse_args()
    root=Path(args.root); hw_ip=root/"hw"/"ip"; out=Path(args.out); out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as fp:
        for ip_dir in sorted([p for p in hw_ip.iterdir() if p.is_dir()]):
            row={"project":"opentitan","entity_type":"ip_block","name":ip_dir.name,"path":str(ip_dir),"summary":f"{ip_dir.name}: OpenTitan IP block candidate","labels":label_for_ip(ip_dir.name),"confidence":0.80,"evidence":[str(ip_dir)],"metadata":{"source_kind":"label_proposal"}}
            fp.write(json.dumps(row, ensure_ascii=False)+"\n")
    print(json.dumps({"status":"ok","out":str(out)}))
if __name__=="__main__": main()
