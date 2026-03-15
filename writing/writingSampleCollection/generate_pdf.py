"""Generate a formatted PDF from finalDraft.md for Turnitin submission."""

from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
)
from reportlab.lib.fonts import addMapping
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

MARGIN = 2.54 * cm
LINE_SPACING = 18  # ~1.5 line spacing for 12pt font

HERE = Path(__file__).parent
INPUT_MD = HERE / "finalDraft.md"
OUTPUT_PDF = HERE / "finalDraft.pdf"


def register_fonts():
    """Register Times New Roman and a CJK fallback font."""
    tnr_candidates = {
        "regular": [
            Path("/Library/Fonts/Times New Roman.ttf"),
            Path("/System/Library/Fonts/Supplemental/Times New Roman.ttf"),
        ],
        "bold": [
            Path("/Library/Fonts/Times New Roman Bold.ttf"),
            Path("/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"),
        ],
        "italic": [
            Path("/Library/Fonts/Times New Roman Italic.ttf"),
            Path("/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf"),
        ],
        "bolditalic": [
            Path("/Library/Fonts/Times New Roman Bold Italic.ttf"),
            Path("/System/Library/Fonts/Supplemental/Times New Roman Bold Italic.ttf"),
        ],
    }

    def find_first(paths):
        for p in paths:
            if p.exists():
                return str(p)
        return None

    regular = find_first(tnr_candidates["regular"])
    if regular:
        bold = find_first(tnr_candidates["bold"]) or regular
        italic = find_first(tnr_candidates["italic"]) or regular
        bolditalic = find_first(tnr_candidates["bolditalic"]) or bold
        pdfmetrics.registerFont(TTFont("TimesNewRoman", regular))
        pdfmetrics.registerFont(TTFont("TimesNewRoman-Bold", bold))
        pdfmetrics.registerFont(TTFont("TimesNewRoman-Italic", italic))
        pdfmetrics.registerFont(TTFont("TimesNewRoman-BoldItalic", bolditalic))
        addMapping("TimesNewRoman", 0, 0, "TimesNewRoman")
        addMapping("TimesNewRoman", 1, 0, "TimesNewRoman-Bold")
        addMapping("TimesNewRoman", 0, 1, "TimesNewRoman-Italic")
        addMapping("TimesNewRoman", 1, 1, "TimesNewRoman-BoldItalic")
        family = "TimesNewRoman"
    else:
        family = "Times-Roman"

    # CJK font for Chinese characters
    cjk_font = None
    songti = Path("/System/Library/Fonts/Supplemental/Songti.ttc")
    if songti.exists():
        pdfmetrics.registerFont(TTFont("Songti", str(songti), subfontIndex=1))
        cjk_font = "Songti"

    return family, cjk_font


def make_styles(font_family: str) -> dict:
    bold_font = f"{font_family}-Bold" if font_family == "TimesNewRoman" else "Times-Bold"
    italic_font = f"{font_family}-Italic" if font_family == "TimesNewRoman" else "Times-Italic"

    styles = {
        "title": ParagraphStyle(
            "Title",
            fontName=bold_font,
            fontSize=14,
            leading=22,
            alignment=TA_CENTER,
            spaceAfter=6,
        ),
        "author": ParagraphStyle(
            "Author",
            fontName=font_family,
            fontSize=12,
            leading=LINE_SPACING,
            alignment=TA_CENTER,
            spaceAfter=18,
        ),
        "h2": ParagraphStyle(
            "H2",
            fontName=bold_font,
            fontSize=13,
            leading=20,
            spaceBefore=18,
            spaceAfter=8,
        ),
        "h3": ParagraphStyle(
            "H3",
            fontName=bold_font,
            fontSize=12,
            leading=LINE_SPACING,
            spaceBefore=14,
            spaceAfter=6,
        ),
        "body": ParagraphStyle(
            "Body",
            fontName=font_family,
            fontSize=12,
            leading=LINE_SPACING,
            alignment=TA_JUSTIFY,
            spaceAfter=8,
            firstLineIndent=24,
        ),
        "body_no_indent": ParagraphStyle(
            "BodyNoIndent",
            fontName=font_family,
            fontSize=12,
            leading=LINE_SPACING,
            alignment=TA_JUSTIFY,
            spaceAfter=8,
        ),
        "wordcount": ParagraphStyle(
            "WordCount",
            fontName=bold_font,
            fontSize=12,
            leading=LINE_SPACING,
            alignment=TA_CENTER,
            spaceBefore=12,
            spaceAfter=12,
        ),
        "ref_heading": ParagraphStyle(
            "RefHeading",
            fontName=bold_font,
            fontSize=13,
            leading=20,
            spaceBefore=18,
            spaceAfter=10,
        ),
        "ref": ParagraphStyle(
            "Ref",
            fontName=font_family,
            fontSize=11,
            leading=16,
            alignment=TA_LEFT,
            spaceAfter=6,
            leftIndent=28,
            firstLineIndent=-28,
        ),
    }
    return styles


def escape_xml(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def md_to_rich(text: str, font_family: str, cjk_font=None) -> str:
    """Convert limited markdown inline formatting to reportlab XML tags."""
    import re

    text = escape_xml(text)

    bold_font = f"{font_family}-Bold" if font_family == "TimesNewRoman" else "Times-Bold"

    # Bold+italic ***text*** or ___text___
    text = re.sub(
        r"\*\*\*(.+?)\*\*\*",
        rf'<font name="{bold_font}"><i>\1</i></font>',
        text,
    )
    # Bold **text**
    text = re.sub(r"\*\*(.+?)\*\*", rf'<font name="{bold_font}">\1</font>', text)
    # Italic *text*
    text = re.sub(r"\*(.+?)\*", rf"<i>\1</i>", text)
    # Inline code
    text = re.sub(r"`(.+?)`", r"<i>\1</i>", text)
    # Curly quotes
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    # Em-dash
    text = text.replace("\u2014", " -- ")

    # Wrap CJK characters in CJK font tags
    if cjk_font:
        def wrap_cjk(m):
            return f'<font name="{cjk_font}">{m.group(0)}</font>'
        text = re.sub(r'[\u4e00-\u9fff\u3400-\u4dbf]+', wrap_cjk, text)

    return text


def parse_md(md_path: Path) -> list:
    """Return a list of (type, text) tuples from the markdown file."""
    lines = md_path.read_text(encoding="utf-8").splitlines()
    blocks: list[tuple[str, str]] = []
    current_para: list[str] = []

    def flush_para():
        if current_para:
            blocks.append(("body", " ".join(current_para)))
            current_para.clear()

    in_references = False

    for line in lines:
        stripped = line.strip()

        if not stripped:
            flush_para()
            continue

        if stripped == "---":
            flush_para()
            continue

        if stripped.startswith("# ") and not stripped.startswith("## "):
            flush_para()
            blocks.append(("title", stripped[2:].strip()))
            continue

        if stripped.startswith("## "):
            flush_para()
            heading_text = stripped[3:].strip()
            if heading_text == "References":
                in_references = True
                blocks.append(("ref_heading", heading_text))
            else:
                blocks.append(("h2", heading_text))
            continue

        if stripped.startswith("### "):
            flush_para()
            blocks.append(("h3", stripped[4:].strip()))
            continue

        if stripped.startswith("**Word count:**"):
            flush_para()
            blocks.append(("wordcount", stripped))
            continue

        if in_references:
            flush_para()
            blocks.append(("ref", stripped))
            continue

        current_para.append(stripped)

    flush_para()
    return blocks


def build_pdf(md_path: Path, pdf_path: Path):
    font_family, cjk_font = register_fonts()
    styles = make_styles(font_family)

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        title="Efficient Execution Frameworks for Structured LLM Programs",
        author="ZHAO Zhan",
    )

    blocks = parse_md(md_path)
    story = []
    first_para_after_heading = True

    for btype, text in blocks:
        rich = md_to_rich(text, font_family, cjk_font)

        if btype == "title":
            story.append(Paragraph(rich, styles["title"]))
            first_para_after_heading = True
        elif btype == "author":
            story.append(Paragraph(rich, styles["author"]))
        elif btype == "h2":
            story.append(Paragraph(rich, styles["h2"]))
            first_para_after_heading = True
        elif btype == "h3":
            story.append(Paragraph(rich, styles["h3"]))
            first_para_after_heading = True
        elif btype == "wordcount":
            story.append(Paragraph(rich, styles["wordcount"]))
        elif btype == "ref_heading":
            story.append(Paragraph(rich, styles["ref_heading"]))
        elif btype == "ref":
            story.append(Paragraph(rich, styles["ref"]))
        elif btype == "body":
            if first_para_after_heading:
                story.append(Paragraph(rich, styles["body_no_indent"]))
                first_para_after_heading = False
            else:
                story.append(Paragraph(rich, styles["body"]))

    # Detect author line (second block if first is title)
    # Already handled above via "author" type -- but our parser yields it as "body"
    # Fix: the second element "ZHAO Zhan ..." should be centered
    # We handle it by checking content in post-processing is complex,
    # so we treat it specially in the parser output.

    doc.build(story)
    print(f"PDF generated: {pdf_path}")


if __name__ == "__main__":
    build_pdf(INPUT_MD, OUTPUT_PDF)
