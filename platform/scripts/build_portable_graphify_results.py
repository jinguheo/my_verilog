#!/usr/bin/env python3
"""Build a portable result bundle for Graphify spec/code KG inspection."""

from __future__ import annotations

import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HTML_VIEWS = ROOT / "dbs" / "graphify-out" / "html-views"
SCHEMATIC = ROOT / "dbs" / "graphify-out" / "schematic"
OUT_DIR = ROOT / "dbs" / "graphify-out" / "portable-results"
DATA_DIR = OUT_DIR / "data"


COPY_GROUPS = {
    "benchmark": [
        ROOT / "out" / "spec_code_retrieval_benchmark" / "catalog.md",
        ROOT / "out" / "spec_code_retrieval_benchmark" / "prompts_only.jsonl",
        ROOT / "out" / "spec_code_retrieval_benchmark" / "questions_all.jsonl",
    ],
    "traceability_eval": [
        ROOT / "out" / "spec_code_graphify_variant_eval" / "spec_code_graphify_variant_report.md",
        ROOT / "out" / "spec_code_graphify_variant_eval" / "spec_code_question_answer_details.csv",
        ROOT / "out" / "spec_code_graphify_variant_eval" / "spec_code_question_answer_details.md",
        ROOT / "out" / "spec_code_graphify_variant_eval" / "spec_code_question_answer_details.jsonl",
    ],
    "user_qa": [
        ROOT / "out" / "spec_code_user_qa_benchmark" / "catalog.md",
        ROOT / "out" / "spec_code_user_qa_benchmark" / "user_qa_prompts_only.jsonl",
        ROOT / "out" / "spec_code_user_qa_benchmark" / "user_qa_questions_all.jsonl",
        ROOT / "out" / "spec_code_user_qa_eval" / "spec_code_graphify_variant_report.md",
        ROOT / "out" / "spec_code_user_qa_eval" / "spec_code_question_answer_details.csv",
        ROOT / "out" / "spec_code_user_qa_eval" / "spec_code_question_answer_details.md",
        ROOT / "out" / "spec_code_user_qa_eval" / "spec_code_question_answer_details.jsonl",
    ],
    "sva_dv_qa": [
        ROOT / "out" / "spec_code_sva_dv_user_qa_benchmark" / "catalog.md",
        ROOT / "out" / "spec_code_sva_dv_user_qa_benchmark" / "sva_dv_user_qa_prompts_only.jsonl",
        ROOT / "out" / "spec_code_sva_dv_user_qa_benchmark" / "sva_dv_user_qa_questions_all.jsonl",
        ROOT / "out" / "spec_code_sva_dv_user_qa_eval" / "spec_code_graphify_variant_report.md",
        ROOT / "out" / "spec_code_sva_dv_user_qa_eval" / "spec_code_question_answer_details.csv",
        ROOT / "out" / "spec_code_sva_dv_user_qa_eval" / "spec_code_question_answer_details.md",
        ROOT / "out" / "spec_code_sva_dv_user_qa_eval" / "spec_code_question_answer_details.jsonl",
    ],
}


def copy_file(src: Path, dst: Path) -> dict[str, object]:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return {
        "source": str(src.relative_to(ROOT)),
        "portable_path": str(dst.relative_to(OUT_DIR)).replace("\\", "/"),
        "bytes": dst.stat().st_size,
    }


def write_open_me(copied: dict[str, list[dict[str, object]]]) -> None:
    def file_links(group: str) -> str:
        items = copied[group]
        lis = []
        for item in items:
            href = item["portable_path"]
            label = Path(str(href)).name
            size_kb = round(int(item["bytes"]) / 1024, 1)
            lis.append(f'<li><a href="{href}">{label}</a> <span>{size_kb} KB</span></li>')
        return "\n".join(lis)

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Portable Spec-Code KG Results</title>
<style>
body{{margin:0;font-family:Arial,Helvetica,sans-serif;background:#f8fafc;color:#17202a}}
main{{max-width:1120px;margin:0 auto;padding:32px 22px 56px}}
h1{{font-size:30px;margin:0 0 8px}} h2{{font-size:20px;margin:28px 0 10px}}
p{{color:#475569;line-height:1.5}} .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}}
.card{{display:block;background:#fff;border:1px solid #d6dee8;border-radius:8px;padding:16px;text-decoration:none;color:#17202a}}
.card:hover{{background:#f1f5f9}} .meta{{font-size:13px;color:#64748b}}
ul{{margin:8px 0 0;padding-left:20px}} li{{margin:5px 0;line-height:1.35}} a{{color:#0f5c9c}} span{{color:#64748b;font-size:12px}}
code{{background:#e8eef5;border-radius:4px;padding:2px 5px}}
</style>
</head>
<body><main>
<h1>Portable Spec-Code KG Results</h1>
<p>Open this file from any cloned or copied workspace. The graph views are self-contained HTML files; the evaluation files are collected under <code>data/</code>.</p>

<h2>Graph Views</h2>
<div class="grid">
  <a class="card" href="html/spec-only.html"><strong>spec-only graph</strong><p class="meta">Spec document KG view.</p></a>
  <a class="card" href="html/code-only.html"><strong>code-only graph</strong><p class="meta">Code KG view.</p></a>
  <a class="card" href="html/spec-code.html"><strong>spec-code graph</strong><p class="meta">Integrated spec/code graph with bridge edges.</p></a>
  <a class="card" href="html/verilog_module_schematic.html"><strong>Verilog module schematic</strong><p class="meta">Top/module hierarchy and instantiation schematic from the code graph.</p></a>
</div>

<h2>Traceability Benchmark</h2>
<ul>{file_links("benchmark")}</ul>

<h2>Traceability Evaluation</h2>
<ul>{file_links("traceability_eval")}</ul>

<h2>User QA Evaluation</h2>
<ul>{file_links("user_qa")}</ul>

<h2>SVA / DV Verification QA Evaluation</h2>
<ul>{file_links("sva_dv_qa")}</ul>

<h2>Full Graph JSON</h2>
<p>The large full graph files are not duplicated in this portable folder. They remain available through relative paths in the repository:</p>
<ul>
  <li><a href="../spec-only-graphify/graph.json">../spec-only-graphify/graph.json</a></li>
  <li><a href="../code-only-graphify/graph.json">../code-only-graphify/graph.json</a></li>
  <li><a href="../spec-code-graphify/graph.json">../spec-code-graphify/graph.json</a></li>
</ul>
</main></body></html>
"""
    (OUT_DIR / "OPEN_ME.html").write_text(html, encoding="utf-8")


def write_readme(copied: dict[str, list[dict[str, object]]]) -> None:
    lines = [
        "# Portable Spec-Code KG Results",
        "",
        "Open `OPEN_ME.html` on another PC after cloning or copying this repository.",
        "",
        "The graph HTML files are self-contained and do not require a web server or CDN.",
        "Evaluation data is collected in `data/` so the reports can be opened directly.",
        "",
        "Full graph JSON files are intentionally referenced from the sibling Graphify variant folders instead of duplicated here.",
        "",
        "## Contents",
        "",
    ]
    for group, items in copied.items():
        lines.append(f"### {group}")
        for item in items:
            lines.append(f"- `{item['portable_path']}`")
        lines.append("")
    (OUT_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "html").mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    for name in ("index.html", "spec-only.html", "code-only.html", "spec-code.html"):
        shutil.copy2(HTML_VIEWS / name, OUT_DIR / "html" / name)
    schematic_html = SCHEMATIC / "verilog_module_schematic.html"
    schematic_data = SCHEMATIC / "verilog_module_schematic_data.json"
    if schematic_html.exists():
        shutil.copy2(schematic_html, OUT_DIR / "html" / "verilog_module_schematic.html")
    if schematic_data.exists():
        (DATA_DIR / "schematic").mkdir(parents=True, exist_ok=True)
        shutil.copy2(schematic_data, DATA_DIR / "schematic" / "verilog_module_schematic_data.json")

    copied: dict[str, list[dict[str, object]]] = {}
    for group, paths in COPY_GROUPS.items():
        copied[group] = []
        for src in paths:
            if src.exists():
                dst = DATA_DIR / group / src.name
                copied[group].append(copy_file(src, dst))

    manifest = {
        "description": "Portable Graphify spec/code KG results for offline inspection on another PC.",
        "open": "OPEN_ME.html",
        "graph_views": [
            "html/spec-only.html",
            "html/code-only.html",
            "html/spec-code.html",
            "html/verilog_module_schematic.html",
        ],
        "data": copied,
        "full_graph_json": [
            "../spec-only-graphify/graph.json",
            "../code-only-graphify/graph.json",
            "../spec-code-graphify/graph.json",
        ],
    }
    (OUT_DIR / "portable_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_open_me(copied)
    write_readme(copied)
    print(json.dumps({"status": "ok", "out_dir": str(OUT_DIR), "files": sum(len(v) for v in copied.values()) + 7}, indent=2))


if __name__ == "__main__":
    main()
