---
name: feasibility-study-framework
description: Use this skill any time the user needs to draft, structure, or fill a chapter of the HALE Feasibility Study. Trigger when the user mentions "studio di fattibilità", "capitolo X", "stesura", "scrivi cap", "PFTE", "DOCFAP", "Quadro Esigenziale", "NASA SE", "redigi il documento", or wants to build/review parts of the technical-economic feasibility study under art. 41 D.Lgs. 36/2023 + NASA SE Handbook hybrid framework. Generates skeletons, section templates, deliverable checklists for any chapter of the 3-volume HALE Feasibility Study.
---

# Feasibility Study Framework — HALE Firmamento Technologies

Questa skill genera **scheletri di capitolo** e **template di sezione** per lo Studio di Fattibilità HALE secondo il framework **ibrido NASA SE Handbook + Codice dei Contratti italiano (art. 41 D.Lgs. 36/2023 + Allegato I.7)**.

## Quando usare

- Stesura di un nuovo capitolo dello Studio
- Revisione di un capitolo esistente per verificarne completezza
- Definizione del Quadro Esigenziale (QE), DOCFAP, DIP secondo Allegato I.7
- Generazione di un Volume 2 — Allegati Tecnici
- Compilazione del Volume 3 — Riferimenti normativi

## Struttura canonica dello Studio (3 volumi)

### Volume 1 — Studio (testuale)

```
Cap. 0  Sintesi Esecutiva (1-3 pagine, target lettore decisore)
Cap. 1  Inquadramento del progetto e obiettivi (= Quadro Esigenziale ex art. 41)
        1.1 Contesto e bando di riferimento
        1.2 Motivazione: Aree Interne, razionale pubblico, caso Liguria
        1.3 Visione tecnologica: HALE + percorso duale 6A/6B
        1.4 Necessità analisi comparativa
        1.5 Obiettivi del Piano di Fattibilità

Cap. 2  Contesto, stakeholder, obiettivi SMART
        2.1 Stakeholder map (con leve di engagement)
        2.2 Obiettivi SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
        2.3 Vincoli e assunzioni iniziali

Cap. 3  Requisiti e criteri di successo (= NASA SE Phase A)
        3.1 Razionale e metodologia
        3.2 Criteri Go/No-Go baseline
        3.3 Stakeholder Needs (StNeeds)
        3.4 System Requirements (SyR)
        3.5 Requirements Traceability Matrix (RTM)
        3.6 Assumptions & Limiti
        3.7 Open Questions

Cap. 4  Perimetro, scope, deliverable, interfacce (ICD preliminare)
        4.1 Scope e obiettivi della fase di fattibilità
        4.2 In-scope / Out-of-scope per dominio
        4.3 Deliverable del Piano di Fattibilità
        4.4 Interfacce principali (ICD preliminare)
        4.5 Criteri di accettazione del perimetro

Cap. 5  Quadro normativo e regolamentare
        5.1 Quadro UE (Reg. 2018/1139, 2019/947, 2019/945, 2021/664-666 U-Space)
        5.2 Quadro Italia (D.Lgs. 28/2018, Reg. ENAC Ed.3, PSN AAM)
        5.3 Categoria EASA target Percorso 6A (Specific Category, SAIL)
        5.4 Categoria EASA target Percorso 6B (Certified, framework HAPS)
        5.5 Spettro radio: ITU, AGCOM, PNRF
        5.6 Privacy: GDPR, Garante, DPIA preliminare
        5.7 Sicurezza: NIS2, cybersecurity aviazione (DO-326A)
        5.8 Ambientale: VIA preliminare (se applicabile)

Cap. 6  Analisi tecnica di fattibilità (NASA SE Phase A engineering)
        6.1 Concept architetture 6A VTOL ibrido + 6B HALE solare
        6.2 Prestazioni preliminari (peso, autonomia, payload, energy balance)
        6.3 Trade studies (= DOCFAP) — config alari, propulsione, payload
        6.4 Analisi rischio ingegneristico (FMECA + FTA + Risk Register)
        6.5 Infrastrutture (ground segment, vertiporti, hangar Pentema)

Cap. 7  Analisi di mercato e business case
        7.1 Segmentazione domanda (B2G/B2B/B2C)
        7.2 TAM / SAM / SOM Italia
        7.3 Competitive landscape (Zephyr, Sunglider, Odysseus, Skydweller, PHASA-35, EuroHAPS)
        7.4 Posizionamento Firmamento
        7.5 Business Model Canvas (per percorso)
        7.6 Value Proposition Canvas (per segmento)
        7.7 Modello di servizio (DaaS/IaaS/canone) e pricing
        7.8 MVP definition

Cap. 8  Analisi economica e finanziaria
        8.1 Quadro Economico (formato art. 41 D.Lgs. 36/2023)
        8.2 CapEx per fase (6A MVP, 6B Phase B)
        8.3 OpEx ricorrente per fase
        8.4 Piano economico-finanziario (NPV, IRR, payback, ROI)
        8.5 Sensitivity & scenario analysis (worst/base/best)
        8.6 Strategia finanziamenti (Coopfond, PNRR, FESR, Horizon, EDF, equity, debito)
        8.7 Cronoprogramma finanziario

Cap. 9  Cronoprogramma e approccio progettuale
        9.1 Master schedule M+0 → M+48
        9.2 Gate decisionali (M+3 Concept, M+6 Architettura, M+10/11 Feasibility, M+24 Eval HALE)
        9.3 V&V Plan
        9.4 Modello di governance e organizzazione team

Cap. 10 Raccomandazione di gate (verdetto finale)
        10.1 Riepilogo evidenze
        10.2 Risk residuo
        10.3 Verdetto Percorso 6A (Go / Go Condizionato / Hold / No-Go)
        10.4 Verdetto Percorso 6B (Hold / Go Condizionato Estremo / Defer)
        10.5 Roadmap post-fattibilità

Cap. 11 Roadmap post-fattibilità
        11.1 Fase 1 — VTOL Pilota Pentema (M+12 → M+24)
        11.2 Fase 2 — Espansione Liguria + scale-up SNAI (M+24 → M+36)
        11.3 Fase 3 — HALE R&D Phase B-C (M+36 → M+60+)
```

### Volume 2 — Allegati tecnici

```
A.1  Requirements Traceability Matrix (RTM) completa
A.2  Risk Register (FMEA + P×I + owner + mitigation + residuo)
A.3  Trade Study Reports (DOCFAP) — uno per ogni decisione architetturale chiave
A.4  Interface Control Document (ICD) preliminare
A.5  Verification & Validation Plan
A.6  Schemi/disegni CAD del concept
A.7  Modelli di calcolo (energy balance, link budget, polare aerodinamica)
A.8  Bilanci di massa preliminari
A.9  Computo Metrico Estimativo (ground segment, hangar, infrastrutture)
A.10 Piano di Manutenzione preliminare
A.11 Piano di Sicurezza Operativa (SORA, Safety Case)
A.12 Relazione VIA preliminare (se applicabile)
A.13 Documentazione fotografica (contesto Pentema, aree pilota)
```

### Volume 3 — Riferimenti

```
R.1  Bibliografia normativa
R.2  Bibliografia tecnica (NASA SE, INCOSE, ECSS, DO-178C, ARP4754A, etc.)
R.3  Fonti dati di mercato (ASD-Eurospace, AIAD, MarkNtel, Grand View, etc.)
R.4  Documenti SNAI e PSNAI
R.5  Studi accademici di riferimento (HELIPLAT, EuroHAPS CIRA, Biogear, etc.)
```

## Template di sezione standard

Ogni sezione/sotto-sezione del Volume 1 segue questo schema:

```markdown
### N.M.k  [Titolo]

**Obiettivo della sezione:** [1 frase]
**Riferimento normativo:** [art. legge / standard]
**Stakeholder primario:** [chi è il destinatario]

#### Contenuto
[testo strutturato in paragrafi brevi + elenchi puntati]

#### Tabelle / Figure
- Tab. N.M.k.1: [titolo]
- Fig. N.M.k.1: [titolo]

#### Open Questions
- OQ-N.M.k-1: [domanda da risolvere prima del gate]

#### Assunzioni
- AS-N.M.k-1: [assunzione]

#### Riferimenti
[link a fonti citate]
```

## Documenti preliminari art. 41 (obbligatori per PFTE)

### Quadro Esigenziale (QE)
- 5-10 pagine
- Contenuti: bisogni (con riferimento SNAI/PSNAI), vincoli (regolatori, finanziari, ambientali), obiettivi del committente, criticità attese
- → Estraibile dai Cap. 1 + Cap. 2 dello Studio

### Documento di Fattibilità delle Alternative Progettuali (DOCFAP)
- = sintesi dei Trade Study NASA SE
- Confronto **opzioni architetturali** (es. VTOL ibrido vs multirotore vs MALE)
- Matrice decisionale ponderata
- → Estraibile dal Cap. 6.3 + skill `trade-study-analysis`

### Documento di Indirizzo della Progettazione (DIP)
- Linee guida del RUP per la fase successiva (Progetto Esecutivo)
- → Da redigere post-Studio (M+12+)

## Workflow tipico per redazione capitolo

1. Identifica il **capitolo target** e i suoi **stakeholder primari**
2. Invoca l'**agente esperto di dominio** appropriato (vedi `.claude/README.md`)
3. Usa il **template di sezione** sopra
4. Compila **tabelle e figure** placeholder
5. Aggancia ogni sezione a:
   - Almeno un **requisito RTM** (Cap. 3)
   - Almeno un **rischio del Risk Register** (App. A.2)
   - Almeno un **gate decisionale** (Cap. 9.2)
6. Verifica la **conformità art. 41 + AS/EN 9100** (citazioni)
7. Genera il deliverable finale via skill `docx` (per il documento Word)

## Convenzioni di stile

- **Lingua:** italiano (terminologia tecnica internazionale resta in EN quando standard)
- **Numerazione:** Cap.N → N.M → N.M.k → N.M.k.j
- **Citazioni:** sempre numerate e raccolte in bibliografia (Cap. R.1-R.5)
- **Acronimi:** glossario obbligatorio in apertura (Cap. 0 o subito dopo)
- **Unit system:** SI + secondary in parentesi per usi industriali (es. "20 km (FL650)")

## Output che produce questa skill

- Scheletro del capitolo richiesto
- Lista deliverable + open questions
- Suggerimento di agenti esperti da convocare
- Checklist di conformità art. 41 / NASA SE / AS-EN 9100
