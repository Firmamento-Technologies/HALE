# Analisi dettagliata — Fac-simili italiani vs framework HALE

**Scopo:** confrontare la prassi italiana per studi di fattibilità ingegneristici aeronautici con il nostro framework attuale (NASA SE Handbook + strategia duale 6A/6B), identificare gap e definire la struttura finale dello Studio di Fattibilità HALE.

---

## 1. I tre quadri di riferimento

### A) Quadro regolatorio italiano per i lavori pubblici — **D.Lgs. 36/2023** (Codice dei Contratti)

- L'**art. 41** sancisce **due livelli** di progettazione (non più tre come nel D.Lgs. 50/2016):
  1. **Progetto di Fattibilità Tecnico-Economica (PFTE)**
  2. **Progetto Esecutivo (PE)**

- L'**Allegato I.7** definisce i **contenuti minimi** di una serie di documenti preliminari/intermedi:
  - **Quadro Esigenziale (QE)** — bisogni da soddisfare, vincoli, obiettivi
  - **Documento di Fattibilità delle Alternative Progettuali (DOCFAP)** — confronto alternative (≡ NASA SE trade study)
  - **Documento di Indirizzo della Progettazione (DIP)** — linee guida operative del RUP
  - **PFTE** — il documento di fattibilità vero e proprio
  - **Progetto Esecutivo (PE)** — esecuzione

**Elaborati tipici del PFTE** (sintesi della prassi):

| # | Elaborato | Equivalente NASA SE |
|---|---|---|
| 1 | Relazione generale | ConOps + Phase A summary |
| 2 | Relazioni specialistiche (geologica, idrogeologica, ambientale, sismica, archeologica, EIA prelim.) | Site Survey + Environmental Assessment |
| 3 | Elaborati grafici (planimetrie, sezioni, prospetti) | System Block Diagram + Layout |
| 4 | Calcoli preliminari (strutture, impianti) | Preliminary Design Analysis (Phase A) |
| 5 | Computo metrico estimativo | Cost Estimate (parametric/bottom-up) |
| 6 | Quadro economico | Total Project Cost Breakdown |
| 7 | Cronoprogramma | Master Schedule + Milestone Chart |
| 8 | Piano economico-finanziario (NPV, IRR, payback, ROI) | Life Cycle Cost Analysis |
| 9 | Piano di manutenzione preliminare | Integrated Logistic Support plan |
| 10 | Piano di sicurezza e coordinamento (PSC) | Safety Case prelim. |
| 11 | Documentazione fotografica / del contesto | Operating Environment Description |

→ Riferimento normativo: <https://www.codiceappalti.it/DLGS_36_2023/Articolo_41__Livelli_e_contenuti_della_progettazione_/12647> | <https://biblus.acca.it/progetto-fattibilita-tecnico-economica-elaborati/>

### B) Quadro settoriale aeronautico italiano — **ENAC**

- **Piano Strategico Nazionale AAM 2021-2030** + due allegati: **Roadmap** + **Business Plan**.
- Approccio: gap analysis su 3 livelli (regolatorio, tecnologico, infrastrutturale) → strategia integrata → allocation risorse pubbliche/private.
- **Stakeholder model**: cabina di regia ENAC + ENAV + MIT/MIMIT + soggetti industriali (Leonardo, Telespazio, ADR).
- Riferimento: <https://www.enac.gov.it/pubblicazioni/piano-strategico-nazionale-aam-2021-2030-per-lo-sviluppo-della-mobilita-aerea-avanzata-in-italia/>

→ **Applicabilità HALE:** il Business Plan AAM è il **template italiano più vicino** al nostro caso d'uso (nuovo sistema aereo, regulatory framework in evoluzione, ecosistema multi-stakeholder).

### C) Fac-simile aerospaziale di filiera — **DTA Puglia, Studio Grottaglie 2020**

- Studio commissionato da Regione Puglia per evento internazionale aerospazio a Grottaglie (sede del **GATB — Grottaglie Airport Test Bed**, riconosciuta come una delle più avanzate infrastrutture di test UAS/UAM in Europa).
- Autori: Acierno, U. Malusà (2020).
- Pattern: studio commissionato da PA regionale per validare un'iniziativa aerospaziale → struttura applicabile al nostro caso (PA regionale = **Regione Liguria**).

---

## 2. Struttura tipica ITA (sintesi del materiale ricevuto)

La struttura "ufficiale-like" italiana per fattibilità aeronautica converge su 7 capitoli + allegati:

1. **Sintesi esecutiva**
2. **Quadro normativo e regolamentare** (ENAC, EASA, AGCOM, ambientale)
3. **Analisi tecnica di fattibilità** (architettura, prestazioni, FMECA, FTA)
4. **Analisi economica e finanziaria** (CapEx, OpEx, NPV, IRR, payback, ROI)
5. **Analisi di mercato e business case**
6. **Cronoprogramma e approccio progettuale**
7. **Allegati tecnici** (disegni, computi, modelli di calcolo)

---

## 3. Confronto: struttura ITA vs framework NASA SE attuale

| Capitolo ITA art.41 / DTA / ENAC | Nostro Studio HALE (attuale) | Status |
|---|---|---|
| 1) Sintesi esecutiva | (presente nel Briefing) | ✓ |
| 2) Quadro normativo | Capitolo 8 (regolatorio) — da espandere su U-Space, HAPS framework, AGCOM | ◐ |
| 3) Analisi tecnica | Capitoli 3-5 (Requisiti, Architettura, Trade Study) — molto sviluppati | ✓ |
| 4) Analisi economica | Capitolo 10 (FinPlan) — da costruire integralmente | ✗ |
| 5) Mercato e business case | Capitolo 9 (Market) — da costruire | ✗ |
| 6) Cronoprogramma | Capitolo 6 (Roadmap M+0→M+48) — presente | ✓ |
| 7) Allegati (disegni, computi) | Capitolo 4.4 (ICD), CAD presenti, computi metrici da costruire | ◐ |
| **Aggiuntivi NASA SE** | RTM, V&V Plan, Risk Register, Gate Reviews | ✓ unico a noi |

**Legenda:** ✓ presente | ◐ parziale | ✗ assente

### Gap identificati nel nostro framework
1. **Mancano i documenti preliminari art.41**: Quadro Esigenziale, DOCFAP, DIP — formalmente non li abbiamo, anche se contenutisticamente ci sono nei nostri Cap.2 e Cap.5.
2. **Manca il Quadro Economico in formato Codice Contratti** (somme a disposizione, IVA, imprevisti, spese tecniche).
3. **Manca il Computo Metrico Estimativo** per le componenti infrastrutturali (ground segment, hangar, vertiporti).
4. **Manca Piano di Manutenzione preliminare** in formato art.41.
5. **Manca Piano di Sicurezza e Coordinamento (PSC)** per le operazioni di volo.
6. **Manca relazione VIA preliminare** (impatto ambientale operazioni UAV in aree protette).

### Punti di forza specifici del nostro framework (NASA SE)
1. **RTM** (Requirements Traceability Matrix) — più rigorosa di qualsiasi fac-simile italiano.
2. **Trade study formali** con AHP/Pugh — più strutturati del DOCFAP italiano.
3. **Gate-driven approach** — più rigoroso del cronoprogramma art.41 (che è solo temporale).
4. **Continuous risk management NASA NPR 8000.4** — più dettagliato di un PSC.

---

## 4. Struttura finale raccomandata — Studio Fattibilità HALE

**Approccio ibrido**: contenuti italiani art.41/ENAC, rigore metodologico NASA SE.

```
Studio di Fattibilità HALE — Indice
─────────────────────────────────────────────────────────────────
Volume 1 — STUDIO (formato art.41 + NASA SE)
  Cap. 0 — Sintesi Esecutiva (1-3 pp)
  Cap. 1 — Inquadramento del progetto e obiettivi (= QE Quadro Esigenziale)
  Cap. 2 — Contesto, stakeholder, obiettivi SMART
  Cap. 3 — Requisiti e criteri di successo (= NASA Needs + StRq + SyRq + RTM)
  Cap. 4 — Perimetro, scope, deliverable, interfacce (ICD)
  Cap. 5 — Quadro normativo e regolamentare (ENAC/EASA/AGCOM/HAPS/U-Space) (= cap.2 ITA)
  Cap. 6 — Analisi tecnica di fattibilità (= cap.3 ITA)
            6.1 Concept architettura 6A VTOL + 6B HALE
            6.2 Prestazioni preliminari (autonomia, payload, energia)
            6.3 Trade studies (= DOCFAP)
            6.4 Analisi rischio ingegneristico (FMECA + FTA)
            6.5 Infrastrutture (ground segment, vertiporti, hangar)
  Cap. 7 — Analisi di mercato e business case (= cap.5 ITA)
            7.1 Segmentazione domanda (B2G/B2B/B2C)
            7.2 TAM/SAM/SOM
            7.3 Competitor IT/EU/Global (Zephyr, Aalto, Aurora, Skydweller)
            7.4 Modello di servizio (DaaS/IaaS) e pricing
  Cap. 8 — Analisi economica e finanziaria (= cap.4 ITA)
            8.1 Quadro Economico CapEx (per fase 6A e 6B)
            8.2 OpEx per fase
            8.3 Piano economico-finanziario (NPV, IRR, payback, ROI)
            8.4 Sensitivity analysis
            8.5 Strategia finanziamenti (Cooding, PNRR, Horizon, EDF)
  Cap. 9 — Cronoprogramma e approccio progettuale (= cap.6 ITA)
            9.1 Master Schedule M+0→M+48
            9.2 Gate decisionali Go/No-Go (M+3, M+6, M+10, M+24, M+36)
            9.3 Verification & Validation Plan
  Cap.10 — Raccomandazione di gate (verdetto Go / Go Condizionato / No-Go / Hold)
  Cap.11 — Roadmap post-fattibilità (Fase 1 VTOL 6A, Fase 3 HALE 6B)

Volume 2 — ALLEGATI TECNICI (= cap.7 ITA)
  A.1 — RTM completa
  A.2 — Risk Register
  A.3 — Trade Study Reports
  A.4 — ICD Preliminare
  A.5 — V&V Plan
  A.6 — Schemi/disegni CAD del concept
  A.7 — Modelli di calcolo (energy balance, link budget, polare)
  A.8 — Bilanci di massa preliminari
  A.9 — Computo Metrico Estimativo (infrastrutture ground)
  A.10 — Piano di Manutenzione preliminare
  A.11 — Piano di Sicurezza Operativa (SORA / Safety Case)
  A.12 — Relazione VIA preliminare (se applicabile)
  A.13 — Documentazione fotografica del contesto (Pentema, aree pilota)

Volume 3 — RIFERIMENTI E BIBLIOGRAFIA
  R.1 — Bibliografia normativa (D.Lgs. 36/2023, Reg.UE 2019/947, EASA AMC, ENAC LRA)
  R.2 — Bibliografia tecnica (NASA SE Handbook, INCOSE, ECSS, DO-178C, etc.)
  R.3 — Fonti dati di mercato (Eurostat HAPS, Frost&Sullivan, ASD Eurospace)
  R.4 — Riferimenti cooperative Legacoop + SNAI
```

---

## 5. Implicazioni operative per il nostro lavoro

### Adeguamenti immediati al CLAUDE.md
- ✅ Aggiunto riferimento art.41 D.Lgs. 36/2023, ENAC, ANAC, AS/EN 9100
- ☐ Da fare: aggiungere riferimento al **Quadro Esigenziale** come deliverable formale del Cap.1

### Nuovi deliverable da pianificare
1. **Quadro Esigenziale (QE)** formale — circa M+2
2. **DOCFAP** formale (basato sui nostri Trade Studies) — circa M+4
3. **Quadro Economico** in formato Codice Contratti — circa M+7
4. **Computo Metrico Estimativo** per ground segment — circa M+8
5. **Piano di Manutenzione preliminare** — circa M+9
6. **Relazione VIA preliminare** — se applicabile, circa M+9

### Conformità da dichiarare
Per la presentazione a bandi pubblici italiani il documento deve dichiarare conformità a:
- **D.Lgs. 36/2023 art. 41** e **Allegato I.7**
- **AS/EN 9100** (Quality Management Aerospace) per le componenti di sviluppo prodotto
- **ISO 9001** per la gestione progetto
- **Reg. UE 2019/947 e 2019/945** per le operazioni UAS
- **NASA SE Handbook Rev2** per la metodologia ingegneristica (citazione non obbligatoria ma forte segnale di rigore)

### Stakeholder validazione esterna
Per dare valore di "ufficialità" al documento, considerare:
- **RINA** o **DNV** come ente terzo per validation indipendente dello studio
- **DTA Puglia / GATB** come partner di test bed per il Percorso 6A (Grottaglie ha l'unico test bed UAS BVLOS in IT)
- **CIRA** (Centro Italiano Ricerche Aerospaziali) come partner ricerca per il Percorso 6B
- **Politecnico di Torino / DIMEAS** come partner accademico per aerodinamica e strutture

---

## 6. Fonti citate

- D.Lgs. 36/2023 art. 41: [codiceappalti.it](https://www.codiceappalti.it/DLGS_36_2023/Articolo_41__Livelli_e_contenuti_della_progettazione_/12647) | [BibLus](https://biblus.acca.it/art-41-nuovo-codice-appalti/)
- Allegato I.7: [codiceappalti.it](https://www.codiceappalti.it/DLGS_36_2023/Allegato_I_7_Contenuti_minimi_del_quadro_esigenziale,_del_documento_di_fattibilit%C3%A0_delle_alternative_progettuali,_del_documento_di_indirizzo_della_progettazione,_del_progetto_di_fattibilit%C3%A0_tecnica_ed_economica_e_del_progetto_esecutivo_/12883)
- PFTE elaborati (esempio Scuole Aperte Milano): [PDF](https://www.scuoleapertemilano.it/documents/20126/470457961/3_Elenco+documenti+PFTE_REV1.pdf)
- ENAC Piano AAM 2021-2030: [enac.gov.it](https://www.enac.gov.it/pubblicazioni/piano-strategico-nazionale-aam-2021-2030-per-lo-sviluppo-della-mobilita-aerea-avanzata-in-italia/)
- ENAC AAM Business Plan: [PDF](https://www.enac.gov.it/app/uploads/2024/04/03_AAM-Business-Plan_web-1.pdf)
- DTA Grottaglie: [PDF](https://www.dtascarl.org/wp-content/uploads/2024/05/GROTTAGLIE-studio-fattibilita.pdf) | [GATB info](https://www.dtascarl.org/en/projects-and-initiatives/airport-test-beds-uas-uam/gatb-grottaglie-airport-test-bed-research-infrastructure/)
- MIMIT prefattibilità aero: [PDF](https://www.mimit.gov.it/images/stories/recuperi/Impresa_internazionalizzazione/mincomes/DIREZGENE/Progetto_Marocco.pdf)
- RINA Feasibility Studies: [rina.org](https://www.rina.org/it/technical-and-economic-feasibility-studies)
