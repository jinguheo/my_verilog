#!/usr/bin/env python3
"""Run OpenKB status/list for prepared KB variants without LLM-only deps.

The local OpenKB CLI imports optional LLM/conversion packages at import time.
For status/list comparisons those packages are not used, so this runner stubs
them and calls the real OpenKB CLI against prepared KB workspaces.
"""

from __future__ import annotations

import argparse
import json
import sys
import types
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OPENKB_ROOT = ROOT / "tools" / "OpenKB"
DEFAULT_OUT = ROOT / "dbs" / "graphify-out" / "openkb_compare"
KB_VARIANTS = {
    "spec-only": ROOT / "dbs" / "graphify-out" / "kb-variants" / "spec-only" / "kb",
    "spec-code": ROOT / "dbs" / "graphify-out" / "kb-variants" / "spec-code" / "kb",
}


def install_import_stubs() -> None:
    sys.path.insert(0, str(OPENKB_ROOT))

    agents = types.ModuleType("agents")
    agents.set_tracing_disabled = lambda *args, **kwargs: None
    sys.modules.setdefault("agents", agents)

    litellm = types.ModuleType("litellm")
    litellm.suppress_debug_info = True
    litellm.api_key = ""
    sys.modules.setdefault("litellm", litellm)

    dotenv = types.ModuleType("dotenv")
    dotenv.load_dotenv = lambda *args, **kwargs: False
    sys.modules.setdefault("dotenv", dotenv)

    class YamlStub(types.ModuleType):
        def safe_load(self, handle):
            text = handle.read() if hasattr(handle, "read") else str(handle)
            out = {}
            for line in text.splitlines():
                line = line.strip()
                if not line or line.startswith("#") or ":" not in line:
                    continue
                key, value = line.split(":", 1)
                value = value.strip().strip("\"'")
                if value.isdigit():
                    value = int(value)
                out[key.strip()] = value
            return out

        def safe_dump(self, data, handle, **_kwargs):
            handle.write("\n".join(f"{key}: {value}" for key, value in sorted(data.items())) + "\n")

    sys.modules.setdefault("yaml", YamlStub("yaml"))

    pymupdf = types.ModuleType("pymupdf")
    pymupdf.open = lambda *args, **kwargs: (_ for _ in ()).throw(
        RuntimeError("pymupdf stub is unavailable for add/convert; status/list only")
    )
    sys.modules.setdefault("pymupdf", pymupdf)

    markitdown = types.ModuleType("markitdown")

    class MarkItDown:
        pass

    markitdown.MarkItDown = MarkItDown
    sys.modules.setdefault("markitdown", markitdown)


def run_cli(kb_dir: Path, command: str) -> str:
    from openkb.cli import cli

    buffer = StringIO()
    with redirect_stdout(buffer):
        cli(args=["--kb-dir", str(kb_dir), command], standalone_mode=False)
    return buffer.getvalue()


def count_files(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.rglob("*") if item.is_file())


def summarize_kb(kb_dir: Path) -> dict[str, object]:
    raw_dir = kb_dir / "raw"
    wiki_dir = kb_dir / "wiki"
    return {
        "kb_dir": str(kb_dir),
        "raw_files": count_files(raw_dir),
        "wiki_files": count_files(wiki_dir),
        "source_files": count_files(wiki_dir / "sources"),
        "summary_files": count_files(wiki_dir / "summaries"),
        "concept_files": count_files(wiki_dir / "concepts"),
        "report_files": count_files(wiki_dir / "reports"),
        "hashes_file": str(kb_dir / ".openkb" / "hashes.json"),
    }


def write_report(out_dir: Path, results: dict[str, dict[str, object]]) -> None:
    lines = [
        "# OpenKB Offline Variant Comparison",
        "",
        "This report runs OpenKB `status` and `list` against the prepared KB variants.",
        "LLM-backed `add/query` was not executed.",
        "",
        "## Summary",
        "",
        "| Variant | Raw files | Wiki files | Source files | Summaries | Concepts | Reports |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for name, result in results.items():
        summary = result["summary"]
        lines.append(
            f"| {name} | {summary['raw_files']} | {summary['wiki_files']} | {summary['source_files']} | "
            f"{summary['summary_files']} | {summary['concept_files']} | {summary['report_files']} |"
        )
    lines.extend(["", "## OpenKB CLI Output", ""])
    for name, result in results.items():
        lines.extend(
            [
                f"### {name} status",
                "",
                "```text",
                str(result["status"]).rstrip(),
                "```",
                "",
                f"### {name} list",
                "",
                "```text",
                str(result["list"]).rstrip(),
                "```",
                "",
            ]
        )
    (out_dir / "openkb_offline_compare.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    install_import_stubs()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    results: dict[str, dict[str, object]] = {}
    for name, kb_dir in KB_VARIANTS.items():
        results[name] = {
            "summary": summarize_kb(kb_dir),
            "status": run_cli(kb_dir, "status"),
            "list": run_cli(kb_dir, "list"),
        }

    (args.out_dir / "openkb_offline_compare.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_report(args.out_dir, results)
    print(json.dumps({"status": "ok", "out_dir": str(args.out_dir)}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
