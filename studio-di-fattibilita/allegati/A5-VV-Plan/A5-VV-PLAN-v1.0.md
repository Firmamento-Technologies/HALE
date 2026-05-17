# Allegato A.5 ‑ Verification & Validation Plan v1.0

> **Studio di Fattibilità ‑ Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies, bando Cooding Prototypes
> Volume 2, Allegato A.5
>
> **Versione:** v1.0 (M+3)
> **Conformità:** NASA Systems Engineering Handbook Rev 2 (NASA/SP-2016-6105 Rev 2), §5.3 Verification + §5.4 Validation
> **Allineamento:** cap-03-requisiti-e-RTM §3.7 V&V Plan preliminare, cap-06-analisi-tecnica §6.6 V&V tecnica, cap-09-cronoprogramma-e-gate (Gate G2/G3/G4/G5/G6)
> **Disciplina metodologica:** applicate le regole di rigore epistemico
> **Output Excel companion:** `VV-Plan-v1.0.xlsx` (7 sheet)

---

## A.5.0 Metodologia (NASA SE §5.3-5.4)

### A.5.0.1 Cornice metodologica

Il V&V Plan adotta la metodologia NASA SE Handbook Rev 2 §5.3-5.4 [^1], allineata anche con INCOSE SE Handbook v5 §4.7-4.8 e ECSS-E-ST-10C Rev 1 §5.4. La distinzione **Verification ≠ Validation** è la seguente:

| Aspetto | **Verification** (§5.3) | **Validation** (§5.4) |
|---|---|---|
| Domanda | *"Did we build the system right?"* | *"Did we build the right system?"* |
| Riferimento | Requirements documentati (SyR, SsR, IR) | Stakeholder Needs (StNeeds), expected outcomes operativi |
| Tempistica | Lungo tutto il ciclo (per ogni livello) | Predominante a Phase B/C/D + Operations |
| Output | Pass/Fail vs requirement | Soddisfazione stakeholder (es. NPS PA/cooperative) |

### A.5.0.2 Boundary conditions

In coerenza con `cap-03 §3.0bis`, `cap-06 §6.0bis`, `cap-09 §9.0bis`:

- **B1**: il modello cooperativo Legacoop è scelta strutturale (Firmamento è operatore di servizi, NON OEM aeronautico). La V&V copre **erogazione di servizi**, non vendita di prodotti.
- **B2**: il presente V&V Plan copre il Percorso 6A (Phase A→B→C operativa) e il Percorso 6B (Phase B R&D), NON il deployment HALE full-scale (out-of-scope dello studio, materia di gate post-M+48).

### A.5.0.3 Coerenza con altri allegati

| Allegato | Contributo a V&V |
|---|---|
| A.1 RTM | Source dei 71 requisiti tracciati e dei method V&V (colonna "V&V Method") |
| A.2 Risk Register + FMECA | Source di rischi che il V&V deve mitigare (colonna "Risk-ID link") |
| A.3 Trade Study Reports (DOCFAP) | Decisioni architetturali che il V&V deve verificare |
| A.4 ICD | Interfacce da verificare (IR-XXX requirements) |
| A.6 Energy Balance | Esempio di **Analysis** per SsR-PROP-001 |
| A.7 Link Budget | Esempio di **Analysis** per SyR-P-007, SsR-COMMS-001/004/005 |
| A.8+ V&V documentation | Test plan, test report, qualification matrix |

---

## A.5.1 Approccio V&V, i 4 metodi standard (I/A/D/T)

Allineato a NASA SE Handbook §5.3.2 (Verification methods) [^1] e a INCOSE GtWR Rule R1, ogni requisito è verificato con uno dei 4 metodi standard, eventualmente combinati:

| Codice | Metodo | Definizione | Esempio progetto HALE/VTOL |
|---|---|---|---|
| **I** | Inspection | Verifica documentale o visiva: lettura di datasheet, BoM, label, processo, contratto | `SyR-C-001` Class UAS via vendor DoC; `SyR-C-005` polizza assicurativa BVLOS |
| **A** | Analysis | Calcoli, simulazioni, modeling. Verifica per *analytical proof* | Allegato `A.6` Energy Balance HALE 44°N; Allegato `A.7` Link Budget; FMECA; FTA |
| **D** | Demonstration | Esercizio operativo del sistema (qualitativo): functional demonstration end-to-end | `SyR-F-001` mission EO Pentema; `SyR-O-001` lost-link RTB; `SsR-AVI-003` IMU fault injection |
| **T** | Test | Misure quantitative su prototype o articolo di volo | `SsR-PROP-003` battery cycle test; `SyR-P-004` wind envelope test; `SsR-COMMS-001` RSSI in volo |

**Regola di selezione del metodo** (riferimento NASA SE §5.3.2.2):

1. Se il requisito è documentale o contrattuale → **I**
2. Se il requisito è una prestazione calcolabile da modello validato → **A**
3. Se il requisito è funzionale operativo senza margini quantificati → **D**
4. Se il requisito richiede misura quantitativa con margine → **T**

Combinazioni tipiche per requisiti di alto rischio: **A+T** (analisi pre-test seguita da test di conferma), **D+T** (demo più misura su funzione critica), **I+T** (audit più test).

### A.5.1.1 Distribuzione metodi V&V

Sui 71 requisiti SyR+SsR+IR tracciati in `VV-Plan-v1.0.xlsx` sheet `VV_Matrix_SyR`, la distribuzione (un requisito può combinare più metodi) è:

| Metodo | Conteggio | % | Note |
|---|---|---|---|
| **I** (Inspection) | 23 | 32% | Dominante per famiglia Compliance e Cost |
| **A** (Analysis) | 27 | 38% | Allegati A.6 + A.7 + FMECA + FTA |
| **D** (Demonstration) | 19 | 27% | Concentrato in Phase B test bed |
| **T** (Test) | 30 | 42% | Concentrato in Phase B/C |

> **Falsifying observation A.5.1**: se in Phase A il numero di SyR con metodo "Test" pianificato supera il 60% del totale, il piano è sovra-dimensionato in costi test e va rivisto verso più Analysis/Demonstration.

---

## A.5.2 V&V Matrix per SyR

La matrice completa risiede nel file Excel sheet `VV_Matrix_SyR` con 71 righe (SyR + SsR + IR + VR). Estratto rappresentativo (10 righe top-priority):

| Req-ID | Description | Method | Phase | Owner | Risk link |
|---|---|---|---|---|---|
| SyR-F-003 | Rileva hotspot ≥40°C, alert ≤5 min | D+T | B,C | EO-expert | RSK-OPS-002 |
| SyR-P-001 | Autonomia sortie ≥4 h con payload 4 kg | A+T | A,C | team propulsione e energia | – |
| SyR-P-007 | C2 link RF range ≥30 km LOS, fade margin ≥12 dB | A+T | A,C | telecom-payload | RSK-TEC-005 |
| SyR-S-002 | FTA top event "Loss of Vehicle BVLOS" ≤ 10⁻⁵/h | A | A | systems-engineer | RSK-TEC-007 |
| SyR-C-002 | ConOps SORA SAIL ≤III Pentema BVLOS auth ENAC | I | Pre-A,A | aviation-regulatory | RSK-REG-002 |
| SsR-PROP-001 | Energy balance HALE inverno 44°N margine ≥20% | A | A | team propulsione e energia | RSK-TEC-001 |
| SsR-AERO-003 | Flutter speed margin ≥20% rispetto VD | A+T | B | aero-structures-engineer | RSK-TEC-002 |
| SsR-AVI-002 | GNSS spoofing/jamming detection + alert | T | B | team avionica e GNC | RSK-TEC-005 |
| SsR-COMMS-005 | HAPS feeder link Ka 31 GHz availability 99.9% | A | A,B | telecom-payload | – |
| SsR-HALE-001 | HALE subscale 1:3 prototype TRL 5 by M+36 | D+T | B (6B) | aero-structures-engineer | RSK-TEC-002 |

**Status legend**:
- **Done** (verde): V&V eseguito e passato (es. SsR-PROP-001 con A.6 Energy Balance Report)
- **Planned** (bianco): metodo definito, esecuzione in corso o pianificata
- **Open** (rosso): requisito da chiudere prima del gate target

> **Falsifying observation A.5.2**: se al M+10 (gate G3) il numero di SyR con status "Open" supera il 10% del totale, il V&V coverage non è investment-grade.

---

## A.5.3 V&V Plan Percorso 6A (Phase A → Phase B → Phase C)

### A.5.3.1 Pre-Phase A (M+0-3), inspection compliance documentale

Obiettivo: chiudere tutti i requisiti di compliance documentale prima dell'avvio Engineering.

| Attività | Owner | Deliverable | Status M+3 |
|---|---|---|---|
| Compliance matrix SyR-C-001..C-006 | consulenza legale-regolatoria aviazione + telecom-payload + consulenza privacy e protezione dati | Allegato `A.5.x` Compliance matrix v1 | Planned |
| Stakeholder workshop + StNeeds collection | team SNAI e funding territoriale | StNeeds-001..017 + provenance log | In progress |
| Vendor selection preliminary VTOL (datasheet review) | team VTOL UAS specialistico | Vendor short-list + DoC review | Done (3 candidati: JOUAV, Tekever, Quantum) |

### A.5.3.2 Phase A (M+3-12), analysis

| Attività | Tipo | Allegato output | Deadline | Owner |
|---|---|---|---|---|
| **Link budget RF** (4 link analizzati) | A | A.7 | M+6 | telecom-payload |
| **Energy balance HALE 44°N** (annual + sensitivity) | A | A.6 | M+10 | team propulsione e energia |
| **FMECA payload + propulsion + avionics** | A | A.2 | M+9 | systems-engineer |
| **FTA "Loss of Vehicle in BVLOS"** | A | A.2 | M+10 | systems-engineer |
| **Trade Study reports** (TS-PLATFORM, TS-MATERIAL, TS-PROP-6B, TS-AVI, TS-PAYLOAD, TS-COMMS) | A | A.3 DOCFAP | M+9 | aerospace-SE |
| **ENAC pre-application + SORA stima GRC** | I + A | A.5.x SORA pre-doc | M+9 | aviation-regulatory |
| **AGCOM spectrum consultation + plan** | I + A | A.5.x Spectrum plan | M+10 | telecom-payload |
| **DPIA preliminary + Garante engagement** | I | A.5.x DPIA prelim | M+9 | consulenza privacy e protezione dati |

Per ogni Analysis l'output include la lista delle **assunzioni dichiarate** e l'**uncertainty quantification** (sensitivity sweep). Vedi convenzione `cap-03 §3.1.4` (epistemic discipline).

### A.5.3.3 Phase B (M+12-24), demonstration test bed e Test subscale

La Phase B 6A corrisponde alla messa in opera del **pilota Pentema** e comprende test bed integrato e prime missioni reali.

| Test | Tipo | Facility | Periodo | Owner |
|---|---|---|---|---|
| GS test bed setup + walkthrough | D | GS Pentema | M+12-15 | aerospace-SE |
| HIL simulator FCS fault injection | D | HIL bench in-house o partner | M+13-20 | team avionica e GNC |
| Range test ground RF + payload swap | T | Albenga/Pentema range | M+14-18 | telecom-payload |
| Climatic chamber test (-10/+30°C) | T | External lab (Pavia/Milano) | M+15-18 | team VTOL UAS specialistico |
| EMC test (EN 55032 + DO-160G §20) | T | IMQ/ICIM/TUV | M+15-18 | team avionica e GNC |
| Parachute drop test | T | In-house drop rig | M+13-15 | team VTOL UAS specialistico |
| GNSS spoofing detection test | T | GNSS simulator (Spirent/Skydel) | M+14-16 | team avionica e GNC |
| Battery thermal runaway (UN 38.3) | T | CNR-ITAE / accredited | M+13-15 | team propulsione e energia |

### A.5.3.4 Phase C (M+9-24), test full-scale e operational validation

La Phase C 6A inizia con l'**autorizzazione ENAC** (M+9) e con le prime missioni operative reali, sovrapponendosi alla Phase B.

| Attività | Tipo | Facility | Periodo | Owner |
|---|---|---|---|---|
| Flight test BVLOS Pentema + GATB Grottaglie | T | Sito Pentema + GATB | M+9-12 | team VTOL UAS specialistico |
| Hotspot detection field trial (fuoco controllato) | D+T | Sito Pentema con autorizzazione | M+11-14 | EO-expert |
| Operations validation Y1 (≥50 missioni) | D | Pentema operativo | M+10-24 | program-manager |
| Customer feedback collection (Regione, PC, coop) | I | NPS survey + meeting | M+12-24 | team strategia business model |

> **Gate G4 (M+12)** entry criteria collegati a V&V:
> - ≥50 missioni completate senza FATAL/major
> - Flight test report consolidato
> - HIL test report disponibile
> - EMC + climatic certs in mano
> - Insurance polizza attiva (SyR-C-005)

---

## A.5.4 V&V Plan Percorso 6B (R&D Phase B)

Il Percorso 6B opera in regime **R&D Phase A/B**: la V&V copre soltanto lab, subscale ground e (auspicabilmente) il primo subscale stratospheric flight. La Phase C/D HALE full-scale resta **out-of-scope** dello Studio attuale.

### A.5.4.1 M+24-30, lab test subsystem

Pre-requisito: il gate **G5** (M+24) ha approvato la Phase B 6B.

| Test | Allegato output | Facility | Owner |
|---|---|---|---|
| Solar panel efficiency (IEC 60904 AM1.5) | Cert IEC | ENEA Casaccia o EURAC Bolzano (TUV cert) | team propulsione e energia |
| Battery LiS/SS-Li pack-level cycle test | Cycle curve + cert | In-house o CNR-ICMATE | team propulsione e energia |
| UV degradation accelerated (ASTM G154/G155) | UV test report | UV chamber lab | team propulsione e energia |
| Composite layup test panel (CFRP/lino skin) | Material qual report | UniGE DICCA / POLITO DIMEAS | aero-structures-engineer |

### A.5.4.2 M+30-36, subscale prototype 1:3 ground tests

Pre-requisito: lab tests M+24-30 passati.

| Test | Allegato output | Facility | Owner |
|---|---|---|---|
| Wind tunnel subscale 1:3 | WT report | POLITO/CIRA wind tunnel | aero-structures-engineer |
| GVT (Ground Vibration Test) subscale | Modal analysis | POLITO DIMEAS / CIRA | aero-structures-engineer |
| Aeroelastic correlation analysis | p-k flutter analysis | CFD/CSD coupled solver | aero-structures-engineer |
| Subscale propulsion integration test | Cell test | In-house o partner | team propulsione e energia |
| Avionics HIL stratospheric envelope | HIL strat report | In-house o DiPSIM | team avionica e GNC |

> **Gate G6 (M+36)** entry criteria collegati a V&V:
> - TRL subsystem critici ≥ 5
> - Energy balance simulazione completa con scenario inverno chiarito (margine ≥20% o fallback seasonal)
> - GVT report + flutter margin verificato
> - Wind tunnel + subscale propulsion test passati

### A.5.4.3 M+36-48, subscale flight test stratosferico

Per il Continue Phase B post-G6:

| Test | Allegato output | Facility | Owner |
|---|---|---|---|
| Subscale stratospheric flight ascent | Flight test report | ESRANGE Kiruna o partner ASI Sardegna | aero-structures-engineer |
| Perennial flight >24h (target Phase C 6B) | Flight log | Site partner | aero-structures-engineer |

> **Phase C+ 6B (out-of-scope studio attuale)**: full-scale HALE flight test stratosferico continuo, Type Certification, deployment commerciale. Materia di gate futuri post-M+48 e di funding consortia (EDF, Horizon Europe, eventuale EU sovereign HAPS initiative).

---

## A.5.5 V&V per tipologia subsistema

Allineato con la tabella di `cap-06 §6.6`:

### A.5.5.1 AERO/Struct

```
Phase A: XFLR5 / AVL low-fidelity polare (Analysis)
 Calcoli analitici + FEA preliminare (Analysis)
 ↓
Phase B: CFD RANS + wind tunnel subscale 1:5 (Analysis + Test)
 Test panel + structural test subscale (Test)
 ↓
Phase C: GVT + flight test load envelope (Test)
 Flight test full-scale aerodynamic (Test)
```

Output deliverables: aerodynamic polare report, FEA report, WT report, GVT report, flight test load envelope.

### A.5.5.2 PROP/Energy

```
Phase A: Modello energy balance + sensitivity (Analysis, Allegato A.6)
 ↓
Phase B: Test cell pannelli (IEC 60904) (Test)
 Battery pack-level cycle test (Test)
 UV degradation accelerated (Test)
 ↓
Phase C: Test integrato subscale propulsione (Test)
 Perennial flight HALE (Test)
```

Output deliverables: A.6 energy report, IEC 60904 cert, battery cycle cert, UV cert, propulsion integration test report.

### A.5.5.3 AVI/GNC

```
Phase A: Architecture document + DAL allocation (Inspection + Analysis)
 ↓
Phase B: HIL simulation (fault injection) (Demonstration + Test)
 GNSS spoofing detection (Test)
 IMU redundancy 2-of-3 voting (Demonstration)
 ↓
Phase C: Ground test integrato (Test)
 Flight test BVLOS (Test)
```

Output deliverables: DO-178C trace matrix (se autopilot custom), HIL test report, GNSS test report, IMU fault test report, flight test BVLOS log.

### A.5.5.4 PAY (Payload EO/IR/Telecom)

```
Phase A: Bench-level functional test (Demonstration)
 Camera/IR spec verification (Inspection)
 ↓
Phase B: Camera MTF calibration (Test)
 IR NEdT calibration (blackbody INRIM) (Test)
 Edge AI ROC curve (Analysis + Test)
 ↓
Phase C: Fly-and-measure missioni reali (Test)
 Operations validation (Demonstration)
```

Output deliverables: MTF report, NEdT cert, FAR ROC curve, fly-and-measure report.

### A.5.5.5 COMMS

```
Phase A: Link budget analysis (Allegato A.7) (Analysis)
 ↓
Phase B: Range test ground RF (Test)
 Crypto bench test + pen-test (Test)
 Antenna pattern measurement (Test)
 ↓
Phase C: RSSI in volo + fade margin measured (Test)
 Throughput iperf in flight (Test)
```

Output deliverables: A.7 link budget Excel, range test report, crypto/pen-test report, antenna pattern report, in-flight RSSI log.

### A.5.5.6 GS (Ground Segment)

```
Phase A: Architecture walkthrough (Inspection)
 ↓
Phase B: Integrated test bed end-to-end (Demonstration)
 Latency test end-to-end (Test)
 ↓
Phase C: Operations validation 24/7 (Demonstration)
 Drill simulato outage (Demonstration)
```

Output deliverables: GS test bed report, end-to-end latency report, operations drill log, 24/7 monitoring dashboard.

---

## A.5.6 V&V Test Facilities required

Catalogo completo nel file Excel sheet `Test_Facilities` (16 facility). Sintesi per categoria:

| Categoria | N. facility | Owner principale | CapEx tot [k€] | OpEx/anno [k€] |
|---|---|---|---|---|
| Ground Segment | 1 | In-house | 35 | 20 |
| Avionics/GNC | 2 | In-house + esterno | 80 | 45 |
| Comms | 1 | In-house | 20 | 10 |
| Aero (wind tunnel) | 2 | Partner academic | 0 | 130 |
| Structures (GVT) | 1 | Partner academic | 0 | 60 |
| Energy (panel + battery) | 2 | Partner + in-house | 40 | 35 |
| Environmental (climatic + EMC) | 2 | External lab | 0 | 50 |
| Payload (IR cal) | 1 | INRIM Torino | 0 | 10 |
| Safety (drop rig + GNSS sim + battery abuse) | 3 | Mix | 15 | 40 |
| Flight Test (Pentema/GATB/Sardegna) | 2 | Partner | 20 | 230 |
| **Totale** | **17** | – | **210** | **630** |

> **Falsifying observation A.5.6**: 6 facility critiche dipendono da partner accademici/industriali (POLITO, CIRA, ENEA, EURAC, IMQ, ICIM). Se almeno 2 partner non confermano disponibilità entro M+18, la timeline Phase B 6A slitta di 3-6 mesi.

### A.5.6.1 Facility critiche con preavviso lungo (>6 mesi booking)

1. **Wind tunnel POLITO/CIRA** (Phase B 6B): booking 12 mesi anticipo. Engagement formale entro M+12.
2. **GVT POLITO DIMEAS** (Phase B 6B): booking 6 mesi anticipo. Engagement entro M+24.
3. **Stratospheric test site** (Sardegna o ESRANGE Kiruna): partnership e permissions a 12-18 mesi. Engagement entro M+24-30.
4. **EMC chamber IMQ/ICIM** (Phase B 6A): booking 3-6 mesi anticipo. Engagement entro M+12.

---

## A.5.7 Test schedule alignment con Gate G2 + G3 + G4 + G5 + G6

Gantt completo nel file Excel sheet `Test_Schedule` (21 attività). Sintesi per gate:

### A.5.7.1 Gate G2 (M+6), Architecture Baselined

V&V entry criteria:
- Stakeholder workshop completed + StNeeds raccolti (Pre-A)
- Vendor short-list VTOL via datasheet inspection (Pre-A)
- Link budget preliminare 4 link analizzati (A.7 v0.5)
- FMECA preliminary in corso (A.2 v0.5)
- Trade Study reports preliminari (A.3 v0.5)

### A.5.7.2 Gate G3 (M+10/M+11), FEASIBILITY GATE PRIMARIO

V&V entry criteria (esaustivi):
- Link budget v1.0 (A.7): 14 scenari analizzati, 12 OK / 2 marginal
- Energy balance v1.0 (A.6): annual + sensitivity, decisione perennial vs seasonal
- FMECA completo (A.2 v1.0): top 10 risk con mitigation
- FTA "Loss of Vehicle BVLOS" (A.2 v1.0): target 10⁻⁵/h verificato
- Trade Study reports completi (A.3 DOCFAP): 6 trade study chiusi
- ENAC pre-application feedback ricevuto (SyR-C-002 status: Open → In progress)
- AGCOM spectrum consultation iniziata (SyR-C-003)
- DPIA preliminary completa + Garante engagement (SyR-C-004)
- Independent verification (RINA o equivalent) iniziata o completata
- V&V plan v1.0 (presente documento) consolidato

### A.5.7.3 Gate G4 (M+12), fine Pilota VTOL 6A

V&V entry criteria:
- ENAC operational autorizzazione ricevuta (M+9)
- Flight test BVLOS Pentema completed (M+9-12)
- ≥50 missioni operative completate
- HIL test report disponibile (SsR-AVI-002, SsR-AVI-003)
- EMC cert + climatic test cert
- Insurance polizza BVLOS attiva (SyR-C-005)

### A.5.7.4 Gate G5 (M+24), evaluation HALE Phase B

V&V entry criteria 6B:
- Energy balance HALE inverno chiarito (A.6 v2.0 con scenario worst-case meteo)
- Roadmap V&V Phase B 6B aggiornata (lab + subscale ground + flight)
- Funding readiness Phase B ≥50% commitment (proxy: budget V&V Phase B 6B €730k coperto)
- Engagement EuroHAPS / CIRA / partner academic formalizzato

### A.5.7.5 Gate G6 (M+36), HALE Phase B Midterm

V&V entry criteria:
- Solar panel cert IEC 60904 (SsR-PROP-002)
- Battery cycle test cert (SsR-PROP-003)
- Wind tunnel subscale 1:3 report (SsR-AERO-001 Phase B 6B)
- GVT report + flutter margin (SsR-AERO-003, SsR-HALE-004)
- Subscale prototype TRL 5 (SsR-HALE-001)

---

## A.5.8 V&V documentation deliverables

Per ogni V&V activity, l'output documentale è strutturato come segue (NASA SE §5.3.2.4):

### A.5.8.1 Test Plan (pre-test)

Template minimo per ogni test:
1. **Test ID** (riferimento a SyR/SsR/IR)
2. **Test objective** (requisito target)
3. **Test setup** (facility, articolo di volo, configurazione)
4. **Test procedure** (step-by-step)
5. **Pass/Fail criteria** (quantitativi)
6. **Risk assessment** (safety of test)
7. **Data collection plan** (sensor list, sampling rate, formato)

### A.5.8.2 Test Report (post-test)

Template minimo:
1. **Test ID** + Test Plan reference
2. **Test conditions** (effettive vs nominali)
3. **Data sheet** (raw measurements)
4. **Data reduction** (con uncertainty budget)
5. **Pass/Fail verdict**
6. **Anomalies / deviations**
7. **Lessons learned**
8. **Sign-off** (test director + indep. reviewer)

### A.5.8.3 Qualification Matrix (consolidata)

Matrice riassuntiva consolidata pre-Gate G3: per ogni requisito, riferimento al test report che lo verifica e status verdict (Pass / Conditional Pass / Fail / Waived).

Output: file Excel `Qualification-Matrix-v1.0.xlsx` (da preparare per G3, M+10-11).

### A.5.8.4 Lista deliverable V&V attesi al Gate G3

| Deliverable | Output type | Owner | Status M+3 |
|---|---|---|---|
| A.5 V&V Plan v1.0 | Markdown + Excel | aerospace-SE (V&V manager) | **Done (presente documento)** |
| A.6 Energy Balance Report v1.0 | Markdown + Python + Excel | team propulsione e energia | Done |
| A.7 Link Budget Report v1.0 | Markdown + Python + Excel | telecom-payload | Done |
| A.2 Risk Register + FMECA + FTA | Markdown + Excel | systems-engineer | In progress |
| A.3 Trade Study Reports (DOCFAP) | Markdown × 6 | aerospace-SE | In progress |
| A.5.x ENAC pre-application doc | PDF formale | aviation-regulatory | Planned M+9 |
| A.5.x AGCOM spectrum plan | Markdown | telecom-payload | Planned M+9 |
| A.5.x DPIA preliminary | PDF + workshop log | consulenza privacy e protezione dati | Planned M+9 |
| A.5.x Compliance Matrix v1 (SyR-C series) | Excel | aviation-regulatory | Planned M+10 |
| Qualification Matrix v1.0 (pre-G3) | Excel | aerospace-SE | Planned M+10 |
| Independent verification report (RINA/DNV) | PDF | program-manager | Planned M+11 |

---

## A.5.9 Independent verification (RINA, DNV, third-party)

### A.5.9.1 Filosofia

Lo Studio di Fattibilità HALE/VTOL non si reputa sufficiente con il solo self-assessment Firmamento Technologies. L'**independent verification** da parte di un ente terzo riconosciuto risulta raccomandata per tre ragioni: aumentare la confidence presso i finanziatori (Coopfond, PNRR, EDF, Horizon Europe), aprire la strada a future certificazioni AS/EN 9100 + ISO 9001, validare la metodologia V&V con peer review esterna.

### A.5.9.2 Indep. Verification Plan

Catalogo completo nel file Excel sheet `Independent_Verification` (9 review). Sintesi:

| Scope | Body | Phase | Mandatory | Cost [k€] |
|---|---|---|---|---|
| **Feasibility audit overall (Vol.1+2+3)** | RINA preferito (o DNV / SGS) | A (M+9-11) | Recommended | 35 |
| ConOps SORA + GRC validation | ENAC pre-application | A (M+3-9) | **Necessary** | 0 |
| Cybersecurity NIS2 audit | ACN-accredited firm | B (M+12-18) | **Necessary** | 18 |
| DPIA + GDPR audit | 3rd-party data privacy counsel | A (M+3-9) | **Necessary** | 12 |
| Wind tunnel test report (subscale) | POLITO DIMEAS / UniGE DICCA | B 6B (M+24-30) | **Necessary** Phase B 6B | 0 (rental) |
| GVT modal analysis | POLITO / CIRA | B 6B (M+30-36) | **Necessary** Phase B 6B | 0 (rental) |
| Solar panel cert IEC 60904 | ENEA Casaccia o EURAC Bolzano (TUV) | B 6B (M+24) | **Necessary** | 0 (rental) |
| Battery thermal runaway UN 38.3 | CNR-ITAE / accredited lab | B 6B (M+24-30) | **Necessary** | 20 |
| EMC compliance EN 55032 + DO-160G | IMQ / ICIM / TUV | B 6A (M+15-18) | **Necessary** ENAC | 30 |
| **TOTAL** | – | – | – | **115** |

### A.5.9.3 Decisione "RINA o equivalente per G3"

**Domanda Open Question** (cf. cap-09 §9.10.3 OQ-S03): RINA o equivalente entro M+9 per l'audit del feasibility study Vol. 1+2+3 è disponibile?

- **Pros**: RINA è notification body riconosciuto IT/EU, ha esperienza aerospace/marine, l'audit risulta credibile per i finanziatori.
- **Cons**: costo €35k (1.5% del CapEx Y1), response time 4-6 settimane.

**Raccomandazione V&V manager**: procedere con RINA feasibility audit pre-G3 come investment-grade upgrade. Il costo €35k è marginale rispetto al rischio reputazionale di consegnare uno Studio non validato esternamente.

---

## A.5.10 Open Questions

Le V&V open questions tracciate per i gate successivi:

| OQ-ID V&V | Domanda | Trigger per chiusura | Owner | Deadline |
|---|---|---|---|---|
| OQ-VV-01 | Disponibilità RINA o equivalente per feasibility audit G3? | Engagement formale entro M+9 | program-manager | M+9 |
| OQ-VV-02 | Quale partner academic per wind tunnel subscale 1:3 (POLITO vs CIRA vs UniGE)? | Negoziazione + booking | aero-structures-engineer | M+18 |
| OQ-VV-03 | Quale battery cycler lab (in-house build vs CNR-ICMATE partnership)? | Decisione CapEx vs OpEx | team propulsione e energia | M+15 |
| OQ-VV-04 | HIL simulator: build in-house vs partner DiPSIM? | Trade-off costo + tempo | team avionica e GNC | M+12 |
| OQ-VV-05 | Quale partner stratospheric test site (Sardegna ASI vs ESRANGE Kiruna)? | Engagement formale + funding Phase B | aero-structures-engineer | M+24 |
| OQ-VV-06 | Engagement INRIM Torino per IR cal blackbody: formal contract? | LoI + Q4 booking | EO-expert | M+12 |
| OQ-VV-07 | Indep. verification cybersecurity NIS2: quale audit firm (Deloitte, PwC, in-house ACN partner)? | RFP + valutazione | aerospace-SE | M+15 |
| OQ-VV-08 | Tasso copertura V&V matrix al Gate G3: target 95% requirement con method+phase definito; valore baseline M+3 = 89% (63/71). Gap da chiudere = 8 requisiti (per lo più SsR-HALE Phase B/C HALE) | Update RTM | aerospace-SE | M+10 |

### A.5.10.1 Falsifying observations

> **A.5.10.1** Se al M+10 (gate G3) il numero di SyR con status V&V "Open" supera il 10% del totale, il V&V coverage non è investment-grade. Trigger automatico per HOLD verdict gate G3 (non No-Go).

> **A.5.10.2** Se al M+18 almeno 2 partner accademici (POLITO, CIRA, ENEA, EURAC) non hanno confermato la disponibilità delle proprie facility, la timeline Phase B 6A/6B slitta di 3-6 mesi.

> **A.5.10.3** Se al M+12 il flight test BVLOS Pentema rivela un margine link budget RF < 6 dB (vs A.7 analysis prediction ≥12 dB), il modello A.7 va re-baseline con dati di campo (model V&V failure).

> **A.5.10.4** Se al M+15 l'EMC test fallisce per emissioni radiate sopra la soglia DO-160G §20, sarà richiesto un re-design della schermatura payload più re-test, con impatto di 2-3 mesi sullo slip del gate G4.

> **A.5.10.5** Se al M+30 la wind tunnel subscale 1:3 mostra un divergence speed margin inferiore al 10% rispetto a VD (target ≥20%), il design HALE Phase B 6B va re-engineered con engagement di aeroelastic specialist esterno.

---

## A.5.11 V&V Risk Register (estratto)

Rischi specifici della V&V che possono compromettere il piano:

| RSK-VV-ID | Rischio | P | I | Score | Mitigation |
|---|---|---|---|---|---|
| RSK-VV-001 | Indisponibilità wind tunnel partner Phase B 6B | 3 | 4 | 12 | Multi-vendor strategy (POLITO + CIRA + UniGE backup), booking anticipato M+12 |
| RSK-VV-002 | Flight test BVLOS Pentema bloccato da meteo > 3 mesi | 3 | 3 | 9 | Schedule estate prioritario + GATB Grottaglie come backup |
| RSK-VV-003 | EMC test fail prima volta (re-design schermatura) | 2 | 3 | 6 | EMC pre-screening interno + chamber commercial pre-emission scan |
| RSK-VV-004 | Cyber pen-test rivela vuln. critiche (release rinviato) | 2 | 4 | 8 | Pen-test interno preventivo Q1 2027, fix backlog dedicato |
| RSK-VV-005 | RINA feasibility audit non confirmable entro M+9 | 2 | 3 | 6 | Plan B: DNV o SGS; budget €40k pre-negoziato |
| RSK-VV-006 | Battery thermal runaway test fail (LiS pack instabile) | 3 | 4 | 12 | Vendor screening + cell-level test pre-pack assembly |
| RSK-VV-007 | INRIM Torino IR blackbody non disponibile in finestra | 2 | 2 | 4 | Partner alternative (DLR Germany, ESA ESTEC backup) |

---

## A.5.12 Note di chiusura

Il presente V&V Plan v1.0 costituisce il **deliverable baseline** richiesto per il **Gate G3 (M+10/M+11) FEASIBILITY GATE PRIMARIO**. Esso:

1. **Traccia 71 requisiti** SyR + SsR + IR (sopra il target minimo 60-70 dichiarato in `cap-03 §3.7`)
2. **Allinea ogni requisito** con metodo V&V (I/A/D/T), fase NASA SE (Pre-A/A/B/C), owner specialista, test facility, document evidence, risk link, trade study link
3. **Fornisce gantt schedule** allineato con i 5 gate (G2/G3/G4/G5/G6)
4. **Quantifica i costi** test (CapEx €210k + OpEx €630k Y1+Y2 + Phase B 6B €730k)
5. **Definisce strategia independent verification** con RINA preferred per il G3 audit

### A.5.12.1 Update plan

| Versione | Mese | Trigger | Note |
|---|---|---|---|
| v1.0 (presente) | M+3 | Baseline | 71 requisiti, allineamento G2-G6 |
| v1.5 | M+6 | Post G2 | Aggiornamento method+phase per i 6 SyR aperti (cf. cap-03 §3.8.2) |
| v2.0 | M+10 | Pre G3 | Versione consegna gate G3 + Qualification Matrix v1.0 |
| v2.5 | M+12 | Post G4 | Lessons learned da Y1 ops + aggiornamento test bed Phase B 6A |
| v3.0 | M+24 | Pre G5 | Estensione full Phase B 6B HALE |

### A.5.12.2 Coerenza epistemica

In coerenza con rigore epistemico:
- Ogni V&V method dichiarato risulta **falsificabile**: se il test fallisce, il requisito è violato.
- Ogni Analysis include **assunzioni esplicite** e sensitivity sweep.
- Ogni cost figure dichiara la propria **source/vendor** (cf. sheet `Test_Costs`).
- Le 8 Open Questions sono **tracciate** con owner e deadline.
- I 7 V&V risks sono **integrati** nel Risk Register principale (A.2).

### A.5.12.3 Statement di limiti

1. **Numerosità requisiti**: 71 SyR+SsR+IR è baseline minima. La V&V matrix completa per Type Certification HALE (Phase C+ 6B) richiede tipicamente 500-1500 requisiti. Out-of-scope studio attuale.
2. **TRL targets**: il piano assume TRL 8-9 commerciali per 6A (vendor delivery) e TRL 5 subsystem per 6B (M+36). Se il vendor 6A consegna un TRL inferiore (es. 7), il V&V plan va esteso con qualification testing aggiuntivo.
3. **Indep. verification**: solo RINA feasibility audit è budgetato per G3. La V&V indipendente completa (notification body per Type Cert) rimane materia di Phase C HALE, out-of-scope.

---

## A.5.13 Riferimenti

[^1]: NASA Systems Engineering Handbook Rev 2 (NASA/SP-2016-6105 Rev 2). Source: `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md`. Specifico: §5.3 Verification Process + §5.4 Validation Process. Confidence: high.

[^2]: INCOSE Systems Engineering Handbook v5 (2023). §4.7 Verification + §4.8 Validation. Confidence: high.

[^3]: ECSS-E-ST-10-02C Rev 1, Space engineering, Verification (ESA). Reference per V&V planning aerospace. Confidence: high.

[^4]: RTCA DO-178C, Software Considerations in Airborne Systems and Equipment Certification. Reference per DAL allocation autopilota (SsR-AVI-001). Confidence: high.

[^5]: RTCA DO-160G, Environmental Conditions and Test Procedures for Airborne Equipment. Reference per environmental test (SyR-E-001, SyR-E-005). Confidence: high.

[^6]: SAE ARP4761, Guidelines and Methods for Conducting the Safety Assessment Process on Civil Airborne Systems and Equipment. Reference per FMECA + FTA (SyR-S-001, SyR-S-002). Confidence: high.

[^7]: IEC 60904, Photovoltaic devices, Measurement methods. Reference per solar panel test (SsR-PROP-002). Confidence: high.

[^8]: UN Manual of Tests and Criteria, Section 38.3, Lithium batteries. Reference per battery transport + flight clearance (SyR-S-005). Confidence: high.

[^9]: EN 55032 / CISPR 32, Electromagnetic compatibility of multimedia equipment. Reference per EMC compliance (SyR-E-005). Confidence: high.

[^10]: D.Lgs. 36/2023 art. 41 + Allegato I.7 (PFTE Progetto di Fattibilità Tecnico-Economica). Reference per allineamento V&V Plan con framework italiano. Confidence: high.

[^11]: EU Regulation 2019/947 (Specific Category UAS) + AMC/GM. Reference per SORA SAIL Pentema BVLOS (SyR-C-002). Confidence: high.

[^12]: ENAC Linee Guida U-Space LG-2023/006. Reference per integrazione U-Space (SyR-O-006). Confidence: high.

[^13]: AGCOM Delibera 93/26/CONS, Piano Nazionale di Ripartizione delle Frequenze. Reference per spettro radio (SyR-C-003). Confidence: high.

[^14]: NIS2 Directive (EU) 2022/2555 + ACN Italia transposition. Reference per cybersecurity audit (SyR-C-006). Confidence: high.

[^15]: GDPR (EU) 2016/679 + Garante Privacy guidelines. Reference per DPIA (SyR-C-004). Confidence: high.

---

**FINE Allegato A.5 v1.0**

*Generato 2026-05-17, Firmamento Technologies, Studio di Fattibilità HALE/VTOL, Volume 2 Allegato A.5*
