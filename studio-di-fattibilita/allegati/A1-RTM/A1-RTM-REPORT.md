# Allegato A.1 — Requirements Traceability Matrix (RTM) v1.0 — Report di Accompagnamento

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes
> Volume 2 — Allegato A.1
>
> **Versione documento:** v1.0 (baseline estesa M+3)
> **Data emissione:** 2026-05-17
> **Owner:** aerospace-systems-engineer (Firmamento Technologies)
> **Riferimento Cap. 3:** `studio-di-fattibilita/cap-03-requisiti-e-RTM.md` (RTM v0.5 baseline)
> **Boundary conditions:** B1 (service-only + Legacoop) + B2 (EU sovereign stratospheric / "complementare a IRIS²")

---

## 1. Metodologia (NASA SE Handbook §4)

La presente RTM v1.0 è costruita secondo la metodologia del **NASA Systems Engineering Handbook Rev 2** (NASA/SP-2016-6105 Rev 2), in particolare:

- **§4.1 Stakeholder Expectations Definition** — identificazione di 28 Stakeholder Needs (StNeed-001 → StNeed-028) raccolti da analisi documentale, briefing iniziale, workshop preliminari con la rete cooperative Legacoop, dossier SNAI Liguria, e protocolli operativi di Protezione Civile e Carabinieri Forestali. Confidence levels esplicitati per ogni need (high/medium/low/boundary).
- **§4.2 Technical Requirements Definition** — derivazione di 65 System Requirements (SyR) misurabili, organizzati in 7 famiglie (F, P, O, S, E, C, Cost), in piena conformità alle regole VAFC (Verificable, Atomic, Feasible, Complete) della Appendix C del Handbook + INCOSE Guide for Writing Requirements (GtWR, 2023).
- **§5.3-5.4 V&V Processes** — pianificazione di 67 Verification Requirements (VR) con metodo (Inspection/Analysis/Demonstration/Test) e fase target NASA SE V-model (Pre-A, A, B, B+).

A questa baseline metodologica si aggiungono:
- **Subsystem Requirements (SsR)** decomposti su 6 sottosistemi tecnici (AERO, PROP, AVI, PAY, COMMS, GS) — totale 81 SsR, espansione fine-grained rispetto agli ~80 SsR campione del Cap. 3.6.
- **Interface Requirements (IR)** — 22 interfacce critiche identificate (payload-bus, C2 link, GS-cloud, ENAV/U-Space, broker assicurativi, NOTAM, PA portal, etc.).
- **Negative Requirements (NegR)** — 15 vincoli "shall not" organizzati in 5 famiglie (B Business, Geo Sovereignty, Reg Regulatory, Tech Technical, Mkt Communication), ereditati senza modifiche dal Cap. 3 §3.5.8 come introdotto in risposta alla Critica 5 del Red Team. Audit semestrale obbligatorio per ognuno (Active / Waived / Reviewed).
- **Disciplina epistemica** (skill `epistemic-rigor`): ogni requisito porta esplicitamente confidence level + falsifying observation. Per i requisiti critici (top-20) la falsifying observation è estesa in forma operativa (trigger osservabile + fonte di evidenza + remediation).

**Standard secondari di riferimento:** INCOSE Systems Engineering Handbook 5th Edition (2023); ISO/IEC/IEEE 15288:2015 "System life cycle processes"; ECSS-E-ST-10C (ESA per coerenza europea aerospace).

---

## 2. Statistiche RTM v1.0

| Categoria | Conteggio v1.0 | Baseline Cap. 3 v0.5 | Δ v1.0 vs v0.5 |
|---|---|---|---|
| Stakeholder Needs (StNeed) | **28** | 17 | +11 (workshop preparatory + extension) |
| System Requirements (SyR) | **65** | 42 | +23 (extension fine-grained per famiglia) |
| Subsystem Requirements (SsR) | **81** | ~80 (campione) | +1 (formalizzato) |
| Interface Requirements (IR) | **22** | non formalizzato | +22 (nuovo) |
| Negative Requirements (NegR) | **15** | 14 nominali (15 effettivi in tabella §3.5.8) | 0 (ereditato verbatim) |
| Verification Requirements (VR) | **68** | non formalizzato (V&V Plan §3.7) | +68 (nuovo) |
| **TOTALE righe RTM** | **279** | ~155 stimato | **+124 (+80%)** |

### Breakdown System Requirements per famiglia

| Famiglia SyR | v1.0 | v0.5 baseline | Note |
|---|---|---|---|
| F — Functional | 10 | 5 | Aggiunti UC-005/006/008 + 6B telecom |
| P — Performance | 12 | 6 | Aggiunti GSD, range C2, MTOW 6A/6B |
| O — Operational | 8 | 3 | Aggiunti SOPs, crew, maintenance |
| S — Safety | 8 | 4 | Aggiunti cyber, geofence, ATEX |
| E — Environmental | 5 | 3 | Aggiunti LCA, EOL |
| C — Compliance | 12 | 6 | Aggiunti AI Act, AgID, Direttiva Macchine, ITU |
| Cost — Cost & Business | 10 | 4 | Aggiunti customer concentration, insurance, R&D 6B |

### Breakdown Subsystem Requirements per sottosistema

| Sottosistema SsR | v1.0 | Note |
|---|---|---|
| AERO (Aerodinamica & Strutture) | 16 | CFRP+lino mix, AR≥25, wind tunnel, fatigue life |
| PROP (Propulsione & Energia) | 13 | Solar GaAs, Li-S/SS, BMS, charger, modular swap |
| AVI (Avionica & GNC) | 17 | Autopilot DAL-C, IMU+GNSS redundancy, FTS, encrypted C2 |
| PAY (Payload) | 13 | RGB, IR LWIR, multispettrale, gNB NTN, gimbal, edge ML |
| COMMS (Comunicazioni) | 11 | Service+feeder link, SATCOM, frequency coord, crypto |
| GS (Ground Segment) | 11 | Pentema GS, cloud PSN, anonimizzazione, ISMS, console PIC |
| **TOTALE** | **81** | |

---

## 3. Coverage Analysis

| Metrica di copertura | Valore v1.0 | Soglia G2 (M+6) | Soglia G3 (M+10) | Esito v1.0 |
|---|---|---|---|---|
| StNeeds con ≥1 SyR figlio | **100.0%** | 100% | 100% | OK (passing) |
| SyR decomponibili (F/P/O/S/E) con ≥1 SsR | **72.1%** | 80% | ≥95% | Sotto soglia — gap chiusura M+5-6 |
| SyR con metodo V&V definito | **100.0%** | 80% | 100% | OK (passing) |
| SsR con allocazione subsystem | **100.0%** | 100% | 100% | OK (passing) |
| Orphan SyR (no parent StNeed/SyR/Cap/Bando) | **0** | 0 | 0 | OK (passing) |
| Untestable SyR (no V&V method) | **0** | ≤2 | 0 | OK (passing) |
| NegR Active monitorati | **15/15 (100%)** | 15/15 + 0 violazioni | 15/15 + 0 violazioni + waiver log | OK (passing, 0 violazioni rilevate al M+3) |

> **Note metodologiche sulla coverage SyR→SsR**:
> Il valore 72.1% si riferisce ai soli SyR delle famiglie "decomponibili tecnicamente" (F/P/O/S/E = 43 SyR), di cui 31 hanno almeno un SsR figlio diretto. I SyR delle famiglie C (Compliance) e Cost (Cost & Business) non sono tipicamente decomposti a livello di sottosistema: la loro verifica avviene per Inspection documentale (compliance audit) o per Analysis (Quadro Economico, sensitivity finanziaria), non per derivazione di SsR. Includendo tutte le 65 SyR il valore nominale è 55.4%, ma metodologicamente NASA SE Handbook §4.3 raccomanda di non forzare decomposizione SsR per requisiti non funzionali (compliance, business).
>
> **Action per chiusura M+5-6 (target 80%)**: aggiungere SsR a SyR-F-006 (SAR), SyR-F-009 (Enti Parco), SyR-F-010 (NTN), SyR-P-002 (cruise speed), SyR-O-007 (HALE ConOps), SyR-O-008 (maintenance), SyR-S-005 (failure rate), SyR-S-008 (ATEX), SyR-E-004 (LCA), SyR-E-005 (EOL), SyR-P-011 (MTOW 6A) — 11 SyR da decomporre, ~10-15 ore engineer work.

---

## 4. Critical Requirements — Top-20 Priority H con Falsifying Observation Operative

I 20 requisiti più critici dello Studio (priorità H + falsifying observation con trigger osservabile esplicito):

| # | Req-ID | Description (estratto) | Falsifying Observation operativa | Risk linkato |
|---|---|---|---|---|
| 1 | **SyR-F-002** | Sistema 6A esegue BVLOS con SORA SAIL ≤III | ENAC pre-application meeting nega SAIL II-III per Pentema → re-design ConOps (VLOS only o relocate) | RSK-REG-002 |
| 2 | **SyR-F-005** | Sistema 6B esegue missioni HAPS persistenti >30 giorni estate Y3 | Energy balance simulation worst-case 2026 mostra <0% margine → seasonal-only mandatory + revisione boundary B2 | RSK-TEC-001 |
| 3 | **SyR-P-006** | Energy balance 6B inverno: margine ≥30% o seasonal-only | Simulazione M+10 con tech 2027 mostra margine inverno <0% → fallback seasonal obbligatorio (Plan A) | RSK-TEC-001 |
| 4 | **SyR-F-003** | Antincendio: alert hotspot in ≤5 min con FAR <5% | Demo scenario fuoco-pilota mostra latency >8 min o FAR >10% → revisione pipeline ML + payload IR | RSK-OPS-002 |
| 5 | **SyR-S-001** | Lost-Link: RTL/safe landing entro 60s da loss C2 | Test lost-link mostra non-conformità OSO #9 SAIL III → mitigation aggiuntiva richiesta da ENAC | RSK-TEC-007 |
| 6 | **SyR-S-005** | Failure rate <1e-6/h per cause catastrophic | FTA mostra failure rate >1e-5/h → re-design FCS architecture DAL-C (impatto Phase B €1-2M + 12 mesi) | RSK-TEC-007 |
| 7 | **SyR-C-003** | Conformità GDPR + DPIA per casi d'uso high-risk | DPIA pubblica bocciata Garante → sospensione UC-001/002/004 fino remediation + DPIA v2 | RSK-TEC-006 |
| 8 | **SyR-C-004** | Conformità NIS2 + ISMS Part-IS entro M+9 | ACN audit rileva ISMS gap critico → operations on hold + remediation + assunzione CISO | RSK-REG-019,RSK-REG-027 |
| 9 | **SyR-C-007** | Conformità AI Act art.5+6 per sistemi ML onboard | Garante/AgID classifica payload IR onboard come "alto rischio AI Act" → conformity assessment 6+ mesi | RSK-REG-016 |
| 10 | **SyR-C-008** | AgID/PSN hosting dati PA cloud qualificato | Dati Pentema in cloud non-PSN-qualified → contratti PA rifiutati in fase amministrativa | RSK-REG-021 |
| 11 | **SyR-Cost-003** | Revenue Y1 ≥€200k da contratti pluriennali | Revenue Y1 <€100k → revisione drastica MVP scope (declass UC-003/005/008) | RSK-FIN-003 |
| 12 | **SyR-Cost-005** | Funding mix ≥60% commitment al G3 | Funding <40% commitment al G3 → verdetto Hold con re-planning 6-12 mesi | RSK-FIN-005 |
| 13 | **SyR-Cost-007** | Pricing validato con LoI PA + soglia realistica | Cluster D (e-GEOS/Planetek/Telespazio) opera servizi EO a €30-60k/anno → pricing baseline €150k non raggiungibile → revisione pricing a €60-90k base + €30-60k premium | RSK-MKT-001 |
| 14 | **SsR-AERO-005** | Margine flutter ≥30% velocità crociera tutto envelope | Aeroelastic analysis nonlineare mostra flutter <20% margin → re-design layup/AR + slip Phase B 6-12 mesi | RSK-TEC-002 |
| 15 | **SsR-PROP-003** | Batterie LiS/SS pack ≥350 Wh/kg TRL ≥5 nel 2027-28 | Mercato batterie 2027 non offre pack >300 Wh/kg → seasonal-only fallback mandatory + Plan A | RSK-TEC-001 |
| 16 | **SsR-AVI-001** | Autopilot 6A TRL ≥8 con DAL-C minimo FCS | Vendor non garantisce DAL-C certification (commercial COTS limitati) → re-spec autopilot custom + slip 9-12 mesi | - |
| 17 | **SsR-AVI-004** | FCS DAL-C completo + triple-channel redundancy Phase B | DO-178C DAL-C verification effort >18 mesi/3 FTE → schedule slip Phase B 6-12 mesi | RSK-TEC-003 |
| 18 | **NegR-B-001 (Critical)** | NON vendere velivoli (service-only) | Firma contratto/MoU/LoI di vendita asset (anche €1, anche prototipale) → re-baseline immediato business model + revisione B1 + comunicazione formale Coopfond | RSK-FIN-002 |
| 19 | **NegR-Geo-001 (Critical)** | NON cloud US default per imagery EO/dati C2/dati personali UE | Imagery EO o dati UE in datacenter US (AWS, Azure, GCP us-east-1) senza accordo + DPIA → violazione GDPR + NIS2 + Schrems II + migrazione obbligatoria 30 giorni a cloud EU + notifica Garante | RSK-REG-021 |
| 20 | **NegR-Mkt-001 (Critical)** | NON usare "alternativa Starlink" pubblico | Linguaggio "alternativa Starlink" / "Starlink europeo" appare in sito web / press release / pitch deck / social → rimozione 7 giorni + statement correttivo + retraining team comms | - |

> **Nota critica**: Tutti i 20 requisiti sopra elencati hanno **falsifying observation operativa** in stile "trigger osservabile + remediation". 9 sono SyR principali (incluso 2 di Compliance), 3 sono SsR architetturali, 3 sono NegR Critical (boundary). I requisiti Cost-001/002/004/008/010 sono importanti ma derivati da assumptions (AS-001 → AS-010 del Cap.3.9.1) — la loro falsifying observation è in larga parte uguale alla invalidazione dell'assumption sottostante.

---

## 5. Open Gaps — Orphan, Untestable, Unallocated

### 5.1 Orphan StNeeds (0 al v1.0)

Tutti i 28 StNeed hanno almeno un SyR figlio. Coverage 100%.

### 5.2 Orphan SyR (0 al v1.0)

Tutti i 65 SyR hanno almeno un parent legittimo (StNeed o SyR padre o Boundary B1/B2 o capitolo del Cap. 5/7/8 di riferimento o bando Cooding). Nota: SyR derivati gerarchicamente da altri SyR (es. SyR-S-005 da SyR-F-002) sono legittimi per la regola NASA SE §4.2.2 di derivazione e non sono considerati orphan.

### 5.3 Untestable SyR (0 al v1.0)

Tutti i 65 SyR hanno un metodo V&V definito (I/A/D/T o combinazione). Coverage 100%.

### 5.4 Unallocated SyR (12 SyR decomponibili senza SsR)

Action item M+5-6 per portare la coverage SyR→SsR da 72% a ≥80% (target G2):

| Req-ID | Famiglia | Sottosistema target decomposizione | Owner |
|---|---|---|---|
| SyR-F-006 | F | PAY (IR notturno) + COMMS (telemedicina) | aerospace-SE |
| SyR-F-009 | F | PAY (EO multi-stagionale) | aerospace-SE |
| SyR-F-010 | F | PAY (gNB 5G NR-NTN, già SsR-PAY-004) — formalizzare link | telecom-ntn-payload-expert |
| SyR-P-002 | P | AERO (cruise + powertrain) | vtol-uas-specialist |
| SyR-P-011 | P | AERO (MTOW 6A, già SsR-AERO-007) — formalizzare link | vtol-uas-specialist |
| SyR-O-007 | O | AVI (ConOps + ENAV LoA) | avionics-gnc-engineer |
| SyR-O-008 | O | AERO + PROP (maintenance program) | vtol-uas-specialist |
| SyR-S-005 | S | AVI (failure rate FTA + FCS DAL-C) | avionics-gnc-engineer |
| SyR-S-008 | S | GS (hangar ATEX) + PROP (BMS) — già SsR-GS-011/SsR-PROP-008 — formalizzare link | esg-sustainability-officer |
| SyR-E-004 | E | (cross-cutting, LCA non si decompone per sottosistema) — accettato senza SsR | esg-sustainability-officer |
| SyR-E-005 | E | (cross-cutting, EOL plan non si decompone per sottosistema) — accettato senza SsR | esg-sustainability-officer |
| SyR-P-010 | P | COMMS (già SsR-COMMS-001/002) — formalizzare link | telecom-ntn-payload-expert |

**Stima effort**: 8-12 ore engineer + 1 review collettiva systems engineering → coverage target 80% raggiungibile entro M+5.

### 5.5 NegR Audit Status

- 15/15 NegR Active al M+3 (5 Critical + 7 High + 3 altri).
- 0 violazioni rilevate al M+3.
- 0 waiver formali concessi.
- Prossimo audit semestrale: M+9 (pre-G3 M+10/M+11).

### 5.6 Nuovo requisito da integrare v1.5 — REQ-NF-AMB-01 (proposto da A.12 VIA v2.0)

Il refinement Allegato A.12 VIA preliminare v2.0 (subagent batch 2 M+3) ha identificato un **nuovo requisito non-funzionale ambientale** da integrare al RTM v1.5 M+6:

| Req-ID | Tipo | Statement | Confidence | Verification | Parent | Riferimento |
|---|---|---|---|---|---|---|
| **REQ-NF-AMB-01** | Non-Functional / Environmental | Le operazioni di volo VTOL del Percorso 6A devono rispettare i vincoli ambientali del Parco Naturale Regionale dell'Antola (L.R. Liguria 12/1995) e della Rete Natura 2000 SIC/ZSC/ZPS IT1331402, includendo: (a) buffer 500 m da nidi specie Allegato I Direttiva Uccelli noti, (b) quota minima 200 m AGL su SIC (vs minimo regolamentare 120 m), (c) restrizione operativa marzo-luglio in zone di nidificazione, (d) monitoraggio acustico in 3 punti rappresentativi Y1. | medium (richiede mappa nidi Ente Parco Antola M+6) | VR-AMB-01 (audit ambientale M+12 con Ente Parco + ARPAL) + VR-AMB-02 (rilievo bioacustico M+10 baseline + M+12 monitoring) | StNeed-XXX (nuovo "rispetto vincoli ambientali Parco Antola") da formalizzare workshop M+6 + Boundary B1 (cooperative + territorio) | A.12 VIA v2.0 §A.12.6 mitigazioni + §A.12.5 RSK-AMB linkage |

**Action item RTM v1.5 (M+6)**:
- Aggiungere REQ-NF-AMB-01 a sheet `SyR` (sezione "Non-Functional / Environmental" nuova) → diventa SyR-NF-AMB-001 (numerazione standard)
- Aggiungere nuovo StNeed "rispetto vincoli Parco Antola + Natura 2000" da workshop M+6 con Ente Parco Antola (parent legittimo del nuovo SyR)
- Aggiungere VR-AMB-01 + VR-AMB-02 a sheet `VR` (audit + monitoring acustico)
- Update coverage matrix: nuovo SyR-NF-AMB-001 deve avere 1+ SsR (es. SsR-OPS-XXX: mission planner deve includere geofence Parco + buffer nidi; SsR-AVI-XXX: FCS deve enforce quota min 200 m AGL su SIC)
- Update statistiche v1.5: StNeed 28→29, SyR 65→66, NegR potenziale +1 ("NO sorvolo nidi avifauna in marzo-luglio")

---

## 6. Versioning Roadmap

| Versione | Milestone | Contenuto target | Owner |
|---|---|---|---|
| **v0.5** | M+3 (Cap. 3 baseline) | 17 StNeed + 42 SyR + ~80 SsR campione + 14 NegR | aerospace-SE |
| **v1.0** (presente) | M+3 estesa | 28 StNeed + 65 SyR + 81 SsR + 22 IR + 15 NegR + 68 VR (279 totali) — coverage 100% StNeed→SyR, 100% SyR→VR, 0 orphan, 0 untestable | aerospace-SE |
| **v1.5** | M+6 (G2 Architecture Baselined) | Workshop stakeholder structured + pre-application ENAC + 30% expansion + chiusura OQ-001/006/007 + **integrazione REQ-NF-AMB-01 (A.12 VIA v2.0) + StNeed Ente Parco Antola + VR-AMB-01/02 + chiusura 24 GAP residui A.4/A.11/A.12** → +10-15 SsR, refresh confidence levels, status update VR | aerospace-SE + tech-leads + ambientalista |
| **v2.0** | M+10/M+11 (G3 FEASIBILITY GATE PRIMARIO) | RTM congelata baseline Operations Manual + SORA application + Quadro Economico + Feasibility verdict — ≥95% coverage SyR→SsR, ≥100% coverage SyR→VR, 0 untestable, 0 orphan | systems engineering board |
| **v2.5** | M+12 (G4 fine pilota VTOL) | Update post-pilot Y1 + lessons learned + revisione SyR-Cost-003 (revenue effettivo) + risk reassessment | aerospace-SE + ops |
| **v3.0** | M+24 (G5 evaluation Phase B HALE) | Phase B HALE expansion + EASA Special Condition baseline + consortium EU formalizzato + SyR-F-005/P-005/P-006 revisione (energy balance simulation completa) | aerospace-SE + 6B tech-leads |
| **v3.5** | M+36 (G6 HALE Phase B Midterm) | Prototipo subscale 1:3 + TRL 5 subsystems critici + ENAV procedure FL400+ + EASA Special Condition aperta | aerospace-SE + 6B tech-leads + EASA RMT engagement |

---

## 7. Convenzioni d'uso del file `RTM-v1.0.xlsx`

### Sheet structure

| # | Sheet | Contenuto | Righe |
|---|---|---|---|
| 1 | Cover | Versione, data, boundary conditions, metodologia, statistiche, criteri G3 | 65 |
| 2 | StNeeds | 28 Stakeholder Needs estesi | 28 + header |
| 3 | SyR | 65 System Requirements in 7 famiglie | 65 + header |
| 4 | SsR_AERO | 16 Subsystem Requirements Aerodinamica & Strutture | 16 + header |
| 5 | SsR_PROP | 13 Subsystem Requirements Propulsione & Energia | 13 + header |
| 6 | SsR_AVI | 17 Subsystem Requirements Avionica & GNC | 17 + header |
| 7 | SsR_PAY | 13 Subsystem Requirements Payload | 13 + header |
| 8 | SsR_COMMS | 11 Subsystem Requirements Comunicazioni | 11 + header |
| 9 | SsR_GS | 11 Subsystem Requirements Ground Segment | 11 + header |
| 10 | IR | 22 Interface Requirements | 22 + header |
| 11 | NegR | 15 Negative Requirements (5 Critical + 7 High + 3 Medium-Low) | 15 + header |
| 12 | VR | 68 Verification Requirements (V&V plan per ogni SyR) | 68 + header |
| 13 | Coverage_Matrix | Matrice tracciabilità StNeed → SyR (mapping completo) | 28 + header |
| 14 | Gap_Analysis | Riepilogo gap: orphan, untestable, unallocated, coverage % | 9 + header |

### Column schema (sheet 2-12)

15 colonne standard secondo schema della skill `requirements-traceability-matrix`:

```
ID | Description | Rationale | Source | Type | Parent | Owner_agent | Priority |
VV_Method | VV_Status | Phase | Trade_Study | Risk | Confidence | Falsifying_Observation
```

### Color coding

- **Header**: blu navy (#1F4E78)
- **StNeed**: verde chiaro (#C6E0B4)
- **SyR**: azzurro (#BDD7EE)
- **SsR**: giallo chiaro (#FFF2CC)
- **IR**: arancio chiaro (#FCE4D6)
- **NegR**: pesca/warning (#F8CBAD)
- **VR**: verde pallido (#E2EFDA)
- **Confidence overlay**: high=verde, medium=ambra, low=rosso, boundary=blu

### CSV export (RTM-v1.0-full.csv)

Esportazione piatta di tutti i 279 record con encoding UTF-8 + quote-all per facile import in:
- IBM DOORS / DOORS Next
- Jama Connect
- Polarion ALM
- Siemens Capital Architect
- LDRA, Cradle, Rational, qualunque tool RTM con import CSV

---

## 8. Note di chiusura del report

La RTM v1.0 rappresenta la **baseline estesa M+3** dello Studio di Fattibilità HALE/VTOL. Le statistiche di coverage attestano:
- Coverage StNeed → SyR: **100%** (target G3: 100%)  — passing
- Coverage SyR → SsR (decomponibili): **72%** (target G2: 80%, G3: ≥95%) — sotto soglia G2, action plan M+5-6
- Coverage SyR → VR: **100%** (target G3: 100%) — passing
- Orphan: **0** — passing
- Untestable: **0** (target G3: 0) — passing
- NegR Active: **15/15** + 0 violazioni — passing

**Prossimi step critici** (in ordine di priorità):

1. **Workshop stakeholder strutturati M+3-6** (cooperative + Regione + PC + Comune + ASL3) per validare i 28 StNeed + raccolta needs aggiuntivi (target +5-10 needs) → RTM v1.5.
2. **Pre-application meeting ENAC M+3-6** per validare SyR-F-002 (SAIL Pentema) e SyR-C-001/002 (SORA application Amendment 3) → falsifying observation per gate G2.
3. **Decomposizione SsR M+5-6** per i 12 SyR unallocated (Section 5.4) → coverage target 80% per G2.
4. **Trade Study chiusi M+6 → M+12** (TS-PLATFORM-6A, TS-AVI-6A, TS-PAYLOAD-EO, TS-MATERIAL, TS-PROP-6B) → chiusura OQ-001/003/005/006/007 → update SyR/SsR confidence levels.
5. **Risk Register v2 (Vol. 2 Allegato A.2)** in coerenza con i Risk linkati nei requisiti (RSK-TEC-001/002/003, RSK-REG-002/016/019/021/027/030, RSK-FIN-001/002/003/005, RSK-OPS-001/002, RSK-SUP-001).
6. **Audit semestrale NegR M+9** prima del G3 → verifica 0 violazioni + waiver log up-to-date.
7. **V&V Plan dettagliato per VR Open → Planned** → 22 VR ancora in stato "Open" da pianificare con data + risorse + budget allocato.

**Action item documentale**:
- Allegato A.1 (questo file) deve essere pubblicato in Vol. 2 dello Studio entro M+10/M+11 (G3).
- File `RTM-v1.0.xlsx` esistente in `/studio-di-fattibilita/allegati/A1-RTM/` è il **single source of truth** della RTM dello Studio.
- Aggiornamento RTM v1.5 M+6: rigenerare via `build_rtm.py` con dati aggiornati (workflow riproducibile + git versioned).

**Disclaimer epistemico** (skill `epistemic-rigor`): la presente RTM v1.0 è una baseline tecnica **provvisoria al M+3**. La confidence aggregata è **medium** (con singoli requisiti high/medium/low/boundary esplicitati). Il documento NON è validato da ente terzo (RINA, DNV); validazione raccomandata per uso "investment-grade" prima del G5 (M+24). I numeri di performance vendor-driven (es. JOUAV CW-30E autonomia 4h) sono **input di progetto**, NON claim di marketing, e attendono triangulation via reference call con almeno 2 operatori EU (DR-003 dell'audit-rigore-epistemico).

---

## 9. Riferimenti

[^1]: **NASA Systems Engineering Handbook Rev 2** (NASA/SP-2016-6105 Rev 2). Source: `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md`. Specifico: §4.1, §4.2, §4.3, §5.3, §5.4, Appendix C. Confidence: high.

[^2]: **INCOSE Systems Engineering Handbook**, 5th Edition (2023). Riferimento esterno citato per coerenza VAFC + GtWR.

[^3]: **ISO/IEC/IEEE 15288:2015** "Systems and software engineering — System life cycle processes". Standard internazionale.

[^4]: **Reg. UE 2019/947** (Operations UAS). Source: `fonti/CELEX_32019R0947_IT_TXT.md`. Confidence: high.

[^5]: **EASA AMC/GM** Issue 1 Amendment 3 (SORA 2.5 europea, settembre 2025). Source: ED Decision 2025/018/R.

[^6]: **Cap. 3 Requisiti e RTM** baseline v0.5: `studio-di-fattibilita/cap-03-requisiti-e-RTM.md`.

[^7]: **Cap. 5 Quadro Normativo** + 15 showstopper aggiuntivi: `studio-di-fattibilita/cap-05-quadro-normativo.md` §5.16.

[^8]: **Cap. 6 Analisi tecnica** + Trade Studies: `studio-di-fattibilita/cap-06-analisi-tecnica.md` §6.3.

[^9]: **Cap. 9 Cronoprogramma e Gate**: `studio-di-fattibilita/cap-09-cronoprogramma-e-gate.md` §9.2 (Gate G0-G6 entry/exit criteria).

[^10]: **Skill `requirements-traceability-matrix`**: `.claude/skills/requirements-traceability-matrix/SKILL.md` — workflow di costruzione applicato.

[^11]: **Skill `epistemic-rigor`**: `.claude/skills/epistemic-rigor/SKILL.md` — disciplina di falsifiability + confidence levels applicata.

[^12]: **Boundary conditions B1+B2** dichiarate in `CLAUDE.md` (project root) + `riferimenti/visione-10-anni.md` + `riferimenti/RESERVED-rischi-geopolitici.md` (riservato, access-controlled).

[^13]: Build script `/studio-di-fattibilita/allegati/A1-RTM/build_rtm.py` — riproducibilità del file `RTM-v1.0.xlsx` e CSV via `python3 build_rtm.py`.
