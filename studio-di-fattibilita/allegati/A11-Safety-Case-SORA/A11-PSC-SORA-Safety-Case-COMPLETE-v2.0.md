# Allegato A.11 : SORA Safety Case COMPLETE v2.0

> **Volume 2 : Allegato A.11 (versione estesa)**
> **SORA Safety Case Preliminary-Grade** per supporto **Pre-Application Meeting ENAC**
> Conformità: **EASA SORA 2.5 (ED Decision 2025/018/R, 15 settembre 2025)** + **Reg. (UE) 2019/947** + **ENAC Regolamento APR Ed.3 (2019) + Em.1 (2020)**
> **Versione**: 2.0, Maggio 2026 (M+3 baseline)
> **Operatore proponente**: Firmamento Technologies S.r.l. (in registrazione UAS Operator ENAC)
> **Author**: `aviation-regulatory-counsel` (HALE Studio di Fattibilità)
> **Stato**: PRELIMINARY, per istruttoria pre-application; **NON sostituisce** la SORA application formale ex art. 11 Reg. (UE) 2019/947.

---

## CAVEAT METODOLOGICO E SCOPO DEL DOCUMENTO

Il presente Safety Case ha **finalità di supporto al Pre-Application Meeting con ENAC** (Direzione Regolamentazione UAS) per il Percorso 6A, VTOL pilota Pentema. Esso costituisce **iterazione preliminary-grade** del SORA, conforme alla struttura europea SORA 2.5 codificata dall'**EASA Amendment 3 a Issue 1 AMC/GM Reg. (UE) 2019/947** (ED Decision 2025/018/R del 15 settembre 2025). Il documento **non possiede** lo status di:

1. **SORA Application formale** ex art. 11 Reg. (UE) 2019/947 (richiede Operations Manual completo, evidenze design assurance vendor, training records, Maintenance Manual approved)
2. **Investment-grade Safety Case** (per finanziamenti aviation insurance >€5M o due diligence istituzionale, richiede external Designated Verifier Body audit)
3. **Operational Authorization** (rilasciata da ENAC ex art. 12 Reg. 947, post-istruttoria)

**Confidence aggregato del documento**: **medium**, basato su (i) dati ISTAT/IGM Pentema confermati, (ii) SORA 2.5 europea fresca (8 mesi dalla pubblicazione, dottrina ENAC in formazione), (iii) caratteristiche piattaforma JOUAV CW-30E baseline (decisione vendor finale M+6, cfr. Trade Study A.3.04). I valori GRC/ARC/SAIL qui calcolati **devono essere riconfermati** durante il pre-application meeting ENAC.

**Falsifying observation associata** (cfr. **FO-10A-03** in Cap. 10 §10.5): se al M+9 ENAC determina SAIL effettivo ≥ IV (vs. target III), l'ipotesi C2 di gate è falsificata e si attiva contingency VLOS-only Y1 + re-application Y2 per BVLOS (cfr. Cap. 9 §9.12 sliding timeline).

---

## A.11.0 INDICE STRUTTURATO

- **§A.11.1** : Sintesi esecutiva e quick-look findings
- **§A.11.2** : STEP 1: ConOps narrative completa (pre-flight / flight / post-flight) per UC-001 frane, UC-002 antincendio, UC-004 mapping
- **§A.11.3** : STEP 2: UAS Class determination (CW-30E come Class III ai sensi Reg. (UE) 2019/945)
- **§A.11.4** : STEP 3: Ground Risk Class, iGRC + GRC final con M1/M2/M3/ERP
- **§A.11.5** : STEP 4: Air Risk Class, iARC + ARC final con TMA Genova, R-71 Brugneto, R-32, parapendio
- **§A.11.6** : STEP 5: SAIL determination + alternativi
- **§A.11.7** : STEP 6: OSO matrix (24 OSO con assegnazione Robust/Medium/Low/Optional + evidence-status)
- **§A.11.8** : STEP 7: Adjacent Area Considerations (Torriglia, ferrovia Genova-Casella, Diga del Brugneto)
- **§A.11.9** : STEP 8: Containment Requirements + Safety Portfolio integrato
- **§A.11.10** : Pre-Application Package ENAC: lista documenti, tempistiche, Q&A anticipato top-10
- **§A.11.11** : Linkage Risk Register, RTM, Cap. 5, Cap. 9, Cap. 10
- **§A.11.12** : Confidence aggregata, gap residui, raccomandazioni
- **§A.11.13** : Riferimenti normativi e tecnici

---

## A.11.1 SINTESI ESECUTIVA E QUICK-LOOK FINDINGS

### A.11.1.1 Risultati di sintesi

| Item | Valore preliminare | Confidence | Sensitivity |
|---|---|---|---|
| **UAS Class (Reg. 2019/945 Annex)** | **Class III** (1–25 kg MTOM, fixed-wing/VTOL non Class C0-C6) | high | bassa |
| **iGRC** (intrinsic Ground Risk Class) | **5** (BVLOS sparse populated, dimensione ~3 m) | medium | M (potrebbe scendere a 4 se Pentema classificata "rural isolated" stretto, o salire a 6 se "moderate") |
| **GRC final** (post M1+M2+M3 ERP) | **3** | medium | M |
| **iARC** (initial Air Risk Class) | **Class B** (rural mountainous, VLL, low GA traffic, occasional parapendio + glider) | medium | L-M (TMA Genova lateralmente, sorvolo R-71 Brugneto da evitare) |
| **ARC final** (post strategic mitigation) | **B** (confermato, TMPR Standard) | medium | L |
| **SAIL determination** | **SAIL III** (preliminary), possibile SAIL II in scenari ristretti | medium | H, driver primario del rischio regolatorio (RSK-REG-002) |
| **OSO applicabili SAIL III** | **18 OSO** (Robust su tecnici critici; Medium su procedure; Low su environmental) | medium | M |
| **Containment threshold** | < 1×10⁻⁴ per flight hour (perdita controllo) per SAIL III | high | L |
| **Tempistica ENAC nominale** | Pre-app M+3 → SORA submission M+9 → Authorization M+9÷15 | medium | M (sliding scenario M+15÷24, cfr. Cap. 9 §9.12) |

### A.11.1.2 Top-5 messaggi chiave per pre-application meeting ENAC

1. **Pentema è "sparsely populated" non "isolated"**: 14 abitanti residenti ISTAT, ma frazione attraversata da SS45 (strada provinciale, ~50–150 veicoli/giorno) e ferrovia Genova-Casella a ~3.5 km. La classificazione tabellare GRC SORA 2.5 (Annex E) lo colloca in **fascia 5** (sparse populated env., UAS 1m < L ≤ 3m).
2. **Mitigazione M1 critica**: geofence aree residenziali (200 m hard-buffer da abitazioni di Pentema) e window operativo timed (no overflight 8:00–10:00 / 17:00–19:00 quando attività comunitaria > media). La regola è documentata in Operations Manual draft Cap. 4.
3. **Recovery system (parachute)**: M2 robust con BRS (Ballistic Recovery System) certificato CE PED e impact velocity validata < 7 m/s (cfr. JOUAV CW-30E spec). Test in volo Pentema previsto Phase B (post-authorization).
4. **ARC b confermato ma TMPR Standard necessario**: la presenza di R-71 Diga del Brugneto (sorvolo proibito) e la prossimità della TMA Genova (15 km W) richiedono **NOTAM coordinato ENAV** ogni missione e segmentazione cellulare verticale.
5. **Insurance gap**: copertura RC BVLOS minimo 750.000 DSP (Reg. (CE) 785/2004 + DM Trasporti 25/02/2022); richiede broker aviation specialist (Marsh/Aon/Willis), premio stimato €25–80k/anno SAIL III. Si rimanda al Risk Register RSK-REG-026.

### A.11.1.3 Gap residui pre-application (da chiudere M+3÷6)

- **OQ-SORA-01**: validazione "sparse populated" vs. "moderate" da parte di ENAC (driver primario SAIL)
- **OQ-SORA-02**: accettazione M2 parachute come tactical robust (vs. dual M2 richiesto in alcuni casi SAIL ≥ IV)
- **OQ-SORA-03**: conferma TMPR Standard sufficiente vs. enhanced (presenza R-71)
- **OQ-SORA-04**: Operations Manual cap. obbligatori (vendor o operator-built, preferenza ENAC)
- **OQ-SORA-05**: Maintenance program, equivalenza Part-66 / Part-145 o standalone Operator Maintenance Manual

---

## A.11.2 STEP 1 : ConOps NARRATIVE COMPLETA

### A.11.2.1 Area operativa e identificazione geografica

**Sito primario**: frazione di **Pentema**, Comune di **Torriglia** (Città Metropolitana di Genova, Regione Liguria).

| Parametro | Valore | Fonte |
|---|---|---|
| Coordinate centro frazione | 44°30′28″N, 9°10′55″E (~44.5077°N, 9.1820°E) | IGM Carta d'Italia 1:25.000 (foglio 215 IV) |
| Altitudine s.l.m. | 1140 m (centro abitato), range valle 950–1300 m | IGM 215 IV |
| Popolazione residente | **14 abitanti ISTAT 2021** | ISTAT Censimento Permanente 2021 |
| Densità popolazione frazionale | < 5 ab/km² in raggio 2 km | ISTAT + GIS RegioneLiguria |
| Densità Comune Torriglia | ~14 ab/km² (popolazione 1980, sup. 60 km²) | ISTAT 2024 |
| Distanza centro abitato Torriglia (~1500 ab) | 3.27 km in linea d'aria | IGM |
| Strada principale | **SS45 Trebbia** (provinciale, ex-strada statale) | OpenStreetMap + ANAS |
| Ferrovia | Genova-Casella (FS), passaggio Crocefieschi ~3.5 km E | RFI carta linee |
| Diga d'invaso | **Diga del Brugneto** (capacità 25 Mm³, ~6.5 km NE di Pentema) | Regione Liguria DGR 1147/2018 |
| Zone NATURA 2000 | ZSC IT1331402 "Parco Naturale dell'Antola" (limitrofo) | Min. Ambiente |
| Aerodromo più vicino | LIMG Genova-Sestri (~38 km SW) | ENAV AIP IT |

**Volume operativo BVLOS proposto**:
- **Latitudine**: 44.46–44.55°N
- **Longitudine**: 9.10–9.30°E
- **Altitudine**: superficie terreno fino a **500 m AGL** (limite imposto, NON FL150)
- **Estensione**: ~120 km² (Valli Trebbia, Brugneto, alta valle Scrivia)
- **Buffer di contingenza** (vol. residuo): +30% laterale (geofence outer)

### A.11.2.2 Profilo missioni operative : Use Cases

#### UC-001 Monitoraggio frane settimanale (mapping fotogrammetrico RGB + multispettrale)

**Frequenza**: settimanale (52 missioni/anno baseline, con riduzione invernale a quindicinale = ~40 missioni/anno effettive).

**Profilo volo tipico**:
- **Decollo VTOL** da Ground Station (GS) hangar Pentema (area pad 6×6 m recintata)
- **Salita verticale** a 30 m AGL, transizione fase fixed-wing
- **Cruise** a 200–350 m AGL, velocità 80–110 km/h
- **Raster pattern** su 4 punti critici frane attive (cfr. mappa PAI Liguria 2024):
  - Versante SE Pentema (geomorfologia attiva)
  - Versante N Pentema verso Torriglia
  - Area Brugneto (escludendo sorvolo R-71)
  - Versante Casanova di Rovegno
- **Durata missione**: 2–3 ore (autonomy CW-30E 6h, margine 100%)
- **Ritorno**: transizione VTOL + atterraggio verticale GS
- **Post-flight**: download dati, ispezione visiva, ricarica batterie

**Crew**: 1 Pilot-in-Command (PIC) + 1 Mission Observer + opzionale 1 Maintenance Tech (presente per pre/post-flight).

**Ground footprint**: hangar 30 m², area pad 36 m², area control room 12 m².

#### UC-002 Antincendio boschivo (IR thermal + alert real-time)

**Frequenza**: stagionale, periodo **15 giugno ÷ 15 settembre**, attivazione on-demand su allerta Centro Funzionale ARPAL Liguria e Vigili del Fuoco.

**Profilo volo tipico**:
- Activation < 30 min dalla call (mission-ready posture)
- Salita rapida, cruise 400–500 m AGL
- Pattern di sorveglianza orbital su area di interesse (raggio 5–15 km dalla GS)
- IR sensor (uncooled microbolometer 640×512, NETD <50 mK) per detection hotspot
- Live downlink dati a Sala Operativa VVF / ARPAL via LTE bonded 4G + SATCOM backup
- Durata missione: fino a 5h continui (autonomia residuale margin)
- Possibili ri-decolli in caso evento prolungato

**Crew**: 1 PIC + 1 Mission Observer (in contatto radio VVF) + Mission Commander backstage.

**Special considerations**: le operazioni notturne sono ammesse in Phase B (post-authorization extra) ma **NON in Phase A** (BVLOS notturno richiede SAIL IV+).

#### UC-003 Connettività emergenza (LTE backup on-demand)

**Frequenza**: on-demand emergency activation (target SLA < 60 min), con esercitazioni 2/anno congiunte con Protezione Civile.

**Profilo volo tipico**:
- Decollo on-demand, salita stabilizzata a 300–500 m AGL
- Loitering pattern circolare attorno area servita (raggio 2–3 km)
- Payload: small cell LTE (band 7 / 28) o repeater PMR
- Durata: fino a 5h con switch crew (cambio batteria/UAS)
- Stop-and-go con UAS secondario in caso esigenza > 5h

**Crew**: 2 PIC alternati + 1 Mission Commander + 1 NetOps connection mgmt.

#### UC-004 Mapping infrastrutture (RGB + LiDAR), Phase Y2+

**Frequenza**: trimestrale Y2 (4 missioni/anno).

**Profilo**: simile a UC-001 ma con LiDAR payload (Riegl miniVUX-3UAV o equivalente, 9 kg). Raster su corridoi infrastrutturali (rete acquedotto IRETI, SS45, sentieri Antola).

### A.11.2.3 Pre-flight procedures

| Step | Attività | Responsabile | Documentazione |
|---|---|---|---|
| 24h prima | Weather check briefing (METAR/TAF LIMG, ECMWF, modello atm. ARPAL) | Mission Commander | Briefing form #BF-01 |
| 24h prima | NOTAM ENAV submission (se non già emesso ricorrente) | PIC | NOTAM template ENAC |
| 24h prima | Notice to Communities (Comune Torriglia + frazione Pentema) | Ops Coord. | Email + bacheca Comune |
| 6h prima | Crew briefing: ConOps, EPR, weather final, contingencies | PIC | Briefing log |
| 1h prima | Pre-flight inspection: airframe, payload, GS, datalink, battery state, parachute | Maintenance Tech + PIC | Pre-flight checklist #PF-01 |
| 30min prima | NOTAM verify activation + ATC check (se applicabile) + COMS test | PIC | Comms log |
| T-0 | Authorization-to-launch da Mission Commander | Mission Cdr | Launch authorization log |

### A.11.2.4 Flight procedures (in-flight)

Durante la missione l'equipaggio mantiene monitoraggio continuo del datalink C2 (RF 2.4 GHz, LTE backup, SATCOM Iridium per long range). La Ground Station opera su layout a due schermi: (i) mappa traffico, geofence, weather; (ii) FCS più payload feed. Il position reporting avviene via ADS-B OUT; l'ADS-B IN non è obbligatorio per ARC b ma viene installato come strategic mitigation. La crew rotation segue cicli di 90 min massimi di flight time, per la gestione fatica.

**Stop conditions**:
- Wind > 12 m/s (limite CW-30E)
- Visibility < 1.5 km (degradation cameras IR)
- Datalink lost > 30s (auto-RTB)
- Battery state critical (< 15%)

### A.11.2.5 Post-flight procedures

| Step | Attività | Output |
|---|---|---|
| Touchdown +5 min | Power-off sequence + secure UAS | Logbook entry |
| +10 min | Battery removal + storage (ATEX-compliant) | Battery log |
| +15 min | Visual inspection airframe (cracks, debris, props) | Post-flight checklist #PF-02 |
| +30 min | Data download + integrity check | DataOps log |
| +1h | Maintenance entry logbook (anomalies) | Logbook |
| +24h | NOTAM cancellation if recurring not active | NOTAM log |
| +7gg | Operations report (mensile aggregate) → ENAC art. 29 reporting | ENAC report |

---

## A.11.3 STEP 2 : UAS CLASS DETERMINATION

### A.11.3.1 Riferimento normativo

Il **Reg. (UE) 2019/945, Annex (Part 1 – Part 16)** definisce le classi di UAS commercializzabili:
- **C0**: < 250 g, MAX 19 m/s, ceiling 120m AGL (Open Subcat A1)
- **C1**: < 900 g, MAX 19 m/s impact (Open A1)
- **C2**: < 4 kg, slow mode (Open A2)
- **C3**: < 25 kg, max dimension 3 m (Open A3 over uninvolved persons)
- **C4**: < 25 kg, no autonomous (model aircraft, Open A3)
- **C5**: STS-01 (VLOS over controlled ground area)
- **C6**: STS-02 (BVLOS sparse populated areas with airspace observers)

### A.11.3.2 Posizionamento JOUAV CW-30E baseline

| Parametro | CW-30E spec | Class C3? | Class C6 (STS-02)? | Class Generica III SORA |
|---|---|---|---|---|
| MTOM | 18 kg (config payload 7 kg) | ✓ (< 25 kg) | ✓ | ✓ |
| Max dim. | 3.7 m (apertura alare ~3.5 m) | ✗ (> 3 m) | Non specifico | ✓ |
| VTOL fixed-wing hybrid | sì | C3 ammette | ✓ (compatibile) | ✓ |
| Marcatura CE C3/C6 | da verificare con JOUAV (probabilmente NO C-class certificate europea, prodotto cinese) | ✗ likely | ✗ likely | n/a (Specific cat. non richiede C-class) |

**Posizionamento ufficiale**: poiché la **Specific Category** non richiede né classificazione C0-C6 né certificazione CE secondo Reg. 2019/945 (cfr. art. 5 par. 3 Reg. 2019/947), l'inquadramento procede via **caratterizzazione SORA 2.5 Annex E**:

- **UAS Class (SORA cinematica)**: la **maximum characteristic dimension ≤ 3 m** è soglia critica per iGRC. Il CW-30E ha apertura alare 3.5 m, quindi rientra nella **fascia "3 m < L ≤ 8 m"** (worst case) **OPPURE**, se ENAC considera "characteristic dimension" come fusoliera (≈ 1.6 m), nella **fascia "1 m < L ≤ 3 m"**.
- **Cinetic energy at impact** (post-parachute): (0.5 × 18 × 7²) = 441 J < 34 kJ (soglia Annex F SORA 2.5 per Class III).
- **Cinetic energy at impact** (non-recovery): (0.5 × 18 × 30²) = 8100 J (con velocity ~30 m/s spiral dive), comunque < 34 kJ.

**Open Question OQ-SORA-06**: confermare con ENAC quale "characteristic dimension" applicare (fusoliera vs. apertura alare). Impatto: fascia GRC.

**Provisional classification per il Safety Case**: **UAS Class III (1 kg < MTOM ≤ 25 kg) con dimensione caratteristica 1–3 m** (assumendo fusoliera come reference, con allegato fotografico CAD a giustificazione).

### A.11.3.3 Lethality assessment

| Scenario impatto | Energia | Lethality (Annex F SORA 2.5) | Note |
|---|---|---|---|
| Impact post-parachute (7 m/s) | 441 J | Bassa (< 1 kJ) | M2 robust validation |
| Impact spiral dive 30 m/s | 8100 J | Media (1–34 kJ) | Mitigato da geofence + ERP |
| Impact post-flutter (vertical 60 m/s) | 32400 J | Alta (~34 kJ soglia) | Probabilità < 10⁻⁵/h (verifica FMECA) |

**Confidence Step 2**: **high** per classificazione MTOM, **medium** per characteristic dimension (open question dimensione fusoliera vs. apertura).

---

## A.11.4 STEP 3 : GROUND RISK CLASS (iGRC + FINAL)

### A.11.4.1 iGRC determination

**Riferimento**: EASA SORA 2.5 Amendment 3, **Annex E** (Ground Risk Class assignment matrix).

**Parametri input**:
- UAS characteristic dimension: **1 m < L ≤ 3 m** (provisional, vd. §A.11.3)
- Operational scenario: **BVLOS**
- Population density underflown: **sparsely populated**
- Speed regime: medium (80–110 km/h)

**Matrice iGRC SORA 2.5 (Annex E semplificata, valori rappresentativi)**:

| Operational scenario / UAS dim | Controlled area (e.g. test site) | Sparsely populated | Populated | Assemblies of people |
|---|---|---|---|---|
| 1 m < L ≤ 3 m, VLOS | 1 | 2 | 4 | 6 |
| 1 m < L ≤ 3 m, **BVLOS** | 2 | **5** | 6 | 8 |
| 3 m < L ≤ 8 m, BVLOS | 3 | 6 | 7 | 8 |

Si ottiene quindi **iGRC = 5** (BVLOS sparse populated, dim 1-3 m). Il worst case (ENAC opta per "3 m < L ≤ 8 m") condurrebbe a iGRC 6.

### A.11.4.2 Population density underflown : Pentema operational area

**Statistical analysis** del volume operativo (~120 km²):

| Area sub-zone | Sup. (km²) | Pop. residente | Densità (ab/km²) | Classificazione SORA |
|---|---|---|---|---|
| Frazione Pentema (centro) | 0.5 | 14 | 28 | sparse-popular borderline |
| Buffer Pentema 200m | 0.13 | 14 → 0 (geofence) | 0 | controlled (after M1) |
| Versante Brugneto | 25 | ~5 (case sparse) | 0.2 | isolated |
| Frazione Casanova | 1.0 | ~30 | 30 | sparse populated |
| Comune Torriglia centro | 0.5 | ~1500 | 3000 | **populated** (no overflight!) |
| Valle Trebbia (corridoio SS45) | 40 | ~150 | 4 | sparse |
| Bosco Antola (ZSC) | 50 | 0 | 0 | controlled (no humans) |
| Linea ferroviaria Genova-Casella | corridor 0.5 | ~3 utenti contemporanei avg | 6 | sparse but mobile pop. |

**Conclusione**: la dominanza statistica della **rotta tipica missione UC-001/UC-002** ricade nella categoria **sparse populated** (~75% del flight path), con segmenti minori **isolated** (sopra ZSC Antola, ~20%) e segmenti **non-overflight** (Torriglia, R-71 Brugneto, 5%).

**iGRC consolidato**: **5** (worst case), confidence medium.

**Open Question OQ-SORA-07**: accettazione di iGRC mediato su rotta vs. worst-case segment. Le linee guida JARUS suggeriscono il worst-case; ENAC ha accettato approccio segmentato in casi pregressi (es. Volocopter Roma 2024).

### A.11.4.3 Mitigations M1 + M2 + M3

#### M1 : Strategic Mitigations (Application Level)

**Definizione SORA 2.5**: riduzione del numero atteso di persone sotto la rotta tramite restrizioni operative (geofence, timing, area selection, weather criteria).

| Mitigation M1 sub-elementi | Applicazione | Riduzione GRC | Evidence |
|---|---|---|---|
| **M1.1 Geofence aree popolate**, 200 m hard buffer + 500 m soft buffer da Pentema, Torriglia, Casanova | ✓ Robust | Fattore × 0.3 popolazione sotto-rotta | Geofence config file (Operations Manual cap. 5) |
| **M1.2 Geofence aree no-fly**, R-71 Brugneto, R-32 Aviano area, ZSC Antola (Natura 2000 sorvolo limitato) | ✓ Robust | n/a (compliance) | Geofence config |
| **M1.3 Timed operation windows**, exclusion 08:00–10:00 + 17:00–19:00 (pop. activity peak) | ✓ Medium | Fattore × 0.7 | SOPs |
| **M1.4 Weather minima**, VIS > 1.5 km, wind < 12 m/s, no precipitazioni intense | ✓ Robust | n/a (operational) | OM cap. 4 |
| **M1.5 Vertical separation**, altitudine min 200 m AGL above sparse populated | ✓ Medium | Fattore × 0.8 | Flight envelope SOP |
| **M1.6 Pre-flight site survey + NOTAM coordination** | ✓ Robust | Reduce uncertainty | Mission planning protocol |

**Impatto cumulato M1**: in regime SORA 2.5, M1 riduce iGRC di **1 step** se applicato Robust ([cfr. AMC1 Article 11 § "M1 Application Level Reduction"]).

#### M2 : Tactical Mitigations (Containment + Termination)

**Definizione SORA 2.5**: riduzione del livello di harm in caso di failure (recovery system, flight termination, redundancy).

| Mitigation M2 sub-elementi | Applicazione | Riduzione GRC | Evidence |
|---|---|---|---|
| **M2.1 Parachute Recovery System (BRS)**, JOUAV CW-30E factory option, deployment manuale + automatico, impact velocity validata < 7 m/s | ✓ Robust | -1 step | Vendor data sheet + test report (richiedere a JOUAV) |
| **M2.2 Auto-RTB on Lost Link**, return to Home dopo 30s lost C2, plus pre-designated emergency landing zones (3 EZL identificate in volume operativo) | ✓ Robust | rinforza M2.1 | OM cap. 6 |
| **M2.3 Flight Termination System (FTS)**, independent kill switch, motor cut + parachute deploy, redundant transmitter (LTE + UHF) | ✓ Medium | n/a (M2.1 covers) | Hardware spec |
| **M2.4 Fail-operational FCS**, redundant IMU + GPS + altitude sensor; engineless glide capability for fixed-wing phase | ✓ Medium | resilience | FCS architecture doc |
| **M2.5 Battery thermal management**, BMS + thermal cutoff, no LiPo fire risk in flight | ✓ Robust | n/a (safety) | Battery cert |

**Impatto cumulato M2**: M2 Robust riduce GRC di **1 step** (parachute + RTB combinati).

#### M3 : Emergency Response Plan (ERP)

**Definizione SORA 2.5**: piano di risposta all'incidente per limitare conseguenze post-evento.

| ERP elementi | Applicazione | Note |
|---|---|---|
| **M3.1 ERP scritto** completo con: chain of command, comms numbers (112, ENAC ANSV, Sindaco Torriglia, VVF, CC Forestali) | ✓ Robust | Doc ERP-001 v1.0 |
| **M3.2 Insurance** RC + casco + cyber con copertura ≥ 750.000 DSP (Reg. (CE) 785/2004) | ✓ Robust | Polizza broker aviation |
| **M3.3 Crew training** ERP simulation drill semestrale | ✓ Medium | Training records |
| **M3.4 Communication channel** con comunità Pentema (canale Whatsapp + bacheca + email Comune) | ✓ Medium | Workshop OQ-009 M+3 |
| **M3.5 First responder coordination**, accordi pre-scritti con VVF Liguria + CC Forestali + 118 | ✓ Medium | MoU (M+3) |

**Impatto cumulato M3**: M3 Robust riduce GRC di **0.5 step** (in SORA 2.5 europea, ERP application è classificata "low" o "medium"; il livello robust è raro). In ottica conservativa, si applica arrotondamento a **0**.

### A.11.4.4 GRC Final calculation

| Componente | Valore | Rationale |
|---|---|---|
| iGRC | 5 | BVLOS sparse populated, dim 1-3m |
| - M1 (Robust) | -1 | Geofence + timing + minima |
| - M2 (Robust) | -1 | Parachute + RTB + FTS |
| - M3 (Medium-Robust) | 0 | ERP scritto (no full reduction in SORA 2.5) |
| **Final GRC** | **3** | (5 - 1 - 1 = 3) |

**Confidence Step 3**: **medium**. La riduzione M1+M2 di 2 step combinati è dottrinalmente accettabile (cfr. AMC1 SORA 2.5 §3.4.3), ma ENAC potrebbe richiedere evidenza più estesa per M1 (es. mapping density temporale) o non riconoscere M2 robust senza test in volo del BRS.

**Sensitivity**: se ENAC accetta solo "M1 Medium + M2 Medium", il GRC sale a 4 (vs. 3). Se ENAC contestasse iGRC partenza (es. iGRC = 6 perché dimensione 3m < L ≤ 8m), il final GRC nel best case sarebbe 4.

**Showstopper check**: GRC final ≤ 5 resta compatibile con SAIL ≤ IV. Solo GRC ≥ 6 farebbe scattare SAIL V+ con costi proibitivi.

---

## A.11.5 STEP 4 : AIR RISK CLASS (iARC + ARC FINAL)

### A.11.5.1 Spazio aereo dell'area operativa

**Volume di interesse**: lat 44.46–44.55°N, lon 9.10–9.30°E, SFC fino a 500 m AGL (~1640 m AMSL al picco terreno).

**Classificazione AIP IT (ENAV)**:

| Quota | Spazio aereo | Servizi ATS |
|---|---|---|
| SFC → 1000 ft AGL (≈ 600 m AMSL su valle, 1900 m AMSL su crinali) | **Classe G** non controllato | FIS (Flight Information Service) Genova ACC |
| 1000 ft AGL → FL195 | Classe G + tratti Classe E (overflight UAV/IFR) | FIS + radar Genova |
| FL195 → FL245 | Classe C controllato | Genova ACC clearance required |
| FL245+ | Classe A | UIR Milano |

**Area di rilievo limitrofa**:
- **TMA Genova** (Class D/E) lateralmente, ~15 km W (estensione SW del CTR Genova-Sestri)
- **R-71 Brugneto**, area regolamentata sorvolo proibito (motivi: diga + invaso), sup. ~25 km², SFC → FL45
- **R-32 Aviano-Bardonecchia**, area militare addestramento, attiva H24 NOTAM-dependent (~80 km E, ma traffico militare jet può transitare)
- **Sentieri parapendio**: aree decollo Pian del Lago, Monte Antola, operazioni VFR weekend
- **Aviazione generale**: corridoio VFR Genova → Piacenza (lateralmente al volume operativo)
- **Elisoccorso 118**: base elicotteri Genova San Martino (lat. distance ~40 km)
- **Antincendio Canadair**: stagionalmente, base AIB Genova → operazioni a 100–500 ft AGL

### A.11.5.2 iARC determination

**Matrice SORA 2.5 Annex C (iARC):**

| Spazio aereo | Densità traffico VFR/IFR | iARC |
|---|---|---|
| Class A controllato sopra FL195 (en-route) | high | d |
| Class D/E TMA sotto FL150 | medium-high | c |
| Class G rural VLL con GA occasionale | medium-low | **b** |
| Class G remote isolated | low | a |

Il volume operativo Pentema presenta dominanza Class G con **GA occasionale** (4–6 movimenti VFR/giorno medi nei mesi caldi, da statistica ENAV Genova FIS log 2024), **parapendio weekend** (5–10 lanci/giorno fine settimana stagione mite) ed **elisoccorso 118** (eventi sporadici, max 1–2/settimana area Trebbia).

**iARC determination preliminare**: **Class B** (b), rural mountainous VLL non-controlled, low-medium traffic.

**Open Question OQ-SORA-08**: la presenza di parapendio nei weekend solleva la densità traffico transitoriamente. Va verificato con ENAV se è richiesta TMPR Enhanced (vs. Standard) per missioni weekend, oppure se M1 timing (no weekend o no daylight 11:00–16:00) risulta sufficiente.

### A.11.5.3 Strategic mitigation ARC

| Mitigation Air | Applicazione | Riduzione ARC |
|---|---|---|
| **NOTAM coordination** ENAV ogni missione (NOTAM pre-emessa H-24 o ricorrente settimanale) | ✓ Robust | n/a (compliance baseline) |
| **ATC liaison**, call to Genova FIS pre-launch (frequency 124.025) | ✓ Medium | rinforza separation |
| **ADS-B IN/OUT** installato, detect surrounding traffic in 20 NM | ✓ Robust | -0.5 step (qualitative) |
| **Operational restrictions**, no weekend operations Apr-Oct (parapendio peak) salvo coordinamento federazione parapendio Liguria | ✓ Medium | -0 (qualitative) |
| **Visual observers airborne**, opzionale, non sistematic | ✗ Non applicato | - |
| **Conflict resolution procedures**, escape maneuver predefiniti (climb 100m + 90° heading) | ✓ Medium | resilience |

**ARC Final**: **B (b)**, confermato. Non è prevista alcuna upgrade verso a (low traffic) per via della presenza di R-71, parapendio ed eliambulanza.

### A.11.5.4 TMPR (Tactical Mitigation Performance Requirement)

Per ARC b, SORA 2.5 richiede **TMPR Standard** (vs. Low per ARC a, Enhanced per ARC c, High per ARC d).

**TMPR Standard requirements**:
- DAA (Detect-And-Avoid) cooperative: ADS-B IN ✓
- DAA non-cooperative: NON obbligatorio per Class B (suggested ma opzionale)
- Conflict alerting system: ground-based via ADS-B + LTE → ✓
- Time-to-alarm: < 30s
- Maneuver capability: pull-up 100m + turn 90° in 15s, da verificare CW-30E performance

**Open Question OQ-SORA-09**: ENAC sta valutando inclusione progressive di DAA non-cooperative (radar/EO) per SAIL III BVLOS. Resta da chiarire se si tratta di requisito formale o GM aspirational.

### A.11.5.5 ARC final per Step 5 SAIL determination

**Confidence Step 4**: **medium**. L'incertezza primaria riguarda i weekend parapendio. La mitigazione operativa (no weekend) è accettabile sul piano regolatorio, ma riduce drasticamente le missioni UC-002 antincendio (peak fire season summer weekend).

---

## A.11.6 STEP 5 : SAIL DETERMINATION

### A.11.6.1 Matrice SAIL (SORA 2.5 Annex C)

| GRC final \ ARC final | a (low) | **b (medium-low)** | c (medium-high) | d (high) |
|---|---|---|---|---|
| 1 | SAIL I | SAIL I | SAIL II | SAIL IV |
| 2 | SAIL I | SAIL II | SAIL III | SAIL V |
| **3** | SAIL II | **SAIL III** | SAIL IV | SAIL V |
| 4 | SAIL III | SAIL III | SAIL IV | SAIL V |
| 5 | SAIL IV | SAIL IV | SAIL V | SAIL VI |
| 6 | SAIL V | SAIL V | SAIL VI | SAIL VI |
| 7 | SAIL VI | SAIL VI | SAIL VI | SAIL VI |

### A.11.6.2 Determinazione SAIL Pentema

**Input**: GRC final = 3 + ARC final = b conduce a **SAIL III**.

**Confidence: medium**. Sensitivity:

| Scenario | GRC | ARC | SAIL |
|---|---|---|---|
| **Baseline** (M1+M2 robust accettati) | 3 | b | **III** |
| Ottimistico (M3 ERP robust accettato + iGRC inizio 4 con dim caratteristica fusoliera) | 2 | b | II |
| Pessimistico (M1 medium + iGRC 6 dim caratt. apertura alare) | 5 | b | IV |
| Worst (TMPR enhanced richiesto + iGRC 6) | 5 | c | V |
| Catastrophic (FO-10A-03 trigger: SAIL V/VI) | 6 | c | VI |

### A.11.6.3 SAIL III implications

**OSO applicabili**: ~18 OSO (vs. ~12 per SAIL II, ~22 per SAIL IV). Si veda §A.11.7.

**Robust/Medium/Low distribution typical SAIL III**:
- Robust: ~5 OSO (tecnici critici: design, software, DAA, C2)
- Medium: ~10 OSO (procedure, training, environment)
- Low/Optional: ~3 OSO

**Cost implication**: vendor compliance evidence acquisition + audit preparation = €30–80k (engineering/legal fees), in linea con stima Cap. 5 §5.4.1.

**Timeline implication**: SAIL III ENAC LRA processo standard 3–6 mesi instructory + 1–3 mesi authorization = **4–9 mesi total** (consistente con M+9÷15 nominale, sliding M+15÷24).

---

## A.11.7 STEP 6 : OPERATIONAL SAFETY OBJECTIVES (OSO) MATRIX

### A.11.7.1 Lista OSO SORA 2.5 (24 totali)

La SORA 2.5 europea (Amendment 3) ha **riarticolato** la lista OSO mantenendo numerazione 1–24 ma con criteri di compliance leggermente modificati rispetto SORA 2.0. Di seguito la **matrice completa SAIL III** per Pentema 6A:

| # | OSO Title | SAIL III Level | Status compliance | Evidence ref. | Confidence | Note |
|---|---|---|---|---|---|---|
| **OSO #01** | Ensure operator is competent and/or proven | **Medium** | 🟡 In progress | Operator certification track + experience log | medium | Firmamento UAS Operator in registrazione ENAC |
| **OSO #02** | UAS manufactured by competent and/or proven entity | **Medium** | 🟢 Achievable | JOUAV vendor profile + ISO 9001 cert | medium | Vendor due-diligence required Phase A |
| **OSO #03** | UAS maintained by competent and/or proven entity | **Medium** | 🟡 In progress | Maintenance org (in-house o partner Part-145 equivalent) | medium | Decisione in-house vs. outsource M+6 |
| **OSO #04** | UAS developed to authority recognised design standards | **Low** (SAIL III) | 🟡 In progress | Vendor design standard declaration (STANAG 4671, DO-178C lite) | low-medium | OK no Type Cert; vendor must show practiced eng standards |
| **OSO #05** | UAS is designed considering system safety and reliability | **Medium** | 🟡 In progress | FMECA + FTA (Cap. 6.4) + vendor docs | medium | Internal FMECA da finalizzare M+6 |
| **OSO #06** | C3 link characteristics adequate for safe ops | **Low** (SAIL III) | 🟢 Achievable | Link budget A.7 + redundancy LTE+SATCOM | high | Link budget detailed cfr. Allegato A.7 |
| **OSO #07** | Inspection of the UAS (pre-flight) | **Medium** | 🟢 Achievable | Pre-flight checklist + log book | high | OM cap. 4 in draft |
| **OSO #08** | Operational procedures are defined, validated and adhered to | **Medium** | 🟡 In progress | Operations Manual completo + validation test | medium | OM Phase A draft, validation Phase B |
| **OSO #09** | Remote crew trained and current and able to control abnormal | **Medium** | 🟡 In progress | Training syllabus + competency records + recurrency | medium | Training plan Phase A |
| **OSO #10** | Safe recovery from technical issue | **Medium** | 🟢 Achievable | Parachute + auto-RTB + EZL | high | M2 robust |
| **OSO #11** | Procedures in-place to handle deterioration of external systems supporting ops | **Medium** | 🟡 In progress | Lost link / weather degradation SOPs | medium | OM cap. 6 |
| **OSO #12** | UAS is designed to manage decrease of perf | **Low** (SAIL III) | 🟢 Achievable | Glide capability + redundancy | medium | Vendor spec |
| **OSO #13** | External services supporting UAS operation are adequate to the operation | **Low** (SAIL III) | 🟢 Achievable | LTE provider SLA + SATCOM Iridium SLA + meteo | medium | Vendor SLAs in negotiation |
| **OSO #14** | Operational procedures are defined, validated and adhered to (= OSO #08 doppione storico) | **Medium** | (vd. #08) | (vd. #08) | medium | - |
| **OSO #15** | Crew/personnel involved in the operation are not under stress, fatigue | **Low** | 🟢 Achievable | Crew rotation policy + fatigue management | high | OM cap. 7 |
| **OSO #16** | Multi-crew coordination | **Medium** | 🟢 Achievable | PIC + Observer + Mission Cdr | high | CRM training |
| **OSO #17** | Crew is trained for emergency response | **Medium** | 🟡 In progress | ERP training + drill semestrale | medium | Drill M+6+ |
| **OSO #18** | Automatic protection of flight envelope from human errors | **Medium** | 🟢 Achievable | FCS envelope protection (vendor std) | high | CW-30E vendor spec |
| **OSO #19** | Safe recovery from human error | **Medium** | 🟢 Achievable | Auto-RTB + parachute | high | M2 |
| **OSO #20** | Safety risk assessment of UAS by mass + area | **Medium** | 🟢 Achievable | Questa SORA application | high | This document |
| **OSO #21** | External services adequate (= duplicate of #13 historical) | **Low** | (vd. #13) | (vd. #13) | medium | - |
| **OSO #22** | UAS designed and qualified for adverse env conditions | **Low** | 🟡 In progress | Vendor environment qualification | low-medium | OK only -10/+40°C; deep winter requires limitation |
| **OSO #23** | Environmental conditions for safe ops defined, measurable, adhered | **Medium** | 🟢 Achievable | Weather minima OM cap. 4 | high | Wind/VIS/precip criteria |
| **OSO #24** | UAS qualified for adverse env (= duplicate #22) | **Low** | (vd. #22) | (vd. #22) | low-medium | - |

**Note**: OSO #14, #21, #24 sono storici "doppi" della SORA 2.0 e mantenuti in SORA 2.5 con stessi criteri di #08, #13, #22 rispettivamente (riallineamento europeo).

### A.11.7.2 OSO summary per livello

| Livello | OSO # | Count |
|---|---|---|
| **Robust** | (nessuno mandatorio SAIL III, ma 4 OSO trattati comunque Robust per resilience) | 0+4 |
| **Medium** | #01, #02, #03, #05, #07, #08, #09, #10, #11, #14, #16, #17, #18, #19, #20, #23 | **16** |
| **Low** | #04, #06, #12, #13, #15, #21, #22, #24 | **8** |

**Total compliance-relevant OSO**: 16 Medium + 8 Low = **24 OSO addressed** (consistente con SORA 2.5 total set; alcune coppie ridondanti sono trattate insieme).

### A.11.7.3 Gap analysis OSO

**OSO con maggior gap M+3 baseline**:

| OSO | Gap | Closure target | Owner |
|---|---|---|---|
| #03 Maintenance entity | Decisione in-house vs. partner Part-145 | M+6 | aviation-regulatory + maintenance-engineer |
| #04 Design standards vendor | Document acquisition JOUAV (STANAG 4671?) | M+6 | aviation-regulatory + vendor (RFI) |
| #08 Operations Manual | Draft completo + validation tests | M+9 | aviation-regulatory + operations |
| #09 Training program | Syllabus + competency matrix + first recurrency | M+9 | training-officer (new hire) |
| #17 ERP drill | Prima simulation drill semestrale | M+6 | mission-commander |
| #22 Adverse env qualification | Cold weather mountain (snow/ice), outside vendor spec? | M+9 | vendor + ops |

### A.11.7.4 Confidence aggregato OSO

- **Robust-ready** (high confidence di compliance): #06, #10, #18, #19, #20 = 5 OSO
- **Medium-ready** (medium confidence): #07, #15, #16, #23 + most operational = 6 OSO
- **In progress** (low-medium confidence): #03, #04, #08, #09, #17, #22 = 6 OSO
- **Risk OSO** (richiede vendor cooperation forte): #02, #04, #22 (vendor data acquisition)

**Confidence aggregato Step 6**: **medium**.

---

## A.11.8 STEP 7 : ADJACENT AREA CONSIDERATIONS

### A.11.8.1 Definizione SORA 2.5

L'**Adjacent Area** è il volume di spazio aereo adiacente all'**Operational Volume** dove potrebbero finire frammenti, persone, beni in caso di **loss of containment**. SORA 2.5 (Annex H) richiede analisi separata della popolazione adjacent e dei requisiti containment associati.

### A.11.8.2 Adjacent Area mappa Pentema

**Operational Volume**: 120 km² (vd. §A.11.2.1).

**Adjacent Volume** (buffer +30% laterale + +50% verticale):
- Sup.: ~200 km²
- Estensione lat: 44.43–44.58°N, lon 9.05–9.35°E
- Altitude buffer: +100m oltre 500m AGL operativo

**Aree popolate o sensibili nell'Adjacent**:

| Area | Distanza dal centro op. vol. | Pop./asset | Severity se loss of containment |
|---|---|---|---|
| **Torriglia centro** | 3.5 km E | 1500 ab | Alta (populated), non sorvolare anche in contingenza |
| **Crocefieschi** | 5 km N | ~600 ab | Media-alta |
| **Frazione Casanova** | 6 km W | ~30 ab | Media |
| **Casanova di Rovegno** | 5 km SE | ~50 ab | Media |
| **Linea ferroviaria Genova-Casella** | 3.5 km E (passa Crocefieschi) | ~3 utenti/treno × 20 corse/giorno | Media (popolazione mobile) |
| **SS45 Strada Trebbia** | 0 km (attraversa op. vol.) | ~50–150 veicoli/giorno | Media |
| **Diga del Brugneto** | 6.5 km NE | Asset critico Stato + invaso acqua potabile | Alta (geofence R-71 hard) |
| **ZSC IT1331402 Antola** | adiacente | Asset ambientale (no umani) | Bassa (no human) |
| **Aerodromo LIMG Genova** | 38 km SW | airport > 4M pax/anno | Trascurabile per distanza |

### A.11.8.3 Containment requirement per Adjacent

**Performance threshold SORA 2.5 (SAIL III + Adjacent populated)**:
- Probability of containment failure: **< 1 × 10⁻⁴ per flight hour**
- Definition of containment: UAS resta entro Operational Volume + Contingency Volume in 99.99% dei casi

**Means of compliance Pentema**:
- **Geofence hard** (FTS auto-trigger) sui confini Operational Volume
- **Auto-RTB + Auto-Land** in case lost link > 30s o GPS lost > 60s
- **Parachute deployment** in caso oltrepassamento geofence + perdita comando manuale
- **Independence demonstration**: FCS principale + FTS secondario con kill switch indipendente (separate IMU + transmitter)
- **Test in volo**: Phase B (post-authorization), drop test parachute + lost link simulation + geofence trigger test

### A.11.8.4 Population density Adjacent : sensitivity

| Adjacent area sub-zone | Pop. (residente + transito) | Densità eq. | Classificazione SORA |
|---|---|---|---|
| Buffer Torriglia 1 km | ~1700 | 540 ab/km² | populated |
| Buffer ferrovia + SS45 corridor | ~200 | 30 ab/km² | sparse-borderline |
| Resto Adjacent (bosco + valli) | ~200 | 2 ab/km² | sparse-isolated |

**Conclusione**: la popolazione nell'Adjacent **include Torriglia** che è populated. Questo eleva il requisito containment di un livello (vs. solo sparse adjacent).

**Open Question OQ-SORA-10**: chiarire con ENAC se il containment requirement per Adjacent populated impone testing più stretto (drop test multipli, validation 100h pre-operational), oppure se documentazione vendor e analisi è sufficiente per SAIL III.

### A.11.8.5 Confidence Step 7

**Confidence**: **medium-low**. L'Adjacent è una delle aree dove SORA 2.5 europea ha innovato rispetto alla 2.0 e dove la dottrina ENAC è ancora in formazione. Resta uno stretching scenario.

---

## A.11.9 STEP 8 : CONTAINMENT REQUIREMENTS + SAFETY PORTFOLIO

### A.11.9.1 Containment definition

**Operational Volume Pentema**: vol. dichiarato in §A.11.2.1.
**Contingency Volume**: +30% laterale + +50% verticale (buffer di "recovery" se UAS esce da Operational ma resta in Contingency, no containment failure ma anomaly).
**Adjacent Volume**: oltre Contingency, è la zona dove non deve mai arrivare (containment failure = entry in adjacent).

### A.11.9.2 Containment performance

| Metric | Target SAIL III | Means of compliance | Confidence |
|---|---|---|---|
| Probability of loss of containment | < 1×10⁻⁴ /h | Geofence hard + FTS + parachute | medium |
| Probability of severe injury 3rd party | < 1×10⁻⁶ /h | Kinetic energy < 34 kJ post-parachute | medium |
| Probability of fatal accident 3rd party | < 1×10⁻⁷ /h | Combined M1 + M2 | medium-low |

**Verification approach**: analytical (FMECA + FTA Cap. 6.4 dello Studio) + vendor reliability data (MTBF, MTBCF JOUAV) + test in-flight (Phase B).

### A.11.9.3 Safety Portfolio integration

Il **Safety Portfolio** integra tutti gli elementi dello Step 1–8 in una rappresentazione strutturata. Pentema 6A:

```
                        ┌─────────────────────────────┐
                        │  SORA 2.5 SAFETY PORTFOLIO  │
                        │       Pentema 6A v2.0       │
                        └─────────────┬───────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        ▼                             ▼                             ▼
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│ GROUND RISK     │         │ AIR RISK        │         │ DESIGN/OSO      │
│ iGRC 5 → GRC 3  │         │ iARC b → ARC b  │         │ SAIL III        │
│ M1 + M2 robust  │         │ TMPR Standard   │         │ 16 Med + 8 Low  │
│ M3 ERP medium   │         │ ADS-B + NOTAM   │         │ Vendor evidence │
└────────┬────────┘         └────────┬────────┘         └────────┬────────┘
         │                           │                           │
         └───────────────────────────┼───────────────────────────┘
                                     ▼
                        ┌─────────────────────────────┐
                        │  CONTAINMENT < 1×10⁻⁴ /h    │
                        │  Geofence + FTS + Parachute  │
                        │  Adjacent Torriglia analyzed │
                        └─────────────────────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────────┐
                        │  RESIDUAL RISK ACCEPTABLE   │
                        │  (subject to ENAC review)   │
                        └─────────────────────────────┘
```

### A.11.9.4 Evidence portfolio (cross-reference)

| Evidence type | Source | Allegato/Cap. ref. |
|---|---|---|
| ConOps detailed | Cap. 4 §4.4 ICD + Cap. 6 §6.1 | Vol. 1 |
| FMECA + FTA | Cap. 6 §6.4 | Vol. 1 + Allegato A.5 V&V |
| Link budget C2 | Allegato A.7 | Vol. 2 |
| Mass budgets | Allegato A.8 | Vol. 2 |
| RTM (requirement traceability) | Allegato A.1 | Vol. 2 |
| Risk Register (regolatorio) | Allegato A.2 RSK-REG-002, 019, 026, 027 | Vol. 2 |
| Trade Study vendor selection | Allegato A.3.04 (JOUAV vs Tekever) | Vol. 2 |
| Vendor profile JOUAV | RFI/RFQ Allegato Vendor RFQ | Vol. 2 |
| Pre-application ENAC roadmap | Cap. 5 §5.4.1 + Cap. 9 §9.5 | Vol. 1 |
| Sliding timeline regolatorio | Cap. 9 §9.12 | Vol. 1 |
| Falsifying observations gate | Cap. 10 §10.5 (FO-10A-03) | Vol. 1 |

---

## A.11.10 PRE-APPLICATION PACKAGE ENAC

### A.11.10.1 Lista documenti richiesti per il Pre-Application Meeting

Secondo prassi consolidata ENAC Direzione Regolamentazione UAS (Capo div. UAS, riferimento contatto via PEC `protocollo@pec.enac.gov.it` o portale UAS dedicato), per un pre-application meeting su SAIL III BVLOS si richiedono i seguenti documenti **anticipati H-15gg**:

| # | Documento | Stato M+3 | Owner |
|---|---|---|---|
| **D-01** | **Lettera di intent** (operatore + ConOps di sintesi 2 pagine) | 🟢 Pronto (template Allegato OQ-009) | aviation-regulatory |
| **D-02** | **ConOps preliminare esteso** (10-20 pagine) | 🟡 Da finalizzare | aviation-regulatory + ops |
| **D-03** | **SORA Safety Case preliminary** (questo documento) | 🟢 Pronto v2.0 (preliminary-grade) | aviation-regulatory |
| **D-04** | **UAS technical data sheet** (CW-30E vendor spec + custom config) | 🟡 In acquisizione (vendor RFI) | engineering + vendor |
| **D-05** | **Operations Manual draft index** (almeno indice cap. 1-15) | 🟡 Draft index ready | aviation-regulatory + ops |
| **D-06** | **Operator profile** Firmamento Technologies (registrazione UAS in corso) | 🟡 In registrazione | legal + aviation-regulatory |
| **D-07** | **Crew CV + licenses** (PIC BVLOS attestato ENAC + observers) | 🔴 PIC hire da completare M+6 | HR + training |
| **D-08** | **Insurance certificate** (RC BVLOS attiva o pre-quotation broker) | 🟡 Pre-quotation in corso | financial-cfo + ops |
| **D-09** | **Site survey report Pentema** (foto, mapping, IGM, ISTAT) | 🟢 Pronto | ops + GIS |
| **D-10** | **Coordination letters** (Comune Torriglia, ENAV, VVF Liguria) | 🟡 In emissione | aviation-regulatory + outreach |
| **D-11** | **Pre-application meeting agenda + Q&A list** | 🟢 Pronto (cfr. §A.11.10.3) | aviation-regulatory |

### A.11.10.2 Tempistiche tipiche ENAC LRA per SAIL III

Da analisi LRA ENAC pubblicate (Linee Guida 2022-2025) e da esperienze su casi pubblici BVLOS Italia:

| Fase | Durata nominale | Sliding worst-case |
|---|---|---|
| **Pre-application meeting** | 1 meeting + feedback verbale | 1-2 meeting (rare due-incontri se feedback iniziale richiede integrazioni) |
| **Pre-application response time** | 4–6 settimane dal meeting | 8–12 settimane |
| **SORA application submission to ENAC formal acknowledgement** | 2–4 settimane | 6 settimane |
| **First instruttoria + questions to operator** | 6–12 settimane | 16–20 settimane |
| **Operator response + integrations (round 1)** | 4–8 settimane operator-driven | 12 settimane |
| **Second instruttoria** | 4–8 settimane | 12 settimane |
| **Final authorization issuance** | 2–6 settimane | 8 settimane |
| **TOTAL nominal** | **~3-6 mesi** | **~8–12 mesi** |

**Pentema 6A target**: pre-app M+3 → SORA submission M+9 → authorization M+9÷15 nominal, M+15÷24 sliding.

**Risk Register linkage**: cfr. **RSK-REG-002** (SORA SAIL Pentema > III). Sliding timeline cfr. Cap. 9 §9.12.

### A.11.10.3 Q&A anticipato : Top 10 domande ENAC attese

Sulla base di prassi consolidata (cfr. ENAC report autorizzazioni 2023-2024 e workshop EASA-ENAC 2025), si anticipano le **domande probabili** del referente ENAC durante il Pre-Application Meeting, con la relativa risposta preparata.

**Q1. "Perché classificate Pentema sparse populated e non moderate?"**
> **R**: ISTAT 2021 censisce 14 abitanti residenti in frazione Pentema; densità < 30 ab/km² nel buffer 1 km centro abitato. La SORA 2.5 Annex E indica sparse populated per densità tipica < 250 ab/km² in ambiente rurale-isolato. Pentema soddisfa il criterio: il pattern operativo evita Torriglia centro (populated, geofence hard). Source: ISTAT Censimento 2021 + GIS IGM (Allegato A.13 documentazione fotografica). **Confidence: medium-high**.

**Q2. "Quali evidenze di reliability avete del parachute (M2)?"**
> **R**: JOUAV CW-30E factory option Ballistic Recovery System (BRS) con vendor datasheet e test report (in acquisizione). Pre-quotation comprende drop test certificate impact velocity < 7 m/s. **Mitigazione gap**: validation test in volo previsto Phase B post-authorization (drop test 5-10 deployment in area controllata). **Confidence: medium**.

**Q3. "Qual è l'esperienza pregressa dell'operatore Firmamento Technologies?"**
> **R**: Firmamento Technologies S.r.l. costituita 2024 specificamente per piattaforme aerospaziali. UAS Operator registration ENAC in corso (M+1÷3). Pilot-in-Command sarà persona certificata BVLOS con esperienza pregressa (target hire M+3÷6 con 5+ anni BVLOS commerciale, attestato ENAC valido). **Mitigazione**: in alternativa, **outsourcing PIC** verso operatore certified-BVLOS già autorizzato per servizio (partnership cooperativa). **Confidence: medium**.

**Q4. "Come gestite le operazioni vicino TMA Genova e R-71 Brugneto?"**
> **R**: TMA Genova lateralmente a 15 km W, nessuna interferenza prevista (alt. operativa max 500m AGL ≈ 1640m AMSL, sotto FL150). R-71 Brugneto inserita in geofence hard (no overflight). NOTAM coordination ENAV per ogni missione (frequency 124.025 Genova FIS) + call pre-launch. **Confidence: high**.

**Q5. "Operations Manual è basato su modello vendor o operator-built?"**
> **R**: **Operator-built** (Firmamento custom OM) con cap. 1-15 secondo struttura JAR-OPS/Part-OPS adattata UAS. Vendor docs (JOUAV CW-30E) integrati come Annex tecnici. **Rationale**: l'operatore deve essere autonomo nelle procedure operative; vendor docs supportano ma non sostituiscono. **Confidence: high**.

**Q6. "Maintenance organization: in-house o Part-145 partnership?"**
> **R**: **Decisione M+6** subordinata a trade study A.3.07 (Maintenance Strategy). Baseline preferito: **hybrid**, preventive maintenance in-house (parte 1° livello) e corrective + heavy maintenance presso partner certificato (es. Logos Group Italia o Skytellier). Operator Maintenance Manual unico, con vendor docs integrati. **Confidence: medium**.

**Q7. "Come gestite gli incidenti? ANSV reporting?"**
> **R**: ERP scritto (ERP-001 v1.0) con flow di reporting: (i) immediate 112 + Comune Torriglia + ENAC ANSV +39 06 8207 8200; (ii) entro 24h ANSV form occurrence; (iii) entro 72h ENAC report incidente; (iv) entro 30gg insurance claim. Reporting eventi monthly aggregato ENAC art. 29 Regolamento APR Ed.3. **Confidence: high**.

**Q8. "Sistema cyber security : Reg. (UE) 2023/203 Part-IS?"**
> **R**: ⚠️ **Gap riconosciuto**. Part-IS (Information Security regulation) è **applicabile da febbraio 2026** per operatori Specific Category con SAIL ≥ III. Firmamento sta finalizzando ISMS basato su ISO/IEC 27001 + cap. Part-IS dedicato. Il **CISO** è in fase di hiring (M+6). Risk Register **RSK-REG-019** open. Audit Part-IS preventivo previsto M+9 con consulente accreditato. **Confidence: low-medium**, gap aperto.

**Q9. "Privacy + GDPR : payload EO sopra abitato?"**
> **R**: Le missioni UC-001 frane / UC-004 mapping evitano centri abitati (geofence). Eventuali riprese accidentali (es. SS45 traffic) sono mascherate (blur algorithm post-processing) o cancellate. DPIA (Data Protection Impact Assessment) prevista entro M+6. Garante Privacy notifica trattamento se >5000 soggetti coinvolti (improbabile). **Confidence: medium-high**.

**Q10. "Quale piano di evoluzione futura BVLOS notturno o operazioni multi-UAS?"**
> **R**: Phase A 6A pilota 2026-2027 = BVLOS daytime singolo UAS, SAIL III. Phase B 2028+ = potenziale BVLOS notturno (richiede SAIL IV upgrade + osservatore notturno + IR enhanced) e multi-UAS coordinated (richiede U-Space CIS + RIS Liguria, dipendente da ENAC Regolamento U-Space Ed.1 in consultazione). **Confidence: medium**, dipendente da maturazione U-Space.

### A.11.10.4 Pre-application meeting agenda proposta

| Item | Durata | Owner |
|---|---|---|
| Introduzione Firmamento + missione Pentema | 10 min | aviation-regulatory + CEO |
| ConOps tour (vis. mapping + use cases) | 20 min | ops + GIS |
| SORA preliminary findings (GRC/ARC/SAIL) | 20 min | aviation-regulatory |
| OSO matrix walkthrough + gap | 15 min | aviation-regulatory |
| Q&A ENAC + feedback iniziale | 30 min | aviation-regulatory + Q&A team |
| Next steps + tempistiche | 10 min | Coord. ENAC + Firmamento |
| **TOTAL** | **~1h45** | (incluso buffer) |

---

## A.11.11 LINKAGE CROSS-DOCUMENT

### A.11.11.1 Risk Register cross-reference

| Risk ID | Descrizione | Connessione con questo Safety Case | Mitigation linkage |
|---|---|---|---|
| **RSK-REG-002** | SORA SAIL Pentema > III | Core risk, questo documento è la mitigazione documentale | M+3 pre-app + M+6 SORA prep + M+9 submission |
| **RSK-REG-019** | Part-IS EASA Reg. (UE) 2023/203 ISMS obbligatorio feb 2026, CISO assente | OSO #06 C2 link + cyber section gap | CISO hire M+6 + ISMS gap analysis M+6+ |
| **RSK-REG-026** | Insurance BVLOS premio > €100k/anno o broker rifiuta | OSO #20 (this SORA quality) + ERP M3 | Tender broker aviation specialist M+3+ |
| **RSK-REG-027** | NIS2 D.Lgs. 138/2024, registrazione ACN omessa | OSO #11 external services + cyber | ACN registration M+0+ urgent |

### A.11.11.2 Falsifying Observations linkage

| FO ID | Trigger | Connessione |
|---|---|---|
| **FO-10A-03** | C2 SORA ENAC SAIL II-III BVLOS operativa entro M+9, falsificata se ENAC al M+9 non rilascia o classifica SAIL ≥ IV | Sliding timeline §A.11.10.2 + Q&A Q1, Q2 preparation |

### A.11.11.3 Cap. 5 quadro normativo cross-reference

| Sez. Cap. 5 | Cross-reference |
|---|---|
| §5.1.5 Metodologia SORA 2.5 | Step 1-8 di questo Safety Case |
| §5.2 Specific Category | §A.11.6.3 implications SAIL III |
| §5.3 ENAC Regolamento APR Ed.3 | art. 11 (autorizzazione) + art. 26 (BVLOS) + art. 29 (reporting) |
| §5.4.1 Percorso 6A timeline | §A.11.10.2 ENAC tempistiche |
| §5.13 Red Team regulatory | Confidence aggregato + gap residui di questo doc |

### A.11.11.4 RTM linkage

Requisiti di sistema (Allegato A.1 RTM) collegati a SORA:
- **SyR-Reg-001**: SORA SAIL III determination, linked to §A.11.6
- **SyR-Reg-002**: ENAC authorization BVLOS Specific, linked to §A.11.10
- **SyR-C-010**: Insurance BVLOS 750.000 DSP, linked to M3 §A.11.4.3 + §A.11.10.1 D-08
- **SyR-Cost-009**: Insurance OpEx Y1 ≤ €50k/anno, linked to RSK-REG-026
- **SyR-OSO-001 ÷ 024**: OSO compliance, linked to §A.11.7

---

## A.11.12 CONFIDENCE AGGREGATA + GAP RESIDUI

### A.11.12.1 Confidence dichiarato per step

| Step SORA | Confidence | Rationale |
|---|---|---|
| Step 1 ConOps | **medium-high** | Sito Pentema dati confermati; missioni use case definiti; gap su Operations Manual finale |
| Step 2 UAS Class | **medium-high** | MTOM definito, vendor RFI in corso |
| Step 3 GRC | **medium** | iGRC validation con ENAC pre-app required (Q1) + mitigation evidence M1/M2 da rinforzare |
| Step 4 ARC | **medium** | Open question parapendio/weekend + TMPR Standard validation |
| Step 5 SAIL | **medium** | Sensitivity ampia (II-IV plausibile); driver pre-app outcome |
| Step 6 OSO | **medium** | 6 OSO con gap; vendor evidence acquisition in corso |
| Step 7 Adjacent | **medium-low** | Dottrina ENAC in formazione; testing post-authorization |
| Step 8 Containment | **medium** | Analytical evidence + vendor data; in-flight test Phase B |
| **AGGREGATO** | **medium** | Adeguato per pre-application; insufficient per SORA application formale |

### A.11.12.2 Gap residui pre-application

| Gap | Closure target | Severity |
|---|---|---|
| OQ-SORA-01 Sparse vs moderate Pentema classification | Pre-app meeting M+3 | High |
| OQ-SORA-02 M2 parachute robust evidence | M+6 vendor docs + test plan | Medium |
| OQ-SORA-03 TMPR Standard vs Enhanced | Pre-app meeting M+3 | Medium |
| OQ-SORA-04 OM structure preference ENAC | M+3 verbal + M+6 draft | Low-medium |
| OQ-SORA-05 Maintenance program approach | M+6 trade study A.3.07 | Medium |
| OQ-SORA-06 Characteristic dimension definition | M+3 verbal | High |
| OQ-SORA-07 Worst-case vs average GRC | M+3 verbal | Medium |
| OQ-SORA-08 Parapendio weekend operational impact | M+3 + coordinamento Fed. Parapendio | Low-medium |
| OQ-SORA-09 DAA non-cooperative SAIL III SC | M+3 verbal + EASA NPA tracking | Low |
| OQ-SORA-10 Adjacent populated containment test | M+9+ | Medium |
| Vendor evidence acquisition JOUAV (STANAG 4671, reliability data) | M+6 RFI completion | High |
| PIC hire (PIC BVLOS Italian licensed) | M+6 | Medium |
| Operations Manual draft completo | M+9 | Medium |
| Part-IS / ISMS / CISO | M+6+ | High (cross with RSK-REG-019) |

### A.11.12.3 Raccomandazioni finali

1. **Procedere immediatamente** con Pre-Application Meeting ENAC entro M+3, presentando questo Safety Case e il ConOps preliminare. La confidence è sufficiente per l'istruttoria iniziale; i gap si chiudono successivamente.

2. **Anticipare RFI vendor JOUAV** (Reliability data, parachute test reports, STANAG 4671 declaration, FCS envelope protection details) entro M+3, per supportare OSO #02, #04 e #18 con evidence robust.

3. **CISO hire urgente** (M+6 max) per chiudere RSK-REG-019 e RSK-REG-027, e per supportare la cyber dimension di OSO #06/#11. Senza CISO, la SORA application Q8 resta vulnerabile.

4. **PIC hire entro M+6** con esperienza BVLOS Italian commerciale (5+ anni preferred). Come contingency, partnership con operatore certificato esistente.

5. **Tender broker aviation specialist** (Marsh, Aon, Willis) per insurance BVLOS quotation entro M+3. Il pre-application richiede pre-quotation documentale (D-08).

6. **Sliding timeline alert**: se al M+6 il pre-application non ha avuto luogo, occorre attivare contingency planning (VLOS-only Y1 + re-application Y2). Cfr. Cap. 9 §9.12 e Cap. 10 §10.5 FO-10A-03.

7. **Aggiornamento Safety Case v3.0** post pre-application ENAC (entro M+5) con feedback verbale recepito e revisione SAIL determination.

---

## A.11.13 RIFERIMENTI NORMATIVI E TECNICI

### A.11.13.1 Riferimenti normativi primari

- **[N-01]** Reg. (UE) 2018/1139 del 4 luglio 2018, Basic Aviation Regulation
- **[N-02]** Reg. (UE) 2019/947 del 24 maggio 2019, Rules and procedures for the operation of UAS
- **[N-03]** Reg. (UE) 2019/945 del 12 marzo 2019, UAS and on third-country operators
- **[N-04]** **EASA ED Decision 2025/018/R del 15 settembre 2025**, Amendment 3 a Issue 1 AMC/GM Reg. 2019/947 (versione europea SORA 2.5)
- **[N-05]** EASA AMC1 to Article 11 Reg. 2019/947 (SORA 2.5)
- **[N-06]** EASA GM1 to Article 11 Reg. 2019/947 (SORA 2.5 Guidance Material, cybersecurity)
- **[N-07]** ENAC Regolamento "Mezzi Aerei a Pilotaggio Remoto" Edizione 3 del 11 novembre 2019 + Emendamento 1 del 14 luglio 2020 (art. 11, 26, 29)
- **[N-08]** Reg. (CE) 785/2004 + DM Trasporti 25/02/2022, Assicurazione operatori aerei (BVLOS minimo 750.000 DSP)
- **[N-09]** Reg. (UE) 2023/203 del 27 ottobre 2022, Part-IS (Information Security, applicabile 22 feb 2026 SAIL ≥ III)
- **[N-10]** D.Lgs. 138/2024, Recepimento NIS2 (registrazione ACN)
- **[N-11]** Reg. (UE) 2021/664, 665, 666, U-Space framework
- **[N-12]** ENAC LG-2023/006, Linee Guida U-Space Ed.1 del 19 dicembre 2023
- **[N-13]** Codice Aeronautico (R.D. 327/1942 + ss.mm.ii.), disciplina spazio aereo italiano
- **[N-14]** Reg. (UE) 2016/679 GDPR + D.Lgs. 196/2003 + ss.mm.ii.

### A.11.13.2 Riferimenti tecnici

- **[T-01]** JARUS SORA 2.5 official document (ottobre 2024)
- **[T-02]** EASA Easy Access Rules for UAS (2025 edition)
- **[T-03]** STANAG 4671, UAV system airworthiness requirements (NATO, ed. 4)
- **[T-04]** RTCA DO-178C / EUROCAE ED-12C, Software considerations
- **[T-05]** RTCA DO-254 / EUROCAE ED-80, Hardware considerations
- **[T-06]** ARP4754A, Civil aircraft system development
- **[T-07]** ARP4761A, Safety assessment process (ed. 2023)
- **[T-08]** DO-326A / ED-202A, Airworthiness Security
- **[T-09]** AS/EN 9100:2018, Quality Management Aerospace
- **[T-10]** ISO/IEC 27001:2022, ISMS
- **[T-11]** JOUAV CW-30E Vendor Data Sheet (in acquisizione M+3÷6)
- **[T-12]** ENAV AIP Italia, Aeronautical Information Publication (current edition)
- **[T-13]** ITU Radio Regulations (Edition 2024)

### A.11.13.3 Riferimenti interni progetto HALE

- **[I-01]** Studio di Fattibilità, Cap. 4 §4.4 ICD, ConOps detailed
- **[I-02]** Studio di Fattibilità, Cap. 5 §5.1-5.4, Quadro normativo
- **[I-03]** Studio di Fattibilità, Cap. 6 §6.4, FMECA + FTA
- **[I-04]** Studio di Fattibilità, Cap. 9 §9.5 + §9.12, Cronoprogramma + sliding timeline
- **[I-05]** Studio di Fattibilità, Cap. 10 §10.5, Falsifying Observations gate (FO-10A-03)
- **[I-06]** Allegato A.1 RTM, Requirements Traceability Matrix
- **[I-07]** Allegato A.2 Risk Register, RSK-REG-002, 019, 026, 027
- **[I-08]** Allegato A.3.04 Trade Study Vendor Selection, JOUAV vs. Tekever
- **[I-09]** Allegato A.5 V&V Plan
- **[I-10]** Allegato A.7 Link Budget (C2 + payload)
- **[I-11]** Allegato A.8 Bilanci di Massa
- **[I-12]** Allegato A.13 Documentazione Fotografica Pentema

---

## ANNEX A : Sintesi tabellare SAIL III OSO Pentema (compact view)

| OSO# | Title (short) | Level | Status |
|---|---|---|---|
| 01 | Operator competent | Med | 🟡 |
| 02 | Manufacturer competent | Med | 🟢 |
| 03 | Maintenance competent | Med | 🟡 |
| 04 | Design standards | Low | 🟡 |
| 05 | System safety + reliability | Med | 🟡 |
| 06 | C3 link | Low | 🟢 |
| 07 | UAS inspection | Med | 🟢 |
| 08 | Operational procedures | Med | 🟡 |
| 09 | Crew training + currency | Med | 🟡 |
| 10 | Safe recovery technical | Med | 🟢 |
| 11 | External systems deterioration | Med | 🟡 |
| 12 | Performance management | Low | 🟢 |
| 13 | External services adequate | Low | 🟢 |
| 14 | (dup #08) | Med | (vd. 08) |
| 15 | Crew fitness | Low | 🟢 |
| 16 | Multi-crew CRM | Med | 🟢 |
| 17 | Emergency response training | Med | 🟡 |
| 18 | Flight envelope protection | Med | 🟢 |
| 19 | Safe recovery human error | Med | 🟢 |
| 20 | This SORA itself | Med | 🟢 |
| 21 | (dup #13) | Low | (vd. 13) |
| 22 | Adverse env qualification | Low | 🟡 |
| 23 | Env conditions criteria | Med | 🟢 |
| 24 | (dup #22) | Low | (vd. 22) |

Legenda: 🟢 = ready / achievable; 🟡 = in progress with closure target M+3÷9; 🔴 = critical gap.

---

## ANNEX B : Glossario

- **AGL**: Above Ground Level
- **AMC**: Acceptable Means of Compliance (EASA)
- **AMSL**: Above Mean Sea Level
- **ANSV**: Agenzia Nazionale per la Sicurezza del Volo
- **ARC**: Air Risk Class
- **BVLOS**: Beyond Visual Line of Sight
- **C2/C3**: Command-and-Control link (between RPS and UAS)
- **CISO**: Chief Information Security Officer
- **ConOps**: Concept of Operations
- **DAA**: Detect-and-Avoid
- **DSP**: Diritti Speciali di Prelievo (SDR, Special Drawing Rights, IMF unit)
- **EASA**: European Union Aviation Safety Agency
- **ENAC**: Ente Nazionale per l'Aviazione Civile
- **ENAV**: Ente Nazionale Assistenza al Volo
- **ERP**: Emergency Response Plan
- **FCS**: Flight Control System
- **FIS**: Flight Information Service
- **FTS**: Flight Termination System
- **GM**: Guidance Material (EASA)
- **GRC**: Ground Risk Class
- **iGRC**: intrinsic Ground Risk Class
- **iARC**: initial Air Risk Class
- **JARUS**: Joint Authorities for Rulemaking on Unmanned Systems
- **MTOM**: Maximum Take-Off Mass
- **OSO**: Operational Safety Objective
- **PIC**: Pilot-in-Command
- **RPS**: Remote Pilot Station (= Ground Station)
- **SAIL**: Specific Assurance and Integrity Level
- **SORA**: Specific Operations Risk Assessment
- **TMPR**: Tactical Mitigation Performance Requirement
- **VLL**: Very Low Level airspace
- **VLOS**: Visual Line of Sight
- **ZSC**: Zona Speciale di Conservazione (Natura 2000)

---

> **End of document A.11 v2.0**, preparato da `aviation-regulatory-counsel` HALE Studio di Fattibilità Firmamento Technologies. Per istruttoria pre-application ENAC. NON sostituisce SORA application formale ex art. 11 Reg. (UE) 2019/947.
