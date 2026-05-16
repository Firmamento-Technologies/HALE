#!/usr/bin/env bash
# Download script for HALE Feasibility Study external references.
# Run this LOCALLY (from your laptop/desktop) — the Claude Code on-the-web
# runtime has a network policy that blocks Italian institutional domains.
#
# Usage:
#   ./download.sh           # download everything (40 files, T1+T2+T3)
#   ./download.sh tier1     # only T1 must-have (12 files)
#   ./download.sh tier2     # T1 + T2 (27 files)
#   ./download.sh tier3     # everything (40 files)
#
# Requirements:
#   - curl
#   - pdftotext (optional, for PDF -> Markdown conversion)
#     macOS:  brew install poppler
#     Ubuntu: sudo apt-get install -y poppler-utils

set -uo pipefail

# Selected tier (default: all)
TIER="${1:-tier3}"

# Realistic UA to avoid simple bot filters (these are public docs, no anti-bot here)
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

# Working dir = this script's directory
cd "$(dirname "$0")" || exit 1

# Init log
LOG="download.log"
: > "$LOG"
echo "Download started at $(date)" | tee -a "$LOG"
echo "Selected tier: $TIER" | tee -a "$LOG"
echo "---" | tee -a "$LOG"

# Counters
SUCCESS=0
FAIL=0
SKIP=0

# Helper: download a file
# Args: tier_required current_tier_filter dir outfile url
download() {
    local req_tier="$1"
    local dir="$2"
    local out="$3"
    local url="$4"

    # Tier filter
    case "$TIER" in
        tier1) [[ "$req_tier" == "T1" ]] || { SKIP=$((SKIP+1)); return 0; } ;;
        tier2) [[ "$req_tier" == "T1" || "$req_tier" == "T2" ]] || { SKIP=$((SKIP+1)); return 0; } ;;
        tier3) ;;  # all
        *)     echo "Unknown tier: $TIER. Use tier1/tier2/tier3"; exit 1 ;;
    esac

    mkdir -p "$dir"
    local path="$dir/$out"

    # Skip if already exists and non-empty
    if [[ -s "$path" ]]; then
        echo "[SKIP] $path (already exists, $(wc -c <"$path") bytes)" | tee -a "$LOG"
        SKIP=$((SKIP+1))
        return 0
    fi

    echo -n "[ $req_tier ] $out ... " | tee -a "$LOG"
    local http_code
    http_code=$(curl -sSL -A "$UA" \
        --connect-timeout 15 --max-time 120 \
        -o "$path" -w "%{http_code}" "$url" 2>>"$LOG" || echo "000")

    local size
    size=$(wc -c <"$path" 2>/dev/null || echo 0)

    if [[ "$http_code" == "200" && "$size" -gt 1024 ]]; then
        echo "OK ($size bytes, HTTP $http_code)" | tee -a "$LOG"
        SUCCESS=$((SUCCESS+1))
    else
        echo "FAIL (HTTP $http_code, $size bytes)" | tee -a "$LOG"
        FAIL=$((FAIL+1))
        # Remove failed file (likely empty or error page)
        rm -f "$path"
    fi
}

# Helper: convert PDF -> MD if pdftotext is available
convert_pdfs() {
    if ! command -v pdftotext >/dev/null 2>&1; then
        echo "[INFO] pdftotext not installed, skipping PDF->MD conversion" | tee -a "$LOG"
        echo "       install: brew install poppler  (macOS)" | tee -a "$LOG"
        echo "                sudo apt-get install -y poppler-utils  (Ubuntu)" | tee -a "$LOG"
        return 0
    fi

    echo "" | tee -a "$LOG"
    echo "=== Converting PDFs to Markdown ===" | tee -a "$LOG"
    local converted=0
    while IFS= read -r -d '' pdf; do
        local md="${pdf%.pdf}.md"
        if [[ -s "$md" ]]; then continue; fi
        if pdftotext -layout -nopgbrk "$pdf" "$md" 2>>"$LOG"; then
            echo "[CONV] $md ($(wc -l <"$md") lines)" | tee -a "$LOG"
            converted=$((converted+1))
        fi
    done < <(find . -type f -name "*.pdf" -print0)
    echo "Converted $converted PDFs to MD" | tee -a "$LOG"
}

# ===== Downloads =====

# 01 — Normativa Italia
download T1 "01-normativa-italia" "01-DLgs-36-2023-testo-integrale.htm" \
    "https://www.bosettiegatti.eu/info/norme/statali/2023_0036.htm"

download T1 "01-normativa-italia" "02-DLgs-36-2023-allegati.pdf" \
    "https://www.bosettiegatti.eu/public/2023_0036_Allegati.pdf"

download T1 "01-normativa-italia" "03-art-41-codiceappalti.htm" \
    "https://www.codiceappalti.it/DLGS_36_2023/Articolo_41__Livelli_e_contenuti_della_progettazione_/12647"

download T2 "01-normativa-italia" "04-allegato-I7-codiceappalti.htm" \
    "https://www.codiceappalti.it/DLGS_36_2023/Allegato_I_7_Contenuti_minimi_del_quadro_esigenziale,_del_documento_di_fattibilit%C3%A0_delle_alternative_progettuali,_del_documento_di_indirizzo_della_progettazione,_del_progetto_di_fattibilit%C3%A0_tecnica_ed_economica_e_del_progetto_esecutivo_/12883"

download T2 "01-normativa-italia" "05-biblus-PFTE-elaborati.htm" \
    "https://biblus.acca.it/progetto-fattibilita-tecnico-economica-elaborati/"

download T2 "01-normativa-italia" "06-PFTE-elenco-documenti-esempio.pdf" \
    "https://www.scuoleapertemilano.it/documents/20126/470457961/3_Elenco+documenti+PFTE_REV1.pdf"

# 02 — Fac-simili aerospaziali
download T1 "02-fac-simili-aero" "07-DTA-Grottaglie-studio-fattibilita-2020.pdf" \
    "https://www.dtascarl.org/wp-content/uploads/2024/05/GROTTAGLIE-studio-fattibilita.pdf"

download T1 "02-fac-simili-aero" "08-ENAC-AAM-Piano-Strategico-Nazionale.pdf" \
    "https://www.enac.gov.it/app/uploads/2024/04/01_Piano-Strategico-Nazionale-AAM_ENAC_web-en-GB.pdf"

download T1 "02-fac-simili-aero" "09-ENAC-AAM-Roadmap-Allegato1.pdf" \
    "https://www.enac.gov.it/app/uploads/2024/04/02_AAM-Italian-Ecosystem-%E2%80%93-Project-overview-and-Roadmap_web-1.pdf"

download T1 "02-fac-simili-aero" "10-ENAC-AAM-Business-Plan-Allegato2.pdf" \
    "https://www.enac.gov.it/app/uploads/2024/04/03_AAM-Business-Plan_web-1.pdf"

download T2 "02-fac-simili-aero" "11-MIMIT-prefattibilita-aero.pdf" \
    "https://www.mimit.gov.it/images/stories/recuperi/Impresa_internazionalizzazione/mincomes/DIREZGENE/Progetto_Marocco.pdf"

download T2 "02-fac-simili-aero" "12-aeropolis-analisi-costi-BP.pdf" \
    "http://www.aeropolis.it/workshop2014/workshop-24-5-2014/AnalisiCostiBusinessPlan24_05_14.pdf"

download T3 "02-fac-simili-aero" "13-camp-otranto-ABMT.pdf" \
    "https://camp-otranto.com/wp-content/uploads/2024/04/04-WEB-ABMT-IT.pdf"

download T3 "02-fac-simili-aero" "14-TE2C-sogaer-presentazione.pdf" \
    "https://www.sogaer.it/sites/default/files/legacy/images/stories/societa/consulenti/presentazione_TE2C.pdf"

download T3 "02-fac-simili-aero" "15-aeronautica-difesa-regolamento.pdf" \
    "https://www.aeronautica.difesa.it/wp-content/uploads/2024/02/Regolamento-amministrativo-ex-art.-15-D.Lgs_.-36.2023-POP-AMM-001_Ed.-20.pdf"

# 03 — ENAC / EASA / U-Space
download T1 "03-enac-easa-uspace" "16-Reg-UE-2019-947-operations-UAS.pdf" \
    "https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32019R0947"

download T2 "03-enac-easa-uspace" "17-Reg-UE-2019-945-design-UAS.pdf" \
    "https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32019R0945"

download T2 "03-enac-easa-uspace" "18-Reg-UE-2021-664-uspace-framework.pdf" \
    "https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32021R0664"

download T3 "03-enac-easa-uspace" "19-Reg-UE-2021-665-atm-ans-uspace.pdf" \
    "https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32021R0665"

download T3 "03-enac-easa-uspace" "20-Reg-UE-2021-666-sera-uspace.pdf" \
    "https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32021R0666"

download T1 "03-enac-easa-uspace" "21-ENAC-LG-2023-006-uspace.pdf" \
    "https://www.enac.gov.it/app/uploads/2023/12/LG-2023_006-UAS-Linee-Guida-U-Space.pdf"

# 04 — Standard tecnici
download T1 "04-standard-tecnici" "22-NASA-SE-Handbook-Rev2.pdf" \
    "https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf"

download T1 "04-standard-tecnici" "23-3GPP-TR-38811-NTN-channel-models.pdf" \
    "https://hscc.csie.ncu.edu.tw/38811.pdf"

download T2 "04-standard-tecnici" "24-3GPP-TR-38821-NTN-solutions.pdf" \
    "https://www.atis.org/wp-content/uploads/3gpp-documents/Rel16/ATIS.3GPP.38.821.V1600.pdf"

download T2 "04-standard-tecnici" "25-ITU-R-P618-rain-fade.pdf" \
    "https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.618-13-201712-S!!PDF-E.pdf"

download T3 "04-standard-tecnici" "26-ITU-R-P676-atmospheric-attenuation.pdf" \
    "https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.676-13-202208-S!!PDF-E.pdf"

# 05 — SNAI territoriale
download T1 "05-snai-territorial" "27-PSNAI-finale-2025.pdf" \
    "https://politichecoesione.governo.it/media/k0unx2d3/psnai_finale_30072025_clean_ministro.pdf"

download T2 "05-snai-territorial" "28-elenco-aree-snai-2014-2027.pdf" \
    "https://politichecoesione.governo.it/media/rpipea3z/elenco_aree_snai_14-20-e-21-27_20231012.pdf"

download T2 "05-snai-territorial" "29-snai-dossier-regionale-liguria.pdf" \
    "https://politichecoesione.governo.it/media/3171/snai-dossier-regionale-liguria.pdf"

download T3 "05-snai-territorial" "30-elenco-aree-snai-2021-2027-aggiornato.pdf" \
    "https://politichecoesione.governo.it/media/3111/elenco-aree-snai-2021-2027.pdf"

# 06 — Tesi accademiche
download T2 "06-tesi-accademiche" "31-polito-tesi-aeroportuale-28852.pdf" \
    "https://webthesis.biblio.polito.it/28852/1/tesi.pdf"

download T2 "06-tesi-accademiche" "32-polito-tesi-aerospace-14893.pdf" \
    "https://webthesis.biblio.polito.it/14893/1/tesi.pdf"

download T2 "06-tesi-accademiche" "33-polimi-tesi-flax-crashworthiness.pdf" \
    "https://www.politesi.polimi.it/retrieve/a81cb05b-7d29-616b-e053-1605fe0a889c/2020_07_Veneruso.pdf"

download T3 "06-tesi-accademiche" "34-unina-fedoa-1003-tesi-gravina.pdf" \
    "http://www.fedoa.unina.it/1003/1/Tesi_Gravina_Francesco.pdf"

download T3 "06-tesi-accademiche" "35-unibo-amslaurea-9491-tesi-cuoccio.pdf" \
    "https://amslaurea.unibo.it/id/eprint/9491/1/cuoccio_davide_tesi.pdf"

# 07 — Compositi fibra di lino
download T3 "07-compositi-lino" "36-univpm-tesi-flax-invecchiamento.htm" \
    "https://tesi.univpm.it/handle/20.500.12075/16766"

download T3 "07-compositi-lino" "37-compositesworld-biogear-flax.htm" \
    "https://www.compositesworld.com/articles/carbon-fiberflax-landing-gear-achieves-54-weight-reduction-via-tailored-layup-optimization"

# 08 — Mercato HAPS / competitor
download T3 "08-mercato-competitor" "38-MarkNtel-HAPS-summary.htm" \
    "https://www.marknteladvisors.com/research-library/high-altitude-pseudo-satellites-market.html"

download T3 "08-mercato-competitor" "39-airbus-zephyr-product-page.htm" \
    "https://www.airbus.com/en/products-services/defence/uas/zephyr"

download T3 "08-mercato-competitor" "40-skydweller-perpetual-flight.htm" \
    "https://www.skydweller.aero/news/skydweller-aero-successfully-demonstrates-perpetual-flight/"

# ===== Convert PDFs =====
convert_pdfs

# ===== Summary =====
echo "" | tee -a "$LOG"
echo "=== SUMMARY ===" | tee -a "$LOG"
echo "Success: $SUCCESS" | tee -a "$LOG"
echo "Failed:  $FAIL" | tee -a "$LOG"
echo "Skipped: $SKIP (filtered or already present)" | tee -a "$LOG"
echo "Log: $(pwd)/$LOG" | tee -a "$LOG"
echo "" | tee -a "$LOG"
echo "Next steps:" | tee -a "$LOG"
echo "  1. Review download.log for failures" | tee -a "$LOG"
echo "  2. Commit downloaded files:" | tee -a "$LOG"
echo "     git add -A && git commit -m 'Add reference sources' && git push" | tee -a "$LOG"
