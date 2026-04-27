#!/usr/bin/env python3
"""
Apply approved/rejected user decisions to PostgreSQL.

- approved  → INSERT/UPDATE ontology_assertions with review_state='approved'
              + resolve matching ontology_review_queue items
- rejected  → mark ontology_assertions review_state='rejected'
              + resolve review_queue items
- Records the KG version tag on each affected assertion.

Usage:
  python apply_labels_to_postgres.py \
    --decisions out/label_approval/user_decisions_<ts>.jsonl \
    --version-tag v002 \
    --db-url "postgresql://postgres:postgres@localhost:5432/verilog"
"""
import argparse
import json
import sys
from datetime import datetime, timezone

try:
    import psycopg2
    import psycopg2.extras
    HAS_PSYCOPG = True
except ImportError:
    HAS_PSYCOPG = False


def read_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def apply(conn, decisions, version_tag: str):
    stats = {"upserted": 0, "rejected": 0, "queue_resolved": 0, "errors": 0}
    now = datetime.now(timezone.utc)

    with conn.cursor() as cur:
        for row in decisions:
            target   = row.get("target_name", "")
            label    = row.get("label", "")
            project  = row.get("project", "")
            decision = row.get("decision", "")
            conf     = row.get("auto_confidence", row.get("source_confidence", 0.0))

            if not target or not label:
                continue

            review_state = "approved" if decision == "auto_approved" else "rejected"

            try:
                # Upsert ontology_entity
                cur.execute("""
                    INSERT INTO ontology_entities
                        (entity_key, project, entity_type, name, file_path)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (entity_key) DO NOTHING
                """, (
                    f"{project}:{target}",
                    project,
                    row.get("entity_type", "module"),
                    target,
                    row.get("path", ""),
                ))

                # Upsert ontology_label
                cur.execute("""
                    INSERT INTO ontology_labels (label_key, label_group, state)
                    VALUES (%s, %s, 'approved')
                    ON CONFLICT (label_key) DO NOTHING
                """, (label, row.get("group", "other")))

                # Fetch IDs
                cur.execute("SELECT entity_id FROM ontology_entities WHERE entity_key = %s",
                            (f"{project}:{target}",))
                entity_row = cur.fetchone()
                cur.execute("SELECT ontology_label_id FROM ontology_labels WHERE label_key = %s",
                            (label,))
                label_row = cur.fetchone()
                if not entity_row or not label_row:
                    stats["errors"] += 1
                    continue

                entity_id = entity_row[0]
                label_id  = label_row[0]

                # Upsert assertion
                cur.execute("""
                    INSERT INTO ontology_assertions
                        (entity_id, ontology_label_id, source_kind, confidence,
                         review_state, created_at, kg_version_tag)
                    VALUES (%s, %s, 'user_review', %s, %s, %s, %s)
                    ON CONFLICT (entity_id, ontology_label_id, source_kind)
                        DO UPDATE SET
                            review_state    = EXCLUDED.review_state,
                            confidence      = EXCLUDED.confidence,
                            kg_version_tag  = EXCLUDED.kg_version_tag
                """, (entity_id, label_id, conf, review_state, now, version_tag))

                if review_state == "approved":
                    stats["upserted"] += 1
                else:
                    stats["rejected"] += 1

                # Resolve review queue
                cur.execute("""
                    UPDATE ontology_review_queue
                    SET state = %s, resolved_at = %s
                    WHERE entity_key = %s AND proposed_label = %s AND state = 'proposed'
                """, (review_state, now, f"{project}:{target}", label))
                stats["queue_resolved"] += cur.rowcount

            except Exception as exc:
                stats["errors"] += 1
                print(f"  WARN: {target}/{label}: {exc}", file=sys.stderr)
                conn.rollback()
                continue

        conn.commit()

    return stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--decisions",   required=True)
    ap.add_argument("--version-tag", required=True)
    ap.add_argument("--db-url",      default="postgresql://postgres:postgres@localhost:5432/verilog")
    args = ap.parse_args()

    if not HAS_PSYCOPG:
        print(json.dumps({"status": "skipped", "reason": "psycopg2 not installed"}))
        return

    decisions = read_jsonl(args.decisions)
    print(f"Loaded {len(decisions)} decisions from {args.decisions}")

    try:
        conn = psycopg2.connect(args.db_url)
    except Exception as exc:
        print(json.dumps({"status": "skipped", "reason": f"DB connection failed: {exc}"}))
        return

    try:
        stats = apply(conn, decisions, args.version_tag)
        print(json.dumps({"status": "ok", "version_tag": args.version_tag, **stats},
                         ensure_ascii=False, indent=2))
    finally:
        conn.close()


if __name__ == "__main__":
    main()
