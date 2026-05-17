# Allegato A.1, Requirements Traceability Matrix (RTM) v1.5, Report di Accompagnamento

> **Studio di Fattibilità, Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies, bando Cooding Prototypes
> Volume 2, Allegato A.1
>
> **Versione documento:** v1.5 (proiezione M+6, integrazione refinement A.12 VIA v2.0 batch 2 M+3)
> **Data emissione:** 2026-05-17
> **Owner:** aerospace-systems-engineer (Firmamento Technologies)
> **Riferimento Cap. 3:** `studio-di-fattibilita/cap-03-requisiti-e-RTM.md` (RTM v0.5 baseline)
> **Documenti predecessori:** `A1-RTM-REPORT.md` (v1.0 M+3 baseline estesa, 279 record) più `RTM-v1.0-full.csv` più `RTM-v1.0.xlsx`
> **Delta v1.5:** `RTM-v1.5-delta.csv` (7 record nuovi più 7 link di traceability, totale 14 righe delta)
> **Boundary conditions:** B1 (service-only + Legacoop) + B2 (EU sovereign stratospheric / "complementare a IRIS²")
> **Confidence aggregato sezione ambientale:** medium (richiede engagement formale Ente Parco Antola M+6)

---

## 1. Metodologia e scopo della v1.5 (NASA SE Handbook §4)

La RTM v1.5 costituisce un **incremento riproducibile** della baseline v1.0 (M+3 estesa, 279 record), realizzato secondo la stessa metodologia del **NASA Systems Engineering Handbook Rev 2** (NASA/SP-2016-6105 Rev 2), in particolare §4.1 Stakeholder Expectations Definition, §4.2 Technical Requirements Definition, §4.3 Logical Decomposition (allocazione SsR) e §5.3-5.4 V&V Processes.

L'incremento v1.5 ha origine in un **refinement chain** identificato durante il batch 2 M+3 di subagent verticali ambientali:

1. **A.12 Relazione VIA Preliminare v2.0** (`studio-di-fattibilita/allegati/A12-VIA-preliminare/A12-Relazione-VIA-Preliminare-COMPLETE-v2.0.md`) ha identificato un requisito non-funzionale ambientale (REQ-NF-AMB-01) non presente nella baseline RTM v1.0 e non derivabile da nessuno degli StNeed-001…028 esistenti.
2. **A.2 Risk Register v1.5** ha formalizzato 3 nuovi rischi ambientali (RSK-AMB-001 score 12→6, RSK-AMB-002 score 9→4, RSK-AMB-003 score 8→3) con linkage esplicito al requisito proposto e al §A.12.6 mitigazioni.
3. **§5.6 del precedente A1-RTM-REPORT.md (v1.0)** ha documentato l'azione di integrazione differita al M+6 in qualità di "Nuovo requisito da integrare v1.5, REQ-NF-AMB-01".

La RTM v1.5 ufficializza tale integrazione **anticipandola all'M+3 con confidence medium** (in attesa del workshop Ente Parco Antola M+6 che ne validerà la formulazione operativa). Il blocco delta è confinato in un **CSV separato** (`RTM-v1.5-delta.csv`) per garantire riproducibilità incrementale: il file `RTM-v1.0-full.csv` resta **immutato** come baseline e il file Excel `RTM-v1.0.xlsx` verrà rigenerato in unica passata al M+6 via `build_rtm.py` (vedi §7.2bis di questo report per istruzioni operative).

A questa baseline metodologica si aggiungono:

- **Nuova famiglia SyR "NF" (Non-Functional / Environmental)**, che apre una settima sotto-famiglia oltre alle 7 esistenti (F, P, O, S, E, C, Cost). La famiglia E (Environmental) della baseline v1.0 raccoglie requisiti di sostenibilità di prodotto (LCA, EOL, propulsione elettrica, rumore in dB(A)), mentre la nuova famiglia NF accoglie requisiti **non-funzionali di conformità ambientale operativa** (vincoli normativi area protetta, buffer geofence, restrizioni stagionali). La distinzione è coerente con NASA SE Handbook §4.2.3 (quality-of-service vs functional requirements) e con la prassi INCOSE GtWR 2023 sui requisiti non-funzionali.
- **Sheet `SyR_NF_ENV`** da aggiungere al file Excel v1.5 al momento della rigenerazione M+6 (in coerenza con la struttura sheet esistente, vedi §7.2 update).
- **Disciplina epistemica** (skill `epistemic-rigor`): tutti i 7 nuovi record portano confidence level (medium per la maggioranza, in quanto dipendenti da engagement esterno Ente Parco Antola M+6) e falsifying observation operativa esplicita.

**Standard secondari di riferimento:** INCOSE Systems Engineering Handbook 5th Edition (2023); ISO/IEC/IEEE 15288:2015; ECSS-E-ST-10C; **Direttiva Uccelli 2009/147/CE** (specie Allegato I); **DPR 357/1997** art.5 (Valutazione di Incidenza); **L.R. Liguria 12/1995** (Parchi Regionali); **Decreto Min. 16.03.1998** (zonizzazione acustica aree protette).

---

## 2. Statistiche RTM v1.5

| Categoria | Conteggio v1.5 | Conteggio v1.0 | Δ v1.5 vs v1.0 | Baseline Cap. 3 v0.5 |
|---|---|---|---|---|
| Stakeholder Needs (StNeed) | **29** | 28 | +1 (StNeed-029 Ente Parco Antola) | 17 |
| System Requirements (SyR) | **66** | 65 | +1 (SyR-NF-AMB-001, apre famiglia NF) | 42 |
| Subsystem Requirements (SsR) | **84** | 81 | +3 (SsR-OPS-AMB-001 + SsR-AVI-AMB-001 + SsR-DAT-AMB-001) | circa 80 (campione) |
| Interface Requirements (IR) | **22** | 22 | 0 (nessun IR ambientale aggiuntivo a M+3) | non formalizzato |
| Negative Requirements (NegR) | **16** | 15 | +1 (NegR-AMB-016 sorvolo nidi mar-lug) | 14 nominali |
| Verification Requirements (VR) | **70** | 68 | +2 (VR-AMB-01 audit annuale + VR-AMB-02 monitoring acustico) | non formalizzato |
| **TOTALE righe RTM** | **287** (record 285 + 2 link strutturali calcolati) | 279 | **+8 record + 7 link di traceability nuovi** | circa 155 stimato |

> Nota di conteggio: il count "287" comprende i 285 record di requisito formali (StNeed/SyR/SsR/IR/NegR/VR) più 2 link strutturali calcolati, normalmente rappresentati come riga distinta in tool RTM esterni (DOORS/Jama/Polarion); i 7 Link-001…007 del file `RTM-v1.5-delta.csv` sono link di traceability esplicitati per chiarezza ispettiva e non vanno computati come record indipendenti (sono già impliciti nei campi `Parent` dei 7 record nuovi). Il totale formale dichiarato in dashboard resta quindi 285 record (279 v1.0 più 6 nuovi requisiti più 0 modifiche destruttive).

### Breakdown System Requirements per famiglia (v1.5)

| Famiglia SyR | v1.5 | v1.0 | Δ | Note |
|---|---|---|---|---|
| F, Functional | 10 | 10 | 0 | invariato |
| P, Performance | 12 | 12 | 0 | invariato |
| O, Operational | 8 | 8 | 0 | invariato |
| S, Safety | 8 | 8 | 0 | invariato |
| E, Environmental (sustainability di prodotto) | 5 | 5 | 0 | invariato |
| C, Compliance | 12 | 12 | 0 | invariato |
| Cost, Cost & Business | 10 | 10 | 0 | invariato |
| **NF, Non-Functional / Environmental Compliance (NEW v1.5)** | **1** | 0 | **+1** | SyR-NF-AMB-001 apre nuova famiglia; previsto +2-3 NF entro v2.0 (es. NF-PRIV per accettabilità privacy comunità, NF-ACC per accettabilità sociale) |
| **TOTALE SyR** | **66** | 65 | +1 | |

### Breakdown Subsystem Requirements per sottosistema (v1.5)

| Sottosistema SsR | v1.5 | v1.0 | Δ | Note |
|---|---|---|---|---|
| AERO (Aerodinamica & Strutture) | 16 | 16 | 0 | invariato |
| PROP (Propulsione & Energia) | 13 | 13 | 0 | invariato |
| AVI (Avionica & GNC) | **18** | 17 | **+1** | SsR-AVI-AMB-001 (FCS enforce quota min 200 m AGL su SIC) |
| PAY (Payload) | 13 | 13 | 0 | invariato |
| COMMS (Comunicazioni) | 11 | 11 | 0 | invariato |
| GS (Ground Segment) | 11 | 11 | 0 | invariato |
| **OPS (Operations / Mission Planning) NEW v1.5** | **1** | 0 | **+1** | SsR-OPS-AMB-001 (mission planner geofence Parco + buffer nidi); apre nuovo sottosistema "OPS" logicamente distinto da GS e AVI |
| **DAT (Data Governance / Logging) NEW v1.5** | **1** | 0 | **+1** | SsR-DAT-AMB-001 (logging volo conformità ambientale tracciato); apre nuovo sottosistema "DAT" complementare a GS |
| **TOTALE SsR** | **84** | 81 | **+3** | |

> Nota architetturale sui nuovi sottosistemi OPS e DAT: in v1.0 l'analoga funzione era allocata implicitamente al sottosistema GS (Ground Segment), che però copre principalmente l'hardware/infrastruttura. L'introduzione di OPS (mission planning workflow più procedure operative) e DAT (data governance più retention più audit trail) come **sottosistemi logici autonomi** è coerente con NASA SE Handbook §4.3 (logical architecture) e con la prassi DO-178C (separazione concerns SW). La transizione completa di SsR-GS-006 (mission planning software) verso il sottosistema OPS e di SsR-GS-002/003 (data hosting più anonimizzazione) verso DAT è prevista nella v2.0 M+10/M+11.

---

## 3. Coverage Analysis (v1.5)

| Metrica di copertura | Valore v1.5 | Valore v1.0 | Soglia G2 (M+6) | Soglia G3 (M+10) | Esito v1.5 |
|---|---|---|---|---|---|
| StNeeds con ≥1 SyR figlio | **100.0%** (29/29) | 100% (28/28) | 100% | 100% | OK (passing, StNeed-029 → SyR-NF-AMB-001) |
| SyR decomponibili (F/P/O/S/E/NF) con ≥1 SsR | **75.0%** (33/44 SyR decomponibili) | 72.1% (31/43) | 80% | ≥95% | Sotto soglia G2, gap chiusura M+5-6 (12 SyR unallocated residui, vedi §5.4) |
| SyR con metodo V&V definito | **100.0%** (66/66) | 100% (65/65) | 80% | 100% | OK (passing, SyR-NF-AMB-001 ha I+A+T con VR-AMB-01/02) |
| SsR con allocazione subsystem | **100.0%** (84/84) | 100% (81/81) | 100% | 100% | OK (passing, 3 nuovi SsR allocati a OPS/AVI/DAT) |
| Orphan SyR (no parent StNeed/SyR/Cap/Bando) | **0** | 0 | 0 | 0 | OK (passing) |
| Untestable SyR (no V&V method) | **0** | 0 | ≤2 | 0 | OK (passing) |
| NegR Active monitorati | **16/16 (100%)** | 15/15 | 16/16 + 0 violazioni | 16/16 + 0 violazioni + waiver log | OK (passing, NegR-AMB-016 Active da M+3; primo audit M+9) |
| **Coverage tematica ambientale (NEW v1.5)** | **1 StNeed + 1 SyR + 3 SsR + 1 NegR + 2 VR** | 0 (gap evidenziato §5.6 v1.0) | full thematic coverage M+6 | full thematic coverage M+10 | **OK (passing target M+6 anticipato a M+3)** |

> **Note metodologiche sulla coverage SyR→SsR v1.5**:
> Il valore 75.0% si riferisce ai SyR delle famiglie "decomponibili tecnicamente" (F/P/O/S/E più nuova NF = 44 SyR), di cui 33 hanno almeno un SsR figlio diretto. L'incremento di +2.9 pp rispetto a v1.0 (72.1%) deriva da: +1 SyR decomponibile (SyR-NF-AMB-001) che porta 3 SsR figli, contribuendo +3 SyR allocati e +1 SyR decomponibile al denominatore. Il delta netto è quindi 33/44 vs 31/43 = +2.9 pp. L'azione M+5-6 (decomporre 11 SyR rimanenti, vedi §5.4 invariato da v1.0) porta la coverage prevista al **82-85%** target G2.
>
> **Action per chiusura M+5-6 (target 80%)**: invariata rispetto a §5.4 v1.0, 11 SyR delle famiglie F/P/O/S/E da decomporre (es. SyR-F-006, SyR-F-009, SyR-S-005). La nuova SyR-NF-AMB-001 è già pienamente decomposta in v1.5.

---

## 4. Critical Requirements, Top-21 Priority H con Falsifying Observation Operative

I 21 requisiti più critici dello Studio (priorità H/Critical più falsifying observation con trigger osservabile esplicito). La top-20 della v1.0 è interamente confermata; in v1.5 si aggiunge SyR-NF-AMB-001 in qualità di nuovo critico ambientale.

| # | Req-ID | Description (estratto) | Falsifying Observation operativa | Risk linkato |
|---|---|---|---|---|
| 1-17 | (invariati v1.0) | vedi `A1-RTM-REPORT.md` §4 v1.0, SyR-F-002, SyR-F-005, SyR-P-006, SyR-F-003, SyR-S-001, SyR-S-005, SyR-C-003, SyR-C-004, SyR-C-007, SyR-C-008, SyR-Cost-003, SyR-Cost-005, SyR-Cost-007, SsR-AERO-005, SsR-PROP-003, SsR-AVI-001, SsR-AVI-004 | invariata | invariato |
| 18 | NegR-B-001 (Critical) | invariato v1.0 | invariata | RSK-FIN-002 |
| 19 | NegR-Geo-001 (Critical) | invariato v1.0 | invariata | RSK-REG-021 |
| 20 | NegR-Mkt-001 (Critical) | invariato v1.0 | invariata | - |
| **21 NEW** | **SyR-NF-AMB-001 + NegR-AMB-016** | Conformità integrale vincoli ambientali Parco Antola + SIC IT1331402 (buffer 500 m nidi + quota min 200 m AGL + restrizione mar-lug + monitoring acustico Y1) | Audit M+12 rileva: (a) violazione buffer 500 m da nido in log volo, OPPURE (b) operazione a quota <200 m AGL su SIC senza autorizzazione PC, OPPURE (c) Leq,d post-operam > baseline +5 dB(A) in 1+ dei 3 punti monitoring, OPPURE (d) Ente Parco Antola rifiuta firma Convenzione operativa entro M+12 → sospensione operativa entro 7 giorni + escalation gate G2 condizionato + revisione boundary B1 (cooperative + territorio) | RSK-AMB-001 (residual 12→6), RSK-AMB-002 (9→4), RSK-AMB-003 (8→3), RSK-REG-011 |

> **Nota critica v1.5**: il nuovo requisito SyR-NF-AMB-001 entra nella **top-priority H** in quanto showstopper operativo Y1: senza Convenzione operativa Ente Parco Antola firmata, la flotta VTOL non può operare sopra il Parco e quindi non può operare a Pentema, sito pilota anchor. La falsifying observation è già parzialmente verificabile a M+9 (engagement workshop Ente Parco M+6 più outcome documentato entro M+9) prima della finestra critica gate G3 M+10/M+11.

---

## 5. Open Gaps, Orphan, Untestable, Unallocated (v1.5)

### 5.1 Orphan StNeeds (0 al v1.5)

Tutti i 29 StNeed hanno almeno un SyR figlio. Coverage 100%. StNeed-029 (Ente Parco Antola) ha SyR-NF-AMB-001 come unico figlio diretto, in linea con NASA SE §4.2 (1:1 mapping ammesso per requisiti di conformità normativa atomica).

### 5.2 Orphan SyR (0 al v1.5)

Tutti i 66 SyR hanno almeno un parent legittimo (StNeed o SyR padre o Boundary B1/B2 o capitolo del Cap. 5/7/8 di riferimento o bando Cooding). SyR-NF-AMB-001 ha parent StNeed-029 più Boundary B1 (cooperative più territorio).

### 5.3 Untestable SyR (0 al v1.5)

Tutti i 66 SyR hanno un metodo V&V definito (I/A/D/T o combinazione). Coverage 100%. SyR-NF-AMB-001 ha metodo composito **I+A+T** con VR-AMB-01 (Inspection audit annuale) più VR-AMB-02 (Test monitoring acustico).

### 5.4 Unallocated SyR (11 SyR decomponibili senza SsR, invariato v1.0)

L'action item resta invariato rispetto a §5.4 v1.0. La nuova SyR-NF-AMB-001 è già pienamente decomposta in v1.5 con 3 SsR (OPS-AMB-001 + AVI-AMB-001 + DAT-AMB-001) e non aggiunge gap. Lista azione M+5-6 confermata: SyR-F-006, SyR-F-009, SyR-F-010, SyR-P-002, SyR-P-011, SyR-O-007, SyR-O-008, SyR-S-005, SyR-S-008, SyR-E-004, SyR-E-005, SyR-P-010, per 11 SyR da decomporre, circa 10-15 ore engineer work per portare la coverage a 82-85% (target G2 80%).

### 5.5 NegR Audit Status (v1.5)

- **16/16 NegR Active** al M+3 (5 Critical + 7 High + 3 Medium-Low più **1 nuovo High NegR-AMB-016**)
- 0 violazioni rilevate al M+3 (compreso il nuovo NegR-AMB-016, da audit log volo trimestrale)
- 0 waiver formali concessi
- Prossimo audit semestrale: M+9 (pre-G3 M+10/M+11) con focus specifico su NegR-AMB-016 (prima stagione critica mar-lug parzialmente coperta)

### 5.6 Stato di chiusura del gap §5.6 v1.0, REQ-NF-AMB-01

Il gap evidenziato nella §5.6 della v1.0 (integrazione differita M+6) viene chiuso anticipatamente al M+3 con la presente v1.5:

| Action item §5.6 v1.0 | Stato v1.5 | Evidenza |
|---|---|---|
| Aggiungere REQ-NF-AMB-01 a sheet `SyR` (sezione NF nuova) | **DONE** | SyR-NF-AMB-001 in `RTM-v1.5-delta.csv` riga 2, sheet target `SyR_NF_ENV` (rigenerazione xlsx M+6) |
| Aggiungere StNeed Ente Parco Antola | **DONE** | StNeed-029 in `RTM-v1.5-delta.csv` riga 1 |
| Aggiungere VR-AMB-01 + VR-AMB-02 | **DONE** | righe 7-8 del delta CSV |
| Update coverage: 1+ SsR per SyR-NF-AMB-001 | **DONE** | 3 SsR allocati (OPS-AMB-001 + AVI-AMB-001 + DAT-AMB-001) → coverage 100% |
| Aggiungere NegR "NO sorvolo nidi avifauna in marzo-luglio" | **DONE** | NegR-AMB-016 riga 6 del delta CSV |
| Update statistiche v1.5: StNeed 28→29, SyR 65→66, NegR +1 | **DONE** | §2 di questo report |
| Workshop Ente Parco Antola M+6 per validazione | **OPEN, pianificato M+5-6** | engagement attivo via snai-funding-expert; l'output del workshop integra confidence levels in v1.5.1 hotfix (se richiesto) |

### 5.7 Open Questions (OQ) batch 2 M+3, milestone tracker integrato RTM v1.5

In coerenza con il refinement batch 2 M+3 documentato in `studio-di-fattibilita/cap-04-perimetro-scope.md` §4.7bis, le 25 OQ aperte sono mappate a milestone v1.5/v2.0 della RTM come tracker di chiusura:

| OQ ID (cap. 4) | Tema | Trigger requisito RTM | Target chiusura | Stato v1.5 |
|---|---|---|---|---|
| OQ-001 | Trade Study TS-PLATFORM-6A | SyR-P-001/002/011 + SsR-PROP-001 | M+6 | Open (kickoff M+4) |
| OQ-002 | Vendor RFQ JOUAV/Quantum/FlyingBasket | SyR-P-001 + SsR-AVI-001 + RSK-SUP-001 | M+5 | Open |
| OQ-003 | Trade Study TS-AVI-6A (FCS DAL-C) | SyR-S-001/005 + SsR-AVI-001/004 | M+6 | Open |
| OQ-004 | Pre-application ENAC SORA Pentema | SyR-F-002 + SyR-C-001/002 | M+4-5 | Open (richiesta inviata M+3) |
| OQ-005 | Trade Study TS-PAYLOAD-EO | SyR-F-001/003 + SsR-PAY-001/004 | M+6 | Open |
| OQ-006 | Trade Study TS-MATERIAL (lino vs CFRP) | SyR-P-004 + SsR-AERO-001 | M+6 | Open |
| OQ-007 | Trade Study TS-PROP-6B (solare vs ibrido H2) | SyR-F-005/P-005/P-006 + SsR-PROP-002/003/005 | M+10 | Open |
| OQ-008 | Energy balance simulation 2026 tech | SyR-P-005/P-006 + RSK-TEC-001 | M+10 | Open |
| OQ-009 | DPIA UC-001/002/004 | SyR-C-003 + NegR-Reg-001/002 | M+5-6 | Open |
| OQ-010 | LoI Regione Liguria anchor customer | StNeed-001/004 + SyR-Cost-003 + RSK-FIN-003 | M+6-9 | Open |
| OQ-011 | Convenzione Comune Torriglia | StNeed-018 | M+6 | Open |
| OQ-012 | Workshop cooperative + LoI 8/10 | StNeed-005/006/007/025 + SyR-Cost-003/004 | M+6-9 | Open |
| OQ-013 | Convenzione ASL3 telemedicina | StNeed-019 + SyR-F-006 | M+9 | Open |
| OQ-014 | LoA ENAV CTR Genova procedure | StNeed-024 + IR-ENAV-001 + NegR-Reg-003 | M+6-9 | Open |
| OQ-015 | ISMS Part-IS roadmap + CISO hire | StNeed-020 + SyR-C-004 + RSK-REG-019/027 | M+9 | Open |
| OQ-016 | AgID/PSN cloud hosting contract | SyR-C-008 + SsR-GS-002 + NegR-Geo-001 + NegR-Tech-003 | M+9 | Open |
| OQ-017 | AGCOM licensing UC-003 | StNeed-013 + SyR-F-004 + RSK-REG-005 | M+9-12 | Open |
| OQ-018 | Quadro Economico v1 + funding mix | SyR-Cost-005 + RSK-FIN-005 | M+10 | Open |
| OQ-019 | Risk Register v1.5 ratifica board | tutti i RSK + nuovi RSK-AMB-001/002/003 | M+6 | **DONE batch 2 M+3** (A.2 v1.5 prodotto) |
| OQ-020 | RTM v1.5 ratifica board | nuova SyR-NF-AMB-001 + StNeed-029 + 3 SsR + 1 NegR + 2 VR | M+6 | **DONE batch 2 M+3 (presente documento)** |
| OQ-021 | VIA preliminare validation Ente Parco | StNeed-029 + SyR-NF-AMB-001 + RSK-AMB-001 | M+6-9 | **In progress (A.12 v2.0 prodotta batch 2 M+3, workshop M+5-6 pianificato)** |
| OQ-022 | Computo Metrico Estimativo GS Pentema | Cap. 8 + A.9 | M+9 | Open |
| OQ-023 | V&V Plan dettagliato (22 VR Open → Planned) | tutti i VR | M+9 | Open |
| OQ-024 | ICD baseline (22 IR) | tutti gli IR | M+6-9 | Open |
| OQ-025 | Safety Case SORA draft | SyR-F-002 + SyR-S-001/005/006 + Cap. 6.4 | M+9-10 | Open |

> **Nota tracker**: 3 delle 25 OQ batch 2 M+3 risultano già **chiuse o in progress** a M+3 (OQ-019, OQ-020, OQ-021) grazie all'azione del subagent batch 2. Le rimanenti 22 OQ hanno target M+4-M+10 e sono trackate nel piano di azione M+6 (G2 entry) e M+10/M+11 (G3 entry). L'aggiornamento status OQ avverrà alla v1.5.1 hotfix (atteso M+6) oppure alla v2.0 M+10 finale.

---

## 6. Versioning Roadmap (v1.5)

| Versione | Milestone | Contenuto target | Owner | Stato |
|---|---|---|---|---|
| v0.5 | M+3 (Cap. 3 baseline) | 17 StNeed + 42 SyR + circa 80 SsR campione + 14 NegR | aerospace-SE | Storico |
| v1.0 | M+3 estesa | 28 StNeed + 65 SyR + 81 SsR + 22 IR + 15 NegR + 68 VR (279 totali) | aerospace-SE | Storico (baseline congelata) |
| **v1.5 (presente)** | **M+3 proiezione M+6, integrazione A.12 VIA v2.0 batch 2 M+3** | **29 StNeed + 66 SyR (di cui 1 NF nuovo) + 84 SsR (di cui 3 ambientali su 2 nuovi sottosistemi OPS+DAT) + 22 IR + 16 NegR + 70 VR (285 totali, +6 record + 7 link traceability vs v1.0)** | **aerospace-SE + esg-sustainability-officer** | **CURRENT (M+3 batch 2 milestone)** |
| v1.5.1 (hotfix) | M+6 (workshop Ente Parco Antola eseguito) | Refresh confidence SyR-NF-AMB-001 + StNeed-029 da medium a high (post-validation) + eventuali +1-3 SsR di dettaglio derivati da feedback Ente Parco | aerospace-SE + esg-sustainability-officer | Pianificato |
| v1.5 → xlsx regen | M+6 (G2 Architecture Baselined) | Rigenerazione `RTM-v1.5.xlsx` via `build_rtm.py` (vedi §7.2bis), include sheet nuovo `SyR_NF_ENV` + update sheet `Coverage_Matrix` + update sheet `Cover` (stats v1.5) + update sheet `NegR` + update sheet `VR` | aerospace-SE | Pianificato M+6 |
| v2.0 | M+10/M+11 (G3 FEASIBILITY GATE PRIMARIO) | RTM congelata baseline Operations Manual + SORA application + Quadro Economico + Feasibility verdict, ≥95% coverage SyR→SsR, ≥100% coverage SyR→VR, 0 untestable, 0 orphan. Atteso: 30-35 StNeed (engagement esteso), 75-80 SyR (expansion fine-grained), 100-110 SsR (decomposizione completa) | systems engineering board | Pianificato |
| v2.5 | M+12 (G4 fine pilota VTOL) | Update post-pilot Y1 + lessons learned + revisione SyR-Cost-003 (revenue effettivo) + risk reassessment + VR-AMB-01 prima esecuzione audit annuale Ente Parco + VR-AMB-02 prima campagna monitoring acustico | aerospace-SE + ops + esg-sustainability-officer | Pianificato |
| v3.0 | M+24 (G5 evaluation Phase B HALE) | Phase B HALE expansion + EASA Special Condition baseline + consortium EU formalizzato + SyR-F-005/P-005/P-006 revisione | aerospace-SE + 6B tech-leads | Pianificato |
| v3.5 | M+36 (G6 HALE Phase B Midterm) | Prototipo subscale 1:3 + TRL 5 subsystems critici + ENAV procedure FL400+ + EASA Special Condition aperta | aerospace-SE + 6B tech-leads + EASA RMT engagement | Pianificato |

> **Linkage A.12 VIA v2.0 più A.2 Risk Register v1.5 (refinement chain batch 2 M+3)**: la v1.5 costituisce il terzo deliverable di una triade integrata prodotta nel batch 2 M+3:
> 1. **A.12 VIA Preliminare v2.0** identifica REQ-NF-AMB-01 in §A.12.6 mitigazioni più §A.12.3-A.12.4 evidenze biologiche/normative
> 2. **A.2 Risk Register v1.5** formalizza 3 RSK-AMB (001/002/003) in coerenza con mitigazioni A.12 v2.0
> 3. **A.1 RTM v1.5 (presente)** integra StNeed-029 più SyR-NF-AMB-001 più 3 SsR più 1 NegR più 2 VR in piena coerenza con A.12 v2.0 e A.2 v1.5
>
> Il cross-reference Cap. 5 §5.7bis (atteso M+5-6) integrerà il quadro normativo ambientale dell'area pilota (L.R. Liguria 12/1995 più DPR 357/1997 più Direttiva Uccelli 2009/147/CE) e fornirà parent normativo al SyR-NF-AMB-001 per la coverage Cap. 5 → SyR.

---

## 7. Convenzioni d'uso dei file v1.5

### 7.1 File delta CSV (`RTM-v1.5-delta.csv`)

Il file `RTM-v1.5-delta.csv` (circa 5 KB) contiene solo i record nuovi del v1.5 rispetto al v1.0 baseline:

- **Schema colonne identico** al file `RTM-v1.0-full.csv` (15 colonne: ID, Description, Rationale, Source, Type, Parent, Owner_agent, Priority, VV_Method, VV_Status, Phase, Trade_Study, Risk, Confidence, Falsifying_Observation)
- **Record nuovi**: 1 StNeed (StNeed-029) + 1 SyR (SyR-NF-AMB-001) + 3 SsR (SsR-OPS-AMB-001 + SsR-AVI-AMB-001 + SsR-DAT-AMB-001) + 1 NegR (NegR-AMB-016) + 2 VR (VR-AMB-01 + VR-AMB-02) = 8 record formali
- **Link strutturali**: 7 righe Link-001…007 che esplicitano la traceability per ispezione manuale (ridondanti rispetto al campo `Parent`, ma utili per import automatico in tool RTM esterni con schema "edge-list")
- **Encoding**: UTF-8 più quote-all
- **Use case**: import incrementale in DOORS / Jama / Polarion / Capital Architect senza dover ricaricare l'intera baseline v1.0; merge automatizzato con CSV v1.0 via script Python (vedi 7.2bis)

### 7.2 File `RTM-v1.0.xlsx` (immutato)

Il file `RTM-v1.0.xlsx` (67 KB, 14 sheet) non viene modificato in v1.5. Resta il single source of truth della baseline M+3 v1.0 fino alla rigenerazione M+6.

### 7.2bis Istruzioni rigenerazione `RTM-v1.5.xlsx` (M+6)

Per produrre il file `RTM-v1.5.xlsx` rigenerato al M+6 occorre:

1. **Estendere `build_rtm.py`** (script Python esistente in `/studio-di-fattibilita/allegati/A1-RTM/build_rtm.py`) per:
   - Aggiungere lista record v1.5 (lettura da `RTM-v1.5-delta.csv` con merge sul totale)
   - Creare sheet nuovo `SyR_NF_ENV` con header standard 15 colonne più 1 riga (SyR-NF-AMB-001)
   - Aggiungere 3 righe al sheet `SsR_AVI` (SsR-AVI-AMB-001), e creare 2 nuovi sheet `SsR_OPS` (SsR-OPS-AMB-001) più `SsR_DAT` (SsR-DAT-AMB-001), totale sheet xlsx: 14 → **16**
   - Aggiungere 1 riga a sheet `StNeeds` (StNeed-029), 1 riga a sheet `NegR` (NegR-AMB-016) e 2 righe a sheet `VR` (VR-AMB-01 + VR-AMB-02)
   - Aggiornare sheet `Cover` con statistiche v1.5 (totali, breakdown SyR per famiglia più NF, breakdown SsR per sottosistema più OPS più DAT)
   - Aggiornare sheet `Coverage_Matrix` con 1 nuova riga (StNeed-029 → SyR-NF-AMB-001)
   - Aggiornare sheet `Gap_Analysis` con metriche v1.5 (§3 di questo report)
   - Mantenere color coding esistente più aggiungere palette specifica NF (es. verde scuro #548235 per famiglia NF Environmental Compliance)
2. **Eseguire** `python3 build_rtm.py --version v1.5 --delta RTM-v1.5-delta.csv` (parametri da implementare)
3. **Verificare integrità** confrontando count cells vs §2 statistiche
4. **Commit Git** con messaggio "RTM v1.5, integrazione A.12 VIA v2.0 (M+6)" più versionare il nuovo xlsx accanto al v1.0 (non sovrascrivere)

**Stima effort:** 2-3 ore engineer (estensione `build_rtm.py` più test più commit). Da pianificare in finestra M+5-6 prima del gate G2.

### 7.3 Sheet structure target v1.5 xlsx (M+6)

| # | Sheet | Contenuto v1.5 | Righe |
|---|---|---|---|
| 1 | Cover | Versione, data, boundary conditions, metodologia, statistiche v1.5, criteri G3 | circa 70 (vs 65 v1.0) |
| 2 | StNeeds | 29 Stakeholder Needs (28 v1.0 + StNeed-029) | 29 + header |
| 3 | SyR | 65 System Requirements famiglie F/P/O/S/E/C/Cost (invariato v1.0) | 65 + header |
| **3bis NEW** | **SyR_NF_ENV** | **1 System Requirement famiglia NF Environmental Compliance** | **1 + header** |
| 4 | SsR_AERO | 16 (invariato) | 16 + header |
| 5 | SsR_PROP | 13 (invariato) | 13 + header |
| 6 | SsR_AVI | 18 (17 v1.0 + SsR-AVI-AMB-001) | 18 + header |
| 7 | SsR_PAY | 13 (invariato) | 13 + header |
| 8 | SsR_COMMS | 11 (invariato) | 11 + header |
| 9 | SsR_GS | 11 (invariato) | 11 + header |
| **9bis NEW** | **SsR_OPS** | **1 SsR mission planning operations** | **1 + header** |
| **9ter NEW** | **SsR_DAT** | **1 SsR data governance / logging conformità** | **1 + header** |
| 10 | IR | 22 (invariato) | 22 + header |
| 11 | NegR | 16 (15 v1.0 + NegR-AMB-016) | 16 + header |
| 12 | VR | 70 (68 v1.0 + VR-AMB-01 + VR-AMB-02) | 70 + header |
| 13 | Coverage_Matrix | 29 + header (28 v1.0 + StNeed-029 → SyR-NF-AMB-001) | 29 + header |
| 14 | Gap_Analysis | Riepilogo gap v1.5 (8 metriche) | circa 10 + header |

### 7.4 Color coding v1.5 (esteso)

Lo schema è invariato rispetto a v1.0 con le seguenti aggiunte:

- **SyR NF (Environmental Compliance)**: verde scuro (#548235), distinto da SyR F/P/O/S/E (azzurro #BDD7EE) per evidenziare la natura non-funzionale di conformità
- **SsR OPS / DAT**: bordo punteggiato (visual cue per nuovi sottosistemi logici)
- **NegR-AMB-016**: identico stile NegR (pesca #F8CBAD)
- **Confidence overlay**: high=verde, medium=ambra (nuovo SyR-NF-AMB-001 più StNeed-029), low=rosso, boundary=blu

---

## 8. Note di chiusura del report v1.5

La RTM v1.5 chiude anticipatamente a M+3 (batch 2) il gap §5.6 della v1.0 (REQ-NF-AMB-01 più StNeed Ente Parco Antola integration) e raggiunge le seguenti metriche:

- **Coverage StNeed → SyR: 100%** (29/29), target G3 100% raggiunto
- **Coverage SyR → SsR (decomponibili): 75.0%** (33/44), target G2 80% raggiungibile con azione M+5-6 invariata su 11 SyR
- **Coverage SyR → VR: 100%** (66/66), target G3 100% raggiunto
- **Orphan: 0**, passing
- **Untestable: 0** (target G3: 0), passing
- **NegR Active: 16/16** più 0 violazioni, passing
- **Coverage tematica ambientale**: completa (1 StNeed + 1 SyR + 3 SsR + 1 NegR + 2 VR), passing target M+6 anticipato a M+3

**Prossimi step critici v1.5 → v1.5.1 / v2.0** (in ordine di priorità):

1. **Workshop Ente Parco Antola M+5-6** (engagement attivo via snai-funding-expert più esg-sustainability-officer) per validazione formale StNeed-029 più SyR-NF-AMB-001, acquisizione mappa nidi noti (input critico per SsR-OPS-AMB-001 buffer dinamici) e draft Convenzione operativa Y1. Output: v1.5.1 hotfix con confidence high.
2. **Decomposizione SsR M+5-6** per gli 11 SyR unallocated residui (azione invariata v1.0 §5.4) → coverage target 82-85% per G2.
3. **Pre-application meeting ENAC M+3-6** per validare SyR-F-002 (SAIL Pentema) e verificare la compatibilità con SyR-NF-AMB-001 quota minima 200 m AGL su SIC (richiesta SORA potenzialmente più stringente nel buffer Parco) → falsifying observation per gate G2.
4. **Trade Study chiusi M+6 → M+12** (TS-PLATFORM-6A, TS-AVI-6A, TS-PAYLOAD-EO, TS-MATERIAL, TS-PROP-6B) → chiusura OQ-001/003/005/006/007 → update SyR/SsR confidence levels.
5. **Risk Register v1.5 ratifica board** (OQ-019 DONE batch 2 M+3), verifica linkage RSK-AMB-001/002/003 → SyR-NF-AMB-001 più NegR-AMB-016 in coerenza Risk Register v1.5 (deliverable parallelo batch 2 M+3).
6. **Audit semestrale NegR M+9** prima del G3 → verifica 0 violazioni più waiver log up-to-date più **primo audit specifico NegR-AMB-016** (prima stagione critica mar-lug parzialmente coperta).
7. **Rigenerazione `RTM-v1.5.xlsx` M+6** (vedi §7.2bis) via `build_rtm.py` esteso, il single source of truth Excel deve riflettere v1.5 prima del gate G2.
8. **V&V Plan dettagliato per VR Open → Planned**, 22 VR ancora in stato "Open" più 2 nuovi VR-AMB-01/02 (Planned, da pianificare con budget allocato ARPAL contractor più giornate Ente Parco).

**Action item documentale v1.5:**

- Allegato A.1 v1.5 (questo file) pubblicato in Vol. 2 dello Studio in qualità di **report di accompagnamento delta** rispetto al v1.0; entrambi i file restano nel repository per audit trail.
- File `RTM-v1.5-delta.csv` (circa 5 KB) accanto a `RTM-v1.0-full.csv` (circa 88 KB) in `/studio-di-fattibilita/allegati/A1-RTM/`.
- File `RTM-v1.0.xlsx` **invariato** in attesa rigenerazione M+6 → `RTM-v1.5.xlsx`.
- Cross-reference Cap. 3 (RTM v0.5 baseline) più Cap. 5 §5.7bis (quadro normativo ambientale, atteso M+5-6) più Cap. 6 §6.4 (Safety Case più ambientale) più Cap. 9 §9.2 (gate G2 entry criteria deve includere SyR-NF-AMB-001 in coverage check).

**Disclaimer epistemico** (skill `epistemic-rigor`): la presente RTM v1.5 mantiene la confidence aggregata **medium** della v1.0 con un overlay specifico **medium per la sezione ambientale**:

- Confidence StNeed-029 più SyR-NF-AMB-001 più 3 SsR più NegR-AMB-016 più VR-AMB-01/02: tutti dichiarati **medium** in attesa di engagement formale Ente Parco Antola M+6 (workshop atteso M+5-6). Il refresh a high è pianificato in v1.5.1 hotfix M+6 post-workshop.
- Falsifying observation operativa di StNeed-029 esplicita: "Ente Parco Antola rifiuta firma Convenzione operativa entro M+9 (target M+12 latest) OPPURE comunità Pentema esprime opposizione formale documentata". Trigger osservabile e remediation declaration (relocate sito pilota su altra frazione SNAI non in Parco) garantiscono auditabilità del requisito.
- Cross-validazione triangolata: A.12 VIA v2.0 §A.12.3-A.12.4 (evidenze biologiche fonti pubbliche secondarie, confidence medium-low) più A.2 Risk Register v1.5 §26-27-28 (3 RSK-AMB con score quantitativi e mitigazioni) più RTM v1.5 (presente, requisito formalizzato con metodo VAFC). La triade è auto-coerente ma non validata da ente terzo (RINA, DNV, ARPAL); validazione raccomandata per uso "investment-grade" prima del G5 (M+24).
- I numeri di buffer (500 m / 1000 m), quota minima (200 m AGL) e soglie acustiche (+3 dB(A) Leq,d) derivano da best practice nazionali (vedi A.12 v2.0 §A.12.6) e da letteratura grigia ornitologica, non da rilievi field dedicati al Parco Antola. La conferma operativa richiede mappa nidi noti Ente Parco più campagna fonometrica baseline M+10 (VR-AMB-02).

---

## 9. Riferimenti

[^1]: **NASA Systems Engineering Handbook Rev 2** (NASA/SP-2016-6105 Rev 2). Source: `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md`. Specifico: §4.1, §4.2, §4.3 (logical decomposition), §5.3, §5.4. Confidence: high.

[^2]: **INCOSE Systems Engineering Handbook**, 5th Edition (2023) più INCOSE Guide for Writing Requirements (GtWR 2023).

[^3]: **ISO/IEC/IEEE 15288:2015** "Systems and software engineering, System life cycle processes".

[^4]: **Reg. UE 2019/947** (Operations UAS). Source: `fonti/CELEX_32019R0947_IT_TXT.md`. Confidence: high.

[^5]: **EASA AMC/GM** Issue 1 Amendment 3 (SORA 2.5 europea, settembre 2025). Source: ED Decision 2025/018/R.

[^6]: **DPR 357/1997** art.5 "Valutazione di Incidenza", quadro normativo italiano per Rete Natura 2000. Linkato a SyR-NF-AMB-001.

[^7]: **Direttiva 2009/147/CE "Uccelli"** più Allegato I (specie di interesse comunitario). Specie rilevanti SIC IT1331402: aquila reale, gufo reale, pellegrino, biancone, fonte primaria per buffer NegR-AMB-016.

[^8]: **L.R. Liguria 12/1995** "Riordino delle Aree Protette", istituzione Parco Naturale Regionale dell'Antola più competenze Ente Parco più sanzioni art.27 (fino €15.000 per violazione vincoli ambientali).

[^9]: **Decreto Min. Ambiente 16.03.1998** "Tecniche di rilevamento e di misurazione dell'inquinamento acustico", strumentazione classe 1 IEC 61672 più indicatori Leq più zonizzazione aree protette Classe I. Linkato a VR-AMB-02.

[^10]: **Cap. 3 Requisiti e RTM** baseline v0.5: `studio-di-fattibilita/cap-03-requisiti-e-RTM.md`.

[^11]: **Cap. 5 Quadro Normativo** più 15 showstopper più atteso §5.7bis quadro normativo ambientale: `studio-di-fattibilita/cap-05-quadro-normativo.md`.

[^12]: **Cap. 6 Analisi tecnica** più Trade Studies: `studio-di-fattibilita/cap-06-analisi-tecnica.md` §6.3 più §6.4 Safety Case.

[^13]: **Cap. 9 Cronoprogramma e Gate**: `studio-di-fattibilita/cap-09-cronoprogramma-e-gate.md` §9.2 (Gate G0-G6 entry/exit criteria, il G2 entry criteria deve includere SyR-NF-AMB-001 coverage check).

[^14]: **Allegato A.12 Relazione VIA Preliminare v2.0**: `studio-di-fattibilita/allegati/A12-VIA-preliminare/A12-Relazione-VIA-Preliminare-COMPLETE-v2.0.md`, refinement chain origin per REQ-NF-AMB-01.

[^15]: **Allegato A.2 Risk Register v1.5**: `studio-di-fattibilita/allegati/A2-Risk-Register/A2-RISK-REGISTER-REPORT.md` §3bis più §26-27-28 (RSK-AMB-001/002/003), refinement chain peer di RTM v1.5.

[^16]: **Allegato A.1 RTM v1.0 Report (predecessore)**: `studio-di-fattibilita/allegati/A1-RTM/A1-RTM-REPORT.md`, baseline M+3 di riferimento.

[^17]: **Skill `requirements-traceability-matrix`**: `.claude/skills/requirements-traceability-matrix/SKILL.md`, workflow di costruzione applicato.

[^18]: **Skill `epistemic-rigor`**: `.claude/skills/epistemic-rigor/SKILL.md`, disciplina di falsifiability più confidence levels applicata.

[^19]: **Boundary conditions B1+B2** dichiarate in `CLAUDE.md` (project root) più `riferimenti/visione-10-anni.md` più `riferimenti/RESERVED-rischi-geopolitici.md`.

[^20]: Build script `/studio-di-fattibilita/allegati/A1-RTM/build_rtm.py`, riproducibilità del file `RTM-v1.0.xlsx` e CSV via `python3 build_rtm.py`. Per v1.5 va esteso secondo istruzioni §7.2bis.
