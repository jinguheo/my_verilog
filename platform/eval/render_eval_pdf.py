#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def esc_pdf_text(text):
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def wrap_line(text, width=100):
    words = str(text).split()
    if not words:
        return [""]
    lines = []
    cur = words[0]
    for word in words[1:]:
        if len(cur) + 1 + len(word) <= width:
            cur += " " + word
        else:
            lines.append(cur)
            cur = word
    lines.append(cur)
    return lines


def build_lines(kg_summary, benchmark_summary, retrieval_report, multiaxis_summary, multiaxis_report):
    lines = []
    lines.append("RTL Knowledge Graph Evaluation Report")
    lines.append("")
    lines.append("1. KG Construction Criteria")
    lines.append("The KG was built from the full merged ontology seed and merged label set, not from a 100-file sample.")
    lines.append("Construction rules:")
    lines.append("- Nodes: module, ip_block, label, port")
    lines.append("- Edges: HAS_LABEL, HAS_PORT, INSTANTIATES")
    lines.append("- Sources: out/merged_ontology_seed.jsonl and out/merged_labels.jsonl")
    lines.append("- Projects: OpenTitan and Ibex")
    lines.append("- Labels are inferred from module names, paths, ports, and instance clues")
    lines.append("")
    lines.append("2. Full KG Summary")
    lines.append(f"Modules: {kg_summary['modules']}")
    lines.append(f"IP blocks: {kg_summary['ip_blocks']}")
    lines.append(f"Ports: {kg_summary['ports']}")
    lines.append(f"Instance edges: {kg_summary['instance_edges']}")
    lines.append(f"Total nodes: {kg_summary['total_nodes']}")
    lines.append(f"Total edges: {kg_summary['total_edges']}")
    lines.append(f"Projects: {kg_summary['projects']}")
    lines.append(f"Top labels: {kg_summary['top_labels']}")
    lines.append("")
    lines.append("3. Baseline QA Benchmark")
    lines.append(f"Question count: {benchmark_summary['total']}")
    lines.append(f"Question types: {benchmark_summary['types']}")
    lines.append(f"Project mix: {benchmark_summary['projects']}")
    lines.append("")
    lines.append("4. Baseline Retrieval Performance")
    for mode in ["baseline", "kg"]:
        metrics = retrieval_report["by_mode"][mode]
        proxy = retrieval_report["proxy_verilogeval"][mode]["score_100"]
        lines.append(f"{mode}: hit@1={metrics['hit_at_1']}, hit@3={metrics['hit_at_3']}, mrr={metrics['mrr']}, weighted_hit@1={metrics['weighted_hit_at_1']}, proxy_score={proxy}")
        lines.append(f"{mode} by difficulty: {metrics['by_difficulty']}")
    lines.append("")
    lines.append("5. Multi-Axis Question Set")
    lines.append(f"Total questions: {multiaxis_summary['total']}")
    lines.append(f"Per level: {multiaxis_summary['levels']}")
    lines.append(f"Per type: {multiaxis_summary['types']}")
    lines.append("Matrix counts:")
    for level, row in multiaxis_summary["matrix"].items():
        lines.append(f"- {level}: {row}")
    lines.append("")
    lines.append("6. Multi-Axis Retrieval Performance")
    for mode in ["baseline", "kg"]:
        metrics = multiaxis_report["by_mode"][mode]
        lines.append(f"{mode}: hit@1={metrics['hit_at_1']}, hit@3={metrics['hit_at_3']}, mrr={metrics['mrr']}, weighted_hit@1={metrics['weighted_hit_at_1']}")
        lines.append("By level:")
        for level, vals in metrics["by_level"].items():
            lines.append(f"  {level}: hit@1={vals['hit_at_1']}, hit@3={vals['hit_at_3']}, mrr={vals['mrr']}, count={vals['count']}")
        lines.append("By type:")
        for qtype, vals in metrics["by_type"].items():
            lines.append(f"  {qtype}: hit@1={vals['hit_at_1']}, hit@3={vals['hit_at_3']}, mrr={vals['mrr']}, count={vals['count']}")
        lines.append("")
    lines.append("7. VerilogEval Status")
    lines.append("Official verilogeval runner/package was not available in this workspace.")
    lines.append("All score_100 numbers are proxy scores, not official VerilogEval scores.")
    return lines


def build_pdf_bytes(lines):
    wrapped = []
    for line in lines:
        wrapped.extend(wrap_line(line, 95))
    pages = []
    page = []
    for line in wrapped:
        if len(page) >= 44:
            pages.append(page)
            page = []
        page.append(line)
    if page:
        pages.append(page)

    objects = []
    kids = []

    def add_object(content):
        objects.append(content)
        return len(objects)

    font_id = add_object("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")

    page_ids = []
    content_ids = []
    pages_id_placeholder = None

    for page_lines in pages:
        content_lines = ["BT", "/F1 10 Tf", "50 790 Td", "14 TL"]
        first = True
        for line in page_lines:
            safe = esc_pdf_text(line)
            if first:
                content_lines.append(f"({safe}) Tj")
                first = False
            else:
                content_lines.append(f"T* ({safe}) Tj")
        content_lines.append("ET")
        stream = "\n".join(content_lines)
        content_id = add_object(f"<< /Length {len(stream.encode('latin-1', errors='replace'))} >>\nstream\n{stream}\nendstream")
        content_ids.append(content_id)
        page_obj = f"<< /Type /Page /Parent PAGES_ID 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 {font_id} 0 R >> >> /Contents {content_id} 0 R >>"
        page_id = add_object(page_obj)
        page_ids.append(page_id)

    kids_refs = " ".join(f"{pid} 0 R" for pid in page_ids)
    pages_id = add_object(f"<< /Type /Pages /Count {len(page_ids)} /Kids [ {kids_refs} ] >>")
    catalog_id = add_object(f"<< /Type /Catalog /Pages {pages_id} 0 R >>")

    # Patch page objects with actual pages id.
    for idx, obj in enumerate(objects):
        if "/Type /Page" in obj and "PAGES_ID" in obj:
            objects[idx] = obj.replace("PAGES_ID", str(pages_id))

    pdf = [b"%PDF-1.4\n"]
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(sum(len(chunk) for chunk in pdf))
        pdf.append(f"{i} 0 obj\n{obj}\nendobj\n".encode("latin-1", errors="replace"))
    xref_pos = sum(len(chunk) for chunk in pdf)
    pdf.append(f"xref\n0 {len(objects)+1}\n".encode("latin-1"))
    pdf.append(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.append(f"{offset:010d} 00000 n \n".encode("latin-1"))
    pdf.append(f"trailer\n<< /Size {len(objects)+1} /Root {catalog_id} 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode("latin-1"))
    return b"".join(pdf)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kg-summary", required=True)
    ap.add_argument("--benchmark-summary", required=True)
    ap.add_argument("--retrieval-report", required=True)
    ap.add_argument("--multiaxis-summary", required=True)
    ap.add_argument("--multiaxis-report", required=True)
    ap.add_argument("--out-pdf", required=True)
    ap.add_argument("--out-json", required=True)
    args = ap.parse_args()

    kg_summary = json.loads(Path(args.kg_summary).read_text(encoding="utf-8"))
    benchmark_summary = json.loads(Path(args.benchmark_summary).read_text(encoding="utf-8"))
    retrieval_report = json.loads(Path(args.retrieval_report).read_text(encoding="utf-8"))
    multiaxis_summary = json.loads(Path(args.multiaxis_summary).read_text(encoding="utf-8"))
    multiaxis_report = json.loads(Path(args.multiaxis_report).read_text(encoding="utf-8"))

    report_json = {
        "kg_summary": kg_summary,
        "benchmark_summary": benchmark_summary,
        "retrieval_report": retrieval_report,
        "multiaxis_summary": multiaxis_summary,
        "multiaxis_report": multiaxis_report,
    }
    Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_json).write_text(json.dumps(report_json, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = build_lines(kg_summary, benchmark_summary, retrieval_report, multiaxis_summary, multiaxis_report)
    pdf_bytes = build_pdf_bytes(lines)
    Path(args.out_pdf).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_pdf).write_bytes(pdf_bytes)
    print(json.dumps({"status": "ok", "out_pdf": args.out_pdf, "out_json": args.out_json}, ensure_ascii=False))


if __name__ == "__main__":
    main()
