# Audit Completezza vs Art. 41 D.Lgs. 36/2023 + Allegato I.7

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes (Coopfond / Legacoop)
>
> **Versione audit:** v1.0
> **Data emissione:** 2026-05-17 (M+3)
> **Auditor:** senior compliance auditor + systems engineer (Claude Code agent)
> **Riferimento normativo primario:** D.Lgs. 31 marzo 2023 n. 36 art. 41 + Allegato I.7 (`fonti/2023_0036.md`)
> **Riferimento metodologico:** NASA SE Handbook Rev 2; INCOSE; ISO/IEC/IEEE 15288
> **Disclaimer:** audit di completezza/tracciabilità formale del corpus documentale al M+3. NON sostituisce validazione esterna RINA/DNV; NON certifica investment-grade.

---

## 0. Verdetto sintetico

> **PFTE-compliant a livello strutturale + Major Gap su evidence-chain esterna**.
>
> Lo Studio è **formalmente completo** per i 14 elaborati PFTE dell'Allegato I.7 (18/18 voci coperte o esplicitamente non applicabili). Le 4 catene di tracciabilità (StNeed→SyR→SsR→V&V; Rischi→Mitigation; Cap.4-ICD; StNeeds-RTM) sono **numericamente verificate** con copertura 100% sui punti hard (no orphan, no untestable, 20/20 INT mappate, 17/17 StNeed baseline ereditati). Permane un **gap di coverage SyR→SsR al 72%** (vs target G2 80%, G3 95%) e **3 placeholder operativi** (A.6 CAD, A.13 fotografica, A.9 CME per scenari di scale-up). Per il **gate G3 metodologico** (M+10/M+11) il documento è **PFTE-compliant**.
>
> Per il **gate G3 investment-grade** (presentazione esterna bandi pubblici Cooding/PNRR/FESR) sono necessari **7 chiusure operative esterne** (LoI Regione, Coopfond 2026, vendor quotation reali, pre-application ENAC, DPIA pubblica, validation RINA/DNV, dichiarazioni di conformità firmate). Non sono difetti strutturali del documento, ma debito di engagement che lo Studio dichiara esplicitamente (15 DR-research-closure).

---

## 1. Matrice 18 elaborati PFTE vs Studio

### 1.1 Documenti preliminari ex Allegato I.7 (Sezione I-II)

| # | Documento art. 41 + All. I.7 | Posizione nello Studio | Coverage | Note |
|---|---|---|---|---|
| **P.1** | **Quadro Esigenziale (QE)** ex All. I.7 Sez. I art. 1 | Vol. 1 Cap. 1 (`cap-01-inquadramento.md`) | ✅ **CONFORME** | §1.6 contiene mappatura esplicita art. 1 c. 1.a-b (obiettivi + KPI + fabbisogni); 8 criticità Aree Interne (§1.2.4); 6 obiettivi OB-01→OB-06 con KPI di gate; QE redatto direttamente da Firmamento come committente (legittimo per iniziativa privata, vedi §1.6); cross-ref PSNAI 2025 + SNAI |
| **P.2** | **DOCFAP (Doc Fattibilità Alt. Progettuali)** ex All. I.7 Sez. II art. 2 | Vol. 2 Allegato A.3 (`A3-DOCFAP-Trade-Studies.md`) | ✅ **CONFORME** | 6 trade study formali (TS-PLATFORM-6A, TS-MATERIAL, TS-PROP-6B, TS-AVI-6A, TS-PAYLOAD-EO, TS-COMMS); ogni trade ha alternative valutate (incluso "do nothing" implicito), criteri + pesi, scoring matrix 1-10, sensitivity, raccomandazione, falsifying observation; §A.3.9 dichiara compliance esplicita ai 6 punti DOCFAP. **Caveat:** TS-PLATFORM-6A in fase di shift JOUAV→Tekever post audit; verdetto formale M+6 post quotation reali (DR-003) |
| **P.3** | **DIP (Doc Indirizzo Progettazione)** ex All. I.7 Sez. II art. 3 | NON in scope (M+12+) | ✅ **ESCLUSIONE ESPLICITA** | Cap. 5 §5.9.1 dichiara DIP "Post-Studio (M+12+)"; Cap. 1 §1.6 nota che DIP è atto del committente per la fase esecutiva, fuori scope PFTE; coerente con prassi italiana (DIP è output operativo del RUP a valle del PFTE) |
| **P.4** | **PE — Progetto Esecutivo** ex All. I.7 Sez. V | NON applicabile a PFTE | ✅ **ESCLUSIONE ESPLICITA** | Cap. 4 §4.1.5 dichiara out-of-scope esplicitamente (procurement esecutivo, lavori civili permanenti, contratti vincolanti deferred post-M+12) |

### 1.2 Elaborati minimi PFTE — Allegato I.7 Sez. IV (1-14)

| # | Elaborato PFTE | Posizione nello Studio | Coverage | Stato |
|---|---|---|---|---|
| **1** | **Relazione generale** | Vol. 1 Cap. 0 (Sintesi Esecutiva, 252 righe) + Cap. 1 (Inquadramento + QE, 576 righe) | ✅ **CONFORME** | Cap. 0 = 5-8 pp executive; Cap. 1 = inquadramento completo M+3 |
| **2** | **Relazione tecnica + indagini specialistiche** | Vol. 1 Cap. 5 (Norm., 883 righe) + Cap. 6 (Tecn., 718 righe) + Cap. 7 (Mercato, 855 righe) | ✅ **CONFORME** | Vol. 1 totale ~7800 righe; relazione tecnica + 5 livelli normativi + analisi tecnica architettura/prestazioni/FMECA/FTA/trade study |
| **3** | **Relazione verifica preventiva interesse archeologico** | NON applicabile | ✅ **ESCLUSIONE LEGITTIMA** | Per il PFTE Firmamento NON sono previste opere fisse significative: hangar in opzione affitto immobile esistente (preferito, vedi A.9 §A.9.3 opzione A); GS fissa è container modificato senza fondazioni archeologicamente rilevanti; il sito Pentema è borgo storico (impatti simbolici trattati in A.12 §A.12.2.7). **Raccomandazione audit:** aggiungere una nota di esclusione formale in Cap. 5 §5.9.1 per disciplina compliance (l'esclusione è implicita ma non dichiarata espressamente con riferimento all'art. 25 D.Lgs. 50/2016 / art. 41 D.Lgs. 36/2023) |
| **4** | **Relazioni specialistiche** (geologica, idrogeologica, ambientale, sismica) | Vol. 2 A.12 VIA preliminare (205 righe) + Vol. 1 Cap. 6 §6.5 (infrastrutture Pentema) | ◐ **PARZIALE** | A.12 copre 8 componenti ambientali (aria, rumore, acque, suolo, biodiversità, paesaggio, patrimonio culturale, salute) ma NON c'è relazione geologica/sismica dedicata (Pentema 1100-1300 m s.l.m., zone sismiche IT 3-4 per Liguria). **Gap:** la natura del progetto (UAS no opere fisse significative) attenua la rilevanza, ma per PFTE compliance formale serve almeno screening sismico del sito GS/hangar. Coverage adeguata per concept/preliminary, da approfondire M+6-9 con sopralluogo |
| **5** | **Studio di Impatto Ambientale** | Vol. 2 A.12 VIA preliminare | ✅ **CONFORME** | A.12 §A.12.0 dichiara verdetto preliminare: VIA piena non obbligatoria per scale 6A (UAS < 100 kg, ops temporanee); raccomandato screening VIA volontario; 8 componenti analizzate; cross-ref D.Lgs. 152/2006 + 104/2017 + LR Liguria 38/1998. Per 6B Phase B+ VIA potrebbe diventare obbligatoria (riconosciuto) |
| **6** | **Elaborati grafici** (planimetrie, sezioni, prospetti) | Vol. 2 A.6 CAD (114 righe) + cartella `/cad/` binari | ◐ **PLACEHOLDER** | A.6 README mappa 12 modelli CAD (CAD-AERO-001/002, CAD-FUSE-001/002, CAD-PROP-001/002, CAD-ALT-001, CAD-STRUCT-001/002, CAD-GS-001/002, CAD-HANGAR-001). Esistono CAD binari in `/cad/` ma non export PDF/PNG accessibili. Roadmap: v1.5 M+6 export PNG; v2.0 M+10 package completo gate G3. **Gap:** planimetrie GS fissa Pentema + GS mobile + layout hangar NON ancora esistenti come elaborati grafici. Critico per gate G3 investment-grade |
| **7** | **Calcoli preliminari** (strutture, impianti) | Vol. 2 A.7 (Link Budget 448 righe + Energy Balance 294 righe + Financial Model README 80 righe) + A.8 Bilanci Massa (154 righe) | ✅ **CONFORME** | Modelli quantitativi: link budget 14 scenari ITU-R 12/14 OK; energy balance HALE 365gg con risultato critico (-50.1% inverno 44°N); mass budget 6A+6B con margini; financial model 10 sheet Excel. Strutture preliminari (longheroni, ala high-AR) in Cap. 6 + Progetto concettuale HALE.md; calcoli FEM detailed deferred a Phase A M+6+ |
| **8** | **Computo Metrico Estimativo (CME)** | Vol. 2 A.9 (171 righe) | ◐ **PARZIALE** | A.9 copre GS fissa Pentema (€76k+IVA = €93k), GS mobile (€64k+IVA = €78k), hangar 2 opzioni (affitto €27-32k Y1 o light build da quantificare). Voci dettagliate per A-F (container, allacciamento, antenne, computing, sicurezza, spese tecniche) con prezzi unitari prezziario Liguria 2024. **Gap:** CME hangar light build (opzione B) incompleto; opzione di scale-up Y2-Y3 non quantificata; confidence "medium-low" dichiarata. Sufficiente per concept, va rifinito post-sopralluogo M+6 |
| **9** | **Quadro Economico** | Vol. 2 A.7 financial-model + Vol. 1 Cap. 8 §8.3 | ✅ **CONFORME** | Cap. 8 §8.0.1 contiene tabella QE 6A (CapEx €700-1200k Y1 + scale €0.5-1.5M Y2-Y3; OpEx Y2 €260-480k); 6B CapEx €5.5-13.5M Y3-Y5. Financial model Excel sheet 9 "Quadro_Economico_art41" formato Codice Contratti. **Caveat onesto:** CapEx Y1 baseline €1.4M, sliding timeline reale €2.5-3.5M (post audit); pricing PA recalibrato €75k/anno (vs €150k originale, falsificato Cluster D) |
| **10** | **Cronoprogramma** | Vol. 1 Cap. 9 (635 righe) + A.5 V&V Plan schedule | ✅ **CONFORME** | Cap. 9 §9.0.1-2: 7 gate principali (G0 M+0 → G6 M+36+); WBS 4 livelli Studio M+0→M+11; gantt operativo Fase 1 6A M+12→M+24; gantt R&D 6B M+24→M+48. Sliding timeline §9.12 dichiarato come piano operativo realistico (scenario base) |
| **11** | **Piano Economico-Finanziario** (NPV, IRR, payback, ROI) | Vol. 2 A.7 financial-model + Vol. 1 Cap. 8 §8.5-6 | ✅ **CONFORME** | Cap. 8 §8.0.1 tabella sintesi: NPV 10y +€3.5M scenario base WACC 12%, IRR 18-22%, payback 5 anni, break-even Y4-Y5; financial model sheet 5 NPV_IRR + sheet 6 Sensitivity (7 driver) + sheet 7 Scenarios (worst/base/best). **Caveat onesto:** confidence aggregato medium-low; investment-grade richiede Monte Carlo + LoI firmate + audit revisore contabile |
| **12** | **Piano di Manutenzione preliminare** | Vol. 2 A.10 (207 righe) | ✅ **CONFORME** | A.10 conforme AS/EN 9110 + Reg.UE 2019/947 art.14 + ENAC Reg. APR Ed.3 art.19. 8 categorie manutenzione (MNT-PRE/POST/DAILY/50H/200H/ANN/CAL/COR); checklist operativa per 6A; costi MNT-50H €500-1500/4-8h, MNT-200H €5-15k; calendario sostituzioni batterie LiPo 24-36 mesi. Confidence medium-low (preliminare); Detailed Maintenance Plan deferred M+6-12 |
| **13** | **Piano di Sicurezza e Coordinamento (PSC)** | Vol. 2 A.11 (208 righe) | ✅ **CONFORME** | A.11 consolida (i) PSC operativo art.41 + (ii) SORA Safety Case 2.5 ED Decision 2025/018/R. ConOps + SORA Step 1-6 preliminare (iGRC 4-5 → final GRC 2-3 post M1+M2+M3; iARC b → SAIL II-III); 18+ OSO applicabili identificati; PSC personale + popolazione + ERP + coordinamento autorità locali + Risk Acceptance Matrix. **Caveat:** Step 7-9 detailed + Operations Manual + Maintenance Manual deferred M+6-9; SAIL preliminary subordinato a pre-application ENAC (DR-004) |
| **14** | **Documentazione fotografica** | Vol. 2 A.13 (148 righe) | ◐ **PLACEHOLDER** | A.13 README contiene indice di acquisizione fotografica raccomandata: 10 foto Pentema, 6 area Valli Antola-Tigullio, 6 piattaforme vendor, 4 HALE CAD render, 5 use cases, 3+ stakeholder workshop. Status M+3: documentazione fisica del sito Pentema "da acquisire durante sopralluogo Y0 M+3-6". **Gap:** zero foto reali nel corpus al M+3; placeholder accettabile per bozza M+3, NON per gate G3 M+10/M+11. Foto vendor (JOUAV, Tekever) e CAD render reperibili immediatamente da media kit pubblici |

### 1.3 Sintesi matrice (18 voci totali)

| Stato | Conteggio | Voci |
|---|---|---|
| ✅ Conforme | 13/18 | P.1 QE, P.2 DOCFAP, P.3 DIP (escl.), P.4 PE (escl.), El.1 Rel.Gen, El.2 Rel.Tec, El.3 Archeo (escl.), El.5 SIA, El.7 Calc., El.9 QE, El.10 Crono, El.11 PEF, El.12 Manut, El.13 PSC |
| ◐ Parziale / Placeholder | 5/18 | El.4 Rel.specialistiche (geo/sismica mancanti, parziale), El.6 Elab. grafici (CAD non esportato), El.8 CME (hangar opt.B incompleto, scale-up non quantificato), El.14 Doc. fotografica (placeholder M+3) |
| ❌ Mancante | 0/18 | – |

**Conformità formale aggregata: 72% conforme + 28% placeholder/parziale = 100% nessun gap critico strutturale.**

---

## 2. Tracciabilità StNeeds → SyR → SsR → V&V

### 2.1 Numerica della catena

| Livello | Cap. 3 (baseline v0.5) | A.1 RTM v1.0 (estesa) | Δ | Coverage forward | Coverage backward |
|---|---|---|---|---|---|
| **StakeholderNeeds (StNeed)** | 17 | **28** | +11 (workshop preparatory + extension) | n/a | 100% (ogni StNeed → ≥1 SyR) ✅ |
| **System Requirements (SyR)** | 42 | **65** | +23 (extension fine-grained 7 famiglie F/P/O/S/E/C/Cost) | 100% → V&V ✅ | 100% (no orphan) ✅ |
| **Subsystem Requirements (SsR)** | ~80 (campione) | **81** (su 6 sottosistemi AERO/PROP/AVI/PAY/COMMS/GS) | +1 (formalizzato) | n/a | 100% allocazione subsystem ✅ |
| **Interface Requirements (IR)** | non formalizzato | **22** | +22 (nuovo) | n/a | n/a |
| **Negative Requirements (NegR)** | 14 nominali (15 effettivi §3.5.8) | **15** (5 Critical + 7 High + 3 Medium-Low) | 0 (ereditato verbatim) | n/a | 15/15 Active, 0 violazioni ✅ |
| **Verification Requirements (VR)** | non formalizzato (V&V Plan §3.7) | **68** | +68 (nuovo) | n/a | n/a |
| **TOTALE righe RTM** | ~155 stimato | **279** | +124 (+80%) | – | – |

### 2.2 Tracciabilità verificata punto per punto

#### A. 28 StNeed → ≥1 SyR figlio?

> ✅ **COVERAGE 100%**. Verificato in A.1 §3 (RTM coverage analysis) + §5.1 (orphan StNeed 0). I 17 StNeed baseline del Cap. 3 §3.3.2 sono **ereditati integralmente** in A.1 (StNeed-001..017 nominali); gli 11 aggiuntivi (StNeed-018..028) vengono dall'extension workshop preparatory + dossier SNAI Liguria + protocolli operativi PC/CC Forestali.

#### B. 65 SyR → ≥1 SsR figlio?

> ◐ **COVERAGE 72% (sotto soglia G2 80%, sotto soglia G3 95%)**. A.1 §3 esplicita: dei 43 SyR delle famiglie decomponibili (F/P/O/S/E), 31 hanno SsR figlio diretto (72.1%). Le famiglie C (Compliance) e Cost (Cost & Business) non sono decomponibili a livello sottosistema (verifica per Inspection documentale / Analysis Quadro Economico — metodologicamente corretto NASA SE §4.3). Includendo tutte le 65 SyR il valore nominale è 55.4%.
>
> **Action plan dichiarato in A.1 §5.4 + A.1 §3 Note**: 12 SyR da decomporre entro M+5-6 (8-12 ore engineer):
> - SyR-F-006 (SAR notturno), SyR-F-009 (Enti Parco EO multi-stagionale), SyR-F-010 (NTN gNB)
> - SyR-P-002 (cruise speed), SyR-P-011 (MTOW 6A)
> - SyR-O-007 (HALE ConOps), SyR-O-008 (maintenance program)
> - SyR-S-005 (failure rate FTA), SyR-S-008 (ATEX hangar+BMS)
> - SyR-E-004 (LCA cross-cutting), SyR-E-005 (EOL plan)
> - SyR-P-010 (COMMS link)
>
> Target post-action: 80% (G2 passing); G3 target 95% raggiungibile entro M+10.

#### C. 65 SyR → V&V Method definito?

> ✅ **COVERAGE 100%**. A.1 §3 (untestable 0); A.5 V&V Plan v1.0 sheet `VV_Matrix_SyR` 71 SyR+SsR+IR con metodo I/A/D/T allocato. Distribuzione: I 32%, A 38%, D 27%, T 42% (con combinazioni). A.5 §A.5.1.1 falsifying observation: se Test >60% Phase A sovra-dimensionato → da rivedere.

#### D. 81 SsR → allocazione subsystem?

> ✅ **COVERAGE 100%**. A.1 §2 breakdown: 6 sottosistemi (AERO 16, PROP 13, AVI 17, PAY 13, COMMS 11, GS 11). Tutti gli 81 SsR hanno allocazione esplicita.

### 2.3 Orphan / Untestable / Unallocated

| Metrica | Valore v1.0 | Soglia G3 (M+10) | Esito |
|---|---|---|---|
| StNeeds con ≥1 SyR figlio | 100.0% | 100% | ✅ |
| SyR decomponibili con ≥1 SsR | 72.1% | ≥95% | ❌ **GAP attivo** (action M+5-6) |
| SyR con metodo V&V definito | 100.0% | 100% | ✅ |
| SsR con allocazione subsystem | 100.0% | 100% | ✅ |
| Orphan SyR | **0** | 0 | ✅ |
| Untestable SyR | **0** | 0 | ✅ |
| NegR Active monitorati | 15/15 (100%) | 15/15 + 0 violazioni | ✅ |

**Verdetto tracciabilità A:** **CONFORME su 6/7 metriche**, **GAP SyR→SsR aperto** con action plan M+5-6 di 8-12 ore engineering documentato. Nessun gap critico strutturale.

### 2.4 Lista 12 SyR unallocated (gap M+5-6)

| Req-ID | Famiglia | Sottosistema target decomposizione | Owner |
|---|---|---|---|
| SyR-F-006 | F | PAY (IR notturno) + COMMS (telemedicina) | aerospace-SE |
| SyR-F-009 | F | PAY (EO multi-stagionale) | aerospace-SE |
| SyR-F-010 | F | PAY (gNB 5G NR-NTN, già SsR-PAY-004) — formalizzare link | telecom-ntn-payload-expert |
| SyR-P-002 | P | AERO (cruise + powertrain) | vtol-uas-specialist |
| SyR-P-011 | P | AERO (MTOW 6A, già SsR-AERO-007) — formalizzare link | vtol-uas-specialist |
| SyR-P-010 | P | COMMS (già SsR-COMMS-001/002) — formalizzare link | telecom-ntn-payload-expert |
| SyR-O-007 | O | AVI (ConOps + ENAV LoA) | avionics-gnc-engineer |
| SyR-O-008 | O | AERO + PROP (maintenance program) | vtol-uas-specialist |
| SyR-S-005 | S | AVI (failure rate FTA + FCS DAL-C) | avionics-gnc-engineer |
| SyR-S-008 | S | GS (hangar ATEX) + PROP (BMS) — già SsR-GS-011/SsR-PROP-008 — formalizzare link | esg-sustainability-officer |
| SyR-E-004 | E | (cross-cutting LCA, NASA SE §4.3 accetta no SsR) — accettato | esg-sustainability-officer |
| SyR-E-005 | E | (cross-cutting EOL plan) — accettato | esg-sustainability-officer |

Action effective: 9 SyR da decomporre + 3 da formalizzare link a SsR esistenti = effort 8-12 ore.

### 2.5 Catena 17 StNeed baseline → 28 v1.0 RTM

> ✅ **CONFORME**. I 17 StNeed del Cap. 3 §3.3.2 sono **ereditati integralmente** in A.1 RTM v1.0:
> - Categoria A "PA + PC" (StNeed-001..004): frane, antincendio, connettività emergenza, SAR
> - Categoria B "Cooperative Legacoop" (StNeed-005..007): mappatura, agricolo, connettività rurale
> - Categoria C "Comunità + Pentema" (StNeed-008..009): privacy, ambiente
> - Categoria D "Operations" (StNeed-010..011): disponibilità, sicurezza BVLOS
> - Categoria E "Compliance" (StNeed-012..014): EASA, AGCOM, privacy
> - Categoria F "Business" (StNeed-015..017): service model, sostenibilità Y1, vision 10y
>
> Extension v1.0 (StNeed-018..028) aggiunge: telemedicina, e-learning, smart grid coop energetiche, turismo culturale, integrazione D-Flight/ENAV/AgID/PSN/Garante, audit AS/EN 9100, MTBF formalizzato, Part-IS ISMS, NIS2 D.Lgs. 138/2024, AI Act art.5+6, AgID/PSN hosting dati PA, cluster D pricing benchmark.

---

## 3. Tracciabilità Rischi → Mitigation

### 3.1 Catena risk register

| Livello | Conteggio | Note |
|---|---|---|
| **Totale rischi tracciati A.2** | **116** | 22 sheet Excel + report 675 righe |
| **Categorie** | 11 (Cybersecurity 7, Finanziario 10, Geopolitico 5, Mercato 10, Operativo 12, Privacy/Legale 7, Regolatorio 30, Reputazionale 5, RU 5, Supply Chain 7, Tecnico 15 + 3 misti) | A.2 §2.1 |
| **Showstopper (pre-mitigation Score 20-25)** | **5** | RSK-TEC-001/002/003 + RSK-REG-001 + RSK-FIN-001 (vedi Cap. 10 §10.2.1) |
| **RED Showstopper aggiuntivi §5.16 (5)** | **5** | RSK-REG-019 Part-IS + RSK-REG-021 AgID/PSN + RSK-REG-025 art.50 PA + RSK-REG-027 NIS2 + RSK-REG-030 ENAV FL400+ (vedi A.2 §4.2) |
| **Critical (Score 16-19)** | 12 + 5 showstopper aggiuntivi | A.2 §2.2 (Open-Critical) |
| **RED totali pre-mitigation** | 17 | A.2 §2.4 |
| **RED post-mitigation (residual)** | **2** | RSK-TEC-001 (residual 20) + RSK-TEC-015 (residual 12) |

### 3.2 116 rischi → tutti hanno mitigation?

> ✅ **VERIFICATO PER 25 RISCHI NARRATI** in A.2 §3 (top-25 Score ≥12), ciascuno con campi obbligatori NASA NPR 8000.4A: Descrizione, Trigger, Owner, Status, Response (Avoid/Mitigate/Transfer/Accept), Mitigation, Residual P×I, Fase critica, Confidence, EWI, Falsifying observation.
>
> ✅ **Sistema di mitigation effectiveness** documentato A.2 §2.4: Pre-mitigation RED=17→YELLOW=66→GREEN=33 = 116; Post-mitigation residuali RED=2→YELLOW=19→GREEN=95 = 116. RED reduction 88% (17→2), YELLOW reduction 71% (66→19).
>
> ◐ **Verifica completezza coverage per i 91 rischi NON narrati nel top-25**: il report A.2 dichiara FMECA + FTA results sintesi (§5-6) + EWI monitoring plan (§8) ma il dettaglio individuale di mitigation per i 91 rischi minori è nei fogli XLSX (`FMECA_Payload/Avionica/Propulsione` + sheet rischi categorizzati). **Coverage formalizzata: 25/116 narrati nel report MD + 91/116 nei fogli XLSX**. Coerente con prassi NASA NPR 8000.4A (narrazione obbligatoria per top-25, tracciamento tabellare per il resto).

### 3.3 5 showstopper originali + 5 showstopper aggiuntivi → action items + owner + deadline?

> ✅ **CONFORME**. A.2 §4.1 (5 originali Cap. 6.4 + Cap. 10.2):
>
> | ID | Owner | Fase critica | Mitigation |
> |---|---|---|---|
> | RSK-TEC-001 | propulsion-energy-engineer | Y3-Y5 (Phase B 6B) | Plan A E5 Seasonal mandatory; Plan B Y6+ SS Li 450 Wh/kg / PEM+LH2; Plan C R&D-only |
> | RSK-REG-001 | aviation-regulatory + sovereign-strategist | Y3-Y6 (Phase B/C) | EASA Innovation Network + consortium CIRA/TAS; ASD-Eurospace HAPS WG; DG MOVE/DEFIS lobby |
> | RSK-FIN-001 | financial-cfo + sovereign-strategist | Y2-Y3 (gate G5) | Mix EDF + Horizon + PNRR + Series B equity (CDP, EIB); partnership prime cost sharing |
> | RSK-TEC-002 | aero-structures-engineer | Y3-Y4 (Phase B 6B) | Aeroelastic non-lineare (NASTRAN+ZAERO) + GVT + flight test subscale + winglet/damping |
> | RSK-TEC-003 | aviation-regulatory + systems-engineer | Y4+ | Parallel ops 6A + Special Condition negoziata + partnership DOA esistente (Leonardo/Tekever/AALTO) |
>
> ✅ **A.2 §4.2 (5 showstopper aggiuntivi §5.16)**:
>
> | ID | Owner | Fase critica | Mitigation |
> |---|---|---|---|
> | RSK-REG-019 (Part-IS ISMS) | aviation-regulatory + CISO new | Y1 M+0→M+12 urgente | Assunzione CISO M+6; ISMS M+9; ISO 27001 M+12; pre-audit ENAC |
> | RSK-REG-021 (AgID/PSN) | data-privacy + IT + DPO | Y1+ | Migrazione provider PSN-qualified TIM/Polo PSN/CDP; audit AgID compliance |
> | RSK-REG-025 (art.50 PA) | snai-funding + legal + business-model | Y0+ | Pre-engagement + accordo quadro art.59; Coopfond veicolo non-gara; SNAI accordi |
> | RSK-REG-027 (NIS2 ACN) | CISO new + legal | Y0+ immediato | Registrazione ACN entro M+1; ISMS Part-IS allineato; 24h notifica incidenti |
> | RSK-REG-030 (ENAV FL400+) | avionics + sovereign-strategist + aviation-regulatory | Y3+ | Engagement ENAV precoce Y2; contributo procedure EUROCONTROL; test bed Sardinia/GATB |
>
> ✅ Tutti i 10 showstopper hanno: owner identificato, fase critica, response strategy (Mitigate), action plan dettagliato, residual P×I post-mitigation, EWI per monitoring.

### 3.4 Implicazione gate G3

A.2 §4.3 + Cap. 10 §10.2.1: "Tutti i 5 RSK-REG critical aggiuntivi mitigated entro M+9-12 (Part-IS, AgID, NIS2 sono **urgenti** M+0-3)". 3 FTE senior (CISO, DPO, Head Reg.Aff.) hired entro M+6-9 (RSK-HR-002). OpEx Y1 aggiornato con +450-800k EUR (RSK-FIN-004). Coerenza con verdetto Cap. 10 §10.0bis "HOLD con piano regolatorio rafforzato" 60-80% probabilità.

### 3.5 Verdetto tracciabilità rischi

> ✅ **CONFORME**. 10 showstopper hanno mitigation + owner + deadline. 25/116 rischi narrati + 91/116 trackati in fogli XLSX. Mitigation effectiveness Pre→Post RED 17→2 (88% reduction). Quarterly review meeting cadence definita (A.2 §8.2). Versioning roadmap v1.0→v3.0 al gate G5 (A.2 §9).

---

## 4. Tracciabilità Interfacce Cap. 4 → ICD A.4

### 4.1 Catena interfacce 20 → 59

| Livello | Conteggio | Note |
|---|---|---|
| **Interfacce primarie Cap. 4 §4.4.1** | **20** | INT-01 → INT-20, ciascuna con descrizione + tipo + standard + owner + status |
| **Sub-interfacce dettagliate A.4 v1.0** | **59** | INT-XX-YYY-NNN (Percorso 6A/6B/X-trasversale × categoria PHY/DATA/C2/GS/REG/NTN/FEEDER/OPS × numero) |
| **Categorie A.4** | 8 (PHY, DATA, C2, GS, REG, NTN, FEEDER, OPS) | Tassonomia A.4 §A.4.1 |
| **Standard di riferimento applicati** | ARP4754A/4761, DO-178C/254/160G/326A, ISO/IEC/IEEE 24765/15288, NASA SP-2016-6105 Rev 2, 3GPP TS 38.x, ITU-R F.1500/1891, Reg.UE 2019/947/945 + 2021/664, GDPR, D.Lgs. 138/2024 | A.4 §A.4.0.2 |

### 4.2 Verifica mapping 20 → 59 (A.4 §A.4.1.3)

> ✅ **COVERAGE 100% (20/20 INT primarie mappate)**. Verificato tabella A.4 §A.4.1.3:

| INT-NN Cap. 4 | Sub-interfacce in A.4 v1.0 |
|---|---|
| INT-01 (Airframe ↔ Payload) | INT-6A-PHY-001/002/003/007; INT-6B-PHY-001/002/003 |
| INT-02 (Payload ↔ Autopilot Data) | INT-6A-DATA-001/002 |
| INT-03 (Air ↔ GS C2 RF Link) | INT-6A-C2-001/002/003/005; INT-6A-DATA-005/006 |
| INT-04 (GS ↔ Aircraft RF Antenna) | INT-6A-PHY-004/005 |
| INT-05 (GS ↔ Backhaul Internet) | INT-6A-PHY-010; INT-6A-DATA-004 |
| INT-06 (Cloud ↔ Cooperative Dashboard) | INT-6A-GS-003; INT-6A-DATA-007 |
| INT-07 (Modem ↔ AGCOM Band) | INT-6A-REG-002 |
| INT-08 (Power Mgmt ↔ FC Battery SOC) | INT-6A-PHY-006 |
| INT-09 (Autopilot ↔ Sensor Suite) | (interno autopilot JOUAV, no sub-interface esposta) |
| INT-10 (Cooperative ↔ GCS ↔ Aircraft) | INT-6A-GS-003 + INT-6A-C2-008 + INT-6A-GS-005 |
| INT-11 (Emergency Escalation PC) | INT-6A-GS-004 |
| INT-12 (Data Governance ↔ DPO Audit) | INT-6A-DATA-008 + INT-6A-GS-007 + INT-X-LOGGING-001 |
| INT-13 (Sistema ↔ ENAC SORA) | INT-6A-REG-001 |
| INT-14 (Sistema ↔ ENAV / D-Flight U-Space) | INT-6A-REG-003 + INT-6B-OPS-001/002 |
| INT-15 (Sistema ↔ Garante Privacy) | INT-6A-REG-004 + INT-X-PRIVACY-001 |
| INT-16 (Firmamento ↔ Vendor UAS) | INT-X-VENDOR-001 |
| INT-17 (Firmamento ↔ Vendor Payload) | INT-X-VENDOR-001 (incluso) |
| INT-18 (Firmamento ↔ Cooperative) | INT-6A-GS-003 (Dashboard) + convenzione operativa |
| INT-19 (Firmamento ↔ Anchor PA) | INT-6A-GS-004 (PC) + convenzione operativa |
| INT-20 (Sistema ↔ Ecosistema EU) | INT-X-CLOUD-001 (GAIA-X) |

**Verifica A.4 §A.4.1.3 (citaz. letterale)**: *"Tutte le 20 interfacce primarie del Cap. 4 sono dettagliate o coperte dall'ICD v1.0. Nessuna interfaccia primaria orphan. Status M+3: 100% copertura mapping."*

### 4.3 Classificazione criticità (A.4 §A.4.1.2)

- **Flight-Critical (DAL-A/B)**: INT-6A-C2-001, INT-6A-C2-004 (Lost-Link), INT-6A-C2-006 (DAA ADS-B)
- **Mission-Critical (DAL-C)**: INT-6A-DATA-001, INT-6A-DATA-005, INT-6A-GS-005
- **Non-Critical (DAL-D/E)**: INT-6A-DATA-007, INT-6A-GS-006
- **Compliance-Critical**: INT-6A-REG-001, INT-6A-REG-004, INT-6A-REG-006
- **Business-Critical**: INT-X-VENDOR-001, INT-6A-GS-004

### 4.4 Verdetto tracciabilità ICD

> ✅ **CONFORME**. 20/20 INT primarie del Cap. 4 → 59 sub-interfacce dettagliate A.4 v1.0. Mapping esplicito in A.4 §A.4.1.3. Coverage 100%. Standard di riferimento applicati a 3 famiglie normative (Aerospace ARP/DO, SE generico ISO/NASA, settore-specifico 3GPP/ITU-R/Reg.UE). Falsifying observation operative su INT critiche.

---

## 5. Compliance dichiarativa

### 5.1 Tabella dichiarazioni di conformità

Il documento dichiara conformità a 7 famiglie normative principali. Verifica evidence chain:

| Norma dichiarata | Dichiarazione (dove) | Evidence chain disponibile | Stato evidence |
|---|---|---|---|
| **D.Lgs. 36/2023 art. 41 + Allegato I.7** | Cap. 0, Cap. 1 §1.6, Cap. 4 §4.1.1, Cap. 5 §5.9, README Vol. 2 | `fonti/2023_0036.md` (testo integrale + Allegati); mappatura QE → Cap.1 + DOCFAP → A.3 + 14 elaborati → tabella §1.2 sopra | ✅ **COMPLETA** |
| **Reg. UE 2019/947 + 2019/945** | Cap. 5 §5.1.2-3, A.11 §A.11.2 (SORA 2.5) | `fonti/CELEX_32019R0947_IT_TXT.md` + `fonti/CELEX_32019R0945_IT_TXT.md`; quotation OSO art. 11 c. 2 | ✅ **COMPLETA** |
| **EASA SORA 2.5 Amendment 3 (settembre 2025)** | Cap. 5 §5.1.4-5, A.11 §A.11.2 | `fonti/ed_decision_2025-018-r.md` + `fonti/annex_to_ed_decision_2025-018-r_1.md` + `fonti/explanatory_note_to_ed_decision_2025-018-r.md`; quotation Annex modifiche SORA 2.5 EU | ✅ **COMPLETA** |
| **Reg. UE 2021/664 + ENAC LG-2023/006 (U-Space)** | Cap. 5 §5.2 | `fonti/CELEX_32021R0664_IT_TXT.md` + `fonti/LG-2023_006-UAS-Linee-Guida-U-Space.md` | ✅ **COMPLETA** |
| **ENAC Reg. APR Ed.3 + Emend.1** | Cap. 5 §5.3, A.11 §A.11.5 | `fonti/Regolamento_APR_Ed_3_Emend_1.md` | ✅ **COMPLETA** |
| **AS/EN 9100 + ISO 9001** | Cap. 5 §5.9.2, A.10 §A.10.0 (riferimento AS/EN 9110 maintenance), Cap. 0 | Standards citati come "in corso certificazione"; nessuna certificazione attiva al M+3 | ◐ **DICHIARATIVA IN CORSO** (legittimo per PFTE M+3; certificazione richiesta per Type Cert HALE Phase C) |
| **GDPR Reg. UE 2016/679 + D.Lgs. 196/2003 novellato** | Cap. 5 §5.6, A.11 §A.11.3.2 (priva-cy), A.12 §A.12.2.8 (salute pub. EMI) | `fonti/CELEX_32016R0679` (non in repo, ma testo normativo accessibile pubblicamente); riferimento art. 35 DPIA + D.Lgs. 101/2018 novella | ◐ **PARZIALE** (DPIA pubblica DR-006 ancora parziale; workshop Garante M+12 raccomandato) |
| **NIS2 Direttiva 2022/2555 + D.Lgs. 138/2024** | Cap. 5 §5.7.1, A.2 RSK-REG-027 | Riferimento normativo + RSK-REG-027 Open-Critical Y0+ immediato; registrazione ACN entro M+1 | ◐ **DICHIARATIVA + ACTION ITEM URGENT** (CISO assunzione M+6 = condizione esecuzione) |
| **EASA Part-IS Reg. UE 2023/203** | Cap. 5 §5.7, A.2 RSK-REG-019 | Riferimento normativo + RSK-REG-019 Showstopper aggiuntivo; ISMS implementazione M+9; ISO 27001 M+12 | ◐ **DICHIARATIVA + ACTION ITEM URGENT** |
| **AI Act Reg. UE 2024/1689** | Cap. 5 §5.7.3 (citato), A.1 SyR-C-007 | Riferimento normativo + SyR-C-007 Open; conformity assessment per ML onboard payload IR | ◐ **DICHIARATIVA** |
| **NASA SE Handbook Rev 2 (NASA/SP-2016-6105)** | Tutti i capitoli + tutti gli allegati | `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md` (full text); §4 RTM + §5 V&V + §6 Interface + §3 Project Life Cycle citati estesamente | ✅ **COMPLETA** |

### 5.2 Verdetto compliance dichiarativa

> ✅ **6/7 dichiarazioni hardcore (PFTE normative) hanno evidence chain documentata in repo (`fonti/`)**.
>
> ◐ **5/11 dichiarazioni in azione**: AS/EN 9100, GDPR DPIA, NIS2 ACN, Part-IS ISMS, AI Act conformity assessment richiedono azioni operative (assunzioni FTE, certificazioni, registrazioni) — coerente con stato M+3 PFTE bozza, gap esplicitato come urgente per gate G3.
>
> ❌ **0 dichiarazioni senza evidence o bluff**: il documento NON dichiara compliance a cose che non ha.

---

## 6. Gap analysis investment-grade

Cosa manca per portare il documento da "PFTE-compliant a livello metodologico per gate G3 interno" a "PFTE investment-grade per bandi pubblici Cooding/PNRR/FESR".

### 6.1 Gap esterni (7 chiusure operative)

Tutti già esplicitati in `riferimenti/audit-rigore-epistemico.md` (15 DR-001..DR-015):

| ID | Gap | Action richiesta | Owner | Deadline |
|---|---|---|---|---|
| **GAP-IG-1** | **LoI Regione Liguria non firmata** | Engagement DGR formale Regione Liguria + Assessorato Coesione + Assessorato Innovazione | snai-funding + CEO | M+6-9 |
| **GAP-IG-2** | **Coopfond bando Cooding 2026 non confermato** (DR-002) | Contatto diretto Coopfond + Legacoop nazionale | snai-funding | M+1 |
| **GAP-IG-3** | **Pre-application ENAC non eseguita** (DR-004) | Domanda formale ENAC + meeting + feedback documentato | aviation-regulatory | M+3-6 |
| **GAP-IG-4** | **Quotation vendor reali mancanti** (DR-003) | RFQ doppia parallela JOUAV + Tekever (template già in `vendor-rfq/`) + reference call con ≥2 operatori EU | vtol-uas-specialist + procurement | M+3-6 |
| **GAP-IG-5** | **DPIA pubblica solo parziale** (DR-006) | Workshop Garante M+12 raccomandato; DPIA v1.0 completa M+5-6; consultazione pubblica comunità Pentema | data-privacy + DPO | M+6 |
| **GAP-IG-6** | **Dichiarazioni di conformità formali firmate mancanti** | Template AS/EN 9100, ISO 9001, ISO/IEC 27001 in corso certificazione → upgrade dichiarazione attiva firmata Firmamento | quality manager + CEO | M+9 |
| **GAP-IG-7** | **Validation RINA/DNV non confermata** (OQ-VV-01) | Engagement RINA o equivalente per audit feasibility study Vol. 1+2+3; budget €35-40k pre-negoziato; deadline M+9 per audit pre-G3 | program-manager | M+9 |

### 6.2 Gap documentali strutturali (4 placeholder/parziali)

| ID | Gap | Action richiesta | Owner | Deadline |
|---|---|---|---|---|
| **GAP-IG-8** | **A.6 CAD non esportato** (placeholder) | Export PNG/PDF planimetria GS fissa + GS mobile + layout hangar + viste 2D CAD HALE | CAD designer | M+6 (v1.5) |
| **GAP-IG-9** | **A.9 CME hangar light build incompleto + scale-up Y2-Y3** | Quantificare opzione B hangar light build + opzioni scale-up multiregionale | snai-funding + procurement | M+6 |
| **GAP-IG-10** | **A.13 documentazione fotografica placeholder** | Sopralluogo Pentema con acquisizione foto F-PENT-001..010 + F-AREA-001..006 + workshop F-STAKE-001..003 | program-manager | M+5-6 |
| **GAP-IG-11** | **Relazione geologica/sismica preliminare GS Pentema mancante** | Screening sismico zona Pentema (Liguria zone sismiche 3-4) + screening geologico per fondazioni hangar | technical advisor | M+9 |

### 6.3 Gap di rigore documentale (3 metodologici)

| ID | Gap | Action richiesta | Owner | Deadline |
|---|---|---|---|---|
| **GAP-IG-12** | **Coverage SyR→SsR 72% < target G2 80%** | Decomporre 9 SyR + formalizzare 3 link (vedi §2.4 sopra), effort 8-12 ore | aerospace-SE | M+5-6 |
| **GAP-IG-13** | **CapEx Y1 sliding timeline non quantificato dettagliatamente** | Cap. 8 + financial-model: scenario "sliding timeline" §9.12 con bridge financing €500k esplicito + cash burn Y1 €2-3M | financial-cfo | M+6 |
| **GAP-IG-14** | **Esclusione formale archeologia non dichiarata** (rel. spec. verifica preventiva interesse archeologico) | Aggiungere nota in Cap. 5 §5.9.1 con motivazione esclusione (no opere fisse significative, hangar in opzione affitto) | aviation-regulatory + legal | M+6 |

### 6.4 Totale gap investment-grade

**14 action item** distribuiti su:
- 7 engagement esterni (M+1 → M+9)
- 4 documentali strutturali (M+5-9)
- 3 metodologici interni (M+5-6)

Nessuno è showstopper strutturale; tutti sono **eseguibili entro il pre-G3** (M+9) con risorse Firmamento + advisors. Il documento al M+3 è una **baseline ragionevole** (citaz. `audit-rigore-epistemico.md` §6) ma **non investment-grade**.

---

## 7. Action items prioritari

In ordine di priorità (urgenza × dipendenze gate G3):

### 7.1 Priorità P0 (M+0-M+3 — già in ritardo se non in corso)

1. **AC-01** — **Registrazione ACN preventiva NIS2** (RSK-REG-027) — Owner: CISO (da assumere) / CEO interim — Deadline: M+1
2. **AC-02** — **Contatto diretto Coopfond per verifica bando Cooding 2026** (DR-002 / GAP-IG-2) — Owner: snai-funding — Deadline: M+1
3. **AC-03** — **RFQ doppia parallela JOUAV + Tekever** (GAP-IG-4 / DR-003) — Owner: vtol-uas-specialist + procurement — Deadline: M+3

### 7.2 Priorità P1 (M+3-M+6 — completamento bozza M+6 = gate G2)

4. **AC-04** — **Pre-application meeting ENAC** (GAP-IG-3 / DR-004) — Owner: aviation-regulatory — Deadline: M+3-6
5. **AC-05** — **Assunzione 3 FTE senior**: CISO + DPO + Head of Regulatory Affairs (RSK-HR-002) — Owner: HR + CFO — Deadline: M+6
6. **AC-06** — **Decomposizione 9 SyR + formalizzazione 3 link** per coverage SyR→SsR 80% G2 (GAP-IG-12) — Owner: aerospace-SE — Deadline: M+5-6 (effort 8-12 ore)
7. **AC-07** — **Engagement DGR Regione Liguria + LoI preliminare** (GAP-IG-1) — Owner: snai-funding + CEO — Deadline: M+6
8. **AC-08** — **Sopralluogo Pentema + documentazione fotografica** (GAP-IG-10) — Owner: program-manager — Deadline: M+5-6
9. **AC-09** — **CAD planimetrie GS+hangar export PNG/PDF** (GAP-IG-8) — Owner: CAD designer — Deadline: M+6
10. **AC-10** — **CME hangar opzione B + scale-up Y2-Y3** (GAP-IG-9) — Owner: snai-funding + procurement — Deadline: M+6
11. **AC-11** — **Workshop pubblico comunità Pentema** (OQ-009 / preludio DPIA) — Owner: data-privacy + community manager — Deadline: M+3-6
12. **AC-12** — **Workshop strutturato 10 cooperative Legacoop** — Owner: snai-funding + Fabrica capofila — Deadline: M+3-6

### 7.3 Priorità P2 (M+6-M+9 — pre-gate G3)

13. **AC-13** — **DPIA v1.0 + consultazione Garante preliminare** (GAP-IG-5 / DR-006) — Owner: data-privacy + DPO — Deadline: M+6-9
14. **AC-14** — **ISMS Part-IS implementazione + pre-audit ENAC** (RSK-REG-019) — Owner: CISO + aviation-regulatory — Deadline: M+9
15. **AC-15** — **AgID/PSN qualification cloud provider** (RSK-REG-021) — Owner: data-privacy + IT + DPO — Deadline: M+9
16. **AC-16** — **Engagement RINA o equivalente per feasibility audit pre-G3** (GAP-IG-7 / OQ-VV-01) — Owner: program-manager — Deadline: M+9
17. **AC-17** — **Dichiarazioni di conformità formali firmate** (AS/EN 9100, ISO 9001, ISO/IEC 27001) (GAP-IG-6) — Owner: quality manager + CEO — Deadline: M+9
18. **AC-18** — **Screening geologico/sismico Pentema GS** (GAP-IG-11) — Owner: technical advisor + Comune Torriglia — Deadline: M+9
19. **AC-19** — **Esclusione formale archeologia in Cap. 5** (GAP-IG-14) — Owner: aviation-regulatory + legal — Deadline: M+6
20. **AC-20** — **Sliding timeline scenario quantificato Cap. 8** (GAP-IG-13) — Owner: financial-cfo — Deadline: M+6

### 7.4 Priorità P3 (M+9-M+11 — chiusura gate G3)

21. **AC-21** — **5 hard conditions C1-C5 status review** (Cap. 10 §10.3.2) — Owner: CEO + program-manager — Deadline: M+10
22. **AC-22** — **Studio v2.0 definitivo per gate G3** (RTM + Risk Reg + DPIA + V&V + Quadro Economico + Strategia finanziamenti) — Owner: full team — Deadline: M+10-11
23. **AC-23** — **Audit semestrale 15 NegR Active** (pre-G3) — Owner: aerospace-SE — Deadline: M+9
24. **AC-24** — **Presentazione formale CdA + Coopfond + Regione Liguria** — Owner: CEO — Deadline: M+11

---

## 8. Verdetto consolidato

### 8.1 PFTE-compliant per gate G3?

> **SÌ — PFTE-compliant a livello metodologico/strutturale per gate G3 interno (M+10/M+11)**.
>
> **NO — non investment-grade per presentazione esterna bandi pubblici (Cooding/PNRR/FESR) senza chiusura dei 14 action items (AC-01..AC-20)**.

### 8.2 Evidenze a supporto del PFTE-compliant

- **18/18 elaborati Allegato I.7** coperti (13 conformi + 5 placeholder/parziali, 0 mancanti)
- **4/4 catene di tracciabilità** verificate numericamente:
  - StNeed→SyR 100%, SyR→V&V 100%, SsR allocazione 100%, 17→28 ereditarietà 100%
  - SyR→SsR 72% (gap aperto con action plan documentato 8-12 ore M+5-6)
  - 25/116 rischi narrati + 91/116 trackati XLSX; 10 showstopper con mitigation/owner/deadline
  - 20/20 INT primarie → 59 sub-interfacce A.4 (mapping esplicito 100%)
- **11 famiglie normative** dichiarate, di cui 6 con evidence chain completa in `fonti/` e 5 con action item documentati (NON dichiarate falsamente)
- **NASA SE methodology** applicata coerentemente (§3 gates, §4 RTM, §5 V&V, §6 ICD)
- **Disciplina epistemica** consolidata: confidence levels, falsifying observations, Red Team review, base-rate awareness, source provenance
- **Boundary conditions B1+B2** mantenute coerentemente in tutti i capitoli + allegati

### 8.3 Caveats onesti

Riprendendo i disclaimer già presenti nello Studio:

1. **Confidence aggregato del corpus**: medium-low (dichiarato in Vol. 2 README + audit-rigore-epistemico §6)
2. **Verdetto Go Condizionato 6A**: probabilità realistica 5-15% scenario A; scenario base atteso (60-80%) è "HOLD con piano regolatorio rafforzato" (Cap. 10 §10.0bis)
3. **Verdetto Hold 6B**: rafforzato post DR-013 (base rate 0% HALE solari commerciali) + DR-014 (capital gap 10-50x)
4. **Validation esterna RINA/DNV**: raccomandata ma non eseguita; budget €35-40k pre-G3
5. **Engagement DR aperti**: 4 ancora completamente aperti (DR-002 Coopfond, DR-003 vendor, DR-005 AGCOM, DR-007 base rate startup IT)

### 8.4 Raccomandazione finale per il management

> **Il management Firmamento Technologies può presentare lo Studio al gate G3 interno (M+10/M+11) come PFTE compliant ex art. 41 D.Lgs. 36/2023 + Allegato I.7**, dichiarando esplicitamente:
> 1. La conformità strutturale del corpus al PFTE
> 2. Il gap di coverage SyR→SsR aperto (72%→target 95% al gate G3) con action plan
> 3. Lo stato di engagement degli stakeholder esterni (15 DR)
> 4. La scelta dichiarata di NON aver fatto validare il documento da RINA/DNV (decisione M+9 raccomandata)
>
> Per **presentazione esterna a bandi pubblici** (Cooding 2026, PNRR Aerospazio, FESR Liguria) il documento richiede l'esecuzione delle 14 action items prioritarie (AC-01..AC-20) entro M+9, con particolare attenzione a:
> - AC-04 pre-application ENAC (sblocca SAIL preliminary → contratti PA → revenue Y1)
> - AC-07 LoI Regione Liguria (anchor customer = pre-condizione gate G3 C1)
> - AC-05 assunzione 3 FTE senior (sblocca RSK-REG critical aggiuntivi + OpEx Y1 +€450-800k)
> - AC-16 RINA/DNV audit (segnale di robustezza per investor + bandi pubblici)
>
> Il documento al M+3 è **autoreflessivamente onesto** sui propri limiti e sulla distanza da investment-grade. Questo è esso stesso un elemento di robustezza metodologica (epistemic-rigor §1 falsifiability + §3 source provenance + §7 base-rate awareness).

---

## 9. Riferimenti audit

- `fonti/2023_0036.md` — D.Lgs. 36/2023 testo integrale + Allegati (Allegato I.7)
- `riferimenti/analisi-fac-simili-IT.md` — mappatura PFTE art. 41 + ENAC AAM + DTA Puglia Grottaglie
- `riferimenti/audit-rigore-epistemico.md` — 15 DR-research-closure (4 chiusi + 6 parziali + 4 aperti)
- `riferimenti/DR-research-closure-M3.md` — desk research M+3 (DR-008/009/011/013 chiusi)
- `studio-di-fattibilita/AUDIT-QUALITY-VOLUME-1.md` — Quality audit + scenario probabilities
- `studio-di-fattibilita/AUDIT-REDTEAM-VOLUME-1.md` + `AUDIT-COMPETITOR-VOLUME-1.md` + `AUDIT-REGULATORY-VOLUME-1.md` — Red Team / Competitor Intelligence / Regulatory Adversary M+3
- `studio-di-fattibilita/README.md` (Vol. 1) + `studio-di-fattibilita/allegati/README.md` (Vol. 2) — stato documentale aggregato
- Tutti i capitoli `cap-00..11-*.md` (Vol. 1, 14.871 righe totali)
- Tutti gli allegati `A1..A13/*.md` + `energy-balance/`, `financial-model/`, `vendor-rfq/`

---

*Fine documento — Audit Completezza vs Art. 41 D.Lgs. 36/2023 + Allegato I.7 — v1.0 — 2026-05-17 — Firmamento Technologies*
