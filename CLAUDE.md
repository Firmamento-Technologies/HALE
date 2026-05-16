# Progetto HALE — Firmamento Technologies

Repository di lavoro per lo **Studio di Fattibilità** di una piattaforma aerea senza pilota per le Aree Interne italiane, con focus sulla Regione Liguria.

## Contesto

- **Soggetto proponente:** Firmamento Technologies
- **Bando di riferimento:** Cooding Prototypes (Coopfond / Legacoop)
- **Rete cooperative pilota:** 10 cooperative aderenti a Legacoop (capofila: Fabrica)
- **Stakeholder istituzionali:** Regione Liguria, ENAC, AGCOM, Protezione Civile
- **Caso studio pilota:** frazione di Pentema (Comune di Torriglia, GE)
- **Metodologia:** NASA Systems Engineering Handbook (gate-driven, risk-informed) **incrociata con la prassi italiana**:
  - Codice dei Contratti Pubblici, **art. 41 D.Lgs. 36/2023** (progetto di fattibilità tecnico-economica)
  - Linee guida **ANAC** per studi di fattibilità
  - Fac-simile **DTA Puglia — Studio di Fattibilità Grottaglie** (template di riferimento aerospaziale)
  - **ENAC AAM Business Plan** (template per nuovi sistemi aeronautici)
  - Studi **MIMIT** di prefattibilità aeronautica
  - Conformità ENAC/EASA, **AS/EN 9100**, ISO 9001

## Strategia duale

| Percorso | Tecnologia | Orizzonte | Budget | Rischio |
|---|---|---|---|---|
| **6A — Pilota VTOL** | Piattaforma commerciale TRL 8-9 (es. JOUAV CW-30E) | 0-12 mesi | €600k–900k | Basso (Go Condizionato) |
| **6B — HALE Stratosferico** | UAV solare HALE a 20 km di quota | 24-48+ mesi | €5.5M–11M (R&D) | Alto (Hold / Go Condizionato Estremo) |

## Layout della repository

```
HALE/
├── Progetto concettuale struttura HALE.{docx,md}   # Concept aerodinamico (high AR, T-tail, fibra di lino)
├── Aree interne/          # Documenti SNAI/PSNAI, dossier territoriali, rapporto Liguria
├── bando/                 # Documenti bando Cooding (progetto, business plan, piano economico, lettere)
├── da revisionare/        # Studio di Fattibilità in lavorazione + briefing + relazione comparativa
├── cad/                   # File CAD del velivolo
└── .claude/               # Agenti esperti e skill operative — vedi .claude/README.md
```

## Lingua

Tutta la documentazione del progetto e i prompt degli agenti sono in **italiano**. Terminologia tecnica internazionale (NASA SE, EASA, ITU, ICAO) può restare in inglese quando standard.

## Struttura canonica dello Studio di Fattibilità

Approccio **ibrido**: contenuti italiani **art. 41 D.Lgs. 36/2023** + rigore metodologico **NASA SE Handbook**. Vedi `riferimenti/analisi-fac-simili-IT.md` per il dettaglio e la mappatura completa.

Lo Studio è strutturato in **3 volumi**:

### Volume 1 — Studio (testuale)
- Cap. 0 Sintesi Esecutiva
- Cap. 1 Inquadramento e obiettivi (= Quadro Esigenziale ex art.41)
- Cap. 2 Contesto, stakeholder, obiettivi SMART
- Cap. 3 Requisiti e RTM (NASA needs/StRq/SyRq)
- Cap. 4 Perimetro, scope, deliverable, ICD
- Cap. 5 Quadro normativo (ENAC/EASA/AGCOM/HAPS/U-Space)
- Cap. 6 Analisi tecnica di fattibilità (architettura, prestazioni, FMECA/FTA, trade study = DOCFAP)
- Cap. 7 Analisi di mercato e business case
- Cap. 8 Analisi economica e finanziaria (CapEx, OpEx, NPV, IRR, payback)
- Cap. 9 Cronoprogramma e gate decisionali
- Cap. 10 Raccomandazione di gate (verdetto Go / Hold / No-Go)
- Cap. 11 Roadmap post-fattibilità (Fase 1 VTOL, Fase 3 HALE)

### Volume 2 — Allegati tecnici
RTM, Risk Register, Trade Study Reports, ICD, V&V Plan, schemi CAD, modelli di calcolo (energy balance, link budget, polare), bilanci di massa, **Computo Metrico Estimativo** (ground segment), **Piano di Manutenzione preliminare**, **PSC operativo (SORA)**, **VIA preliminare**, documentazione fotografica.

### Volume 3 — Riferimenti
Bibliografia normativa (D.Lgs. 36/2023, Reg.UE 2019/947, EASA AMC, ENAC LRA), bibliografia tecnica (NASA SE, INCOSE, ECSS, DO-178C), fonti dati di mercato.

### Documenti preliminari ex art. 41 / Allegato I.7
Da formalizzare oltre allo Studio: **Quadro Esigenziale (QE)**, **DOCFAP** (= sintesi dei nostri Trade Study), **DIP**. Servono per allineare il documento alla forma richiesta dai bandi pubblici italiani.

## Convenzioni operative

- I documenti originali (`.docx`, `.pdf`, `.xlsx`) sono stati convertiti in `.md` accanto agli originali: lavorare sui `.md` per analisi/lettura.
- Quando produci deliverable finali (studio, slide, modello finanziario), genera **`.docx` / `.pptx` / `.xlsx`** usando le skill ufficiali Anthropic.
- Ogni capitolo dello studio di fattibilità deve essere agganciato a un **gate decisionale Go/No-Go** con evidenze tracciabili (RTM, risk register, trade study).
- Niente affermazioni non verificate: ogni numero/normativa/competitor deve citare la fonte (file locale o URL).

## Agenti ed esperti disponibili

Vedi `.claude/README.md` per la lista completa con quando usare ciascun esperto.
