# Audit Quality Investment-Grade. M+3 Final Review

> **Data:** 17 maggio 2026 (M+3, proiezione M+11)
> **Scope:** Volume 1 (Cap. 0-11) + Volume 2 Allegati (A1-A13 + Energy + Financial + Vendor RFQ) + Volume 3 Riferimenti (R1-R5) + 4 audit precedenti (RedTeam + Competitor + Regulatory + Quality).
> **Mandato:** verifica investment-grade per 5 target audience: Coopfond/Legacoop, Regione Liguria/Protezione Civile, PNRR Aerospazio/MIMIT, EDF/Horizon/EU, Investor seed/Series A.
> **Boundary conditions non attaccabili:** B1 (service-only + cooperative Legacoop) + B2 (EU sovereign / "complementare IRIS²"). I 3 audit avversariali precedenti attaccano *come ci si arriva*, non gli obiettivi strategici.
> **Stile:** brutalmente fattuale, no whitewashing.

---

## 0. Verdetto sintetico

> **QUASI-INVESTMENT-GRADE per audience PA/cooperativa con 11 FIX VINCOLANTI; NON investment-grade per VC top-tier né per EDF/Horizon nello stato attuale M+3.**

Detail:
- **Coopfond / Legacoop**: **READY** (con caveat), il documento è formalmente più rigoroso del 90% degli SDF aerospace italiani early-stage.
- **Regione Liguria + PC**: **READY** sui contenuti (Pentema motivato, KPI quantitativi, ROI sociale), **NOT READY** sull'evidenza esterna (LoI mancante, pre-app ENAC mancante, DPIA non depositata).
- **PNRR Aerospazio / MIMIT**: **PARTIALLY READY** (Cap. 5 NIS2/Part-IS coperto, Cap. 8 Quadro Economico art.41 OK), **non investment-grade** senza Cap. 5 §5.16 riscritto come pillar, non come addendum.
- **EDF / Horizon Europe**: **NOT READY**. Il documento dichiara onestamente confidence low su TAM commerciale single-source (MarkNtel) + EuroHAPS Phase 2 non calendarizzata + CIRA partnership non firmata + framework EASA HAPS non aperto. La forma è impeccabile, le evidenze sono insufficienti.
- **Investor VC / seed**: **NOT READY** in scenario "Series A presentation". Il modello finanziario è executable (161 formule, 10 sheet) ma il pricing Cluster D recalibrato post-audit (€60-90k vs €150k baseline) ha **declassificato** automaticamente il revenue Y1 da €355-405k a €220-260k, e P(Go pieno) = 5-15% scenario realistico (dichiarato). Un VC top-tier rigetta su questa base.

**Forza unica del documento**: l'**onestà metodologica** (4 audit avversariali integrati con response e action items, scenario B2-relaxed esplicitato, base rate 0% HALE solari operativi dichiarata, sliding timeline §9.12, caveat post-DR-014 capital intensity). Questa è leva di credibilità verso audience sofisticate (DG DEFIS, RINA review, EIB DCF specialist), ma può essere debolezza verso audience "pitch deck classico" (founder-mode VC) che si aspettano un documento puramente bullish.

---

## 1. Confidence levels

### 1.1 Statistiche aggregate

| Capitolo | Confidence dichiarate | FO dichiarate | Confidence/FO ratio |
|---|---:|---:|---:|
| Cap. 0 Sintesi Esecutiva | 0 | 1 | n/a |
| Cap. 1 Inquadramento | 16 | 4 | 4.0 |
| Cap. 2 Stakeholder/SMART | 12 | 9 | 1.3 |
| Cap. 3 Requisiti/RTM | **61** | **28** | 2.2 |
| Cap. 4 Scope/ICD | 14 | 3 | 4.7 |
| Cap. 5 Quadro Normativo | 14 | 21 | 0.7 |
| Cap. 6 Analisi Tecnica | 9 | 7 | 1.3 |
| Cap. 7 Mercato/Business | **31** | 9 | 3.4 |
| Cap. 8 Economico-Fin. | 5 | 6 | 0.8 |
| Cap. 9 Cronoprogramma | 2 | 3 | 0.7 |
| Cap. 10 Verdetto | 0 | 0 | n/a |
| Cap. 11 Roadmap | 11 | 22 | 0.5 |

### 1.2 Inconsistenze e gap

1. **Cap. 0 (Sintesi Esecutiva) non dichiara nessuna confidence per i numeri chiave** §0.11 (NPV +€3-8M, IRR 18-25%, ARR Y3 €1.5-3.5M, capital intensity Y10 €500M-2B / €10-30B). Per audience investor questo è **deal-breaker**: la sintesi esecutiva è il documento più letto, e nessun numero ha confidence dichiarato accanto. **FIX OBBLIGATORIO**.

2. **Cap. 8 (Economico-Finanziario) ha solo 5 confidence dichiarate** in tutto il capitolo finanziario. La tabella §8.6.1 cash flow Y1-Y5 e §8.6.2 scenari worst/base/best **non hanno confidence per riga**. Il caveat §8.6.1 dichiara "low per anni Y3+" ma non applicato cella per cella. **FIX RACCOMANDATO**: aggiungere colonna "Confidence" alla tabella P&L Y1-Y5 e scenari.

3. **Cap. 9 (Cronoprogramma) ha solo 2 confidence dichiarate** nonostante §9.12 sliding timeline contenga 16 milestone con slippage atteso. Confidence per ogni milestone (es. SORA M+9 nominale = confidence low, M+15-24 sliding = confidence medium-high) **non è dichiarata**. **FIX RACCOMANDATO**.

4. **Cap. 10 (Verdetto) ha 0 confidence levels esplicite** nonostante l'intero capitolo sia il verdetto del documento. §10.0bis.1 ha probabilità (5-15%, 45-60%, 20-30%, 5-10%) ma **non confidence sulle probabilità stesse**. Quanto è la confidence che "Scenario B base case ha 45-60% probabilità"? **FIX OBBLIGATORIO**.

5. **DR findings sono trasferiti con confidence in 2/9 casi su 9** dei DR chiusi/parz-chiusi (`DR-research-closure-M3.md`). Esempi:
   - DR-014 (capital intensity $50M-1B) **non ha confidence** trasferita esplicitamente in Cap. 8 caveat (è dichiarato "benchmark" senza confidence)
   - DR-013 (0% base rate HALE) **è dichiarato confidence high in DR doc** ma trasferito in Cap. 6 §6.0.1 senza confidence esplicita ("CAVEAT CRITICO POST DR-013" ma non "confidence high")
   - DR-009 (IRIS² no stratospheric) trasferito con confidence implicita "high" in §5.16bis, OK

6. **Numeri commerciali single-source declassificati a low ma usati come baseline**:
   - TAM HAPS MarkNtel €99M→€240M: dichiarato "confidence low" Cap. 7 §7.1.2 ✓
   - Costo Zephyr/Skydweller: dichiarato "vendor PR confidence medium-low" Cap. 7 ✓
   - Insurance BVLOS €15-40k/anno: NO confidence dichiarata in Cap. 8 §8.5.1 ⚠️
   - Pricing PA €150k/anno: **falsificato post-audit Cluster D** e dichiarato in §7.4.4.2 + financial model README; ma Cap. 8 §8.6.1 baseline ancora usa €380k revenue Y1 senza nota di recalibrazione. **INCONSISTENZA CRITICA Cap. 7 vs Cap. 8**.

7. **Numeri normativi sono uniformemente confidence high** ✓ (D.Lgs. 36/2023 + Reg. UE 2019/947 + EASA SORA 2.5 + GDPR + NIS2). Coerente con la regola.

### 1.3 Verdetto Confidence Levels

**ONESTÀ METODOLOGICA: 8.5/10**. La disciplina è applicata in modo eccezionale in Cap. 1, 3, 7, 11. È **lacunosa** in Cap. 0, 8, 9, 10, proprio i capitoli più letti da audience investment-grade. **FIX OBBLIGATORIO**: applicare la stessa disciplina al Cap. 0 (sintesi esecutiva) + Cap. 10 (verdetto) + tabelle finanziarie Cap. 8.

---

## 2. Falsifying observations

### 2.1 Conteggio per capitolo (target NASA SE: 4-7 per capitolo)

| Capitolo | FO totali | Target 4-7 | Status |
|---|---:|:---:|---|
| Cap. 0 | 1 | 4-7 | ⚠️ **SOTTO TARGET** (Sintesi Esecutiva non ha FO aggregate) |
| Cap. 1 | 4 | 4-7 | ✓ |
| Cap. 2 | 9 | 4-7 | ✓ over-target |
| Cap. 3 | 28 | 4-7 | ✓✓ eccezionale (richiede tassonomia) |
| Cap. 4 | 3 | 4-7 | ⚠️ **SOTTO TARGET** (3 < 4) |
| Cap. 5 | 21 | 4-7 | ✓ over-target (15 showstopper + 6 base) |
| Cap. 6 | 7 | 4-7 | ✓ esattamente in target |
| Cap. 7 | 9 | 4-7 | ✓ |
| Cap. 8 | 6 | 4-7 | ✓ |
| Cap. 9 | 3 | 4-7 | ⚠️ **SOTTO TARGET** (3 < 4) |
| Cap. 10 | 0 | 4-7 | ⚠️ **GAP CRITICO** (0 FO nel verdetto!) |
| Cap. 11 | 22 | 4-7 | ✓✓ over-target |
| **+ Addendum M+3** | **+10 FO-ADD** | n/a | ✓ chiude la lacuna |

**Totale Volume 1**: ~135 FO dichiarate (+ 10 ADD = ~145). Eccede ampiamente il "target ~40" dichiarato in Cap. 0.11.

### 2.2 Qualità delle FO (operative, osservabili, datate)

Sample analizzato:
- **FO-NegR-Mkt-001** (Cap. 3): "linguaggio 'alternativa Starlink' appare in sito web / press release / pitch deck / social": **operativo, osservabile, ma non datato** (manca threshold temporale). ⚠️ Minor.
- **FO-ADD-04 pricing PA**: "se entro M+9 nessun contratto Regione Liguria firmato a pricing ≥ €100k/anno": **operativo + osservabile + datato** ✓
- **FO-ADD-10 Visione 10 anni**: 4 milestone Y4/Y6/Y8/Y9 con soglie ARR/funding: **operativo + datato** ✓
- **§9.12.6 sliding timeline**: "slippage cumulato > 30% al M+12": **operativo + osservabile + datato** ✓
- **§8.6.2**: "FCF cumulato Y2 < -€2.5M attiva strategic review": **operativo + osservabile + datato** ✓
- **Cap. 10**: **0 FO esplicite nel verdetto**, il verdetto contiene scenari A-D con probabilità ma non FO di attivazione. ⚠️ **GAP CRITICO**.

### 2.3 Top-50 FO complessive identificabili

**Identificabili sì, ma non centralizzate**. Le FO sono distribuite nei capitoli + FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md (10 FO ADD). Manca una **TOP-50 FO consolidate** in un singolo documento per gate review. ⚠️ Per investment-grade VC top-tier serve una **FO Master Table** con: FO-ID, claim originale, trigger osservabile, data milestone, action se attivata, owner. **FIX RACCOMANDATO M+6**.

### 2.4 Verdetto FO

**RIGORE: 9/10**. La distribuzione è eccezionale per Cap. 1-3-5-7-8-11. **3 capitoli SOTTO TARGET** (Cap. 0, 4, 9). **Cap. 10 ha 0 FO esplicite**: questo è il **gap più visibile** per investment-grade. **FIX OBBLIGATORIO pre-G3**.

---

## 3. Linguaggio pubblico

### 3.1 Pattern "complementare IRIS²"

| File | Occorrenze "complementare IRIS²" | Occorrenze "alternativa Starlink" |
|---|---:|---:|
| Cap. 0 | 0 (solo "complementare a IRIS²" 3×) | 1 (in clausola NEGATIVA) |
| Cap. 1 | 4 | 3 (in NEGATIVE: "mai", "non", "RESERVED") |
| Cap. 5 | 3 | 4 (in NEGATIVE: §5.0bis dichiarazione boundary) |
| Cap. 11 | 8 | 5 (3 negative + 2 con caveat post-DR-014) |
| Allegato A1-RTM | 2 | 2 (NegR-Mkt-001 dichiarazione vincolante) |

**Risultato**: **18 occorrenze "complementare IRIS²" in Volume 1**. **20 occorrenze "alternativa Starlink"** ma **17/20 sono in formulazione NEGATIVA** ("NON usare", "mai", "linguaggio scartato", clausola NegR-Mkt-001).

Le **3/20 occorrenze NON-negative** di "alternativa Starlink":
1. **Cap. 8 §0.0.3 row "Scenario EU sovereign full scale"**: "(100+ HAPS, **alternativa Starlink EU**)", è dichiarato come scenario teorico capital intensity €10-30B con precondizione esterna IRIS²-equivalent. Tecnicamente in contesto interno tecnico, ma usato in tabella visibile. ⚠️ **MINOR: rimuovere parentetica "alternativa Starlink EU"** dato che è inutile e contraddice NegR-Mkt-001.
2. **Cap. 7 §7.5.2** (riga 494): "Alternativa europea a Starlink": appare in lista di **linguaggio da NON usare**. ✓ OK contesto.
3. **Cap. 7 §7.12.2.667** caveat capital intensity: "Per scala 'alternativa Starlink EU' servono **€10-30B**": usa virgolette per marcare distanza ma ancora ambiguo. ⚠️ **MINOR: riscrivere come "Per scala EU sovereign full scale"**.

### 3.2 Pattern "operatore di servizi" vs "OEM aeronautico"

- **"Operatore di servizi"**: 30+ occorrenze in Cap. 1, 2, 7, 11, uso disciplinato ✓
- **"OEM aeronautico" usato come termine di contrasto NEGATIVO**: 5 occorrenze (Cap. 1 r.21, Cap. 2 r.33, Cap. 4 r.35, Cap. 7 r.22, Cap. 3 r.510) ✓
- **"Vendita di velivoli" / "no vendita asset"**: 13 occorrenze, sempre in contesto NEGATIVO ✓
- **NegR-B-001** (Cap. 3.5.8): formalmente dichiarato come vincolo "Critical" con audit semestrale contratti ✓

### 3.3 Pattern "Visione strategica 10 anni" vs "Operatività garantita"

- **"Visione strategica 10 anni"** / **"vettore strategico"**: 48 occorrenze ✓
- **"Operatività garantita 10 anni"** / **"garantito 10 anni"**: 0 occorrenze ✓
- **Disclaimer finale Cap. 11.13** (riga 952): "la roadmap presentata è **vettore strategico onesto**, non promessa di esecuzione lineare. La probabilità che il vettore venga eseguito esattamente come descritto è **bassa (6-15%)**" ✓

### 3.4 Verdetto linguaggio pubblico

**DISCIPLINA: 9.5/10**. La disciplina è applicata in modo eccezionale. **2 fix minori**: rimuovere parentetica "(alternativa Starlink EU)" da Cap. 8 §0.0.3 e Cap. 7 §7.12.2.667. Non bloccante per investment-grade ma irritante per audit RESERVED-rischi-geopolitici.

---

## 4. Boundary conditions B1 + B2

### 4.1 B1 (service-only + cooperative Legacoop). Preservazione

| Cap. | B1 dichiarata in §0bis? | Coerenza interna? | Note |
|---|:---:|---|---|
| Cap. 1 | ✓ §1.0bis | ✓ pillar centrale | Cooperatività esplicitata come scelta strutturale, non vantaggio competitivo (Red Team R1 OK) |
| Cap. 2 | ✓ §2.0bis | ✓ SMART obj derivati | 30 obj coerenti con service-only |
| Cap. 3 | ✓ §3.0bis | ✓ + NegR-B-001 Critical | Audit semestrale contratti vendita asset |
| Cap. 4 | ✓ §4.0bis | ✓ Scope service-only | "NON è in scope alcuna vendita velivoli" esplicito |
| Cap. 5 | ✓ §5.0bis | ✓ Quadro normativo service-only | Modello operatore Starlink-equivalente |
| Cap. 6 | ✓ §6.0bis | ✓ Architettura supporta servizi | Asset riusabili 6A→6B per servizio |
| Cap. 7 | ✓ §7.0bis | ✓ Business model service-only | 4 archetipi revenue, no transattivo |
| Cap. 8 | ✓ §8.0bis | ✓ + Caveat post-DR-014 | Service-only consente "no full capex se operare HAPS altrui" |
| Cap. 9 | ✓ §9.0bis (sintetico) | ✓ Milestone tutti erogazione servizi | Cronoprogramma service-driven |
| Cap. 10 | ✓ §10.7 "cosa non facciamo" | ✓ "Non vendiamo velivoli" #1 in lista | NegR-B-001 binding |
| Cap. 11 | ✓ §11.0bis | ✓ B1 preservata fino Y10 | Anche scenario B2-relaxed mantiene B1 integralmente |

**VERDETTO B1**: **preservazione perfetta in 11/11 capitoli**. La cooperatività è trattata come given strategico, **non** come "vantaggio competitivo". L'unica critica residua: Cap. 7 §7.5.1 "modello cooperativo come pilastro vantaggio competitivo" (rivisitato post-audit Cluster D §7.4.4-7), il pilastro #2 è dichiarato non difendibile vs Cluster D. **FO-ADD-01** del FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md formalizza questo.

### 4.2 B2 (EU sovereign / complementare IRIS²). Preservazione

| Cap. | B2 dichiarata in §0bis? | Linguaggio pubblico OK? | Confidence appropriato? |
|---|:---:|:---:|---|
| Cap. 0 | ✓ §0.4 | ✓ "complementare IRIS²" + "mai alternativa Starlink" | ⚠️ confidence non dichiarato |
| Cap. 1 | ✓ §1.0bis B2 | ✓ | ✓ visione esplicitamente "vettore strategico" |
| Cap. 5 | ✓ §5.0bis + §5.16bis post-DR-009 | ✓ "complementarità è opportunità non integrazione predefinita" | ✓ aspirazione Y4-Y7 dichiarata |
| Cap. 7 | ✓ §7.5.2 + §7.0bis | ✓ disclaimer NDA-only | ✓ |
| Cap. 8 | ✓ §8.0bis | ⚠️ §0.0.3 "alternativa Starlink EU" parentetica | ✓ caveat capital intensity onesto |
| Cap. 11 | ✓ §11.0bis + §11.6bis B2-relaxed | ✓ disclaimer §11.5.2 + Cap. 11.13 finale | ✓ probabilità 6-15% B2 full dichiarata |

**VERDETTO B2**: **preservazione robusta**, con **scenario B2-relaxed** formalmente integrato (Cap. 11 §11.6bis come raccomandato dall'audit M+3). **2 fix minori sul linguaggio** (Cap. 8 + Cap. 7 §7.12.2.667).

### 4.3 Verdetto Boundary Conditions

**INTEGRITÀ: 9.5/10**. B1+B2 preservate in 11/11 capitoli. Scenario B2-relaxed esplicitato. NegR-Mkt-001 + NegR-B-001 binding nella RTM v1.0. **2 fix minori linguistici** non bloccanti.

---

## 5. Disciplina epistemica (7 regole skill epistemic-rigor)

### 5.1 Audit per capitolo

| Regola | Cap. 0 | Cap. 1 | Cap. 2 | Cap. 3 | Cap. 4 | Cap. 5 | Cap. 6 | Cap. 7 | Cap. 8 | Cap. 9 | Cap. 10 | Cap. 11 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| R1 Falsifiability | ⚠️ | ✓ | ✓ | ✓✓ | ⚠️ | ✓ | ✓ | ✓ | ✓ | ⚠️ | ⚠️ | ✓✓ |
| R2 Triangulation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓ | ⚠️ (TAM single-source) | ⚠️ | ✓ | ✓ | ✓ |
| R3 Source provenance | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| R4 Confidence levels | ⚠️ | ✓ | ✓ | ✓✓ | ✓ | ✓ | ✓ | ✓ | ⚠️ | ⚠️ | ⚠️ | ✓ |
| R5 Pre-mortem | ⚠️ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ | ✓✓ |
| R6 Distinzione concetti | ⚠️ (Critica G-05 RedTeam aperta) | ⚠️ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ⚠️ (Critica G-05) | ✓ |
| R7 Base rates | ⚠️ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓✓ (0% HALE) | ✓ (programmi falliti) | ⚠️ (aerospace cost overrun citato ma non applicato a CapEx Y1) | ⚠️ | ✓ | ✓ |

### 5.2 Gap critici identificati

1. **R1 (Falsifiability): Cap. 10 ha 0 FO esplicite**. ⚠️ FIX obbligatorio.
2. **R4 (Confidence): Cap. 0, 8, 9, 10 sotto-applicato**. ⚠️ FIX obbligatorio.
3. **R5 (Pre-mortem): Cap. 0 non ha pre-mortem aggregato**. Pre-mortem aggregato esiste in AUDIT-QUALITY-VOLUME-1.md §7 ma **non trasferito in Cap. 0**. ⚠️ FIX raccomandato.
4. **R6 (Distinzione concetti): Critica G-05 Red Team identifica confusione "feasibile / fattibile / operativo"** in Cap. 0, 6, 10. **Risposta nei capitoli: non implementata**, il documento sa che è un problema, lo dichiara, non lo corregge. ⚠️ FIX raccomandato Cap. 0 + Cap. 10.
5. **R7 (Base rates): Cap. 8 cita "base rate aerospace cost overrun 30-150%" (GAO-20-195G ref) ma applica contingency solo 15%**. Inconsistenza: l'output del scenario base CapEx Y1 €1.4M è 30% sotto la base rate aerospace. ⚠️ FIX raccomandato.

### 5.3 Steel-manning della posizione contraria

- **Cap. 1 Red Team (5 critiche)**: ✓ steel-manning R1-R5 con risposte dettagliate
- **Cap. 7 Red Team (6 critiche post-Cluster D)**: ✓ steel-manning su Starlink, modello cooperativo, TAM ottimismo, AALTO entry, MVP ambizioso, pricing inventato, tutti con **risposta + action item**
- **Cap. 10 Red Team (6 critiche)**: ✓ steel-manning ma **Red Team critica G-08** dell'AUDIT-REDTEAM: "Tutte le risposte concludono in difesa del verdetto. Nessuna critica ha provocato modifica del verdetto. Pattern 'red team theater'". Questa critica è valida: post-audit M+3 il Cap. 10 ha aggiunto §10.0bis con HOLD CON PIANO RAFFORZATO come scenario base, **risolvendo la critica G-08** ✓ POST-FIX
- **Cap. 8 Red Team (6 critiche)**: ✓ steel-manning su CapEx, Revenue, WACC, Phase B, Capital Intensity, Mix funding

**VERDETTO STEEL-MANNING: 9/10**. Eccezionale per documento aerospace early-stage. Il pattern "red team theater" del Cap. 10 originale è stato corretto post-audit M+3.

### 5.4 Base rate aerospace dichiarate

| Base rate | Citata in | Confidence | Applicata? |
|---|---|---|---|
| **0% HALE solari commerciali operativi (DR-013)** | Cap. 6 §6.0, Cap. 7 §7.1.2, Cap. 10 §10.0bis.2 | high | ✓ Hold 6B subordinato a partnership prime contractor |
| **Capital intensity $50M-1B per HALE operativo (DR-014)** | Cap. 6 §6.0, Cap. 8 §8.3.3, Cap. 10 §10.0bis.2 | high | ✓ riposizionamento "Phase B = R&D Phase 0/A" |
| **Aerospace cost overrun 30-150% (GAO-20-195G)** | Cap. 8 §8.10 critica 1, §8.12 ref | medium-high | ⚠️ **NON applicata**: contingency 15% non riflette base rate centro 30-50% |
| **EASA novel framework 5-10 anni (Critica regulatory)** | Cap. 5 §5.16, Cap. 9 §9.12 sliding | high | ✓ sliding timeline assume M+60-120 vs M+36+ nominale |
| **SORA SAIL II-III approval 8-14 mesi (audit Regulatory)** | Cap. 9 §9.12 sliding | medium | ✓ sliding M+15-24 vs M+9 nominale |
| **Pilota commerciale 12 mesi (base rate 18-36)** | AUDIT-QUALITY-VOLUME-1.md §5 base rate #2 | high | ⚠️ NON applicata a Cap. 9 piano nominale |
| **TRL 4→6 in 24 mesi (base rate 3-5 anni)** | AUDIT-QUALITY-VOLUME-1.md §5 base rate #3 | high | ⚠️ NON applicata a Cap. 11 Fase 3 |
| **Bandi pubblici vinti al primo tentativo 15-25%** | AUDIT-QUALITY-VOLUME-1.md §5 base rate #11 | medium | ⚠️ NON applicata a Cap. 8 mix funding 60% target |
| **Startup aerospace seed→revenue operational 10-20%** | DR-007 (aperto), Cap. 7 §7.1.2 | low | ⚠️ NON triangulata né applicata |

**Verdetto base rate**: **4 out of 9 base rate non applicate** dove dovrebbero essere. Le base rate citate sono CITATE ma non sempre RIFLESSE nei piani. Questo è il **pattern G-03 del Red Team audit** ancora non chiuso.

### 5.5 Survivor bias

- **Cap. 6 §6.0.1**: lista programmi falliti (Helios, Aalto HAWK30, Solara 50, Sanswire) ✓
- **Cap. 7 §7.1.2**: lista programmi falliti ✓
- **Cap. 10 §10.6 Critica 4**: survivor bias dichiarato ✓
- **DR-013 chiusura**: 12 programmi 2003-2025 analizzati, 0% commerciali civili operativi ✓ **confidence high**
- **Cap. 11 §11.4**: NON cita esplicitamente i programmi falliti nelle assumption Fase 3 ⚠️ MINOR

**Verdetto survivor bias: 8.5/10**. Coperto in Cap. 6, 7, 10. Manca riflesso esplicito in Cap. 11 Fase 3-5.

### 5.6 Verdetto disciplina epistemica

**RIGORE: 8.5/10**. Eccezionale in Cap. 1, 3, 5, 7, 11. **4 gap critici da chiudere**: Cap. 0 (no FO + no confidence), Cap. 10 (no FO + R6 distinzione concetti aperta), Cap. 8 (R4 + R7 sotto-applicate), Cap. 9 (R4 + R1 sotto-applicate).

---

## 6. Red Team check coverage

### 6.1 Capitoli con Red Team check

| Cap. | Red Team explicit | # critiche | Response + action items? | Qualità critiche |
|---|:---:|:---:|:---:|---|
| Cap. 0 | ⚠️ no esplicito | 0 | n/a | ⚠️ Sintesi Esecutiva non auditata dal RT |
| Cap. 1 | ✓ §1.10 | 5 (R1-R5) | ✓ 5 action items + 6 DR | Eccellente |
| Cap. 2 | ✓ §2.6 | 7+ (multiple) | ✓ | Buono |
| Cap. 3 | ✓ §3.11 | 6 | ✓ + NegR section aggiunta come response | Eccellente |
| Cap. 4 | ✓ §4.8 | 5+ | ✓ | Buono |
| Cap. 5 | ✓ §5.13 (esistente) + §5.16 (post-audit RegAdv) | 4 base + 15 showstopper post | ✓ 15 mitigation owner | Eccellente post-fix |
| Cap. 6 | ✓ §6.8 | 6 | ✓ + action items | Buono |
| Cap. 7 | ✓ §7.13 (post Cluster D) | 6 + revisione §7.4.4-7 | ✓ 8 action items | Eccellente post-fix |
| Cap. 8 | ✓ §8.10 | 6 | ✓ + 6 action items | Buono |
| Cap. 9 | ✓ §9.8 + §9.12 sliding (post-audit) | 5 base + sliding timeline | ✓ + mitigation | Buono post-fix |
| Cap. 10 | ✓ §10.6 (6 critiche) + §10.0bis post-audit | 6 + revisione scenario base | ✓ + response | Eccellente post-fix |
| Cap. 11 | ✓ §11.10 + §11.6bis post-audit | 5 + scenario B2-relaxed | ✓ + 8 trigger | Eccellente |

### 6.2 Coerenza tra i 4 audit avversariali

| Tema cross-audit | RedTeam | Competitor | Regulatory | Quality | Coerenza? |
|---|---|---|---|---|---|
| **P(Go pieno 6A) realistica** | 15-35% | <15% standalone | 35-45% blocco operativo M+12-18 | 5-15% (audit Q calcolo) | ✓ allineati su "5-35%, scenario base = Hold" |
| **6B HALE prospettive** | "Hold corretto ma framework HAPS = placebo" | "Acquisizione difensiva P 50-70%" | "P stalling permanente 75% fino 2030+" | "Probabilità operatività perennial Y10 ~6-15%" | ✓ allineati su "Hold strutturale" |
| **Pricing PA realistico** | "€150k inventato" | "Cluster D €30-80k tipico" | n/a | "Recalibrato €60-90k base + €30-60k premium" | ✓ Cluster D ha forzato pivot |
| **Cooperative come vantaggio competitivo** | "boundary scudo" | "Solo se moat legale" | n/a | FO-ADD-01 formalizzata | ✓ allineati su "non vantaggio competitivo, vincolo strutturale" |
| **Capital intensity 6B realistic** | "Hold ammissibile €5.5-13.5M" | "AALTO scale incompatibile" | n/a | DR-014: $50M-1B benchmark | ✓ allineati su "€5.5-13.5M = Phase 0/A only" |
| **Cap. 10 verdetto** | "Go Cond = postura" | "Approva con caveat" | "Hold con piano rafforzato" | "HOLD scenario base + 5-15% Go pieno" | ✓ tutti convergono su Hold con piano |

**VERDETTO COERENZA: 9.5/10**. I 4 audit sono **strutturalmente coerenti**. Nessun audit contraddice gli altri sui temi chiave. Il Cap. 10 §10.0bis ha integrato esplicitamente i finding dei 4 audit.

### 6.3 Gap Red Team

1. **Cap. 0 (Sintesi Esecutiva) non è Red Team-auditato esplicitamente**. AUDIT-REDTEAM §2.0 fornisce critiche puntuali (Critica 2.0.3, 2.0.4, 2.0.6) ma **non integrate nel Cap. 0 stesso**. ⚠️ FIX OBBLIGATORIO: aggiungere §0.13 "Red Team check executive" come response.

2. **Pattern "Red Team theater" residuo**: l'AUDIT-REDTEAM Critica G-08 ("Tutte le risposte concludono in difesa del verdetto") è **risolta solo per Cap. 10** post-audit M+3. Cap. 7 §7.13, Cap. 6 §6.8, Cap. 8 §8.10, Cap. 4 §4.8 hanno tutte risposte che difendono il verdetto. Necessario un audit **"quale critica ha modificato il verdetto?"** per evitare il pattern teatrale.

3. **Cap. 0 + Cap. 10 mancano "kill criteria"** formali (Red Team Critica G-04). Quando un verdetto "Hold" diventa "No-Go"? Quante Hold consecutive? ⚠️ FIX RACCOMANDATO.

### 6.4 Verdetto Red Team coverage

**COVERAGE: 9.5/10**. Tutti i capitoli 1-11 hanno Red Team. **Cap. 0 manca**. Coerenza tra 4 audit avversariali eccezionale.

---

## 7. Investment-grade readiness per audience

### 7.1 Score per audience target

| Audience | Investment-grade score | Blocking issues | Ready oggi? |
|---|:---:|---|:---:|
| **Coopfond / Legacoop** | **8.5/10** | Mancano LoI Regione + workshop cooperative; format già coerente con bando | ✓ con caveat |
| **Regione Liguria + Protezione Civile** | **8/10** | LoI mancante + pre-app ENAC mancante + DPIA non depositata + cambio governo Bucci 2024 | ✓ con caveat ma non per delibera politica |
| **PNRR Aerospazio / MIMIT** | **6.5/10** | Cap. 5 §5.16 in addendum non in pillar; Quadro Economico art.41 OK; PNRR ha richieste specifiche che richiedono iterazione | ⚠️ partially ready |
| **EDF / Horizon Europe / DG DEFIS** | **5/10** | EuroHAPS Phase 2 non calendarizzata (DR-008 chiuso con confidence very-low); CIRA LoI mancante; Position paper "Italian Stratospheric Sovereignty" non pubblicato | ✗ NOT READY |
| **Investor seed (Coopfond-Invest, angel, family office)** | **6/10** | Modello finanziario executable ma scenario base recalibrato post-Cluster D non riflesso in Cap. 0; P(Go pieno) 5-15% dichiarato apertamente non aiuta seed-pitch | ⚠️ |
| **Investor Series A VC top-tier** | **3.5/10** | DCF 5y non 10y; Monte Carlo mancante; competitive moat dichiarato non difendibile vs Cluster D; "EU sovereign" frame per VC = "complicated"; Series A pipeline non visibile | ✗ NOT READY |
| **Banca / debito strutturato (CDP, EIB, BPS)** | **5/10** | Garanzie reali mancanti per asset hardware piccoli; bridge financing €500k previsto ma non strutturato; piano cash flow stress-tested manca | ✗ NOT READY senza Series A |

### 7.2 Document executability check

| Asset | Disponibilità | Executable? | Investment-grade? |
|---|---|---|---|
| **Modello finanziario Excel** | HALE-Financial-Model-M3.xlsx (22.7 KB, 10 sheet, 161 formule) | ✓ sì (formule attive su CapEx, OpEx, Revenue, Cash Flow, NPV/IRR, Quadro Economico) | ⚠️ Sensitivity + Scenarios + Cover sono **statici (0 formule)**, per VC top-tier non basta |
| **Build script Python** | build_financial_model.py (42 KB) | ✓ riproducibile | ✓ raro/positivo per audit |
| **RTM** | RTM-v1.0.xlsx (67 KB, 14 sheet) | ✓ 28 StNeed + 65 SyR + 81 SsR + 22 IR + 15 NegR + 68 VR, coverage 100% | ✓ NASA SE compliant |
| **Risk Register** | RISK-REGISTER-v1.0.xlsx (98 KB, 116 rischi, top-25 narrato) | ✓ owner + deadline + mitigation + EWI + falsifying observation | ✓ ISO 31000 compliant |
| **Computo Metrico** | A9-Computo-Metrico-Estimativo.md | ⚠️ md only, no xlsx | ✓ contenuto OK, format placeholder |
| **PSC SORA preliminare** | A11-PSC-SORA-Safety-Case-Preliminary.md | ⚠️ md only, no compilato formale ENAC | ⚠️ format placeholder |
| **VIA preliminare** | A12-Relazione-VIA-Preliminare.md | ⚠️ md only | ⚠️ placeholder |
| **Vendor RFQ JOUAV** | VENDOR-QUOTATION-ANALYSIS-JOUAV-TEKEVER.md | ⚠️ analisi non quotation firmata | ⚠️ DR-016 aperto |

### 7.3 Cronoprogramma doppio (nominal + sliding realistic)

**§9.1-9.5 nominale + §9.12 sliding timeline**: ✓ presente e ben strutturato. **Per investment-grade**: il Cap. 0 sintesi esecutiva NON richiama la sliding timeline. ⚠️ FIX raccomandato.

### 7.4 Risk Register actionable

**A2-RISK-REGISTER-REPORT.md**: 116 rischi, top-25 narrato con **owner + status + response + mitigation + residual P×I + fase critica + confidence + EWI + falsifying observation** per ognuno. ✓ ECCEZIONALE per documento M+3 early-stage. **Effective mitigation reduction**: RED 17→2 (-88%), YELLOW 66→19 (-71%). ✓ ISO 31000 compliant.

### 7.5 Verdetto investment-grade readiness

**SCORE PESATO PER AUDIENCE**:
- Coopfond + Regione + Cooperative: **READY 8/10** (audience naturale del documento, premia onestà metodologica)
- PNRR + MIMIT: **PARTIAL 6.5/10** (richiede iterazione formale + fix Cap. 5)
- EDF / Horizon: **NOT READY 5/10** (richiede engagement esterno DG DEFIS + CIRA LoI)
- VC Series A: **NOT READY 3.5/10** (richiede DCF 10y + Monte Carlo + Series A pipeline + simplified narrative)

---

## 8. Pivot 6B + B2-relaxed propagation

### 8.1 Pivot 6B "Firmamento operatore servizi su prime contractor" (post DR-014)

| Capitolo | Pivot 6B propagato? | Citation DR-014? |
|---|:---:|:---:|
| Cap. 0 Sintesi Esecutiva | ⚠️ **NON propagato**: la sintesi parla ancora di "Phase B €5.5-11M R&D" senza menzionare il pivot prime contractor | ⚠️ no |
| Cap. 6 §6.0.1 | ✓ "valido solo se modello R&D include partnership prime contractor o consortium EU bid come elemento strutturale" | ✓ |
| Cap. 8 §8.3.3 | ✓ caveat CRITICO post-DR-014 dettagliato (€50M-1B benchmark) | ✓ |
| Cap. 8 §0.0.3 | ⚠️ tabella scenario "EU sovereign full scale" non riflette pivot | ⚠️ no |
| Cap. 10 §10.0bis.2 | ✓ "Pivot raccomandato per 6B" esplicitato | ✓ |
| Cap. 11 §11.6bis | ✓ scenario B2-relaxed integra "Firmamento operatore VTOL/MALE" come fallback | ✓ |
| Risk Register RSK-TEC-001 | ✓ E5 "Seasonal-only" mandatory, prime contractor mitigation citato | ✓ |

**GAP CRITICO**: Cap. 0 Sintesi Esecutiva **NON propaga il pivot 6B**. Per audience VC/EDF/MIMIT che leggono prima la sintesi, il primo messaggio è ancora "HALE proprietario Firmamento €5.5-11M" senza pivot. ⚠️ **FIX OBBLIGATORIO**.

### 8.2 B2-relaxed scenario presente in Cap. 11?

**§11.6bis "Standalone IT Operator Small Fleet"**: ✓ ECCEZIONALMENTE INTEGRATO:
- Trigger §11.6bis.2: 6 TRG-B2R-01..06 (3 Critical + 3 High)
- Caratteristiche operative §11.6bis.3: ARR €30-80M, flotta 10-20 VTOL/MALE + 3-5 HAPS seasonal
- KPI Y10 §11.6bis.4: 6 KPI quantitativi
- Confronto B2 full vs B2-relaxed §11.6bis.5: tabella esaustiva
- Probabilità: 30-50% B2-relaxed vs 6-15% B2 full
- FO-F11-07 e FO-F11-08 nuove + integrazione con AUDIT-QUALITY-VOLUME-1.md §2 raccomandazione

**Coerenza con Cap. 7 + Cap. 8**: §11.6bis.7 azione 1: "il modello finanziario deve includere scenario B2-relaxed come caso base operativo Y6-Y10 (ARR €30-80M, EBITDA 20-35%, capital intensity €500M-1.5B), non come 'fallback negativo'". **GAP**: Cap. 8 non aggiornato ancora. ⚠️ FIX RACCOMANDATO M+9.

### 8.3 HOLD CON PIANO RAFFORZATO come scenario base in Cap. 10?

**§10.0bis "Revisione Verdetto post-Audit M+3"**: ✓ INTEGRATO COME SCENARIO BASE:
- Tabella §10.0bis.1: 4 scenari A/B/C/D con probabilità (5-15% / 45-60% / 20-30% / 5-10%)
- **Scenario base = HOLD CON PIANO REGOLATORIO RAFFORZATO** (Scenario B, 45-60%)
- Caveat probabilistico esplicito §10.3.2: "P(Go pieno) 15-35% non 60-80%"
- §10.0bis.5 action immediato CdA: bridge financing €500k + double-track planning + Re-baseline Gate G3-bis a M+13-16

**GAP MINORE**: §10.1 "Sintesi del verdetto" rimane "Go Condizionato" come prima dichiarazione, con nota M+3 che rinvia a §10.0bis. ⚠️ Per chiarezza pre-CdA, ribaltare l'ordine: §10.0bis (HOLD scenario base) **prima** di §10.1 (Go Condizionato scenario A). Minor fix.

### 8.4 Verdetto pivot 6B + B2-relaxed propagation

**PROPAGAZIONE: 9/10**. Cap. 6, 8, 10, 11 + Risk Register hanno integrato i pivot. **Cap. 0 + Cap. 8 §0.0.3 + Cap. 7 §7.12.2.667 mancano ancora propagazione completa**. Cap. 8 modello finanziario non aggiornato a "scenario B2-relaxed come caso base Y6-Y10". ⚠️ 3 FIX (1 obbligatorio Cap. 0).

---

## 9. Action items prioritari

Lista numerata per portare il documento da "quasi-investment-grade" a "investment-grade":

### Priorità 1. Bloccanti per audience institutional (Coopfond + Regione + PNRR)

1. **Riscrittura Cap. 0 (Sintesi Esecutiva)**: 4-6 ore
   - Aggiungere confidence per ogni numero in §0.11 (NPV, IRR, ARR, capital intensity)
   - Aggiungere §0.13 "Red Team check executive" con 3-5 critiche aggregate dei 4 audit
   - Aggiungere §0.14 "Pre-mortem aggregato top 5+1 driver di fallimento"
   - Propagare pivot 6B "operatore servizi su prime contractor" in §0.3
   - Richiamare sliding timeline §9.12 in §0.10 cronoprogramma
   - Aggiungere disclaimer epistemico finale (come Cap. 11.13 closing)

2. **Cap. 10, Top-5 Falsifying Observations del verdetto**: 1-2 ore
   - Attualmente 0 FO esplicite (gap critico R1)
   - Aggiungere §10.10bis "FO del verdetto Cap. 10": almeno 5 FO operative + datate
   - Es. "Se al M+6 mix funding committed < 25%, attivazione Hold automatico"
   - Es. "Se al M+9 nessun contratto Regione firmato, Scenario D PIVOT STRATEGICO attivato"

3. **Cap. 5 §5.16, promozione da addendum a pillar**: 2-3 ore
   - 15 showstopper regolatori aggiuntivi sono in §5.16 ma non integrati nel discorso generale del capitolo
   - Per investment-grade PNRR/EDF serve riscrittura Cap. 5 con i 15 showstopper come **categoria 4° del framework** (oltre a EASA/ENAC/AGCOM/Garante)

### Priorità 2. Bloccanti per VC / EDF / Horizon

4. **Modello finanziario Excel, completamento Sensitivity + Scenarios + Monte Carlo**: 8-12 ore
   - Sensitivity sheet attualmente statico (0 formule), necessario tabulato data-table
   - Scenarios sheet statico, formule che leggono da Assumptions
   - Monte Carlo: aggiungere foglio dedicato (5000 iterazioni) su 7 driver primari
   - DCF estesa Y6-Y10 (attualmente solo Y1-Y5 tabulato + estrapolazione testuale Y6-Y10)

5. **Cap. 7 + Cap. 8, recepimento Cluster D recalibrazione pricing**: 3-4 ore
   - Cap. 7 §7.8.2 originale (€150k base) **non riscritto** post-audit Cluster D; il valore è declassato solo nel financial model README + nel Red Team risposta §7.13.6
   - Cap. 8 §8.6.1 cash flow Y1 €380k revenue non recalibrato a €220-260k post-Cluster D
   - **INCONSISTENZA NUMERICA** tra Cap. 7 / Cap. 8 / financial model README

6. **Position paper "Italian Stratospheric Sovereignty"**: 6-8 ore (esterno allo Studio)
   - Pre-condizione per credibilità DG DEFIS / DG CNECT
   - Cap. 11 §11.10.1 azione 2 obbligatoria entro M+12
   - Senza, narrazione "complementare IRIS²" è auto-narrativa (Critica 2.0.6 Red Team)

### Priorità 3. Raccomandate (non bloccanti ma alta utilità)

7. **TOP-50 FO consolidate in singolo documento**: 2-3 ore
   - Distribuire 145 FO nel Volume 1 + 10 FO ADD = ~155 FO totali
   - Per investment-grade serve **Master FO Table** consolidato per gate review
   - Format: FO-ID | Capitolo | Claim | Trigger | Milestone | Confidence | Action | Owner

8. **Cap. 8, base rate aerospace cost overrun applicata**: 1-2 ore
   - Contingency 15% sotto base rate 30-150%; aggiornare CapEx scenario realistico Y1 €1.3-3.0M (vs €0.97-1.96M nominale)
   - Aggiungere riga "Scenario realistico aerospace base rate" nelle tabelle §8.3.1 + §8.6.2

9. **Cap. 11 §11.6bis.7, Cap. 7 + Cap. 8 aggiornati a B2-relaxed come caso base Y6-Y10**: 4-6 ore
   - Cap. 8 modello finanziario M+9 deve avere scenario B2-relaxed (ARR €30-80M Y8) come caso base operativo
   - Cap. 7 pricing target PA €100-200k/anno regione coerente con scala B2-relaxed (non scala B2 full)

10. **Cap. 0 + Cap. 10, kill criteria escalation matrix**: 1-2 ore
    - "Quanti Hold consecutivi prima del No-Go automatico" non dichiarato
    - Es. "3 Hold consecutivi su LoI Regione (M+13 / M+16 / M+20) = No-Go scale-up Liguria + pivot Piemonte"

11. **Rimozione 2 minor "alternativa Starlink"** non-negative (Cap. 7 + Cap. 8): 15 min
    - Cap. 8 §0.0.3: parentetica "(alternativa Starlink EU)" → rimuovere o sostituire con "EU sovereign full scale"
    - Cap. 7 §7.12.2.667: "Per scala 'alternativa Starlink EU'" → "Per scala EU sovereign full scale"

### Effort totale stimato per portare a investment-grade per VC/EDF: **30-45 ore di scrittura focused**.

---

## 10. Verdetto consolidato

### 10.1 Quale audience può ricevere il documento OGGI (M+3)?

| Audience | Verdetto oggi | Condizioni per migliorare |
|---|:---:|---|
| **Coopfond / Legacoop** | ✅ **GO** con caveat onesti | Workshop 10 coop M+6 + LoI Coopfond Cooding 2026 |
| **Regione Liguria, istruttoria tecnica** | ✅ **GO** con caveat | Pre-app ENAC + LoI bilaterale + DPIA preliminare M+6 |
| **Regione Liguria, DGR politica** | ⚠️ **NOT YET** | Necessaria evidenza esterna (LoI ENAC + 5 coop firmate + workshop Pentema) |
| **Protezione Civile / ARPA Liguria** | ✅ **GO** con caveat | Convenzione operativa M+6 |
| **Comunità Pentema (14 abitanti)** | ⚠️ **NOT YET** | Workshop pubblico + DPIA pubblica + delibera comunale |
| **PNRR Aerospazio / MIMIT** | ⚠️ **PARTIALLY READY** | Cap. 5 riscritto + position paper sovranità + Cap. 8 PNRR target tracking |
| **EDF / Horizon Europe / DG DEFIS** | ❌ **NOT READY** | CIRA LoI + position paper + engagement EASA Innovation Network + 6-12 mesi engagement |
| **Investor seed (Coopfond-Invest)** | ⚠️ **READY con caveat** | Recalibrazione Cap. 7 pricing + DCF aggiornato + mix funding M+10 |
| **Investor Series A VC top-tier** | ❌ **NOT READY** | DCF 10y + Monte Carlo + competitive moat legalmente vincolante + Series A pipeline visibile + simplified pitch |
| **Banca / EIB / CDP debt** | ❌ **NOT READY** | Series A chiusa + revenue Y1 reale + asset-backed structure |

### 10.2 Confronto onesto con il claim "investment-grade"

| Dimensione | Score | Note |
|---|:---:|---|
| **Rigore metodologico** (NASA SE + art.41) | **9/10** | Eccezionale. Tutti i deliverable PFTE coperti. RTM v1.0 con 0 orphan + 0 untestable. Risk Register ISO 31000 compliant. |
| **Onestà epistemica** (7 regole epistemic-rigor) | **8.5/10** | Eccezionale per Cap. 1, 3, 7, 11. Lacuna in Cap. 0 + 10 (confidence + FO). |
| **Coerenza interna** (boundary B1/B2 + linguaggio) | **9.5/10** | B1+B2 preservate 11/11 capitoli. 2 fix minori linguistici. |
| **Coerenza inter-capitolo** (numeri allineati) | **6.5/10** | **GAP CRITICO**: Cap. 7 pricing originale (€150k) vs Cap. 8 revenue baseline (€380k) vs financial model README (€260k) NON allineati post-recalibrazione Cluster D. |
| **Audit avversariali integrati** | **9/10** | 4 audit + AUDIT-QUALITY-VOLUME-1.md + FALSIFYING-OBSERVATIONS-M3-ADDENDUM. Pattern "Red Team theater" corretto Cap. 10. |
| **Allegati Volume 2 maturità** | **7.5/10** | A1 RTM + A2 Risk Register + A7 Link Budget + Energy Balance maturi. A9 Computo Metrico + A10 Piano Manutenzione + A11 PSC SORA + A12 VIA = placeholder. |
| **Modello finanziario executable** | **6/10** | 161 formule funzionanti. Sensitivity + Scenarios + Monte Carlo statici. DCF solo Y1-Y5 tabulato. |
| **Evidenze esterne raccolte** (LoI, contratti, pre-app ENAC) | **2/10** | **GAP STRUTTURALE M+3**: 0 LoI firmate, 0 contratti, 0 pre-app ENAC formalmente documentata. DR-001..DR-005 aperti. |

**Verdetto pesato investment-grade**:
- **Per onestà metodologica**: **9/10** (raro per aerospace early-stage IT)
- **Per evidence base operativa**: **3/10** (debito di rigore residuo non chiuso)
- **Per coerenza inter-capitolo post-recalibrazioni**: **6.5/10** (gap Cap. 7-8-financial model)
- **Score complessivo investment-grade audience Coopfond/Regione/PA**: **7.5/10** ✓
- **Score complessivo investment-grade audience VC/EDF**: **4.5/10** ✗

### 10.3 Sintesi brutalmente onesta

Il documento è **strutturalmente più rigoroso del 90% degli Studi di Fattibilità aerospace italiani early-stage** (giudizio del Red Team audit confermato). Ha **4 audit avversariali integrati** con response e action items, scenario B2-relaxed esplicitato, base rate 0% HALE solari dichiarata, sliding timeline §9.12, caveat post-DR-014, NegR-Mkt-001 binding sul linguaggio pubblico. Questa onestà metodologica è **leva di credibilità verso audience sofisticate** (RINA review, DG DEFIS, EIB DCF specialist).

Ma:
- Per **audience VC top-tier "pitch deck classico"** il pattern di onestà brutale è **debolezza percepita**: P(Go pieno) 5-15% dichiarato apertamente non vende.
- Per **audience EDF / DG DEFIS** mancano evidenze esterne (CIRA LoI, position paper, EuroHAPS Phase 2 calendarizzato).
- Per **audience PNRR / MIMIT** Cap. 5 §5.16 in addendum invece che pillar è gap visibile.
- Per **Comunità Pentema** (14 abitanti) il documento è strumento di lavoro tecnico, non di accettabilità sociale: manca workshop pubblico + DPIA pubblica.

**Conclusione operativa per il management Firmamento**:
- **Presentare oggi a**: Coopfond, Regione Liguria istruttoria tecnica, Protezione Civile, MIMIT in regime di engagement (non di formal application)
- **NON presentare oggi a**: VC Series A top-tier, EDF formal application, banche per debito strutturato, EuroHAPS consortium senza pre-engagement CIRA
- **Pre-G3 (M+10/M+11) priorità**: chiudere i **11 action items** §9 per portare il documento a "investment-grade" per audience VC + EDF + PNRR

### 10.4 Verdetto in una riga

> **Lo Studio di Fattibilità HALE/VTOL Firmamento Technologies è QUASI-INVESTMENT-GRADE per audience PA/cooperativa (M+3 GO con 11 fix prioritari) e NON-INVESTMENT-GRADE per audience VC/EDF nello stato attuale, con effort residuo stimato 30-45 ore di scrittura focused + 6-12 mesi di engagement esterno per arrivare a "investment-grade per tutte le audience" entro il gate G3 M+10/M+11.**

---

## 11. Note metodologiche dell'audit

**Coverage**: 22 file analizzati (12 capitoli Cap. 0-11 + 13 allegati MD + 5 R-bibliografia + 4 audit precedenti + AUDIT-QUALITY-VOLUME-1.md + FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md + DR-research-closure-M3.md + financial model + RTM + Risk Register Excel).

**Strumenti**: grep pattern matching su 8 disciplina (confidence, falsifying, IRIS², Starlink, service-only, OEM, visione, B2-relaxed) + audit di executability su Excel (161 formule verified) + analisi cross-coherence sui 4 audit avversariali precedenti.

**Limiti**:
- Lettura sample-based per capitoli > 800 righe (Cap. 2, 3, 7, 11)
- Verifica Excel formulas presence ma non logical correctness
- Nessun engagement esterno verificato (LoI Regione = claim del documento, non verificata)

**Disclaimer**: questo audit è uno **strumento di gate review interno**, non sostituisce una **due diligence formale** di RINA / DNV / revisore istituzionale. Per investment-grade Series A è raccomandato review indipendente di terza parte ai sensi di `riferimenti/analisi-fac-simili-IT.md` §5.

---

## 12. Riferimenti audit

- `AUDIT-REDTEAM-VOLUME-1.md` (417 righe): red-team-skeptic
- `AUDIT-COMPETITOR-VOLUME-1.md` (474 righe): competitor-intelligence
- `AUDIT-REGULATORY-VOLUME-1.md` (445 righe): regulatory-adversary
- `AUDIT-QUALITY-VOLUME-1.md` (295 righe): quality consolidation M+3
- `FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md` (226 righe): 10 FO ADD
- `riferimenti/DR-research-closure-M3.md`: 9/15 DR chiusi M+3
- `riferimenti/audit-rigore-epistemico.md`: debito di rigore baseline
- Presente file `AUDIT-QUALITY-INVESTMENT-GRADE.md`: **audit investment-grade M+3 consolidato**

---

*Audit Quality Investment-Grade. Firmamento Technologies. Studio di Fattibilità HALE/VTOL. M+3. 17 maggio 2026*
