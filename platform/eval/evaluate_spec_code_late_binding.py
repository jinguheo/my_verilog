#!/usr/bin/env python3
"""Evaluate late-binding links between spec documents and the code KG.

The intended architecture keeps three stores separate:

- code KG: the custom RTL ontology/KG remains the primary retrieval engine
- Graphify: a broad architecture/navigation graph
- OpenKB: a spec/document wiki graph

This evaluator checks whether spec docs can be joined to code modules/IP blocks
through shared keys such as module_name, ip_block, spec_section, doc_anchor, and
approved_label.  It does not physically merge the graphs.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SPEC_DIR = ROOT / "out" / "spec_documents_20260514_204108"
DEFAULT_OUT = ROOT / "out" / "spec_code_late_binding_eval"
DEFAULT_SEED = ROOT / "out" / "merged_ontology_seed.jsonl"
DEFAULT_LABELS = ROOT / "out" / "merged_labels.jsonl"

TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_$]*")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
SUPPORTED_SUFFIXES = {".md", ".rst", ".txt", ".hjson", ".csv"}
WEAK_LABELS = {"clocked", "resettable", "hierarchical", "opentitan_ip", "ibex_core"}
GENERIC_MODULE_NAMES = {
    "tb", "dut", "top", "core", "clk", "rst", "reset", "logic", "assert",
    "cover", "bind", "sim", "test", "model", "pkg",
}


@dataclass
class ModuleRecord:
    project: str
    name: str
    path: str
    ip_block: str
    labels: list[str]
    ports: list[str]
    instances: list[str]


@dataclass
class DocAnchor:
    doc_id: str
    path: str
    project: str
    doc_kind: str
    ip_block: str
    spec_sections: list[str]
    module_mentions: list[str]
    ip_mentions: list[str]
    label_mentions: list[str]
    token_count: int


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def norm(text: str) -> str:
    return text.lower().replace("-", "_")


def slug(text: str) -> str:
    text = norm(text)
    text = re.sub(r"[^a-z0-9_]+", "_", text)
    return re.sub(r"_+", "_", text).strip("_") or "section"


def derive_ip_block(project: str, path_text: str, module_name: str = "") -> str:
    p = path_text.replace("/", "\\").lower()
    parts = [part for part in re.split(r"[\\/]+", p) if part]

    def after(marker: str) -> str:
        try:
            idx = parts.index(marker)
        except ValueError:
            return ""
        return parts[idx + 1] if idx + 1 < len(parts) else ""

    if project == "opentitan":
        if "\\hw\\ip\\" in p:
            return after("ip")
        if "\\ip_autogen\\" in p:
            return after("ip_autogen")
        if "\\top_" in p and "\\ip\\" in p:
            return after("ip")
    if project == "ibex":
        if "\\vendor\\lowrisc_ip\\ip\\" in p:
            return after("ip")
        if "\\doc\\" in p or "\\rtl\\" in p:
            if module_name.startswith("ibex") or "ibex" in p:
                return "ibex"
        if "\\icache\\" in p:
            return "ibex_icache"
    return ""


def doc_project(path: Path, spec_dir: Path) -> str:
    try:
        first = path.relative_to(spec_dir).parts[0].lower()
    except ValueError:
        first = ""
    return first if first in {"ibex", "opentitan"} else ""


def doc_kind(path: Path, spec_dir: Path) -> str:
    rel = str(path.relative_to(spec_dir)).replace("/", "\\").lower()
    name = path.name.lower()
    if "\\hw\\ip\\" in rel and "\\doc\\" in rel:
        return "opentitan_ip_doc"
    if "\\hw\\ip\\" in rel and "\\data\\" in rel and name.endswith(".hjson"):
        return "opentitan_ip_hjson"
    if "testplan" in name:
        return "testplan"
    if "\\doc\\03_reference\\" in rel:
        return "ibex_reference"
    if "\\vendor\\lowrisc_ip\\ip\\prim\\doc\\" in rel:
        return "prim_doc"
    if name == "readme.md":
        return "readme"
    return "generic_doc"


def extract_sections(text: str, path: Path) -> list[str]:
    sections: list[str] = []
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        match = HEADING_RE.match(line.strip())
        if match:
            sections.append(f"{path.name}#{slug(match.group(2))}")
            continue
        if idx + 1 < len(lines):
            underline = lines[idx + 1].strip()
            if line.strip() and len(underline) >= 3 and set(underline) <= {"=", "-", "~", "^"}:
                sections.append(f"{path.name}#{slug(line.strip())}")
    return sorted(set(sections))[:80]


def load_modules(seed_path: Path, labels_path: Path) -> tuple[list[ModuleRecord], dict[str, list[str]]]:
    label_by_module: dict[tuple[str, str], set[str]] = defaultdict(set)
    ip_labels: dict[str, list[str]] = defaultdict(list)
    if labels_path.exists():
        for row in read_jsonl(labels_path):
            labels = {str(label).lower() for label in row.get("labels", [])}
            if row.get("entity_type") == "module":
                label_by_module[(row.get("project", ""), row.get("name", ""))].update(labels)
            elif row.get("entity_type") == "ip_block":
                ip_labels[row.get("name", "")].extend(sorted(labels))

    modules: list[ModuleRecord] = []
    for row in read_jsonl(seed_path):
        if row.get("entity_type") != "module":
            continue
        name = row.get("name", "")
        if norm(name) in GENERIC_MODULE_NAMES or len(name) < 3:
            continue
        labels = set(str(label).lower() for label in row.get("labels", []))
        labels.update(label_by_module.get((row.get("project", ""), name), set()))
        ip_block = derive_ip_block(row.get("project", ""), row.get("path", ""), name)
        if ip_block:
            labels.update(ip_labels.get(ip_block, []))
        modules.append(ModuleRecord(
            project=row.get("project", ""),
            name=name,
            path=row.get("path", ""),
            ip_block=ip_block,
            labels=sorted(labels),
            ports=[p.get("name", "") for p in row.get("ports", []) if p.get("name")],
            instances=[i.get("type", "") for i in row.get("instances", []) if i.get("type")],
        ))
    return modules, ip_labels


def build_doc_anchor(
    path: Path,
    spec_dir: Path,
    module_names: set[str],
    ip_blocks: set[str],
    labels: set[str],
) -> DocAnchor:
    text = path.read_text(encoding="utf-8", errors="replace")
    project = doc_project(path, spec_dir)
    rel = str(path.relative_to(spec_dir)).replace("/", "\\")
    tokens = {norm(token) for token in TOKEN_RE.findall(text)}
    path_tokens = {norm(part) for part in re.split(r"[\\/_.-]+", rel)}
    all_tokens = tokens | path_tokens

    module_mentions = sorted(name for name in module_names if norm(name) in all_tokens)
    ip_mentions = sorted(ip for ip in ip_blocks if norm(ip) in all_tokens)
    label_mentions = sorted(label for label in labels if label not in WEAK_LABELS and norm(label) in all_tokens)
    ip_block = derive_ip_block(project, rel)
    if ip_block and ip_block not in ip_mentions:
        ip_mentions.insert(0, ip_block)

    return DocAnchor(
        doc_id=rel,
        path=str(path),
        project=project,
        doc_kind=doc_kind(path, spec_dir),
        ip_block=ip_block,
        spec_sections=extract_sections(text, path),
        module_mentions=module_mentions[:100],
        ip_mentions=ip_mentions[:60],
        label_mentions=label_mentions[:60],
        token_count=len(tokens),
    )


def confidence_for(anchor: DocAnchor) -> str:
    if anchor.module_mentions:
        return "high"
    if anchor.ip_block or anchor.ip_mentions:
        return "medium"
    if anchor.label_mentions:
        return "low"
    return "none"


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def write_pdf(path: Path, title: str, lines: list[str]) -> None:
    def esc(s: str) -> str:
        return str(s).replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

    pages: list[list[tuple[str, int]]] = []
    page: list[tuple[str, int]] = [(title, 18), ("", 10)]
    for raw in lines:
        size = 12 if raw.startswith("# ") else 9
        text = raw[2:] if raw.startswith("# ") else raw
        words = text.split()
        wrapped: list[str] = []
        cur = ""
        for word in words:
            if len(cur) + len(word) + 1 <= 96:
                cur = (cur + " " + word).strip()
            else:
                if cur:
                    wrapped.append(cur)
                cur = word
        if cur:
            wrapped.append(cur)
        for item in wrapped or [""]:
            if len(page) > 44:
                pages.append(page)
                page = []
            page.append((item, size))
    if page:
        pages.append(page)

    objects: list[str] = []

    def obj(payload: str) -> int:
        objects.append(payload)
        return len(objects)

    font_id = obj("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    content_ids = []
    for page in pages:
        y = 760
        chunks = ["BT"]
        for text, size in page:
            if not text:
                y -= 10
                continue
            chunks.append(f"/F1 {size} Tf")
            chunks.append(f"60 {y} Td ({esc(text)}) Tj")
            chunks.append(f"-60 -{int(size * 1.45)} Td")
            y -= int(size * 1.45)
        chunks.append("ET")
        stream = "\n".join(chunks)
        content_ids.append(obj(f"<< /Length {len(stream.encode('latin-1', errors='replace'))} >>\nstream\n{stream}\nendstream"))
    page_ids = [
        obj(f"<< /Type /Page /Parent 0 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 {font_id} 0 R >> >> /Contents {cid} 0 R >>")
        for cid in content_ids
    ]
    pages_id = obj("<< /Type /Pages /Kids [" + " ".join(f"{pid} 0 R" for pid in page_ids) + f"] /Count {len(page_ids)} >>")
    objects[:] = [payload.replace("/Parent 0 0 R", f"/Parent {pages_id} 0 R") for payload in objects]
    catalog_id = obj(f"<< /Type /Catalog /Pages {pages_id} 0 R >>")
    pdf = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for idx, payload in enumerate(objects, 1):
        offsets.append(len(pdf))
        pdf.extend(f"{idx} 0 obj\n".encode())
        pdf.extend(payload.encode("latin-1", errors="replace"))
        pdf.extend(b"\nendobj\n")
    xref = len(pdf)
    pdf.extend(f"xref\n0 {len(objects) + 1}\n".encode())
    pdf.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.extend(f"{offset:010d} 00000 n \n".encode())
    pdf.extend(f"trailer << /Size {len(objects) + 1} /Root {catalog_id} 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode())
    path.write_bytes(pdf)


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate spec/code KG late binding")
    parser.add_argument("--spec-dir", type=Path, default=DEFAULT_SPEC_DIR)
    parser.add_argument("--seed", type=Path, default=DEFAULT_SEED)
    parser.add_argument("--labels", type=Path, default=DEFAULT_LABELS)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    modules, ip_label_map = load_modules(args.seed, args.labels)
    module_names = {module.name for module in modules if module.name}
    ip_blocks = {module.ip_block for module in modules if module.ip_block} | set(ip_label_map)
    labels = {label for module in modules for label in module.labels}

    doc_paths = [
        path for path in sorted(args.spec_dir.rglob("*"))
        if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES and path.name.lower() != "manifest.csv"
    ]
    anchors = [
        build_doc_anchor(path, args.spec_dir, module_names, ip_blocks, labels)
        for path in doc_paths
    ]

    modules_by_ip: dict[str, list[ModuleRecord]] = defaultdict(list)
    for module in modules:
        if module.ip_block:
            modules_by_ip[module.ip_block].append(module)

    module_docs: dict[str, set[str]] = defaultdict(set)
    module_docs_exact: dict[str, set[str]] = defaultdict(set)
    module_docs_ip: dict[str, set[str]] = defaultdict(set)
    ip_docs: dict[str, set[str]] = defaultdict(set)
    doc_rows: list[dict[str, Any]] = []

    for anchor in anchors:
        confidence = confidence_for(anchor)
        linked_modules = set(anchor.module_mentions)
        for name in anchor.module_mentions:
            module_docs[name].add(anchor.doc_id)
            module_docs_exact[name].add(anchor.doc_id)
        for ip in set([anchor.ip_block] + anchor.ip_mentions):
            if not ip:
                continue
            ip_docs[ip].add(anchor.doc_id)
            for module in modules_by_ip.get(ip, []):
                linked_modules.add(module.name)
                module_docs[module.name].add(anchor.doc_id)
                module_docs_ip[module.name].add(anchor.doc_id)
        doc_rows.append({
            "doc_id": anchor.doc_id,
            "project": anchor.project,
            "doc_kind": anchor.doc_kind,
            "ip_block": anchor.ip_block,
            "confidence": confidence,
            "module_mentions": ";".join(anchor.module_mentions[:30]),
            "ip_mentions": ";".join(anchor.ip_mentions[:30]),
            "label_mentions": ";".join(anchor.label_mentions[:30]),
            "spec_sections": ";".join(anchor.spec_sections[:20]),
            "linked_module_count": len(linked_modules),
            "token_count": anchor.token_count,
        })

    module_rows = []
    for module in modules:
        docs = module_docs.get(module.name, set())
        module_rows.append({
            "project": module.project,
            "module": module.name,
            "ip_block": module.ip_block,
            "doc_count": len(docs),
            "exact_doc_count": len(module_docs_exact.get(module.name, set())),
            "ip_doc_count": len(module_docs_ip.get(module.name, set())),
            "labels": ";".join(module.labels),
            "path": module.path,
            "sample_docs": ";".join(sorted(docs)[:8]),
        })

    total_docs = len(anchors)
    docs_with_any = sum(1 for row in doc_rows if row["confidence"] != "none")
    docs_with_module = sum(1 for anchor in anchors if anchor.module_mentions)
    docs_with_ip = sum(1 for anchor in anchors if anchor.ip_block or anchor.ip_mentions)
    docs_with_label = sum(1 for anchor in anchors if anchor.label_mentions)
    rtl_doc_kinds = {"opentitan_ip_doc", "opentitan_ip_hjson", "testplan", "ibex_reference", "prim_doc"}
    rtl_docs = [row for row in doc_rows if row["doc_kind"] in rtl_doc_kinds]
    rtl_docs_linked = [row for row in rtl_docs if row["confidence"] != "none"]
    modules_with_docs = sum(1 for row in module_rows if row["doc_count"] > 0)
    modules_with_exact_docs = sum(1 for row in module_rows if row["exact_doc_count"] > 0)
    modules_with_ip_docs = sum(1 for row in module_rows if row["ip_doc_count"] > 0)
    ip_blocks_with_docs = sum(1 for ip in ip_blocks if ip_docs.get(ip))

    summary = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "architecture": {
            "code_kg": "custom RTL ontology/KG remains primary retrieval engine",
            "graphify": "assistant architecture/navigation graph",
            "openkb": "separate spec/document wiki graph",
            "integration": "late binding by module_name, ip_block, spec_section, doc_anchor, approved_label",
        },
        "inputs": {
            "spec_dir": str(args.spec_dir),
            "seed": str(args.seed),
            "labels": str(args.labels),
            "documents_seen": total_docs,
            "modules_seen": len(modules),
            "ip_blocks_seen": len(ip_blocks),
        },
        "doc_linking": {
            "docs_with_any_link": docs_with_any,
            "docs_with_any_link_rate": round(docs_with_any / total_docs, 4) if total_docs else 0,
            "docs_with_module_name_link": docs_with_module,
            "docs_with_ip_block_link": docs_with_ip,
            "docs_with_approved_label_link": docs_with_label,
            "rtl_spec_docs": len(rtl_docs),
            "rtl_spec_docs_linked": len(rtl_docs_linked),
            "rtl_spec_docs_link_rate": round(len(rtl_docs_linked) / len(rtl_docs), 4) if rtl_docs else 0,
            "confidence_counts": dict(sorted(Counter(row["confidence"] for row in doc_rows).items())),
            "doc_kind_counts": dict(sorted(Counter(row["doc_kind"] for row in doc_rows).items())),
        },
        "code_coverage": {
            "modules_with_any_doc": modules_with_docs,
            "modules_with_any_doc_rate": round(modules_with_docs / len(modules), 4) if modules else 0,
            "modules_with_exact_doc": modules_with_exact_docs,
            "modules_with_ip_doc": modules_with_ip_docs,
            "ip_blocks_with_docs": ip_blocks_with_docs,
            "ip_blocks_with_docs_rate": round(ip_blocks_with_docs / len(ip_blocks), 4) if ip_blocks else 0,
        },
        "top_ip_blocks_by_doc_count": [
            {"ip_block": ip, "doc_count": len(docs)}
            for ip, docs in sorted(ip_docs.items(), key=lambda item: (-len(item[1]), item[0]))[:25]
        ],
        "top_modules_by_doc_count": [
            {"module": row["module"], "ip_block": row["ip_block"], "doc_count": row["doc_count"], "exact_doc_count": row["exact_doc_count"]}
            for row in sorted(module_rows, key=lambda item: (-item["doc_count"], item["module"]))[:25]
        ],
        "assessment": {
            "can_late_bind": True,
            "physical_merge_recommended": False,
            "main_risk": "Exact module-name links are much sparser than IP/path links; use IP-level binding as the default and exact module links as high-confidence evidence.",
        },
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    write_json(args.out_dir / "spec_code_late_binding_report.json", summary)
    write_json(args.out_dir / "spec_doc_anchors.json", [asdict(anchor) for anchor in anchors])
    write_csv(
        args.out_dir / "spec_doc_links.csv",
        doc_rows,
        ["doc_id", "project", "doc_kind", "ip_block", "confidence", "module_mentions", "ip_mentions", "label_mentions", "spec_sections", "linked_module_count", "token_count"],
    )
    write_csv(
        args.out_dir / "module_doc_coverage.csv",
        module_rows,
        ["project", "module", "ip_block", "doc_count", "exact_doc_count", "ip_doc_count", "labels", "path", "sample_docs"],
    )

    lines = [
        "# Spec-Code KG Late Binding Evaluation",
        "",
        "## Architecture Decision",
        "",
        "- Keep the custom code KG as the primary retrieval engine.",
        "- Keep Graphify as a broad code/architecture navigation graph.",
        "- Keep OpenKB as a separate spec-document wiki/KG.",
        "- Integrate at query time using shared keys: `module_name`, `ip_block`, `spec_section`, `doc_anchor`, and `approved_label`.",
        "",
        "## Link Coverage",
        "",
        f"- Spec docs scanned: {total_docs}",
        f"- Docs with any late-binding key: {docs_with_any} ({summary['doc_linking']['docs_with_any_link_rate']:.2%})",
        f"- RTL/spec-like docs linked: {len(rtl_docs_linked)}/{len(rtl_docs)} ({summary['doc_linking']['rtl_spec_docs_link_rate']:.2%})",
        f"- Module exact-name doc links: {docs_with_module}",
        f"- IP/path doc links: {docs_with_ip}",
        f"- Approved-label doc links: {docs_with_label}",
        "",
        "## Code Coverage",
        "",
        f"- Code modules scanned: {len(modules)}",
        f"- Modules with any doc link: {modules_with_docs} ({summary['code_coverage']['modules_with_any_doc_rate']:.2%})",
        f"- Modules with exact module-name doc link: {modules_with_exact_docs}",
        f"- Modules with IP-level doc link: {modules_with_ip_docs}",
        f"- IP blocks with docs: {ip_blocks_with_docs}/{len(ip_blocks)} ({summary['code_coverage']['ip_blocks_with_docs_rate']:.2%})",
        "",
        "## Top IP Blocks by Spec Doc Count",
        "",
    ]
    for item in summary["top_ip_blocks_by_doc_count"][:15]:
        lines.append(f"- {item['ip_block']}: {item['doc_count']} docs")
    lines += [
        "",
        "## Assessment",
        "",
        "Late binding is feasible and preferable to physical graph merge. The strongest reliable key is `ip_block` from paths and HJSON/doc layout. Exact `module_name` links exist, but are too sparse to be the only integration bridge. `approved_label` is useful as a weak recall signal.",
        "",
        "Recommended query-time flow:",
        "",
        "1. Resolve code query against the custom code KG.",
        "2. Expand result modules to `ip_block` and `approved_label` keys.",
        "3. Fetch OpenKB doc anchors matching those keys.",
        "4. Add Graphify community/context only for architecture questions.",
        "5. Return merged answer with provenance from each store instead of merging graph storage.",
    ]
    md_path = args.out_dir / "SPEC_CODE_LATE_BINDING_EVAL.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    write_pdf(args.out_dir / "SPEC_CODE_LATE_BINDING_EVAL.pdf", "Spec-Code KG Late Binding Evaluation", lines)

    print(json.dumps({
        "status": "ok",
        "out_dir": str(args.out_dir),
        "docs": total_docs,
        "modules": len(modules),
        "docs_linked_rate": summary["doc_linking"]["docs_with_any_link_rate"],
        "rtl_spec_docs_link_rate": summary["doc_linking"]["rtl_spec_docs_link_rate"],
        "modules_with_doc_rate": summary["code_coverage"]["modules_with_any_doc_rate"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
