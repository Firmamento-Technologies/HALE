"""
Mock-up template grafico Studio HALE Firmamento Technologies
Stile: Istituzionale sobrio
Genera 3 pagine PDF di validazione:
1. Frontespizio Vol. 1
2. Pagina interna tipo (Cap. 0 sezione)
3. Pagina con immagine HALE (Cap. 6 sezione)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Image,
                                 Table, TableStyle, PageBreak, KeepTogether)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ============== BRAND COLORS ==============
BRAND_NAVY = HexColor("#0a1a3d")
BRAND_GOLD = HexColor("#f0c95c")
BRAND_GOLD_DARK = HexColor("#c9a64a")
BRAND_GREY_LIGHT = HexColor("#f4f4f6")
BRAND_GREY_TEXT = HexColor("#3a3a3a")
BRAND_GREY_RULE = HexColor("#cfcfd4")

# ============== ASSET PATHS ==============
ASSETS_DIR = "/home/user/HALE/cad"
LOGO_PATH = os.path.join(ASSETS_DIR, "LogoFirmamento Technologies.png")
HALE_COVER_PATH = os.path.join(ASSETS_DIR, "HALE2.png")
OUT_PDF = "/home/user/HALE/studio-di-fattibilita/deliverables-template-mockup/TEMPLATE-MOCKUP-VALIDAZIONE.pdf"

# ============== PAGE FRAME ==============
PAGE_W, PAGE_H = A4
MARGIN_L = 2.2 * cm
MARGIN_R = 2.2 * cm
MARGIN_T = 2.5 * cm
MARGIN_B = 2.5 * cm

# ============== STYLES ==============
def get_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="CoverTitle", fontName="Times-Bold", fontSize=26, leading=32,
        textColor=BRAND_NAVY, alignment=TA_CENTER, spaceBefore=0, spaceAfter=12
    ))
    styles.add(ParagraphStyle(
        name="CoverSubtitle", fontName="Times-Italic", fontSize=15, leading=20,
        textColor=BRAND_GREY_TEXT, alignment=TA_CENTER, spaceBefore=6, spaceAfter=24
    ))
    styles.add(ParagraphStyle(
        name="CoverProponent", fontName="Times-Bold", fontSize=12, leading=16,
        textColor=BRAND_NAVY, alignment=TA_CENTER, spaceBefore=0, spaceAfter=4
    ))
    styles.add(ParagraphStyle(
        name="CoverMeta", fontName="Times-Roman", fontSize=10, leading=14,
        textColor=BRAND_GREY_TEXT, alignment=TA_CENTER, spaceBefore=2, spaceAfter=2
    ))
    styles.add(ParagraphStyle(
        name="SectionH1", fontName="Times-Bold", fontSize=18, leading=22,
        textColor=BRAND_NAVY, alignment=TA_LEFT, spaceBefore=10, spaceAfter=12,
        keepWithNext=1
    ))
    styles.add(ParagraphStyle(
        name="SectionH2", fontName="Times-Bold", fontSize=13, leading=17,
        textColor=BRAND_NAVY, alignment=TA_LEFT, spaceBefore=14, spaceAfter=6,
        keepWithNext=1
    ))
    styles.add(ParagraphStyle(
        name="SectionH3", fontName="Times-Bold", fontSize=11, leading=14,
        textColor=BRAND_GREY_TEXT, alignment=TA_LEFT, spaceBefore=10, spaceAfter=4,
        keepWithNext=1
    ))
    styles.add(ParagraphStyle(
        name="Body", fontName="Times-Roman", fontSize=10.5, leading=14.5,
        textColor=black, alignment=TA_JUSTIFY, spaceBefore=0, spaceAfter=8,
        firstLineIndent=0
    ))
    styles.add(ParagraphStyle(
        name="Caption", fontName="Times-Italic", fontSize=9, leading=11,
        textColor=BRAND_GREY_TEXT, alignment=TA_CENTER, spaceBefore=4, spaceAfter=12
    ))
    styles.add(ParagraphStyle(
        name="TableCell", fontName="Times-Roman", fontSize=9, leading=12,
        textColor=black, alignment=TA_LEFT
    ))
    styles.add(ParagraphStyle(
        name="TableCellBold", fontName="Times-Bold", fontSize=9, leading=12,
        textColor=BRAND_NAVY, alignment=TA_LEFT
    ))
    styles.add(ParagraphStyle(
        name="Quote", fontName="Times-Italic", fontSize=10, leading=14,
        textColor=BRAND_GREY_TEXT, alignment=TA_JUSTIFY,
        leftIndent=12, rightIndent=12, spaceBefore=6, spaceAfter=10,
        borderColor=BRAND_GOLD, borderPadding=8, borderWidth=0,
        backColor=HexColor("#fdf8e8")
    ))
    styles.add(ParagraphStyle(
        name="FooterText", fontName="Times-Italic", fontSize=8, leading=10,
        textColor=BRAND_GREY_TEXT, alignment=TA_CENTER
    ))
    return styles

STYLES = get_styles()

# ============== PAGE TEMPLATES ==============
def cover_decorations(canvas, doc):
    """Decorazioni grafiche per il frontespizio"""
    c = canvas
    c.saveState()
    # Bordo navy top
    c.setStrokeColor(BRAND_NAVY)
    c.setLineWidth(3)
    c.line(MARGIN_L, PAGE_H - 1.5 * cm, PAGE_W - MARGIN_R, PAGE_H - 1.5 * cm)
    # Sottobordo oro
    c.setStrokeColor(BRAND_GOLD)
    c.setLineWidth(1.2)
    c.line(MARGIN_L, PAGE_H - 1.65 * cm, PAGE_W - MARGIN_R, PAGE_H - 1.65 * cm)
    # Bordo navy bottom
    c.setStrokeColor(BRAND_NAVY)
    c.setLineWidth(3)
    c.line(MARGIN_L, 1.5 * cm, PAGE_W - MARGIN_R, 1.5 * cm)
    c.setStrokeColor(BRAND_GOLD)
    c.setLineWidth(1.2)
    c.line(MARGIN_L, 1.35 * cm, PAGE_W - MARGIN_R, 1.35 * cm)

    # Versione + data in footer
    c.setFont("Times-Italic", 8)
    c.setFillColor(BRAND_GREY_TEXT)
    c.drawCentredString(PAGE_W / 2, 0.85 * cm,
                        "Bozza M+11 (versione di lavoro), Maggio 2026 . Documento riservato . PEC firmamentotechnologies@pec.it")
    c.restoreState()

def inner_decorations(canvas, doc):
    """Header e footer pagine interne"""
    c = canvas
    c.saveState()
    # Header: linea sottile sotto logo+nome
    c.setStrokeColor(BRAND_NAVY)
    c.setLineWidth(0.6)
    c.line(MARGIN_L, PAGE_H - 1.85 * cm, PAGE_W - MARGIN_R, PAGE_H - 1.85 * cm)
    # Logo header (piccolo)
    try:
        c.drawImage(LOGO_PATH, MARGIN_L, PAGE_H - 1.75 * cm,
                    width=2.6 * cm, height=1.0 * cm,
                    preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    # Titolo Studio (header destro)
    c.setFont("Times-Italic", 8.5)
    c.setFillColor(BRAND_NAVY)
    c.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 1.3 * cm,
                      "Studio di Fattibilita HALE/VTOL")
    c.setFont("Times-Roman", 7.5)
    c.setFillColor(BRAND_GREY_TEXT)
    c.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 1.6 * cm,
                      "Volume 1 . Bozza M+11 . Maggio 2026")

    # Footer
    c.setStrokeColor(BRAND_GOLD)
    c.setLineWidth(0.8)
    c.line(MARGIN_L, 1.4 * cm, PAGE_W - MARGIN_R, 1.4 * cm)
    c.setFont("Times-Italic", 8)
    c.setFillColor(BRAND_GREY_TEXT)
    c.drawString(MARGIN_L, 1.05 * cm,
                 "Firmamento Technologies Societa Cooperativa . P.IVA IT03038500991")
    c.drawRightString(PAGE_W - MARGIN_R, 1.05 * cm,
                      "Pagina %d" % doc.page)
    c.drawString(MARGIN_L, 0.75 * cm,
                 "Via Brigata Liguria 105 R, 16121 Genova . REA 528629 . PEC firmamentotechnologies@pec.it")
    c.restoreState()

# ============== CUSTOM DOC ==============
class HALEDocTemplate(SimpleDocTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def afterFlowable(self, flowable):
        pass

# ============== BUILD STORY ==============
def build_story():
    story = []
    SS = STYLES

    # ============== PAGE 1 - FRONTESPIZIO ==============
    # Logo grande centrato
    if os.path.exists(LOGO_PATH):
        logo_img = Image(LOGO_PATH, width=8 * cm, height=4 * cm, kind='proportional')
        logo_img.hAlign = 'CENTER'
        story.append(Spacer(1, 1.2 * cm))
        story.append(logo_img)
        story.append(Spacer(1, 0.4 * cm))

    # Denominazione sociale
    story.append(Paragraph(
        "FIRMAMENTO TECHNOLOGIES SOCIETA' COOPERATIVA",
        SS["CoverProponent"]
    ))
    story.append(Paragraph(
        "Via Brigata Liguria 105 R, 16121 Genova (GE)",
        SS["CoverMeta"]
    ))
    story.append(Paragraph(
        "P.IVA / C.F. IT03038500991 . REA 528629 . PEC firmamentotechnologies@pec.it",
        SS["CoverMeta"]
    ))
    story.append(Spacer(1, 1.5 * cm))

    # Titolo studio
    story.append(Paragraph(
        "Studio di Fattibilita<br/>Tecnico-Economica",
        SS["CoverTitle"]
    ))
    story.append(Paragraph(
        "Piattaforma Aerea HALE / VTOL<br/>per le Aree Interne Italiane",
        SS["CoverSubtitle"]
    ))

    # Render copertina
    if os.path.exists(HALE_COVER_PATH):
        cover_img = Image(HALE_COVER_PATH, width=12 * cm, height=8 * cm, kind='proportional')
        cover_img.hAlign = 'CENTER'
        story.append(cover_img)
        story.append(Paragraph(
            "Velivolo HALE Firmamento Technologies, rendering CAD",
            SS["Caption"]
        ))

    story.append(Spacer(1, 0.4 * cm))

    # Box info volume
    info_data = [
        [Paragraph("<b>Volume</b>", SS["TableCell"]),
         Paragraph("1 di 3 . Studio (testuale)", SS["TableCell"])],
        [Paragraph("<b>Caso pilota</b>", SS["TableCell"]),
         Paragraph("Frazione di Pentema, Comune di Torriglia (GE)", SS["TableCell"])],
        [Paragraph("<b>Bando di riferimento</b>", SS["TableCell"]),
         Paragraph("Coopfond Cooding Prototypes (Legacoop)", SS["TableCell"])],
        [Paragraph("<b>Conformita normativa</b>", SS["TableCell"]),
         Paragraph("D.Lgs. 36/2023 art. 41 + Allegato I.7", SS["TableCell"])],
        [Paragraph("<b>Metodologia</b>", SS["TableCell"]),
         Paragraph("NASA SE Handbook Rev 2 (NASA/SP-2016-6105)", SS["TableCell"])],
        [Paragraph("<b>Versione</b>", SS["TableCell"]),
         Paragraph("Bozza M+11, Maggio 2026", SS["TableCell"])],
    ]
    info_table = Table(info_data, colWidths=[4.5 * cm, 11.5 * cm])
    info_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOX", (0, 0), (-1, -1), 0.6, BRAND_NAVY),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, BRAND_GREY_RULE),
        ("BACKGROUND", (0, 0), (0, -1), BRAND_GREY_LIGHT),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    info_table.hAlign = 'CENTER'
    story.append(info_table)

    # PAGE BREAK after cover
    story.append(PageBreak())

    # ============== PAGE 2 - PAGINA INTERNA TIPO (sezione testuale) ==============
    story.append(Paragraph("Capitolo 0. Sintesi Esecutiva", SS["SectionH1"]))
    story.append(Paragraph("0.1 Il progetto", SS["SectionH2"]))

    story.append(Paragraph(
        "Firmamento Technologies propone lo sviluppo e l'attivazione di una piattaforma aerea unmanned, "
        "operata come erogatore di servizi e non come venditore di velivoli, a beneficio delle Aree Interne "
        "italiane: territori a bassa densita demografica, orografia complessa, carenza di servizi essenziali "
        "e divario digitale strutturale.",
        SS["Body"]
    ))

    story.append(Paragraph(
        "Lo Studio e redatto in conformita all'art. 41 D.Lgs. 36/2023 e all'Allegato I.7 del Codice dei "
        "Contratti Pubblici, con metodologia derivata dal NASA Systems Engineering Handbook Rev 2 e dai "
        "template italiani autoritativi (ENAC AAM Business Plan 2021-2030, MIMIT prefattibilita aero, DTA "
        "Puglia Studio Grottaglie).",
        SS["Body"]
    ))

    story.append(Paragraph(
        "Il caso pilota e la frazione di Pentema, nel Comune di Torriglia (Genova), area SNAI riconosciuta "
        "nel ciclo 2021-2027 (Valli dell'Antola e del Tigullio), Regione Liguria: un laboratorio italiano "
        "per le politiche pubbliche delle Aree Interne. La rete di utenti-pilota e composta da dieci "
        "cooperative aderenti a Legacoop, con Fabrica come capofila.",
        SS["Body"]
    ))

    # Citazione/highlight box
    story.append(Paragraph(
        "Il verdetto consolidato dello Studio per il Percorso 6A e <b>HOLD CON PIANO REGOLATORIO RAFFORZATO</b> "
        "come scenario base (P 45-60%), con possibilita di GO CONDIZIONATO (P 5-15%) solo al verificarsi "
        "simultaneo delle cinque hard conditions al gate M+10-11.",
        SS["Quote"]
    ))

    story.append(Paragraph("0.2 Strategia duale", SS["SectionH2"]))

    story.append(Paragraph(
        "Il progetto adotta una strategia duale a riduzione del rischio, articolata su due percorsi "
        "paralleli. Il Percorso 6A copre il pilota VTOL di Pentema su orizzonte 0-12 mesi con piattaforma "
        "commerciale TRL 8-9 (baseline JOUAV CW-30E, Plan B Tekever AR3) e payload modulare EO+IR+telecom. "
        "Il Percorso 6B copre la fase R&D HALE stratosferico su orizzonte 24-48+ mesi con piattaforma solare "
        "ad apertura 25-30 m e quota operativa 18-21 km.",
        SS["Body"]
    ))

    # Tabella numeri chiave
    story.append(Paragraph("Numeri chiave del progetto", SS["SectionH3"]))

    nums_data = [
        ["Metrica", "Valore"],
        ["CapEx Y1 (6A)", "€700k - €2M"],
        ["OpEx Y2 run-rate (post Cap. 5 §5.17)", "€1.18M/anno (range €1.05-1.30M)"],
        ["Revenue Y1 baseline RECALIBRATED", "€260k centrale (range €220-300k)"],
        ["Break-even cumulato", "Y5-Y6"],
        ["NPV 10y scenario base", "+€3.5M"],
        ["IRR 10y scenario base", "12-18%"],
        ["Capital intensity Y10 small fleet", "€500M - €2B"],
    ]
    nums_table = Table(nums_data, colWidths=[10 * cm, 6 * cm])
    nums_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BACKGROUND", (0, 0), (-1, 0), BRAND_NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Times-Roman"),
        ("FONTSIZE", (0, 0), (-1, -1), 9.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, BRAND_GREY_LIGHT]),
        ("BOX", (0, 0), (-1, -1), 0.5, BRAND_NAVY),
        ("LINEBELOW", (0, 0), (-1, 0), 1.2, BRAND_GOLD),
    ]))
    story.append(nums_table)

    story.append(PageBreak())

    # ============== PAGE 3 - PAGINA CON IMMAGINE HALE ==============
    story.append(Paragraph("Capitolo 6. Analisi Tecnica di Fattibilita", SS["SectionH1"]))
    story.append(Paragraph("6.1 Concept architetturale", SS["SectionH2"]))

    story.append(Paragraph(
        "Il presente capitolo costituisce il cuore tecnico dello Studio di Fattibilita e copre architettura, "
        "prestazioni, analisi di rischio ingegneristico e infrastrutture per i due percorsi del progetto. "
        "Per ciascuno dei due percorsi, il capitolo definisce l'architettura di sistema preliminare, calcola "
        "le prestazioni stimate (autonomia, payload, energia, link budget), conduce le trade study chiave "
        "(DOCFAP ex art. 41) con scelte motivate, esegue l'analisi rischio ingegneristico (FMECA e FTA "
        "preliminare) e dimensiona le infrastrutture (ground segment, hangar, base operativa).",
        SS["Body"]
    ))

    # Immagine HALE
    if os.path.exists(HALE_COVER_PATH):
        hale_img = Image(HALE_COVER_PATH, width=14 * cm, height=9.3 * cm, kind='proportional')
        hale_img.hAlign = 'CENTER'
        story.append(hale_img)
        story.append(Paragraph(
            "Figura 6.1. Velivolo HALE Firmamento Technologies, configurazione T-tail high-AR con propulsione "
            "100% solare e pannelli fotovoltaici GaAs ad alto rendimento. Quota operativa target 18-21 km "
            "(FL590-690), apertura alare 25-30 m, MTOW 80-150 kg, endurance perennial estate Y3.",
            SS["Caption"]
        ))

    story.append(Paragraph("6.1.1 Caratteristiche chiave del Percorso 6B HALE", SS["SectionH3"]))

    tech_data = [
        ["Parametro", "Valore target", "Confidence"],
        ["Apertura alare", "25-30 m", "high"],
        ["MTOW", "80-150 kg", "medium"],
        ["Quota operativa", "18-21 km (FL590-690)", "high"],
        ["Endurance Y3 (estate, 44°N)", "≥ 30 giorni perennial", "medium"],
        ["Endurance Y5 (target)", "12 mesi continuativi", "low"],
        ["Payload", "5-10 kg", "high"],
        ["Propulsione", "Solare GaAs multi-junction", "high"],
        ["Storage energetico", "Batterie LiS pack 350 Wh/kg", "medium"],
    ]
    tech_table = Table(tech_data, colWidths=[6 * cm, 6 * cm, 4 * cm])
    tech_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BACKGROUND", (0, 0), (-1, 0), BRAND_NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Times-Roman"),
        ("FONTSIZE", (0, 0), (-1, -1), 9.5),
        ("ALIGN", (2, 0), (2, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, BRAND_GREY_LIGHT]),
        ("BOX", (0, 0), (-1, -1), 0.5, BRAND_NAVY),
        ("LINEBELOW", (0, 0), (-1, 0), 1.2, BRAND_GOLD),
    ]))
    story.append(tech_table)

    return story

# ============== MAIN ==============
def main():
    # Doc con primo template per cover, secondo per resto
    from reportlab.platypus.doctemplate import PageTemplate
    from reportlab.platypus.frames import Frame

    doc = HALEDocTemplate(
        OUT_PDF, pagesize=A4,
        leftMargin=MARGIN_L, rightMargin=MARGIN_R,
        topMargin=MARGIN_T, bottomMargin=MARGIN_B,
        title="Studio di Fattibilita HALE/VTOL - Mock-up Template",
        author="Firmamento Technologies",
        subject="Validazione template grafico"
    )

    cover_frame = Frame(MARGIN_L, MARGIN_B, PAGE_W - MARGIN_L - MARGIN_R,
                       PAGE_H - MARGIN_T - MARGIN_B, id='cover')
    inner_frame = Frame(MARGIN_L, MARGIN_B, PAGE_W - MARGIN_L - MARGIN_R,
                       PAGE_H - MARGIN_T - MARGIN_B, id='inner')

    cover_template = PageTemplate(id='cover', frames=[cover_frame],
                                  onPage=cover_decorations)
    inner_template = PageTemplate(id='inner', frames=[inner_frame],
                                  onPage=inner_decorations)
    doc.addPageTemplates([cover_template, inner_template])

    story = build_story()

    # Forza il passaggio da cover a inner dopo prima pagina
    from reportlab.platypus.doctemplate import NextPageTemplate
    new_story = []
    new_story.append(NextPageTemplate('cover'))
    # Inseriamo il marker prima del PageBreak della cover
    for i, item in enumerate(story):
        new_story.append(item)
        # Dopo il primo PageBreak, switch a inner template
        if isinstance(item, PageBreak) and i < 30:
            # Inserisci NextPageTemplate prima del PageBreak per le pagine successive
            pass

    # Approccio più semplice: passa esplicitamente
    final_story = []
    final_story.append(NextPageTemplate('cover'))
    for item in story:
        if isinstance(item, PageBreak):
            final_story.append(NextPageTemplate('inner'))
            final_story.append(item)
        else:
            final_story.append(item)

    doc.build(final_story)
    print(f"PDF generato: {OUT_PDF}")
    print(f"Size: {os.path.getsize(OUT_PDF)} bytes")

if __name__ == "__main__":
    main()
