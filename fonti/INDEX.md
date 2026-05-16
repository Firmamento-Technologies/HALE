# Fonti esterne scaricate — Inventario

**Data:** maggio 2026
**Cartella:** `fonti/` (root del repo) — i file sono stati scaricati manualmente dall'utente e convertiti in `.md` con `pdftotext -layout` + `pandoc` per i `.docx`.

**Stato copertura:** 10/12 must-have (Tier 1) + 3 bonus (Allegati ENAC U-Space) = **dati sufficienti per chiudere la maggior parte del debito di rigore critico** ed entrare nella stesura dello Studio di Fattibilità.

---

## 1. Inventario file scaricati

### 1.1 Normativa Italia
| File | MB | .md righe | Cosa contiene |
|---|---|---|---|
| `2023_0036.pdf` | 3.1 | 12.680 | **Testo integrale D.Lgs. 36/2023 Codice Contratti aggiornato al 28/12/2023 + Allegati** (inclusi Allegato I.7 con contenuti minimi PFTE/QE/DOCFAP/DIP). Copre fonti #1+#2+#3 del piano originale. |

### 1.2 Fac-simili aerospaziali italiani
| File | MB | .md righe | Cosa contiene |
|---|---|---|---|
| `GROTTAGLIE-studio-fattibilita.pdf` | 6.8 | 5.253 | **DTA Puglia 2020** — fac-simile principale aerospaziale. Indice navigabile, sezione conclusiva "opportunità – volontà – fattibilità". |
| `01_Piano-Strategico-Nazionale-AAM_ENAC_web-1.pdf` | 1.8 | – | ENAC Piano Strategico Nazionale AAM 2021-2030 |
| `02_AAM-Italian-Ecosystem-Roadmap_web-1.pdf` | 3.3 | – | ENAC Roadmap AAM 2021-2030 (Allegato 1 del Piano) |
| `03_AAM-Business-Plan_web-1.pdf` | 2.1 | 1.402 | **ENAC Business Plan AAM 2021-2030 (Allegato 2)** — template BP aeronautico italiano principale |

### 1.3 ENAC / EASA / U-Space
| File | MB | .md righe | Cosa contiene |
|---|---|---|---|
| `CELEX_32019R0947_IT_TXT.pdf` | 0.5 | – | **Reg. UE 2019/947** — Operations UAS (Open/Specific/Certified) — testo italiano |
| `LG-2023_006-UAS-Linee-Guida-U-Space.pdf` | 1.1 | – | **ENAC Linee Guida U-Space Ed.1** (dicembre 2023) — framework U-Space italiano |
| `ALLEGATO-1-Domanda-di-certificazione-USSP.docx` | 0.04 | – | 🎁 Bonus: Domanda certificazione USSP (U-space Service Provider) |
| `ALLEGATO-2-Comunicazione-del-fornitore-di-servizi-U-SPACE.docx` | 0.03 | – | 🎁 Bonus: Comunicazione fornitore U-Space |
| `ALLEGATO-3-Domanda-di-certificazione-CISP.docx` | 0.04 | – | 🎁 Bonus: Domanda certificazione CISP (Common Information Service Provider) |

### 1.4 Standard tecnici aerospaziali
| File | MB | .md righe | Cosa contiene |
|---|---|---|---|
| `NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).pdf` | 4.1 | 14.819 | **NASA Systems Engineering Handbook Rev 2** — metodologia di base del progetto, V-model, RTM, trade studies, gate reviews |
| `38811.pdf` | 4.7 | 7.815 | **3GPP TR 38.811** — NR-NTN channel models, scenari deployment HAPS — base per skill `link-budget-calculator` |

### 1.5 SNAI territoriale
| File | MB | .md righe | Cosa contiene |
|---|---|---|---|
| `psnai_finale_30072025_clean_ministro.pdf` | 1.9 | 6.415 | **PSNAI finale 2025** — Piano Strategico Nazionale Aree Interne. (Già presente anche in `Aree interne/`, duplicato non rimosso.) |

**Totale:** 13 file, ~34 MB convertiti, ~50.000+ righe markdown indicizzabili.

---

## 2. Confronto con piano originale (40 fonti pianificate)

### Tier 1 — Must-have (12) → **10 coperti (83%)** ✅

| # | Originale | Stato |
|---|---|---|
| 1 | D.Lgs. 36/2023 testo integrale (bosettiegatti.htm) | ✅ via PDF integrale `2023_0036.pdf` |
| 2 | D.Lgs. 36/2023 Allegati (bosettiegatti.pdf) | ✅ Inclusi nel PDF integrale (verificato presenza Allegato I.7) |
| 3 | art. 41 codiceappalti.htm | ✅ Incluso nel PDF integrale |
| 7 | **DTA Grottaglie** | ✅ Scaricato |
| 8 | **ENAC AAM Piano Strategico** | ✅ Scaricato (versione web 1, probabilmente IT) |
| 9 | **ENAC AAM Roadmap** | ✅ Scaricato |
| 10 | **ENAC AAM Business Plan** | ✅ Scaricato |
| 16 | Reg. UE 2019/947 | ✅ Scaricato (CELEX italiano) |
| 21 | ENAC LG-2023/006 U-Space | ✅ Scaricato |
| 22 | NASA SE Handbook Rev2 | ✅ Scaricato |
| 23 | 3GPP TR 38.811 | ✅ Scaricato |
| 27 | PSNAI finale 2025 | ✅ Scaricato |

**Bonus non pianificati ma utili:**
- 🎁 Allegati USSP/CISP della ENAC LG-2023/006 — essenziali per la fase regolatoria operativa

### Tier 2 — Should-have (15) → **0 coperti (0%)** ⏳
### Tier 3 — Nice-to-have (13) → **0 coperti (0%)** ⏳

---

## 3. Cosa manca ancora — round successivo

### T2 mancanti (priorità alta per triangulation)

| Documento | URL | Perché serve |
|---|---|---|
| MIMIT Progetto Marocco prefattibilità | https://www.mimit.gov.it/images/stories/recuperi/Impresa_internazionalizzazione/mincomes/DIREZGENE/Progetto_Marocco.pdf | Cap. 5+7 template MIMIT |
| Aeropolis Analisi Costi BP | http://www.aeropolis.it/workshop2014/workshop-24-5-2014/AnalisiCostiBusinessPlan24_05_14.pdf | Cap. 8 struttura costing aerospace |
| Reg. UE 2019/945 (Design UAS) | https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32019R0945 | Cap. 5 classi UAS C0-C6 |
| Reg. UE 2021/664 (U-Space framework) | https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32021R0664 | Cap. 5 base U-Space |
| 3GPP TR 38.821 (NTN solutions) | https://www.atis.org/wp-content/uploads/3gpp-documents/Rel16/ATIS.3GPP.38.821.V1600.pdf | Cap. 6.2 |
| ITU-R P.618 (rain fade) | https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.618-13-201712-S!!PDF-E.pdf | skill `link-budget-calculator` |
| Polimi tesi flax crashworthiness | https://www.politesi.polimi.it/retrieve/a81cb05b-7d29-616b-e053-1605fe0a889c/2020_07_Veneruso.pdf | Agente `aerodynamics-structures-engineer` |
| Politecnico Torino tesi aerospace | https://webthesis.biblio.polito.it/14893/1/tesi.pdf | Cap. 6 riferimenti accademici |

### T3 (nice-to-have, opzionali)

Vedi `riferimenti/fonti/README.md` per la lista completa.

### Fonti senza URL diretto (richiede ricerca manuale)

- **ENAC Regolamento Mezzi Aerei a Pilotaggio Remoto Ed.3** (2021) — su enac.gov.it, URL specifico cambia
- **EASA SORA AMC/GM** rev. corrente — su easa.europa.eu
- **EASA SC-Light-UAS** — su easa.europa.eu
- **ITU Radio Regulations 2024** — può richiedere registrazione ITU
- **AGCOM PNRF aggiornato** — pubblicato da MIMIT
- **Coopfond bando Cooding 2026** — non ancora pubblicato (verifica diretta Coopfond)

---

## 4. Impatto sul Debito di Rigore (audit-rigore-epistemico.md)

### DR ora coperti o parzialmente coperti
| DR-ID | Item | Stato |
|---|---|---|
| DR-001 | Pentema-Torriglia anagrafica | ⏳ Non coperto (richiede contatto Comune) |
| DR-002 | Coopfond Cooding bando attivo 2026 | ⏳ Non coperto (richiede contatto Coopfond) |
| DR-003 | TRL JOUAV CW-30E EASA-equivalent | ⏳ Non coperto (richiede quotation vendor + reference operatori) |
| DR-004 | ENAC SAIL stima per Pentema | ◐ **Parzialmente coperto** — la `LG-2023_006-UAS-Linee-Guida-U-Space.md` fornisce framework U-Space; per SAIL specifico Pentema serve pre-application meeting ENAC |
| DR-005 | AGCOM spettro HAPS Italia | ⏳ Non coperto (richiede consultazione AGCOM) |
| DR-006 | Garante Privacy posizione su sorveglianza HAPS | ⏳ Non coperto (richiede analisi precedenti dedicata) |
| DR-007 | Base rate aerospace startup IT | ⏳ Non coperto |
| DR-008 | EuroHAPS estensione civile / call EDF | ⏳ Non coperto (richiede engagement DG DEFIS) |
| DR-009 | IRIS² timeline e architettura stratosferica | ◐ **Parzialmente coperto** — Piano Strategico AAM ENAC dà contesto italiano AAM; per IRIS² serve engagement DG CNECT |
| DR-010 | CIRA willingness for civilian HALE | ⏳ Non coperto |
| DR-011 | Fibra di lino qualificazione aerospace primaria | ⏳ Non coperto (richiede peer-reviewed dedicata) |
| DR-012 | Mercato HAPS triangulation fonti non commerciali | ⏳ Non coperto (richiede AIAD/Eurospace/EUSPA reports) |
| DR-013 | Programmi HALE falliti — cause | ⏳ Non coperto (richiede ricerca dedicata) |
| DR-014 | Capital intensity HAPS perennial — stime indipendenti | ⏳ Non coperto |
| DR-015 | Posizione Leonardo/TAS verso Firmamento | ⏳ Non coperto |

### Nuovi possibili utilizzi dai download

Le 13 fonti scaricate **abilitano** stesura sostanziale di:

| Capitolo Studio | Fonte abilitante | Note |
|---|---|---|
| **Cap. 1** Inquadramento | PSNAI finale 2025 | Razionale pubblico SNAI consolidato |
| **Cap. 3** Requisiti + RTM | NASA SE Handbook §4 | Metodologia requirements + RTM template |
| **Cap. 5** Quadro normativo | D.Lgs.36/2023 + Reg.947 + LG U-Space + 3 Allegati USSP/CISP | **Capitolo regolatorio sostanzialmente completabile** |
| **Cap. 6** Analisi tecnica | NASA SE + 3GPP 38.811 + DTA Grottaglie sezioni tecniche | Struttura tecnica + link budget HAPS |
| **Cap. 7** Mercato + BP | ENAC AAM Piano + Roadmap + BP | **Template italiano BP aeronautico ufficiale disponibile** |
| **Cap. 8** Economico-finanziario | ENAC AAM Business Plan (struttura) + D.Lgs.36 Allegato I.7 (Quadro Economico) | Template QE conforme art.41 |
| **Cap. 9** Cronoprogramma | DTA Grottaglie + NASA SE Phase A-B-C | Esempio aerospace IT + framework NASA |

---

## 5. Riorganizzazione cartelle (suggerita)

I file sono attualmente in `fonti/` (root del repo, flat). Per allinearli alla struttura previsto nel piano (`riferimenti/fonti/01-normativa-italia/`, `02-fac-simili-aero/`, ecc.) servirebbe spostarli in categorie.

**Decisione:** lasciare per ora **flat** in `fonti/` come ha fatto l'utente, perché:
1. Sono 13 file, gestibili senza categorizzazione
2. Hanno nomi descrittivi
3. Spostarli ora rompe i path già in repo
4. Una categorizzazione si fa al meglio quando ci saranno tutti i 40 file

**Quando aggiungere altri T2/T3**, valutare riorganizzazione in sottocartelle.

---

## 6. Prossimi passi raccomandati

1. **Ora**: posso iniziare a **leggere e citare** i 13 documenti per chiudere il debito di rigore parziale e generare bozze sostanziali dei Cap. 3-5-6-7-8
2. **Round successivo download** (utente, ~30 min): scaricare i 8 T2 critici elencati in §3
3. **Engagement esterno** (utente, settimane): chiudere DR-001-002-003-005-006-008-010-015 con contatti diretti istituzioni
4. **Ricerca dedicata** (Claude su input utente, ore): chiudere DR-011 + DR-013 + DR-014 con triangulation peer-reviewed
