# Capitolo 9 — Cronoprogramma e Gate Decisionali

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes
> Volume 1, Capitolo 9
>
> **Versione:** bozza M+3
> **Conformità:** D.Lgs. 36/2023 art. 41 (sezione "Cronoprogramma") + NASA SE Handbook §3.0 (Project Life Cycle Reviews) + skill `gate-review-checklist`
> **Disciplina epistemica:** Regole 1-7 della skill `epistemic-rigor`
> **Red Team review:** `aerospace-systems-engineer` + `red-team-skeptic` — vedi §9.8

---

## 9.0 Sintesi del capitolo

Il presente capitolo definisce il **cronoprogramma** dello Studio di Fattibilità (M+0 → M+11) e dei due percorsi (6A operativo + 6B R&D Phase B), insieme ai **gate decisionali Go/No-Go** con criteri di entry/exit, in coerenza con NASA SE Handbook §3.0 e il framework italiano art. 41 D.Lgs. 36/2023.

### 9.0.1 Cronoprogramma overall

```
M+0    M+3    M+6    M+10/11   M+12         M+24            M+36            M+48
│      │      │      │         │            │               │               │
│ G0   │ G1   │ G2   │ G3       │ G4         │ G5            │ G6            │
│ Kick │ Conc │ Arch │ FEAS     │ End 6A     │ Eval 6B       │ Eval 6B       │ Phase B
│ off  │ ept  │ itet │ verdict  │ MVP        │ start         │ midterm       │ end
│      │ fro  │ tura │ Go/Hold  │            │ Phase B       │               │
│      │ zen  │ base │          │            │               │               │
│      │      │ line │          │            │               │               │
├──────┼──────┼──────┼──────────┼────────────┼───────────────┼───────────────┼─────►
│   STUDIO DI FATTIBILITÀ      │   PILOTA 6A VTOL OP        │   R&D 6B HALE PHASE B           │
│       (Pre-Phase A → A)       │   (Phase B operativo)      │   (Phase B/C R&D HALE)          │
```

### 9.0.2 Gate decisionali del Piano di Fattibilità

| Gate | Mese | Fase NASA SE | Verdetto target | Documenti chiave da consegnare |
|---|---|---|---|---|
| **G0** | M+0 | Kick-off | Avvio Studio (no formal Go) | Briefing + Contratto Coopfond |
| **G1** | M+3 | Pre-Phase A → A | Concept Frozen | Concept doc + StNeeds raccolti + Risk Reg v0 |
| **G2** | M+6 | Phase A | Architecture Baselined | Arch 6A+6B base + RTM v0.5 + ICD prelim + Trade Study iniziali |
| **G3** ⭐ | **M+10/M+11** | **FEASIBILITY GATE PRIMARIO** | **Go / Go Cond. / Hold / No-Go** per **ogni percorso** | **Studio completo Vol.1+2+3** + RTM v0.8 + Risk Reg v2 + Quadro Economico + Strategia finanziamenti + DPIA prelim |
| **G4** | M+12 | Fine pilota VTOL 6A | Go espansione SNAI / Hold | Ops Y1 results + Customer feedback + Financial Y1 |
| **G5** | M+24 | Evaluation HALE 6B start Phase B | Go Phase B / Defer | EuroHAPS-adjacent partnership + Funding readiness + Reg progress |
| **G6** | M+36+ | HALE Phase B mid | Continue / Stop | TRL HALE subsystem 5+ |

### 9.0.3 Verdetto cronoprogramma in sintesi

| Aspetto | Stato | Note |
|---|---|---|
| Tempistiche realistiche | ✅ allineate base rate aerospace | 11 mesi per fattibilità + 12 mesi pilota: aggressivi ma fattibili |
| Gate decisionali strutturati | ✅ NASA SE compliant | 7 gate principali con entry/exit criteria |
| Risk-informed | ✅ Risk Register agganciato | Ogni gate ha review showstopper |
| Verificabile | ✅ criteri quantitativi | KPI numerici per ogni gate |
| Flessibilità | ✅ "Hold" e "Defer" disponibili | No-Go solo per showstopper insuperabili |

---

## 9.0bis Boundary conditions

In coerenza con Cap. 5.0bis, 3.0bis, 7.0bis:
- **B1**: tutti i milestone operativi sono erogazione di servizi (non manufacturing/sale)
- **B2**: la sequenza dei gate è coerente con la visione 10 anni (Cap. 11)

---

## 9.1 Master Schedule dello Studio di Fattibilità (M+0 → M+11)

### 9.1.1 Work Breakdown Structure (WBS) — Studio di Fattibilità

```
Studio di Fattibilità HALE/VTOL — WBS
├── 1.0 Project Management
│   ├── 1.1 Project planning + governance
│   ├── 1.2 Risk management continuous (Risk Register update)
│   ├── 1.3 Stakeholder engagement coordination
│   └── 1.4 Gate review preparation (G1-G3)
│
├── 2.0 Stakeholder & Requirements
│   ├── 2.1 Stakeholder workshop (M+0-3)
│   ├── 2.2 StNeeds collection + validation (M+3-6)
│   ├── 2.3 System Requirements (SyR) baseline (M+3-6)
│   ├── 2.4 RTM construction + expansion (M+3-10)
│   └── 2.5 Subsystem Requirements (SsR) decomposition (M+6-10)
│
├── 3.0 Technical Engineering
│   ├── 3.1 Concept architecture 6A + 6B (M+0-3)
│   ├── 3.2 Trade studies (M+3-9)
│   │   ├── TS-PLATFORM-6A
│   │   ├── TS-MATERIAL
│   │   ├── TS-PROP-6B
│   │   ├── TS-AVI-6A
│   │   ├── TS-PAYLOAD-EO
│   │   └── TS-COMMS
│   ├── 3.3 Performance analysis (M+3-9)
│   ├── 3.4 FMECA + FTA preliminary (M+6-10)
│   └── 3.5 Energy balance HALE simulation (M+6-10)
│
├── 4.0 Regulatory Engagement
│   ├── 4.1 Pre-application meeting ENAC (M+3-6)
│   ├── 4.2 Engagement EASA Innovation Network (M+6-9)
│   ├── 4.3 AGCOM spectrum consultation (M+6-10)
│   ├── 4.4 Privacy/Garante DPIA preliminary (M+3-9)
│   └── 4.5 Compliance documentation (M+9-11)
│
├── 5.0 Market & Business
│   ├── 5.1 Market analysis Liguria (M+0-3)
│   ├── 5.2 Stakeholder workshop cooperative (M+3-6)
│   ├── 5.3 LoI Regione Liguria (M+3-6)
│   ├── 5.4 Customer pricing benchmark (M+3-9)
│   ├── 5.5 BMC + VPC consolidation (M+6-9)
│   └── 5.6 MVP definition (M+6-10)
│
├── 6.0 Financial
│   ├── 6.1 Quadro Economico baseline (M+3-9)
│   ├── 6.2 NPV/IRR/Payback model (M+6-9)
│   ├── 6.3 Sensitivity + Monte Carlo (M+9-11)
│   ├── 6.4 Funding mix consolidation (M+6-10)
│   └── 6.5 Funding LoI/contracts (M+6-11)
│
├── 7.0 Documentation
│   ├── 7.1 Volume 1 — Studio (Cap. 1-11) (M+0-11)
│   ├── 7.2 Volume 2 — Allegati tecnici (M+3-11)
│   ├── 7.3 Volume 3 — Riferimenti (M+9-11)
│   └── 7.4 Executive Summary (Cap. 0) (M+10-11)
│
└── 8.0 Gate Review
    ├── 8.1 G1 preparation (M+2-3)
    ├── 8.2 G2 preparation (M+5-6)
    └── 8.3 G3 FEASIBILITY GATE prep (M+9-11)
```

### 9.1.2 Gantt schematico dello Studio di Fattibilità (M+0 → M+11)

```
M+0          M+3          M+6          M+10        M+11
│            │            │            │           │
│ ── PM/Governance ──────────────────────────────► │
│            │            │            │           │
│ Stakeholder workshop ──►│            │           │
│            │ ── Requirements + RTM ─────────────►│
│            │            │            │           │
│ ── Concept arch 6A+6B ─►│            │           │
│            │ ── Trade studies ──────►│           │
│            │            │ Performance + FMECA ──►│
│            │            │            │           │
│            │ ENAC pre-application ──►│           │
│            │            │ EASA engagement ──────►│
│            │            │ AGCOM consultation ───►│
│            │            │ Garante DPIA ─────────►│
│            │            │            │           │
│ Market Liguria ────────►│            │           │
│            │ LoI Regione + workshop coop ──────►│           │
│            │            │ MVP definition ───────►│           │
│            │            │            │           │
│            │ Quadro Economico ──────────────────►│           │
│            │            │ NPV/IRR ──────────────►│           │
│            │            │ Sensitivity + funding ►│           │
│            │            │            │           │
│ ── Vol.1 chapters draft ──────────────────────►│           │
│            │            │ Vol.2 allegati ────►│           │
│            │            │            │ Vol.3 + Exec Summary │
│            │            │            │           │
│ G0        G1           G2            G3         G3 final
│ Kick      Concept      Arch          FEAS       FEAS verdict
│ off       Frozen       Baselined     review     Go/Hold
```

### 9.1.3 Risorse umane per fase

| Mese | Team interno Firmamento | Consulenti esterni | Note |
|---|---|---|---|
| M+0-3 | 3-4 FTE (founder + 2 ing + 0.5 PM) | 1-2 (regulatory + finance) | Setup operativo |
| M+3-6 | 4-5 FTE (+ 1 analyst GIS) | 2-3 (regulatory + finance + market) | Engagement intensivo |
| M+6-10 | 5-7 FTE (+ pilota UAS) | 3-4 (+ technical advisor + DPO) | Validazione esterna |
| M+10-11 | 7 FTE | 4 + 1 reviewer indipendente | Gate G3 preparation |

---

## 9.2 Gate Decisionali — Entry e Exit Criteria

### 9.2.1 G0 — Kick-off (M+0)

**Tipologia**: avvio progetto, no formal Go/No-Go.

**Entry criteria**:
- Bando Cooding aggiudicato o Letter of Award firmata
- Contratto Coopfond eseguito
- Team Firmamento allocato
- Briefing approvato dal CdA Firmamento

**Output**: kick-off meeting + project charter + master schedule baseline.

### 9.2.2 G1 — Concept Frozen (M+3)

**Entry criteria** (da soddisfare per poter tenere il review):
- ☐ Briefing iniziale rivisto e approvato
- ☐ Stakeholder identificati e prima mappa engagement
- ☐ StNeeds raccolti (≥ 17 needs documentati, conf. medium-high)
- ☐ Vincoli e assunzioni iniziali baselined
- ☐ Risk Register v0 (top-10 rischi identificati)
- ☐ Quadro Esigenziale (Cap. 1) bozza
- ☐ Concept architettura 6A + 6B definito a livello narrativo

**Exit criteria** (per passare a G2):
- ✅ Concept architetture 6A + 6B approvato
- ✅ StNeeds confidence ≥ medium su almeno 12 stakeholder principali
- ✅ Top-10 rischi con preliminary owner + mitigation plan
- ✅ G1 review board sign-off

**Verdetto possibili**:
- **Go** → procedere a Phase A engineering
- **Hold** → re-do entro 30-60 giorni
- **Pivot** → ridefinire concept (rara, attiva re-baseline)

### 9.2.3 G2 — Architecture Baselined (M+6)

**Entry criteria**:
- ☐ Architettura concettuale 6A + 6B documentata (Cap. 6.1)
- ☐ System Requirements baselined (SyR-XXX completi, ≥ 30 SyR)
- ☐ RTM v0.5 (tracciabilità StNeeds → SyR)
- ☐ ICD preliminare (interfacce principali, ≥ 15)
- ☐ Trade Study chiave conclusi (TS-PLATFORM-6A, TS-MATERIAL, TS-PROP-6B preliminary)
- ☐ Risk Register v1 con scoring P×I
- ☐ DOCFAP draft per le decisioni architetturali principali

**Exit criteria**:
- ✅ Architecture sign-off da systems engineer + Red Team check OK
- ✅ RTM coverage ≥ 70% StNeeds tracciati
- ✅ Tutti i trade study chiave hanno una raccomandazione preliminare
- ✅ Risk score top-5 con mitigation plan definito

### 9.2.4 G3 — FEASIBILITY GATE PRIMARIO (M+10/M+11) ⭐

Il gate principale dello Studio. Verdetto formale Go/No-Go per ogni percorso.

**Entry criteria** (lista esaustiva):
- ☐ Studio di Fattibilità Vol.1 (Cap. 0-11) completo
- ☐ Vol.2 Allegati tecnici completi
- ☐ Vol.3 Riferimenti completi
- ☐ Tutti i trade study chiusi e DOCFAP redatto
- ☐ RTM v0.8 (≥ 95% StNeeds tracciati a SyR; ≥ 100% SyR con V&V method)
- ☐ Risk Register v2 (top rischi con mitigation in progress / planned)
- ☐ Quadro Economico (art. 41) approvato
- ☐ Piano economico-finanziario con sensitivity (Excel modello)
- ☐ Strategia finanziamenti consolidata + LoI principali firmate
- ☐ Engagement preliminare ENAC (pre-application docs ricevuti)
- ☐ Engagement Regione Liguria (commitment formale: DGR o accordo)
- ☐ Privacy/GDPR DPIA preliminare pubblica
- ☐ Master schedule M+12 → M+48 per Fase 2-3

**Exit criteria 6A** per **Go**:
- ✅ ≥ 90% entry criteria soddisfatti
- ✅ Verdetto Cap. 5 (Regulatory) = "GO"
- ✅ Verdetto Cap. 6 (Tecnico) = "GO" + risk score top 3 < 16 (giallo)
- ✅ Verdetto Cap. 7 (Mercato) = "GO" + LoI ≥ 3 firmate
- ✅ Verdetto Cap. 8 (Finanziario) = "GO" + funding mix ≥ 60% commitment
- ✅ Verdetto Cap. 10 (Raccomandazione) coerente

**Exit criteria 6A** per **Go Condizionato**:
- 80-90% entry criteria + condizioni esplicite scritte
- Risk top 3 score ≤ 16 con piano mitigation chiaro
- Almeno 2 LoI firmate (no minimo 3)
- Funding ≥ 40% commitment + plan per ulteriore 30-40% entro M+12

**Exit criteria 6B** per **Hold / Go Cond. Estremo**:
- Verdetto Cap. 5 (Regulatory) = "HOLD" o "Go Cond. Estremo" (atteso)
- Verdetto Cap. 6 (Tecnico) = HOLD con showstopper RSK-TEC-001/002 dichiarati
- Roadmap Phase B definita con engagement EASA + funding multi-source

**Verdetti possibili G3**:
- **6A Go + 6B Hold/Defer** (scenario base atteso)
- **6A Go Cond. + 6B Defer** (scenario realistico se LoI/funding non completi)
- **6A Hold + 6B Hold** (scenario peggiore, attiva pivot strategico)
- **6A No-Go + 6B No-Go** (scenario catastrofico, esclusione progetto — unlikely)

> **Falsifying observation G3**: se al M+10/M+11 ≥ 30% degli entry criteria non sono soddisfatti, verdetto è **HOLD**, non No-Go. Il No-Go è riservato a showstopper insuperabili (es. ENAC nega esplicitamente path SAIL Pentema, Regione si tira indietro, funding zero).

### 9.2.5 G4 — Fine Pilota VTOL 6A (M+12)

**Entry criteria**:
- ☐ Operazioni Y1 completate
- ☐ ≥ 50 missioni eseguite
- ☐ Customer feedback Regione + PC + cooperative documentato
- ☐ Financial Y1 (utilization, revenue, OpEx) consolidato
- ☐ Lessons learned report
- ☐ Plan espansione SNAI multi-area redatto

**Exit criteria** per **Go scale-up**:
- ✅ ≥ 50 missioni completate senza FATAL/major
- ✅ ≥ 3 contratti pluriennali firmati (Y1 + estensione Y2-Y3)
- ✅ Revenue Y1 cumulato ≥ €200k (SyR-Cost-003)
- ✅ NPS PA/cooperative ≥ 40
- ✅ Almeno 1 LoI per espansione 2nda regione SNAI

### 9.2.6 G5 — Evaluation HALE Phase B (M+24)

**Entry criteria** (per decidere Phase B 6B):
- ☐ Risultati Pilota 6A (G4) + Y2 scale-up consolidati
- ☐ Risultati EuroHAPS Phase A pubblicati / engagement CIRA formalizzato
- ☐ Framework EASA HAPS aperto formalmente o atteso entro 2030
- ☐ Funding readiness commit ≥ 50% Phase B €5.5-13.5M (LoI EDF/Horizon/PNRR/Series)
- ☐ Technology maturity 6B subsystems re-assessed (TRL targets per gate G6 a M+36)
- ☐ Risk Register 6B aggiornato

**Verdetti possibili**:
- **Go Phase B** (full)
- **Go Cond. Phase B** (subordinato a milestone interno entro 6-12 mesi)
- **Defer 6B** (rinvio a M+36)
- **No-Go 6B** (cancellazione, focus solo 6A scale-up)

### 9.2.7 G6 — HALE Phase B Midterm (M+36)

**Entry criteria**:
- ☐ Phase B in corso da 12 mesi (M+24 → M+36)
- ☐ Prototipo subscale 1:3 in test bed (TRL 5)
- ☐ Energy balance simulazione completa con scenario inverno chiarito
- ☐ FCS subsystem in test integrato (TRL 5)
- ☐ Engagement EASA Special Condition aperto

**Exit criteria** per **Continue Phase B**:
- ✅ TRL subsystem critici ≥ 5
- ✅ Energy balance inverno: margine ≥ 20% o fallback seasonal accettato
- ✅ Mid-Phase B financial review OK
- ✅ No showstopper aggiunto

---

## 9.3 Cronoprogramma Operativo Percorso 6A (M+12 → M+36)

### 9.3.1 Fase 1 — Y1 MVP (M+0 → M+12)

(Sovrapposto con lo Studio di Fattibilità nei primi 11 mesi)

```
M+0     M+3      M+6        M+9         M+12
│       │        │          │           │
│ Setup │ SORA   │ License  │ Auth      │ Operations
│ team  │ pre-   │ AGCOM    │ ENAC      │ + first
│ + GS  │ app    │ + DPIA   │ + first   │ revenue
│       │ ENAC   │          │ missions  │ → G4
│       │        │          │           │
```

| Milestone | Mese | Deliverable |
|---|---|---|
| M+1 | Acquisto piattaforma JOUAV CW-30E | Contratto vendor |
| M+2 | Setup GS Pentema | Container + antenne + UPS |
| M+3 | SORA pre-application meeting ENAC | Feedback ENAC + GRC/SAIL stima |
| M+4-5 | Costruzione SORA application | ConOps + GRC computation + OSO compliance |
| M+6 | Submission SORA application | Documenti consegnati a ENAC |
| M+7-9 | Integrazione payload + test bench | Test piattaforma + payload + GS |
| M+9 | Autorizzazione ENAC ricevuta | Auth Specific Category SAIL II-III |
| M+10 | Prime missioni operative | Log operativi |
| M+11 | Consolidamento + feedback | Customer survey |
| M+12 | Gate G4 + financial Y1 close | Financial report Y1 |

### 9.3.2 Fase 2 — Y2 Espansione Liguria (M+12 → M+24)

```
M+12      M+15        M+18        M+21        M+24
│         │           │           │           │
│ Scale   │ Expand    │ 2-3 GS    │ Multi-    │ G5
│ to 4    │ to 4-6    │ flotta    │ regione   │ Phase B
│ SNAI    │ use case  │ 2-3 UAS   │ adds      │ start
│         │           │           │           │
```

| Milestone | Mese | Deliverable |
|---|---|---|
| M+13 | Acquisto 2nd UAS | Contratto vendor |
| M+15 | Apertura 2nd GS (mobile o fissa zona Antola) | GS operativa |
| M+18 | Espansione casi d'uso (multispettrale agricolo, LiDAR mapping) | New service modules |
| M+21 | LoI 2nda regione SNAI (Piemonte / Calabria) | LoI signed |
| M+24 | Gate G5 Phase B 6B evaluation | Phase B Go/No-Go |

### 9.3.3 Fase 3 — Y3 Multi-regione SNAI (M+24 → M+36)

```
M+24       M+30         M+36
│          │            │
│ Flotta 3-5│ 3-4 regioni│ HALE
│ UAS       │ servite    │ subscale
│           │            │ TRL 5
│           │            │ G6
```

| Milestone | Mese | Deliverable |
|---|---|---|
| M+27 | Espansione flotta 3 UAS | |
| M+30 | LoI 3a regione SNAI | |
| M+33 | First Phase B 6B subscale flight test | Subscale prototype TRL 5 |
| M+36 | Gate G6 Phase B midterm review | Continue/Stop Phase B |

---

## 9.4 Cronoprogramma Percorso 6B R&D Phase B (M+24 → M+48)

### 9.4.1 Phase B engineering (M+24 → M+36)

| Mese | Task | Output |
|---|---|---|
| M+24-26 | Setup team R&D 8-15 FTE | Team allocated, infrastructure |
| M+26-30 | Detailed design 6B HALE subscale | Detailed drawings + analysis |
| M+30-32 | Prototyping subscale 1:3 (24 m wingspan) | Subscale article |
| M+32-34 | Ground tests (GVT + structural) | Test reports |
| M+34-36 | First flight test subscale | Flight data + TRL 5 dichiarato |

### 9.4.2 Phase B integration (M+36 → M+48)

| Mese | Task | Output |
|---|---|---|
| M+36-40 | Test envelope expansion subscale | Flight envelope chart |
| M+40-44 | Payload integration subscale | Payload demo |
| M+44-48 | Stratospheric flight test (target FL400+ subscale) | Stratospheric data |

Phase C-D (Full-scale + Type Certification, M+48-72+): out-of-scope dello Studio attuale, descritto in Cap. 11 (Roadmap post-fattibilità).

---

## 9.5 Cronoprogramma Engagement Istituzionale

Sintesi (dettaglio in Cap. 5 §5.11.3 + Cap. 8 §8.7).

| Stakeholder | M+0-3 | M+3-6 | M+6-12 | M+12-24 | M+24+ |
|---|---|---|---|---|---|
| **ENAC** | Pre-app meeting | SORA submission | Auth operativa | Renewal + Phase 2 | Special Cond. HAPS |
| **EASA** | – | Innovation Network engagement | RMT request HAPS | Special Cond. dialogue | Special Cond. plan approved |
| **AGCOM** | – | Spectrum consultation | License application | License granted | Bands HAPS dedicated |
| **Garante Privacy** | – | DPIA pubblica draft | DPIA submit | DPIA close | Update |
| **Regione Liguria** | First meeting | LoI | DGR / Contract | Renewal | Multi-regione |
| **Coopfond** | Cooding domanda | Cooding-Invest | Reporting Y1 | Reporting Y2 | – |
| **MIMIT** | – | PNRR scouting | Bando submission | Award + reporting | – |
| **CIRA** | Letter intent | MOU negotiation | MOU signed | Partnership Phase B | Active R&D consortium |
| **DG CNECT/DEFIS** | – | – | EDF/Horizon proposal | Project award | Ongoing |
| **D-Flight** | – | – | Engagement U-Space | Service agreement | Renewal |
| **Comunità Pentema** | Workshop pubblico | DPIA pubblica | Update + reporting | Consultazione continua | Renewal sociale |

---

## 9.6 Risk-Informed Gate Approach

Ogni gate review include una **review esplicita dei rischi**:

| Gate | Rischi top da rivedere | Soglia per Go |
|---|---|---|
| G1 (M+3) | Risk Register v0 top-10 | Tutti i rischi hanno owner + preliminary plan |
| G2 (M+6) | Risk Register v1, scoring P×I | Nessun rischio rosso (≥15) senza piano definito |
| **G3 (M+10/M+11)** | **Risk Register v2 + showstopper** | **Top 3 risk score < 16 (giallo); RSK-TEC-001 e RSK-REG-001 con piano credibile** |
| G4 (M+12) | Risk Register v3 post-Y1 ops | Nessun nuovo showstopper aggiunto |
| G5 (M+24) | Risk Register 6B aggiornato | RSK-TEC-001 (energy balance inverno) con simulazione decisiva |
| G6 (M+36) | Risk Register Phase B midterm | TRL subsystem ≥ 5 + no nuovo showstopper |

### 9.6.1 Showstopper formali (richiamo dai capitoli)

| ID | Rischio | Score | Gate critico | Mitigation owner |
|---|---|---|---|---|
| RSK-TEC-001 | Energy balance HALE inverno 44°N | 20 🔴 | G5 (M+24) | propulsion-energy-engineer |
| RSK-TEC-002 | Aeroelasticità ala high-AR | 15 🔴 | G6 (M+36) | aero-structures-engineer |
| RSK-REG-001 | Mancanza framework HAPS EASA | 20 🔴 | G5 | aviation-regulatory-counsel |
| RSK-FIN-001 | Mancanza funding R&D 6B €5.5-11M | 20 🔴 | G3-G5 | financial-cfo-analyst |
| RSK-TEC-003 | Type Cert HALE > 5 anni | 16 🔴 | G3 (per Phase B Go) | aviation-regulatory-counsel |

---

## 9.7 Governance e Composizione Board del Gate Review

### 9.7.1 Board standard (interno) per G1, G2, G4

- Project Manager (chair)
- Aerospace Systems Engineer (technical lead)
- Financial CFO Analyst
- Aviation Regulatory Counsel
- Business Model Strategist

### 9.7.2 Board allargato per G3 (FEASIBILITY GATE)

Standard board +:
- Rappresentante Regione Liguria
- Rappresentante Coopfond
- Rappresentante cooperative (Fabrica capofila)
- **Independent reviewer** (consultant aerospace senior o ente terzo, es. RINA — per validation indipendente)
- Osservatore ENAC (su invito informale)

### 9.7.3 Board G5, G6 (Phase B HALE)

Board allargato +:
- Rappresentante CIRA (se partnership formalizzata)
- Rappresentante EDF / DG DEFIS (su invito)
- Rappresentante TAS-Leonardo (su invito, condizionato)

---

## 9.8 Red Team Check — Schedule Stress Test

### Critica 1 — "11 mesi per Studio di Fattibilità completo è poco vs base rate aerospace"
**Razionale**: Studi di fattibilità aerospace richiedono tipicamente 12-24 mesi. 11 mesi è aggressivo.
**Risposta**: corretto, è aggressivo. Mitigazione: (a) scope limitato a 2 percorsi (non multi-architettura), (b) reuse di documenti esistenti (Briefing + Studio preliminare in `da revisionare/`), (c) team focused + consultants esterni. Se al G2 (M+6) il progress è < 60%, si può estendere G3 a M+13-14.

### Critica 2 — "Engagement ENAC pre-application in 3 mesi: aggressivo"
**Razionale**: ENAC ha tempi di risposta normalmente 30-90 giorni, anche solo per pre-meeting. Pretendere SAIL stima entro M+3 è ottimistico.
**Risposta**: confermato. Plan B: spostare SORA submission a M+9 se M+3-6 ENAC restituisce solo feedback preliminare senza commitment SAIL. Il gate G3 può accomodare questo slittamento.

### Critica 3 — "FEASIBILITY GATE (G3) con 13 entry criteria: troppi per single review"
**Razionale**: gate review tipico aerospace ha 5-8 entry criteria. 13 rende il gate "gate killer" — tutti i criteri devono essere allineati simultaneamente.
**Risposta**: corretto. I 13 criteri sono il **set ideale**. Soglia pragmatica: ≥ 90% per Go pieno, 80-90% per Go Condizionato. < 80% = Hold con re-review entro 30-60 giorni.

### Critica 4 — "Phase B HALE M+24-48 con TRL target 5 a M+36 e flight stratosferico a M+44-48 è speculativo"
**Razionale**: TRL transition da 3-4 a 5-6 richiede tipicamente 2-3 anni per HALE solare. M+44-48 stratospheric flight è scenario best-case.
**Risposta**: confermato. La timeline è target ottimistico. Il gate G6 (M+36) è decisivo: se TRL < 5, Phase B continua ma estesa a M+60+. Il Cap. 11 (Roadmap) include scenari realistici.

### Critica 5 — "Engagement Garante Privacy: M+6 DPIA submit è ottimismo. Garante può richiedere mesi di consultazione."
**Razionale**: il Garante è notoriamente conservativo, richiede multiple round di richieste integrazioni.
**Risposta**: corretto. Il M+6 DPIA submit è target; M+12 close DPIA è realistico. Mitigazione: DPIA preliminare M+3 + consultazione informale Garante M+3-6 per identificare gap precoci.

---

## 9.9 Open Questions del Cronoprogramma

| OQ-ID | Domanda | Owner | Deadline |
|---|---|---|---|
| OQ-S01 | Tempi reali ENAC per SAIL feedback | regulatory-counsel | M+3 |
| OQ-S02 | Tempi reali AGCOM licensing per banda commerciale | telecom-payload | M+6 |
| OQ-S03 | Disponibilità reviewer indipendente per G3 (RINA o equivalente) | PM | M+9 |
| OQ-S04 | Calendar exact bandi 2026-2027 (Coopfond, FESR, PNRR, Horizon) | snai-funding | M+1 |
| OQ-S05 | Eventual condivisione gate review con stakeholder (Coopfond + Regione) | PM | M+3 |
| OQ-S06 | Buffer schedule per imprevisti (gate M+10 vs M+13) | PM + sponsor | M+6 |

---

## 9.10 Riferimenti

[^1]: NASA Systems Engineering Handbook Rev 2 (NASA/SP-2016-6105 Rev 2), §3.0 Project Life Cycle Reviews. Source: `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md`. Confidence: high.

[^2]: D.Lgs. 36/2023 art. 41 + Allegato I.7 (Cronoprogramma). Source: `fonti/2023_0036.md`. Confidence: high.

[^3]: Skill `gate-review-checklist` (`.claude/skills/gate-review-checklist/SKILL.md`). Workflow Go/No-Go applicato.

[^4]: Skill `epistemic-rigor` + `red-team-skeptic` per stress test cronoprogramma.

[^5]: ENAC AAM Roadmap 2021-2030 — reference per timing engagement istituzionale. Source: `fonti/02_AAM-Italian-Ecosystem-Roadmap_web-1.md`.

[^6]: EuroHAPS — riferimento per timing R&D HAPS subscale (Sardinia/Fuerteventura demonstration 2024). Source: `riferimenti/ricerche-approfondite.md` §6.

[^7]: GAO Cost Estimating Guide (GAO-20-195G) — base rate per schedule overrun aerospace 30-100%.

---

## 9.11 Note di chiusura del capitolo

Il Cap. 9 è **bozza M+3** con verdetto Red Team **OK con caveat** sulla aggressività dei tempi.

**Verdetto cronoprogramma riepilogato**:
- Studio di Fattibilità (M+0-11): **realizzabile** con team focused + consultants
- Gate G3 (M+10-11): **gate primario realistico** con criteri di flessibilità (90% / 80% / < 80%)
- Pilota 6A (M+12-36): **realistico** con margine
- Phase B 6B (M+24-48): **aggressivo**, richiede gate G5 + G6 conferme TRL

**Action items entro M+3**:
- Acquisto piattaforma VTOL (Plan A JOUAV / Plan B Tekever decisione)
- Pre-application meeting ENAC
- LoI Regione Liguria (in negoziazione)
- Workshop comunità Pentema
- Workshop cooperative

Il capitolo è chiuso al M+3 con verdetto Red Team **OK con 5 azioni**.
