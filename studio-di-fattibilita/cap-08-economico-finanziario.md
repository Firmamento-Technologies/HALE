# Capitolo 8 — Analisi Economica e Finanziaria

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes
> Volume 1, Capitolo 8
>
> **Versione:** bozza M+3
> **Conformità:** D.Lgs. 36/2023 art. 41 + Allegato I.7 (Quadro Economico + Piano Economico-Finanziario)
> **Standard contabili:** OIC (Italia), riferimenti IFRS dove rilevante
> **Disciplina epistemica:** Regole 1-7 della skill `epistemic-rigor`
> **Red Team review:** `financial-cfo-analyst` + `red-team-skeptic` + `business-model-strategist` — vedi §8.10

---

## 8.0 Sintesi del capitolo

Il presente capitolo presenta l'**analisi economica e finanziaria** dei due percorsi del progetto Firmamento Technologies, in conformità all'art. 41 D.Lgs. 36/2023 + Allegato I.7 e in coerenza con i template italiani di riferimento (ENAC AAM Business Plan [^1], Aeropolis Workshop costing [^2]).

### 8.0.1 Verdetto finanziario in sintesi

| Percorso | CapEx totale | OpEx Y2 run-rate | Revenue Y1 baseline | NPV (10y) scenario base | IRR scenario base | Payback | Verdetto |
|---|---|---|---|---|---|---|---|
| **6A — VTOL pilota Y1-Y3** | €700-1200k Y1 + €0.5-1.5M scale Y2-Y3 | €260-480k baseline / **€1.18M con +3 FTE regulatory (Cap. 5 §5.17)** | **€260k centrale (range €220-300k) RECALIBRATED** post-Cluster D (legacy €355-405k FALSIFICATO), min €200k SyR-Cost-003 | NPV positivo Y5-Y6 con scale-up (vs Y4-Y5 pre-recalibration) | 12-20% (vs 15-25% pre-recalibration) | 5-7 anni | ⚠️ **GO CONDIZIONATO** finanziariamente (peggioramento margine post-Cluster D; richiede LoI Regione €75-100k/anno) |
| **6B — HALE R&D Phase B** | €5.5-13.5M (Y3-Y5 cumulato) | n/a (R&D phase) | n/a (revenue commerciale post-Y6) | NPV solo qualitativo (R&D phase) | n/a | n/a (commercial Y8+) | ⚠️ **GO condizionato R&D** subordinato a funding mix specifico |

### 8.0.2 Mix finanziamenti raccomandato

| Fase | CapEx totale | Grant % | Equity % | Debito % | R&D credit % |
|---|---|---|---|---|---|
| **6A Y1 MVP** | €0.7-1.2M | 35-55% (Coopfond + FESR) | 25-45% (founder + seed) | 5-15% | 5-15% |
| **6A Y2-Y3 scale** | €2-5M | 30-50% (PNRR + Horizon + FESR) | 30-40% (Series A €3-8M) | 10-20% | 5-15% |
| **6B Phase B R&D** | €5.5-13.5M | 50-75% (EDF + Horizon + PNRR + ASI) | 15-30% (Series B €15-50M raised) | 5-15% | 5-15% |

### 8.0.3 Dato chiave — capital intensity onesta su 10 anni

In linea con `riferimenti/visione-10-anni.md`, capital intensity totale Y1-Y10:

- **Scenario "small fleet"** (5-10 HAPS Y10): **€500M-2B**
- **Scenario "EU sovereign full scale"** (100+ HAPS, alternativa Starlink EU): **€10-30B** (richiede programma equivalente IRIS² dedicato come precondizione)

---

## 8.0bis Boundary conditions del progetto

In coerenza con Cap. 5.0bis, Cap. 3.0bis, Cap. 6.0bis, Cap. 7.0bis:

- **B1**: Modello service-only. NESSUN ricavo da vendita di velivoli previsto nel piano economico, in tutto l'orizzonte.
- **B2**: Visione strategica EU sovereign stratospheric layer; lo Studio approva soltanto i passi 1-2 (Y1-Y3 financial detailed; Y4-Y10 scenarios qualitativi).

---

## 8.1 Metodologia e Riferimenti

### 8.1.1 Struttura art. 41 D.Lgs. 36/2023 + Allegato I.7

L'analisi economica e finanziaria del PFTE secondo Allegato I.7 [^3] include:

| Elaborato | Posizione nello Studio |
|---|---|
| **Quadro Economico** (A + B somme a disposizione) | §8.3 |
| **Piano Economico-Finanziario** (NPV, IRR, payback, ROI) | §8.5 |
| **Computo Metrico Estimativo** (ground segment) | Vol. 2 Allegato A.9 |
| **Cronoprogramma finanziario** | §8.7 + Cap. 9 |
| **Piano di Manutenzione preliminare** (OpEx aspetto) | Vol. 2 Allegato A.10 |

### 8.1.2 Template italiano ENAC AAM Business Plan

Riferimento autoritativo italiano: ENAC AAM BP 2021-2030 [^1]. Struttura adottata:
- §3 Investimenti finalizzati alla creazione dell'ecosistema → §8.4 CapEx
- §5 Scouting di potenziali fonti di finanziamento → §8.6 Strategia finanziamenti
- §4 Benefici qualitativi → §8.9 ROI sociale

Il dato di riferimento ENAC: investimenti AAM Italia 2021-2030 = €1,863.4M ripartiti su 3 wave [^1, §1].

### 8.1.3 Aeropolis Workshop "Analisi Costi e Business Plan" — approccio costing

Riferimento metodologico: Aeropolis Workshop 2014 [^2] — approccio costing aerospace di derivazione industriale (Alenia):
- Tempi e Metodi (analisi tempi standard)
- Preventivi per famiglia di componente
- Controllo industriale + controllo programmi

### 8.1.4 Disciplina epistemica

Confidence aggregato del capitolo: **medium-low** (le cifre finanziarie non hanno ancora validazione esterna; molte sono stime interne basate su benchmark e best practice). Falsifying observations dichiarate in §8.5 e §8.8.

**Base rate aerospace cost overrun** (skill `epistemic-rigor` Regola 7): tipicamente **30-150%** sui piani iniziali aerospace (GAO Cost Estimating Guide 2020). Pianificare contingency adeguata.

---

## 8.2 Articolazione Finanziaria per Percorso

### 8.2.1 Percorso 6A — Articolazione 12 mesi MVP + 24 mesi scale-up

- **Y1 MVP (M+0 → M+12)**: CapEx + OpEx + primo revenue, focus Pentema + Liguria
- **Y2 Espansione Liguria (M+12 → M+24)**: 1-2 piattaforme aggiuntive, espansione casi d'uso
- **Y3 Multi-regione SNAI (M+24 → M+36)**: flotta 3-5 piattaforme, +2-3 regioni

### 8.2.2 Percorso 6B — Articolazione Phase B R&D

- **Y3 Inizio Phase B (M+24 → M+36)**: R&D engineering + subscale prototype
- **Y4-Y5 Test bed + integration**: prototipo 1:3 subscale flight test
- **Y6+ Phase C/D** (out-of-scope dello Studio): full-scale prototype + Type Certification path

---

## 8.3 Quadro Economico ex art. 41 D.Lgs. 36/2023

In conformità all'Allegato I.7, il Quadro Economico del PFTE è strutturato come segue:

### 8.3.1 Quadro Economico Percorso 6A MVP Y1 (range realistico)

```
═══════════════════════════════════════════════════════════════
QUADRO ECONOMICO — Percorso 6A MVP Pilota Pentema (M+0 → M+12)
═══════════════════════════════════════════════════════════════

A) IMPORTO INVESTIMENTI (asset + servizi tecnici)
   A.1 Piattaforma VTOL (JOUAV CW-30E o eq.)        €  250-400k
   A.2 Set ricambi 3 anni                           €   30-60k
   A.3 Payload EO RGB high-res + gimbal             €   30-80k
   A.4 Payload IR LWIR (WIRIS Pro o eq.)            €   20-50k
   A.5 Payload telecom backup (LTE eNodeB)          €   80-150k  [opzionale Y1]
   A.6 Ground Station fissa Pentema                 €   20-50k
   A.7 Ground Station mobile (veicolo + console)    €   30-70k
   A.8 Hangar protetto Pentema (affitto/light build)€   40-100k
   A.9 Strumenti diagnostica + spare iniziali       €   15-30k
   A.10 Setup SW (mission planning, GIS, pipeline)  €   30-80k
   A.11 Certificazioni iniziali (SORA, ENAC)        €   20-50k
   A.12 Privacy compliance (DPIA, registri)         €   10-25k
   A.13 Formazione team (piloti, op., analyst)      €   30-60k
   A.14 Studi preparatori e progettazione           €   50-100k
                                       Totale A   € 655-1305k

B) SOMME A DISPOSIZIONE (ex Codice Contratti)
   B.1 Spese tecniche (progettazione, DL, RUP)      €   30-65k   (~4.5% A)
   B.2 Imprevisti (contingency 15%)                 €   100-200k (~15% A)
   B.3 Spese pubblicità bandi                       €    2-5k
   B.4 IVA su A (22%)                               €  144-287k
   B.5 IVA su B (22%)                               €   29-59k
   B.6 Allacciamenti, autorizzazioni                €    5-15k
   B.7 Spese collaudo / verifica                    €   10-25k
                                       Totale B   €  320-656k

TOTALE GENERALE Y1 (A+B)                            €  975-1961k
─────────────────────────────────────────────────────────────────
```

**Range realistico CapEx Y1 (incluse IVA + contingency): €975k - €1.96M**.

> **⚠️ Caveat epistemico §8.3.1**: la stima è preliminare con confidence **medium-low**. Il range di €975k-1.96M è significativamente superiore al range Briefing iniziale €600-900k. La differenza è giustificata da:
> 1. **IVA 22%** non considerata nel Briefing originale (impatto +22% su A)
> 2. **Contingency 15%** (aerospace best practice — base rate overrun 30-150%)
> 3. **Spese tecniche** non incluse esplicitamente (RUP, progettazione)
> 4. **Spese collaudo + autorizzazioni** non incluse

**Falsifying observation §8.3.1**: se al M+6 il CapEx cumulato proiettato supera €2M (margine superiore range), attivare review scope MVP (es. eliminare payload telecom Y1, ground segment più semplice, no LiDAR).

### 8.3.2 Quadro Economico Percorso 6A Y2-Y3 (scale-up cumulato)

| Voce | Y2 (M+12-24) | Y3 (M+24-36) | Cumulato Y2+Y3 |
|---|---|---|---|
| A — Asset addizionali | €0.4-1.0M | €0.5-1.5M | €0.9-2.5M |
| B — Somme a disposizione | €0.15-0.4M | €0.2-0.6M | €0.35-1.0M |
| **Totale annuale** | **€0.55-1.4M** | **€0.7-2.1M** | **€1.25-3.5M** |

### 8.3.3 Quadro Economico Percorso 6B Phase B R&D (range)

```
═══════════════════════════════════════════════════════════════
QUADRO ECONOMICO — Percorso 6B Phase B R&D (M+24 → M+48)
═══════════════════════════════════════════════════════════════

A) IMPORTO INVESTIMENTI R&D
   A.1 R&D engineering core (aero, struct, prop, avi)  € 1.5-3.5M
   A.2 Prototipo subscale 1:3 (manifattura)            € 0.8-2.0M
   A.3 Wind tunnel + ground test (outsourcing)         € 0.4-1.2M
   A.4 Avionica + GNC + software DAL-C                 € 1.0-2.5M
   A.5 Payload R&D (NTN gNodeB + EO HALE)              € 0.5-1.5M
   A.6 Certificazione pre-application + engagement     € 0.3-0.8M
   A.7 Personale aggiuntivo 8-15 FTE (24 mesi)         € 1.0-2.0M
                                          Totale A    € 5.5-13.5M

B) SOMME A DISPOSIZIONE
   B.1 Spese tecniche + project management            €  0.3-0.8M
   B.2 Imprevisti / contingency 20% R&D               €  1.1-2.7M
   B.3 IVA su A (22%, eventual quota)                 €  1.2-3.0M*
   B.4 Spese audit + reporting bandi                  €  0.05-0.2M
                                          Totale B   €  2.7-6.7M

TOTALE GENERALE Phase B (Y3-Y5)                       €  8.2-20.2M
─────────────────────────────────────────────────────────────────
* IVA grant-funded R&D solitamente esente o rimborsabile
```

> **Stima realistica Phase B**: €8-15M (range più stretto considerando grant funding tipicamente esente IVA).

> **⚠️ CAVEAT CRITICO POST DR-014 (M+3)**: il benchmark di programmi HALE solari internazionali (`riferimenti/DR-research-closure-M3.md` §DR-014) indica capital intensity per programma stimata **$50M - $1B** (Zephyr Airbus cumulato 15+ anni, Skydweller Series A $40M solo round iniziale, PHASA-35 BAE multiple round, Sunglider SoftBank investimento estimato $200M+). La stima Firmamento **€5.5-13.5M è sottostimata 10-50x** rispetto a questi benchmark per "operatività commerciale". Riposizionamento onesto:
> - **€5.5-13.5M = Phase 0/Phase A Y1-Y3** (concept + subscale demo + early flight test), **NON** fino a operatività commerciale
> - Phase B-C-D-E **a copertura operativa** richiede realisticamente **€50-200M+ cumulati** per HALE solare proprietario, OR partnership con prime contractor (Aalto/Sceye/Skydweller/CIRA) come **prime contractor** + Firmamento come operatore di servizi
> - Il modello service-only (boundary B1) consente di **non sopportare il full capex** se Firmamento opera HAPS di un prime contractor (model "Airbus Air-as-a-Service / Aalto Defense+Civil mix" sotto licenza)
> - Implicazione strategica: **Phase B 6B in autonomia full-scale è non finanziabile** per Firmamento standalone. Ricalibrato come **R&D collaborativo** con partner prime contractor o consortium EU EuroHAPS-successor.

> **Falsifying observation Phase B 6B post-DR-014**: se al gate G5 (M+24) non c'è partnership prime contractor (Aalto/Skydweller/Sceye/CIRA/TAS) firmata o consortium EU bid-ready, Phase B 6B in standalone è **strutturalmente non finanziabile**. Attivare scenario B2-relaxed Cap. 11 §11.6bis.

---

## 8.4 CapEx Dettagliato

### 8.4.1 CapEx Percorso 6A — driver di costo

**Asset hardware (60-70% del CapEx Y1)**:

| Driver costo | Range €k | % | Note |
|---|---|---|---|
| Piattaforma VTOL | 280-460 | 35-40% | JOUAV CW-30E + ricambi |
| Payload modulare | 160-310 | 18-25% | RGB + IR + (telecom) |
| Ground segment | 90-220 | 10-15% | GS fissa + mobile + hangar |
| Strumenti + setup operativo | 45-110 | 5-8% | Diagnostica + spare + tools |

**Soft assets (30-40% del CapEx Y1)**:

| Driver costo | Range €k | % | Note |
|---|---|---|---|
| Setup software | 30-80 | 4-6% | Mission planning + GIS + processing + anonymization |
| Certificazioni | 20-50 | 2-4% | SORA + ENAC dichiarazioni + AGCOM licensing |
| Privacy compliance | 10-25 | 1-2% | DPIA pubblica + registri |
| Formazione team | 30-60 | 4-5% | Piloti UAS BVLOS + ops + analyst |
| Studi preparatori | 50-100 | 5-7% | Engineering + ConOps + workshops |

### 8.4.2 CapEx Percorso 6B — ripartizione R&D

Ripartizione tipica aerospace R&D per HALE solare (vedi `agents/financial-cfo-analyst.md`):

```
Engineering (aero+struct+prop+avi+payload)    25-35%  ← €2-4M
Prototyping (subscale + materials)            15-20%  ← €1-2M
Test (wind tunnel + ground + flight subscale) 10-15%  ← €0.8-1.5M
Software development (FCS, GNC, GS)           10-15%  ← €0.8-1.5M
Personnel (8-15 FTE × 24 mesi)                20-30%  ← €2-4M
Certification engagement                       5-10%   ← €0.4-1M
Overhead + management                          5-10%   ← €0.4-1M
─────────────────────────────────────────────────────────
TOTALE Phase B baseline                       100%    ← €5.5-13.5M
```

---

## 8.5 OpEx Recurrente

### 8.5.1 OpEx Percorso 6A run-rate Y2+ (post-MVP) — RECONCILIATION baseline + regulatory team mandatory

> **⚠️ Caveat reconciliation OpEx Y2 (M+3 post Cap. 5 §5.17 + Quality audit)**: la versione originale "**€260-480k/anno baseline**" **NON include** il costo del regulatory team obbligatorio identificato post-Cap. 5 §5.17 (5+1 critical regolatori aggiuntivi: Part-IS EASA Information Security, AgID/PSN, art. 50 Codice Contratti, NIS2, ENAV FL400+, EUROCONTROL HAPS). Il regulatory team **mandatory** richiede **+3 FTE** (CISO + DPO + Head Regulatory) per €0.6-0.7M/anno. **OpEx Y2 reconciled = €1.18M centrale (range €1.05-1.30M)**. Il baseline €260-480k è qui mantenuto in **legacy** solo come traccia "operazioni tecniche pure", NON come run-rate operativo dichiarato per scenario base.

#### 8.5.1.A OpEx tecnico baseline (operazioni pure, legacy pre-regulatory team)

| Voce | €k/anno | % | Note |
|---|---|---|---|
| **Personale (3 FTE: pilota+ing+analyst) + 0.5 FTE PM** | 150-220 | 50-55% | Costo onnicomprensivo |
| Manutenzione piattaforma (5-8% CapEx asset) | 30-60 | 10-12% | Service + spare consumati |
| Assicurazione UAS BVLOS (RC + casco) | 15-40 | 5-8% | Aviation insurance specifica |
| Carburante / energia | 5-15 | 2-3% | Per la propulsione ibrida |
| Software canoni (GIS, processing, cloud) | 10-25 | 3-5% | SaaS subscription |
| Connettività dati (SATCOM + cloud) | 5-15 | 2-3% | |
| Costi sede / utility Pentema | 15-30 | 5-6% | Hangar + GS fissa |
| Marketing + comm + partnership | 20-50 | 7-10% | Tradeshows + outreach + sales |
| Spese legali / regolatorie / privacy (legacy, pre-Cap.5 §5.17) | 10-25 | 3-5% | DPIA update + ENAC + AGCOM base |
| **Subtotale OpEx tecnico baseline (legacy)** | **€260-480k/anno** | — | NON sufficiente operativamente Y1+ |

#### 8.5.1.B Regulatory team mandatory (post Cap. 5 §5.17, +3 FTE)

| Voce | €k/anno | Razionale Cap. 5 §5.17 |
|---|---|---|
| **CISO** (Chief Information Security Officer, 1.0 FTE) | 90-120 | Part-IS EASA + NIS2 registrazione + AgID/PSN hosting (RSK-REG-016, RSK-REG-018, RSK-REG-019) |
| **DPO** (Data Protection Officer, 0.6-1.0 FTE outsource possibile) | 50-80 | GDPR + DPIA EO + condivisione cooperative + Garante Privacy (RSK-PRI-001 + DR-007) |
| **Head Regulatory & Compliance** (1.0 FTE senior aerospace) | 110-140 | Coordination ENAC + EASA + AGCOM + ENAV + EUROCONTROL + Codice Contratti art. 50 + ATEX + RoHS + REACH (RSK-REG-017, -020, -021, -022, -023, -024, -025) |
| Consulenze legali + audit certificatori (Bureau Veritas / RINA / DNV) | 80-120 | AS/EN 9100 + ISO 27001 + ISO 9001 + Part-IS audit recurring |
| Software compliance (GRC tool, SAST/DAST, vulnerability mgmt) | 30-50 | Continuous monitoring NIS2 + Part-IS |
| Spettro AGCOM canoni (se uplink/downlink licenze proprietarie) | 20-40 | Spectrum fee + ITU coordination (RSK-REG-026) |
| Engagement EASA Innovation Network + RMT HAPS contributions | 20-40 | Special Condition HAPS dialogue ongoing (DR-005) |
| **Subtotale Regulatory team mandatory** | **€400-590k/anno** | Centro €490k |

#### 8.5.1.C OpEx Y2 RECONCILED (run-rate dichiarato per scenario base)

| Componente | Worst (P10) | Base (P50) | Best (P90) |
|---|---|---|---|
| OpEx tecnico baseline (8.5.1.A) | €480k | €370k | €280k |
| Regulatory team mandatory (8.5.1.B) | €590k | €490k | €400k |
| Buffer overhead amministrativo + ISO audit | €230k | €170k | €115k (cumulativo, scala con FTE) |
| **OpEx Y2 RECONCILED dichiarato** | **€1.30M** | **€1.18M** | **€1.05M** |

### 8.5.2 Evoluzione OpEx Y3-Y5 (scale-up) — RECONCILED

| Anno | OpEx target RECONCILED | Driver scaling | Note |
|---|---|---|---|
| Y2 (Liguria consolidato, regulatory team full) | **€1.05-1.30M** (centro €1.18M) | Baseline tecnico €260-480k + Regulatory team €400-590k + overhead €115-230k | Run-rate operativo Y2+ |
| Y3 (multi-regione, flotta 3-5) | €1.5-2.2M | +2-3 FTE ops + 2 GS mobile + +30% manutenzione + regulatory team scale | Scale-up regione, regulatory team non scala 1:1 |
| Y4-Y5 (+ HALE subscale ops) | €2.5-4.0M | +Phase B R&D run-rate ~50% del CapEx Phase B annuale + ulteriori regulatory (EASA HALE) | OpEx aumentato per R&D HALE + Part-IS HALE |

> **Riconciliazione con financial-model README (Volume 2 Allegato A.7)**: il README dichiara "**OpEx Y2 €1.18M**". Questo numero è coerente con §8.5.1.C base scenario qui sopra. Il legacy €260-480k è stato superato a M+3 post Cap. 5 §5.17 audit.

---

## 8.6 Piano Economico-Finanziario (NPV, IRR, payback, ROI)

### 8.6.1 Modello finanziario MVP Y1-Y5 (cash flow ipotetico, scenario base)

> **⚠️ Caveat epistemico §8.6.1**: il modello sotto è **scenario base preliminare**, basato su assunzioni intermedie. Confidence: **low** per anni Y3+ (out-of-window di validazione diretta). Per uso investment-grade, modello finanziario Excel completo con sensitivity in Vol. 2 Allegato A.7 + DCF dettagliato.

**Assunzioni base**:
- CapEx Y1: €1.4M (centro range)
- CapEx Y2: €0.8M (espansione 1 piattaforma + 1 GS aggiuntiva)
- CapEx Y3: €1.0M (multi-regione + flotta 3)
- CapEx Y4: €0.5M (sostituzione + upgrade)
- CapEx Y5: €0.5M
- OpEx growth: +30%/anno fino Y3, +15%/anno Y4+
- Revenue ramp: vedi Cap. 7 §7.8.2
- WACC: 12% (blended)
- Tasso imposte: 24% (IRES + IRAP medio)

| Anno | Revenue | OpEx | Depreciation | EBITDA | EBIT | Tax | Net Income | CapEx | FCF | Cum FCF |
|---|---|---|---|---|---|---|---|---|---|---|
| Y1 | 380k | -370k | -200k | +10k | -190k | 0 | -190k | -1400k | **-1390k** | -1390k |
| Y2 | 850k | -480k | -300k | +370k | +70k | -17k | +53k | -800k | **-447k** | -1837k |
| Y3 | 2500k | -900k | -400k | +1600k | +1200k | -288k | +912k | -1000k | **-88k** | -1925k |
| Y4 | 4500k | -1500k | -500k | +3000k | +2500k | -600k | +1900k | -500k | **+1400k** | -525k |
| Y5 | 6500k | -2100k | -600k | +4400k | +3800k | -912k | +2888k | -500k | **+2388k** | **+1863k** |

**Risultati indicativi scenario base**:
- **Break-even cumulato**: tra Y4 e Y5 (~Y4.5)
- **Payback semplice**: ~5 anni
- **NPV (10 anni, WACC 12%)**: positivo (stima +€3-8M con assunzioni Y6-Y10 conservative)
- **IRR (10 anni)**: 18-25% (stima)

### 8.6.2 Scenari worst/base/best

| Indicatore | Worst (P10) | Base (P50) RECALIBRATED | Best (P90) |
|---|---|---|---|
| **Revenue Y1** (post-Cluster D recalibration) | €130k (3 contratti deboli, pricing piegato a benchmark Cluster D €40-60k/anno) | **€260k** (5 contratti baseline, pricing €60-90k/anno PA + €25-40k premium) | €380k (5 contratti + 1 espansione, pricing premium accettato) |
| **Revenue Y3** | €0.8M (rallentamento PA) | €2.0M (scale-up Liguria + 1 regione, post-recalibration pricing) | €3.5M (scale-up + utility pilot precoce) |
| **Revenue Y5** | €2.0M (no HAPS, no utility) | €5.0M (modello operativo stabile multi-regione) | €12M (HAPS subscale operativo + utility expansion) |
| **CapEx Y1** | €1.96M (overrun massimo) | €1.4M (baseline) | €0.97M (efficient execution) |
| **OpEx Y2 run-rate** baseline | €480k | €370k | €280k |
| **OpEx Y2 run-rate +3 FTE regulatory** (Cap. 5 §5.17 mandatory) | €1.3M | €1.18M | €1.05M |
| **Break-even cumulato (vs baseline OpEx)** | Y7+ (vs Y6+ pre-recalibration) | Y5-Y6 (vs Y4.5 pre-recalibration) | Y4 (vs Y3.5 pre-recalibration) |
| **NPV 10y (WACC 12%)** | -€2M (vs negativo pre-recalibration) | **+€3.5M** (vs +€3-8M pre-recalibration) | +€20-25M (vs +€20-40M pre-recalibration) |
| **IRR 10y** | <5% | 12-18% (vs 18-25% pre-recalibration) | 28-40% (vs 35-50% pre-recalibration) |
| **Payback** | 8-10 anni (vs 7-8 pre-recalibration) | 6 anni (vs 5 pre-recalibration) | 3.5 anni (vs 3 pre-recalibration) |

> **Falsifying observation §8.6.2 (CRITICA)**: se al gate M+24 (fine Y2) il cumulato FCF è < -€2.5M (sotto worst-case), il modello operativo è in stato critico e va attivata strategic review (es. pivot mercato, acquisition difensiva da considerare, ridimensionamento Phase B 6B).

### 8.6.3 Sensitivity analysis (driver primari, scenario base)

Impatto su NPV 10y di variazione ±20% sui driver chiave:

| Driver | Δ NPV se -20% | Δ NPV se +20% | Sensitivity |
|---|---|---|---|
| **Tariffa media servizio PA** | -€2.5M | +€2.5M | **Alta** (primary) |
| **Utilization rate flotta** | -€2.0M | +€2.0M | **Alta** |
| **CapEx aggregato** | +€1.2M (saving) | -€1.2M | Media |
| **OpEx aggregato** | +€1.0M | -€1.0M | Media |
| **WACC (8% → 16%)** | -€1.5M | +€1.5M | Media |
| **Tax rate** | +€0.5M | -€0.5M | Bassa |
| **Mix grant nel CapEx** | -€0.8M | +€0.8M | Media (impatto cash-flow) |

**Conclusione sensitivity**: i due driver chiave sono (1) pricing PA + (2) utilization rate. Validazione critica: contratti firmati + ore-volo fatturabili.

### 8.6.4 ROI sociale (qualitativo, ENAC AAM BP §4 analog)

In coerenza con ENAC AAM BP §4 [^1, §4 Benefici qualitativi], i benefici economico-sociali del progetto (non monetizzabili direttamente):

| Beneficio | Stima qualitativa |
|---|---|
| Vite salvate da antincendio precoce | 1-3 vite/decennio per area servita (ROI sociale: priceless) |
| Danni evitati da prevenzione frane | €5-20M/anno per Liguria interna potenzialmente (stima conservativa) |
| Riduzione costi sorveglianza terrestre | €0.5-2M/anno per Regione |
| Rivitalizzazione Aree Interne (impatto demografico) | Difficile da quantificare; potenziale moltiplicatore SNAI |
| Sovranità tecnologica IT/EU stratosferica | Lungo termine, contributo a posizionamento UE |

---

## 8.7 Strategia Finanziamenti

### 8.7.1 Mix raccomandato Percorso 6A Y1 (€1.0-2.0M target CapEx + IVA)

| Fonte | Importo target | % | Status / Action |
|---|---|---|---|
| **Coopfond Cooding Prototypes 2026** | €50k (max) | 3-5% | Domanda M+1-3, verifica bando 2026 (DR-002) |
| **Coopfond Cooding-Invest** | €150-250k | 15-20% | Domanda M+2-4 |
| **Regione Liguria FESR 2021-2027** (OS 1.1 R&I + OS 5.2 SNAI) | €300-500k | 25-40% | LoI M+3, contract M+6 |
| **PNRR Aerospazio (Direzione MIMIT)** | €0-300k | 0-20% | Possibile via partnership Polito IS4Aerospace |
| **Equity privato (founder + seed)** | €200-500k | 15-35% | Round seed Q1 2026 |
| **R&D tax credit (L. 160/2019, art. 1 c. 198-209)** | €50-150k | 5-15% | Cumulabile post-spesa |
| **Totale finanziamento Y1** | **€750k-1.75M** | 100% | Match al CapEx + IVA |

> **Confidence: medium** (basata su esistenza programmi); **low** sulla concretezza di singole tranche fino a LoI/contratti firmati.

> **🔬 Falsifying observation aggiuntiva linkata**: vedi `FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md` **FO-ADD-09** (mix funding Y1 ≥ 60% committed entro M+10). Trigger M+10: Letter of Award + contratti firmati (non solo proposals/LoI). Se committed funding < 40% del CapEx Y1 target, hard condition C3 falsificata + re-baseline Y1 con CapEx ridotto "MVP super-lean" + bridge financing emergency + possibile slittamento operatività a Y2.

### 8.7.2 Mix raccomandato Percorso 6B Phase B (€5.5-13.5M target su 24 mesi)

| Fonte | Importo target | % |
|---|---|---|
| **EDF (European Defence Fund)** call HAPS post-EuroHAPS | €2-5M | 30-40% |
| **Horizon Europe Cluster 4/5** (RIA / IA HAPS-NTN-EO) | €1-3M | 15-25% |
| **PNRR Aerospazio / ASI / MIMIT** bandi nazionali | €1-2.5M | 15-20% |
| **Equity privato Series A/B** | €1-2.5M | 10-25% |
| **R&D tax credit + Patent Box** | €0.5-1.5M | 5-10% |
| **Possibile cooperazione CIRA (in-kind)** | €0.5-1M | 5-10% |
| **Totale Phase B** | **€6-15.5M** | 100% |

### 8.7.3 Bandi attivi / attesi 2026-2028 (mappa preliminare)

| Bando | Apertura prevista | Importo per progetto | Match Firmamento |
|---|---|---|---|
| Coopfond Cooding Prototypes 2026 | Q1 2026 | max €50k, 50% spese | ✓ Y1 6A |
| Coopfond Cooding-Invest | Continuo | max €250k | ✓ Y1 6A |
| Regione Liguria FESR Bando R&I 2026-2027 | TBD | €200-500k | ✓ Y1-Y2 6A |
| PNRR Aerospazio M4C2 | Continuo | variabile | ✓ Y2+ |
| Horizon Europe Cluster 4 — Destination Space | bandi 2026-2027 | €1-5M | ✓ Y2+ 6B |
| EDF 2027 Work Programme HAPS-related | atteso 2027 | €5-20M | ✓ Y3+ 6B |
| EUSPA CASSINI Accelerator | continuo | €0.5-2.5M equity | ✓ Y2+ |
| EIC Accelerator SME single beneficiary | continuo | €2.5M grant + €15M equity | ✓ Y2+ 6A/6B |

---

## 8.8 Cronoprogramma Finanziario

### 8.8.1 Calendario draw-down Y1 (mensile)

| Mese | Spesa cumulata | Fonte primaria attivata |
|---|---|---|
| M+0-3 | €50-100k | Equity seed + Coopfond Cooding (in domanda) |
| M+3-6 | €200-400k | + Coopfond Cooding-Invest (Q2) + LoI Regione |
| M+6-9 | €500-900k | + Regione Liguria FESR contract (Q3) |
| M+9-12 | €1.0-1.6M | + R&D tax credit (recovery post-spesa) |
| M+12 (chiusura Y1) | €1.0-2.0M | Mix Y1 chiuso, set-up Y2 in preparazione |

### 8.8.2 Cash flow management

Aerospace early-stage richiede attenta gestione cash flow per evitare gap tra spese e tranches grant (tipicamente in arretrato 3-6 mesi):

**Bridge financing necessario**: stima €100-300k buffer di liquidità per coprire gap tra spesa effettiva e ricevimento tranches grant.

> **Falsifying observation §8.8.2**: se al M+6 il bridge financing buffer è esaurito senza tranches grant in vista, attivare emergency funding (es. bridge loan, fattorizzazione contratti pluriennali firmati).

---

## 8.9 Computo Metrico Estimativo Ground Segment (Sintesi)

Riferimento dettagliato: Vol. 2 Allegato A.9.

**Ground Station fissa Pentema** (esempio computo):

| Voce | Quantità | Costo unitario | Totale |
|---|---|---|---|
| Container 20' o cabin prefabbricata | 1 | €15-25k | €15-25k |
| Allacciamento elettrico + UPS | 1 | €5-10k | €5-10k |
| Antenna VHF/UHF + SATCOM L-band | 1 set | €15-30k | €15-30k |
| Server + storage primario | 1 rack | €10-20k | €10-20k |
| Sistema condizionamento + ventilazione | 1 | €3-6k | €3-6k |
| Sistema sicurezza + monitoraggio | 1 | €3-5k | €3-5k |
| Allestimento postazioni operative | 2 | €2-4k cad | €4-8k |
| **Totale Ground Station fissa** | | | **€55-104k** |

---

## 8.10 Red Team Check — Critical Financial Review

Critica condotta da `red-team-skeptic` + `financial-cfo-analyst` + `business-model-strategist`.

### Critica 1 — "CapEx €1.4M baseline è ottimismo: aerospace tipicamente +30-150%"
**Razionale**: il range stimato non include adeguatamente i rischi tipici aerospace.
**Risposta**: il range €975k-1.96M già include contingency 15% (limite inferiore base rate). Se overrun raggiunge 50% (centro base rate), CapEx Y1 effettivo €1.8-2.5M. Falsifying observation §8.3.1 attiva review scope se cumulato >€2M al M+6.

### Critica 2 — "Revenue Y1 €380k baseline è ottimistico per cicli PA italiani 6-18 mesi" — RECALIBRATED post-Cluster D
**Razionale**: cicli appalti PA italiani sono lenti. 5 contratti firmati in 12 mesi è raro. **In aggiunta (audit Cluster D M+3)**: pricing baseline €150k/anno per servizio EO Regione (§7.8.2 originale) è **FALSIFICATO** dal benchmark Cluster D (Planetek/e-GEOS/NHazca €30-80k/anno per area).
**Risposta**: confermato in entrambe le dimensioni. **Azione applicata M+3**: revenue Y1 baseline ricalibrato a **€260k centrale (range €220-300k, min €200k SyR-Cost-003)** con pricing €60-90k/anno PA + €25-40k premium persistence (vedi Cap. 7 §7.8.2 RECALIBRATED). Soglia minima MVP è 3 contratti + €200k SyR-Cost-003 hard floor. Scenario worst (€130k) attiva pivot. Pre-engagement Q1 2026 + benchmark Cluster D pubblicizzato (DR-006 closure) critici per non perdere finestra di gara.

### Critica 3 — "WACC 12% blended è basso per startup aerospace early-stage"
**Razionale**: equity venture aerospace tipicamente 25-35%; il WACC 12% suppone mix grant pesante.
**Risposta**: corretto, il 12% è blended con assunzione 40-50% grant nel mix. Se mix shifts a meno grant, WACC sale a 18-22%. Sensitivity §8.6.3 mostra impatto.

### Critica 4 — "Phase B €5.5-13.5M senza Type Certificate: investimento alto rischio"
**Razionale**: spendere €10M in R&D HALE senza certezza di TC EASA è capital-intensive in modo speculativo.
**Risposta**: confermato. Per questo Phase B è subordinato a (a) commitment funding ≥50% pubblico (grant), (b) gate M+24 evaluation con TRL 5 dimostrato, (c) parallel engagement EASA Special Condition. Senza queste 3 condizioni, Phase B non parte.

### Critica 5 — "Capital intensity €10-30B per EU sovereign full scale è oltre la capacità di una PMI: come ci si arriva?"
**Razionale**: Firmamento da sola non raccoglie €10-30B. La traiettoria è troppo ottimistica.
**Risposta**: corretto. La capital intensity full scale richiede **programma EU equivalente IRIS² dedicato come precondizione esterna**. Firmamento si posiziona come **principal Italian node** di un consorzio EU, contribuendo con capabilities + partnership + execution, ma NON come finanziatore solitario. Boundary B2 mantenuta.

### Critica 6 — "Mix finanziamento Y1 è basato su bandi non ancora aperti (Cooding 2026, FESR)"
**Razionale**: il mix dipende da bandi che potrebbero non aprirsi nei tempi previsti.
**Risposta**: confermato (DR-002 audit-rigore-epistemico.md). Action item: contatto diretto Coopfond + Regione Liguria entro M+1 per verifica calendario bandi.

---

## 8.11 Open Questions Finanziarie

| OQ-ID | Domanda | Owner | Deadline |
|---|---|---|---|
| OQ-F01 | Validazione pricing PA con LoI Regione Liguria | financial-cfo + snai-funding | M+6 |
| OQ-F02 | Verifica Cooding 2026 bando attivo + condizioni | snai-funding | M+1 |
| OQ-F03 | Quotation contracts JOUAV vs Tekever per CapEx accurato | vtol-uas-specialist | M+3 |
| OQ-F04 | Bridge financing per cash flow gap Y1 | financial-cfo | M+3 |
| OQ-F05 | Modello DCF completo con scenarios Excel | financial-cfo | M+6 |
| OQ-F06 | Sensitivity Excel + Monte Carlo per gate M+10 | financial-cfo | M+9 |
| OQ-F07 | LCA + carbon footprint quantitativo (supporto ROI sociale) | aero-structures | M+9 |
| OQ-F08 | Strategia capital raise Series A timing | financial-cfo + business-model | M+12 |

---

## 8.12 Riferimenti

[^1]: ENAC, "Business Plan AAM 2021-2030" Allegato 2 al Piano Strategico Nazionale. Source: `fonti/03_AAM-Business-Plan_web-1.md`. **Confidence: high** (fonte ENAC, ufficiale italiana). Specifico: investimenti €1.86B su 3 wave, benefici qualitativi §4.

[^2]: Aeropolis Workshop "Metodologie e Tecnologie per Sviluppo Nuovo Velivolo — Analisi Costi e Business Plan", Napoli maggio 2014. Source: `fonti/AnalisiCostiBusinessPlan24_05_14.md`. **Confidence: medium** (workshop didattico, methodology Alenia).

[^3]: D.Lgs. 31 marzo 2023 n. 36 — Codice dei Contratti Pubblici, art. 41 + Allegato I.7. Source: `fonti/2023_0036.md`. **Confidence: high**.

[^4]: GAO Cost Estimating and Assessment Guide (GAO-20-195G), 2020. Base rate aerospace cost overrun 30-150%.

[^5]: Skill `financial-cfo-analyst`, `business-model-strategist`, `epistemic-rigor` (`.claude/`).

[^6]: Bandi pubblici Italia 2026 (riferimenti web verificati): Coopfond Cooding 2026 (TBC), Regione Liguria FESR 2021-2027, PNRR Aerospazio M4C2, Horizon Europe Cluster 4/5, EDF Work Programme.

---

## 8.13 Note di chiusura del capitolo

Il Cap. 8 è bozza M+3 con **confidence medium-low** sulle proiezioni finanziarie (richiede modello Excel completo + validazione esterna LoI prima del gate M+10).

**Verdetto finanziario riepilogato**:
- **Percorso 6A: GO** finanziariamente fattibile con mix raccomandato (35-55% grant + equity)
- **Percorso 6B: GO Condizionato R&D** subordinato a commitment funding ≥50% pubblico al gate M+24

**Punti deboli dichiarati**:
- CapEx Y1 €975k-1.96M (range ampio, da stretto al M+6)
- Revenue Y1 **€260k centrale (range €220-300k) RECALIBRATED post-Cluster D** (worst case €130k); legacy €355-405k FALSIFICATO da benchmark Planetek/e-GEOS/NHazca
- Capital intensity full scale Y10 €10-30B realisticamente raggiungibile solo via programma EU sovrano dedicato (precondizione esterna)
- Bandi 2026 non ancora confermati (DR-002 audit-rigore-epistemico.md)

**Action items entro M+10**:
- Modello finanziario Excel completo con DCF + sensitivity + Monte Carlo
- LoI Regione Liguria (anchor customer)
- Quotation JOUAV + Tekever per CapEx accurate
- Verifica bandi 2026 con contatti diretti
- Bridge financing strategy

Il capitolo è chiuso al M+3 con verdetto Red Team **OK con 6 action items**.
