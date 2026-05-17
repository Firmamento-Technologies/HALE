"""
Build PDF dei 3 volumi dello Studio di Fattibilita HALE/VTOL Firmamento Technologies.

Pipeline:
1. Genera cover HTML per ciascun volume
2. Converte ogni file markdown -> HTML via pandoc (preserva GFM tables)
3. Combina HTML in un singolo documento per volume
4. WeasyPrint -> PDF con CSS stile mock-up validato

Output: 3 PDF in deliverables-FINAL/
- Volume-1-Studio.pdf
- Volume-2-Allegati.pdf
- Volume-3-Riferimenti.pdf
"""

import os
import subprocess
import re
import glob
from pathlib import Path
from weasyprint import HTML, CSS

BASE = "/home/user/HALE/studio-di-fattibilita"
ASSETS = "/home/user/HALE/cad"
OUT = os.path.join(BASE, "deliverables-FINAL")
LOGO = os.path.join(ASSETS, "LogoFirmamento Technologies.png")
HALE_RENDER = os.path.join(ASSETS, "HALE2.png")

# ============== CSS COMUNE ==============
CSS_TEMPLATE = """
@page {
    size: A4;
    margin: 2.5cm 2.2cm 2.5cm 2.2cm;
    @top-left {
        content: element(headerLeft);
    }
    @top-right {
        content: element(headerRight);
    }
    @bottom-left {
        content: "Firmamento Technologies Societa Cooperativa . P.IVA IT03038500991";
        font-family: "Times New Roman", serif;
        font-size: 8pt;
        font-style: italic;
        color: #3a3a3a;
        vertical-align: top;
        padding-top: 6pt;
        border-top: 0.8pt solid #f0c95c;
        width: 100%;
    }
    @bottom-center {
        content: counter(page);
        font-family: "Times New Roman", serif;
        font-size: 9pt;
        color: #0a1a3d;
        font-weight: bold;
        vertical-align: top;
        padding-top: 6pt;
    }
    @bottom-right {
        content: "Volume __VOL__ . Bozza M+11 . Maggio 2026";
        font-family: "Times New Roman", serif;
        font-size: 8pt;
        font-style: italic;
        color: #3a3a3a;
        vertical-align: top;
        padding-top: 6pt;
        border-top: 0.8pt solid #f0c95c;
        width: 100%;
    }
}
@page :first {
    margin: 0;
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-left { content: none; }
    @bottom-center { content: none; }
    @bottom-right { content: none; }
}
@page cover {
    margin: 0;
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-left { content: none; }
    @bottom-center { content: none; }
    @bottom-right { content: none; }
}
html, body {
    font-family: "Times New Roman", "Liberation Serif", serif;
    font-size: 10.5pt;
    line-height: 1.45;
    color: #1a1a1a;
    margin: 0;
    padding: 0;
}
#headerLeft {
    position: running(headerLeft);
    font-family: "Times New Roman", serif;
    font-size: 8.5pt;
    color: #0a1a3d;
}
#headerLeft img {
    height: 0.95cm;
    vertical-align: middle;
}
#headerRight {
    position: running(headerRight);
    font-family: "Times New Roman", serif;
    font-size: 8.5pt;
    color: #0a1a3d;
    font-style: italic;
    text-align: right;
}
/* Cover page */
.cover {
    page: cover;
    page-break-after: always;
    padding: 2cm 2.2cm;
    height: 297mm;
    box-sizing: border-box;
    position: relative;
}
.cover .border-top {
    border-top: 3pt solid #0a1a3d;
    border-bottom: 1.2pt solid #f0c95c;
    height: 4pt;
    margin-bottom: 1.5cm;
}
.cover .border-bottom {
    border-top: 1.2pt solid #f0c95c;
    border-bottom: 3pt solid #0a1a3d;
    height: 4pt;
    position: absolute;
    bottom: 2cm;
    left: 2.2cm;
    right: 2.2cm;
}
.cover .logo {
    text-align: center;
    margin-bottom: 0.5cm;
}
.cover .logo img {
    width: 9cm;
    max-width: 100%;
}
.cover .denom {
    text-align: center;
    font-family: "Times New Roman", serif;
    font-weight: bold;
    font-size: 12pt;
    color: #0a1a3d;
    margin: 0.2cm 0;
}
.cover .meta {
    text-align: center;
    font-family: "Times New Roman", serif;
    font-size: 9.5pt;
    color: #3a3a3a;
    margin: 0.1cm 0;
}
.cover .title {
    text-align: center;
    font-family: "Times New Roman", serif;
    font-weight: bold;
    font-size: 27pt;
    line-height: 1.2;
    color: #0a1a3d;
    margin: 1.5cm 0 0.4cm 0;
}
.cover .subtitle {
    text-align: center;
    font-family: "Times New Roman", serif;
    font-style: italic;
    font-size: 15pt;
    color: #3a3a3a;
    margin: 0.4cm 0 1cm 0;
}
.cover .render {
    text-align: center;
    margin: 0.5cm 0;
}
.cover .render img {
    max-width: 13cm;
    max-height: 9cm;
}
.cover .caption {
    text-align: center;
    font-family: "Times New Roman", serif;
    font-style: italic;
    font-size: 9pt;
    color: #3a3a3a;
    margin-top: 0.3cm;
}
.cover .info-table {
    margin: 0.7cm auto 0 auto;
    width: 90%;
    border: 0.6pt solid #0a1a3d;
    border-collapse: collapse;
    font-family: "Times New Roman", serif;
    font-size: 9.5pt;
}
.cover .info-table td {
    padding: 5pt 8pt;
    border-bottom: 0.3pt solid #cfcfd4;
    vertical-align: top;
}
.cover .info-table td:first-child {
    background: #f4f4f6;
    font-weight: bold;
    color: #0a1a3d;
    width: 30%;
}
.cover .footnote {
    text-align: center;
    font-family: "Times New Roman", serif;
    font-style: italic;
    font-size: 8pt;
    color: #3a3a3a;
    position: absolute;
    bottom: 0.8cm;
    left: 0;
    right: 0;
}
/* Body styles */
h1 {
    font-family: "Times New Roman", serif;
    font-size: 19pt;
    color: #0a1a3d;
    border-bottom: 2pt solid #0a1a3d;
    padding-bottom: 6pt;
    margin: 1.2cm 0 0.6cm 0;
    page-break-before: always;
    page-break-after: avoid;
}
h1:first-of-type {
    page-break-before: avoid;
}
h2 {
    font-family: "Times New Roman", serif;
    font-size: 14pt;
    color: #0a1a3d;
    margin: 0.8cm 0 0.3cm 0;
    padding-bottom: 2pt;
    border-bottom: 0.5pt solid #f0c95c;
    page-break-after: avoid;
}
h3 {
    font-family: "Times New Roman", serif;
    font-size: 12pt;
    color: #0a1a3d;
    margin: 0.6cm 0 0.2cm 0;
    page-break-after: avoid;
}
h4 {
    font-family: "Times New Roman", serif;
    font-size: 11pt;
    color: #3a3a3a;
    font-style: italic;
    margin: 0.4cm 0 0.15cm 0;
    page-break-after: avoid;
}
h5, h6 {
    font-family: "Times New Roman", serif;
    font-size: 10.5pt;
    color: #3a3a3a;
    font-weight: bold;
    margin: 0.3cm 0 0.1cm 0;
    page-break-after: avoid;
}
p {
    text-align: justify;
    margin: 0 0 0.3cm 0;
    orphans: 3;
    widows: 3;
}
ul, ol {
    margin: 0.2cm 0 0.3cm 0.5cm;
    padding-left: 0.5cm;
}
li {
    margin-bottom: 0.1cm;
}
blockquote {
    background: #fdf8e8;
    border-left: 3pt solid #f0c95c;
    padding: 6pt 10pt;
    margin: 0.4cm 0;
    font-style: italic;
    color: #3a3a3a;
}
code, pre {
    font-family: "Courier New", monospace;
    font-size: 9pt;
    background: #f4f4f6;
    padding: 1pt 3pt;
}
pre {
    padding: 6pt 8pt;
    border-left: 2pt solid #cfcfd4;
    page-break-inside: avoid;
    white-space: pre-wrap;
    word-wrap: break-word;
}
table {
    border-collapse: collapse;
    margin: 0.4cm auto;
    font-size: 9pt;
    width: 100%;
    page-break-inside: avoid;
}
th {
    background: #0a1a3d;
    color: white;
    font-family: "Times New Roman", serif;
    font-weight: bold;
    padding: 5pt 6pt;
    text-align: left;
    border: 0.4pt solid #0a1a3d;
    border-bottom: 1.5pt solid #f0c95c;
}
td {
    padding: 4pt 6pt;
    border: 0.3pt solid #cfcfd4;
    vertical-align: top;
}
tr:nth-child(even) td {
    background: #f4f4f6;
}
strong, b {
    color: #0a1a3d;
}
em, i {
    color: #3a3a3a;
}
hr {
    border: none;
    border-top: 0.5pt solid #cfcfd4;
    margin: 0.5cm 0;
}
a {
    color: #0a1a3d;
    text-decoration: none;
    border-bottom: 0.5pt dotted #0a1a3d;
}
/* Chapter divider */
.chapter-divider {
    page-break-before: always;
}
.toc {
    page-break-after: always;
}
.toc h1 {
    page-break-before: avoid;
    text-align: center;
    border: none;
    margin-bottom: 1cm;
}
.toc-entry {
    display: flex;
    justify-content: space-between;
    margin: 4pt 0;
    font-family: "Times New Roman", serif;
}
.toc-entry .title-side {
    flex: 1;
}
.toc-entry .page-side {
    font-weight: bold;
    color: #0a1a3d;
}
"""

# ============== HEADER/FOOTER COMUNI ==============
def make_running_header():
    return f"""
    <div id="headerLeft">
        <img src="file://{LOGO}" alt="Firmamento"/>
    </div>
    <div id="headerRight">
        Studio di Fattibilita HALE/VTOL
    </div>
    """

# ============== COVER HTML PER VOLUME ==============
COVER_TEMPLATES = {
    1: {
        "subtitle": "Volume 1, Studio (testuale)",
        "title": "Studio di Fattibilita<br/>Tecnico-Economica",
        "subtitle2": "Piattaforma Aerea HALE / VTOL<br/>per le Aree Interne Italiane",
        "volume_label": "1 di 3, Studio (testuale), 11 capitoli",
    },
    2: {
        "subtitle": "Volume 2, Allegati Tecnici",
        "title": "Allegati Tecnici",
        "subtitle2": "RTM, Risk Register, ICD, V&amp;V Plan,<br/>Computo Metrico, Safety Case SORA, VIA",
        "volume_label": "2 di 3, Allegati tecnici, 13 allegati + refinement v1.5/v2.0",
    },
    3: {
        "subtitle": "Volume 3, Riferimenti",
        "title": "Riferimenti<br/>Bibliografici",
        "subtitle2": "Normativa UE+IT, bibliografia tecnica NASA SE/INCOSE/DO,<br/>fonti mercato, documenti SNAI, studi accademici",
        "volume_label": "3 di 3, Riferimenti bibliografici, 5 sezioni R + README",
    },
}

def make_cover(volume_num):
    cfg = COVER_TEMPLATES[volume_num]
    return f"""
    <div class="cover">
        <div class="border-top"></div>
        <div class="logo">
            <img src="file://{LOGO}" alt="Logo Firmamento Technologies"/>
        </div>
        <p class="denom">FIRMAMENTO TECHNOLOGIES SOCIETA' COOPERATIVA</p>
        <p class="meta">Via Brigata Liguria 105 R, 16121 Genova (GE)</p>
        <p class="meta">P.IVA / C.F. IT03038500991 . REA 528629 . PEC firmamentotechnologies@pec.it</p>
        <h1 class="title">{cfg['title']}</h1>
        <p class="subtitle">{cfg['subtitle2']}</p>
        <div class="render">
            <img src="file://{HALE_RENDER}" alt="HALE Firmamento"/>
            <p class="caption">Velivolo HALE Firmamento Technologies, rendering CAD configurazione T-tail high-AR</p>
        </div>
        <table class="info-table">
            <tr><td>Volume</td><td>{cfg['volume_label']}</td></tr>
            <tr><td>Caso pilota</td><td>Frazione di Pentema, Comune di Torriglia (GE), area SNAI Valli Antola-Tigullio</td></tr>
            <tr><td>Bando di riferimento</td><td>Coopfond Cooding Prototypes (Legacoop)</td></tr>
            <tr><td>Rete cooperative</td><td>10 cooperative aderenti Legacoop, capofila Fabrica</td></tr>
            <tr><td>Conformita normativa</td><td>D.Lgs. 36/2023 art. 41 + Allegato I.7</td></tr>
            <tr><td>Metodologia</td><td>NASA SE Handbook Rev 2 (NASA/SP-2016-6105)</td></tr>
            <tr><td>Versione documento</td><td>Bozza M+11, Maggio 2026</td></tr>
        </table>
        <p class="footnote">Documento riservato . PEC firmamentotechnologies@pec.it . Bozza M+11 Maggio 2026</p>
        <div class="border-bottom"></div>
    </div>
    """

# ============== CONVERSIONE MARKDOWN -> HTML ==============
def md_to_html(md_path):
    """Convert markdown to HTML body via pandoc."""
    result = subprocess.run(
        ["pandoc", "-f", "gfm+pipe_tables+raw_html",
         "-t", "html5", "--wrap=preserve",
         "--no-highlight",
         md_path],
        capture_output=True, text=True, timeout=60
    )
    if result.returncode != 0:
        print(f"  WARN pandoc on {md_path}: {result.stderr[:200]}")
        return ""
    return result.stdout

def post_process_html(html):
    """Pulizia HTML post-pandoc."""
    # Rimuovi link interni rotti (riferimenti md, riferimenti cap)
    html = re.sub(r'<a href="[^"]*\.md[^"]*">([^<]*)</a>', r'\1', html)
    # Pulisci link a #section anchors
    html = re.sub(r'<a href="#[^"]*">([^<]*)</a>', r'\1', html)
    # Footnote refs di pandoc rimossi (li lasciamo come testo)
    return html

# ============== VOLUME 1 ==============
def volume1_files():
    """File del Volume 1 (capitoli)."""
    files = sorted(glob.glob(os.path.join(BASE, "cap-*.md")))
    return files

# ============== VOLUME 2 ==============
def volume2_files():
    """File del Volume 2 (allegati). Ordine logico."""
    base = os.path.join(BASE, "allegati")
    order = [
        ("A1-RTM/A1-RTM-REPORT-v1.5.md", "Allegato A.1 RTM v1.5"),
        ("A2-Risk-Register/A2-RISK-REGISTER-REPORT-v1.5.md", "Allegato A.2 Risk Register v1.5"),
        ("A3-Trade-Studies/A3-DOCFAP-Trade-Studies.md", "Allegato A.3 DOCFAP Trade Studies"),
        ("A4-ICD/A4-ICD-DETAILED-v2.0.md", "Allegato A.4 ICD Detailed v2.0"),
        ("A5-VV-Plan/A5-VV-PLAN-v1.0.md", "Allegato A.5 V&V Plan v1.0"),
        ("A7-Link-Budget/A7-LINK-BUDGET-REPORT.md", "Allegato A.7 Link Budget"),
        ("energy-balance/ENERGY-BALANCE-HALE-44N-REPORT.md", "Allegato A.7b Energy Balance HALE 44 deg N"),
        ("A8-Bilanci-Massa/A8-Bilanci-Massa-Preliminari.md", "Allegato A.8 Bilanci Massa Preliminari"),
        ("A9-Computo-Metrico/A9-Computo-Metrico-Estimativo-v1.5-WBS3.md", "Allegato A.9 Computo Metrico WBS 3"),
        ("A10-Piano-Manutenzione/A10-Piano-Manutenzione-Operativo-v1.5.md", "Allegato A.10 Piano Manutenzione Operativo v1.5"),
        ("A11-Safety-Case-SORA/A11-PSC-SORA-Safety-Case-COMPLETE-v2.0.md", "Allegato A.11 SORA Safety Case v2.0"),
        ("A12-VIA-preliminare/A12-Relazione-VIA-Preliminare-COMPLETE-v2.0.md", "Allegato A.12 VIA Preliminare v2.0"),
        ("A13-Documentazione-Fotografica/A13-Documentazione-Fotografica.md", "Allegato A.13 Documentazione Fotografica"),
        ("vendor-rfq/RFQ-TEMPLATE-VTOL-FIRMAMENTO.md", "RFQ Template VTOL"),
        ("vendor-rfq/VENDOR-QUOTATION-ANALYSIS-JOUAV-TEKEVER.md", "Analisi Vendor Quotation JOUAV vs Tekever"),
    ]
    return [(os.path.join(base, p), title) for p, title in order]

# ============== VOLUME 3 ==============
def volume3_files():
    base = os.path.join(BASE, "volume-3-riferimenti")
    order = [
        ("R1-bibliografia-normativa.md", "R.1 Bibliografia Normativa"),
        ("R2-bibliografia-tecnica.md", "R.2 Bibliografia Tecnica"),
        ("R3-fonti-mercato-competitor.md", "R.3 Fonti di Mercato e Competitor"),
        ("R4-documenti-SNAI-territoriali.md", "R.4 Documenti SNAI e Territoriali"),
        ("R5-studi-accademici.md", "R.5 Studi Accademici"),
    ]
    return [(os.path.join(base, p), title) for p, title in order]

# ============== BUILD VOLUME ==============
def build_volume(volume_num, files, out_pdf):
    print(f"\n=== Building Volume {volume_num} ({len(files)} files) ===")
    cover = make_cover(volume_num)
    headers = make_running_header()

    body_parts = []
    for f in files:
        if isinstance(f, tuple):
            path, title = f
        else:
            path = f
            title = None
        if not os.path.exists(path):
            print(f"  SKIP missing: {path}")
            continue
        print(f"  Pandoc: {os.path.basename(path)}")
        html = md_to_html(path)
        html = post_process_html(html)
        # Wrap in chapter-divider div
        body_parts.append(f'<div class="chapter-divider">{html}</div>')

    body_html = "\n".join(body_parts)
    full_html = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8"/>
<title>Studio di Fattibilita HALE/VTOL Volume {volume_num}</title>
</head>
<body>
{headers}
{cover}
{body_html}
</body>
</html>"""

    css_text = CSS_TEMPLATE.replace("__VOL__", str(volume_num))
    css = CSS(string=css_text)

    print(f"  Generating PDF...")
    HTML(string=full_html, base_url=BASE).write_pdf(out_pdf, stylesheets=[css])
    size_mb = os.path.getsize(out_pdf) / 1024 / 1024
    print(f"  -> {out_pdf} ({size_mb:.2f} MB)")

def main():
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "all"
    if target in ("1", "all"):
        build_volume(1, volume1_files(),
                     os.path.join(OUT, "Volume-1-Studio.pdf"))
    if target in ("2", "all"):
        build_volume(2, volume2_files(),
                     os.path.join(OUT, "Volume-2-Allegati.pdf"))
    if target in ("3", "all"):
        build_volume(3, volume3_files(),
                     os.path.join(OUT, "Volume-3-Riferimenti.pdf"))

if __name__ == "__main__":
    main()
