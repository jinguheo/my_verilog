#!/usr/bin/env python3
"""
Apply approved/rejected user decisions to Neo4j.

- approved  → MERGE (m:Module)-[:HAS_LABEL {version}]->(l:Label)
- rejected  → DELETE the HAS_LABEL relationship if it exists
- Stamps each node/relationship with kg_version_tag property.

Usage:
  python apply_labels_to_neo4j.py \
    --decisions out/label_approval/user_decisions_<ts>.jsonl \
    --version-tag v002 \
    --uri neo4j://localhost:7687 \
    --user neo4j --password neo4jpassword
"""
import argparse
import json
import sys
from datetime import datetime, timezone

try:
    from neo4j import GraphDatabase
    HAS_NEO4J = True
except ImportError:
    HAS_NEO4J = False


def read_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def apply_approved(tx, target, project, label, version_tag, confidence):
    tx.run("""
        MERGE (m:Module {name: $name, project: $project})
        MERGE (l:Label  {key: $label})
        MERGE (m)-[r:HAS_LABEL {label: $label}]->(l)
        SET r.version_tag = $version_tag,
            r.confidence  = $confidence,
            r.reviewed_by = 'user',
            l.key         = $label
    """, name=target, project=project, label=label,
         version_tag=version_tag, confidence=confidence)


def apply_rejected(tx, target, project, label, version_tag):
    tx.run("""
        MATCH (m:Module {name: $name, project: $project})-[r:HAS_LABEL]->(l:Label {key: $label})
        SET r.review_state = 'rejected', r.version_tag = $version_tag
    """, name=target, project=project, label=label, version_tag=version_tag)


def apply(driver, decisions, version_tag: str):
    stats = {"approved": 0, "rejected": 0, "errors": 0}
    with driver.session() as session:
        for row in decisions:
            target   = row.get("target_name", "")
            label    = row.get("label", "")
            project  = row.get("project", "")
            decision = row.get("decision", "")
            conf     = float(row.get("auto_confidence", row.get("source_confidence", 0.0)))

            if not target or not label:
                continue
            try:
                if decision == "auto_approved":
                    session.execute_write(apply_approved, target, project, label, version_tag, conf)
                    stats["approved"] += 1
                elif decision == "auto_rejected":
                    session.execute_write(apply_rejected, target, project, label, version_tag)
                    stats["rejected"] += 1
            except Exception as exc:
                stats["errors"] += 1
                print(f"  WARN: {target}/{label}: {exc}", file=sys.stderr)
    return stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--decisions",   required=True)
    ap.add_argument("--version-tag", required=True)
    ap.add_argument("--uri",         default="neo4j://localhost:7687")
    ap.add_argument("--user",        default="neo4j")
    ap.add_argument("--password",    default="neo4jpassword")
    args = ap.parse_args()

    if not HAS_NEO4J:
        print(json.dumps({"status": "skipped", "reason": "neo4j driver not installed"}))
        return

    decisions = read_jsonl(args.decisions)
    print(f"Loaded {len(decisions)} decisions from {args.decisions}")

    try:
        driver = GraphDatabase.driver(args.uri, auth=(args.user, args.password))
        driver.verify_connectivity()
    except Exception as exc:
        print(json.dumps({"status": "skipped", "reason": f"Neo4j connection failed: {exc}"}))
        return

    try:
        stats = apply(driver, decisions, args.version_tag)
        print(json.dumps({"status": "ok", "version_tag": args.version_tag, **stats},
                         ensure_ascii=False, indent=2))
    finally:
        driver.close()


if __name__ == "__main__":
    main()
