#!/usr/bin/env python3
"""Render the currently indexed OpenKB sample wiki pages as a standalone HTML view."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
WIKI_ROOT = REPO_ROOT / "dbs" / "graphify-out" / "kb-variants" / "spec-only" / "kb" / "wiki"
OUT_DIR = REPO_ROOT / "dbs" / "graphify-out" / "openkb-current"
OUT_HTML = OUT_DIR / "spec_only_openkb_sample.html"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :].lstrip()
    return text


def wikilink_to_html(match: re.Match[str]) -> str:
    target = match.group(1).strip()
    label = target.split("/")[-1].replace("-", " ")
    page_id = target
    return f'<a href="#{html.escape(page_id)}">{html.escape(label)}</a>'


def inline_md(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\[\[([^\]]+)\]\]", wikilink_to_html, escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    return escaped


def markdown_to_html(text: str) -> str:
    text = strip_front_matter(text).replace("\r\n", "\n")
    lines = text.split("\n")
    out: list[str] = []
    in_ul = False
    in_ol = False
    in_code = False
    code_lines: list[str] = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    for raw in lines:
        line = raw.rstrip()
        if line.strip().startswith("```"):
            if in_code:
                out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines = []
                in_code = False
            else:
                close_lists()
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            close_lists()
            continue
        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            close_lists()
            level = len(heading.group(1))
            out.append(f"<h{level}>{inline_md(heading.group(2))}</h{level}>")
            continue
        bullet = re.match(r"^\s*[-*]\s+(.*)$", line)
        if bullet:
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_md(bullet.group(1))}</li>")
            continue
        ordered = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if ordered:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline_md(ordered.group(1))}</li>")
            continue
        close_lists()
        out.append(f"<p>{inline_md(line)}</p>")

    close_lists()
    if in_code:
        out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
    return "\n".join(out)


def collect_pages() -> list[dict[str, str]]:
    pages: list[dict[str, str]] = []
    index_path = WIKI_ROOT / "index.md"
    if index_path.exists():
        pages.append(
            {
                "id": "index",
                "kind": "Index",
                "title": "OpenKB Index",
                "html": markdown_to_html(read_text(index_path)),
            }
        )
    for subdir, kind in (("summaries", "Summary"), ("concepts", "Concept")):
        root = WIKI_ROOT / subdir
        if not root.exists():
            continue
        for path in sorted(root.glob("*.md")):
            page_id = f"{subdir}/{path.stem}"
            title = path.stem.replace("_", " ").replace("-", " ")
            pages.append(
                {
                    "id": page_id,
                    "kind": kind,
                    "title": title,
                    "html": markdown_to_html(read_text(path)),
                }
            )
    return pages


def render_html(pages: list[dict[str, str]]) -> str:
    page_json = json.dumps(pages, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>OpenKB Spec-Only Sample</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f7f8fb;
      --panel: #ffffff;
      --ink: #17202a;
      --muted: #5f6b7a;
      --line: #d8dee8;
      --accent: #006d77;
      --accent-soft: #e1f3f3;
      --code: #f1f4f8;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "Segoe UI", Arial, sans-serif;
      background: var(--bg);
      color: var(--ink);
      letter-spacing: 0;
    }}
    .app {{
      display: grid;
      grid-template-columns: minmax(260px, 340px) minmax(0, 1fr);
      min-height: 100vh;
    }}
    aside {{
      border-right: 1px solid var(--line);
      background: #fbfcfe;
      padding: 18px;
      position: sticky;
      top: 0;
      height: 100vh;
      overflow: auto;
    }}
    main {{
      padding: 28px clamp(20px, 4vw, 56px);
      max-width: 1100px;
      width: 100%;
    }}
    h1, h2, h3 {{ line-height: 1.2; }}
    h1 {{ font-size: 24px; margin: 0 0 8px; }}
    h2 {{ font-size: 22px; margin-top: 28px; border-bottom: 1px solid var(--line); padding-bottom: 8px; }}
    h3 {{ font-size: 18px; margin-top: 22px; }}
    p, li {{ line-height: 1.58; }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .subtitle {{ color: var(--muted); margin: 0 0 16px; font-size: 13px; }}
    .search {{
      width: 100%;
      height: 38px;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 0 10px;
      font-size: 14px;
      margin: 8px 0 14px;
      background: white;
    }}
    .group-label {{
      margin: 18px 0 8px;
      color: var(--muted);
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
    }}
    .nav-item {{
      display: block;
      width: 100%;
      text-align: left;
      border: 0;
      border-radius: 6px;
      background: transparent;
      padding: 9px 10px;
      color: var(--ink);
      cursor: pointer;
      font-size: 13px;
      overflow-wrap: anywhere;
    }}
    .nav-item:hover, .nav-item.active {{ background: var(--accent-soft); color: #004a52; }}
    .badge {{
      display: inline-block;
      padding: 4px 8px;
      border-radius: 999px;
      background: var(--accent-soft);
      color: #00535b;
      font-size: 12px;
      font-weight: 700;
      margin-bottom: 12px;
    }}
    article {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: clamp(18px, 3vw, 34px);
      box-shadow: 0 8px 24px rgba(23, 32, 42, 0.06);
    }}
    code, pre {{
      background: var(--code);
      border-radius: 6px;
    }}
    code {{ padding: 2px 5px; }}
    pre {{ padding: 14px; overflow: auto; }}
    @media (max-width: 820px) {{
      .app {{ grid-template-columns: 1fr; }}
      aside {{ position: static; height: auto; border-right: 0; border-bottom: 1px solid var(--line); }}
      main {{ padding: 18px; }}
    }}
  </style>
</head>
<body>
  <div class="app">
    <aside>
      <h1>OpenKB Sample</h1>
      <p class="subtitle">Spec-only wiki output: 5 summaries and 10 concepts.</p>
      <input class="search" id="search" placeholder="Search pages" />
      <div id="nav"></div>
    </aside>
    <main>
      <article id="content"></article>
    </main>
  </div>
  <script>
    const pages = {page_json};
    const nav = document.getElementById('nav');
    const content = document.getElementById('content');
    const search = document.getElementById('search');

    function renderNav(filter = '') {{
      const query = filter.trim().toLowerCase();
      nav.innerHTML = '';
      const groups = ['Index', 'Summary', 'Concept'];
      for (const group of groups) {{
        const groupPages = pages.filter(p => p.kind === group && (!query || p.title.toLowerCase().includes(query) || p.id.toLowerCase().includes(query)));
        if (!groupPages.length) continue;
        const label = document.createElement('div');
        label.className = 'group-label';
        label.textContent = `${{group}} (${{groupPages.length}})`;
        nav.appendChild(label);
        for (const page of groupPages) {{
          const button = document.createElement('button');
          button.className = 'nav-item';
          button.dataset.pageId = page.id;
          button.textContent = page.title;
          button.onclick = () => showPage(page.id);
          nav.appendChild(button);
        }}
      }}
      syncActive();
    }}

    function syncActive() {{
      const active = location.hash.slice(1) || 'index';
      document.querySelectorAll('.nav-item').forEach(btn => {{
        btn.classList.toggle('active', btn.dataset.pageId === active);
      }});
    }}

    function showPage(id) {{
      const page = pages.find(p => p.id === id) || pages[0];
      location.hash = page.id;
      content.innerHTML = `<div class="badge">${{page.kind}}</div>` + page.html;
      syncActive();
    }}

    search.addEventListener('input', () => renderNav(search.value));
    window.addEventListener('hashchange', () => showPage(location.hash.slice(1) || 'index'));
    renderNav();
    showPage(location.hash.slice(1) || 'index');
  </script>
</body>
</html>
"""


def main() -> None:
    pages = collect_pages()
    if not pages:
        raise SystemExit(f"No OpenKB pages found under {WIKI_ROOT}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_HTML.write_text(render_html(pages), encoding="utf-8")
    print(f"Wrote {OUT_HTML}")
    print(f"Pages: {len(pages)}")


if __name__ == "__main__":
    main()
