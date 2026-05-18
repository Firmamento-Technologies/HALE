"""
Build PPTX deck HALE 3-slide in English, style coerente con il deck master
Firmamento Technologies (dark navy + gold accents, monospace + sans-serif).
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt, Cm, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

BASE = "/home/user/HALE/studio-di-fattibilita"
ASSETS = "/home/user/HALE/cad"
OUT = os.path.join(BASE, "deliverables-FINAL")
LOGO = os.path.join(ASSETS, "LogoFirmamento Technologies.png")
HALE_RENDER = os.path.join(ASSETS, "HALE2.png")
OUT_PPTX = os.path.join(OUT, "DECK-HALE-3slide-EN.pptx")

NAVY = RGBColor(0x0a, 0x1a, 0x3d)
GOLD = RGBColor(0xf0, 0xc9, 0x5c)
GOLD_DARK = RGBColor(0xc9, 0xa6, 0x4a)
LIGHT_BLUE = RGBColor(0xa8, 0xc5, 0xeb)
WHITE = RGBColor(0xff, 0xff, 0xff)
GREY = RGBColor(0x3a, 0x3a, 0x3a)
GREY_LIGHT = RGBColor(0xe6, 0xe6, 0xea)

prs = Presentation()
prs.slide_width = Cm(33.867)
prs.slide_height = Cm(19.05)
SW = prs.slide_width
SH = prs.slide_height
BLANK = prs.slide_layouts[6]

FONT_DISPLAY = "Inter"     # fallback Calibri
FONT_BODY = "Inter"
FONT_MONO = "Consolas"     # monospace

def text_box(slide, x, y, w, h, text, font_size=14, bold=False, italic=False,
             color=WHITE, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
             font_name=FONT_BODY, line_spacing=1.2):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    lines = text.split("\n") if isinstance(text, str) else [text]
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        r = p.add_run()
        r.text = line
        r.font.size = Pt(font_size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
        r.font.name = font_name
    return tb

def rich_text_box(slide, x, y, w, h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
                  line_spacing=1.3):
    """runs = list of dicts {text, size, bold, italic, color, font}"""
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    for r_def in runs:
        r = p.add_run()
        r.text = r_def["text"]
        r.font.size = Pt(r_def.get("size", 12))
        r.font.bold = r_def.get("bold", False)
        r.font.italic = r_def.get("italic", False)
        r.font.color.rgb = r_def.get("color", WHITE)
        r.font.name = r_def.get("font", FONT_BODY)
    return tb

def add_rect(slide, x, y, w, h, fill=NAVY, line=None, line_w=0.75):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    if line:
        shape.line.color.rgb = line
        shape.line.width = Pt(line_w)
    else:
        shape.line.fill.background()
    return shape

def add_line(slide, x1, y1, x2, y2, color=GOLD, weight=1.0):
    line = slide.shapes.add_connector(1, x1, y1, x2, y2)
    line.line.color.rgb = color
    line.line.width = Pt(weight)
    return line

def add_image(slide, path, x, y, w=None, h=None):
    if not os.path.exists(path):
        return None
    if w and h:
        return slide.shapes.add_picture(path, x, y, width=w, height=h)
    if w:
        return slide.shapes.add_picture(path, x, y, width=w)
    if h:
        return slide.shapes.add_picture(path, x, y, height=h)
    return slide.shapes.add_picture(path, x, y)

# ============== SLIDE 1: PROJECT HALE ==============
def slide_1_intro():
    s = prs.slides.add_slide(BLANK)
    add_rect(s, 0, 0, SW, SH, fill=NAVY)

    # Title block top-left
    text_box(s, Cm(1.5), Cm(1.5), Cm(20), Cm(2),
             "Project H.A.L.E.",
             font_size=46, bold=True, color=WHITE, font_name=FONT_DISPLAY,
             anchor=MSO_ANCHOR.TOP)
    text_box(s, Cm(1.5), Cm(3.5), Cm(20), Cm(1),
             "(High Altitude Long Endurance)",
             font_size=22, color=WHITE, font_name=FONT_DISPLAY)

    # Subtitle
    text_box(s, Cm(1.5), Cm(5.5), Cm(15), Cm(2.5),
             "The cooperative pseudo-satellite\nfor national resilience.",
             font_size=20, color=WHITE, font_name=FONT_MONO, line_spacing=1.4)

    # Tech specs (style monospace, code-like)
    specs_y = Cm(9.5)
    specs = [
        ("Operating altitude", "20 km", LIGHT_BLUE, WHITE),
        ("Macro-regional coverage", "> 500 km", LIGHT_BLUE, WHITE),
        ("Latency", "< 20 ms", LIGHT_BLUE, WHITE),
        ("Propulsion", "Solar-electric", LIGHT_BLUE, WHITE),
        ("Endurance target", "30+ days perennial (Y3)", LIGHT_BLUE, WHITE),
    ]
    for label, val, color_l, color_v in specs:
        rich_text_box(s, Cm(1.5), specs_y, Cm(15), Cm(0.9), [
            {"text": label + " ", "size": 16, "color": color_l, "font": FONT_MONO},
            {"text": val, "size": 16, "color": color_v, "bold": True, "font": FONT_MONO},
        ])
        specs_y += Cm(1.1)

    # HALE Render right side
    add_image(s, HALE_RENDER, Cm(16.5), Cm(4.5), w=Cm(16), h=Cm(11))

    # Footer / branding
    add_line(s, Cm(1.5), SH - Cm(1.6), SW - Cm(1.5), SH - Cm(1.6), color=GOLD, weight=0.5)
    text_box(s, Cm(1.5), SH - Cm(1.2), Cm(15), Cm(0.6),
             "FIRMAMENTO TECHNOLOGIES",
             font_size=9, bold=True, color=GOLD, font_name=FONT_DISPLAY)
    text_box(s, SW - Cm(16.5), SH - Cm(1.2), Cm(15), Cm(0.6),
             "Pentema pilot . Liguria SNAI . Cooperative Deep-Tech",
             font_size=9, color=WHITE, font_name=FONT_MONO,
             align=PP_ALIGN.RIGHT)

# ============== SLIDE 2: VALUE / USE CASES ==============
def slide_2_value():
    s = prs.slides.add_slide(BLANK)
    add_rect(s, 0, 0, SW, SH, fill=WHITE)

    # Title
    text_box(s, Cm(1.5), Cm(1.2), Cm(30), Cm(1.8),
             "Public Value & Territorial Resilience",
             font_size=36, bold=True, color=NAVY, font_name=FONT_DISPLAY)
    text_box(s, Cm(1.5), Cm(3.1), Cm(30), Cm(0.9),
             "Standardized plug-and-play interface for rapid sensor integration.",
             font_size=15, color=GREY, font_name=FONT_MONO)

    # H.A.L.E. Core vertical box (left side)
    core_x = Cm(2)
    core_y = Cm(6)
    core_w = Cm(2.2)
    core_h = Cm(11)
    add_rect(s, core_x, core_y, core_w, core_h, fill=WHITE, line=NAVY, line_w=1.5)
    # Vertical text inside
    text_box(s, core_x, core_y, core_w, core_h,
             "H.A.L.E.\nCore",
             font_size=15, bold=True, color=NAVY, font_name=FONT_MONO,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Connecting line
    conn_x = Cm(4.4)
    add_line(s, conn_x, Cm(11.5), Cm(6.5), Cm(11.5), color=NAVY, weight=1.2)

    # 4 use case boxes (right side, vertical stack)
    use_cases = [
        ("Disaster Response", "Rapid", "network restoration after floods or landslides.", LIGHT_BLUE),
        ("Environmental Monitoring", "Wildfire alert", "and hydrogeological surveillance, multispectral / thermal sensors.", LIGHT_BLUE),
        ("Telemedicine", "Ultra-reliable", "network links for remote health posts.", LIGHT_BLUE),
        ("Civic Connectivity", "Smart agriculture", "and local e-governance support.", LIGHT_BLUE),
    ]
    uc_y = Cm(6)
    uc_x = Cm(6.5)
    uc_w = Cm(25)
    uc_h = Cm(2.5)
    uc_spacing = Cm(0.4)
    for title, keyword, desc, key_color in use_cases:
        add_rect(s, uc_x, uc_y, uc_w, uc_h, fill=WHITE, line=NAVY, line_w=1.0)
        # connector to core
        add_line(s, conn_x, uc_y + uc_h / 2, uc_x, uc_y + uc_h / 2, color=NAVY, weight=0.8)
        # Title
        text_box(s, uc_x + Cm(0.4), uc_y + Cm(0.3), uc_w - Cm(0.8), Cm(0.9),
                 title,
                 font_size=15, bold=True, color=NAVY, font_name=FONT_DISPLAY)
        # Description with colored keyword
        rich_text_box(s, uc_x + Cm(0.4), uc_y + Cm(1.3), uc_w - Cm(0.8), Cm(1.0),
            [
                {"text": keyword, "size": 13, "color": key_color, "bold": True, "font": FONT_MONO},
                {"text": " " + desc, "size": 13, "color": GREY, "font": FONT_MONO},
            ])
        uc_y += uc_h + uc_spacing

    # Footer
    add_line(s, Cm(1.5), SH - Cm(1.6), SW - Cm(1.5), SH - Cm(1.6), color=GOLD, weight=0.5)
    text_box(s, Cm(1.5), SH - Cm(1.2), Cm(15), Cm(0.6),
             "FIRMAMENTO TECHNOLOGIES",
             font_size=9, bold=True, color=NAVY, font_name=FONT_DISPLAY)
    text_box(s, SW - Cm(16.5), SH - Cm(1.2), Cm(15), Cm(0.6),
             "H.A.L.E. Stratospheric Layer . 20 km AGL",
             font_size=9, color=GREY, font_name=FONT_MONO, align=PP_ALIGN.RIGHT)

# ============== SLIDE 3: BEYOND THE DRONE ==============
def slide_3_beyond():
    s = prs.slides.add_slide(BLANK)
    add_rect(s, 0, 0, SW, SH, fill=WHITE)

    # Title
    text_box(s, Cm(1.5), Cm(1.2), Cm(30), Cm(1.8),
             "Beyond the Drone",
             font_size=36, bold=True, color=NAVY, font_name=FONT_DISPLAY)
    text_box(s, Cm(1.5), Cm(3.1), Cm(30), Cm(0.9),
             "Three structural pillars defining the strategic positioning.",
             font_size=15, color=GREY, font_name=FONT_MONO)

    # Three columns
    cols = [
        ("Data\nSovereignty", LIGHT_BLUE,
         "European data residency. Consent management and sovereign cloud integration. Full GDPR + NIS2 compliance, AgID/PSN hosting for PA-grade data."),
        ("Dual-Use\nResilience", GOLD,
         "Support and backup to critical infrastructure. Persistent regional coverage for civil protection, disaster recovery and emergency telecom."),
        ("Seasonal\nPersistence", LIGHT_BLUE,
         "Architecture optimized for the 44 deg N energy balance, with continuous monitoring March-October and seasonal-only fallback as Plan A."),
    ]
    col_x = Cm(1.5)
    col_y = Cm(5.5)
    col_w = Cm(10)
    col_h = Cm(8)
    spacing = Cm(0.5)
    for title, color, desc in cols:
        # Title large color
        text_box(s, col_x, col_y, col_w, Cm(3),
                 title,
                 font_size=32, bold=True, color=color, font_name=FONT_DISPLAY,
                 line_spacing=1.05)
        # Description body
        text_box(s, col_x, col_y + Cm(3.5), col_w, col_h - Cm(3.5),
                 desc,
                 font_size=13, color=NAVY, font_name=FONT_MONO, line_spacing=1.4)
        col_x += col_w + spacing

    # Bottom box: pilot + numbers (Pentema)
    bottom_y = Cm(14)
    bottom_h = Cm(3.5)
    add_rect(s, Cm(1.5), bottom_y, SW - Cm(3), bottom_h, fill=NAVY)

    # Pilot info inside dark box
    rich_text_box(s, Cm(2), bottom_y + Cm(0.4), Cm(13), Cm(1),
        [
            {"text": "Pilot site . ", "size": 11, "color": GOLD, "font": FONT_MONO, "bold": True},
            {"text": "Pentema, Torriglia (Genova), Liguria, Italy . SNAI Inner Area",
             "size": 11, "color": WHITE, "font": FONT_MONO},
        ])
    rich_text_box(s, Cm(2), bottom_y + Cm(1.0), Cm(13), Cm(1),
        [
            {"text": "Network . ", "size": 11, "color": GOLD, "font": FONT_MONO, "bold": True},
            {"text": "10 Legacoop cooperatives . capofila Fabrica",
             "size": 11, "color": WHITE, "font": FONT_MONO},
        ])
    rich_text_box(s, Cm(2), bottom_y + Cm(1.6), Cm(13), Cm(1),
        [
            {"text": "Tender . ", "size": 11, "color": GOLD, "font": FONT_MONO, "bold": True},
            {"text": "Coopfond Cooding Prototypes (Legacoop)",
             "size": 11, "color": WHITE, "font": FONT_MONO},
        ])
    rich_text_box(s, Cm(2), bottom_y + Cm(2.2), Cm(13), Cm(1),
        [
            {"text": "Compliance . ", "size": 11, "color": GOLD, "font": FONT_MONO, "bold": True},
            {"text": "Italian PFTE art. 41 D.Lgs. 36/2023 + NASA SE Handbook Rev 2",
             "size": 11, "color": WHITE, "font": FONT_MONO},
        ])

    # Key numbers right side of bottom box
    nums_x = Cm(17)
    nums_w = Cm(13)
    rich_text_box(s, nums_x, bottom_y + Cm(0.4), nums_w, Cm(1.2),
        [
            {"text": "€700k – €2M ", "size": 18, "color": GOLD, "bold": True, "font": FONT_DISPLAY},
            {"text": "CapEx Y1", "size": 12, "color": WHITE, "font": FONT_MONO},
        ])
    rich_text_box(s, nums_x, bottom_y + Cm(1.4), nums_w, Cm(1.2),
        [
            {"text": "€1.18M/y ", "size": 18, "color": GOLD, "bold": True, "font": FONT_DISPLAY},
            {"text": "OpEx Y2 reconciled (incl. regulatory team)", "size": 12, "color": WHITE, "font": FONT_MONO},
        ])
    rich_text_box(s, nums_x, bottom_y + Cm(2.4), nums_w, Cm(1.2),
        [
            {"text": "€260k ", "size": 18, "color": GOLD, "bold": True, "font": FONT_DISPLAY},
            {"text": "Revenue Y1 baseline (range €220-300k)", "size": 12, "color": WHITE, "font": FONT_MONO},
        ])

    # Footer
    text_box(s, Cm(1.5), SH - Cm(1.0), Cm(15), Cm(0.5),
             "FIRMAMENTO TECHNOLOGIES SOCIETA' COOPERATIVA",
             font_size=8, bold=True, color=NAVY, font_name=FONT_DISPLAY)
    text_box(s, SW - Cm(16.5), SH - Cm(1.0), Cm(15), Cm(0.5),
             "P.IVA IT03038500991 . PEC firmamentotechnologies@pec.it",
             font_size=8, color=GREY, font_name=FONT_MONO, align=PP_ALIGN.RIGHT)

def build():
    slide_1_intro()
    slide_2_value()
    slide_3_beyond()
    prs.save(OUT_PPTX)
    print(f"PPTX generato: {OUT_PPTX}")
    print(f"Size: {os.path.getsize(OUT_PPTX)/1024:.1f} KB")

if __name__ == "__main__":
    build()
