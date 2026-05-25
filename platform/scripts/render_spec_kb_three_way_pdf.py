#!/usr/bin/env python3
"""Render a professional PDF report for the 3-way spec KB comparison."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = REPO_ROOT / "out" / "reports"
OUT_PDF = OUT_DIR / "spec_kb_three_way_professional_ko.pdf"


def register_fonts() -> str:
    candidates = [
        Path(r"C:\Windows\Fonts\malgun.ttf"),
        Path(r"C:\Windows\Fonts\malgunbd.ttf"),
    ]
    for path in candidates:
        if path.exists():
            pdfmetrics.registerFont(TTFont("ReportFont", str(path)))
            return "ReportFont"
    return "Helvetica"


FONT_NAME = register_fonts()


def make_styles():
    base = getSampleStyleSheet()
    styles = {
        "title": ParagraphStyle(
            "TitleKR",
            parent=base["Title"],
            fontName=FONT_NAME,
            fontSize=22,
            leading=28,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#0f172a"),
            spaceAfter=10,
        ),
        "subtitle": ParagraphStyle(
            "SubtitleKR",
            parent=base["Normal"],
            fontName=FONT_NAME,
            fontSize=10,
            leading=14,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#475569"),
            spaceAfter=18,
        ),
        "h1": ParagraphStyle(
            "H1KR",
            parent=base["Heading1"],
            fontName=FONT_NAME,
            fontSize=15,
            leading=20,
            textColor=colors.HexColor("#0f172a"),
            spaceBefore=10,
            spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "H2KR",
            parent=base["Heading2"],
            fontName=FONT_NAME,
            fontSize=12,
            leading=16,
            textColor=colors.HexColor("#111827"),
            spaceBefore=6,
            spaceAfter=6,
        ),
        "body": ParagraphStyle(
            "BodyKR",
            parent=base["BodyText"],
            fontName=FONT_NAME,
            fontSize=9.5,
            leading=14,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#1f2937"),
            spaceAfter=6,
        ),
        "bullet": ParagraphStyle(
            "BulletKR",
            parent=base["BodyText"],
            fontName=FONT_NAME,
            fontSize=9.5,
            leading=14,
            leftIndent=12,
            firstLineIndent=-8,
            textColor=colors.HexColor("#1f2937"),
            spaceAfter=4,
        ),
        "small": ParagraphStyle(
            "SmallKR",
            parent=base["BodyText"],
            fontName=FONT_NAME,
            fontSize=8.5,
            leading=12,
            textColor=colors.HexColor("#475569"),
            spaceAfter=4,
        ),
    }
    return styles


def p(text: str, style) -> Paragraph:
    return Paragraph(text.replace("\n", "<br/>"), style)


def table(data, col_widths):
    tbl = Table(data, colWidths=col_widths, repeatRows=1)
    tbl.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), FONT_NAME),
                ("FONTSIZE", (0, 0), (-1, -1), 8.5),
                ("LEADING", (0, 0), (-1, -1), 11),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e2e8f0")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#0f172a")),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#cbd5e1")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return tbl


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont(FONT_NAME, 8)
    canvas.setFillColor(colors.HexColor("#64748b"))
    canvas.drawRightString(195 * mm, 10 * mm, f"{doc.page}")
    canvas.restoreState()


def build_pdf():
    styles = make_styles()
    story = []

    story.append(p("Spec KB 3-Way Comparative Evaluation Report", styles["title"]))
    story.append(
        p(
            "작성일: 2026-05-25<br/>기준 시점: 2026-05-25 16:55 KST<br/>대상 워크스페이스: D:\\MyWork\\verilog",
            styles["subtitle"],
        )
    )

    story.append(p("1. Executive Summary", styles["h1"]))
    story.append(
        p(
            "본 보고서는 동일한 spec 문서 집합을 세 가지 방식으로 처리한 결과를 비교 평가한다. 비교 대상은 "
            "<b>OpenKB &lt;- raw docs</b>, <b>Graphify raw</b>, <b>OpenKB &lt;- Graphify wiki</b>이다. "
            "평가 목적은 구조 보존, 탐색성, 요약 품질, deep evidence 회수 능력의 차이를 분석하고 실제 운영 구조를 권고하는 데 있다.",
            styles["body"],
        )
    )
    for line in [
        "구조형 지식 그래프의 품질은 Graphify raw가 가장 우수하다.",
        "사람 중심 탐색성과 요약형 KB 사용성은 OpenKB <- Graphify wiki가 가장 우수하다.",
        "가장 깊은 증거 회수와 원문 coverage는 OpenKB <- raw docs가 가장 우수하다.",
    ]:
        story.append(p(f"- {line}", styles["bullet"]))

    story.append(Spacer(1, 6))
    story.append(
        p(
            "결론적으로 단일 방식으로 모든 목적을 해결하기보다, <b>Graphify raw</b>를 backbone으로 두고 "
            "<b>OpenKB <- Graphify wiki</b>를 browsing layer로, <b>OpenKB <- raw docs</b>를 evidence fallback으로 두는 "
            "계층형 운영이 가장 타당하다.",
            styles["body"],
        )
    )

    story.append(p("2. Evaluation Scope", styles["h1"]))
    story.append(
        p(
            "세 방식은 모두 동일한 원본 문서 집합을 기준으로 한다. 소스 경로는 "
            "D:\\MyWork\\verilog\\out\\spec_documents_20260514_204108 이며, 총 985개 파일로 구성된다.",
            styles["body"],
        )
    )

    scope_table = [
        ["항목", "값"],
        ["전체 파일 수", "985"],
        ["Markdown (.md)", "545"],
        ["HJSON (.hjson)", "367"],
        ["reStructuredText (.rst)", "70"],
        ["주요 프로젝트", "OpenTitan 933, Ibex 52"],
    ]
    story.append(table(scope_table, [55 * mm, 110 * mm]))
    story.append(Spacer(1, 8))

    story.append(p("3. Measured Status Snapshot", styles["h1"]))
    status_table = [
        ["Pipeline", "Current measurable state", "Interpretation"],
        [
            "OpenKB <- raw docs",
            "747 hashes / 748 sources / 747 summaries / 477 concepts / target 985",
            "가장 넓은 coverage를 확보 중이며, 현재도 ingest 진행 중이다.",
        ],
        [
            "Graphify raw",
            "8196 nodes / 30054 edges / 33 communities / 100% extracted",
            "결정론적 구조형 spec graph로서 backbone 역할에 적합하다.",
        ],
        [
            "OpenKB <- Graphify wiki",
            "107 hashes / 104 sources / 104 summaries / 52 concepts",
            "compact input 기반의 안정적인 탐색형 KB가 완성되었다.",
        ],
    ]
    story.append(table(status_table, [42 * mm, 63 * mm, 70 * mm]))
    story.append(Spacer(1, 8))

    story.append(p("4. Architectural Strengths and Limits", styles["h1"]))
    for heading, body, bullets in [
        (
            "4.1 OpenKB <- raw docs",
            "원본 문서를 직접 ingest하기 때문에 section-level evidence 보존력이 가장 높다. registers, interfaces, theory_of_operation, testplan 계열에서 강점을 보인다.",
            [
                "장점: coverage 최상, deep evidence 최상, 상세 spec 회수에 유리",
                "한계: 처리 시간이 가장 길고 retrieval noise 가능성이 가장 크다",
            ],
        ),
        (
            "4.2 Graphify raw",
            "원본 spec 문서를 직접 구조화하는 결정론적 graph pipeline이다. component, topic, community, hub 관점의 해석이 가장 선명하다.",
            [
                "장점: 구조 명확성 최상, 재현성 최상, token cost 없음",
                "한계: 자연어 summary 레이어가 없고 analyst-friendly answer surface가 약하다",
            ],
        ),
        (
            "4.3 OpenKB <- Graphify wiki",
            "Graphify가 먼저 compact wiki/anchor를 만든 뒤 OpenKB가 다시 요약과 개념 연결을 생성한다. 구조 anchor와 탐색성이 균형을 이룬다.",
            [
                "장점: summary, related concepts, related documents가 붙어 사람 중심 탐색이 쉽다",
                "한계: Graphify에서 이미 압축된 정보 이상의 원문 근거를 복원하지는 못한다",
            ],
        ),
    ]:
        story.append(p(heading, styles["h2"]))
        story.append(p(body, styles["body"]))
        for bullet in bullets:
            story.append(p(f"- {bullet}", styles["bullet"]))

    story.append(p("5. Comparative Evaluation Matrix", styles["h1"]))
    matrix_table = [
        ["Category", "OpenKB raw", "Graphify raw", "OpenKB <- Graphify wiki"],
        ["Source coverage", "Highest", "High", "Medium"],
        ["Structural clarity", "Medium", "Highest", "High"],
        ["Natural-language summary", "High", "Low", "High"],
        ["Concept browsing", "Highest", "Low", "Medium to High"],
        ["Traceability", "High", "Highest", "High"],
        ["Processing cost", "Highest", "Lowest", "Low"],
        ["Processing speed", "Slowest", "Fastest", "Fast"],
        ["Retrieval noise risk", "Medium to High", "Low", "Low to Medium"],
        ["Deep evidence fallback", "Highest", "Medium", "Medium"],
        ["Community / topology analysis", "Medium", "Highest", "High"],
    ]
    story.append(table(matrix_table, [44 * mm, 42 * mm, 42 * mm, 52 * mm]))
    story.append(Spacer(1, 8))

    story.append(p("6. Expert Recommendation", styles["h1"]))
    story.append(
        p(
            "단일 저장소로 완전 통합하기보다 역할 기반 계층 구조를 권장한다. Graphify raw를 구조 backbone으로 유지하고, "
            "OpenKB <- Graphify wiki를 analyst browsing layer로 사용하며, OpenKB <- raw docs를 deep evidence fallback으로 두는 방식이 "
            "정확도, 비용, 운영 편의성의 균형이 가장 좋다.",
            styles["body"],
        )
    )
    rec_table = [
        ["Layer", "Recommended system", "Primary role"],
        ["Layer 1", "Graphify raw", "구조 기준면, component map, community map"],
        ["Layer 2", "OpenKB <- Graphify wiki", "빠른 summary browsing, concept navigation"],
        ["Layer 3", "OpenKB <- raw docs", "상세 spec evidence, section-level fallback"],
    ]
    story.append(table(rec_table, [25 * mm, 55 * mm, 100 * mm]))
    story.append(Spacer(1, 8))

    story.append(p("7. Final Conclusion", styles["h1"]))
    story.append(
        p(
            "세 방식은 경쟁 관계라기보다 상호보완 관계에 가깝다. <b>Graphify raw</b>가 가장 좋은 구조형 KG이고, "
            "<b>OpenKB <- Graphify wiki</b>가 가장 좋은 탐색형 KB이며, <b>OpenKB <- raw docs</b>가 가장 좋은 증거 백업층이다. "
            "따라서 실제 운영에서는 세 방식을 분리 계층으로 유지하되, 질의 시점에서 late fusion 형태로 결합하는 것이 가장 현실적이다.",
            styles["body"],
        )
    )
    story.append(
        p(
            "부가적으로, 본 시점의 raw OpenKB ingest는 아직 진행 중이므로 최종 deep evidence 비교는 ingest 완료 후 한 차례 더 업데이트하는 것이 바람직하다.",
            styles["small"],
        )
    )

    doc = SimpleDocTemplate(
        str(OUT_PDF),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=16 * mm,
        title="Spec KB 3-Way Comparative Evaluation Report",
        author="OpenAI Codex",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_pdf()
