#!/usr/bin/env python3
import argparse, json
from neo4j import GraphDatabase
def read_jsonl(path):
    with open(path, "r", encoding="utf-8") as fp:
        for line in fp:
            line=line.strip()
            if line: yield json.loads(line)
def ensure_constraints(tx):
    tx.run("CREATE CONSTRAINT module_name IF NOT EXISTS FOR (m:Module) REQUIRE (m.project, m.name, m.path) IS UNIQUE")
    tx.run("CREATE CONSTRAINT label_key IF NOT EXISTS FOR (l:Label) REQUIRE l.key IS UNIQUE")
    tx.run("CREATE CONSTRAINT ip_key IF NOT EXISTS FOR (i:IPBlock) REQUIRE (i.project, i.name) IS UNIQUE")
def insert_module(tx, row):
    tx.run("MERGE (m:Module {project:$project, name:$name, path:$path}) SET m.summary=$summary", project=row["project"], name=row["name"], path=row["path"], summary=row.get("summary",""))
    for label in row.get("labels", []):
        tx.run("MERGE (l:Label {key:$label}) MERGE (m:Module {project:$project, name:$name, path:$path}) MERGE (m)-[:HAS_LABEL]->(l)", label=label, project=row["project"], name=row["name"], path=row["path"])
def insert_ip(tx, row):
    tx.run("MERGE (i:IPBlock {project:$project, name:$name}) SET i.path=$path, i.summary=$summary, i.confidence=$confidence", project=row["project"], name=row["name"], path=row["path"], summary=row.get("summary",""), confidence=row.get("confidence",0.0))
    for label in row.get("labels", []):
        tx.run("MERGE (l:Label {key:$label}) MERGE (i:IPBlock {project:$project, name:$name}) MERGE (i)-[:HAS_LABEL]->(l)", label=label, project=row["project"], name=row["name"])
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--seed", required=True); ap.add_argument("--labels", required=True); ap.add_argument("--uri", required=True); ap.add_argument("--user", required=True); ap.add_argument("--password", required=True); args=ap.parse_args()
    driver=GraphDatabase.driver(args.uri, auth=(args.user, args.password))
    with driver.session() as s:
        s.execute_write(ensure_constraints)
        for row in read_jsonl(args.seed):
            if row.get("entity_type")=="module": s.execute_write(insert_module, row)
        for row in read_jsonl(args.labels):
            if row.get("entity_type")=="ip_block": s.execute_write(insert_ip, row)
    driver.close(); print(json.dumps({"status":"ok"}))
if __name__=="__main__": main()
